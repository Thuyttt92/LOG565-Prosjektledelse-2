# -*- coding: utf-8 -*-
"""APA7-inspirert stilmal for Komplett prosjektrapport.

Bygger på reportlab Platypus. Tilbyr:
  - Konsistent typografi (Helvetica som digital substitutt for Times)
  - 5-nivå overskriftshierarki (APA7)
  - Sitering med (Forfatter, år, s. X) som inline-funksjoner
  - Innholdsfortegnelse via TableOfContents
  - Sidehoder/-foter med kapittelnavn og sidetall
  - Tabell- og figurnummerering med caption
  - Sidemargin 2.5 cm (akademisk standard)
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Image, HRFlowable, Frame, PageTemplate,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ============================================================
# FARGEPALETT (samme som status-PDFene for konsistens)
# ============================================================
NAVY = colors.HexColor("#0F2A47")
PRIMARY = colors.HexColor("#1F4E79")
ACCENT = colors.HexColor("#4472C4")
SUBTLE = colors.HexColor("#A6BCD5")
SOFT_BG = colors.HexColor("#F4F7FB")
SOFT_BG_2 = colors.HexColor("#FAFBFD")

SUCCESS = colors.HexColor("#548235")
WARN = colors.HexColor("#BF8F00")
DANGER = colors.HexColor("#C00000")
INFO = colors.HexColor("#2E75B6")

TEXT = colors.HexColor("#1F2937")
TEXT_MUTED = colors.HexColor("#4B5563")
MUTED = colors.HexColor("#6B7280")
BORDER = colors.HexColor("#D9DEE5")

# ============================================================
# TYPOGRAFI — APA7 anbefaler 12pt serif. Vi bruker Helvetica
# for digital lesbarhet med 11pt body.
# ============================================================
BODY_FONT = "Helvetica"
BODY_FONT_BOLD = "Helvetica-Bold"
BODY_FONT_ITALIC = "Helvetica-Oblique"

_styles = getSampleStyleSheet()

# Forside-stiler
ST_COVER_TITLE = ParagraphStyle(
    "CoverTitle", parent=_styles["Heading1"],
    fontName=BODY_FONT_BOLD, fontSize=32, leading=38,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=4)

ST_COVER_SUB = ParagraphStyle(
    "CoverSub", parent=_styles["BodyText"],
    fontName=BODY_FONT, fontSize=15, leading=20,
    textColor=PRIMARY, alignment=TA_LEFT, spaceAfter=24)

ST_COVER_META = ParagraphStyle(
    "CoverMeta", parent=_styles["BodyText"],
    fontName=BODY_FONT, fontSize=11, leading=15,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=4)

ST_COVER_META_BOLD = ParagraphStyle(
    "CoverMetaBold", parent=_styles["BodyText"],
    fontName=BODY_FONT_BOLD, fontSize=11, leading=15,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=4)

# Heading-stiler (APA7-hierarki)
ST_H1 = ParagraphStyle(
    "H1", parent=_styles["Heading1"],
    fontName=BODY_FONT_BOLD, fontSize=20, leading=26,
    textColor=NAVY, alignment=TA_LEFT,
    spaceBefore=18, spaceAfter=10,
    keepWithNext=1)

ST_H2 = ParagraphStyle(
    "H2", parent=_styles["Heading2"],
    fontName=BODY_FONT_BOLD, fontSize=14, leading=18,
    textColor=PRIMARY, alignment=TA_LEFT,
    spaceBefore=16, spaceAfter=6,
    keepWithNext=1)

ST_H3 = ParagraphStyle(
    "H3", parent=_styles["Heading3"],
    fontName=BODY_FONT_BOLD, fontSize=12, leading=15,
    textColor=NAVY, alignment=TA_LEFT,
    spaceBefore=12, spaceAfter=4,
    keepWithNext=1)

ST_H4 = ParagraphStyle(
    "H4", parent=_styles["Heading3"],
    fontName=BODY_FONT_ITALIC, fontSize=11.5, leading=14,
    textColor=PRIMARY, alignment=TA_LEFT,
    spaceBefore=10, spaceAfter=2,
    keepWithNext=1)

# Body-stiler
ST_BODY = ParagraphStyle(
    "Body", parent=_styles["BodyText"],
    fontName=BODY_FONT, fontSize=11, leading=16,
    textColor=TEXT, alignment=TA_JUSTIFY,
    spaceBefore=2, spaceAfter=8,
    firstLineIndent=0)

ST_BODY_INDENT = ParagraphStyle(
    "BodyIndent", parent=ST_BODY,
    leftIndent=20, spaceAfter=6)

ST_QUOTE = ParagraphStyle(
    "Quote", parent=ST_BODY,
    fontName=BODY_FONT_ITALIC, fontSize=10.5, leading=15,
    leftIndent=24, rightIndent=24,
    textColor=TEXT_MUTED, spaceBefore=8, spaceAfter=10)

ST_BULLET = ParagraphStyle(
    "Bullet", parent=ST_BODY,
    leftIndent=18, bulletIndent=4,
    spaceBefore=1, spaceAfter=3)

ST_CAPTION = ParagraphStyle(
    "Caption", parent=_styles["BodyText"],
    fontName=BODY_FONT_ITALIC, fontSize=9.5, leading=12.5,
    textColor=TEXT_MUTED, alignment=TA_LEFT,
    spaceBefore=4, spaceAfter=14)

ST_CAPTION_BOLD = ParagraphStyle(
    "CaptionBold", parent=ST_CAPTION,
    fontName=BODY_FONT_BOLD, textColor=NAVY)

ST_PULL = ParagraphStyle(
    "Pull", parent=_styles["BodyText"],
    fontName=BODY_FONT_ITALIC, fontSize=13, leading=18,
    textColor=PRIMARY, alignment=TA_LEFT,
    leftIndent=20, rightIndent=20,
    spaceBefore=10, spaceAfter=12)

ST_NOTE = ParagraphStyle(
    "Note", parent=ST_BODY,
    fontName=BODY_FONT_ITALIC, fontSize=10, leading=13,
    textColor=MUTED, leftIndent=12, rightIndent=12,
    spaceBefore=6, spaceAfter=10)

ST_TOC_H1 = ParagraphStyle(
    "TOC1", fontName=BODY_FONT_BOLD, fontSize=11.5,
    leading=18, textColor=NAVY, leftIndent=0)

ST_TOC_H2 = ParagraphStyle(
    "TOC2", fontName=BODY_FONT, fontSize=10.5,
    leading=15, textColor=TEXT, leftIndent=18)

ST_TOC_H3 = ParagraphStyle(
    "TOC3", fontName=BODY_FONT, fontSize=10,
    leading=14, textColor=TEXT_MUTED, leftIndent=34)

ST_REFERENCE = ParagraphStyle(
    "Reference", parent=ST_BODY,
    fontName=BODY_FONT, fontSize=10, leading=14,
    leftIndent=24, firstLineIndent=-24,
    spaceAfter=8)


# ============================================================
# PAGE TEMPLATES — Header + Footer
# ============================================================
class HeaderFooterCanvas(canvas.Canvas):
    """Custom canvas for sidehoder, sidetall og fotnoter."""

    def __init__(self, *args, **kwargs):
        self.section_title = kwargs.pop("section_title", "")
        self.report_title = kwargs.pop("report_title", "")
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for i, page in enumerate(self.pages, 1):
            self.__dict__.update(page)
            # Skip header/footer på forsiden (side 1)
            if i > 1:
                self.draw_header(self.report_title)
                self.draw_footer(i, page_count)
            super().showPage()
        super().save()

    def draw_header(self, report_title):
        """Tom header — ingen tekst, ren topp."""
        pass

    def draw_footer(self, page_num, total):
        """Minimalistisk footer: kun sidenummer sentrert."""
        self.saveState()
        self.setFont(BODY_FONT, 9)
        self.setFillColor(MUTED)
        self.drawCentredString(A4[0] / 2, 1.4 * cm, str(page_num))
        self.restoreState()


def build_doc(out_path: str, report_title: str):
    """Bygger SimpleDocTemplate med marginer + canvas-maker."""
    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.2 * cm,
        title=report_title,
        author="Gruppe 4.5 — Bachelor i logistikk, Høgskolen Molde",
    )

    def canvas_maker(filename, **kwargs):
        return HeaderFooterCanvas(filename, report_title=report_title, **kwargs)

    return doc, canvas_maker


# ============================================================
# Custom flowables
# ============================================================
class TOCEntry(Paragraph):
    """Paragraph som registreres i TOC ved bygging."""
    def __init__(self, text, style, level=0, key=None):
        super().__init__(text, style)
        self.toc_level = level
        self.toc_key = key or text

    def draw(self):
        super().draw()
        self.canv.bookmarkPage(self.toc_key)
        self.canv.addOutlineEntry(self.text, self.toc_key, self.toc_level, 0)


def kapittel(nr, tittel, story, toc=None, level=0):
    """Legg til en kapitteloverskrift (H1) med TOC-registrering."""
    text = f"{nr} {tittel}"
    p = Paragraph(text, ST_H1)
    story.append(p)
    if toc is not None:
        toc.addEntry(level, text, story.__len__())  # tracked separat
    return p


def seksjon(nr, tittel, story):
    """H2-overskrift."""
    p = Paragraph(f"{nr} {tittel}", ST_H2)
    story.append(p)
    return p


def underseksjon(nr, tittel, story):
    """H3-overskrift."""
    p = Paragraph(f"{nr} {tittel}", ST_H3)
    story.append(p)
    return p


def body(text, story, style=None):
    """Brødtekstparagraf."""
    story.append(Paragraph(text, style or ST_BODY))


def bullet_list(items, story, style=None):
    """Punktliste."""
    for item in items:
        story.append(Paragraph(item, style or ST_BULLET, bulletText="•"))


def pull_quote(text, story):
    """Pull-quote (sentralt sitat med visual emphasis)."""
    story.append(Spacer(1, 0.2 * cm))
    story.append(HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=0, spaceAfter=0))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph(f"«{text}»", ST_PULL))
    story.append(HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=0, spaceAfter=0))
    story.append(Spacer(1, 0.3 * cm))


def info_box(text, story, color=INFO):
    """Sidebar/info-boks."""
    t = Table([[Paragraph(text, ST_NOTE)]], colWidths=[None])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEBEFORE", (0, 0), (0, -1), 3, color),
    ]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(t)
    story.append(Spacer(1, 0.2 * cm))


def figure(path, story, caption_number, caption_text, width_cm=15):
    """Sett inn figur med APA-stil bildetekst. Proporsjonal skalering."""
    try:
        from PIL import Image as PILImage
        pil = PILImage.open(str(path))
        w_px, h_px = pil.size
        height_cm = width_cm * (h_px / w_px)
        img = Image(str(path), width=width_cm * cm, height=height_cm * cm)
    except Exception:
        img = Image(str(path), width=width_cm * cm)
    img.hAlign = "CENTER"
    story.append(Spacer(1, 0.2 * cm))
    story.append(img)
    p = Paragraph(
        f"<b>Figur {caption_number}.</b> {caption_text}",
        ST_CAPTION)
    story.append(p)


def tabell_caption(number, text, story):
    """APA-stil tabelltekst (over tabellen)."""
    story.append(Spacer(1, 0.2 * cm))
    p = Paragraph(f"<b>Tabell {number}</b>", ST_CAPTION_BOLD)
    story.append(p)
    p2 = Paragraph(f"<i>{text}</i>", ST_CAPTION)
    story.append(p2)


ST_TABLE_CELL = ParagraphStyle(
    "TableCell", parent=_styles["BodyText"],
    fontName=BODY_FONT, fontSize=9.5, leading=12,
    textColor=TEXT, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=0)

ST_TABLE_HEADER = ParagraphStyle(
    "TableHeader", parent=_styles["BodyText"],
    fontName=BODY_FONT_BOLD, fontSize=10, leading=13,
    textColor=colors.white, alignment=TA_LEFT,
    spaceBefore=0, spaceAfter=0)


def _wrap_cells(data, header_row=True):
    """Wrapper strenger i Paragraph-objekter for å unngå tekstoverlapp."""
    nye = []
    for i, row in enumerate(data):
        ny_rad = []
        for c in row:
            if isinstance(c, str):
                stil = ST_TABLE_HEADER if (header_row and i == 0) else ST_TABLE_CELL
                ny_rad.append(Paragraph(c, stil))
            else:
                ny_rad.append(c)
        nye.append(ny_rad)
    return nye


def make_table(data, col_widths=None, header_row=True, zebra=True):
    """Profesjonell tabell med konsistent styling og automatisk tekst-wrapping."""
    data = _wrap_cells(data, header_row=header_row)
    t = Table(data, colWidths=col_widths)
    style = [
        ("FONTNAME", (0, 0), (-1, -1), BODY_FONT),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, BORDER),
        ("LINEABOVE", (0, 0), (-1, 0), 0.8, NAVY),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, NAVY),
    ]
    if header_row:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TOPPADDING", (0, 0), (-1, 0), 8),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), SOFT_BG_2))
    t.setStyle(TableStyle(style))
    return t


# ============================================================
# APA-sitering
# ============================================================
def sit(forfatter: str, år: str, sidetall: str = None) -> str:
    """Inline sitering i APA-stil. Returnerer (Forfatter, år) eller (Forfatter, år, s. X)."""
    if sidetall:
        return f"({forfatter}, {år}, s. {sidetall})"
    return f"({forfatter}, {år})"


def ref(forfatter: str, år: str, tittel: str, kilde: str = "", url: str = "") -> str:
    """Returnerer en APA7-formatert referanseoppføring som rik-tekst paragraf-streng."""
    base = f"{forfatter} ({år}). <i>{tittel}</i>."
    if kilde:
        base += f" {kilde}."
    if url:
        base += f" {url}"
    return base
