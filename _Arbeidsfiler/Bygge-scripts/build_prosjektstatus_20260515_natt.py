# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-15 (natt) — Mappestruktur ryddet.

Tredje status-PDF for samme dag, fordi vi gjorde to vesentlige bolker:
  - dag/kveld: bygde opp fase 3 og fase 4 (egen PDF)
  - natt: ryddet mappestrukturen til leveringsverdig form (denne PDF)
"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer

from _status_style import (
    build_doc, hero_block, info_card, section_header, section_rule,
    make_table, status_badge,
    ST_BODY, ST_LEAD, ST_HIGHLIGHT, ST_INFO,
)
from paths import GRUPPEMOTER

OUT = GRUPPEMOTER / "PROSJEKTSTATUS_2026-05-15_natt_mappestruktur.pdf"
PROJECT_LABEL = "LOG565 — Nye Hædda barneskole — Gruppe 4.5"

doc, on_page = build_doc(str(OUT), "Prosjektstatus 15.05.2026 (natt) — mappestruktur", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Prosjektstatus — natt",
    subtitle="Mappestrukturen ryddet til leveringsverdig form",
    date_label="Status pr. 15. mai 2026, natt",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda barneskole — fiktiv skole for 600 elever"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow (17 dager igjen)"],
    ["Mål", "A-nivå (90–100 poeng)"],
    ["Forrige status", "Tidligere i kveld (fase 3 og 4 bygget opp)"],
    ["Denne status", "Mappestruktur ryddet etter A-leveringsverdig standard"],
]))
story.append(Spacer(1, 0.3 * cm))

# === 1. HOVEDPOENG ===
story.append(section_header(1, "Hovedpoeng"))
story.append(section_rule())
story.append(Paragraph(
    "Etter at fase 3 og 4 ble bygget opp i kveld lå alle leveransene i en mappestruktur "
    "som hadde vokst organisk gjennom prosjektet — med rotfiler, blandede maler og "
    "arbeidsfiler, og inkonsistent plassering av planleggingsleveransene. "
    "I natt har vi ryddet hele strukturen til en form som er <b>profesjonell og lett "
    "navigerbar for sensor</b>.",
    ST_LEAD))
story.append(Paragraph(
    "Endelig struktur: 6 numererte/navngitte toppmapper + én skjult arbeidsmappe. "
    "Sensorvennlig leserekkefølge er bygget inn via mappenavn (00 → 04 → Vedlegg). "
    "117 filoperasjoner utført programmatisk via migreringsscript med full logging.",
    ST_BODY))

# === 2. NY MAPPESTRUKTUR ===
story.append(section_header(2, "Ny mappestruktur"))
story.append(section_rule())
struktur = [
    ["Mappe", "Innhold", "Antall filer"],
    ["00 - Les meg først.pdf", "Sensor-guide (ny i natt)", "1 fil"],
    ["01 - Initiering", "Prosjektforslag + Konseptløsning", "2 filer"],
    ["02 - Planlegging",
     "Komplett prosjektplan, kravspec, WBS, risiko, MS Project Baseline 0",
     "9 filer"],
    ["03 - Gjennomføring",
     "Endringsdokumenter/, Månedsrapporter/, EVM-arbeidsbok, MS Project-instruks",
     "36 filer"],
    ["04 - Avslutning", "Sluttrapport (docx + pdf)", "2 filer"],
    ["Oppgavebeskrivelse", "Sensorveiledning + oppgavetekst", "2 filer"],
    ["Vedlegg/", "A-E: Bårds rådata, S-kurver, gruppemøter, tidligere innl., maler", "40 filer"],
    ["_Arbeidsfiler/", "Bygge-scripts, skjermbilder, Pensum, MDV3 (skjult fra leveranse)", "56 filer"],
]
story.append(make_table(struktur, col_widths=[5.5 * cm, 9 * cm, 2 * cm]))

