# -*- coding: utf-8 -*-
"""Felles, polert stilmal for PROSJEKTSTATUS-PDF.

Konsulent-aktig estetikk:
- Hero-tittel med farget bånd
- Innholdskort øverst med prosjektrammer
- Nummererte seksjons-headere med fargechip
- Statusbadges (OK / Gjenstår / Avvik) som fargede piller
- Mykere tabeller med tynne grå linjer og lav-kontrast alternering
- Footer med sidenummer og prosjektnavn på hver side

Brukes av build_prosjektstatus_*.py.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether,
)

# ============================================================
# FARGEPALETT
# ============================================================
NAVY = colors.HexColor("#0F2A47")       # Deep brand color
PRIMARY = colors.HexColor("#1F4E79")    # Primary blue
ACCENT = colors.HexColor("#4472C4")     # Medium blue
SOFT_BG = colors.HexColor("#F4F7FB")    # Very light blue card bg
SOFT_BG_2 = colors.HexColor("#FAFBFD")  # Even lighter for row alt

SUCCESS = colors.HexColor("#548235")
SUCCESS_BG = colors.HexColor("#E8F1DC")
WARN = colors.HexColor("#BF8F00")
WARN_BG = colors.HexColor("#FFF4D9")
DANGER = colors.HexColor("#C00000")
DANGER_BG = colors.HexColor("#FDE7E7")
INFO = colors.HexColor("#2E75B6")
INFO_BG = colors.HexColor("#E1ECF7")

TEXT = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#6B7280")
BORDER = colors.HexColor("#D9DEE5")
THIN = colors.HexColor("#EDF0F4")

# ============================================================
# TYPOGRAFI
# ============================================================
_styles = getSampleStyleSheet()

ST_HERO_TITLE = ParagraphStyle(
    "HeroTitle", parent=_styles["Heading1"],
    fontName="Helvetica-Bold", fontSize=30, leading=34,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=2)

ST_HERO_SUB = ParagraphStyle(
    "HeroSub", parent=_styles["BodyText"],
    fontName="Helvetica", fontSize=11.5, leading=15,
    textColor=MUTED, alignment=TA_LEFT, spaceAfter=2)

ST_HERO_DATE = ParagraphStyle(
    "HeroDate", parent=_styles["BodyText"],
    fontName="Helvetica-Bold", fontSize=11, leading=14,
    textColor=PRIMARY, alignment=TA_LEFT, spaceAfter=6)

ST_SECTION = ParagraphStyle(
    "Section", parent=_styles["Heading2"],
    fontName="Helvetica-Bold", fontSize=15, leading=19,
    textColor=PRIMARY, alignment=TA_LEFT,
    spaceBefore=14, spaceAfter=2, leftIndent=0)

ST_H3 = ParagraphStyle(
    "H3", parent=_styles["Heading3"],
    fontName="Helvetica-Bold", fontSize=11.5, leading=15,
    textColor=NAVY, alignment=TA_LEFT,
    spaceBefore=10, spaceAfter=4)

ST_BODY = ParagraphStyle(
    "Body", parent=_styles["BodyText"],
    fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=7)

ST_LEAD = ParagraphStyle(
    "Lead", parent=_styles["BodyText"],
    fontName="Helvetica", fontSize=11.5, leading=16,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=10)

ST_MUTED = ParagraphStyle(
    "Muted", parent=_styles["BodyText"],
    fontName="Helvetica-Oblique", fontSize=9.5, leading=12.5,
    textColor=MUTED, alignment=TA_LEFT, spaceAfter=6)

ST_BULLET = ParagraphStyle(
    "Bullet", parent=_styles["BodyText"],
    fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=3,
    leftIndent=14, bulletIndent=2)

# Cell styles
ST_CELL = ParagraphStyle(
    "Cell", parent=_styles["BodyText"],
    fontName="Helvetica", fontSize=9.5, leading=13,
    textColor=TEXT, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=0)

ST_CELL_BOLD = ParagraphStyle(
    "CellB", parent=ST_CELL,
    fontName="Helvetica-Bold", textColor=NAVY)

ST_HEADER_CELL = ParagraphStyle(
    "HCell", parent=_styles["BodyText"],
    fontName="Helvetica-Bold", fontSize=9.5, leading=13,
    textColor=colors.white, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=0)

# Callout styles
ST_INFO = ParagraphStyle(
    "Info", parent=ST_BODY,
    fontSize=10, leading=14, textColor=NAVY,
    backColor=INFO_BG, borderColor=INFO, borderWidth=0,
    borderPadding=(8, 10, 8, 12),
    leftIndent=0, rightIndent=0,
    spaceBefore=8, spaceAfter=8)

ST_NOTE = ParagraphStyle(
    "Note", parent=ST_BODY,
    fontSize=9.5, leading=13, textColor=MUTED,
    fontName="Helvetica-Oblique",
    backColor=SOFT_BG, borderColor=BORDER, borderWidth=0,
    borderPadding=(8, 10, 8, 12),
    leftIndent=0, rightIndent=0,
    spaceBefore=6, spaceAfter=6)

ST_HIGHLIGHT = ParagraphStyle(
    "Highlight", parent=ST_BODY,
    fontSize=10.5, leading=14, textColor=colors.HexColor("#7F6000"),
    fontName="Helvetica-Bold",
    backColor=WARN_BG, borderColor=WARN, borderWidth=0,
    borderPadding=(10, 12, 10, 14),
    leftIndent=0, rightIndent=0,
    spaceBefore=8, spaceAfter=4)


# ============================================================
# KOMPONENTER
# ============================================================
def _to_cell(content, bold=False):
    if isinstance(content, Paragraph):
        return content
    s = str(content) if content is not None else ""
    return Paragraph(s, ST_CELL_BOLD if bold else ST_CELL)


def _to_header_cell(content):
    if isinstance(content, Paragraph):
        return content
    s = str(content) if content is not None else ""
    return Paragraph(s, ST_HEADER_CELL)


def status_badge(text, kind="ok"):
    """Lager en fargekodet pille for statuskolonner.

    kind: 'ok' (grønn), 'pending' (gul), 'warn' (rød), 'info' (blå), 'neutral' (grå)
    """
    palette = {
        "ok": (SUCCESS, SUCCESS_BG),
        "pending": (WARN, WARN_BG),
        "warn": (DANGER, DANGER_BG),
        "info": (INFO, INFO_BG),
        "neutral": (MUTED, THIN),
    }
    fg, bg = palette.get(kind, palette["neutral"])
    st = ParagraphStyle(
        f"Badge_{kind}", parent=ST_CELL,
        fontName="Helvetica-Bold", fontSize=8.5, leading=11,
        textColor=fg, alignment=TA_CENTER,
        backColor=bg,
        borderPadding=(3, 5, 3, 5),
        spaceBefore=0, spaceAfter=0,
    )
    return Paragraph(text, st)


def make_table(data, header=True, col_widths=None, badge_col=None):
    """Stilren tabell.

    - Header-rad i mørk navy med hvit fet tekst
    - Veldig myke alternerende rader (hvit / svært lys blå)
    - Tynne lysegrå linjer
    - Generøs padding

    badge_col: indeks på kolonne som inneholder status_badge() Paragraph-er
               (de wrappes ikke om — beholder sin egen styling)
    """
    wrapped = []
    for ri, row in enumerate(data):
        is_hdr = header and ri == 0
        new_row = []
        for ci, cell in enumerate(row):
            if is_hdr:
                new_row.append(_to_header_cell(cell))
            elif badge_col is not None and ci == badge_col and isinstance(cell, Paragraph):
                new_row.append(cell)  # Allerede en badge
            else:
                new_row.append(_to_cell(cell))
        wrapped.append(new_row)

    style = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1),
         [colors.white, SOFT_BG_2]),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
        style.append(("TOPPADDING", (0, 0), (-1, 0), 9))
        style.append(("BOTTOMPADDING", (0, 0), (-1, 0), 9))
        style.append(("LINEBELOW", (0, 0), (-1, 0), 0, NAVY))
    if badge_col is not None:
        style.append(("ALIGN", (badge_col, 1 if header else 0), (badge_col, -1), "CENTER"))

    t = Table(wrapped, colWidths=col_widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle(style))
    return t


def info_card(rows, col_widths=None):
    """Et 'kort' med prosjektrammer øverst — to kolonner, ingen header."""
    if col_widths is None:
        col_widths = [4.8 * cm, 11.7 * cm]
    wrapped = []
    for label, value in rows:
        lbl_st = ParagraphStyle("CardLbl", parent=ST_CELL,
                                fontName="Helvetica", textColor=MUTED, fontSize=9)
        val_st = ParagraphStyle("CardVal", parent=ST_CELL,
                                fontName="Helvetica-Bold", textColor=NAVY, fontSize=10)
        wrapped.append([
            Paragraph(label, lbl_st),
            Paragraph(value, val_st),
        ])
    t = Table(wrapped, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, -1), SOFT_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEABOVE", (0, 0), (-1, 0), 0, colors.white),
        ("LINEABOVE", (0, 1), (-1, -1), 0.4, colors.white),
    ]))
    return t


def section_header(number, title):
    """Nummerert seksjons-header med farget chip foran tittelen."""
    chip_st = ParagraphStyle(
        "Chip", parent=_styles["BodyText"],
        fontName="Helvetica-Bold", fontSize=10, leading=14,
        textColor=colors.white, alignment=TA_CENTER,
        backColor=PRIMARY, borderPadding=(2, 5, 2, 5),
        spaceBefore=0, spaceAfter=0)
    title_st = ParagraphStyle(
        "STitle", parent=ST_SECTION,
        leftIndent=0, spaceBefore=0, spaceAfter=0)
    chip = Paragraph(f"&nbsp;{number:02d}&nbsp;", chip_st)
    title_para = Paragraph(title, title_st)
    tbl = Table([[chip, title_para]], colWidths=[1.1 * cm, None])
    tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 10),
    ]))
    return tbl


def section_rule():
    """Tynn delelinje under seksjons-header."""
    return HRFlowable(width="100%", thickness=0.6, color=ACCENT,
                      spaceBefore=4, spaceAfter=10)


def hero_block(title, subtitle, date_label):
    """Stor topp-tittel for PDF-ens første side."""
    return [
        HRFlowable(width="100%", thickness=3, color=PRIMARY, spaceBefore=0, spaceAfter=8),
        Paragraph(title, ST_HERO_TITLE),
        Paragraph(subtitle, ST_HERO_SUB),
        Paragraph(date_label, ST_HERO_DATE),
        HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=0, spaceAfter=14),
    ]


# ============================================================
# SIDE-FOOTER
# ============================================================
def make_footer(canvas, doc, project_label):
    """Tegner tynn linje + sidenummer + prosjektnavn nederst på hver side."""
    canvas.saveState()
    page_num = canvas.getPageNumber()
    width = A4[0]
    # tynn linje
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.4)
    canvas.line(2 * cm, 1.4 * cm, width - 2 * cm, 1.4 * cm)
    # tekst
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(2 * cm, 1 * cm, project_label)
    canvas.drawRightString(width - 2 * cm, 1 * cm, f"Side {page_num}")
    canvas.restoreState()


def build_doc(out_path, title, project_label):
    """Returnerer en SimpleDocTemplate + bound onPage-funksjon klar til build()."""
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.8 * cm, bottomMargin=2 * cm,
        title=title, author="LOG565 — Nye Hædda barneskole",
    )
    def _on_page(c, d):
        make_footer(c, d, project_label)
    return doc, _on_page
