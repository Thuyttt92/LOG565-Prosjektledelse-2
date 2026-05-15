# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-15 (sen kveld) — Hovedleveranse + sluttrapport ferdig.

Fjerde status-PDF for samme dag, fordi vi gjorde fire arbeidsbolker:
  - morgen: Gantt-diagrammet bygget i MS Project
  - kveld: fase 3 og fase 4 dokumentasjon bygget opp
  - natt: mappestruktur ryddet til leveringsverdig form
  - sen kveld: Komplett prosjektrapport (35 s) + utvidet sluttrapport (13 s)
    levert med APA7-stil, 10 figurer og tabellfikset uten tekstoverlapp
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

OUT = GRUPPEMOTER / "PROSJEKTSTATUS_2026-05-15_senkveld_hovedrapport.pdf"
PROJECT_LABEL = "LOG565 — Nye Hædda Barneskole — Gruppe 4.5"

doc, on_page = build_doc(str(OUT), "Prosjektstatus 15.05.2026 (sen kveld) — hovedrapport", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Prosjektstatus — sen kveld",
    subtitle="Komplett prosjektrapport (35 s) + utvidet sluttrapport (13 s) levert",
    date_label="Status pr. 15. mai 2026, sen kveld",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda Barneskole"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow (17 dager igjen)"],
    ["Mål", "A-nivå (90–100 poeng)"],
    ["Forrige status", "Tidligere i natt (mappestruktur ryddet)"],
    ["Denne status", "Hovedleveranse i 05-mappa + sluttrapport oppdatert"],
]))
story.append(Spacer(1, 0.3 * cm))

# === 1. HOVEDPOENG ===
story.append(section_header(1, "Hovedpoeng — hovedleveransen er på plass"))
story.append(section_rule())
story.append(Paragraph(
    "Vi har bygget den endelige hovedleveransen — <b>Komplett prosjektrapport — Nye Hædda "
    "Barneskole</b>, 35 sider med APA7-stil, 10 figurer, fullstendig EVM-analyse, "
    "endringsstyring, refleksjon og konklusjon. Filen ligger i den nye mappen <i>05 - Endelig "
    "innlevering Hædda Barneskole/</i> som hovedleveranse for sensor.",
    ST_LEAD))
story.append(Paragraph(
    "Den enkle sluttrapporten i 04 - Avslutning er også oppgradert til en utvidet 13-siders PDF "
    "med samme stil og figurer. Sammen utgjør disse to dokumentene rammen rundt hele "
    "mappestrukturen — alle støttedokumenter (16 månedsrapporter, 2 endringsdokumenter, "
    "EVM-arbeidsbok, MS Project-instruks, kildedata) er pekt til fra disse rapportene.",
    ST_BODY))

# === 2. SAKSNUMMER OG GRUPPENAVN-FIKS ===
story.append(section_header(2, "Konsistens-rydding i hele dokumentsamlingen"))
story.append(section_rule())
story.append(Paragraph(
    "To navnefikser er gjort gjennomgående i ALLE dokumenter (rapporter, månedsrapporter, "
    "endringsdokumenter, instrukser, status-PDF-er):",
    ST_BODY))

ryddinger = [
    ["Før", "Etter", "Begrunnelse"],
    ["Gruppe 4.5 — irgesundinger",
     "Gruppe 4.5",
     "«irgesundinger» var Bårds simuleringsfilnavn, ikke gruppens navn"],
    ["NHB-IRGESUND (kommunestyresak)",
     "NHB-2026-15",
     "Sakssuffikset «IRGESUND» var også fra simuleringsfilnavnet — "
     "nytt nøytralt saksnummer brukt overalt"],
]
story.append(make_table(ryddinger, col_widths=[5 * cm, 4 * cm, 7 * cm]))

# === 3. LEVERANSER ===
story.append(section_header(3, "Endelige leveranser"))
story.append(section_rule())
leveranser = [
    ["Leveranse", "Fil", "Status"],
    ["Hovedleveranse (NY)",
     "05 - Endelig innlevering Hædda Barneskole/Komplett prosjektrapport - Nye Hædda Barneskole.pdf (35 s)",
     status_badge("OK", "ok")],
    ["Sluttrapport (UTVIDET)",
     "04 - Avslutning/Sluttrapport - Nye Hædda barneskole.pdf (13 s)",
     status_badge("OK", "ok")],
    ["Les meg først (sensor-guide)",
     "00 - Les meg først.pdf",
     status_badge("OK", "ok")],
    ["Endringsdokumenter (regenerert)",
     "03 - Gjennomføring/Endringsdokumenter/ (NHB-2026-15 og CR-001)",
     status_badge("OK", "ok")],
    ["16 månedsrapporter (regenerert)",
     "03 - Gjennomføring/Månedsrapporter/ (docx + pdf for hver)",
     status_badge("OK", "ok")],
    ["EVM-arbeidsbok (regenerert)",
     "03 - Gjennomføring/EVM-arbeidsbok - Nye Hædda barneskole.xlsx",
     status_badge("OK", "ok")],
    ["MS Project tracking-instruks",
     "03 - Gjennomføring/MS Project tracking-instruks.xlsx",
     status_badge("OK", "ok")],
]
story.append(make_table(leveranser, col_widths=[5.5 * cm, 8.5 * cm, 2.5 * cm], badge_col=2))