# === 3. ENDRINGER VI GJORDE ===
story.append(section_header(3, "Konkrete endringer"))
story.append(section_rule())
endringer = [
    ["Type", "Hva", "Status"],
    ["Slettet",
     "UTKAST-versjon av sluttrapport, 2 gamle plan-utkast, "
     "GANTT-guide bak-fil + engelsk versjon, EVM-PREVIEW, internt strateginotat",
     status_badge("OK", "ok")],
    ["Flyttet",
     "Hædda barneskole GANTT.mpp → 02 - Planlegging/MS Project - Plan (Baseline 0).mpp",
     status_badge("OK", "ok")],
    ["Strukturert",
     "Endringsdokumenter samlet i egen undermappe under 03 - Gjennomføring",
     status_badge("OK", "ok")],
    ["Bygget",
     "Vedlegg/ med A–E undermapper for støttemateriale (Bårds rådata, S-kurver, "
     "gruppemøter, tidligere innleveringer, maler)",
     status_badge("OK", "ok")],
    ["Skjult",
     "Pensum, MDV3-maler, build-scripts og skjermbilder flyttet til _Arbeidsfiler/ "
     "(underscore-prefix sorteres sist)",
     status_badge("OK", "ok")],
    ["Programvare",
     "paths.py opprettet for sentralisert sti-config; 6 generate_*.py-scripts oppdatert "
     "til å bruke det. Testet at regenerering fortsatt fungerer.",
     status_badge("OK", "ok")],
    ["Levert",
     "00 - Les meg først.pdf (3-siders sensor-guide) plassert på rotnivå",
     status_badge("OK", "ok")],
]
story.append(make_table(endringer, col_widths=[2.5 * cm, 11.5 * cm, 2.2 * cm], badge_col=2))

# === 4. POENG-EFFEKT ===
story.append(section_header(4, "Forventet poengeffekt"))
story.append(section_rule())
story.append(Paragraph(
    "Sensorveiledningens D-område (Sporbarhet og profesjonalitet, 15 poeng) "
    "kjennetegnes av <i>tydelig sporbarhet, god dokumentdisiplin og høy "
    "presentasjonskvalitet</i>. Opprydningen i natt løfter konkret denne dimensjonen:",
    ST_BODY))
effekt = [
    ["Tiltak", "D-effekt", "Hvorfor"],
    ["Nummererte fasemapper (01–04)",
     "+sporbarhet",
     "Sensor følger sensurprosessens rekkefølge automatisk"],
    ["00 - Les meg først.pdf",
     "+presentasjonskvalitet",
     "Signaliserer profesjonalitet før sensor åpner én eneste leveransefil"],
    ["Vedlegg/A–E med tematisk prefix",
     "+dokumentdisiplin",
     "Støttemateriale er kategorisert, ikke en haug"],
    ["_Arbeidsfiler/ skjult",
     "+presentasjonskvalitet",
     "Sensor blir ikke distrahert av arbeidsfiler"],
    ["Slettet utkast og duplikater",
     "+presentasjonskvalitet",
     "Ingen forvirring om hva som er endelig versjon"],
]
story.append(make_table(effekt, col_widths=[5 * cm, 4 * cm, 7 * cm]))
story.append(Paragraph(
    "Estimert poengeffekt: D-området fra ~13 (kveld) til <b>~14 (natt)</b>. "
    "Mer kritisk er at <i>vi har eliminert risikoen for trekk på "
    "\"ujevn profesjonell kvalitet\"</i> som sensorveiledningen eksplisitt advarer mot.",
    ST_INFO))

# === 5. GJENSTÅR ===
story.append(section_header(5, "Det som gjenstår"))
story.append(section_rule())
gjenstaar = [
    ["Når", "Hva", "Status"],
    ["I morgen",
     "MS Project tracking-input (Baseline 0 → crash 4.1 → Baseline 1 → 16 mnd tracking). "
     "Bruk MS Project tracking-instruks.xlsx som referanse.",
     status_badge("PLAN", "info")],
    ["Etter MS Project",
     "Eksporter Tracking-Gantt som PNG og lim inn på 'Figur 1'-plass i de 16 månedsrapportene. "
     "Regenerer PDF-er.",
     status_badge("PLAN", "info")],
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
story.append(make_table(gjenstaar, col_widths=[3 * cm, 11 * cm, 2.5 * cm], badge_col=2))

# === 6. AVSLUTNING ===
story.append(section_header(6, "Sammendrag dagen"))
story.append(section_rule())
story.append(Paragraph(
    "Tre statusrapporter er produsert i dag, som speiler tre arbeidsbolker:",
    ST_BODY))
story.append(Paragraph(
    "<b>Morgen</b> — Gantt-diagrammet bygget i MS Project (fase 2 ferdigstilt). "
    "<b>Kveld</b> — fase 3 (gjennomføring) og fase 4 (sluttrapport) bygget opp på "
    "grunnlag av Bårds nyleverte rådata. <b>Natt</b> — mappestrukturen ryddet til "
    "leveringsverdig form, sensor-guide produsert.",
    ST_BODY))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Estimerte poeng har gått fra ~26 (gårsdagen) → ~46 (morgen) → ~87 (kveld) → ~88 (natt). "
    "Resten henter vi i morgen etter MS Project-arbeidet, med realistisk mål ~93 poeng (A).",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
