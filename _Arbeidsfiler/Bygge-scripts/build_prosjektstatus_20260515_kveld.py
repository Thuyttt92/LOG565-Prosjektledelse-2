# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-15 (kveld) — Fase 3 ferdigstilt.

Erstatter morgenens PROSJEKTSTATUS_2026-05-15.pdf med en helhetlig sluttstatus
for dagen, etter at fase 3 (gjennomføring) og fase 4 (sluttrapport) er bygd opp.
"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer

from _status_style import (
    build_doc, hero_block, info_card, section_header, section_rule,
    make_table, status_badge,
    ST_BODY, ST_H3, ST_LEAD, ST_HIGHLIGHT, ST_INFO, ST_NOTE,
)

OUT = (
    r"C:\Users\Gusta\OneDrive\Documents\Privat\Studier\Bachelore i Logistikk\LOG565 - Prosjektledelse"
    r"\Gruppe 4.5 møter\PROSJEKTSTATUS_2026-05-15.pdf"
)
PROJECT_LABEL = "LOG565 — Nye Hædda barneskole — Gruppe 4.5"

doc, on_page = build_doc(OUT, "Prosjektstatus 15.05.2026 — fase 3 ferdig", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Prosjektstatus — kveld",
    subtitle="Fase 3 (gjennomføring) og fase 4 (sluttrapport) bygd opp i dag",
    date_label="Status pr. 15. mai 2026, kveld",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda barneskole — fiktiv skole for 600 elever"],
    ["Vurderingsform", "Mappeinnlevering, 100 % av karakter"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow (17 dager igjen)"],
    ["Mål", "A-nivå (90–100 poeng)"],
    ["Forrige status", "Tidligere i dag (morgen: Gantt-bygget)"],
]))
story.append(Spacer(1, 0.4 * cm))

# === 1. HOVEDPOENG ===
story.append(section_header(1, "Hovedpoeng — fase 3 og 4 bygget opp"))
story.append(section_rule())
story.append(Paragraph(
    "Bård leverte de to siste vedleggene i Teams i ettermiddag — <b>godkjenning-av-budsjettendring.pdf</b> "
    "(kommunestyrets vedtak NHB-2026-15 om rammeutvidelse 700 → 800 MNOK) og <b>månedsrapporter.pdf</b> "
    "(16 teamledermøtereferater for hele gjennomføringsfasen). Med disse på plass har vi i dag "
    "<b>fullført hele fase 3 (gjennomføring) og fase 4 (sluttrapport) som dokumentasjon</b> — alt unntatt "
    "selve MS Project tracking-arbeidet, som leveres som detaljert instruks med eksakte verdier.",
    ST_LEAD))
story.append(Paragraph(
    "Sentral innsikt fra Bårds rådata: <b>crashing av 4.1 Råbygg er allerede applisert i Baseline 1</b> "
    "(kommunestyret har gitt fullmakt). Vår jobb er å dokumentere endringen, ikke å gjennomføre den. "
    "Tre risikohendelser ble realisert (R-05 forurenset masse mnd 4, R-07 brann hos vindusprodusent "
    "mnd 11, R-06/CR-001 DSB sprinkler/rømning mnd 13). Sluttkost: 800 MNOK på prikken (CPI=1.000), "
    "sluttdato 15.05.2026 holdt (SPI=1.000, 1.5 av 8 uker tidsbuffer brukt).",
    ST_BODY))

# === 2. DAGENS LEVERANSER ===
story.append(section_header(2, "Dagens leveranser — fase 3"))
story.append(section_rule())

leveranser = [
    ["Leveranse", "Fil(er)", "Status"],
    ["Endringsdokument NHB-2026-15 (crashing)",
     "03 - Gjennomføring/Endringsdokument NHB-2026-15 - Schedule crashing.docx",
     status_badge("OK", "ok")],
    ["Endringsdokument CR-001 (sprinkler)",
     "03 - Gjennomføring/Endringsdokument CR-001 - Sprinkler-romning.docx",
     status_badge("OK", "ok")],
    ["EVM-arbeidsbok (KPI-er + S-kurve)",
     "03 - Gjennomføring/EVM-arbeidsbok - Nye Hædda barneskole.xlsx",
     status_badge("OK", "ok")],
    ["16 S-kurve PNG-er (én per måned)",
     "Arbeidsfiler/s_kurver/s_kurve_mnd_01–16.png",
     status_badge("OK", "ok")],
    ["16 månedsrapporter (docx + PDF)",
     "03 - Gjennomføring/Månedsrapporter/Månedsrapport mnd 01–16.{docx,pdf}",
     status_badge("OK", "ok")],
    ["MS Project tracking-instruks",
     "03 - Gjennomføring/MS Project tracking-instruks.xlsx",
     status_badge("OK", "ok")],
    ["Sluttrapport (oppdatert med faktiske sluttall)",
     "04 - Avslutning/Sluttrapport - Nye Hædda barneskole.{docx,pdf}",
     status_badge("OK", "ok")],
]
story.append(make_table(leveranser, col_widths=[6 * cm, 8 * cm, 2.5 * cm], badge_col=2))

