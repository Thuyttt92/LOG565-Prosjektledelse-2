# -*- coding: utf-8 -*-
"""Prosjektrapport — Nye Hædda Barneskole.

Reell prosjektrapport skrevet for prosjekteier (Hædda kommune). Inkluderer
hele dokumentsamlingen — hovedrapport pluss alle vedlegg i samme PDF.
"""
from __future__ import annotations
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable,
)
from reportlab.lib import colors

from apa_style import (
    build_doc, body, bullet_list, pull_quote, info_box, figure, tabell_caption,
    make_table,
    ST_COVER_TITLE, ST_COVER_SUB, ST_COVER_META, ST_COVER_META_BOLD,
    ST_H1, ST_H2, ST_H3, ST_BODY, ST_BULLET, ST_CAPTION, ST_NOTE,
    ST_TOC_H1, ST_TOC_H2, ST_TOC_H3, ST_PULL,
    NAVY, PRIMARY, ACCENT, BORDER, MUTED,
)
from paths import ROOT, ARBEIDSFILER

FIGURER = ARBEIDSFILER / "sluttrapport_figurer"
ENDELIG = ROOT / "05 - Endelig innlevering Hædda Barneskole"
ENDELIG.mkdir(exist_ok=True)
OUT = ENDELIG / "Prosjektrapport - Nye Hædda Barneskole.pdf"
REPORT_TITLE = "Prosjektrapport — Nye Hædda Barneskole"

doc, canvas_maker = build_doc(str(OUT), REPORT_TITLE)
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
def forside():
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("PROSJEKTRAPPORT", ST_COVER_TITLE))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("Nye Hædda Barneskole", ST_COVER_SUB))
    story.append(HRFlowable(width="40%", thickness=2, color=PRIMARY,
                            spaceBefore=0, spaceAfter=20))

    meta = [
        ("Til", "Hædda kommune, kommunestyret"),
        ("Fra", "Prosjektledelsen, Gruppe 4.5"),
        ("Prosjekt", "Ny barneskole — 600 elever"),
        ("Periode", "1. februar 2025 – 15. mai 2026"),
        ("Sluttkost", "800 millioner kroner"),
        ("Sluttdato", "Levert 15. mai 2026"),
        ("Rapportdato", "15. mai 2026"),
        ("Versjon", "1.0 — endelig"),
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
        "Denne rapporten dokumenterer gjennomføringen av prosjekt Nye Hædda Barneskole. "
        "Hele dokumentsamlingen — kommunestyrevedtak, endringsdokumenter, månedsoversikt, "
        "risikoregister og rådata — ligger som vedlegg bakerst i rapporten.",
        ST_NOTE))
    story.append(PageBreak())


# ============================================================
# FORORD
# ============================================================
def forord():
    story.append(Paragraph("Forord", ST_H1))
    body(
        "Hædda kommune vedtok i 2025 å bygge en ny barneskole for å avlaste kapasitetspresset "
        "på eksisterende skoler. Vedtaket satte både kostnadsrammen og sluttdatoen som "
        "faste rammer, med skolestart høsten 2026 som den uforhandlebare tidsfristen. "
        "Prosjektet er gjennomført av kommunens prosjektledelse i samarbeid med leverandører "
        "og fagansvarlige.",
        story)
    body(
        "Rapporten dokumenterer hva som er levert, hva som måtte justeres underveis, og "
        "hva som er status ved overlevering. Den er primært skrevet til kommunestyret, "
        "byggekomiteen og driftsorganisasjonen som overtar bygget. Bakerst ligger alle "
        "vedlegg med formelle dokumenter, økonomiske detaljer og kildemateriale.",
        story)

    info_box(
        "<b>Slik bruker du rapporten.</b> Kapitlene 1–8 gir overordnet status, økonomi og "
        "læringspunkter. Vedleggene A–F bakerst inneholder kommunestyrevedtaket NHB-2026-15, "
        "endringsdokument CR-001, månedsoversikt, risikoregister, fremdriftsdata og "
        "dokumentliste.",
        story)


# ============================================================
# INNHOLDSFORTEGNELSE
# ============================================================
TOC_DATA = [
    ("1   Sammendrag", 0, 5),
    ("2   Om prosjektet", 0, 8),
    ("    2.1  Hva som skulle bygges", 1, 8),
    ("    2.2  Vedtatte rammer", 1, 8),
    ("    2.3  Organisering", 1, 9),
    ("3   Måloppnåelse", 0, 11),
    ("    3.1  Hovedtall ved overlevering", 1, 11),
    ("    3.2  Omfang", 1, 12),
    ("    3.3  Tid", 1, 12),
    ("    3.4  Kostnad", 1, 13),
    ("    3.5  Kvalitet", 1, 13),
    ("4   Gjennomføringen", 0, 14),
    ("    4.1  Slik gikk det måned for måned", 1, 14),
    ("    4.2  Endringen som reddet sluttdatoen", 1, 16),
    ("    4.3  Tre hendelser vi var forberedt på", 1, 18),
    ("    4.4  Kostnadsutvikling", 1, 20),
    ("5   Earned Value-analyse", 0, 22),
    ("6   Risiko og bruk av reserver", 0, 25),
    ("7   Læringspunkter", 0, 27),
    ("8   Anbefalinger til kommunen", 0, 29),
    ("Vedlegg A   Kommunestyrevedtak NHB-2026-15", 0, 31),
    ("Vedlegg B   Endringsdokument CR-001", 0, 34),
    ("Vedlegg C   Månedsoversikt", 0, 37),
    ("Vedlegg D   Risikoregister", 0, 39),
    ("Vedlegg E   Earned Value-data per måned", 0, 40),
    ("Vedlegg F   Kildemateriale og dokumentliste", 0, 42),
]


def innholdsfortegnelse():
    story.append(PageBreak())
    story.append(Paragraph("Innhold", ST_H1))
    story.append(Spacer(1, 0.4 * cm))
    rows = []
    for tittel, niva, side in TOC_DATA:
        stil = ST_TOC_H1 if niva == 0 else ST_TOC_H2
        rows.append([Paragraph(tittel, stil), Paragraph(f"<b>{side}</b>", stil)])
    t = Table(rows, colWidths=[14 * cm, 1.5 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
    ]))
    story.append(t)


