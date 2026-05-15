# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-15 (natt 2) — Hovedrapport skrevet om.

Femte status-PDF for samme dag. Skrevet enkelt til kollokvie-medlemmene
i Gruppe 4.5 etter at hovedrapporten ble omskrevet til ekte prosjektrapport-stil.
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

OUT = GRUPPEMOTER / "PROSJEKTSTATUS_2026-05-15_natt2_prosjektrapport.pdf"
PROJECT_LABEL = "LOG565 — Nye Hædda Barneskole — Gruppe 4.5"

doc, on_page = build_doc(str(OUT), "Prosjektstatus 15.05.2026 (natt 2) — prosjektrapport skrevet om", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Status til gruppa",
    subtitle="Hovedrapporten er skrevet om — nå en ekte prosjektrapport, ikke akademisk skisse",
    date_label="Natt til 16. mai 2026",
)

# INFO CARD
story.append(info_card([
    ["Hva har skjedd", "Hovedrapporten er skrevet helt om og pushet til GitHub"],
    ["Hvor ligger den nye filen", "05 - Endelig innlevering Hædda Barneskole/Prosjektrapport - Nye Hædda Barneskole.pdf"],
    ["Antall sider", "29 sider (var 36 sider i forrige versjon)"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 (16 dager igjen)"],
]))
story.append(Spacer(1, 0.3 * cm))

# === 1. HVA SOM VAR PROBLEMET ===
story.append(section_header(1, "Hva var problemet med den gamle rapporten?"))
story.append(section_rule())
story.append(Paragraph(
    "Den forrige versjonen var skrevet som en akademisk avhandling — med metode-kapittel, "
    "APA-siteringer i hver setning, og masse fagsjargong. Det er ikke slik en ekte prosjektrapport "
    "ser ut. En ekte rapport er skrevet til oppdragsgiver (kommunen), ikke til en sensor, "
    "og den forteller en historie i stedet for å gjengi teori.",
    ST_LEAD))

problemer = [
    ["Det som var galt", "Hvorfor det var galt"],
    ["For mye akademisk språk",
     "Vi skrev til en sensor i stedet for til kommunen som skal lese rapporten"],
    ["Metode-kapittel om PMBOK og PRINCE2",
     "Kommunen trenger ikke en innføring i prosjektledelsesteori"],
    ["APA-siteringer (Forfatter, år, s. X) i hver setning",
     "Gjør teksten tung å lese og virker stivt"],
    ["Vedleggene var bare henvisninger til andre filer",
     "I en ekte rapport ligger vedleggene <i>i</i> dokumentet, ikke utenfor"],
    ["Mye tekst i header og footer på hver side",
     "Sensor blir distrahert — en ekte rapport har minimalistisk layout"],
    ["Tabeller med overlappende tekst",
     "Så uprofesjonelt ut — kolonnene var for smale"],
]
story.append(make_table(problemer, col_widths=[6 * cm, 10 * cm]))

# === 2. HVA SOM ER GJORT I NATT ===
story.append(section_header(2, "Det vi har gjort i natt"))
story.append(section_rule())

endringer = [
    ["Endring", "Resultat", "Status"],
    ["Skrevet om hele hovedrapporten",
     "Nå skrevet som ekte prosjektrapport til kommunen",
     status_badge("OK", "ok")],
    ["Lagt vedleggene <i>inn i</i> rapporten",
     "Kommunestyrevedtak, CR-001, månedsoversikt, risikoregister og datatabeller "
     "ligger som vedlegg A–F i samme PDF",
     status_badge("OK", "ok")],
    ["Fjernet header på hver side",
     "Mindre rotete utseende",
     status_badge("OK", "ok")],
    ["Forenklet footer til kun sidenummer",
     "Ren og pen — som en faktisk rapport",
     status_badge("OK", "ok")],
    ["Fjernet metode-kapittelet",
     "Teori om PMBOK og EVM er nå korte forklaringer der det trengs, ikke et eget kapittel",
     status_badge("OK", "ok")],
    ["Skrevet sammendraget som historie",
     "Forteller hva som skjedde, ikke bare radet opp tall",
     status_badge("OK", "ok")],
    ["Fikset gruppenavn",
     "Gruppe 4.5 (ikke «Gruppe 4.5 — irgesundinger»)",
     status_badge("OK", "ok")],
    ["Endret saksnummer",
     "Kommunestyrevedtaket heter nå NHB-2026-15 (var NHB-IRGESUND)",
     status_badge("OK", "ok")],
]
story.append(make_table(endringer, col_widths=[5.5 * cm, 8.5 * cm, 2 * cm], badge_col=2))

# === 3. SLIK SER DEN UT NÅ ===
story.append(section_header(3, "Slik er den nye rapporten bygd opp"))
story.append(section_rule())
story.append(Paragraph(
    "Rapporten er 29 sider og deler seg i to deler: hovedrapport (kapittel 1–8) og vedlegg (A–F).",
    ST_BODY))

oppbygging = [
    ["Del", "Kapittel", "Hva er i det"],
    ["Hovedrapport", "1   Sammendrag", "Hva som skjedde, fortalt som historie"],
    ["", "2   Om prosjektet", "Hva som skulle bygges og rammene"],
    ["", "3   Måloppnåelse", "Status mot omfang, tid, kost og kvalitet"],
    ["", "4   Gjennomføringen", "Måned for måned + de to endringene + tre hendelser"],
    ["", "5   Earned Value-analyse", "Tre tall som forteller om vi var på plan"],
    ["", "6   Risiko og bruk av reserver", "Hvordan vi brukte de 50 millionene"],
    ["", "7   Læringspunkter", "Fire ting vi tar med oss"],
    ["", "8   Anbefalinger til kommunen", "Hva de bør gjøre videre"],
    ["Vedlegg", "A   Kommunestyrevedtak NHB-2026-15", "Det formelle vedtaket gjengitt i sin helhet"],
    ["", "B   Endringsdokument CR-001", "DSB sprinkler-saken med full konsekvensanalyse"],
    ["", "C   Månedsoversikt", "Kumulative tall for hver av de 16 månedene"],
    ["", "D   Risikoregister", "Alle realiserte risikoer med status"],
    ["", "E   EVM-data per måned", "Detaljert fremdriftsdata"],
    ["", "F   Kildemateriale og dokumentliste", "Pekere til alle bakgrunnsdokumenter"],
]
story.append(make_table(oppbygging, col_widths=[2.5 * cm, 5.5 * cm, 8 * cm]))

# === 4. SLIK ER SAMMENDRAGET NÅ ===
story.append(section_header(4, "Eksempel — slik leser sammendraget nå"))
story.append(section_rule())
story.append(Paragraph(
    "Bare for å vise forskjellen. Slik åpner det nye sammendraget:",
    ST_BODY))
story.append(Paragraph(
    "<i>«Vi overleverte Nye Hædda Barneskole til Hædda kommune 15. mai 2026 — på den dagen "
    "vi hadde lovet i det opprinnelige kommunestyrevedtaket. Prosjektet brukte 800 millioner "
    "kroner, akkurat det kommunestyret hadde satt av etter justeringen vi gjorde underveis. "
    "[...]</i>",
    ST_INFO))
story.append(Paragraph(
    "<i>Det er enkelt å lese sluttall som disse og tenke at prosjektet gikk uten dramatikk. "
    "Det stemmer ikke. To ganger i løpet av de 16 månedene kunne vi ha kommet skjevt ut — én "
    "gang økonomisk og fremdriftsmessig, og én gang regulatorisk. Begge gangene rettet vi opp "
    "i tide, og vi gjorde det gjennom formelle vedtak og dokumenterte endringer.»</i>",
    ST_INFO))
story.append(Paragraph(
    "Sammenliknet med den gamle versjonen som åpnet med «Cost Performance Index (CPI) og "
    "Schedule Performance Index (SPI) lander begge på 1,000 ved prosjektslutt», er dette en "
    "ganske annerledes leseopplevelse.",
    ST_BODY))

# === 5. STATUS PÅ HELE LEVERANSEN ===
story.append(section_header(5, "Status på hele mappeinnleveringen"))
story.append(section_rule())
story.append(Paragraph(
    "Mappen ligger pushet til GitHub og er klar for innlevering 1. juni. Det som gjenstår er "
    "MS Project tracking-input (1–2 timer manuelt arbeid i morgen).",
    ST_BODY))

leveranser = [
    ["Hva", "Hvor", "Status"],
    ["Hovedrapport (NY)",
     "05 - Endelig innlevering/Prosjektrapport - Nye Hædda Barneskole.pdf",
     status_badge("FERDIG", "ok")],
    ["Sluttrapport (utvidet)",
     "04 - Avslutning/Sluttrapport - Nye Hædda Barneskole.pdf",
     status_badge("FERDIG", "ok")],
    ["16 månedsrapporter",
     "03 - Gjennomføring/Månedsrapporter/",
     status_badge("FERDIG", "ok")],
    ["2 endringsdokumenter",
     "03 - Gjennomføring/Endringsdokumenter/",
     status_badge("FERDIG", "ok")],
    ["EVM-arbeidsbok + MS Project-instruks",
     "03 - Gjennomføring/",
     status_badge("FERDIG", "ok")],
    ["Les meg først (sensor-guide)",
     "00 - Les meg først.pdf",
     status_badge("FERDIG", "ok")],
    ["MS Project tracking-data lagt inn",
     "02 - Planlegging/MS Project - Plan (Baseline 0).mpp",
     status_badge("GJENSTÅR", "pending")],
]
story.append(make_table(leveranser, col_widths=[5.5 * cm, 8.5 * cm, 2 * cm], badge_col=2))

# === 6. KORT TIL DERE I GRUPPA ===
story.append(section_header(6, "Til dere i gruppa"))
story.append(section_rule())
story.append(Paragraph(
    "Last gjerne ned <b>Prosjektrapport - Nye Hædda Barneskole.pdf</b> fra GitHub-repoet og "
    "les gjennom. Den er bygd slik at man kan lese den fra ende til annen som en ekte rapport, "
    "og vedleggene bak gir detaljene for de som vil grave dypere.",
    ST_BODY))

story.append(Paragraph(
    "Det som gjenstår av selvstendig arbeid er å fylle inn faktisk fremdrift i MS Project-fila. "
    "Det er beskrevet trinn for trinn i 03 - Gjennomføring/MS Project tracking-instruks.xlsx. "
    "Estimert tid: 1–2 timer. Det er det siste leddet før hele mappen er klar for innlevering.",
    ST_BODY))

story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Si fra på Teams om noe er uklart eller om det er noe i rapporten dere mener bør justeres "
    "før vi leverer.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
