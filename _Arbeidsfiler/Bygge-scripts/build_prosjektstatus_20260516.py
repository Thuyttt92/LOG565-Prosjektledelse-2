# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-16 — MS Project instruks som PDF + det som gjenstår.

Status til kollokvie-medlemmene morgenen etter at hovedrapporten ble omskrevet.
Forklarer hvor MS Project-instruksen ligger nå (som PDF) og hva som gjenstår.
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

OUT = GRUPPEMOTER / "PROSJEKTSTATUS_2026-05-16_msprojectinstruks.pdf"
PROJECT_LABEL = "LOG565 — Nye Hædda Barneskole — Gruppe 4.5"

doc, on_page = build_doc(str(OUT), "Prosjektstatus 16.05.2026 — MS Project-instruks som PDF", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Status til gruppa",
    subtitle="MS Project-instruksen ligger nå som PDF — klar til bruk",
    date_label="16. mai 2026",
)

# INFO CARD
story.append(info_card([
    ["Hva har skjedd", "MS Project tracking-instruks konvertert til PDF"],
    ["Hvor", "03 - Gjennomføring/MS Project tracking-instruks.pdf (10 sider)"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 (16 dager igjen)"],
    ["Status totalt", "Dokumentasjon ferdig — kun MS Project-arbeid gjenstår"],
]))
story.append(Spacer(1, 0.3 * cm))

# === 1. HOVEDPOENG ===
story.append(section_header(1, "Hvor vi står nå"))
story.append(section_rule())
story.append(Paragraph(
    "Vi er nesten ferdige. Hele dokumentsamlingen — prosjektrapporten, sluttrapporten, "
    "16 månedsrapporter, endringsdokumenter, EVM-arbeidsbok — er på plass og pushet til "
    "GitHub. Det som gjenstår er bare MS Project-arbeidet og noen siste justeringer.",
    ST_LEAD))

story.append(Paragraph(
    "Jeg har også konvertert MS Project tracking-instruksen fra Excel til <b>PDF</b>, slik at "
    "den er enklere å åpne og lese for de av oss som ikke har Excel klart. Den ligger på "
    "<b>03 - Gjennomføring/MS Project tracking-instruks.pdf</b> og er 10 sider lang.",
    ST_BODY))

# === 2. HVA SOM ER I PDF-EN ===
story.append(section_header(2, "Hva inneholder MS Project-instruksen?"))
story.append(section_rule())

innhold = [
    ["Side", "Hva", "Hvorfor"],
    ["1–2", "Steg-for-steg instruks (Del A–E)",
     "Slik fyller du ut MS Project-fila — fra start til ferdig"],
    ["3", "Alle 32 arbeidspakker",
     "Hvilke pakker som er i prosjektet, med varighet og budsjett per pakke"],
    ["4", "Crashing-endringen på 4.1 Råbygg",
     "Hva som er forskjellen mellom Baseline 0 og Baseline 1"],
    ["5–9", "Tracking-data per måned",
     "Eksakte verdier for hver av de 16 statusdatoene — fullføringsgrad og påløpt kostnad"],
    ["10", "Månedstabell med PV/EV/AC",
     "Sluttkontroll: når du er ferdig, skal disse tallene matche"],
]
story.append(make_table(innhold, col_widths=[1.5 * cm, 5 * cm, 9.5 * cm]))

# === 3. SLIK GJØR DU MS PROJECT-ARBEIDET ===
story.append(section_header(3, "Slik gjør du MS Project-arbeidet"))
story.append(section_rule())
story.append(Paragraph(
    "Hele jobben er beskrevet i PDF-en, men her er hovedflyten enkelt forklart:",
    ST_BODY))

steg = [
    ["Steg", "Hva du gjør", "Tid"],
    ["1", "Åpne Hædda barneskole GANTT.mpp og lagre kopi som «- tracking.mpp»",
     "5 min"],
    ["2", "Sett Baseline 0 (Prosjekt → Set Baseline → Baseline 0)",
     "5 min"],
    ["3", "Endre 4.1 Råbygg: varighet 7→5 mnd, kostnad 190→240 MNOK",
     "10 min"],
    ["4", "Sett Baseline 1 (samme meny som steg 2)",
     "5 min"],
    ["5", "For hver av de 16 månedene: skriv inn % fullført + påløpt kostnad fra tabellen "
     "i PDF-en",
     "1–1,5 t"],
    ["6", "Eksporter Tracking-Gantt som bilde for hver måned",
     "30 min"],
    ["7", "Lim Gantt-bildene inn i månedsrapportene (DOCX) og lagre som PDF",
     "1 t"],
]
story.append(make_table(steg, col_widths=[1.5 * cm, 11 * cm, 3.5 * cm]))

story.append(Paragraph(
    "Totalt: ca. <b>3–4 timer</b> arbeid. Du kan ta det i én økt eller dele opp.",
    ST_INFO))

# === 4. HVA GJENSTÅR ETTER MS PROJECT ===
story.append(section_header(4, "Hva gjenstår etter MS Project er ferdig?"))
story.append(section_rule())

gjenstaar = [
    ["Når", "Hva", "Tid", "Status"],
    ["Snart",
     "MS Project tracking-input (steg 1–5 over)",
     "1–1,5 t",
     status_badge("NESTE", "pending")],
    ["Etter MS Project",
     "Eksportere Gantt-bilder fra MS Project (16 + 1 sammenstilt)",
     "30 min",
     status_badge("VENTER", "info")],
    ["Etter Gantt-bildene",
     "Lim Gantt-bildene inn i månedsrapportene + regenerer PDF",
     "1 t",
     status_badge("VENTER", "info")],
    ["Før innlevering",
     "Visuell gjennomgang av hele mappestrukturen",
     "1 t",
     status_badge("PLAN", "info")],
    ["1. juni kl 15:00",
     "Last opp i WiseFlow (hele mappen som ZIP, eller hovedfilen)",
     "15 min",
     status_badge("MÅL", "pending")],
]
story.append(make_table(gjenstaar, col_widths=[3 * cm, 8 * cm, 2 * cm, 2.5 * cm], badge_col=3))

# === 5. HVA SOM ER FERDIG (TIL DERES TRYGGHET) ===
story.append(section_header(5, "Dette er allerede ferdig (ikke noe å bekymre seg for)"))
story.append(section_rule())

ferdig = [
    ["Leveranse", "Hvor"],
    ["Hovedrapport (Prosjektrapport.pdf, 29 sider)",
     "05 - Endelig innlevering Hædda Barneskole/"],
    ["Sluttrapport (utvidet, 13 sider)",
     "04 - Avslutning/"],
    ["16 månedsrapporter (docx + pdf)",
     "03 - Gjennomføring/Månedsrapporter/"],
    ["2 endringsdokumenter (docx + pdf)",
     "03 - Gjennomføring/Endringsdokumenter/"],
    ["EVM-arbeidsbok",
     "03 - Gjennomføring/"],
    ["MS Project tracking-instruks (xlsx + PDF)",
     "03 - Gjennomføring/"],
    ["Les meg først (sensor-guide)",
     "00 - Les meg først.pdf"],
    ["Komplett prosjektplan + kravspec + WBS + risikoregister",
     "02 - Planlegging/"],
    ["Kildemateriale fra Bård (rådata)",
     "Vedlegg/A - Kildemateriale fra Bård/"],
    ["S-kurver og statusrapporter",
     "Vedlegg/B og C/"],
]
story.append(make_table(ferdig, col_widths=[8 * cm, 8 * cm]))

# === 6. KORT TIL DERE I GRUPPA ===
story.append(section_header(6, "Til dere i gruppa"))
story.append(section_rule())
story.append(Paragraph(
    "Last gjerne ned <b>MS Project tracking-instruks.pdf</b> fra GitHub-repoet. Den er "
    "selvforklarende og bygd slik at du kan følge den steg for steg uten å måtte huske "
    "noe på forhånd.",
    ST_BODY))

story.append(Paragraph(
    "Når MS Project-arbeidet er ferdig, er vi praktisk talt klare for innlevering. Sjekk "
    "også gjerne prosjektrapporten på 29 sider — det er den sensor leser først, så det er "
    "lurt at alle i gruppa har lest gjennom den minst én gang.",
    ST_BODY))

story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Si fra på Teams hvis noe i instruksen er uklart, eller om du finner noe i rapporten "
    "som bør justeres før vi leverer.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