# ============================================================
# 1. SAMMENDRAG
# ============================================================
def kap_sammendrag():
    h1("1   Sammendrag")
    body(
        "Vi overleverte Nye Hædda Barneskole til Hædda kommune 15. mai 2026 — på den dagen vi "
        "hadde lovet i det opprinnelige kommunestyrevedtaket. Prosjektet brukte <b>800 "
        "millioner kroner</b>, akkurat det kommunestyret hadde satt av etter justeringen vi "
        "gjorde underveis. Alle 59 krav i kravspesifikasjonen er oppfylt. Bygget besto "
        "ferdigbefaringen uten kritiske mangler. Brannvesenet har gitt brukstillatelse. "
        "Skolen er klar til å ta imot 600 elever når skoleåret begynner i august.",
        story)
    body(
        "Det er enkelt å lese sluttall som disse og tenke at prosjektet gikk uten dramatikk. "
        "Det stemmer ikke. To ganger i løpet av de 16 månedene kunne vi ha kommet skjevt ut — "
        "én gang økonomisk og fremdriftsmessig, og én gang regulatorisk. Begge gangene rettet "
        "vi opp i tide, og vi gjorde det gjennom formelle vedtak og dokumenterte endringer.",
        story)

    h2("Endringen som reddet sluttdatoen")
    body(
        "Tidlig i prosjektet avdekket detaljprosjekteringen at det viktigste byggearbeidet — "
        "selve råbygget — var underestimert. Det reelle behovet var 50 millioner kroner og "
        "to måneder mer enn det opprinnelige estimatet. Råbygget ligger på den kritiske veien "
        "gjennom prosjektet, så uten korrigerende tiltak ville prosjektet samtidig sprenge "
        "kostnadsrammen og bomme på fristen for skolestart.",
        story)
    body(
        "Vi gikk tilbake til kommunestyret med et konkret forslag: utvid kostnadsrammen med "
        "100 millioner kroner — 50 millioner for å dekke den faktiske kostnaden på råbygget, "
        "og 50 millioner for å forsere arbeidet slik at vi holdt sluttdatoen. Vedtaket kom "
        "7. mai 2026, og vi klarte det. Detaljene i vedtaket står i Vedlegg A.",
        story)

    h2("Endringen som sikret brukstillatelse")
    body(
        "I februar 2026 publiserte Direktoratet for samfunnssikkerhet og beredskap en "
        "oppdatert veileder om sprinkler- og rømningssikkerhet. Hadde vi holdt fast på den "
        "opprinnelige løsningen, ville skolen ikke fått brukstillatelse — og dermed ikke "
        "kunnet åpne til skolestart. Endringen ble behandlet som formell endringsforespørsel "
        "CR-001. Vi brukte 5 millioner kroner fra reservefondet på oppgradert VVS-løsning, "
        "og 1 uke forsinkelse ble dekket av tidsbufferen.",
        story)

    pull_quote(
        "Prosjektet leverte til avtalt tid og avtalt pris ikke fordi det var enkelt, men fordi "
        "vi dokumenterte hver endring formelt og fulgte tett opp mot planen i alle 16 måneder.",
        story)

    h2("Tre hendelser vi var forberedt på")
    body(
        "Underveis traff vi på tre hendelser vi visste kunne skje, og som vi hadde satt av "
        "penger og tid til å håndtere. I mai 2025 fant vi en ikke-kartlagt oljetank under "
        "rivingen. Massene rundt var forurenset, og miljøsanering kostet 6 millioner kroner. "
        "I desember 2025 oppstod brann hos vindusprodusenten, og leveransen ble forsinket "
        "halvannen uke. I februar 2026 ble DSB-saken behandlet som CR-001.",
        story)
    body(
        "Sumarisk brukte vi <b>11 millioner kroner av 50 millioner</b> i risikoreserve "
        "(22 prosent), og <b>1,5 av 8 uker tidsbuffer</b> (19 prosent). Reservene var altså "
        "rikelig dimensjonert; vi har god margin igjen ved overtakelse til driftsorganisasjonen.",
        story)

    h2("Det viktigste vi tar med oss")
    bullet_list([
        "<b>Formell endringsstyring fungerte.</b> Uten endringsdokumentene ville vi ikke "
        "kunne forklare etterprøvbart hvorfor sluttkost er 800 millioner og ikke 700.",
        "<b>Å bevare opprinnelig plan parallelt med justert plan</b> gjør at vi i denne "
        "rapporten kan vise hele forløpet fra første estimat til endelig leveranse.",
        "<b>Earned Value-analysen ga objektiv status.</b> Tall fra fremdriftsanalysen "
        "fortalte ærligere hvor vi sto enn den løpende magefølelsen — særlig i de fem "
        "månedene råbygget pågikk i intensiv forseringsfase.",
        "<b>Tidsbufferen var ikke akademisk reserve.</b> Den brukte vi faktisk da "
        "vindusprodusenten fikk brann, og uten den ville sluttdatoen vært i fare.",
    ], story)


# ============================================================
# 2. OM PROSJEKTET
# ============================================================
def kap_om_prosjektet():
    h1("2   Om prosjektet")

    h2("2.1  Hva som skulle bygges")
    body(
        "Hædda kommune skulle bygge en ny barneskole for 1.–10. trinn med plass til inntil "
        "600 elever og rundt 100 ansatte. Behovet kom av kapasitetspress på eksisterende "
        "skoler og et politisk ønske om å gi elevene tidsriktige fysiske læringsmiljøer.",
        story)
    body(
        "Bygget er levert i tre etasjer med 4 608 kvadratmeter grunnflate og rundt "
        "13 824 kvadratmeter bruttoareal — godt innenfor den øvre arealrammen på 14 000 "
        "kvadratmeter. Bygget inneholder klasserom for alle trinn, gymsal på 900 kvadratmeter "
        "som også er tilgjengelig for nærmiljøet utenom skoletid, kantine i første etasje, "
        "samt bibliotek og auditorium i andre etasje. Tekniske anlegg er dimensjonert for "
        "BREEAM Very Good-standard, og det beregnede energiforbruket er under 75 kilowattimer "
        "per kvadratmeter per år.",
        story)

    h2("2.2  Vedtatte rammer")
    body("Kommunestyret vedtok opprinnelig følgende rammer:", story)
    bullet_list([
        "<b>Kostnadsramme:</b> 700 millioner kroner inkludert 50 millioner i risikoreserve. "
        "Rammen ble senere utvidet til 800 millioner gjennom vedtak NHB-2026-15 (Vedlegg A).",
        "<b>Sluttdato:</b> 15. mai 2026 — i god tid før skolestart høsten 2026.",
        "<b>Tidsbuffer:</b> 8 uker mellom vedtatt sluttdato og skolestart.",
        "<b>Kvalitet:</b> 59 spesifikke krav i kravspesifikasjonen fordelt på funksjonelle, "
        "tekniske, miljømessige, sikkerhetsmessige og driftsmessige kategorier.",
    ], story)
    body(
        "I tillegg ble det vedtatt at hovedfristen — skolestart høsten 2026 — er "
        "uforhandlebar. Følgekostnader ved forsinkelse ville være langt høyere enn "
        "kostnadsutvidelser i selve byggeprosjektet. Denne avveiingen — at tid er viktigere "
        "enn kostnad — ligger bak hele logikken i hvordan vi senere håndterte "
        "underestimeringen av råbygget.",
        story)

    h2("2.3  Organisering")
    body(
        "Prosjektorganisasjonen følger den vanlige byggeprosjektmodellen med "
        "kommunestyret som prosjekteier på toppen, prosjektledelse i midten, og "
        "leverandører i bunnen. Tabell 2.1 viser hovedrollene.",
        story)
    tabell_caption("2.1", "Prosjektorganisasjon — roller og ansvar.", story)
    story.append(make_table([
        ["Rolle", "Ansvar"],
        ["Kommunestyret (prosjekteier)",
         "Vedtak om rammer, budsjettendringer og scope-endringer som krever ny baseline"],
        ["Byggekomiteen",
         "Operativ tilsyn på prosjekteiernivå; behandler endringsforespørsler under terskelverdi"],
        ["Prosjektledelse (Gruppe 4.5)",
         "Daglig styring, fremdriftsoppfølging, endringshåndtering, månedsrapportering"],
        ["Byggeleder",
         "Operativ leveranseoppfølging på byggeplass og koordinering av underleverandører"],
        ["Økonomiansvarlig",
         "Påløpsregistrering og kostnadsoppfølging mot arbeidspakkene"],
        ["Fagansvarlige (råbygg, VVS, elektro, automasjon, IKT)",
         "Faglig styring og kvalitetsoppfølging per fagområde"],
        ["HMS-/KS-ansvarlig",
         "Sikkerhet, kvalitet, miljøkrav og varsling mot myndigheter"],
        ["Byggherreombud",
         "Byggherrens interesser på byggeplass og befaringer"],
    ], col_widths=[5.5 * cm, 10 * cm]))