# === 3. SLUTTTALL FRA FASE 3 ===
story.append(section_header(3, "Sluttall — fase 3 (EVM)"))
story.append(section_rule())
story.append(Paragraph(
    "Alle tall er sporbare til Bårds <i>månedsrapporter.pdf</i> via vår master datastruktur "
    "<font name='Courier'>Arbeidsfiler/log565_master_data.py</font>.",
    ST_BODY))

slutttall = [
    ["KPI", "Verdi", "Mot ramme"],
    ["BAC (Baseline 1)", "800 MNOK", "Vedtatt NHB-2026-15"],
    ["AC kum. ved slutt", "800,0 MNOK", "På prikken"],
    ["EV kum. ved slutt", "800,0 MNOK", "100 % fullført"],
    ["CPI ved slutt", "1.000", "Innenfor budsjett"],
    ["SPI ved slutt", "1.000", "Iht. plan"],
    ["Risikoreserve brukt", "11 MNOK", "av godkjent 50 MNOK (22 %)"],
    ["Tidsbuffer brukt", "1,5 uker", "av godkjent 8 uker (19 %)"],
    ["Sluttdato (faktisk)", "15.05.2026", "På datoen — frist holdt"],
    ["Antall hendelser realisert", "3 av registrerte risikoer", "R-05, R-06/CR-001, R-07"],
]
story.append(make_table(slutttall, col_widths=[6 * cm, 4 * cm, 6.5 * cm]))

# === 4. ENDRINGSSTYRING — SENTRALT FOR A ===
story.append(section_header(4, "Endringsstyring — kjernebevis for A"))
story.append(section_rule())
story.append(Paragraph(
    "Sensorveiledningen sier eksplisitt at gjennomføringsfasen skal være <i>reell, med baseline, "
    "tracking, hendelser, endringer og oppfølging dokumentert</i>. Vi har nå to formelle "
    "endringer dokumentert med full konsekvensanalyse:",
    ST_BODY))
endringer = [
    ["ID", "Tittel", "Pakke", "Kost", "Tid", "Beslutter"],
    ["NHB-2026-15",
     "Komprimering 4.1 Råbygg + rammeutvidelse",
     "4.1 Råbygg",
     "+100 MNOK",
     "–2 mnd",
     "Kommunestyret"],
    ["CR-001",
     "DSB-veileder sprinkler/rømning",
     "5.1 VVS",
     "+5 MNOK (RR)",
     "+1 uke (TB)",
     "Prosjekteier"],
]
story.append(make_table(endringer, col_widths=[3.2 * cm, 5.5 * cm, 2.3 * cm, 2.6 * cm, 1.8 * cm, 2.6 * cm]))

# === 5. SPORBARHET ===
story.append(section_header(5, "Sporbarhet — referat → rapport → MS Project"))
story.append(section_rule())
story.append(Paragraph(
    "Sporbarhet er det sensor ser etter (eksplisitt nevnt som en \"typisk svakhet\" "
    "i sensorveiledningen kap. 8). Vi har QA-verifisert eksakt sporbarhet for 5 stikkmåneder:",
    ST_BODY))
sporbarhet = [
    ["Mnd", "Hendelse i Bårds referat", "I månedsrapport (avvik-tab)", "Status"],
    ["1", "Ingen hendelse", "ISS ID — | Ingen avvik", status_badge("OK", "ok")],
    ["4", "R-05 forurenset masse, 6 MNOK, 1 uke", "ISS-04-01 (R-05) | 6,0 MNOK / 1,0 uke", status_badge("OK", "ok")],
    ["11", "R-07 brann vindusprodusent, 0 MNOK, 1,5 uker", "ISS-11-01 (R-07) | 0 MNOK / 1,5 uker", status_badge("OK", "ok")],
    ["13", "R-06 sprinkler / CR-001, 5 MNOK, 1 uke", "ISS-13-01 (R-06 / CR-001) | 5 MNOK / 1 uke", status_badge("OK", "ok")],
    ["16", "Ingen hendelse", "ISS ID — | Ingen avvik", status_badge("OK", "ok")],
]
story.append(make_table(sporbarhet, col_widths=[1.2 * cm, 6 * cm, 7.4 * cm, 2 * cm], badge_col=3))

