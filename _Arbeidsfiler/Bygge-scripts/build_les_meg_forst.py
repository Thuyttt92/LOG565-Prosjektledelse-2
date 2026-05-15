# -*- coding: utf-8 -*-
"""Bygger 00 - Les meg først.pdf — sensor-guide for mappeinnleveringen.

Plassering: prosjektroten. Skal gi sensor en rask oversikt over strukturen
og pekere til sentrale leveranser per fase.
"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer

from _status_style import (
    build_doc, hero_block, info_card, section_header, section_rule,
    make_table, ST_BODY, ST_LEAD, ST_HIGHLIGHT, ST_NOTE,
)

from paths import ROOT

OUT = ROOT / "00 - Les meg først.pdf"
PROJECT_LABEL = "LOG565 — Nye Hædda barneskole — Gruppe 4.5"

doc, on_page = build_doc(str(OUT), "Les meg først", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Les meg først",
    subtitle="Leseguide til mappeinnleveringen — LOG565 Prosjektledelse 2",
    date_label="Innlevert til WiseFlow",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda barneskole (fiktivt — 600 elever, 100 ansatte)"],
    ["Studenter", "Gruppe 4.5 — Bachelor i logistikk, Høgskolen Molde"],
    ["Emne", "LOG565 Prosjektledelse 2"],
    ["Vurderingsform", "Mappeinnlevering (100 % av karakter)"],
    ["Omfang", "Fase 2 (planlegging), fase 3 (gjennomføring), fase 4 (avslutning)"],
]))
story.append(Spacer(1, 0.3 * cm))

# === 1. KORT OVERSIKT ===
story.append(section_header(1, "Hva ligger hvor"))
story.append(section_rule())
story.append(Paragraph(
    "Mappestrukturen følger oppgavens fasestruktur (01–04) og legger støttemateriale "
    "i en egen Vedlegg-mappe. Numrene gjør at fasene sorteres riktig i Filutforsker.",
    ST_LEAD))

oversikt = [
    ["Mappe", "Innhold", "Sentrale dokumenter"],
    ["01 - Initiering",
     "Prosjektets opprinnelse og rammer",
     "Prosjektforslag, Konseptløsning"],
    ["02 - Planlegging",
     "Plangrunnlaget (fase 2)",
     "Komplett prosjektplan, Kravspesifikasjon, WBS, Risikoregister, MS Project Baseline 0"],
    ["03 - Gjennomføring",
     "Tracking og rapportering (fase 3)",
     "16 månedsrapporter, 2 endringsdokumenter, EVM-arbeidsbok, MS Project Baseline 1 + tracking"],
    ["04 - Avslutning",
     "Sluttrapport (fase 4)",
     "Sluttrapport (.docx + .pdf)"],
    ["Vedlegg",
     "Støttemateriale (A–E)",
     "Bårds rådata, S-kurver, gruppemøter, tidligere innleveringer, maler"],
    ["_Arbeidsfiler",
     "Intern dokumentasjon (sensor kan ignorere)",
     "Bygge-scripts, skjermbilder, planleggingsnotater"],
]
story.append(make_table(oversikt, col_widths=[3.5 * cm, 5 * cm, 7.5 * cm]))

# === 2. LESEREKKEFØLGE FOR SENSUR ===
story.append(section_header(2, "Anbefalt leserekkefølge"))
story.append(section_rule())
story.append(Paragraph(
    "Sensurveiledningen anbefaler å vurdere planleggingsfasen som fundament, "
    "deretter gjennomføring, og til slutt avslutning. Denne leveransen er "
    "strukturert slik at det er enkelt å følge:",
    ST_BODY))

rekkefolge = [
    ["#", "Steg", "Filer"],
    ["1", "Fundament — fase 2",
     "02 - Planlegging/Komplett prosjektplan - Nye Hædda barneskole.pdf "
     "(samler alt — krav, WBS, presedens, risiko, Gantt). "
     "Detaljer i de øvrige filene i samme mappe."],
    ["2", "Gjennomføring — fase 3",
     "Start med 03 - Gjennomføring/Endringsdokumenter/ (de 2 endringsdokumentene "
     "viser hvordan vi har dokumentert endringsstyring). "
     "Deretter 03 - Gjennomføring/Månedsrapporter/ (16 rapporter med S-kurve, "
     "EVM, avvik). EVM-arbeidsbok.xlsx er den sentrale KPI-kilden."],
    ["3", "Avslutning — fase 4",
     "04 - Avslutning/Sluttrapport - Nye Hædda barneskole.pdf "
     "(syntese av hele forløpet + læringspunkter)."],
    ["4", "Kildemateriale",
     "Vedlegg/A - Kildemateriale fra Bård/ inneholder rådataene vi har jobbet ut fra "
     "(godkjenning-PDF og månedsrapporter-PDF)."],
]
story.append(make_table(rekkefolge, col_widths=[1 * cm, 4 * cm, 11 * cm]))

# === 3. NØKKELTALL ===
story.append(section_header(3, "Nøkkeltall — sluttstatus"))
story.append(section_rule())
nokkeltall = [
    ["Parameter", "Verdi", "Status"],
    ["Vedtatt sluttdato", "15. mai 2026", "Holdt på datoen"],
    ["Vedtatt budsjettramme (etter NHB-2026-15)", "800 MNOK", "Brukt 800 MNOK på prikken"],
    ["CPI ved prosjektslutt", "1.000", "Innenfor budsjett"],
    ["SPI ved prosjektslutt", "1.000", "Iht. plan"],
    ["Risikoreserve brukt", "11 av 50 MNOK", "22 % brukt"],
    ["Tidsbuffer brukt", "1,5 av 8 uker", "19 % brukt"],
    ["Antall hendelser realisert", "3 risikoer (R-05, R-06, R-07)", "1 ble formell CR (CR-001)"],
    ["Antall endringsdokumenter", "2 (NHB-2026-15 + CR-001)", "Begge med full konsekvensanalyse"],
    ["WBS — arbeidspakker (leaves)", "32 stk", "Alle 100 % fullført"],
    ["Kravspesifikasjon — antall krav", "59 krav, 9 kategorier", "Alle levert"],
]
story.append(make_table(nokkeltall, col_widths=[6 * cm, 4.5 * cm, 6 * cm]))

# === 4. ENDRINGSSTYRING ===
story.append(section_header(4, "Endringsstyring — kort sammendrag"))
story.append(section_rule())
story.append(Paragraph(
    "To formelle endringer er dokumentert i fase 3:",
    ST_BODY))
endringer = [
    ["ID", "Hva", "Konsekvens"],
    ["NHB-2026-15",
     "Komprimering (crashing) av 4.1 Råbygg + utvidelse av budsjettramme fra 700 til 800 MNOK. "
     "Vedtak fattet i kommunestyret 7. mai 2026.",
     "Sluttdato 15.05.2026 overholdt. +100 MNOK på totalramme. "
     "4.1 Råbygg: 7→5 mnd varighet, 190→240 MNOK kostnad."],
    ["CR-001",
     "Regulatorisk endring — oppgradert sprinklerdekning og rømningsskilting på 5.1 VVS "
     "iht. ny DSB-veileder. Godkjent 3. februar 2026.",
     "+5,0 MNOK fra risikoreserve, +1 uke (absorbert i tidsbuffer). "
     "Sikrer brukstillatelse for skolen."],
]
story.append(make_table(endringer, col_widths=[3 * cm, 6.5 * cm, 6.5 * cm]))

# === 5. SPORBARHET ===
story.append(section_header(5, "Sporbarhet — referat → rapport → MS Project"))
story.append(section_rule())
story.append(Paragraph(
    "Tallene i hver månedsrapport er sporbare tilbake til Bårds rådata "
    "(Vedlegg/A/månedsrapporter.pdf). Eksempler:",
    ST_BODY))
sporbarhet = [
    ["Måned", "I Bårds referat", "I månedsrapport"],
    ["Mnd 4 (mai 2025)", "R-05: forurenset masse, 6,0 MNOK", "ISS-04-01 (R-05), 6,0 MNOK"],
    ["Mnd 11 (des 2025)", "R-07: brann hos vindusprodusent, 1,5 uker", "ISS-11-01 (R-07), 1,5 uker"],
    ["Mnd 13 (feb 2026)", "R-06: DSB sprinkler/rømning, 5,0 MNOK, 1 uke", "ISS-13-01 (R-06 / CR-001), 5,0 MNOK"],
]
story.append(make_table(sporbarhet, col_widths=[3.5 * cm, 6 * cm, 6.5 * cm]))

# === 6. TEKNISK INFO ===
story.append(section_header(6, "Teknisk info om mappen"))
story.append(section_rule())
story.append(Paragraph(
    "Mappen er strukturert for å være selvforklarende ved bla. Nummererte fasemapper "
    "(01–04) inneholder kun leveranser; Vedlegg/ samler støttemateriale med "
    "tydelige A–E-prefiks; _Arbeidsfiler/ (skjult fra leveranse-perspektiv) inneholder "
    "interne bygge-scripts og notater som ikke er en del av selve mappeinnleveringen.",
    ST_BODY))
story.append(Paragraph(
    "Filene er PDF for lesbarhet, supplert med originale .docx/.xlsx/.mpp/.pptx der "
    "sensor måtte ønske å gå inn i kildedataene. EVM-beregningen er gjort programmatisk "
    "for sporbarhet (kilde: _Arbeidsfiler/Bygge-scripts/log565_master_data.py).",
    ST_NOTE))

story.append(Spacer(1, 0.4 * cm))
story.append(Paragraph(
    "Takk for vurderingen. Spørsmål kan rettes til Gruppe 4.5 via Teams eller "
    "studiekoordinator.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
