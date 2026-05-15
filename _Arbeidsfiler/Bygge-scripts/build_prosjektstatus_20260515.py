# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-15 (omarbeidet med ny stilmal) — Gantt bygget."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak

from _status_style import (
    build_doc, hero_block, info_card, section_header, section_rule,
    make_table, status_badge,
    ST_BODY, ST_H3, ST_LEAD, ST_MUTED, ST_HIGHLIGHT, ST_INFO, ST_NOTE,
)

OUT = (
    r"C:\Users\Gusta\OneDrive\Documents\Privat\Studier\Bachelore i Logistikk\LOG565 - Prosjektledelse"
    r"\Gruppe 4.5 møter\PROSJEKTSTATUS_2026-05-15.pdf"
)
PROJECT_LABEL = "LOG565 — Nye Hædda barneskole — Gruppe 4.5"

doc, on_page = build_doc(OUT, "Prosjektstatus 15.05.2026", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Prosjektstatus",
    subtitle="LOG565 Prosjektledelse 2 — Gantt-diagrammet er bygget",
    date_label="Status pr. 15. mai 2026",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda barneskole — fiktiv skole for 600 elever"],
    ["Vurderingsform", "Mappeinnlevering, 100 % av karakter"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow"],
    ["Mål", "A-nivå (90–100 poeng)"],
    ["Forrige status", "5. mai 2026 (10 dager siden)"],
]))
story.append(Spacer(1, 0.4 * cm))

# === 1. HOVEDPOENG ===
story.append(section_header(1, "Hovedpoeng i dag"))
story.append(section_rule())
story.append(Paragraph(
    "Vi har <b>bygget Gantt-diagrammet i MS Project</b> basert på Bårds simulerte WBS. "
    "Filen ligger i prosjektets rotmappe som "
    "<font name='Courier'>Hædda barneskole GANTT.mpp</font>. "
    "Total kostnad er bekreftet til <b>750 millioner kroner</b> — som matcher Bårds simulering "
    "eksakt — og sluttdatoen er 8. mai 2026, som ligger innenfor den harde fristen 15. mai 2026.",
    ST_LEAD))
story.append(Paragraph(
    "Mellom forrige status (5. mai) og i dag har det vært en pause på 10 dager. Arbeidet i dag har "
    "vært fokusert på selve Gantt-byggingen. Vi har valgt manuell innskriving fremfor "
    "Excel-import fordi importveiviseren ikke fungerte stabilt — manuell innskriving ga oss "
    "bedre kontroll på resultatet og gjorde det enklere å feilsøke underveis.",
    ST_BODY))

# === 2. STATUS GANTT ===
story.append(section_header(2, "Status — Gantt-diagram"))
story.append(section_rule())

gantt_status = [
    ["Parameter", "Verdi", "Status"],
    ["Antall aktiviteter", "44 (40 oppgaver + 4 milepæler)", status_badge("OK", "ok")],
    ["Startdato", "01.02.2025", status_badge("OK", "ok")],
    ["Sluttdato", "08.05.2026 (innenfor frist 15.05.2026)", status_badge("OK", "ok")],
    ["Total kostnad", "750 000 000 kr", status_badge("OK", "ok")],
    ["Innrykk / sammendragslinjer", "8 hovedgrener, 36 underaktiviteter", status_badge("OK", "ok")],
    ["Foregangsoppgaver", "Satt på 32 aktiviteter", status_badge("OK", "ok")],
    ["Kritisk linje", "Aktivert (Format → Kritiske oppgaver)", status_badge("OK", "ok")],
    ["Basisplan 0", "Settes nå (siste steg)", status_badge("VENTER", "pending")],
    ["PNG-eksport av Gantt", "Lagres i 02 - Planlegging/", status_badge("VENTER", "pending")],
]
story.append(make_table(gantt_status, col_widths=[5.5 * cm, 8.5 * cm, 2.5 * cm], badge_col=2))

story.append(Paragraph(
    "<b>Merk:</b> Bårds simulering antok en sluttdato i juli 2026 (~6 uker etter fristen). "
    "Vår Gantt slutter 8. mai 2026 — innenfor fristen. Forskjellen skyldes hvordan parallelle "
    "aktiviteter sekvenseres i MS Project. Kostnadsoverskridelsen (750 vs budsjettramme 700) "
    "består uansett, og det er denne som skal løses med <i>schedule crashing</i> når Bård "
    "sender gruppespesifikk instruks i Teams.",
    ST_INFO))

