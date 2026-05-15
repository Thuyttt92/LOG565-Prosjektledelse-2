"""Lager prosjektstatus til hele teamet (3 studenter) — pedagogisk men kollegial tone."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

PATH = r"C:\Users\Gusta\OneDrive\Documents\Privat\Studier\Bachelore i Logistikk\LOG565 - Prosjektledelse\PROSJEKTSTATUS - Til teamet.pdf"

st_title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=26, leading=30, alignment=TA_CENTER, textColor=colors.HexColor("#1F4E79"), spaceAfter=10)
st_sub = ParagraphStyle("sub", fontName="Helvetica", fontSize=14, leading=18, alignment=TA_CENTER, textColor=colors.HexColor("#2E75B6"), spaceAfter=6)
st_meta = ParagraphStyle("meta", fontName="Helvetica", fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#595959"), spaceAfter=18)
st_h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#1F4E79"), spaceBefore=14, spaceAfter=8)
st_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=colors.HexColor("#2E75B6"), spaceBefore=8, spaceAfter=4)
st_body = ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=14.5, alignment=TA_JUSTIFY, spaceAfter=4)
st_bullet = ParagraphStyle("bul", parent=st_body, leftIndent=18, bulletIndent=4, spaceAfter=2)
st_callout = ParagraphStyle("co", fontName="Helvetica", fontSize=10.5, leading=14.5, backColor=colors.HexColor("#FFF2CC"), borderPadding=8, spaceAfter=8, spaceBefore=4, leftIndent=4, rightIndent=4)
st_box = ParagraphStyle("bx", fontName="Helvetica", fontSize=10, leading=13.5, backColor=colors.HexColor("#DEEBF7"), borderPadding=8, spaceAfter=6, spaceBefore=2, leftIndent=4, rightIndent=4)
st_code = ParagraphStyle("code", fontName="Courier", fontSize=9, leading=12, backColor=colors.HexColor("#F2F2F2"), borderPadding=6, leftIndent=8, rightIndent=8, spaceAfter=6, spaceBefore=2)

doc = SimpleDocTemplate(PATH, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm,
                         title="Prosjektstatus - LOG565")
story = []

# Forside
story.append(Spacer(1, 1*cm))
story.append(Paragraph("PROSJEKTSTATUS", st_title))
story.append(Paragraph("LOG565 — Nye Hædda barneskole", st_sub))
story.append(Paragraph("Status pr. 04.05.2026 — til hele studiegruppen", st_meta))

# Korte fakta
fakta = [
    ["Emne", "LOG565 Prosjektledelse 2"],
    ["Vurderingsform", "Mappeinnlevering, 100 % av karakter"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow"],
    ["Format", "Zip-fil med alle leveranser fra fase 2, 3 og 4"],
    ["Mål", "A-nivå (90–100 poeng)"],
    ["Prosjekt i oppgaven", "Nye Hædda barneskole — fiktiv ny skole for 600 elever"],
]
t = Table(fakta, colWidths=[5*cm, 10*cm])
t.setStyle(TableStyle([
    ("FONT", (0, 0), (0, -1), "Helvetica-Bold", 10.5),
    ("FONT", (1, 0), (1, -1), "Helvetica", 10.5),
    ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#1F4E79")),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(t)

# 1. Hva oppgaven går ut på
story.append(Paragraph("1. Det vi skal levere", st_h1))
story.append(Paragraph(
    "Vi skal styre prosjektet «Nye Hædda barneskole» gjennom tre faser av PMI-modellen "
    "(planlegging, gjennomføring, avslutning) og levere en mappe med alle styringsdokumentene. "
    "Fase 1 (initiering — prosjektforslag og konseptløsning) er allerede gitt og legges ved som vedlegg.",
    st_body))
story.append(Paragraph("Konkrete leveranser per fase:", st_h2))
fase = [
    ["Fase", "Leveranser", "Vekt"],
    ["1 — Initiering (vedlegg)", "Prosjektforslag + konseptløsning. Ikke sensurert, men skal være med.", "—"],
    ["2 — Planlegging", "Kravspesifikasjon, WBS, WBS-diagram, presedensdiagram, Gantt, risikoregister, komplett prosjektplan (PDF).", "40 %"],
    ["3 — Gjennomføring", "Gantt med status tracking, månedlige styringsrapporter (KPI, S-kurve, EVM), endringsstyring, problemliste.", "35 %"],
    ["4 — Avslutning", "Sluttrapport med måloppnåelse, lærdom og refleksjon.", "10 %"],
    ["+ Tverrgående", "Sporbarhet, profesjonalitet og dokumentkvalitet.", "15 %"],
]
ft = Table(fase, colWidths=[4*cm, 9.5*cm, 2*cm])
ft.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(ft)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "<b>For A-nivå</b> krever sensorveiledningen minst 40 krav i kravspesifikasjonen og en WBS "
    "med minst 60 leveranser i 4 nivåer.",
    st_callout))

# 2. Viktig endring fra Bård
story.append(Paragraph("2. Viktig endring fra Bård (04.05.2026)", st_h1))
story.append(Paragraph(
    "Bård sendte beskjed om at simuleringsappen som skulle gi oss kostnader og varigheter ikke fungerer. "
    "Han kjører simuleringen manuelt i stedet:",
    st_body))
for s in [
    "Vi sender WBS, kravspesifikasjon og risikoregister til Bård via Oppgaver i Canvas.",
    "Bård fyller inn tids- og kostnadsestimater per WBS-leveranse og sender filen tilbake.",
    "Vi legger tallene inn i Gantt (MS Project) og fortsetter med plan, gjennomføring og rapportering.",
    "Vi sender Bård en personlig melding på Teams etter innlevering, så han ser at filene er klare.",
]:
    story.append(Paragraph(f"&bull; {s}", st_bullet))
story.append(Paragraph(
    "Konsekvens: Kvaliteten på det vi sender Bård er nå ekstra viktig. Hans estimater bygger direkte "
    "på det vi leverer, så jo tydeligere WBS-en og kravspecen er, desto bedre estimater får vi tilbake.",
    st_body))

story.append(PageBreak())

# 3. Hva vi gjorde i dag
story.append(Paragraph("3. Det vi har gjort i dag", st_h1))
story.append(Paragraph(
    "Hovedfokus i dag har vært å få planleggingsfasens grunnlag opp på A-nivå og pakke det klart "
    "for innsending til Bård. Hver leveranse ligger i mappa <b>02 - Planlegging</b>.",
    st_body))

story.append(Paragraph("3.1 Mappestruktur ryddet", st_h2))
story.append(Paragraph(
    "Filene var spredt i mange undermapper og hadde lange tekniske filnavn. Vi har strammet opp "
    "strukturen og samlet ting tematisk:",
    st_body))
struct = [
    ["Mappe", "Innhold"],
    ["00 - Oversikt", "Arbeidsdokumenter (innleveringsoversikt, fremdriftsplan, A-nivå-utkast)."],
    ["01 - Initiering", "Prosjektforslag og konseptløsning."],
    ["02 - Planlegging", "Alle leveranser for fase 2 — det vi sender til Bård + plandokumenter."],
    ["03 - Gjennomføring", "Maler og kommende leveranser for fase 3."],
    ["04 - Avslutning", "Mal og kommende sluttrapport."],
    ["Pensum", "Forelesningskapitler og MS Project how-to-PDF."],
    ["Oppgavebeskrivelse", "Konkretisering og sensorveiledning."],
    ["Maler og eksempler MDV3", "Skolens 1.x og 2.x referanseeksempler."],
]
st = Table(struct, colWidths=[5*cm, 10.5*cm])
st.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(st)

# 3.2 Kravspesifikasjon
story.append(Paragraph("3.2 Kravspesifikasjonen — utvidet til 59 krav", st_h2))
story.append(Paragraph(
    "Kravspesifikasjonen er en strukturert liste over hva bygget «Skal» eller «Bør» oppfylle. "
    "Hver linje har ID, kategori, beskrivelse, prioritet, kobling til en WBS-leveranse, "
    "ansvarlig disiplin (f.eks. arkitekt, elektro), verifikasjonsmetode og kilde.",
    st_body))
story.append(Paragraph(
    "Vi har 59 krav fordelt på 9 kategorier — over A-grensen på 40:",
    st_body))
kat = [
    ["Kategori", "Antall", "Eksempler"],
    ["Funksjonelt", "15", "Antall elever, klasserom, gymsal, kantine, helseavdeling, SFO."],
    ["Teknisk", "11", "TEK17, ventilasjon, vannbåren varme, WiFi 100 Mbps, SD-anlegg, heis."],
    ["Miljø", "6", "BREEAM Very Good, sedumtak, ladeplasser, energiforbruk, avfallssortering."],
    ["Sikkerhet", "6", "Sprinkler, rømningsveier, adgangskontroll, kamera, alarm, lockdown."],
    ["Uteområde", "7", "Lekeplass m/fallunderlag, ballbinge, sykkelparkering, belysning, skjerming."],
    ["Akustikk", "3", "Etterklangstid i klasserom, gymsal, fellesarealer (NS 8175)."],
    ["Universell utforming", "4", "TEK17 §12, heis i alle etasjer, ledelinjer, teleslynge."],
    ["Kvalitet", "3", "Null kritiske mangler ved overtakelse, FDV, garantitid."],
    ["Drift/FDV", "4", "Slitesterke materialer, energiavlesning per sone, brukeropplæring."],
]
kt = Table(kat, colWidths=[3.5*cm, 1.5*cm, 10.5*cm])
kt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(kt)

# 3.3 WBS
story.append(Paragraph("3.3 WBS — 116 linjer i 4 nivåer", st_h2))
story.append(Paragraph(
    "WBS (Work Breakdown Structure) er en hierarkisk nedbrytning av prosjektet i håndterbare leveranser. "
    "Hver leveranse blir en oppgave i Gantt-diagrammet. Strukturen er bygget i 4 nivåer slik sensorveiledningen "
    "krever for A.",
    st_body))
wbs = [
    ["Nivå 1", "Hovedgren (8 stk)"],
    ["1", "Prosjektledelse og administrasjon"],
    ["2", "Planlegging og prosjektering"],
    ["3", "Forberedelse og riving"],
    ["4", "Skolebygg — bygningsmessige arbeider"],
    ["5", "Skolebygg — tekniske anlegg"],
    ["6", "Utomhus og uteområder"],
    ["7", "Inventar og utstyr (FF&E)"],
    ["8", "Overtakelse og avslutning"],
]
wt = Table(wbs, colWidths=[2*cm, 13.5*cm])
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
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(
    "Hver hovedgren er brutt videre ned på nivå 2, 3 og 4. Eksempel på dybde i kjede 4.1 Råbygg:",
    st_body))
story.append(Paragraph(
    "4.1 Råbygg<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;4.1.1 Bærekonstruksjon<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.1 Søyler og dragere (stål/limtre)<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.2 Etasjeskillere (hulldekker)<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.3 Stabiliserende vegger og avstivninger",
    st_box))
story.append(Paragraph(
    "Total: 116 linjer, hvorav 108 er reelle leveranser (nivå 2 og dypere). Hver leveranse har avhengigheter "
    "(hva som må være ferdig før den kan starte) og kobling til kravspesifikasjonen.",
    st_body))

story.append(PageBreak())

# 3.4 Risiko
story.append(Paragraph("3.4 Risikoregister — 15 risikoer med scoring og budsjett", st_h2))
story.append(Paragraph(
    "Risikoregisteret kartlegger ting som kan gå galt og hva vi gjør for å redusere dem. "
    "Hver risiko er scoret 1–5 på sannsynlighet (S) og konsekvens (K). Score = S × K.",
    st_body))
story.append(Paragraph("Kolonnene i registeret:", st_h2))
for s in [
    "ID, kategori, beskrivelse av risikoen.",
    "S og K på 1–5-skala. Score-feltet beregner nivå (lav/middels/høy/kritisk).",
    "Risikoeier (den som har overordnet ansvar) vs. tiltaksansvarlig (den som utfører).",
    "Tiltak for å redusere sannsynligheten og/eller konsekvensen.",
    "Restrisiko etter tiltak (S og K på nytt).",
    "Risikobudsjett: hvor mye tid (dager) og kostnad (mill. kr) som settes av hvis risikoen slår til.",
    "Kobling til WBS-elementet risikoen påvirker.",
]:
    story.append(Paragraph(f"&bull; {s}", st_bullet))
story.append(Paragraph(
    "Sum risikobudsjett er ca. <b>158 dager og 26,4 mill. kr</b> totalt. "
    "Topp 3 før tiltak: kvikkleire (R-001, score 20), råvarepriser (R-005, score 12), ekstremvær (R-009, score 12).",
    st_body))

# 3.5 PPT-diagrammer
story.append(Paragraph("3.5 WBS-diagram og presedensdiagram (PowerPoint)", st_h2))
story.append(Paragraph(
    "WBS-diagrammet viser hierarkiet visuelt over 10 slides. Presedensdiagrammet viser hvordan "
    "leveransene henger sammen i tid og hva som må komme først (Activity-on-Node) over 11 slides. "
    "Begge ligger i 02 - Planlegging.",
    st_body))

# 3.6 Komplett prosjektplan
story.append(Paragraph("3.6 Komplett prosjektplan (PDF)", st_h2))
story.append(Paragraph(
    "Dette er sammenstillingsdokumentet som binder alt sammen — sammendrag, mål, omfang, organisering, "
    "krav, WBS, presedens, tidsplan, kostnadsbudsjett, risikostyring, kvalitet/HMS/miljø, kommunikasjon, "
    "endringsstyring og vedlegg. Dokumentet har 14 kapitler over ca. 14 sider. "
    "De spesifikke tids- og kostnadstallene fylles inn når Bård svarer.",
    st_body))

# 3.7 MS Project import
story.append(Paragraph("3.7 MS Project-import-fil", st_h2))
story.append(Paragraph(
    "Vi har laget en Excel som er ferdig formatert for direkte import til MS Project (File &rarr; Open). "
    "Når vi får tallene fra Bård, kan vi kopiere dem inn og åpne MS Project — så har vi en Gantt med "
    "korrekt struktur, avhengigheter og baseline.",
    st_body))

# 4. Hvor ting ligger
story.append(Paragraph("4. Filer i 02 - Planlegging", st_h1))
files = [
    ["Filnavn", "Hva"],
    ["Kravspesifikasjon - Nye Hædda barneskole.xlsx", "Kravspec — 59 krav, 9 kategorier."],
    ["WBS - Nye Hædda barneskole.xlsx", "WBS — 116 linjer i 4 nivåer."],
    ["Risikoregister - Nye Hædda barneskole.xlsx", "Risiko — 15 stk med scoring og budsjett."],
    ["WBS-diagram - Nye Hædda barneskole.pptx", "Visuelt WBS-tre."],
    ["Presedensdiagram - Nye Hædda barneskole.pptx", "Avhengigheter mellom leveranser."],
    ["Komplett prosjektplan - Nye Hædda barneskole.pdf", "Sammenstillingsdokumentet."],
    ["Gantt-import (klar for MS Project) - Nye Hædda barneskole.xlsx", "Klar for import når Bård svarer."],
    ["Følgebrev til Bård.md", "Tekst som ligger i zip-en til Bård."],
    ["Til Bård - Nye Hædda barneskole.zip", "Pakken som skal sendes inn."],
    ["Maler og eksempler/", "Maler, eldre utkast, eksempler."],
]
fil = Table(files, colWidths=[8*cm, 7.5*cm])
fil.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(fil)

# 5. Neste steg
story.append(Paragraph("5. Neste steg", st_h1))
story.append(Paragraph(
    "Pakken er klar til å sendes til Bård. Etter det er det en venteperiode mens han fyller inn "
    "tids- og kostnadsestimater. Når svaret kommer:",
    st_body))
neste = [
    ["Når", "Hva"],
    ["I morgen tidlig (5. mai)", "Lever zip-pakken til Bård via Oppgaver i Canvas + sende ham personlig melding på Teams."],
    ["5.–12. mai", "Vente på Bård. Bruke tiden til finpussing av Komplett prosjektplan og lese pensum."],
    ["Når Bård svarer", "Kopiere tall inn i Gantt-import-fila → importere til MS Project → sette baseline → eksportere .mpp."],
    ["13.–17. mai", "Sammenstille fase 2: oppdatere Komplett prosjektplan, sende inn for Bårds godkjenning."],
    ["18.–26. mai", "Fase 3: status tracking i MS Project, månedlige rapporter med S-kurve og earned value."],
    ["27.–31. mai", "Fase 4: skrive sluttrapport. Buffer/finpussing."],
    ["1. juni 15:00", "Innlevering i WiseFlow."],
]
nt = Table(neste, colWidths=[4.5*cm, 11*cm])
nt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E75B6")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
    ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#FFE699")),
    ("FONT", (0, -1), (-1, -1), "Helvetica-Bold", 10.5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9D9D9")),
]))
story.append(nt)

# 6. Vurderingskriterier
story.append(Paragraph("6. Hva sensor ser etter (sensorveiledning)", st_h1))
story.append(Paragraph(
    "100 poeng totalt fordelt over fire områder. For å sikte på A er det særlig viktig at:",
    st_body))
for s in [
    "Filene henger sammen — krav peker til WBS, WBS peker til risiko, risiko peker tilbake til WBS.",
    "Plan, gjennomføring og avslutning forteller én sammenhengende historie.",
    "Vi har baseline + status tracking i MS Project (ikke bare en plan, men også oppfølging).",
    "Månedsrapportene bruker KPI, S-kurve og earned value-analyse — ikke bare beskrivelse.",
    "Endringer dokumenteres med konsekvensanalyse for omfang, tid, kostnad og risiko.",
    "Sluttrapporten har analyse og refleksjon — ikke bare oppsummering.",
    "Profesjonell utforming — ryddige tabeller, figurer, språk.",
]:
    story.append(Paragraph(f"&bull; {s}", st_bullet))

story.append(Spacer(1, 0.5*cm))
story.append(Paragraph(
    "Spør gjerne hvis noe i strukturen er uklart — alle filene har vi forklart strukturen på i fanen "
    "«Til Bård» internt i Excel-dokumentene, og samme struktur brukes i Komplett prosjektplan-PDFen.",
    st_box))

doc.build(story)
print(f"Lagret: {PATH}")
