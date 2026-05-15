# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-05 (omarbeidet med ny stilmal)."""
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
    r"\Gruppe 4.5 møter\PROSJEKTSTATUS_2026-05-05.pdf"
)
PROJECT_LABEL = "LOG565 — Nye Hædda barneskole — Gruppe 4.5"

doc, on_page = build_doc(OUT, "Prosjektstatus 05.05.2026", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Prosjektstatus",
    subtitle="LOG565 Prosjektledelse 2 — Mappeinnlevering",
    date_label="Status pr. 5. mai 2026",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda barneskole — fiktiv skole for 600 elever"],
    ["Vurderingsform", "Mappeinnlevering, 100 % av karakter"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow"],
    ["Mål", "A-nivå (90–100 poeng)"],
]))
story.append(Spacer(1, 0.4 * cm))

# === 1. HOVEDPOENG ===
story.append(section_header(1, "Hovedpoeng siden forrige status"))
story.append(section_rule())
story.append(Paragraph(
    "I løpet av dagen har vi mottatt Bårds simulerte WBS med konkrete tids- og kostnadsestimater, "
    "og dermed fått det tallgrunnlaget vi har ventet på for å bygge Gantt-diagrammet. "
    "Vi har også fått ny informasjon fra Bård om at planen <b>bevisst overskrider rammene for "
    "både tid og kostnad</b> — og at vi som gruppe må løse dette med "
    "<i>schedule crashing</i> (fremskynde aktiviteter på kritisk sti mot økt kostnad).",
    ST_LEAD))
story.append(Paragraph("Konkrete tall fra Bårds simulering:", ST_BODY))

n_tab = [
    ["Parameter", "Prosjektforslag", "Bårds simulering", "Avvik"],
    ["Sluttdato", "15. mai 2026", "ca. 31. juli 2026", "~6 uker over"],
    ["Totalkostnad", "700 mill kr", "ca. 750 mill kr", "+50 mill kr"],
]
story.append(make_table(n_tab, col_widths=[3.5 * cm, 4 * cm, 4.5 * cm, 4.5 * cm]))
story.append(Paragraph(
    "Dette er presis det Bård signaliserte — overskridelsene er innebygd i oppgaven. "
    "Vi har fått varsel om at Bård sender en gruppespesifikk crashing-instruks via Teams "
    "(hvilken aktivitet som skal crashes og hvor mye ekstra det koster). Endringen skal "
    "deretter dokumenteres formelt i et endringsdokument.",
    ST_INFO))

# === 2. HVA VI HAR GJORT ===
story.append(section_header(2, "Det vi har gjort i dag"))
story.append(section_rule())

story.append(Paragraph("2.1 Tilpassing mot prosjektforslaget", ST_H3))
story.append(Paragraph(
    "Etter en grundig gjennomlesning av prosjektforslaget har vi rettet to avvik i grunnlaget vi "
    "sendte til Bård:",
    ST_BODY))
for item in [
    "<b>F-009 (Kravspesifikasjon):</b> Antall ansatte er korrigert fra 70 til <b>100</b> "
    "(60 faglige + 15 administrasjon + 25 drift), med arealnormer på 10 m²/ansatt for faglige "
    "og 6 m²/ansatt for drift, jf. prosjektforslag kap. 4.3.",
    "<b>F-003 (Kravspesifikasjon):</b> Klasserom-areal hevet fra 2,5 til <b>3 m² per elev</b>, "
    "også jf. prosjektforslag kap. 4.3.",
    "<b>Risikoregister:</b> Total risikoavsetning er hevet fra 27 til <b>50 mill kr</b> for å matche "
    "prosjektforslagets usikkerhetsavsetning (kap. 6.4). Vi har lagt til R-016 (Generell uspesifisert "
    "avsetning, 23 mill kr) som dekker forskjellen mellom våre 15 spesifikke risikoer og rammen.",
]:
    story.append(Paragraph(f"&bull;&nbsp;&nbsp;{item}", ST_BODY))
story.append(Paragraph("Begge xlsx-filer har nå versjon 1.1.", ST_NOTE))

