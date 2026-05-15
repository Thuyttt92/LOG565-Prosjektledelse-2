"""Lager en huskeliste-PDF som ligger synlig i rotmappen."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

PATH = r"C:\Users\Gusta\OneDrive\Documents\Privat\Studier\Bachelore i Logistikk\LOG565 - Prosjektledelse\HUSKELISTE - Start her i morgen.pdf"

styles = getSampleStyleSheet()
st_title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=26, leading=30, alignment=TA_CENTER, textColor=colors.HexColor("#1F4E79"), spaceAfter=14)
st_subtitle = ParagraphStyle("sub", fontName="Helvetica", fontSize=13, leading=16, alignment=TA_CENTER, textColor=colors.HexColor("#595959"), spaceAfter=18)
st_h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#1F4E79"), spaceBefore=14, spaceAfter=8)
st_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=colors.HexColor("#2E75B6"), spaceBefore=8, spaceAfter=4)
st_body = ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=14, alignment=TA_JUSTIFY, spaceAfter=4)
st_step = ParagraphStyle("step", fontName="Helvetica", fontSize=11, leading=15, leftIndent=20, bulletIndent=4, spaceAfter=3)
st_code = ParagraphStyle("code", fontName="Courier", fontSize=9, leading=12, backColor=colors.HexColor("#F2F2F2"), borderPadding=6, leftIndent=8, rightIndent=8, spaceAfter=6, spaceBefore=4)
st_warn = ParagraphStyle("warn", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=colors.HexColor("#C00000"), backColor=colors.HexColor("#FFF2CC"), borderPadding=8, spaceAfter=8, spaceBefore=4)

doc = SimpleDocTemplate(PATH, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm,
                         title="Huskeliste - LOG565")
story = []

story.append(Paragraph("HUSKELISTE", st_title))
story.append(Paragraph("LOG565 — Nye Hædda barneskole — Start her i morgen", st_subtitle))

# Status pr i kveld
story.append(Paragraph("Hvor vi står (oppdatert 04.05.2026 kveld)", st_h1))
status = [
    ["Det som er FERDIG i kveld", "Status"],
    ["Filstruktur ryddet — alt er enkelt å finne", "OK"],
    ["INNLEVERINGSOVERSIKT.md og FREMDRIFTSPLAN_LOG565.md oppdatert med Bårds nye flyt", "OK"],
    ["Kravspesifikasjon utvidet til 59 krav (A-nivå krever 40)", "OK"],
    ["WBS utvidet til 116 linjer i 4 nivåer (A-nivå krever 60 leveranser, 4 nivåer)", "OK"],
    ["Risikoregister oppgradert med scoring, risikobudsjett, restrisiko, eier", "OK"],
    ["WBS-diagram (pptx) bygget — 10 slides", "OK"],
    ["Presedensdiagram (pptx) bygget — 11 slides", "OK"],
    ["Komplett prosjektplan (pdf) skjelett klart — 14 kapitler", "OK"],
    ["MS Project-import-fil bygget", "OK"],
    ["Zip-pakke til Bård klar i 02 - Planlegging", "OK"],
    ["Følgebrev til Bård skrevet", "OK"],
]
t = Table(status, colWidths=[14*cm, 2*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("BACKGROUND", (1, 1), (1, -1), colors.HexColor("#C6E0B4")),
    ("ALIGN", (1, 1), (1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(t)

story.append(Paragraph("DET SOM SKAL GJØRES I MORGEN", st_h1))
story.append(Paragraph(
    "Hovedmålet i morgen er å sende pakken til Bård så raskt som mulig. Bård sender den tilbake "
    "med tids- og kostnadsestimater, og de er kritiske for å fullføre Gantt og resten av planen.",
    st_body))

# === STEG 1 ===
story.append(Paragraph("Steg 1 — Kvalitetssjekk pakken (5 min)", st_h2))
story.append(Paragraph("Åpne disse tre filene og bla raskt gjennom:", st_body))
files1 = [
    "02 - Planlegging\\Kravspesifikasjon - Nye Hædda barneskole.xlsx",
    "02 - Planlegging\\WBS - Nye Hædda barneskole.xlsx",
    "02 - Planlegging\\Risikoregister - Nye Hædda barneskole.xlsx",
]
for f in files1:
    story.append(Paragraph(f"&bull; {f}", st_step))
story.append(Paragraph("Sjekk at:", st_body))
for s in [
    "Antall krav er 59 (Statistikk-arket).",
    "WBS er 116 linjer i 4 nivåer (Statistikk-arket).",
    "Risikoregisteret har 15 rader, og sum-raden viser ca. 158 dager / 26,4 mill kr.",
    "Æ/Ø/Å vises riktig — ikke som rare tegn.",
]:
    story.append(Paragraph(f"&bull; {s}", st_step))

# === STEG 2 ===
story.append(Paragraph("Steg 2 — Lever pakken i Canvas (5 min)", st_h2))
story.append(Paragraph(
    "Logg inn i Canvas → LOG565 → Oppgaver → finn riktig oppgave for innlevering av WBS+kravspec → last opp:",
    st_body))
story.append(Paragraph(
    "02 - Planlegging\\Til Bård - Nye Hædda barneskole.zip",
    st_code))
story.append(Paragraph(
    "Hvis Canvas vil ha individuelle filer i stedet for zip, last opp disse fire filene direkte:",
    st_body))
files2 = [
    "Kravspesifikasjon - Nye Hædda barneskole.xlsx",
    "WBS - Nye Hædda barneskole.xlsx",
    "Risikoregister - Nye Hædda barneskole.xlsx",
    "Følgebrev til Bård.md",
]
for f in files2:
    story.append(Paragraph(f"&bull; {f}", st_step))

# === STEG 3 ===
story.append(Paragraph("Steg 3 — Send Teams-melding til Bård (2 min)", st_h2))
story.append(Paragraph(
    "Åpne Teams → finn Bård → send personlig melding. Forslag til tekst:",
    st_body))
story.append(Paragraph(
    "Hei Bård,<br/><br/>"
    "Jeg har nettopp lastet opp pakken med WBS, kravspesifikasjon og risikoregister i Oppgaver "
    "for Nye Hædda barneskole, slik du beskrev i meldingen om alternativ simulering.<br/><br/>"
    "Pakken inneholder:<br/>"
    "&bull; Kravspesifikasjon — 59 krav<br/>"
    "&bull; WBS — 116 linjer i 4 nivåer<br/>"
    "&bull; Risikoregister — 15 risikoer med scoring og foreslått risikobudsjett<br/>"
    "&bull; Et kort følgebrev<br/><br/>"
    "WBS-fila har gule kolonner (H–K) der jeg har forberedt plass for dine "
    "tids- og kostnadsestimater. Si gjerne fra hvis noe trenger justering.<br/><br/>"
    "Tusen takk!",
    st_body))

story.append(PageBreak())

# === STEG 4 ===
story.append(Paragraph("Steg 4 — Mens du venter på Bård", st_h1))
story.append(Paragraph(
    "Bård kan trenge noen dager. Bruk ventetiden til:",
    st_body))
for s in [
    "Lese gjennom Komplett prosjektplan - Nye Hædda barneskole.pdf og se om noe kan finpusses.",
    "Sjekke gjennom WBS-diagrammet og presedensdiagrammet (pptx-filer i 02 - Planlegging).",
    "Lese pensum i Pensum/-mappa hvis du har tid.",
    "Bli kjent med malene i 03 - Gjennomføring/Maler og 04 - Avslutning/Maler.",
]:
    story.append(Paragraph(f"&bull; {s}", st_step))

# === STEG 5 ===
story.append(Paragraph("Steg 5 — Når Bård svarer (gjør så fort som mulig)", st_h1))
story.append(Paragraph("Du får tilbake en oppdatert WBS-fil med tall i kolonnene H–K.", st_body))
story.append(Paragraph("a) Lagre Bårds fil i 02 - Planlegging og overskriv din versjon.", st_step))
story.append(Paragraph("b) Åpne Gantt-import-filen og kopier inn Bårds varigheter og kostnader:", st_step))
story.append(Paragraph(
    "02 - Planlegging\\Gantt-import (klar for MS Project) - Nye Hædda barneskole.xlsx",
    st_code))
story.append(Paragraph(
    "c) Åpne MS Project (NB: må være installert) → File → Open → bla deg frem til denne Excel-fila → "
    "velg 'Excel Workbook' i filtypen → følg Import Wizard.",
    st_step))
story.append(Paragraph(
    "d) Sett prosjektets startdato i MS Project, og lagre baseline (Project → Set Baseline → Save Baseline).",
    st_step))
story.append(Paragraph(
    "e) Eksporter som .mpp og lagre som «Gantt - Nye Hædda barneskole.mpp» i 02 - Planlegging.",
    st_step))
story.append(Paragraph(
    "f) Si til Claude (denne assistenten) at Bård har svart, så oppdaterer jeg Komplett prosjektplan-PDFen "
    "med korrekte tall og bygger månedsrapport-skjelett med riktig baseline.",
    st_step))

# === FILSTRUKTUR ===
story.append(Paragraph("Filstruktur — hvor ting ligger", st_h1))
struct = [
    ["Mappe", "Innhold"],
    ["00 - Oversikt", "Arbeidsdokumenter (.md): innleveringsoversikt, fremdriftsplan, A-nivå-utkast"],
    ["01 - Initiering", "Prosjektforslag + konseptløsning (vedlegg, ikke sensurert)"],
    ["02 - Planlegging", "ALLE leveranser for fase 2 — alt vi sender til Bård"],
    ["03 - Gjennomføring", "Maler og kommende leveranser for fase 3"],
    ["04 - Avslutning", "Mal og kommende sluttrapport for fase 4"],
    ["Pensum", "Forelesningskapitler + MS Project how-to-PDF"],
    ["Oppgavebeskrivelse", "Sensorveiledning + konkretisering — les ofte!"],
    ["Maler og eksempler MDV3", "Skolens 1.x og 2.x-eksempler — kun referanse"],
]
ts = Table(struct, colWidths=[4.5*cm, 11*cm])
ts.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(ts)

# === Frist ===
story.append(Paragraph("Husk frister", st_h1))
frister = [
    ["Hva", "Når"],
    ["Sende pakke til Bård", "I morgen tidlig (5. mai)"],
    ["Bårds svar (forventet)", "Innen 1 uke (12. mai)"],
    ["Fase 2 låst (Gantt + komplett prosjektplan)", "17. mai"],
    ["Fase 3 ferdig (gjennomføring + månedsrapporter)", "26. mai"],
    ["Fase 4 ferdig (sluttrapport)", "29. mai"],
    ["Buffer/finpussing", "30.–31. mai"],
    ["INNLEVERING I WISEFLOW", "1. juni 2026 kl 15:00"],
]
tf = Table(frister, colWidths=[10*cm, 5.5*cm])
tf.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#C00000")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 10),
    ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#FFE699")),
    ("FONT", (0, -1), (-1, -1), "Helvetica-Bold", 10.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(tf)

story.append(Spacer(1, 0.6*cm))
story.append(Paragraph(
    "VIKTIG: Når du fortsetter i morgen, bare si til Claude noe sånt som «Jeg er tilbake — hvor var vi?» "
    "så plukker jeg opp tråden og går gjennom denne huskelisten med deg punkt for punkt.",
    st_warn))

doc.build(story)
print(f"Lagret: {PATH}")
