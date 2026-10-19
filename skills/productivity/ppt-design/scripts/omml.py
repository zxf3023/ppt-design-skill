"""Office Math (OMML) equations in slides -> plain Unicode text.

PowerPoint stores equations typed with the equation editor as <a14:m><m:oMath>…</m:oMath></a14:m>
inside a paragraph. python-pptx skips them and LibreOffice draws nothing, so a deck full of
formulas came out with holes ("用一块边长为  的正方形铁皮"). flatten_math() rewrites every
equation into an ordinary run whose text is a linear form of the formula, e.g.

  V(x) = x(a − 2x)²      f′(x₀)      x = a/6      lim[Δx→0]

The run keeps the font size and colour the equation had. Extraction, previews and the
fidelity check then all see the same text, and the beautified deck shows the formula as
editable text in any app.
"""
import re
import zipfile
from pathlib import Path

from lxml import etree

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "a14": "http://schemas.microsoft.com/office/drawing/2010/main",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
}
M = "{%s}" % NS["m"]
A = "{%s}" % NS["a"]

SUP = dict(zip("0123456789+-−=()niax", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿⁱᵃˣ"))
SUB = dict(zip("0123456789+-−=()aeoxhklmnpstijruv", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ"))
PRIMES = {"'": "′", "′": "′", "''": "″", "″": "″"}


def _val(el, path, default=None):
    """m:val attribute of a property element, e.g. dPr/begChr."""
    if el is None:
        return default
    node = el.find(path, NS)
    if node is None:
        return default
    return node.get(M + "val", default)


def _kids(el, tag):
    return [c for c in el if c.tag == M + tag]


def _one(el, tag):
    k = _kids(el, tag)
    return lin(k[0]) if k else ""


def _script(s, table, mark):
    s = s.strip()
    if not s:
        return ""
    if all(ch in table for ch in s):
        return "".join(table[ch] for ch in s)
    if len(s) == 1 or re.fullmatch(r"[一-鿿]+", s):
        return s  # CJK labels stay on the line
    return f"{mark}({s})"


def _wrap(s):
    """Parenthesise a compound operand: a+b -> (a+b), keep a, 2x, x₀."""
    return f"({s})" if re.search(r"[+\-−·/ ]", s) and not (s.startswith("(") and s.endswith(")")) else s


def lin(el):
    """Linear text of one OMML element (recursive)."""
    tag = el.tag[len(M):] if el.tag.startswith(M) else None
    if tag is None:
        return ""
    if tag == "r":
        return "".join(t.text or "" for t in el.iter(M + "t"))
    if tag == "t":
        return el.text or ""
    if tag in ("sSub",):
        return _one(el, "e") + _script(_one(el, "sub"), SUB, "_")
    if tag in ("sSup",):
        base, sup = _one(el, "e"), _one(el, "sup").strip()
        if sup in PRIMES:
            return base + PRIMES[sup]
        return base + _script(sup, SUP, "^")
    if tag == "sSubSup":
        base, sub, sup = _one(el, "e"), _one(el, "sub"), _one(el, "sup").strip()
        tail = PRIMES.get(sup) or _script(sup, SUP, "^")
        return base + _script(sub, SUB, "_") + tail
    if tag == "sPre":
        return _script(_one(el, "sub"), SUB, "_") + _script(_one(el, "sup"), SUP, "^") + _one(el, "e")
    if tag == "d":
        pr = el.find("m:dPr", NS)
        beg = _val(pr, "m:begChr", "(")
        end = _val(pr, "m:endChr", ")")
        sep = _val(pr, "m:sepChr", "|")
        sep = ", " if sep == "," else sep
        return (beg or "") + sep.join(lin(e) for e in _kids(el, "e")) + (end or "")
    if tag == "f":
        num, den = _one(el, "num").strip(), _one(el, "den").strip()
        kind = _val(el.find("m:fPr", NS), "m:type", "bar")
        if kind == "noBar":
            return f"({num} {den})"
        return f"{_wrap(num)}/{_wrap(den)}"
    if tag == "rad":
        deg, body = _one(el, "deg").strip(), _one(el, "e")
        root = {"2": "√", "3": "∛", "4": "∜", "": "√"}.get(deg, _script(deg, SUP, "^") + "√")
        return root + _wrap(body)
    if tag == "nary":
        pr = el.find("m:naryPr", NS)
        op = _val(pr, "m:chr", "∫")
        sub, sup = _one(el, "sub").strip(), _one(el, "sup").strip()
        lims = (f"[{sub}]" if sub else "") + (f"^{sup}" if sup else "")
        return f"{op}{lims} {_one(el, 'e')}".rstrip()
    if tag == "func":
        name, body = _one(el, "fName"), _one(el, "e")
        return name + ("" if body.startswith("(") else " ") + body
    if tag == "limLow":
        return f"{_one(el, 'e')}[{_one(el, 'lim')}]"
    if tag == "limUpp":
        return f"{_one(el, 'e')}^({_one(el, 'lim')})"
    if tag == "acc":
        ch = _val(el.find("m:accPr", NS), "m:chr", "̂")
        return _one(el, "e") + ch
    if tag == "bar":
        return _one(el, "e") + "̅"
    if tag == "groupChr":
        return _one(el, "e")
    if tag == "eqArr":
        return "；".join(lin(e) for e in _kids(el, "e"))
    if tag == "m":  # matrix
        rows = [" ".join(lin(e) for e in _kids(r, "e")) for r in _kids(el, "mr")]
        return "[" + "; ".join(rows) + "]"
    if tag in ("oMathPara",):
        return "\n".join(lin(c) for c in _kids(el, "oMath"))
    if tag.endswith("Pr") or tag in ("ctrlPr",):
        return ""
    return "".join(lin(c) for c in el)


def tidy(s):
    """Typeset the linear text a little: real minus, primes, spaces around = and arrows."""
    s = s.replace("-", "−").replace("'", "′")
    s = re.sub(r"\s*(=|≠|≈|≤|≥|→|<|>)\s*", r" \1 ", s)
    s = re.sub(r"\[\s*(.*?)\s*\]", lambda m: "[" + m.group(1).replace(" → ", "→") + "]", s)
    return re.sub(r" {2,}", " ", s).strip()


def equation_text(m_el):
    """Text for one <a14:m> element (holds m:oMath or m:oMathPara)."""
    parts = [lin(c) for c in m_el]
    return tidy("".join(parts))


def _run_for(m_el, text):
    """An <a:r> that stands in for the equation, keeping its size and colour."""
    r = etree.Element(A + "r")
    rpr = m_el.find(".//m:r/a:rPr", NS)
    if rpr is not None:
        new = etree.fromstring(etree.tostring(rpr))
        new.attrib.pop("i", None)
        r.append(new)
    else:
        etree.SubElement(r, A + "rPr", lang="en-US")
    t = etree.SubElement(r, A + "t")
    t.text = text
    return r


def flatten_slide_xml(data):
    """Rewrite one slide's XML. Returns (bytes, list of equation texts)."""
    root = etree.fromstring(data)
    found = []
    for m_el in list(root.iter("{%s}m" % NS["a14"])):
        text = equation_text(m_el)
        if not text:
            continue
        target = m_el
        # equation behind a compatibility switch: replace the whole switch (fallback is a picture)
        anc = m_el.getparent()
        while anc is not None and anc.tag != "{%s}AlternateContent" % NS["mc"] and anc.tag != A + "p":
            anc = anc.getparent()
        if anc is not None and anc.tag == "{%s}AlternateContent" % NS["mc"]:
            target = anc
        parent = target.getparent()
        if parent is None:
            continue
        parent.replace(target, _run_for(m_el, text))
        found.append(text)
    if not found:
        return data, []
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True), found


def flatten_math(pptx_path):
    """Rewrite every slide of a pptx in place. Returns {slide_number: [equation texts]}."""
    pptx_path = Path(pptx_path)
    out, report = {}, {}
    with zipfile.ZipFile(pptx_path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    changed = False
    for info, data in items:
        mt = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", info.filename)
        if mt and (b"a14:m" in data or b"oMath" in data):
            new, found = flatten_slide_xml(data)
            if found:
                report[int(mt.group(1))] = found
                data, changed = new, True
        out[info.filename] = (info, data)
    if changed:
        tmp = pptx_path.with_suffix(".tmp")
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
            for name, (info, data) in out.items():
                z.writestr(info, data)
        tmp.replace(pptx_path)
    return report