story.append(Paragraph("2.2 Forberedelser for fase 3 og crashing-saken", ST_H3))
story.append(Paragraph(
    "Vi har bygget alt som kan bygges uten konkrete tall fra Bård, slik at vi kan gjøre kort prosess "
    "når svarene kommer:",
    ST_BODY))
fase3 = [
    ["Hva", "Hvor"],
    ["Endringsdokument CR-001 — pre-fylt skjelett for crashing-saken "
     "(11 tabeller, 6 konsekvensområder, narrativ flyt leverandør → tilbud → eier-godkjenning)",
     "03 - Gjennomføring/"],
    ["MS Project baseline-strategi (Baseline 0 → Baseline 1)", "03 - Gjennomføring/"],
    ["Problemliste-mal — løpende issue-tracking", "03 - Gjennomføring/Maler/"],
    ["EVM/S-kurve Excel-arbeidsbok — formler, sample-data, innebygd diagram",
     "03 - Gjennomføring/Maler/"],
    ["Månedsrapport-mal — foreldede 'simuleringsportal'-referanser ryddet",
     "03 - Gjennomføring/Maler/"],
]
story.append(make_table(fase3, col_widths=[11 * cm, 5.5 * cm]))

story.append(Paragraph("2.3 Klargjøring for Gantt-bygging", ST_H3))
story.append(Paragraph(
    "Vi har ferdigstilt en MS Project-import-fil med Bårds 40 oppgaver + 4 milepæler "
    "(BP2, BP3, hard frist 15. mai, skolestart august), inkludert varigheter, kostnader, "
    "ressursnavn og avhengigheter. I tillegg har vi laget en illustrert byggeguide "
    "(både markdown og PDF) med 11 steg, kvalitetssjekklister og en preview av forventet "
    "sluttresultat.",
    ST_BODY))
gantt = [
    ["Hva", "Hvor"],
    ["MS Project-import-fil (40 oppgaver + 4 milepæler)",
     "Arbeidsfiler/Gantt-import (Bårds simulering) ... .xlsx"],
    ["Illustrert byggeguide (PDF, 14 sider)",
     "02 - Planlegging/GANTT_BYGGE_GUIDE.pdf"],
    ["Markdown-versjon av byggeguiden",
     "02 - Planlegging/GANTT_BYGGE_GUIDE.md"],
    ["Preview av forventet sluttresultat (Gantt-bilde)",
     "Arbeidsfiler/Gantt - Baseline 0 - PREVIEW.png"],
]
story.append(make_table(gantt, col_widths=[7.5 * cm, 9 * cm]))

story.append(Paragraph("2.4 Opprydning av mappestruktur", ST_H3))
story.append(Paragraph(
    "Mappestrukturen er ryddet for å gjøre det enklere å navigere mot innleveringen. "
    "Filene som skal til Bård ligger nå samlet i én mappe, og foreldede dokumenter er fjernet.",
    ST_BODY))
struktur = [
    ["Mappe", "Innhold"],
    ["Innleveringer til Bård/Sendt til Bård/",
     "Følgebrev, kravspec (v1.1), WBS, risikoregister (v1.1), zip-pakke"],
    ["Innleveringer til Bård/Mottatt fra Bård/", "Bårds simulerte WBS"],
    ["Arbeidsfiler/", "Interne ting (Gantt-import-fil, preview-bilder)"],
    ["Gruppe 4.5 møter/", "Disse statusrapportene"],
    ["02 - Planlegging/", "Fase 2-leveranser (prosjektplan-PDF, WBS-diagram, presedensdiagram)"],
    ["03 - Gjennomføring/", "Fase 3-artefakter + maler"],
    ["04 - Avslutning/", "Sluttrapport-mal"],
]
story.append(make_table(struktur, col_widths=[7.5 * cm, 9 * cm]))

# === 3. STATUS MOT SENSORVEILEDNINGEN ===
story.append(section_header(3, "Status mot sensorveiledningen"))
story.append(section_rule())
story.append(Paragraph(
    "Sensorveiledningen vekter 100 poeng fordelt på fire områder. Med dagens arbeid mener vi "
    "vi ligger godt an, særlig på planleggingsfasens grunnlag og forberedelsene for endringsstyring "
    "(et eksplisitt sensorpunkt på 8 poeng). Vurdert estimat:",
    ST_BODY))