# === 3. DAGENS LØP ===
story.append(section_header(3, "Det vi har gjort i dag"))
story.append(section_rule())

story.append(Paragraph("3.1 Ny manuell innskrivingsguide", ST_H3))
story.append(Paragraph(
    "Den opprinnelige Excel-importmetoden i MS Project lot seg ikke gjennomføre i praksis. "
    "Vi har derfor laget en ny detaljert guide for manuell innskriving av alle 44 rader, "
    "med korte forklaringer på <i>hvorfor</i> hvert steg gjøres. Guiden er bygget for å være "
    "lett å følge selv i lav-energi-tilstand — én ting om gangen, gule 'Hvorfor:'-bokser med "
    "fagforklaringer, og grønne pause-tips mellom seksjonene.",
    ST_BODY))
guides = [
    ["Hva", "Hvor"],
    ["Ny manuell innskrivingsguide (PDF, 12 sider)",
     "02 - Planlegging/GANTT - Manuell innskriving (enkel guide).pdf"],
    ["Opprinnelig importguide (PDF) — beholdt som backup",
     "02 - Planlegging/GANTT_BYGGE_GUIDE_NORSK.pdf"],
    ["MS Project-fil med Gantt-data",
     "Hædda barneskole GANTT.mpp (rotmappe)"],
]
story.append(make_table(guides, col_widths=[7.5 * cm, 9 * cm]))

story.append(Paragraph("3.2 To feil oppdaget og rettet underveis", ST_H3))
story.append(Paragraph(
    "Etter første runde med innskriving avdekket statistikken to klare avvik. Begge ble "
    "diagnostisert via skjermbilder og rettet:",
    ST_BODY))
feil = [
    ["Feil", "Symptom", "Årsak", "Løsning"],
    ["Kostnad dobbelt",
     "Total kostnad viste 1 482 mill (skulle vært 750)",
     "Fast kostnad var skrevet både på sammendragslinjer og underaktiviteter",
     "Satt Fast kostnad = 0 på de 8 sammendragsradene"],
    ["Rad 33 — 0,05 mnd",
     "Spesialutstyr ble 1 dag i stedet for 10 dager",
     "Norsk MS Project bruker komma som desimalseparator; '0.5' ble tolket som '0,05'",
     "Endret til '0,5' (med komma)"],
    ["Manuell planlegging",
     "Spørsmålstegn (?) i varighetsfeltet på rad 10, 31, 33",
     "Noen oppgaver var ikke satt som 'Automatisk planlagt'",
     "Markerte alle rader → Oppgave → Automatisk planlegging"],
]
story.append(make_table(feil, col_widths=[3 * cm, 4 * cm, 5 * cm, 4.5 * cm]))
story.append(Paragraph(
    "Disse erfaringene er verdt å ha med seg hvis flere i gruppen bygger egen Gantt: "
    "(1) bruk komma som desimalskille i norsk MS Project; (2) sett alle oppgaver til 'Automatisk "
    "planlagt' før du begynner; (3) sammendragslinjer skal IKKE ha egen Fast kostnad — "
    "underaktivitetenes kostnader summeres automatisk i 'Kostnad'-kolonnen.",
    ST_NOTE))

# === 4. SENSORVEILEDNINGEN ===
story.append(section_header(4, "Status mot sensorveiledningen"))
story.append(section_rule())
story.append(Paragraph(
    "Etter dagens arbeid er Gantt-leveransen på plass. Dette løfter A-områdets delpoeng "
    "vesentlig — Gantt-diagrammet alene utgjør 12 av 40 poeng i planleggingsfasen.",
    ST_BODY))
