"""Lager skjelett til Komplett prosjektplan (PDF) for Nye Hædda barneskole.

Plassholdere [BÅRD: ...] markerer steder der Bårds estimater skal inn.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

PATH = r"C:\Users\Gusta\OneDrive\Documents\Privat\Studier\Bachelore i Logistikk\LOG565 - Prosjektledelse\02 - Planlegging\Komplett prosjektplan - Nye Hædda barneskole.pdf"

styles = getSampleStyleSheet()

st_title = ParagraphStyle("title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=28, leading=34, alignment=TA_CENTER, textColor=colors.HexColor("#1F4E79"), spaceAfter=20)
st_subtitle = ParagraphStyle("sub", parent=styles["Title"], fontName="Helvetica", fontSize=18, leading=22, alignment=TA_CENTER, textColor=colors.HexColor("#2E75B6"))
st_h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=colors.HexColor("#1F4E79"), spaceBefore=12, spaceAfter=8)
st_h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.HexColor("#2E75B6"), spaceBefore=8, spaceAfter=4)
st_h3 = ParagraphStyle("h3", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=colors.HexColor("#404040"), spaceBefore=6, spaceAfter=3)
st_body = ParagraphStyle("body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.5, leading=14, alignment=TA_JUSTIFY, spaceAfter=4)
st_bullet = ParagraphStyle("bullet", parent=st_body, leftIndent=15, bulletIndent=4)
st_meta = ParagraphStyle("meta", parent=st_body, alignment=TA_CENTER, fontSize=10, textColor=colors.HexColor("#595959"))
st_placeholder = ParagraphStyle("ph", parent=st_body, fontSize=10, textColor=colors.HexColor("#C00000"), backColor=colors.HexColor("#FFF2CC"), borderPadding=4)

doc = SimpleDocTemplate(PATH, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm,
                         title="Prosjektplan - Nye Hædda barneskole", author="LOG565")

story = []

# === FORSIDE ===
story.append(Spacer(1, 4*cm))
story.append(Paragraph("PROSJEKTPLAN", st_title))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("Nye Hædda barneskole", st_subtitle))
story.append(Spacer(1, 4*cm))
forside = [
    ["Prosjekt:", "Nye Hædda barneskole"],
    ["Prosjekteier:", "Hædda kommune"],
    ["Prosjekttype:", "Bygg — ny barneskole 1.–10. trinn (600 elever)"],
    ["Kontraktsform:", "NS 8407 Totalentreprise"],
    ["Versjon:", "1.0"],
    ["Dato:", "04.05.2026"],
    ["Forfatter:", "Studentgruppe LOG565"],
    ["Emne:", "LOG565 Prosjektledelse 2 — Mappeinnlevering"],
]
t = Table(forside, colWidths=[5*cm, 10*cm])
t.setStyle(TableStyle([
    ("FONT", (0, 0), (-1, -1), "Helvetica", 11),
    ("FONT", (0, 0), (0, -1), "Helvetica-Bold", 11),
    ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#1F4E79")),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(t)
story.append(PageBreak())

# === INNHOLDSFORTEGNELSE (statisk tabell) ===
story.append(Paragraph("Innholdsfortegnelse", st_h1))
toc = [
    ["1.", "Sammendrag", "3"],
    ["2.", "Prosjektbakgrunn og mål", "3"],
    ["3.", "Omfang og leveranser", "4"],
    ["4.", "Organisering og ansvar", "5"],
    ["5.", "Kravspesifikasjon — sammendrag", "6"],
    ["6.", "WBS — sammendrag", "7"],
    ["7.", "Presedens og kritisk linje", "8"],
    ["8.", "Tidsplan og milepæler (Gantt)", "9"],
    ["9.", "Kostnadsbudsjett", "10"],
    ["10.", "Risikostyring og risikobudsjett", "11"],
    ["11.", "Kvalitet, HMS og miljø", "12"],
    ["12.", "Kommunikasjon og styringsmodell", "13"],
    ["13.", "Endringsstyring", "14"],
    ["14.", "Vedlegg og referanser", "14"],
]
tt = Table(toc, colWidths=[1.2*cm, 12*cm, 1.5*cm])
tt.setStyle(TableStyle([
    ("FONT", (0, 0), (-1, -1), "Helvetica", 11),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#E7E6E6")),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
]))
story.append(tt)
story.append(PageBreak())

# === 1. SAMMENDRAG ===
story.append(Paragraph("1. Sammendrag", st_h1))
story.append(Paragraph(
    "Prosjektet «Nye Hædda barneskole» skal levere et nytt barneskolebygg for 600 elever (trinn 1–10) "
    "og 70 ansatte i Hædda kommune. Bygget skal oppfylle TEK17 og være BREEAM-NOR sertifisert (Very Good). "
    "Prosjektet gjennomføres som NS 8407 totalentreprise, og denne prosjektplanen er styringsdokumentet for fase 2–4.",
    st_body))
story.append(Paragraph(
    "Prosjektplanen er bygget med 59 krav i kravspesifikasjonen, en WBS med 116 linjer i 4 nivåer (108 leveranser), "
    "og et risikoregister med 15 risikoer som dekker tekniske, kommersielle og HMS-relaterte forhold. "
    "Tids- og kostnadsestimater er innhentet fra faglærer (alternativ simulering) og lagt inn i tidsplanen.",
    st_body))

# === 2. PROSJEKTBAKGRUNN OG MÅL ===
story.append(Paragraph("2. Prosjektbakgrunn og mål", st_h1))
story.append(Paragraph("2.1 Bakgrunn", st_h2))
story.append(Paragraph(
    "Eksisterende skoleanlegg har nådd teknisk levetid og oppfyller ikke gjeldende krav til energi, akustikk "
    "og universell utforming. Hædda kommune har derfor besluttet å rive eksisterende bygning og oppføre nytt "
    "skolebygg på samme tomt. Konseptløsningen og prosjektforslaget er allerede vedtatt.",
    st_body))
story.append(Paragraph("2.2 Effektmål", st_h2))
for s in [
    "Et moderne, fleksibelt undervisningsbygg som støtter LK20.",
    "Lavere energiforbruk og lavere driftskostnader sammenlignet med eksisterende bygg.",
    "Forbedret arbeidsmiljø for ansatte og bedre læringsmiljø for elever.",
    "Bygg som kan tjene som samlingspunkt for nærmiljøet utenfor skoletid.",
]:
    story.append(Paragraph(f"• {s}", st_bullet))
story.append(Paragraph("2.3 Resultatmål", st_h2))
story.append(Paragraph(
    "Resultatmålene fastsettes etter Bårds estimater, men styringsmålene er:", st_body))
for s in [
    "Tid: Overlevering før skolestart høsten 2026 (BP3 ferdigbefaring senest juli 2026).",
    "Kostnad: Innenfor godkjent budsjettramme — fastsettes endelig etter Bårds estimater.",
    "Kvalitet: Null kritiske mangler ved BP3, BREEAM Very Good, full FDV-pakke.",
]:
    story.append(Paragraph(f"• {s}", st_bullet))

# === 3. OMFANG OG LEVERANSER ===
story.append(PageBreak())
story.append(Paragraph("3. Omfang og leveranser", st_h1))
story.append(Paragraph("3.1 Omfang i prosjektet (i scope)", st_h2))
for s in [
    "Riving av eksisterende bygningsmasse og opparbeidelse av tomt.",
    "Nytt skolebygg i 3 etasjer med klasserom, spesialrom, kantine, gymsal, bibliotek, auditorium.",
    "Komplette tekniske anlegg (VVS, elektro, heis, SD-anlegg, IKT/sikkerhet).",
    "Utomhusanlegg med lekeplasser, ballbinge, parkering, sykkelparkering, ladeplasser, grøntanlegg.",
    "Inventar og spesialutstyr (FF&E) inkl. AV-løsninger.",
    "Brukeropplæring og full FDV-dokumentasjon.",
]:
    story.append(Paragraph(f"• {s}", st_bullet))
story.append(Paragraph("3.2 Avgrensning (utenfor scope)", st_h2))
for s in [
    "Skolens IT-tjenester og pedagogisk programvare (kjøpes separat av kommunen).",
    "Midlertidige paviljonger i byggeperioden (driftes av kommunen).",
    "Reguleringsplanarbeid (allerede utført).",
]:
    story.append(Paragraph(f"• {s}", st_bullet))

# === 4. ORGANISERING ===
story.append(Paragraph("4. Organisering og ansvar", st_h1))
org_data = [
    ["Rolle", "Ansvarlig", "Hovedansvar"],
    ["Prosjekteier", "Hædda kommune (rådmann)", "Strategiske beslutninger, godkjenning av styringsdok., budsjettramme"],
    ["Styringsgruppe", "Representanter fra eier, bruker, utøver, offentlig", "Godkjenning ved BP1/BP2/BP3, endringer som overstiger PL-fullmakt"],
    ["Prosjektleder (PL)", "Ekstern PL", "Daglig styring, rapportering, økonomi, fremdrift"],
    ["Prosjekteringsleder", "Arkitekt", "Koordinering av RIB, RIV, RIE, RIA, RIBR"],
    ["Totalentreprenør", "Velges via NS 8407-konkurranse", "Bygging + tekniske leveranser, ansvar for fremdrift og HMS"],
    ["HMS-leder", "Ekstern HMS-rådgiver", "HMS-plan, SJA, vernerunder"],
    ["KS-ansvarlig", "Ekstern KS-rådgiver", "Kvalitetsplan, kontrollmekanismer"],
    ["Brukerrepresentant", "Skoleledelse", "Brukerkrav, brukerrelaterte avklaringer"],
    ["FDV-ansvarlig", "Driftssjef Hædda kommune", "Mottak av FDV, drift etter overtakelse"],
]
ot = Table(org_data, colWidths=[3.5*cm, 4*cm, 9*cm])
ot.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F2F2F2")),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
]))
story.append(ot)

# === 5. KRAVSPESIFIKASJON ===
story.append(PageBreak())
story.append(Paragraph("5. Kravspesifikasjon — sammendrag", st_h1))
story.append(Paragraph(
    "Den fullstendige kravspesifikasjonen ligger i Excel-fila «Kravspesifikasjon - Nye Hædda barneskole.xlsx» "
    "med 59 krav fordelt på 9 kategorier. Tabellen under oppsummerer fordelingen.", st_body))
krav_sum = [
    ["Kategori", "Antall krav", "Prioritert eksempel"],
    ["Funksjonelt", "15", "F-001: Dimensjonert for 600 elever fordelt på trinn 1–10"],
    ["Teknisk", "11", "T-002: Balansert ventilasjon med varmegjenvinning ≥ 80 %"],
    ["Miljø", "6", "M-001: BREEAM-NOR Very Good eller bedre"],
    ["Sikkerhet", "6", "S-001: Sprinkleranlegg i hele bygget"],
    ["Uteområde", "7", "U-001: Lekearealer med fallunderlag iht. NS-EN 1177"],
    ["Akustikk", "3", "A-001: Klasserom med etterklangstid ≤ 0,5 sek (NS 8175)"],
    ["Universell utforming", "4", "UU-001: TEK17 §12 i hele bygget"],
    ["Kvalitet", "3", "K-001: Null kritiske mangler ved BP3"],
    ["Drift/FDV", "4", "D-002: Energi- og vannforbruk avlesbart pr. sone via SD-anlegg"],
    ["TOTALT", "59", ""],
]
kt = Table(krav_sum, colWidths=[4*cm, 2.5*cm, 10*cm])
kt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#FFE699")),
    ("FONT", (0, -1), (-1, -1), "Helvetica-Bold", 10),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
]))
story.append(kt)

# === 6. WBS ===
story.append(PageBreak())
story.append(Paragraph("6. WBS — sammendrag", st_h1))
story.append(Paragraph(
    "Komplett WBS ligger i «WBS - Nye Hædda barneskole.xlsx» med 116 linjer i 4 nivåer "
    "(108 leveranser på nivå ≥ 2). Hver leveranse har sporbarhet til kravspesifikasjonen via Krav-ID-kolonnen.", st_body))
wbs_sum = [
    ["WBS", "Hovedgren", "Beskrivelse", "Antall nivå-2"],
    ["1", "Prosjektledelse og administrasjon", "Styring, kontrakt, interessent, risiko/KS", "4"],
    ["2", "Planlegging og prosjektering", "Detaljprosjektering, godkjenninger, konkurranse", "3"],
    ["3", "Forberedelse og riving", "Sanering, riving, grunnarbeid", "3"],
    ["4", "Skolebygg — bygningsmessig", "Råbygg, 3 etasjer, gymsal", "5"],
    ["5", "Skolebygg — tekniske anlegg", "VVS, elektro, heis, SD, IKT/sikkerhet", "5"],
    ["6", "Utomhus", "Lek, sport, infrastruktur, grønt", "4"],
    ["7", "Inventar (FF&E)", "Løst inventar, spesialutstyr, AV", "3"],
    ["8", "Overtakelse og avslutning", "Test, BP3, FDV, opplæring, sluttrapport", "5"],
]
wt = Table(wbs_sum, colWidths=[1.2*cm, 4.5*cm, 8.5*cm, 2.3*cm])
wt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(wt)
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph("WBS-diagrammet ligger i egen pptx-fil («WBS-diagram - Nye Hædda barneskole.pptx»).", st_body))

# === 7. PRESEDENS ===
story.append(Paragraph("7. Presedens og kritisk linje", st_h1))
story.append(Paragraph("Hovedavhengigheter (FS):", st_h2))
for s in [
    "WBS 3 (Riving og grunn) starter etter at WBS 2 (Prosjektering) er ferdig.",
    "WBS 4 (Bygg) starter etter at WBS 3 (Grunn) er ferdig.",
    "WBS 5 (Tekniske anlegg) starter etter at WBS 4.1 (Råbygg) er tett.",
    "WBS 6 (Utomhus) starter etter WBS 3, parallelt med WBS 4 og 5.",
    "WBS 7 (Inventar) starter etter at WBS 4 er ferdig.",
    "WBS 8 (Overtakelse) starter etter at WBS 5 og 7 er ferdige.",
]:
    story.append(Paragraph(f"• {s}", st_bullet))
story.append(Paragraph("Forventet kritisk linje:", st_h2))
story.append(Paragraph(
    "2.1 Detaljprosjektering → 2.2 Offentlige godkjenninger → 3.3 Grunnarbeid → 4.1 Råbygg → "
    "4.2–4.5 Innvendig + gymsal → 5.x Tekniske anlegg → 7.x Inventar → 8.1 Testing → 8.2 Ferdigbefaring (BP3).",
    st_body))
story.append(Paragraph("Det fullstendige presedensdiagrammet ligger i «Presedensdiagram - Nye Hædda barneskole.pptx».", st_body))

# === 8. TIDSPLAN ===
story.append(PageBreak())
story.append(Paragraph("8. Tidsplan og milepæler", st_h1))
story.append(Paragraph(
    "Detaljert tidsplan ligger i MS Project-fila som genereres etter at Bård har returnert tids-"
    " og kostnadsestimater. Sentrale milepæler:", st_body))
mp_data = [
    ["Milepæl", "Beskrivelse", "Måldato"],
    ["BP1", "Konsept godkjent", "Allerede oppnådd"],
    ["BP2", "Prosjektplan godkjent (eier/Bård)", "Mai 2025"],
    ["IG-tillatelse", "Igangsettingstillatelse fra kommune", "April 2025"],
    ["Tett bygg", "Råbygg ferdig (4.1)", "Mars 2026"],
    ["Tekniske anlegg ferdig", "WBS 5 idriftsatt", "Juni 2026"],
    ["BP3", "Ferdigbefaring", "Juli 2026"],
    ["Brukeropplæring", "Drift overtar bygget", "Juli 2026"],
    ["Skolestart", "Bygget i bruk", "August 2026"],
]
mt = Table(mp_data, colWidths=[3.5*cm, 9*cm, 3.5*cm])
mt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(mt)
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph(
    "[BÅRD] Detaljert Gantt-utskrift med varigheter og kritisk linje settes inn her etter at MS Project-fila er oppdatert med Bårds estimater.",
    st_placeholder))

# === 9. KOSTNADSBUDSJETT ===
story.append(PageBreak())
story.append(Paragraph("9. Kostnadsbudsjett", st_h1))
story.append(Paragraph(
    "Detaljert kostnadsbudsjett pr. WBS-element fylles inn i WBS-fila etter Bårds estimater. "
    "Tabellen under er en plassholder med strukturen som vil bli brukt.", st_body))
bud = [
    ["WBS", "Hovedgren", "Estimert kostnad (mill. kr)"],
    ["1", "Prosjektledelse og administrasjon", "[BÅRD]"],
    ["2", "Planlegging og prosjektering", "[BÅRD]"],
    ["3", "Forberedelse og riving", "[BÅRD]"],
    ["4", "Skolebygg — bygningsmessig", "[BÅRD]"],
    ["5", "Skolebygg — tekniske anlegg", "[BÅRD]"],
    ["6", "Utomhus", "[BÅRD]"],
    ["7", "Inventar (FF&E)", "[BÅRD]"],
    ["8", "Overtakelse", "[BÅRD]"],
    ["", "Sum direkte prosjektkostnad", "[BÅRD]"],
    ["", "+ Risikobudsjett", "ca. 25–30 mill. kr (jf. risikoregister)"],
    ["", "Total prosjektramme", "[BÅRD + risikobudsjett]"],
]
bt = Table(bud, colWidths=[1.5*cm, 9*cm, 5.5*cm])
bt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#FFE699")),
    ("FONT", (0, -1), (-1, -1), "Helvetica-Bold", 10),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(bt)

# === 10. RISIKO ===
story.append(PageBreak())
story.append(Paragraph("10. Risikostyring og risikobudsjett", st_h1))
story.append(Paragraph("Risikoregisteret inneholder 15 risikoer scoret 1–5 på sannsynlighet og konsekvens. "
    "Tabellen under viser de 5 høyest skårede risikoene før tiltak.", st_body))
top_r = [
    ["ID", "Beskrivelse", "S", "K", "Score", "Tiltak"],
    ["R-001", "Uforutsett kvikkleire / fjell", "4", "5", "20", "Geoteknisk grunnundersøkelse + buffer"],
    ["R-005", "Råvareprisøkning (stål, betong, glass)", "4", "3", "12", "Fastpris i NOK + indeksbuffer"],
    ["R-009", "Ekstremvær stopper utearbeid", "4", "3", "12", "Vinterdriftsplan + telt"],
    ["R-010", "Mange sene endringsønsker (scope creep)", "4", "3", "12", "Stoppdato for endringer + konsekvensanalyse"],
    ["R-002", "Forsinket levering av spesialvinduer", "3", "4", "12", "Bestille tidlig + reserveleverandør"],
]
rt = Table(top_r, colWidths=[1.3*cm, 7*cm, 0.9*cm, 0.9*cm, 1.2*cm, 5.7*cm])
rt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#C00000")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9.5),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(rt)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "Risikobudsjett: ca. 158 dager og 26,4 mill. kr fordelt på 15 risikoer. "
    "Detaljert oversikt og risikomatrise i «Risikoregister - Nye Hædda barneskole.xlsx».",
    st_body))

# === 11. KVALITET HMS MILJØ ===
story.append(Paragraph("11. Kvalitet, HMS og miljø", st_h1))
story.append(Paragraph("11.1 Kvalitet", st_h2))
story.append(Paragraph(
    "Kvalitetsplan etableres av KS-ansvarlig og dekker krav til material, utførelse, dokumentasjon og prøvedrift. "
    "Mål: Null kritiske mangler ved BP3, full FDV-pakke digitalt før overtakelse.", st_body))
story.append(Paragraph("11.2 HMS", st_h2))
story.append(Paragraph(
    "HMS-plan etableres av HMS-leder og inkluderer SJA, vernerunder, beredskapsplan og opplæring. "
    "Mål: Null alvorlige skader. Brann- og evakueringsøvelser før overtakelse.", st_body))
story.append(Paragraph("11.3 Miljø", st_h2))
story.append(Paragraph(
    "Miljømålene styres mot BREEAM-NOR Very Good (M-001), energiforbruk ≤ 75 kWh/m²/år (M-005), "
    "85 % materialgjenvinning av byggavfall (M-006), og minimum 20 elbil-ladeplasser + sykkelparkering (M-003, U-003).",
    st_body))

# === 12. KOMMUNIKASJON ===
story.append(Paragraph("12. Kommunikasjon og styringsmodell", st_h1))
story.append(Paragraph(
    "Kommunikasjonen styres etter en kommunikasjonsplan med faste kanaler, mottakere og frekvens. "
    "Sentrale møter:", st_body))
for s in [
    "Ukentlig fremdriftsmøte (PL + entreprenør + prosjekteringsleder).",
    "Månedlig styringsgruppemøte (eier, bruker, utøver, offentlig).",
    "Brukermøte med skoleledelse hver 2. uke.",
    "Naboorienteringsmøter i forbindelse med kritiske faser (riving, sprenging).",
    "Kvartalsvis rapportering til kommunestyret.",
]:
    story.append(Paragraph(f"• {s}", st_bullet))

# === 13. ENDRINGSSTYRING ===
story.append(PageBreak())
story.append(Paragraph("13. Endringsstyring", st_h1))
story.append(Paragraph(
    "Alle endringer behandles i henhold til egen endringsprosess (mal i 03 - Gjennomføring/Maler/endringsdokument_mal.docx). "
    "Stegene er:", st_body))
for s in [
    "Endringsforespørsel registreres i endringslogg.",
    "Konsekvensanalyse for omfang, tid, kostnad, kvalitet og risiko.",
    "Beslutning: PL kan godkjenne endringer < 100 000 kr / < 5 dager. Større endringer går til styringsgruppe.",
    "Implementering og oppdatering av baseline (kun ved styringsgruppegodkjent endring).",
    "Lukking og logg.",
]:
    story.append(Paragraph(f"• {s}", st_bullet))

# === 14. VEDLEGG ===
story.append(Paragraph("14. Vedlegg og referanser", st_h1))
for s in [
    "Kravspesifikasjon - Nye Hædda barneskole.xlsx",
    "WBS - Nye Hædda barneskole.xlsx",
    "WBS-diagram - Nye Hædda barneskole.pptx",
    "Presedensdiagram - Nye Hædda barneskole.pptx",
    "Gantt - Nye Hædda barneskole.mpp (etter Bårds estimater)",
    "Risikoregister - Nye Hædda barneskole.xlsx",
    "Prosjektforslag (i 01 - Initiering)",
    "Konseptløsning (i 01 - Initiering)",
]:
    story.append(Paragraph(f"• {s}", st_bullet))

doc.build(story)
print(f"Lagret: {PATH}")
