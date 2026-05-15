# -*- coding: utf-8 -*-
"""Sluttrapport — Nye Hædda Barneskole (utvidet versjon).

Fokusert sluttrapport for avslutningsfasen (~10 sider).
Hovedleveransen er Komplett prosjektrapport i mappen 05 - Endelig innlevering;
denne rapporten er det formelle sluttdokumentet for fase 4 alene.
"""
from __future__ import annotations
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, Image,
)

from apa_style import (
    build_doc, body, bullet_list, pull_quote, info_box, figure, tabell_caption,
    make_table, sit, ref,
    ST_COVER_TITLE, ST_COVER_SUB, ST_COVER_META, ST_COVER_META_BOLD,
    ST_H1, ST_H2, ST_H3, ST_BODY, ST_BULLET, ST_CAPTION, ST_NOTE, ST_REFERENCE,
    NAVY, PRIMARY, ACCENT, BORDER,
)
from paths import ROOT, ARBEIDSFILER, AVSLUTNING

FIGURER = ARBEIDSFILER / "sluttrapport_figurer"
OUT = AVSLUTNING / "Sluttrapport - Nye Hædda Barneskole.pdf"

doc, canvas_maker = build_doc(str(OUT), "Sluttrapport — Nye Hædda Barneskole")
story = []


def h1(text):
    story.append(PageBreak())
    story.append(Paragraph(text, ST_H1))


def h2(text):
    story.append(Paragraph(text, ST_H2))


def h3(text):
    story.append(Paragraph(text, ST_H3))


# ============================================================
# FORSIDE
# ============================================================
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("SLUTTRAPPORT", ST_COVER_TITLE))
story.append(Spacer(1, 0.6 * cm))
story.append(Paragraph("Nye Hædda Barneskole", ST_COVER_SUB))
story.append(HRFlowable(width="40%", thickness=2, color=PRIMARY,
                        spaceBefore=0, spaceAfter=20))
meta = [
    ("Prosjekt", "Nye Hædda Barneskole"),
    ("Sluttdato", "15. mai 2026 (vedtatt og holdt)"),
    ("Sluttkost", "800 MNOK (BAC, CPI = 1,000)"),
    ("Emne", "LOG565 Prosjektledelse 2"),
    ("Gruppe", "Gruppe 4.5 — Bachelor i logistikk, Høgskolen Molde"),
    ("Versjon", "1.0 — endelig sluttrapport"),
    ("Rapportdato", "15. mai 2026"),
]
rows = [[Paragraph(k, ST_COVER_META_BOLD), Paragraph(v, ST_COVER_META)] for k, v in meta]
t = Table(rows, colWidths=[4.5 * cm, 11 * cm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(t)
story.append(Spacer(1, 4 * cm))
story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER))
story.append(Spacer(1, 0.4 * cm))
story.append(Paragraph(
    "Denne sluttrapporten er det formelle dokumentet for prosjektets avslutningsfase. "
    "For en omfattende behandling av planlegging, gjennomføring og avslutning samlet — "
    "se <b>Komplett prosjektrapport - Nye Hædda Barneskole.pdf</b> i mappen "
    "<i>05 - Endelig innlevering Hædda Barneskole/</i>.",
    ST_NOTE))


# ============================================================
# 1. SAMMENDRAG
# ============================================================
h1("1   Sammendrag")
body(
    "Prosjekt Nye Hædda Barneskole er overlevert til Hædda kommune 15. mai 2026 — på "
    "vedtatt dato — med en sluttkost på 800 millioner kroner som tilsvarer Budget at "
    "Completion (BAC) etter kommunestyrets vedtak NHB-2026-15. Cost Performance Index "
    "(CPI) og Schedule Performance Index (SPI) er begge 1,000 ved sluttføring. Av godkjent "
    "risikoreserve på 50 millioner ble 11 brukt; av 8 ukers tidsbuffer ble 1,5 brukt. "
    "Alle 59 krav i kravspesifikasjonen er levert, alle 32 arbeidspakker er 100 % "
    "fullført, og K-001/K-002 (null kritiske mangler og komplett FDV-dokumentasjon) "
    "er oppfylt. Skolen er klar for skolestart høsten 2026.",
    story)
