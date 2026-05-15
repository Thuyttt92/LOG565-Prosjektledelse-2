"""Felles PDF-hjelpefunksjoner for alle build_*.py-script.

VIKTIG (etter 05.05.2026):
- make_table() wrapper alle celler i Paragraph for å unngå tekst-overlap.
- Bruk denne i stedet for å bygge Table direkte.
"""
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import Paragraph, Table, TableStyle

_styles = getSampleStyleSheet()
BLUE = colors.HexColor("#1F4E79")

CELL_STYLE = ParagraphStyle(
    "Cell", parent=_styles["BodyText"],
    fontSize=9.5, leading=12, alignment=TA_LEFT,
    textColor=colors.black, spaceAfter=0, spaceBefore=0,
)
HEADER_CELL_STYLE = ParagraphStyle(
    "HCell", parent=_styles["BodyText"],
    fontSize=9.5, leading=12, alignment=TA_LEFT,
    textColor=colors.white, fontName="Helvetica-Bold",
    spaceAfter=0, spaceBefore=0,
)


def to_para(cell, header=False):
    """Konverter celleverdi til Paragraph for proper wrapping."""
    if isinstance(cell, Paragraph):
        return cell
    s = str(cell) if cell is not None else ""
    style = HEADER_CELL_STYLE if header else CELL_STYLE
    return Paragraph(s, style)


def make_table(data, header=True, col_widths=None, header_color=None):
    """Bygg tabell hvor alle celler wrappes i Paragraph.

    - Forhindrer tekst-overlap når celleinnhold er lengre enn kolonnebredde.
    - Header-rad får automatisk blå bakgrunn med hvit fet skrift.
    - Alternerende radfarger: hvit / grå.
    """
    wrapped = []
    for ri, row in enumerate(data):
        is_hdr = header and ri == 0
        wrapped.append([to_para(c, header=is_hdr) for c in row])

    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BFBFBF")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1),
         [colors.white, colors.HexColor("#F2F2F2")]),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), header_color or BLUE))
    t = Table(wrapped, colWidths=col_widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle(style))
    return t