# === 6. ESTIMERT POENGSCORE ===
story.append(section_header(6, "Estimert score mot sensorveiledningen"))
story.append(section_rule())
story.append(Paragraph(
    "Etter dagens arbeid er fase 3 (35 poeng) og fase 4 (10 poeng) i hovedsak dekket. "
    "Det eneste manuelle arbeidet som gjenstår er MS Project tracking-input (eksakt instruks "
    "levert som xlsx).",
    ST_BODY))
score = [
    ["Område", "Maks", "Morgen", "Kveld", "Etter MS Project + finpuss"],
    ["A. Planleggingsfasen", "40", "~36", "~36", "~37"],
    ["B. Gjennomføringsfasen", "35", "0", "~30", "~33"],
    ["    — MS Project tracking", "(10)", "0", "0", "~9 (når MS Project er fylt inn)"],
    ["    — Månedsrapporter", "(12)", "0", "~12", "~12"],
    ["    — Endringsstyring", "(8)", "0", "~7", "~7"],
    ["    — Problemliste", "(5)", "0", "~3", "~5 (oppgraderes)"],
    ["C. Avslutningsfasen", "10", "0", "~8", "~9"],
    ["D. Sporbarhet og profesjonalitet", "15", "~10", "~13", "~14"],
    ["TOTALT (estimert)", "100", "~46", "~87", "~93"],
]
story.append(make_table(score, col_widths=[5.6 * cm, 1.4 * cm, 1.6 * cm, 1.6 * cm, 5.8 * cm]))
story.append(Paragraph(
    "<b>Mål A (90+) er nå realistisk innenfor rekkevidde</b>. Største gjenværende risiko er "
    "MS Project tracking-input — uten reell baseline+tracking i .mpp-fila trekkes 10 poeng (sperre).",
    ST_HIGHLIGHT))

# === 7. NESTE STEG ===
story.append(section_header(7, "Neste steg"))
story.append(section_rule())
neste = [
    ["Når", "Hva", "Status"],
    ["Snart",
     "Åpne MS Project, sett Baseline 0 → crash 4.1 Råbygg → sett Baseline 1. "
     "Bruk 'MS Project tracking-instruks.xlsx' som referanse. Estimert tid: 1–2 timer.",
     status_badge("NESTE", "pending")],
    ["Etter MS Project",
     "Eksporter Tracking-Gantt som PNG og lim inn på 'Figur 1'-plass i hver av de 16 "
     "månedsrapportene. Regenerer PDF-er.",
     status_badge("VENTER", "info")],
    ["Før innlevering",
     "Oppgradere problemliste til samme detaljnivå som månedsrapportene (5 poeng).",
     status_badge("PLAN", "info")],
    ["Før innlevering",
     "Endelig korrekturlesning av alle PDF-er.",
     status_badge("PLAN", "info")],
    ["1. juni 15:00",
     "Innlevering i WiseFlow.",
     status_badge("MÅL", "pending")],
]
story.append(make_table(neste, col_widths=[3 * cm, 11.5 * cm, 2 * cm], badge_col=2))

# === 8. TIL GRUPPEN ===
story.append(section_header(8, "Til resten av gruppen"))
story.append(section_rule())
story.append(Paragraph(
    "Alle de tunge gjennomføringsfase-leveransene er nå på plass: 16 månedsrapporter med "
    "S-kurve, EVM-tall og avviksanalyse; 2 endringsdokumenter med konsekvensvurdering; "
    "EVM-arbeidsbok; oppdatert sluttrapport. Vi har bygget en master datakilde "
    "(<font name='Courier'>Arbeidsfiler/log565_master_data.py</font>) som er den eneste "
    "sannhetskilden — alle rapporter er generert fra den.",
    ST_BODY))
story.append(Paragraph(
    "Det som gjenstår av selvstendig arbeid for hver enkelt er MS Project tracking-input. "
    "Det er konseptuelt viktig — sensor sjekker at .mpp-fila reflekterer hele endringshistorikken. "
    "Bruk 'MS Project tracking-instruks.xlsx' (5 ark med eksakte verdier) som referanse mens "
    "dere oppdaterer Gantt-fila. Det tar ca. 1–2 timer.",
    ST_BODY))

story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Vi har gått fra ~46 estimerte poeng i morges til ~87 nå, med en realistisk vei til ~93 "
    "etter MS Project og finpuss. A-nivå er innen rekkevidde. Si fra på Teams hvis noe er uklart.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