body(
    "Det er to formelle endringer som er behandlet i prosjektets løp. NHB-2026-15 var "
    "kommunestyrets vedtak om utvidet budsjettramme fra 700 til 800 MNOK og fullmakt "
    "til komprimering (crashing) av kritisk aktivitet 4.1 Råbygg, slik at vedtatt sluttdato "
    "kunne overholdes. CR-001 var en regulatorisk endring som utvidet scope på arbeidspakke "
    "5.1 VVS med oppgradert sprinkler- og rømningsdekning iht. ny DSB-veileder. Tre risikoer "
    "fra registeret ble realisert (R-05, R-06, R-07) og håndtert innenfor godkjente reserver.",
    story)

pull_quote(
    "Prosjektet har lykkes — leveransen er på datoen, på budsjettet og med full "
    "kvalitetsoppfyllelse — fordi vi har håndtert endringer og hendelser med formell "
    "dokumentasjon og analytisk disiplin, ikke fordi prosjektet var enkelt.",
    story)


# ============================================================
# 2. MÅLOPPNÅELSE
# ============================================================
h1("2   Måloppnåelse mot vedtatte rammer")
body(
    "Måloppnåelsen vurderes mot de fire klassiske ytelsesdimensjonene som er felles for "
    f"prosjektledelseslitteraturen — omfang, tid, kost og kvalitet {sit('Project Management Institute', '2021')}. "
    "Tabell 2.1 sammenfatter planlagt mot faktisk for hver dimensjon.",
    story)

tabell_caption("2.1", "Måloppnåelse ved overlevering 15. mai 2026.", story)
mtab = make_table([
    ["Dimensjon", "Planlagt", "Faktisk", "Vurdering"],
    ["Omfang", "59 krav, 32 arbeidspakker",
     "Alle 59 krav levert, alle 32 pakker 100 % fullført",
     "Måloppnådd"],
    ["Tid", "15. mai 2026", "15. mai 2026 (på datoen)",
     "Måloppnådd, 1,5 av 8 uker buffer brukt"],
    ["Kost", "BAC 800 MNOK (etter NHB-2026-15)",
     "AC kumulativ 800,0 MNOK",
     "Måloppnådd, 11 av 50 MNOK reserve brukt"],
    ["Kvalitet", "K-001 (null kritiske mangler), K-002 (komplett FDV)",
     "0 kritiske mangler, FDV levert, brukstillatelse innvilget",
     "Måloppnådd"],
], col_widths=[2.2 * cm, 4.0 * cm, 4.4 * cm, 5.4 * cm])
story.append(mtab)

h2("2.1  Omfang")
body(
    "Den leverte løsningen dekker hele kravspesifikasjonens 59 krav fordelt på funksjonelle, "
    "tekniske, miljømessige, sikkerhetsmessige og driftsmessige kategorier. Bygget er levert "
    "i tre etasjer med 4 608 kvadratmeter grunnflate og om lag 13 824 kvadratmeter bruttoareal "
    "— godt innenfor arealrammen på 14 000 kvadratmeter. Crashing-vedtaket NHB-2026-15 endret "
    "kostnad og tid, men ikke scope. Endringen CR-001 utvidet scope marginalt på arbeidspakke "
    "5.1 VVS med oppgradert sprinklerdekning og rømningsskilting iht. ny DSB-veileder.",
    story)

h2("2.2  Tid")
body(
    "Vedtatt sluttdato 15. mai 2026 er overholdt på datoen. Den opprinnelige Baseline 0 ga "
    "sluttdato i juli 2026 — om lag seks uker etter den vedtatte fristen — basert på Bårds "
    "simulerte WBS som avdekket et underestimat på arbeidspakke 4.1 Råbygg. Etter crashing av "
    "denne aktiviteten ble Baseline 1 etablert med sluttdato innenfor frist. Faktisk fremdrift "
    "målt mot Baseline 1 viser SPI = 1,000 ved overlevering. Av 8 ukers godkjent tidsbuffer "
    "ble 1,5 uker brukt, alle i forbindelse med R-07 (brann hos vindusprodusent i måned 11). "
    "Resterende 6,5 uker er ubrukt.",
    story)