# === 4. KORREKTURLESNING ===
story.append(section_header(4, "Korrekturlesning og tabellfikset"))
story.append(section_rule())
story.append(Paragraph(
    "Etter tilbakemelding ble alle PDF-rapportene gjennomgått systematisk:",
    ST_BODY))
fikser = [
    ["Problem", "Status"],
    ["Tekstoverlapp i tabeller (cellinnhold flytt sammen)",
     status_badge("FIKSET", "ok")],
    ["«irgesundinger» som gruppenavn",
     status_badge("FIKSET", "ok")],
    ["«IRGESUND» som suffix i saksnummer",
     status_badge("FIKSET", "ok")],
    ["Tom side mellom TOC og Sammendrag i komplett rapport",
     status_badge("FIKSET", "ok")],
]
story.append(make_table(fikser, col_widths=[12 * cm, 4 * cm], badge_col=1))

# === 5. KOMPLETT RAPPORT — INNHOLD ===
story.append(section_header(5, "Komplett prosjektrapport — innholdsoversikt"))
story.append(section_rule())
story.append(Paragraph(
    "35 sider strukturert i åtte kapitler + referanser + vedlegg, med APA7-inspirert formatering:",
    ST_BODY))
innhold = [
    ["Kap", "Tittel", "Hovedtemaer"],
    ["—", "Sammendrag", "Sluttall, nøkkelhendelser, fire styringsprinsipper"],
    ["1", "Innledning", "Formål, rammer, prosjektorganisasjon, interessenter, avgrensning"],
    ["2", "Metode og teoretisk grunnlag", "PMBOK, EVM, endringsstyring, datakilder"],
    ["3", "Planleggingsfasen", "Krav, WBS (32 pakker), Gantt, milepæler, risiko"],
    ["4", "Gjennomføringsfasen", "Endringsstyring, EVM-sluttanalyse, hendelser, sporbarhet"],
    ["5", "Avslutningsfasen", "Måloppnåelse, business case og gevinstrealisering"],
    ["6", "Refleksjon", "Læringspunkter, hva overrasket oss, forbedringer"],
    ["7", "Anbefalinger", "Gevinstoppfølging, FDV, erfaringsoverføring, opplæring"],
    ["8", "Konklusjon", "Oppsummering og avsluttende vurdering"],
]
story.append(make_table(innhold, col_widths=[1 * cm, 5 * cm, 10 * cm]))

# === 6. NESTE STEG ===
story.append(section_header(6, "Det som gjenstår"))
story.append(section_rule())
neste = [
    ["Når", "Hva", "Status"],
    ["I morgen",
     "MS Project tracking-input — bruk MS Project tracking-instruks.xlsx",
     status_badge("NESTE", "pending")],
    ["Etter MS Project",
     "Eksporter Tracking-Gantt som PNG og lim inn i månedsrapportene",
     status_badge("VENTER", "info")],
    ["Før innlevering",
     "Korrekturlesning av rapportene visuelt — gjør hver gruppemedlem en runde",
     status_badge("PLAN", "info")],
    ["1. juni 15:00",
     "Innlevering i WiseFlow — last opp hele mappestrukturen som ZIP",
     status_badge("MÅL", "pending")],
]
story.append(make_table(neste, col_widths=[3 * cm, 11 * cm, 2.5 * cm], badge_col=2))

# === 7. AVSLUTNING ===
story.append(section_header(7, "Avslutning"))
story.append(section_rule())
story.append(Paragraph(
    "Med hovedrapporten og oppdatert sluttrapport på plass har vi nå hele dokumentsamlingen som "
    "trengs for mappeinnleveringen, med rimelig kvalitet på alle nivåer. Estimerte poeng står "
    "ved ~90 (A-grensen) før MS Project-arbeidet — etter MS Project er fylt ut, vurderer vi at "
    "~93 er realistisk.",
    ST_BODY))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Hele dokumentsamlingen er pushet til GitHub-repoet for backup og deling. Si fra på Teams "
    "om noe trenger justering før innlevering.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