# ============================================================
# 3. MÅLOPPNÅELSE
# ============================================================
def kap_maloppnaelse():
    h1("3   Måloppnåelse")

    h2("3.1  Hovedtall ved overlevering")
    body("Tabell 3.1 viser status mot hver av de fire rammene kommunestyret vedtok.", story)
    tabell_caption("3.1", "Status mot vedtatte rammer ved overlevering 15. mai 2026.", story)
    story.append(make_table([
        ["Ramme", "Vedtatt", "Faktisk", "Vurdering"],
        ["Omfang", "59 krav i kravspesifikasjonen",
         "Alle 59 krav levert", "Måloppnådd"],
        ["Tid", "Sluttdato 15. mai 2026",
         "Levert 15. mai 2026", "Måloppnådd"],
        ["Kostnad", "800 millioner kroner (etter NHB-2026-15)",
         "800 millioner kroner", "Måloppnådd"],
        ["Kvalitet", "Null kritiske mangler ved ferdigbefaring",
         "Null kritiske mangler, brukstillatelse innvilget", "Måloppnådd"],
    ], col_widths=[2.2 * cm, 4.5 * cm, 4.5 * cm, 4.3 * cm]))

    body(
        "I tillegg viser tabell 3.2 utviklingen i reservene. Vi gikk inn med 50 millioner "
        "kroner i risikoreserve og 8 ukers tidsbuffer; ved overlevering hadde vi henholdsvis "
        "39 millioner og 6,5 uker igjen.",
        story)
    tabell_caption("3.2", "Bruk av risikoreserve og tidsbuffer.", story)
    story.append(make_table([
        ["Reserve", "Godkjent", "Brukt", "Igjen", "Andel brukt"],
        ["Risikoreserve (kostnad)", "50 mill. kr", "11 mill. kr", "39 mill. kr", "22 %"],
        ["Tidsbuffer", "8 uker", "1,5 uker", "6,5 uker", "19 %"],
    ], col_widths=[5 * cm, 2.7 * cm, 2.7 * cm, 2.7 * cm, 2.5 * cm]))

    h2("3.2  Omfang")
    body(
        "Alle 59 krav i kravspesifikasjonen er levert. Bygget oppfyller funksjonelle krav "
        "(klasserom, spesialrom, fellesarealer, drift- og personalareal), tekniske krav "
        "(VVS, elektro, automasjon, IKT/sikkerhet), miljøkrav, sikkerhetskrav, uteområde-"
        "krav og krav til universell utforming.",
        story)
    body(
        "Den eneste scope-endringen som ble vedtatt underveis er CR-001, som utvidet sprinkler- "
        "og rømningsdekningen på VVS-anlegget. Endringen er dokumentert i Vedlegg B.",
        story)

    h2("3.3  Tid")
    body(
        "Bygget ble overlevert 15. mai 2026 — på den vedtatte datoen. Opprinnelig estimat "
        "(Baseline 0) ga sluttdato i juli 2026 fordi råbyggsestimatet var underestimert. "
        "Etter at kommunestyret vedtok komprimering av det kritiske arbeidet, ble det "
        "etablert en oppdatert plan (Baseline 1) med sluttdato innenfor frist. Det er denne "
        "planen vi har målt fremdriften mot, og det er denne planen vi har levert iht.",
        story)
    body(
        "Av 8 ukers godkjent tidsbuffer brukte vi 1,5 uker. Bruken kom som følge av brann hos "
        "vindusprodusenten i desember 2025; uten den hendelsen ville buffer-bruken vært null. "
        "De resterende 6,5 ukene mellom 15. mai og skolestart gir kommunen handlerom til "
        "flytting, opplæring og eventuell oppretting av småmangler.",
        story)

    h2("3.4  Kostnad")
    body(
        "Sluttkost er 800 millioner kroner — eksakt lik den vedtatte rammen etter "
        "justeringen. Av godkjent risikoreserve på 50 millioner brukte vi 11 millioner: "
        "6 millioner til miljøsanering etter funn av forurenset masse i mai 2025, og "
        "5 millioner til oppgradert sprinkler- og rømningsløsning i februar 2026.",
        story)
    body(
        "Kostnadseffektiviteten — forholdet mellom verdien vi har skapt og kronene vi har "
        "brukt — ligger på 1,00 ved overlevering. Vi har altså opptjent verdien vi har "
        "betalt for. Detaljene står i kapittel 5.",
        story)

    h2("3.5  Kvalitet")
    body(
        "Ferdigbefaringen ble gjennomført i april 2026 uten kritiske mangler. FDV-"
        "dokumentasjonen for forvaltning, drift og vedlikehold er overlevert samlet ved "
        "sluttovertakelsen. Brannvesenet har vurdert de oppgraderte sprinkler- og "
        "rømningsløsningene som tilfredsstillende, og brukstillatelse er innvilget i god tid "
        "før skolestart.",
        story)


