# Fonts

Fonts in a PPT are rendered by the computer that opens it; a font that isn't installed gets substituted, so compatibility comes first when choosing fonts.

## Default Configuration

| Role | Chinese | Latin | Notes |
|---|---|---|---|
| heading | Microsoft YaHei | Arial | Bundled with Windows; also available in WPS |
| body | Microsoft YaHei | Arial | Same as above |
| display | Follows heading | Arial Black | Cover titles and large numbers; strongly geometric |

build_deck.py writes both the Latin font (latin) and the East Asian font (ea), and both PowerPoint and WPS select them automatically per character.

## Optional Substitutions

| Style | Chinese | Latin | Notes |
|---|---|---|---|
| Many Apple users | PingFang SC | Helvetica Neue | Falls back on Windows |
| Free for commercial use, more refined | Source Han Sans SC / Alibaba PuHuiTi / HarmonyOS Sans SC | Montserrat | Requires installation on the recipient's computer; remind them at delivery |
| Formal, literary | Source Han Serif SC | Georgia | Serif for headings, sans-serif still for body |

Among the presets, the black-gold report and blue-pink soft mist sets use exactly this serif heading set. The preview environment maps names like Source Han Serif, STZhongsong, and SimSun to Noto Serif CJK, so what you see in preview is the serif effect; if the recipient's computer doesn't have Source Han Serif, it falls back to a system font — remind them to install it at delivery, or change heading_ea to a serif font they already have.

## Differences Between Preview and Actual Output

The cloud environment doesn't have Microsoft YaHei, so LibreOffice preview substitutes Source Han Sans (Noto Sans CJK); Chinese character widths are basically the same, with slight differences in Latin text.
Layout font-size calculations and QA overflow checks are all measured against Source Han Sans, with about 3% of margin left.
Users have reported that a few text lines wrap differently on their own computers; this is usually a Latin font difference, and fine-tuning the font size on that page is enough.