h2("2.3  Kost")
body(
    "Sluttkost er 800 millioner kroner — eksakt lik vedtatt BAC etter NHB-2026-15. Av godkjent "
    "risikoreserve på 50 millioner ble 11 millioner brukt: 6 MNOK i måned 4 (R-05 forurenset "
    "masse) og 5 MNOK i måned 13 (R-06/CR-001 DSB sprinkler). Cost Performance Index er 1,000 "
    "ved overlevering, hvilket innebærer at vi har opptjent verdien vi har betalt for. "
    "Estimate at Completion (EAC) konvergerte mot BAC fra måned 1, og Variance at Completion "
    "(VAC) er null ved slutten.",
    story)

h2("2.4  Kvalitet")
body(
    "Ferdigbefaringen (BP3) i april 2026 ble gjennomført med null kritiske mangler — "
    "kravspesifikasjonens K-001 er dermed oppfylt. FDV-dokumentasjonen er overlevert samlet, "
    "i tråd med K-002. Brannvesenets vurdering av de oppgraderte sprinkler- og rømningsløsningene "
    "fra CR-001 er positiv, og brukstillatelse er innvilget i god tid før skolestart høsten 2026.",
    story)


# ============================================================
# 3. EARNED VALUE
# ============================================================
h1("3   Earned Value Management — sluttanalyse")
body(
    "EVM-resultatet for hele gjennomføringsfasen vises i S-kurven nedenfor. Planned Value (PV) "
    "er beregnet som Baseline 1 lineært fordelt over hver pakkes varighet. Earned Value (EV) er "
    "BAC multiplisert med faktisk fullføringsgrad per pakke, aggregert. Actual Cost (AC) er "
    "direkte hentet fra kumulativ påløpt aktivitetskost i månedsreferatene.",
    story)

figure(FIGURER / "figur_01_s_kurve.png", story, "3.1",
       "S-kurven — kumulativ PV / EV / AC for hele gjennomføringsfasen. De tre realiserte "
       "risikoene er markert. Sluttverdier: PV = EV = AC = 800 MNOK.")

body(
    "Tre observasjoner fra S-kurven er sentrale. PV, EV og AC er nært sammenfallende gjennom "
    "hele forløpet — prosjektet har styrt mot Baseline 1 med høy presisjon. Det tydelige "
    "knekkpunktet rundt måned 7 markerer oppstart av råbyggsperioden, hvor månedlig kostnadsforbruk "
    "økte fra cirka 25 MNOK til over 60 MNOK i tråd med crashing-vedtaket. Og den relativt høye "
    "SPI-verdien i de første månedene (1,15–1,25) skyldes at detaljprosjektering ble fullført "
    "raskere enn lineær fordeling skulle tilsi — en metodisk effekt av PV-modelleringen, ikke "
    "en faktisk forsering.",
    story)

tabell_caption("3.1", "EVM-sluttverdier ved overlevering 15. mai 2026.", story)
evm_tab = make_table([
    ["KPI", "Verdi", "Formel"],
    ["BAC", "800,0 MNOK", "Baseline 1 etter NHB-2026-15"],
    ["PV (kum.)", "800,0 MNOK", "Σ BAC_pakke (lineær fordeling)"],
    ["EV (kum.)", "800,0 MNOK", "Σ BAC_pakke × 100 %"],
    ["AC (kum.)", "800,0 MNOK", "Σ påløpt mnd 1–16"],
    ["CPI", "1,000", "EV / AC"],
    ["SPI", "1,000", "EV / PV"],
    ["EAC", "800,0 MNOK", "BAC / CPI"],
    ["VAC", "0,0 MNOK", "BAC − EAC"],
    ["Risikoreserve brukt", "11 av 50 MNOK", "R-05 (6) + R-06/CR-001 (5)"],
    ["Tidsbuffer brukt", "1,5 av 8 uker", "R-07"],
], col_widths=[4 * cm, 3.5 * cm, 8 * cm])
story.append(evm_tab)


# ============================================================
# 4. ENDRINGSSTYRING OG HENDELSER
# ============================================================
h1("4   Endringsstyring og hendelser")
body(
    "Prosjektets to formelle endringer og tre realiserte risikoer er behandlet med "
    "konsekvensanalyse og dokumentasjon i tråd med PMBOK-prinsippene om integrated change "
    f"control {sit('Project Management Institute', '2021', '113')}.",
    story)