# ============================================================
# 4. GJENNOMFØRINGEN
# ============================================================
def kap_gjennomforing():
    h1("4   Gjennomføringen")

    h2("4.1  Slik gikk det måned for måned")
    body(
        "Gjennomføringsfasen strakk seg fra prosjektstart 1. februar 2025 til overlevering "
        "15. mai 2026 — 16 kalendermåneder med månedlige teamledermøter som styringspunkter. "
        "Tabell 4.1 viser hovedfasene.",
        story)
    tabell_caption("4.1", "Gjennomføringen i hovedfaser.", story)
    story.append(make_table([
        ["Periode", "Fase", "Hva skjedde"],
        ["Måned 1–4 (feb–mai 2025)", "Forprosjekt",
         "Detaljprosjektering, offentlige godkjenninger, konkurransegrunnlag og "
         "kontraktsignering med entreprenører"],
        ["Måned 4–6 (mai–jul 2025)", "Riving og grunnarbeid",
         "Miljøsanering, riving av eksisterende bygg, grunnarbeid. "
         "Funn av forurenset masse i mai"],
        ["Måned 7–11 (aug–des 2025)", "Råbygg — komprimert",
         "Bærekonstruksjon, tak, fasade. Komprimert iht. NHB-2026-15. "
         "Brann hos vindusprodusent i desember"],
        ["Måned 12–15 (jan–apr 2026)", "Innvendig og tekniske anlegg",
         "Innvendig komplettering, VVS, elektro, automasjon, IKT, "
         "inventar. DSB-saken behandlet i februar"],
        ["Måned 16 (mai 2026)", "Overtakelse",
         "Testing, prøvedrift, ferdigbefaring, brukeropplæring og "
         "sluttovertakelse 15. mai"],
    ], col_widths=[3.5 * cm, 3.5 * cm, 9 * cm]))
    body(
        "Vi har dokumentert hver enkelt måned med egen statusrapport som inneholder fremdrift, "
        "kostnader, avvik og risikobilde — totalt 16 månedsrapporter. Et sammendrag av disse "
        "ligger i Vedlegg C.",
        story)

    h2("4.2  Endringen som reddet sluttdatoen")
    body(
        "Den viktigste enkeltbeslutningen i prosjektet ble fattet 7. mai 2026. Da behandlet "
        "kommunestyret saken NHB-2026-15 — et forslag om å utvide kostnadsrammen mot å "
        "forsere det kritiske byggearbeidet, og dermed holde sluttdatoen.",
        story)

    h3("Det som ble oppdaget")
    body(
        "Detaljprosjekteringen i begynnelsen av prosjektet avdekket noe ubehagelig: arbeidet "
        "med selve råbygget — bærekonstruksjon, tak, fasade — var underestimert i det "
        "opprinnelige tilbudet. Det reelle behovet var 50 millioner kroner mer, og det krevde "
        "to måneder lengre tid. Råbygget ligger på prosjektets kritiske vei, så enhver "
        "forsinkelse her ville forskyve sluttdatoen direkte.",
        story)
    body("Uten korrigerende tiltak ville prosjektet ende slik:", story)
    bullet_list([
        "Totalkostnad: 750 millioner kroner — 50 millioner over rammen.",
        "Sluttdato: juli 2026 — om lag seks uker etter den vedtatte fristen.",
        "Konsekvens: skolen åpner ikke til skolestart, og kommunen må leie midlertidige "
        "skolelokaler med tilhørende følgekostnader.",
    ], story)

    figure(FIGURER / "figur_07_baseline_sammenligning.png", story, "4.1",
           "Tre scenarioer: opprinnelig vedtatt plan, prognose før korrigerende tiltak, og "
           "endelig plan etter kommunestyrets vedtak. Vedtaket utvidet rammen med "
           "100 millioner mot at sluttdatoen ble holdt.")

    h3("Vedtaket og hva pengene gikk til")
    body(
        "Kommunestyret behandlet saken og vedtok å utvide kostnadsrammen fra 700 til "
        "800 millioner kroner — fordelt på 50 millioner til den faktiske kostnaden på "
        "råbygget og 50 millioner til selve komprimeringen. Komprimeringskostnaden gikk til "
        "fire konkrete tiltak vist i tabell 4.2.",
        story)
    tabell_caption("4.2", "Slik ble komprimeringskostnaden på 50 millioner brukt.", story)
    story.append(make_table([
        ["Tiltak", "Kostnad", "Begrunnelse"],
        ["Overtid og ekstra mannskap", "18 mill. kr",
         "Helgearbeid og ettermiddagsskift på bærekonstruksjon og tak"],
        ["Parallelle skift (natt)", "12 mill. kr",
         "Tre måneder med nattskift på fasade og innvendig arbeid for å "
         "parallellisere kritiske aktiviteter"],
        ["Premium-leveranser av materialer", "14 mill. kr",
         "Hasteleveranser av tak- og fasadeelementer (om lag 30 % høyere stykkpris)"],
        ["Forsering hos underleverandører", "6 mill. kr",
         "Tillegg til underleverandørkontrakter for prioritert produksjonskapasitet"],
        ["SUM", "50 mill. kr", "Som vedtatt"],
    ], col_widths=[5.2 * cm, 2.3 * cm, 8.5 * cm]))

    pull_quote(
        "Vedtaket sier i praksis at tid er viktigere enn kostnad. Det er en anerkjennelse av "
        "at konsekvensene av å bomme på skolestart er større enn 100 millioner kroner.",
        story)

    body(
        "Den største praktiske utfordringen var nattskiftene. De krever særskilt HMS-"
        "oppfølging og legger en koordineringsbyrde på byggeleder. Vi løste det ved å innføre "
        "et ukentlig SHA-statusmøte gjennom hele råbyggsperioden.",
        story)

    h2("4.3  Tre hendelser vi var forberedt på")
    body(
        "Et godt prosjekt unngår ikke hendelser; det forbereder seg på dem. Vi gikk inn i "
        "prosjektet med et risikoregister på 16 punkter og en risikoreserve på 50 millioner. "
        "Underveis materialiserte tre av risikoene seg. Alle ble håndtert innenfor reservene.",
        story)

    figure(FIGURER / "figur_06_hendelsestidslinje.png", story, "4.2",
           "Tidslinjen viser når i prosjektet de tre hendelsene inntraff. Ingen av dem endret "
           "sluttdatoen.")

    h3("Mai 2025: Den ukartlagte oljetanken")
    body(
        "Under rivingen av det eksisterende bygget i mai 2025 fant vi en eldre, ikke-kartlagt "
        "nedgravd oljetank. Massene rundt var forurenset. Vi måtte gjennomføre miljøsanering "
        "med separat bortkjøring og prøvetaking. Kostnaden ble 6 millioner kroner, dekket fra "
        "risikoreserven. En ukes forsinkelse ble absorbert i tidsplanen mellom riving og "
        "grunnarbeid. Statsforvalter ble formelt varslet.",
        story)

    h3("Desember 2025: Brannen hos vindusprodusenten")
    body(
        "I desember 2025 oppstod brann hos vindusprodusenten. Leveransen ble forsinket med "
        "halvannen uke. Vi utredet bytte til alternativ leverandør, men kombinasjonen av "
        "produksjonstid og merkostnad gjorde det uforsvarlig. Vi trakk 1,5 uker fra "
        "tidsbufferen og planla om de etterfølgende arbeidene. Dette er det eneste tilfellet "
        "i hele prosjektet hvor vi faktisk brukte av tidsbufferen.",
        story)

    h3("Februar 2026: DSB-veilederen (CR-001)")
    body(
        "Direktoratet for samfunnssikkerhet og beredskap publiserte i januar 2026 oppdatert "
        "veileder om sprinkler- og rømningsdekning. Veilederen trådte i kraft før vår "
        "ferdigstillelse. Hadde vi ignorert den, ville vi risikert å ikke få brukstillatelse. "
        "Endringen ble behandlet som formell endringsforespørsel CR-001 (Vedlegg B). "
        "Tilleggskostnad: 5 millioner kroner fra risikoreserven. Tidskonsekvens: 1 uke fra "
        "tidsbufferen.",
        story)

    h2("4.4  Kostnadsutvikling")
    body(
        "Kostnadsforbruket har vært ujevnt fordelt gjennom de 16 månedene. Figur 4.3 viser "
        "månedlig påløpt kostnad og kumulativt forbruk.",
        story)
    figure(FIGURER / "figur_08_ac_per_maned.png", story, "4.3",
           "Månedlig påløpt kostnad (blå stolper) og kumulativ totalkostnad (rød linje). "
           "Topper i råbyggsperioden (måned 7–11) og innvendigfasen (måned 12–14).",
           width_cm=15.5)
    body(
        "Hovedinntrykket er to klare belastningstopper. Den første ligger i råbyggsperioden "
        "fra august til desember 2025, hvor selve råbygget kostet om lag 240 millioner — "
        "30 prosent av hele rammen på fem måneder. Den andre kommer i januar–mars 2026 når "
        "innvendig komplettering og tekniske anlegg pågår parallelt.",
        story)
    figure(FIGURER / "figur_03_kostnadsfordeling.png", story, "4.4",
           "Slik fordelte kostnadene seg på prosjektets åtte hovedområder. Skolebygg — "
           "bygningsmessige arbeider er størst med 360 millioner (45 prosent), drevet av "
           "råbygget alene som utgjorde 240 millioner.")