status_tab = [
    ["Område", "Maks", "I dag", "Etter Gantt", "Etter fase 3+4"],
    ["A. Planleggingsfasen", "40", "~17", "~36", "—"],
    ["B. Gjennomføringsfasen", "35", "0", "0", "~31"],
    ["C. Avslutningsfasen", "10", "0", "0", "~9"],
    ["D. Sporbarhet og profesjonalitet", "15", "~9", "~10", "~13"],
    ["TOTALT (estimert)", "100", "~26", "~46", "~89"],
]
story.append(make_table(status_tab, col_widths=[6 * cm, 2.0 * cm, 2.0 * cm, 2.5 * cm, 4 * cm]))
story.append(Paragraph(
    "Realistisk estimert sluttkarakter ligger på <b>B/A-grensen (88–92 poeng)</b>. "
    "For å lande klart på A må vi: (a) bygge Gantt korrekt med Baseline 0, (b) gjennomføre "
    "fase 3 med reell tracking og månedsrapporter med S-kurve og earned value-analyse, "
    "(c) skrive en sluttrapport som <i>analyserer</i> crashing-saken som læringspunkt — "
    "ikke bare oppsummerer.",
    ST_BODY))

# === 4. NESTE STEG ===
story.append(section_header(4, "Neste steg"))
story.append(section_rule())
neste = [
    ["Når", "Hva", "Status"],
    ["Snarest",
     "Bygge Gantt i MS Project iht. GANTT_BYGGE_GUIDE.pdf — gir 12 sensor-poeng.",
     status_badge("NÅ", "pending")],
    ["Når Bård sender crashing-instruks",
     "Fylle ut endringsdokument CR-001 + sette Baseline 1 i MS Project.",
     status_badge("PLAN", "info")],
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

# === 5. PÅGÅENDE ARBEID ===
story.append(section_header(5, "Pågående arbeid i gruppen"))
story.append(section_rule())
story.append(Paragraph(
    "<b>Gantt-diagrammet:</b> Gustavo A Holmedal er i gang med å bygge Gantt-diagrammet i MS Project "
    "basert på Bårds simulerte tall. Når det er ferdig (med Baseline 0 satt), eksporteres det som "
    ".mpp + PNG til <font name='Courier'>02 - Planlegging/</font>. Dette blir vår offisielle "
    "innlevering for delområdet 'Gantt/MS Project — plan' (12 sensorpoeng).",
    ST_BODY))
story.append(Paragraph(
    "<b>Anbefaling til resten av gruppen:</b> Det skader ikke at hver av oss lager et eget "
    "Gantt-diagram som øving. MS Project er et verktøy vi bør beherske — både for denne "
    "innleveringen og for fremtidig praksis. Bruk samme grunnlag og følg "
    "<font name='Courier'>02 - Planlegging/GANTT_BYGGE_GUIDE.pdf</font>. Den illustrerte guiden "
    "tar deg gjennom hvert steg, så det er fullt mulig å gjøre selv.",
    ST_BODY))
story.append(Paragraph(
    "Vi sammenligner gjerne resultatene etterpå — det blir lettere å se hva som er gode valg og "
    "hvilke feller man kan gå i. Læringen sitter mye bedre når man har gjort det selv én gang.",
    ST_BODY))

# === 6. SENSOR ===
story.append(section_header(6, "Hva sensor særlig ser etter"))
story.append(section_rule())
story.append(Paragraph(
    "Sensorveiledningen bruker formuleringen «<i>den beste besvarelsen er ikke nødvendigvis den "
    "mest omfattende, men den som viser best prosjektfaglig dømmekraft, høy intern konsistens "
    "og tydelig sporbarhet mellom plan, gjennomføring og avslutning.</i>» "
    "For oss betyr det at filene må henge sammen — krav peker til WBS, WBS peker til risiko, "
    "risiko peker tilbake til WBS. Plan, gjennomføring og avslutning skal fortelle én "
    "sammenhengende historie. Det er denne røde tråden vi har bygget opp i dag.",
    ST_BODY))

story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Spør gjerne hvis noe i strukturen er uklart — vi kan gå gjennom det sammen i Teams.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