h2("4.1  NHB-2026-15 — Schedule crashing av 4.1 Råbygg")
body(
    "Detaljprosjektering avdekket at arbeidspakke 4.1 Råbygg var underestimert i Baseline 0 "
    "med +50 MNOK og +2 måneder. Aktiviteten ligger på prosjektets kritiske vei. Uten "
    "korrigerende tiltak ville prosjektet samtidig brutt tids- og kostnadsrammen. Etter "
    "vurdering av tre alternativer vedtok kommunestyret 7. mai 2026 å komprimere aktiviteten "
    "fra 7 til 5 måneders varighet, mot en tilleggskostnad på 50 MNOK. Budsjettrammen ble "
    "utvidet fra 700 til 800 MNOK, hvilket inkluderer både den avdekkede overskridelsen "
    "(50 MNOK) og selve crashing-tiltaket (50 MNOK).",
    story)

h2("4.2  CR-001 — DSB-veileder for sprinkler og rømning")
body(
    "I februar 2026 publiserte Direktoratet for samfunnssikkerhet og beredskap (DSB) oppdatert "
    "veileder for sprinklerdekning og rømningsskilting i kommunale byggeprosjekter. Endringen "
    "kunne ikke ignoreres uten å risikere at skolen ikke ville få brukstillatelse. Endringsforespørselen "
    "ble vedtatt 3. februar 2026 på teamledermøtet i måned 13. Scope på arbeidspakke 5.1 VVS ble "
    "utvidet. Tilleggskostnaden på 5,0 MNOK ble dekket fra risikoreserven, og 1 uke forsinkelse "
    "ble absorbert i tidsbufferen. BAC ble dermed ikke endret.",
    story)

h2("4.3  Realiserte risikoer")
body(
    "Tre av 16 identifiserte risikoer ble realisert gjennom gjennomføringsfasen. Tabell 4.1 "
    "viser håndteringen av hver.",
    story)

tabell_caption("4.1", "Realiserte risikoer i gjennomføringsfasen.", story)
risiko_tab = make_table([
    ["ID", "Måned", "Hendelse", "Kostnad", "Tid", "Respons"],
    ["R-05", "Mnd 4 (mai 2025)",
     "Forurenset masse / oljetank under 3.2 Riving",
     "6 MNOK", "1 uke",
     "Risikoreserve. Forsinkelse absorbert i slack. Statsforvalter varslet."],
    ["R-07", "Mnd 11 (des 2025)",
     "Brann hos vindusprodusent — forsinker 4.1 Råbygg",
     "0", "1,5 uker",
     "Tidsbuffer. Etterfølgende arbeider replanlagt for å begrense kaskade."],
    ["R-06 / CR-001", "Mnd 13 (feb 2026)",
     "DSB-veileder oppgraderer sprinkler/rømning",
     "5 MNOK", "1 uke",
     "Risikoreserve + tidsbuffer. Formell endring CR-001 vedtatt."],
], col_widths=[2.5 * cm, 2.5 * cm, 4.5 * cm, 1.5 * cm, 1.3 * cm, 5.2 * cm])
story.append(risiko_tab)


# ============================================================
# 5. BUSINESS CASE
# ============================================================
h1("5   Business case og gevinstrealisering")
body(
    "Prosjektforslagets opprinnelige business case anslo en netto nåverdi (NNV) på +109,2 MNOK "
    "over 60 år ved 1 % realrente, et Benefit-Cost Ratio (BCR) på 1,16 og en Return on Investment "
    f"(ROI) på 15,6 % {sit('Hædda kommune', '2025a', '38')}. Effektmålene var 30 % reduksjon i "
    "driftskostnader per elev (anslått besparelse om lag 18 MNOK/år) og 20 % økning i programareal "
    "per elev sammenlignet med eksisterende skoler.",
    story)