# ============================================================
# 5. EARNED VALUE-ANALYSE
# ============================================================
def kap_evm():
    h1("5   Earned Value-analyse")
    body(
        "Vi har fulgt prosjektets fremdrift med Earned Value Management — en metode for å "
        "måle om vi får ut den verdien vi har planlagt for de pengene vi har brukt. Denne "
        "delen gir et samlet bilde av analysen ved overlevering.",
        story)

    h2("Tre tall og hva de betyr")
    body("Tre størrelser danner grunnlaget for fremdriftsanalysen:", story)
    bullet_list([
        "<b>Planlagt verdi (PV)</b> — hvor mye av prosjektet vi skulle ha fullført ved en "
        "gitt dato, målt i kroner. Dette kommer fra Baseline 1, den oppdaterte planen etter "
        "NHB-2026-15.",
        "<b>Opptjent verdi (EV)</b> — hvor mye av prosjektet vi faktisk har fullført ved "
        "samme dato, beregnet som fullføringsgraden på hver arbeidspakke ganget med pakkens "
        "budsjett.",
        "<b>Faktisk kostnad (AC)</b> — hva prosjektet faktisk har brukt fram til samme dato.",
    ], story)
    body(
        "Fra disse tre størrelsene utleder vi to forholdstall: <b>kostnadseffektivitet "
        "(CPI = EV/AC)</b> som forteller om vi får ut den verdien vi betaler for, og "
        "<b>fremdriftseffektivitet (SPI = EV/PV)</b> som forteller om vi er forut eller bak "
        "planen. Begge bør ligge på eller over 1,00.",
        story)

    figure(FIGURER / "figur_01_s_kurve.png", story, "5.1",
           "S-kurven viser hvordan planlagt verdi (blå), opptjent verdi (grønn) og faktisk "
           "kostnad (rød) har utviklet seg i de 16 månedene. Kurvene følger hverandre tett "
           "gjennom hele forløpet — prosjektet har styrt etter planen med høy presisjon.")
    figure(FIGURER / "figur_02_cpi_spi_trend.png", story, "5.2",
           "Kostnadseffektivitet og fremdriftseffektivitet gjennom prosjektet. Det grønne "
           "feltet markerer akseptabelt avviksområde. Begge tallene konvergerer mot 1,00 ved "
           "overlevering.")

    body("Tre observasjoner:", story)
    bullet_list([
        "<b>Kostnadseffektiviteten holdt seg på 1,00 hele veien.</b> Prosjektet har ikke hatt "
        "kostnadssprekkninger mot Baseline 1.",
        "<b>Fremdriftseffektiviteten var høyere enn 1,00 i de første månedene.</b> "
        "Detaljprosjekteringen ble fullført raskere enn lineær fordeling tilsier — en "
        "metodisk effekt, ikke faktisk forsering.",
        "<b>Ingen periode med kritisk avvik.</b> Bruken av reserve og buffer har ikke gitt "
        "utslag som krever korrigerende tiltak.",
    ], story)

    h2("Sluttverdier")
    tabell_caption("5.1", "Sluttverdier i Earned Value-analysen.", story)
    story.append(make_table([
        ["Størrelse", "Verdi", "Hva det betyr"],
        ["Budsjett ved sluttføring (BAC)", "800 mill. kr",
         "Det vi hadde råd til å bruke etter NHB-2026-15"],
        ["Planlagt verdi (PV)", "800 mill. kr",
         "Det vi skulle ha skapt iht. Baseline 1"],
        ["Opptjent verdi (EV)", "800 mill. kr",
         "Det vi faktisk har skapt"],
        ["Faktisk kostnad (AC)", "800 mill. kr",
         "Det vi faktisk har brukt"],
        ["Kostnadseffektivitet (CPI)", "1,00",
         "Vi har fått ut den verdien vi har betalt for"],
        ["Fremdriftseffektivitet (SPI)", "1,00",
         "Vi har levert i tråd med planen"],
        ["Prognose sluttkost (EAC)", "800 mill. kr",
         "Prognose for hva prosjektet ville koste totalt"],
        ["Avvik mot BAC (VAC)", "0 mill. kr",
         "Ingen prognosticert overskridelse"],
        ["Brukt risikoreserve", "11 av 50 mill. kr",
         "22 prosent — god margin igjen"],
        ["Brukt tidsbuffer", "1,5 av 8 uker",
         "19 prosent — god margin igjen"],
    ], col_widths=[5.5 * cm, 3 * cm, 7 * cm]))

    info_box(
        "<b>En faglig presisering.</b> At alle tre kurvene ender på 800 millioner kroner er "
        "ikke et tegn på flaks. Det er et tegn på at vi har styrt aktivt mot Baseline 1 "
        "gjennom hele prosjektet, og at hver endring har vært formelt dokumentert slik at "
        "planen alltid har vært en realistisk plan å måle mot.",
        story)


# ============================================================
# 6. RISIKO
# ============================================================
def kap_risiko():
    h1("6   Risiko og bruk av reserver")
    body(
        "Prosjektet hadde 16 identifiserte risikoer ved oppstart. Tre av disse ble realisert. "
        "De øvrige 13 forble i overvåket tilstand og krevde ingen aktiv respons. Det "
        "fullstendige risikoregisteret med sluttvurdering ligger i Vedlegg D.",
        story)
    figure(FIGURER / "figur_10_risikomatrise.png", story, "6.1",
           "De tre realiserte risikoene plassert i risikomatrisen. Alle lå i oransje sone — "
           "middels til høy sannsynlighet og konsekvens.",
           width_cm=13)

    h2("Slik utviklet bruken av reserven seg")
    figure(FIGURER / "figur_04_risikobudsjett.png", story, "6.2",
           "Bruk av risikoreserven gjennom prosjektet. To uttak: 6 millioner i mai 2025 "
           "(oljetanken) og 5 millioner i februar 2026 (DSB-veilederen). Resterende 39 millioner.",
           width_cm=15.5)
    figure(FIGURER / "figur_05_tidsbuffer.png", story, "6.3",
           "Bruk av tidsbufferen. Eneste uttak: 1,5 uker i desember 2025 ved brannen hos "
           "vindusprodusenten. Resterende 6,5 uker.",
           width_cm=15.5)
    body(
        "Mønsteret er verdt å merke seg: risikoreserven ble brukt to ganger, hver gang "
        "knyttet til en konkret hendelse. Tidsbufferen ble derimot brukt bare én gang. Begge "
        "ressurser har god margin igjen, som er ønskelig ved overtakelse — eventuelle mangler "
        "eller etterbestillinger i garantiperioden kan dekkes innenfor disse rammene.",
        story)


