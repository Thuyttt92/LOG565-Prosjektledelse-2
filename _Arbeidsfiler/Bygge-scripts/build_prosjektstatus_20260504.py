# -*- coding: utf-8 -*-
"""Prosjektstatus 2026-05-04 (omarbeidet med ny stilmal)."""
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
    r"\Gruppe 4.5 møter\PROSJEKTSTATUS_2026-05-04.pdf"
)
PROJECT_LABEL = "LOG565 — Nye Hædda barneskole — Gruppe 4.5"

doc, on_page = build_doc(OUT, "Prosjektstatus 04.05.2026", PROJECT_LABEL)
story = []

# HERO
story += hero_block(
    title="Prosjektstatus",
    subtitle="LOG565 Prosjektledelse 2 — Mappeinnlevering",
    date_label="Status pr. 4. mai 2026",
)

# INFO CARD
story.append(info_card([
    ["Prosjekt", "Nye Hædda barneskole — fiktiv skole for 600 elever"],
    ["Vurderingsform", "Mappeinnlevering, 100 % av karakter"],
    ["Innleveringsfrist", "1. juni 2026 kl 15:00 i WiseFlow"],
    ["Mål", "A-nivå (90–100 poeng)"],
    ["Format", "Zip-fil med alle leveranser fra fase 2, 3 og 4"],
]))
story.append(Spacer(1, 0.4 * cm))

# === 1. DET VI SKAL LEVERE ===
story.append(section_header(1, "Det vi skal levere"))
story.append(section_rule())
story.append(Paragraph(
    "Vi skal styre prosjektet «Nye Hædda barneskole» gjennom tre faser av PMI-modellen "
    "(planlegging, gjennomføring, avslutning) og levere en mappe med alle styringsdokumentene. "
    "Fase 1 (initiering — prosjektforslag og konseptløsning) er allerede gitt og legges ved som vedlegg.",
    ST_LEAD))

leveranser = [
    ["Fase", "Leveranser", "Vekt"],
    ["1 — Initiering (vedlegg)",
     "Prosjektforslag + konseptløsning. Ikke sensurert, men skal være med.", "—"],
    ["2 — Planlegging",
     "Kravspesifikasjon, WBS, WBS-diagram, presedensdiagram, Gantt, risikoregister, komplett prosjektplan.",
     "40 %"],
    ["3 — Gjennomføring",
     "Gantt med status tracking, månedlige styringsrapporter (KPI, S-kurve, EVM), endringsstyring, problemlogg.",
     "35 %"],
    ["4 — Avslutning", "Sluttrapport med måloppnåelse, lærdom og refleksjon.", "10 %"],
    ["+ Tverrgående", "Sporbarhet, profesjonalitet og dokumentkvalitet.", "15 %"],
]
story.append(make_table(leveranser, col_widths=[4.5 * cm, 9.5 * cm, 2.5 * cm]))
story.append(Paragraph(
    "For A-nivå krever sensorveiledningen <b>minst 40 krav</b> i kravspesifikasjonen og en "
    "<b>WBS med minst 60 leveranser i 4 nivåer</b>.",
    ST_INFO))

# === 2. VIKTIG ENDRING FRA BÅRD ===
story.append(section_header(2, "Viktig endring fra Bård (04.05.2026)"))
story.append(section_rule())
story.append(Paragraph(
    "Bård sendte beskjed om at simuleringsappen som skulle gi oss kostnader og varigheter ikke "
    "fungerer. Han kjører simuleringen <b>manuelt</b> i stedet:",
    ST_BODY))
for item in [
    "Vi sender WBS, kravspesifikasjon og risikoregister til Bård via Oppgaver i Canvas.",
    "Bård fyller inn tids- og kostnadsestimater per WBS-leveranse og sender filen tilbake.",
    "Vi legger tallene inn i Gantt (MS Project) og fortsetter med plan, gjennomføring og rapportering.",
    "Vi sender Bård en personlig melding på Teams etter innlevering, så han ser at filene er klare.",
]:
    story.append(Paragraph(f"&bull;&nbsp;&nbsp;{item}", ST_BODY))