body(
    "Disse målene er forankret i den leverte løsningen gjennom BREEAM Very Good-sertifisering, "
    "balansert ventilasjon med varmegjenvinning og et beregnet energiforbruk under 75 kWh/m²/år. "
    "Reell måloppnåelse kan først dokumenteres 12–24 måneder etter ibruktagelse, når faktiske "
    "drifts- og energidata er sammenlignbare med utgangspunktet.",
    story)
body(
    "Kostnadsutvidelsen fra NHB-2026-15 (700 → 800 MNOK) forskyver tilbakebetalingstiden, "
    "men gjør ikke business casen netto negativ. Et oppdatert anslag av NNV gir om lag +59 MNOK "
    "ved 1 % realrente, som tilsvarer omtrent halvparten av opprinnelig estimat. Det understreker "
    "at crashing-vedtaket var en avveiing mellom dårlig business case og dårligere "
    "samfunnskonsekvens — ikke et fritt valg.",
    story)


# ============================================================
# 6. LÆRINGSPUNKTER
# ============================================================
h1("6   Læringspunkter og erfaringsoverføring")
body(
    "Fire læringspunkter trekker vi fram som mest sentrale for å overføre erfaringen fra dette "
    "prosjektet til fremtidige byggeprosjekter i Hædda kommune.",
    story)

h3("6.1  Endringer som ikke dokumenteres formelt blir usynlige")
body(
    "Den viktigste innsikten fra prosjektet er konkret: endringer må ha eget dokument med "
    "konsekvensanalyse. NHB-2026-15 og CR-001 har hver sitt endringsdokument med vurdering "
    "av omfang, tid, kostnad, kvalitet og risiko. Det er disse dokumentene som gjør at "
    "sluttrapporten kan argumentere etterprøvbart for hvorfor sluttkost er 800 MNOK og ikke "
    "700, og hvorfor scope på 5.1 VVS ble utvidet. Uten dokumentasjonen ville argumentet "
    "vært muntlig — og dermed angripelig.",
    story)

h3("6.2  Baseline-disiplin gjør hele endringshistorikken etterprøvbar")
body(
    "Vi bevarte både Baseline 0 (opprinnelig plan før crashing) og Baseline 1 (godkjent etter "
    "NHB-2026-15) i MS Project. Denne disiplinen gjør at sluttrapporten kan vise hele "
    "forløpet: fra opprinnelig estimat via dokumentert endring til revidert plan og faktisk "
    "gjennomføring. Uten parallell baseline-disiplin ville «før»-tilstanden gått tapt.",
    story)

h3("6.3  Earned Value Management gir objektiv status uavhengig av subjektive vurderinger")
body(
    "CPI og SPI har gjennom prosjektet gitt oss et målbart bilde av status som er uavhengig "
    "av subjektive vurderinger fra leverandører eller team. I månedene rundt 4.1 Råbygg, hvor "
    "det subjektive bildet var preget av høyt aktivitetsnivå og krevende koordinering, viste "
    "EVM at vi faktisk leverte iht. Baseline 1. Det er en disiplin vi anbefaler kommunen "
    "å innføre som standard i alle prosjekter over en viss størrelse.",
    story)

h3("6.4  Tidsbuffer er et reelt styringsinstrument, ikke en akademisk reserve")
body(
    "R-07 (brann hos vindusprodusent) viste verdien av å ha satt av 8 uker tidsbuffer i "
    "planfasen. Da risikoen materialiserte seg, transformerte tidsbufferen en potensiell krise "
    "til en planlagt justering uten kostnadskonsekvens. På beslutningstidspunktet for "
    "tidsbufferen — i planleggingsfasen — så det ut som en triviell reserveallokasjon. "
    "I praksis var det den mekanismen som forhindret kaskadeforsinkelse.",
    story)


# ============================================================
# 7. ANBEFALINGER
# ============================================================
h1("7   Anbefalinger til oppdragsgiver")
body(
    "Fire prioriterte anbefalinger gjelder for tiden etter overlevering.",
    story)

h3("7.1  Gevinstoppfølging med årlig kadens")
body(
    "Business case-anslaget på +59 MNOK netto nåverdi realiseres kun gjennom faktisk drift "
    "av skolen. Driftsorganisasjonen bør utarbeide en gevinstrealiseringsplan med måltall for "
    "driftskostnad per elev, energiforbruk per kvadratmeter, og brukertilfredshet hos ansatte "
    "og elever. Kadensen bør være årlig de første tre årene, med kommunestyret som "
    "beslutningsforum for justeringer.",
    story)