# ============================================================
# 7. LÆRINGSPUNKTER
# ============================================================
def kap_laeringspunkter():
    h1("7   Læringspunkter")
    body(
        "Disse fire punktene tar vi med oss som det mest sentrale fra prosjektet. De er "
        "skrevet med tanke på fremtidige byggeprosjekter i kommunen.",
        story)

    h2("Endringer som ikke dokumenteres formelt, blir usynlige")
    body(
        "Det viktigste verktøyet vi hadde var de to endringsdokumentene (NHB-2026-15 og "
        "CR-001). Hvert av dem har egen konsekvensanalyse for omfang, tid, kostnad og "
        "kvalitet. Uten disse dokumentene ville denne rapporten måtte argumentere muntlig "
        "for hvorfor sluttkost er 800 millioner og ikke 700. Med dokumentene er argumentet "
        "etterprøvbart.",
        story)

    h2("Å bevare opprinnelig plan parallelt med den justerte er gull verdt")
    body(
        "Det ville vært enklere å lagre kun den justerte planen i MS Project og slette den "
        "opprinnelige etter kommunestyrevedtaket. Vi valgte å beholde begge. Det viste seg å "
        "være avgjørende for at denne rapporten kan vise hele forløpet — fra opprinnelig "
        "estimat via dokumentert vedtak til revidert plan og faktisk gjennomføring.",
        story)

    h2("Earned Value-analysen ga objektiv status uavhengig av magefølelse")
    body(
        "I praksis er det fristende å oppdatere prosent fullført på arbeidspakker for å "
        "«føle» at man har kontroll. Earned Value-analysen tvinger oss til å se det samme "
        "fra to vinkler — hva som er opptjent i kroner og hva som faktisk er brukt — og gjør "
        "avvik kvantitative i stedet for følelsesmessige. Dette ble særlig tydelig i månedene "
        "rundt råbygget.",
        story)

    h2("Tidsbufferen var ikke akademisk reserve")
    body(
        "Brannen hos vindusprodusenten i desember 2025 viste verdien av å ha satt av åtte "
        "uker tidsbuffer i planfasen. Da risikoen materialiserte seg, transformerte "
        "tidsbufferen en potensiell krise til en planlagt justering uten kostnadskonsekvens.",
        story)


# ============================================================
# 8. ANBEFALINGER
# ============================================================
def kap_anbefalinger():
    h1("8   Anbefalinger til kommunen")
    body(
        "Følgende anbefalinger gjelder for tiden etter overlevering. De er rettet til "
        "kommunen som prosjekteier og fremtidig driftseier.",
        story)

    h2("8.1  Gevinstoppfølging med årlig kadens")
    body(
        "Den opprinnelige business casen anslo en nettogevinst på 109 millioner kroner over "
        "60 år. Etter kostnadsutvidelsen i NHB-2026-15 er anslaget redusert til om lag "
        "59 millioner — fortsatt positiv, men forskjøvet i tid. Realiseringen avhenger av "
        "faktisk drift. Vi anbefaler at driftsorganisasjonen utarbeider en "
        "gevinstrealiseringsplan med måltall for driftskostnad per elev, energiforbruk per "
        "kvadratmeter og brukertilfredshet. Kadensen bør være årlig de første tre årene.",
        story)

    h2("8.2  Årlig sikkerhetsvurdering av sprinkler- og rømningsløsningene")
    body(
        "De oppgraderte løsningene fra CR-001 bør gjennomgås av brannvesenet hvert år de "
        "første tre årene. Dette sikrer at kommunens etterlevelse av DSB-kravene holder seg, "
        "og at eventuelle senere veilederrevisjoner fanges opp tidlig.",
        story)

    h2("8.3  Erfaringsoverføring til kommunens prosjektmal")
    body(
        "NHB-2026-15 og CR-001 er konkrete eksempler på henholdsvis schedule crashing og "
        "regulatorisk scope-endring. Vi anbefaler at kommunen tar disse inn i sin interne "
        "prosjektledelsesmal som referansecase for fremtidige prosjekter.",
        story)

    h2("8.4  Oppfølgende brukeropplæring etter seks måneder")
    body(
        "Den bygde løsningen omfatter avanserte tekniske systemer — særlig automasjon "
        "(sentral driftskontroll) og IKT/sikkerhet. Initial brukeropplæring er gjennomført i "
        "overtakelsesfasen, men erfaringsmessig er det først etter et halvår med drift at de "
        "virkelige opplæringsbehovene melder seg. Vi anbefaler en oppfølgende opplæringsbolk "
        "etter seks måneders drift.",
        story)

    h2("8.5  Bevar resterende reserver til garantiperioden")
    body(
        "Av godkjent risikoreserve på 50 millioner er 39 millioner ubrukt ved overlevering. "
        "Av godkjent tidsbuffer på 8 uker er 6,5 uker ubrukt. Vi anbefaler at disse reservene "
        "bevares i kommunens regnskap fram til garantiperioden er utløpt, som dekning for "
        "eventuelle mangler eller etterbestillinger som måtte dukke opp i driftens første år.",
        story)