sensor = [
    ["Område", "Maks", "Forrige", "I dag", "Etter fase 3+4"],
    ["A. Planleggingsfasen", "40", "~17", "~36", "—"],
    ["B. Gjennomføringsfasen", "35", "0", "0", "~31"],
    ["C. Avslutningsfasen", "10", "0", "0", "~9"],
    ["D. Sporbarhet og profesjonalitet", "15", "~9", "~10", "~13"],
    ["TOTALT (estimert)", "100", "~26", "~46", "~89"],
]
story.append(make_table(sensor, col_widths=[6 * cm, 2.0 * cm, 2.0 * cm, 2.0 * cm, 4.5 * cm]))
story.append(Paragraph(
    "Estimert sluttkarakter ligger fortsatt på <b>B/A-grensen (88–92 poeng)</b>. For å lande "
    "klart på A trenger vi nå: (a) Baseline 0 satt og PNG eksportert (i dag), "
    "(b) crashing-saken dokumentert når Bård sender instruks via Teams, (c) fase 3 med "
    "reell tracking og månedsrapporter (S-kurve + EVM), (d) sluttrapport som analyserer "
    "crashing-saken som læringspunkt.",
    ST_BODY))

# === 5. NESTE STEG ===
story.append(section_header(5, "Neste steg"))
story.append(section_rule())
neste = [
    ["Når", "Hva", "Status"],
    ["I dag",
     "Sette Basisplan 0 i MS Project (Prosjekt → Angi basisplan).",
     status_badge("NÅ", "pending")],
    ["I dag",
     "Eksportere PNG av Gantt til 02 - Planlegging/Gantt - Baseline 0 - Opprinnelig estimat.png.",
     status_badge("NÅ", "pending")],
    ["Når Bård sender crashing-instruks",
     "Fylle ut endringsdokument CR-001 + sette Basisplan 1.",
     status_badge("VENTER", "info")],
    ["17. mai",
     "Fase 2 låst — komplett prosjektplan sendes til Bård for godkjenning.",
     status_badge("PLAN", "info")],
    ["18.–26. mai",
     "Fase 3: simulert tracking, månedsrapporter med S-kurve og EVM.",
     status_badge("PLAN", "info")],
    ["27.–29. mai",
     "Fase 4: sluttrapport med analyse og refleksjon.",
     status_badge("PLAN", "info")],
    ["1. juni 15:00",
     "Innlevering i WiseFlow.",
     status_badge("MÅL", "pending")],
]
story.append(make_table(neste, col_widths=[3.5 * cm, 10.8 * cm, 2.2 * cm], badge_col=2))

# === 6. TIL GRUPPEN ===
story.append(section_header(6, "Til resten av gruppen"))
story.append(section_rule())
story.append(Paragraph(
    "Den manuelle innskrivingsguiden er bygget slik at hver av oss kan gjøre øvelsen selv uten "
    "å være avhengig av importfunksjonen. Det tar ca. 45 minutter, og det gir solid trening i "
    "MS Project — et verktøy vi alle bør ha forsøkt minst én gang før vi er ferdige med studiet. "
    "Følg <font name='Courier'>02 - Planlegging/GANTT - Manuell innskriving (enkel guide).pdf</font>; "
    "tabellen i steg 2 inneholder alle 44 rader du trenger.",
    ST_BODY))
story.append(Paragraph(
    "Når dere har gjort det selv, kan vi sammenlikne resultatene og diskutere valgene "
    "(særlig sluttdatoen avhenger av hvordan parallelle aktiviteter knyttes opp). Læringen "
    "blir mye mer konkret når man har vært gjennom det selv.",
    ST_BODY))

# === 7. SPORBARHET ===
story.append(section_header(7, "Sporbarhet for sensor"))
story.append(section_rule())
story.append(Paragraph(
    "Når Basisplan 0 er satt og PNG er eksportert, har vi den fulle <i>før</i>-tilstanden "
    "dokumentert: opprinnelig plan basert på Bårds estimater, med 50 mill kostnadsoverskridelse "
    "synlig som forventet. Når Bård sender crashing-instruks blir det neste leddet i kjeden "
    "endringsdokument CR-001 + Basisplan 1 (etter-tilstand). Det er denne kjeden — fra rå "
    "estimater via dokumentert endring til revidert plan — som er bevis på at vi behersker "
    "endringsstyring i praksis, og som gir poeng på sensorveiledningens eksplisitte 8 poeng "
    "for nettopp dette.",
    ST_BODY))

story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Filer som dokumenterer dagens arbeid er på plass. Si fra på Teams hvis noe er uklart.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