story.append(Paragraph(
    "<b>Konsekvens:</b> Kvaliteten på det vi sender Bård er nå ekstra viktig. Hans estimater bygger "
    "direkte på det vi leverer, så jo tydeligere WBS-en og kravspecen er, desto bedre estimater "
    "får vi tilbake.",
    ST_HIGHLIGHT))

# === 3. DET VI HAR GJORT I DAG ===
story.append(section_header(3, "Det vi har gjort i dag"))
story.append(section_rule())
story.append(Paragraph(
    "Hovedfokus i dag har vært å få planleggingsfasens grunnlag opp på A-nivå og pakke det klart "
    "for innsending til Bård. Hver leveranse ligger i mappa <font name='Courier'>02 - Planlegging</font>.",
    ST_LEAD))

# 3.1
story.append(Paragraph("3.1 Mappestruktur ryddet", ST_H3))
story.append(Paragraph(
    "Filene var spredt i mange undermapper og hadde lange tekniske filnavn. Vi har strammet opp "
    "strukturen og samlet ting tematisk:",
    ST_BODY))
struktur = [
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
story.append(make_table(struktur, col_widths=[5 * cm, 11.5 * cm]))

# 3.2 Kravspec
story.append(Paragraph("3.2 Kravspesifikasjonen — utvidet til 59 krav", ST_H3))
story.append(Paragraph(
    "Kravspesifikasjonen er en strukturert liste over hva bygget «Skal» eller «Bør» oppfylle. "
    "Hver linje har ID, kategori, beskrivelse, prioritet, kobling til en WBS-leveranse, "
    "ansvarlig disiplin (f.eks. arkitekt, elektro), verifikasjonsmetode og kilde.",
    ST_BODY))
story.append(Paragraph(
    "Vi har <b>59 krav</b> fordelt på 9 kategorier — over A-grensen på 40:",
    ST_BODY))
kategorier = [
    ["Kategori", "Antall", "Eksempler"],
    ["Funksjonelt", "15", "Antall elever, klasserom, gymsal, kantine, helseavdeling, SFO."],
    ["Teknisk", "11", "TEK17, ventilasjon, vannbåren varme, WiFi 100 Mbps, SD-anlegg, heis."],
    ["Miljø", "6", "BREEAM Very Good, sedumtak, ladeplasser, energiforbruk, avfallssortering."],
    ["Sikkerhet", "6", "Sprinkler, rømningsveier, adgangskontroll, kamera, alarm, lockdown."],
    ["Uteområde", "7", "Lekeplass m/fallunderlag, ballbinge, sykkelparkering, belysning."],
    ["Akustikk", "3", "Etterklangstid i klasserom, gymsal, fellesarealer (NS 8175)."],
    ["Universell utforming", "4", "TEK17 §12, heis i alle etasjer, ledelinjer, teleslynge."],
    ["Kvalitet", "3", "Null kritiske mangler ved overtakelse, FDV, garantitid."],
    ["Drift/FDV", "4", "Slitesterke materialer, energiavlesning per sone, brukeropplæring."],
]
story.append(make_table(kategorier, col_widths=[4 * cm, 2.0 * cm, 10.5 * cm]))

# 3.3 WBS
story.append(Paragraph("3.3 WBS — 116 linjer i 4 nivåer", ST_H3))
story.append(Paragraph(
    "WBS (Work Breakdown Structure) er en hierarkisk nedbrytning av prosjektet i håndterbare "
    "leveranser. Hver leveranse blir en oppgave i Gantt-diagrammet. Strukturen er bygget i "
    "<b>4 nivåer</b> slik sensorveiledningen krever for A.",
    ST_BODY))
hovedgrener = [
    ["#", "Hovedgren"],
    ["1", "Prosjektledelse og administrasjon"],
    ["2", "Planlegging og prosjektering"],
    ["3", "Forberedelse og riving"],
    ["4", "Skolebygg — bygningsmessige arbeider"],
    ["5", "Skolebygg — tekniske anlegg"],
    ["6", "Utomhus og uteområder"],
    ["7", "Inventar og utstyr (FF&amp;E)"],
    ["8", "Overtakelse og avslutning"],
]
story.append(make_table(hovedgrener, col_widths=[1.5 * cm, 15 * cm]))
story.append(Paragraph(
    "Hver hovedgren er brutt videre ned på nivå 2, 3 og 4. Eksempel på dybde i kjede 4.1 Råbygg:",
    ST_BODY))
story.append(Paragraph(
    "<font name='Courier'>4.1 Råbygg<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;4.1.1 Bærekonstruksjon<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.1 Søyler og dragere (stål/limtre)<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.2 Etasjeskillere (hulldekker)<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.3 Stabiliserende vegger og avstivninger</font>",
    ST_NOTE))
story.append(Paragraph(
    "<b>Total:</b> 116 linjer, hvorav 108 er reelle leveranser (nivå 2 og dypere). Hver leveranse "
    "har avhengigheter (hva som må være ferdig før den kan starte) og kobling til kravspesifikasjonen.",
    ST_BODY))

# 3.4 Risiko
story.append(Paragraph("3.4 Risikoregister — 15 risikoer med scoring og budsjett", ST_H3))
story.append(Paragraph(
    "Risikoregisteret kartlegger ting som kan gå galt og hva vi gjør for å redusere dem. "
    "Hver risiko er scoret 1–5 på sannsynlighet (S) og konsekvens (K). Score = S × K.",
    ST_BODY))
story.append(Paragraph("Kolonnene i registeret:", ST_BODY))
for item in [
    "ID, kategori, beskrivelse av risikoen.",
    "S og K på 1–5-skala. Score-feltet beregner nivå (lav/middels/høy/kritisk).",
    "Risikoeier (overordnet ansvar) vs. tiltaksansvarlig (utfører).",
    "Tiltak for å redusere sannsynligheten og/eller konsekvensen.",
    "Restrisiko etter tiltak (S og K på nytt).",
    "Risikobudsjett: dager + mill. kr som settes av hvis risikoen slår til.",
    "Kobling til WBS-elementet risikoen påvirker.",
]:
    story.append(Paragraph(f"&bull;&nbsp;&nbsp;{item}", ST_BODY))
story.append(Paragraph(
    "<b>Sum risikobudsjett:</b> ca. 158 dager og 26,4 mill. kr totalt. "
    "<b>Topp 3 før tiltak:</b> kvikkleire (R-001, score 20), råvarepriser (R-005, score 12), "
    "ekstremvær (R-009, score 12).",
    ST_INFO))

# 3.5
story.append(Paragraph("3.5 WBS-diagram og presedensdiagram (PowerPoint)", ST_H3))
story.append(Paragraph(
    "WBS-diagrammet viser hierarkiet visuelt over 10 slides. Presedensdiagrammet viser hvordan "
    "leveransene henger sammen i tid og hva som må komme først (Activity-on-Node) over 11 slides. "
    "Begge ligger i <font name='Courier'>02 - Planlegging</font>.",
    ST_BODY))

# 3.6
story.append(Paragraph("3.6 Komplett prosjektplan (PDF)", ST_H3))
story.append(Paragraph(
    "Dette er sammenstillingsdokumentet som binder alt sammen — sammendrag, mål, omfang, "
    "organisering, krav, WBS, presedens, tidsplan, kostnadsbudsjett, risikostyring, "
    "kvalitet/HMS/miljø, kommunikasjon, endringsstyring og vedlegg. Dokumentet har 14 kapitler "
    "over ca. 14 sider. De spesifikke tids- og kostnadstallene fylles inn når Bård svarer.",
    ST_BODY))

# 3.7
story.append(Paragraph("3.7 MS Project-import-fil", ST_H3))
story.append(Paragraph(
    "Vi har laget en Excel som er ferdig formatert for direkte import til MS Project "
    "(File → Open). Når vi får tallene fra Bård, kan vi kopiere dem inn og åpne MS Project — "
    "så har vi en Gantt med korrekt struktur, avhengigheter og baseline.",
    ST_BODY))

# === 4. FILER ===
story.append(section_header(4, "Filer i 02 - Planlegging"))
story.append(section_rule())
filer = [
    ["Filnavn", "Hva"],
    ["Kravspesifikasjon - Nye Hædda barneskole.xlsx", "Kravspec — 59 krav, 9 kategorier."],
    ["WBS - Nye Hædda barneskole.xlsx", "WBS — 116 linjer i 4 nivåer."],
    ["Risikoregister - Nye Hædda barneskole.xlsx", "Risiko — 15 stk med scoring og budsjett."],
    ["WBS-diagram - Nye Hædda barneskole.pptx", "Visuelt WBS-tre."],
    ["Presedensdiagram - Nye Hædda barneskole.pptx", "Avhengigheter mellom leveranser."],
    ["Komplett prosjektplan - Nye Hædda barneskole.pdf", "Sammenstillingsdokumentet."],
    ["Gantt-import (klar for MS Project) - ... .xlsx", "Klar for import når Bård svarer."],
    ["Følgebrev til Bård.md", "Tekst som ligger i zip-en til Bård."],
    ["Til Bård - Nye Hædda barneskole.zip", "Pakken som skal sendes inn."],
    ["Maler og eksempler/", "Maler, eldre utkast, eksempler."],
]
story.append(make_table(filer, col_widths=[9 * cm, 7.5 * cm]))

# === 5. NESTE STEG ===
story.append(section_header(5, "Neste steg"))
story.append(section_rule())
story.append(Paragraph(
    "Pakken er klar til å sendes til Bård. Etter det er det en venteperiode mens han fyller inn "
    "tids- og kostnadsestimater. Når svaret kommer:",
    ST_BODY))
neste = [
    ["Når", "Hva", "Status"],
    ["I morgen tidlig (5. mai)",
     "Lever zip-pakken til Bård via Oppgaver i Canvas + send personlig melding på Teams.",
     status_badge("PLAN", "info")],
    ["5.–12. mai",
     "Vente på Bård. Bruke tiden til finpussing av Komplett prosjektplan og lese pensum.",
     status_badge("PLAN", "info")],
    ["Når Bård svarer",
     "Kopiere tall inn i Gantt-import-fila → importere til MS Project → sette baseline → eksportere.",
     status_badge("PLAN", "info")],
    ["13.–17. mai",
     "Sammenstille fase 2: oppdatere Komplett prosjektplan, sende inn for Bårds godkjenning.",
     status_badge("PLAN", "info")],
    ["18.–26. mai",
     "Fase 3: status tracking i MS Project, månedlige rapporter med S-kurve og earned value.",
     status_badge("PLAN", "info")],
    ["27.–31. mai",
     "Fase 4: skrive sluttrapport. Buffer/finpussing.",
     status_badge("PLAN", "info")],
    ["1. juni 15:00", "Innlevering i WiseFlow.", status_badge("MÅL", "pending")],
]
story.append(make_table(neste, col_widths=[3.3 * cm, 11 * cm, 2.2 * cm], badge_col=2))

# === 6. SENSORVEILEDNING ===
story.append(section_header(6, "Hva sensor ser etter (sensorveiledning)"))
story.append(section_rule())
story.append(Paragraph(
    "100 poeng totalt fordelt over fire områder. For å sikte på A er det særlig viktig at:",
    ST_BODY))
for item in [
    "Filene henger sammen — krav peker til WBS, WBS peker til risiko, risiko peker tilbake til WBS.",
    "Plan, gjennomføring og avslutning forteller én sammenhengende historie.",
    "Vi har baseline + status tracking i MS Project (ikke bare en plan, men også oppfølging).",
    "Månedsrapportene bruker KPI, S-kurve og earned value-analyse — ikke bare beskrivelse.",
    "Endringer dokumenteres med konsekvensanalyse for omfang, tid, kostnad og risiko.",
    "Sluttrapporten har analyse og refleksjon — ikke bare oppsummering.",
    "Profesjonell utforming — ryddige tabeller, figurer, språk.",
]:
    story.append(Paragraph(f"&bull;&nbsp;&nbsp;{item}", ST_BODY))

story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "Spør gjerne hvis noe i strukturen er uklart — alle filene har vi forklart strukturen på i "
    "fanen «Til Bård» internt i Excel-dokumentene, og samme struktur brukes i Komplett "
    "prosjektplan-PDFen.",
    ST_HIGHLIGHT))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF lagret: {OUT}")