# ============================================================
# VEDLEGG A — KOMMUNESTYREVEDTAKET
# ============================================================
def vedlegg_a():
    h1("Vedlegg A   Kommunestyrevedtak NHB-2026-15")
    body(
        "Dette vedlegget gjengir kommunestyrets vedtak om budsjettjustering og komprimering "
        "av kritisk aktivitet, fattet 7. mai 2026. Vedtaket er den formelle hjemmelen for "
        "rammeutvidelsen fra 700 til 800 millioner kroner.",
        story)

    h2("Bakgrunn")
    body(
        "Kommunestyret vedtok den opprinnelige rammen for prosjekt Nye Hædda Barneskole til "
        "700 millioner kroner med planlagt sluttdato 15. mai 2026, basert på en "
        "gjennomføringstid på 15 måneder fra prosjektstart 1. februar 2025.",
        story)
    body(
        "Detaljprosjekteringen avdekket at arbeidspakke 4.1 Råbygg var underestimert i den "
        "opprinnelige planen. Aktivitetens reelle behov var +50 millioner kroner og +2 "
        "måneder ut over det opprinnelige estimatet — varigheten økte fra 5 til 7 måneder, "
        "og kostnaden fra 140 til 190 millioner. Aktiviteten ligger på prosjektets kritiske "
        "vei, og overskridelsen forplantet seg derfor direkte til prosjektets totalkostnad "
        "og sluttdato.",
        story)
    body(
        "Prognose før korrigerende tiltak: totalkostnad 750 millioner (+50 over rammen), "
        "sluttdato juli 2026 (forsinkelse ca. 2 måneder). Uten korrigerende tiltak ville "
        "både kostnadsrammen og tidsrammen brytes samtidig.",
        story)

    h2("Forslag til løsning")
    body(
        "Prosjektledelsen anbefalte å komprimere aktivitet 4.1 Råbygg ved å øke "
        "ressurspådraget gjennom overtid, parallelle skift, premium-leveranser og forsering "
        "hos underleverandører. Komprimeringen anslås å medføre en ekstra kostnad på "
        "50 millioner ut over den allerede avdekkede overskridelsen, og innebærer at "
        "aktivitetens varighet bringes tilbake fra 7 til 5 måneder.",
        story)

    h2("Konsekvenser")
    tabell_caption("A.1",
                   "Konsekvensoversikt — opprinnelig vedtak, prognose uten tiltak, vedtatt løsning.",
                   story)
    story.append(make_table([
        ["", "Opprinnelig vedtak", "Prognose uten tiltak", "Med komprimering"],
        ["Totalkostnad", "700 mill. kr", "750 mill. kr", "800 mill. kr"],
        ["Sluttdato", "15. mai 2026", "juli 2026", "15. mai 2026"],
        ["Avvik fra vedtatt", "—", "+50 mill. / +2 mnd", "+100 mill. / 0 mnd"],
    ], col_widths=[3 * cm, 4 * cm, 4 * cm, 4.5 * cm]))

    h2("Vurdering av alternativer")
    body(
        "Tid er definert som den viktigste rammebetingelsen. Skolen skal stå klar til "
        "skolestart høsten 2026. En forsinkelse til juli 2026 vil utløse betydelige "
        "følgekostnader til midlertidige skolelokaler og omdømmebelastning.",
        story)
    bullet_list([
        "<b>Ikke iverksette tiltak:</b> bryter både tids- og kostnadsramme. Ikke akseptabelt.",
        "<b>Redusere omfang:</b> ville bryte kravspesifikasjonen og opprinnelig bestilling.",
        "<b>Komprimering (anbefalt):</b> tidsrammen overholdes fullt ut, kostnadsrammen "
        "utvides med 100 millioner. Risikoen er konsentrert til én kjent aktivitet på den "
        "kritiske veien og lar seg styre med tett oppfølging.",
    ], story)

    h2("Vedtak")
    body("Kommunestyret fattet følgende vedtak 7. mai 2026:", story)
    bullet_list([
        "Budsjettrammen for prosjekt Nye Hædda Barneskole utvides fra 700 millioner kroner "
        "til 800 millioner kroner (en økning på 100 millioner).",
        "Prosjektledelsen gis fullmakt til å iverksette komprimering av aktivitet 4.1 Råbygg "
        "for å overholde vedtatt sluttdato 15. mai 2026.",
        "Prosjektledelsen rapporterer status på den komprimerte aktiviteten månedlig til "
        "byggekomiteen fram til aktiviteten er ferdigstilt.",
    ], story)


# ============================================================
# VEDLEGG B — CR-001
# ============================================================
def vedlegg_b():
    h1("Vedlegg B   Endringsdokument CR-001")
    body(
        "Dette vedlegget dokumenterer endringsforespørsel CR-001 — oppgradert sprinkler- og "
        "rømningsdekning på VVS-anlegget iht. ny DSB-veileder. Vedtatt på teamledermøte "
        "3. februar 2026.",
        story)

    h2("Bakgrunn")
    body(
        "Direktoratet for samfunnssikkerhet og beredskap publiserte i januar 2026 en oppdatert "
        "veileder for sprinklerdekning og rømningsskilting i kommunale byggeprosjekter. "
        "Veilederen trer i kraft før prosjektets ferdigstillelse og påvirker arbeidspakke "
        "5.1 VVS direkte. Endringen kan ikke ignoreres uten å risikere at skolen ikke får "
        "brukstillatelse — i praksis samme alvorlighetsgrad som en forsinkelse på selve "
        "byggetiden.",
        story)

    h2("Foreslått endring")
    body(
        "Oppgradere sprinklerdekning og forsterke rømningsskilting i hele bygningsmassen iht. "
        "ny DSB-veileder. Omfanget av leveranse 5.1 VVS utvides tilsvarende. Eksisterende "
        "VVS-entreprenør tar tilleggsbestilling og innarbeider endringen i pågående "
        "installasjonssekvens.",
        story)

    h2("Konsekvensanalyse")
    tabell_caption("B.1", "Konsekvensvurdering CR-001 på fem dimensjoner.", story)
    story.append(make_table([
        ["Dimensjon", "Påvirkning", "Beskrivelse"],
        ["Omfang", "Middels — scope-utvidelse på 5.1",
         "Sprinklerdekning utvides og rømningsskilting forsterkes iht. ny DSB-veileder"],
        ["Tid", "Lav — 1 uke forskyvning",
         "Absorberes innenfor godkjent tidsbuffer (8 uker)"],
        ["Kostnad", "Middels — 5 mill. kr fra risikoreserve",
         "Tilleggskostnaden dekkes av godkjent risikoreserve. BAC påvirkes ikke"],
        ["Kvalitet", "Forbedring",
         "Strengere sikkerhetsstandard for sprinkler og rømning"],
        ["Risiko", "Forbedring",
         "Bedre brann- og rømningssikkerhet reduserer HMS-risiko under drift"],
    ], col_widths=[2.7 * cm, 4 * cm, 8.5 * cm]))

    h2("Beslutning")
    body(
        "Godkjent av prosjekteier 3. februar 2026. Beslutningsbegrunnelse: regulatorisk krav "
        "som ikke kan ignoreres. Kostnaden dekkes av godkjent risikoreserve, og forsinkelsen "
        "absorberes i godkjent tidsbuffer. Vedtatt sluttdato 15. mai 2026 og totalramme "
        "800 millioner kroner opprettholdes uendret.",
        story)

    h2("Implementering")
    bullet_list([
        "Kontraktstillegg med VVS-entreprenør på 5.1.",
        "Oppdatert installasjonsplan og bemanningsskjema for 5.1 VVS.",
        "Replanlegging av etterfølgende innvendige arbeider.",
        "Oppdatert risikoregister.",
        "Oppdatert kostnadsprognose med 5 millioner uttrekk fra risikoreserve.",
    ], story)
    body(
        "Ansvarlig: prosjektleder. Frist: 14. mars 2026. Lukket etter ferdigbefaring i april "
        "2026 da brannvesenet godkjente løsningen.",
        story)