h3("7.2  Årlig sikkerhetsvurdering av CR-001-løsninger")
body(
    "De oppgraderte sprinkler- og rømningsløsningene som ble innført i CR-001 bør gjennomgås "
    "av brannvesenet hvert år de første tre årene. Dette sikrer at kommunens etterlevelse av "
    "DSB-kravene holder seg, og at eventuelle senere veilederrevisjoner fanges opp tidlig.",
    story)

h3("7.3  Erfaringsoverføring til kommunens prosjektmal")
body(
    "NHB-2026-15 og CR-001 er konkrete eksempler på schedule crashing og regulatorisk "
    "scope-endring. Vi anbefaler at kommunen innarbeider disse som referansecase i sin "
    "interne prosjektledelsesmal og fremtidige opplæringer.",
    story)

h3("7.4  Oppfølgende brukeropplæring etter seks måneder")
body(
    "Den bygde løsningen omfatter avanserte tekniske systemer — særlig automasjon (SD-anlegg) "
    "og IKT/sikkerhet. Initial brukeropplæring er gjennomført i måned 16, men erfaringsmessig "
    "er det først etter et halvår med drift at de virkelige opplæringsbehovene melder seg. "
    "En oppfølgende opplæringsbolk etter seks måneders drift anbefales, særskilt rettet mot "
    "driftspersonalets kompetanse på SD-anlegget og adgangskontrollsystemet.",
    story)


# ============================================================
# 8. VEDLEGG
# ============================================================
h1("Vedleggsliste")
body(
    "Denne sluttrapporten er en fokusert leveranse for avslutningsfasen. For omfattende "
    "behandling av planlegging, gjennomføring og avslutning samlet, se:",
    story)
bullet_list([
    "<b>Komplett prosjektrapport - Nye Hædda Barneskole.pdf</b> "
    "(mappen 05 - Endelig innlevering Hædda Barneskole/) — hovedleveransen, 35 sider med "
    "syntese av alle faser, 10 figurer og detaljert EVM-analyse.",
    "<b>00 - Les meg først.pdf</b> (i prosjektroten) — leseguide til hele mappestrukturen.",
    "<b>16 månedsrapporter</b> (mappen 03 - Gjennomføring/Månedsrapporter/) — med S-kurver, "
    "EVM, avvik og risikoer per måned.",
    "<b>2 endringsdokumenter</b> (mappen 03 - Gjennomføring/Endringsdokumenter/) — NHB-2026-15 "
    "og CR-001 med full konsekvensanalyse.",
    "<b>Bårds kildemateriale</b> (mappen Vedlegg/A - Kildemateriale fra Bård/) — "
    "godkjenning-av-budsjettendring.pdf, månedsrapporter.pdf og simulerte WBS-data.",
], story)


# ============================================================
# REFERANSER
# ============================================================
h1("Referanser")
refs = [
    ref("Direktoratet for samfunnssikkerhet og beredskap", "2026",
        "Veileder for sprinklerdekning og rømningsskilting i kommunale byggeprosjekter",
        "DSB-publikasjon, henvist i CR-001"),
    ref("Hædda kommune", "2025a",
        "Prosjektforslag — Nye Hædda Barneskole",
        "Kommunestyresak, mappen 01 - Initiering"),
    ref("Hædda kommune", "2025b",
        "Konseptløsning — Nye Hædda Barneskole",
        "Kommunestyresak, mappen 01 - Initiering"),
    ref("Høgskolen i Molde", "2026",
        "Sensorveiledning — LOG565 Prosjektledelse 2",
        "Faglig vurderingsgrunnlag for mappeinnleveringen"),
    ref("Project Management Institute", "2021",
        "A guide to the Project Management Body of Knowledge (PMBOK Guide) (7. utg.)",
        "Project Management Institute"),
]
for r in refs:
    story.append(Paragraph(r, ST_REFERENCE))


print("Bygger PDF...")
doc.build(story, canvasmaker=canvas_maker)
print(f"PDF lagret: {OUT}")