# ============================================================
# VEDLEGG C — MÅNEDSOVERSIKT
# ============================================================
def vedlegg_c():
    h1("Vedlegg C   Månedsoversikt")
    body(
        "Tabellen viser kumulativ status ved slutten av hver måned. Detaljerte "
        "månedsrapporter med fullstendige tabeller og figurer ligger i mappen "
        "<i>03 - Gjennomføring/Månedsrapporter/</i>.",
        story)

    from log565_master_data import alle_måneder, MÅNEDER, HENDELSER

    tabell_caption("C.1", "Månedsoversikt — kumulative tall.", story)
    rader = [["Mnd", "Periode", "AC kum.", "% fullført", "CPI", "SPI", "Hendelse"]]
    hendelse_per_mnd = {h.måned: h.tittel for h in HENDELSER}
    for evm in alle_måneder():
        hendelse = hendelse_per_mnd.get(evm.måned, "")
        if len(hendelse) > 40:
            hendelse = hendelse[:38] + "…"
        rader.append([
            f"M{evm.måned}", MÅNEDER[evm.måned][0],
            f"{evm.ac_kum:.0f} mill.", f"{evm.pct_complete:.0f} %",
            f"{evm.cpi:.3f}", f"{evm.spi:.3f}", hendelse or "—",
        ])
    story.append(make_table(rader,
                              col_widths=[1.2 * cm, 2.5 * cm, 2 * cm, 1.8 * cm,
                                          1.5 * cm, 1.5 * cm, 5.5 * cm]))


# ============================================================
# VEDLEGG D — RISIKOREGISTER
# ============================================================
def vedlegg_d():
    h1("Vedlegg D   Risikoregister med sluttvurdering")
    body(
        "De viktigste risikoene fra prosjektets risikoregister med status ved overlevering.",
        story)
    tabell_caption("D.1", "Realiserte risikoer i gjennomføringsfasen.", story)
    story.append(make_table([
        ["ID", "Beskrivelse", "Realisert", "Konsekvens", "Status"],
        ["R-05", "Ukartlagt forurensning under riving", "Mai 2025",
         "6 mill. kr fra risikoreserve. 1 uke absorbert i lokal slack.",
         "Lukket. Statsforvalter varslet"],
        ["R-06", "Regulatorisk endring fra DSB", "Februar 2026",
         "5 mill. kr fra risikoreserve. 1 uke fra tidsbuffer. Eskalert til CR-001",
         "Lukket. Brukstillatelse innvilget"],
        ["R-07", "Leveransesvikt fra underleverandør", "Desember 2025",
         "Ingen kostnad. 1,5 uker fra tidsbuffer. Arbeider replanlagt",
         "Lukket. Sluttdato holdt"],
    ], col_widths=[1.3 * cm, 4 * cm, 2.4 * cm, 4.5 * cm, 4 * cm]))
    body(
        "De øvrige 13 risikoene i registeret forble i overvåket tilstand gjennom hele "
        "gjennomføringsfasen og krevde ingen aktiv respons. Disse omfatter blant annet "
        "værforhold på byggeplass, sykefravær i kritisk fagmiljø, leveranseforsinkelser fra "
        "øvrige underleverandører, kostnadsutvikling på materialer, og regulatoriske "
        "endringer på andre fagområder enn DSB-veilederen. Risikoregisteret er vedlikeholdt "
        "løpende gjennom månedsrapportene.",
        story)


# ============================================================
# VEDLEGG E — EVM-DATA
# ============================================================
def vedlegg_e():
    h1("Vedlegg E   Earned Value-data per måned")
    body(
        "Detaljerte fremdriftsdata for alle 16 månedene. Tabellen gjengir kumulative tall, "
        "som er grunnlaget for figurene i kapittel 5.",
        story)

    from log565_master_data import alle_måneder, MÅNEDER

    tabell_caption("E.1", "Kumulativ PV, EV og AC per måned (i millioner kroner).", story)
    rader = [["Måned", "Periode", "PV kum.", "EV kum.", "AC kum.", "CPI", "SPI"]]
    for evm in alle_måneder():
        rader.append([
            f"M{evm.måned}", MÅNEDER[evm.måned][0],
            f"{evm.pv_kum:.0f}", f"{evm.ev_kum:.0f}", f"{evm.ac_kum:.0f}",
            f"{evm.cpi:.3f}", f"{evm.spi:.3f}",
        ])
    story.append(make_table(rader,
                              col_widths=[1.4 * cm, 2.6 * cm, 2 * cm, 2 * cm,
                                          2 * cm, 1.7 * cm, 1.7 * cm]))


# ============================================================
# VEDLEGG F — KILDEMATERIALE
# ============================================================
def vedlegg_f():
    h1("Vedlegg F   Kildemateriale og dokumentliste")
    body(
        "Dette vedlegget peker til kildedokumenter som ligger i prosjektmappen. Disse "
        "dokumentene utgjør grunnlaget for hovedrapportens innhold og er bevart i opprinnelig "
        "form for sporbarhet.",
        story)

    h2("Faseleveranser")
    bullet_list([
        "<i>01 - Initiering/Prosjektforslag.pdf</i> og <i>Konseptløsning.pdf</i> — opprinnelig "
        "behovsbeskrivelse og konseptuell byggeløsning.",
        "<i>02 - Planlegging/Komplett prosjektplan.pdf</i> — fullstendig plangrunnlag.",
        "<i>02 - Planlegging/Kravspesifikasjon.xlsx</i> — 59 krav i 9 kategorier.",
        "<i>02 - Planlegging/WBS.xlsx</i> og <i>WBS-diagram.pptx</i> — 32 arbeidspakker i "
        "fire nivåer.",
        "<i>02 - Planlegging/Risikoregister.xlsx</i> — 16 identifiserte risikoer.",
        "<i>02 - Planlegging/MS Project - Plan (Baseline 0).mpp</i> — opprinnelig Gantt-plan.",
        "<i>03 - Gjennomføring/Månedsrapporter/</i> — 16 månedsrapporter (docx + pdf).",
        "<i>03 - Gjennomføring/EVM-arbeidsbok.xlsx</i> — fullstendig Earned Value-grunnlag.",
        "<i>03 - Gjennomføring/MS Project tracking-instruks.xlsx</i> — instruks for tracking.",
    ], story)

    h2("Kildemateriale")
    bullet_list([
        "<i>Vedlegg/A - Kildemateriale fra Bård/godkjenning-av-budsjettendring.pdf</i> — det "
        "formelle kommunestyrevedtaket (vedlegg A i denne rapporten gjengir innholdet).",
        "<i>Vedlegg/A - Kildemateriale fra Bård/månedsrapporter.pdf</i> — 16 "
        "teamledermøtereferater med fremdrifts- og kostnadsdata.",
        "<i>Vedlegg/A - Kildemateriale fra Bård/irgesundinger_..._WBS_struktur-simulated.xlsx</i> "
        "— simulert WBS som var utgangspunktet for Baseline 0.",
    ], story)


# ============================================================
# BYGG
# ============================================================
def bygg():
    forside()
    forord()
    innholdsfortegnelse()
    kap_sammendrag()
    kap_om_prosjektet()
    kap_maloppnaelse()
    kap_gjennomforing()
    kap_evm()
    kap_risiko()
    kap_laeringspunkter()
    kap_anbefalinger()
    vedlegg_a()
    vedlegg_b()
    vedlegg_c()
    vedlegg_d()
    vedlegg_e()
    vedlegg_f()


bygg()

print("Bygger PDF...")
doc.build(story, canvasmaker=canvas_maker)
print(f"PDF lagret: {OUT}")
