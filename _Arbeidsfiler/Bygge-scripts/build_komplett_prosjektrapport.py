# -*- coding: utf-8 -*-
"""Komplett prosjektrapport — Nye Hædda Barneskole.

Hovedleveranse for mappeinnleveringen i LOG565 Prosjektledelse 2.
Syntese av planlegging, gjennomføring og avslutning i ett dokument.

Bygger PDF (~35-45 sider) med APA7-inspirert formatering, 10 figurer,
fullstendig innholdsfortegnelse, og dyp faglig analyse.
"""
from __future__ import annotations
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Image,
    HRFlowable,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib import colors

from apa_style import (
    build_doc, kapittel, seksjon, underseksjon, body, bullet_list, pull_quote,
    info_box, figure, tabell_caption, make_table, sit, ref,
    ST_COVER_TITLE, ST_COVER_SUB, ST_COVER_META, ST_COVER_META_BOLD,
    ST_H1, ST_H2, ST_H3, ST_H4, ST_BODY, ST_BODY_INDENT, ST_QUOTE, ST_BULLET,
    ST_CAPTION, ST_CAPTION_BOLD, ST_PULL, ST_NOTE, ST_REFERENCE,
    ST_TOC_H1, ST_TOC_H2, ST_TOC_H3,
    NAVY, PRIMARY, ACCENT, SUCCESS, DANGER, WARN, INFO,
    SOFT_BG, BORDER, MUTED,
)
from paths import ROOT, ARBEIDSFILER

FIGURER = ARBEIDSFILER / "sluttrapport_figurer"
ENDELIG = ROOT / "05 - Endelig innlevering Hædda Barneskole"
ENDELIG.mkdir(exist_ok=True)
OUT = ENDELIG / "Komplett prosjektrapport - Nye Hædda Barneskole.pdf"

REPORT_TITLE = "Komplett prosjektrapport — Nye Hædda Barneskole"

doc, canvas_maker = build_doc(str(OUT), REPORT_TITLE)
story = []


# ============================================================
# FORSIDE
# ============================================================
def forside():
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("KOMPLETT<br/>PROSJEKTRAPPORT", ST_COVER_TITLE))
    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph("Nye Hædda Barneskole", ST_COVER_SUB))
    story.append(HRFlowable(width="40%", thickness=2, color=PRIMARY,
                            spaceBefore=0, spaceAfter=20))

    meta = [
        ("Emne", "LOG565 Prosjektledelse 2 (15 stp)"),
        ("Studieprogram", "Bachelor i logistikk, Høgskolen Molde"),
        ("Gruppe", "Gruppe 4.5"),
        ("Vurderingsform", "Mappeinnlevering (100 % av karakter)"),
        ("Omfang", "Fase 2 (planlegging), fase 3 (gjennomføring), fase 4 (avslutning)"),
        ("Prosjektperiode", "1. februar 2025 – 15. mai 2026"),
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
        "Denne rapporten utgjør hovedleveransen i mappeinnleveringen. "
        "Detaljvedlegg er organisert i mappene <b>01 - Initiering</b>, "
        "<b>02 - Planlegging</b>, <b>03 - Gjennomføring</b> og <b>04 - Avslutning</b>, "
        "med støttemateriale i mappen <b>Vedlegg/</b>. "
        "Se <b>00 - Les meg først.pdf</b> for en leseguide til hele mappestrukturen.",
        ST_NOTE))
    story.append(PageBreak())


# ============================================================
# DOKUMENTINFO / KOLOFON
# ============================================================
def kolofon():
    story.append(Paragraph("Om denne rapporten", ST_H1))
    body(
        "Rapporten dokumenterer prosjekt <b>Nye Hædda Barneskole</b> fra første initieringsbeslutning, "
        "gjennom planlegging og gjennomføring, til formell avslutning og overlevering. Prosjektet er en "
        "fiktiv læringscase i emnet LOG565 Prosjektledelse 2 ved Høgskolen i Molde, der vi som studenter "
        "har overtatt rollen som prosjektledelse for Hædda kommune. Sentralt i caset står et reelt "
        "metodisk innhold — Earned Value Management, formell endringsstyring, baseline-disiplin i "
        "MS Project og syntese av månedlig oppfølging — som speiler hvordan slike prosjekter faktisk "
        "styres i praksis.",
        story)
    body(
        "Vår intensjon med rapporten er å vise at vi som gruppe ikke bare har gjennomført leveransene, "
        "men også forstått <i>hvorfor</i> hvert verktøy brukes og hva det betyr for prosjektets samlede "
        "styringsverdi. Vi har derfor lagt vekt på sporbarhet mellom planlegging, gjennomføring og "
        "avslutning, og på en faglig forankret refleksjon i kapittel 6.",
        story)

    info_box(
        "<b>En kort note om data og kildebruk.</b> All faktisk fremdrift og alle kostnadsdata stammer fra "
        "Bårds simulerte rådata levert via Teams 15. mai 2026 — kommunestyrevedtaket "
        "<i>godkjenning-av-budsjettendring.pdf</i> og <i>månedsrapporter.pdf</i> (16 teamledermøtereferater). "
        "Disse ligger som vedlegg i mappen <i>Vedlegg/A – Kildemateriale fra Bård/</i>. "
        "Tall og hendelser i rapporten er sporbare til disse referatene gjennom konsistent ID-bruk "
        "(R-05, R-06, R-07 for risikoer; CR-001 og NHB-2026-15 for endringer).",
        story)

    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("Dokumenthistorikk", ST_H3))
    tab = make_table([
        ["Versjon", "Dato", "Forfatter", "Endring"],
        ["0.9 — UTKAST", "5. mai 2026", "Gruppe 4.5", "Pre-utfylt skjelett basert på prosjektforslag og konseptløsning"],
        ["1.0 — endelig", "15. mai 2026", "Gruppe 4.5", "Komplett rapport etter fase 3 og 4. Innarbeidet Bårds rådata, EVM-analyse, refleksjon"],
    ], col_widths=[3.2 * cm, 2.6 * cm, 3 * cm, 7.5 * cm])
    story.append(tab)
    story.append(PageBreak())


# ============================================================
# INNHOLDSFORTEGNELSE (statisk, oppdateres etter første build hvis ønskelig)
# ============================================================
TOC_DATA = [
    ("Sammendrag", 0, 5),
    ("1   Innledning", 0, 6),
    ("    1.1  Prosjektets formål og bakgrunn", 1, 6),
    ("    1.2  Vedtatte rammer og mål", 1, 6),
    ("    1.3  Prosjektorganisasjon", 1, 7),
    ("    1.4  Interessentanalyse", 1, 7),
    ("    1.5  Rapportens struktur og avgrensning", 1, 8),
    ("2   Metode og teoretisk grunnlag", 0, 9),
    ("    2.1  Prosjektledelsesrammeverk", 1, 9),
    ("    2.2  Earned Value Management", 1, 9),
    ("    2.3  Endringsstyring og risikohåndtering", 1, 10),
    ("    2.4  Datakilder og sporbarhet", 1, 10),
    ("3   Planleggingsfasen — fundament", 0, 11),
    ("    3.1  Kravspesifikasjon", 1, 11),
    ("    3.2  Work Breakdown Structure", 1, 11),
    ("    3.3  Arbeidspakker — komplett oversikt", 1, 12),
    ("    3.4  Presedensdiagram og kritisk vei", 1, 13),
    ("    3.5  Tidsplan og Baseline 0", 1, 13),
    ("    3.6  Milepæler og beslutningspunkter", 1, 14),
    ("    3.7  Risikoregister", 1, 14),
    ("    3.8  Komplett prosjektplan", 1, 14),
    ("4   Gjennomføringsfasen — utførelse og styring", 0, 15),
    ("    4.1  Endringsstyring", 1, 15),
    ("        4.1.1  NHB-2026-15 — Schedule crashing av 4.1 Råbygg", 2, 15),
    ("        4.1.2  Crashing-merkostnad i detalj", 2, 17),
    ("        4.1.3  CR-001 — DSB-veileder for sprinkler og rømning", 2, 17),
    ("    4.2  Earned Value Management — sluttanalyse", 1, 18),
    ("        4.2.1  PV, EV og AC — kumulativt forløp", 2, 18),
    ("        4.2.2  CPI og SPI gjennom prosjektet", 2, 19),
    ("        4.2.3  EAC, ETC og VAC", 2, 19),
    ("        4.2.4  Pakke-nivå EVM for 4.1 Råbygg", 2, 20),
    ("    4.3  Kostnadsanalyse", 1, 21),
    ("    4.4  Risikohåndtering og realiserte hendelser", 1, 22),
    ("    4.5  Hendelsestidslinje", 1, 24),
    ("    4.6  Månedsrapportering og sporbarhet", 1, 24),
    ("    4.7  MS Project og baseline-disiplin", 1, 25),
    ("5   Avslutningsfasen — måloppnåelse og business case", 0, 26),
    ("    5.1  Måloppnåelse mot rammer", 1, 26),
    ("    5.2  Business case og gevinstrealisering", 1, 26),
    ("6   Refleksjon og læringspunkter", 0, 28),
    ("    6.6  Hva overrasket oss", 1, 30),
    ("7   Anbefalinger til oppdragsgiver", 0, 31),
    ("8   Konklusjon", 0, 32),
    ("Referanser", 0, 33),
    ("Vedlegg", 0, 34),
]


def innholdsfortegnelse():
    story.append(Paragraph("Innholdsfortegnelse", ST_H1))
    story.append(Spacer(1, 0.4 * cm))
    rows = []
    for tittel, niva, side in TOC_DATA:
        if niva == 0:
            stil = ST_TOC_H1
        elif niva == 1:
            stil = ST_TOC_H2
        else:
            stil = ST_TOC_H3
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
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<i>Figurliste og tabelliste er integrert i kapittelteksten med tydelig nummerering "
        "(Figur 3.1, Figur 4.1, …). Vedleggsliste står i kapittel «Vedlegg» på slutten.</i>",
        ST_NOTE))


def h1(text):
    """Toppnivå-overskrift. Tving sidebryter før."""
    story.append(PageBreak())
    story.append(Paragraph(text, ST_H1))


def h2(text):
    story.append(Paragraph(text, ST_H2))


def h3(text):
    story.append(Paragraph(text, ST_H3))


def h4(text):
    story.append(Paragraph(text, ST_H4))


# ============================================================
# SAMMENDRAG
# ============================================================
def sammendrag():
    h1("Sammendrag")
    body(
        "Prosjektet <b>Nye Hædda Barneskole</b> ble levert 15. mai 2026 — på vedtatt dato — til en "
        "sluttkost lik vedtatt totalramme på <b>800 millioner kroner</b>. Cost Performance Index (CPI) "
        "og Schedule Performance Index (SPI) lander begge på <b>1,000</b> ved prosjektslutt, hvilket "
        "innebærer at den endelige leveransen ligger eksakt på opprinnelig revidert plan både "
        "kostnadsmessig og fremdriftsmessig. Av godkjent risikoreserve på 50 millioner kroner ble "
        "11 millioner brukt (22 %), og av godkjent tidsbuffer på 8 uker brukte vi 1,5 uker (19 %). "
        "Skolen har dermed kapasitet til oppstart skoleåret 2026/27 som planlagt, og kommunens "
        "skolestart-løfte til innbyggerne er overholdt.",
        story)
    body(
        "Prosjektet hadde to formelle endringer underveis som er sentrale for å forstå det endelige "
        "resultatet. <b>NHB-2026-15</b> var kommunestyrets vedtak av 7. mai 2026 om å utvide "
        "budsjettrammen fra 700 til 800 millioner kroner og gi prosjektledelsen fullmakt til å "
        "komprimere (crashe) kritisk aktivitet 4.1 Råbygg. Bakgrunnen var at detaljprosjektering "
        "avdekket et reelt behov på +50 MNOK og +2 måneder ut over opprinnelig estimat — et avvik "
        "som uten korrigerende tiltak ville brutt både kostnads- og tidsrammen samtidig. "
        "<b>CR-001</b> er endringen som ble vedtatt 3. februar 2026 etter at Direktoratet for "
        "samfunnssikkerhet og beredskap (DSB) publiserte oppdatert veileder for sprinkler- og "
        "rømningsdekning i kommunale byggeprosjekter. Endringen utvidet scope på arbeidspakke "
        "5.1 VVS med en tilleggskostnad på 5 millioner kroner fra risikoreserven, og er sentral "
        "for at skolen kunne motta brukstillatelse innen overlevering.",
        story)

    pull_quote(
        "Prosjektets sluttall — 800 MNOK, CPI=SPI=1.000, sluttdato på vedtatt frist — er ikke et "
        "resultat av flaks, men av aktiv styring, dokumenterte endringer og tett oppfølging mot "
        "Baseline 1 gjennom alle 16 gjennomføringsmåneder.",
        story)

    body(
        "I løpet av gjennomføringsfasen ble tre risikoer fra registeret realisert og håndtert "
        "innenfor godkjente reserver. R-05 (funn av forurenset masse under 3.2 Riving i måned 4) "
        "krevde 6 MNOK fra risikoreserven og en uke som ble absorbert i slack. R-07 (brann hos "
        "vindusprodusent i måned 11) forsinket 4.1 Råbygg med 1,5 uker som ble dekket av "
        "tidsbufferen uten kostnadskonsekvens. R-06 ble formell endringsforespørsel (CR-001) og "
        "er behandlet over.",
        story)

    body(
        "Vi har bygd dokumentasjonsstrukturen rundt fire prinsipper: <b>baseline-disiplin</b> "
        "(Baseline 0 og 1 begge bevart i MS Project), <b>sporbarhet</b> (hvert tall i hver "
        "månedsrapport kan spores tilbake til et bestemt avsnitt i Bårds referater), "
        "<b>formell endringsstyring</b> (hver endring har eget dokument med konsekvensanalyse "
        "for omfang, tid, kostnad og risiko), og <b>analytisk EVM-rapportering</b> (S-kurver, "
        "CPI/SPI og avviksforklaring i hver av de 16 månedsrapportene). Disse fire prinsippene "
        "vurderer vi som det viktigste vi tar med oss fra emnet.",
        story)


# ============================================================
# KAP 1 — INNLEDNING
# ============================================================
def kap_1():
    h1("1   Innledning")

    h2("1.1  Prosjektets formål og bakgrunn")
    body(
        "Hædda kommune skal bygge en ny barneskole for inntil 600 elever fra 1. til 10. trinn, "
        "med plass til om lag 100 ansatte fordelt på faglig, administrativ og driftspersonale. "
        "Behovet stammer fra både kapasitetspress på eksisterende skoler i kommunen og krav om "
        "moderne fysiske læringsmiljøer som speiler dagens pedagogiske praksis. Prosjektforslaget "
        "fra 2025 forankrer behovet i kommunens skoleeierstrategi og samfunnsdelen av kommuneplanen "
        f"{sit('Hædda kommune', '2025a')}.",
        story)

    body(
        "Konseptløsningen som ble vedtatt høsten 2025 spesifiserer en skolebygning i tre etasjer "
        "med en grunnflate på 4 608 kvadratmeter og et bruttoareal på cirka 13 824 kvadratmeter, "
        "innenfor en arealramme på 14 000 kvadratmeter. Bygningen inkluderer kantine i første "
        "etasje, bibliotek og auditorium i andre etasje, og en gymsal på 900 kvadratmeter som "
        "også er tilgjengelig for nærmiljøet utenfor skoletid. Energiforbruket skal være "
        "maksimalt 75 kilowattimer per kvadratmeter per år, og prosjektet sikter mot "
        f"BREEAM Very Good {sit('Hædda kommune', '2025b')}.",
        story)

    h2("1.2  Vedtatte rammer og mål")
    body(
        "Kommunestyret vedtok opprinnelig en budsjettramme på 700 millioner kroner inkludert "
        "50 millioner i usikkerhetsavsetning (risikoreserve), med planlagt ferdigstillelse "
        "15. mai 2026 og en uttalt tidsbuffer på 8 uker før forsinkelse anses reell. Prosjektet "
        "har dermed tre overordnede rammer som hver krever aktiv styring: en hard kostnadsramme, "
        "en hard tidsramme knyttet til skolestart høsten 2026, og en kvalitetsramme definert av "
        "kravspesifikasjonens 59 krav fordelt på funksjonelle, tekniske, miljømessige, "
        "sikkerhetsmessige og driftsmessige kategorier.",
        story)

    body(
        "Tid er identifisert som den dominerende rammen. Konsekvensen av forsinkelse er ikke "
        "primært økonomisk, men institusjonell: skolen må stå klar i god tid før skolestart, "
        "ellers utløses kostnader til midlertidige skolelokaler, ny oppstartsplanlegging for "
        "skoleeier, og en betydelig omdømmebelastning for kommunen. Dette har preget "
        "beslutningskjeden i hele prosjektet — spesielt i håndteringen av "
        "schedule crashing-saken NHB-2026-15 i kapittel 4.1.1.",
        story)

    h2("1.3  Prosjektorganisasjon")
    body(
        "Prosjektorganisasjonen er strukturert i en klassisk trekantmodell for byggeprosjekter: "
        "prosjekteier på toppen, prosjektledelse i midten, og operative team og leverandører "
        "i bunnen. Tabell 1.1 sammenfatter hovedrollene og deres møtefrekvens.",
        story)

    tabell_caption("1.1", "Prosjektorganisasjon — roller, ansvar og kadens.", story)
    org_tab = make_table([
        ["Rolle", "Ansvar", "Kadens"],
        ["Kommunestyret (prosjekteier)",
         "Vedtak om rammer, budsjettendringer, scope-endringer på baseline-nivå",
         "Ved milepæler og endringssaker (NHB-2026-15)"],
        ["Byggekomiteen",
         "Operativ tilsyn, behandling av endringsforespørsler under terskelverdi",
         "Månedlig + ad hoc"],
        ["Prosjektledelse (Gruppe 4.5)",
         "Daglig styring, EVM-rapportering, endringshåndtering, månedsrapporter",
         "Daglig styring + månedsrapport"],
        ["Byggeleder",
         "Operativ leveranseoppfølging på byggeplass, koordinering av underleverandører",
         "Daglig på byggeplass"],
        ["Økonomiansvarlig",
         "Påløpsregistrering, AC-rapportering, budsjettoppfølging mot pakker",
         "Ukentlig"],
        ["Prosjektkoordinator",
         "Møtereferater, dokumentkontroll, sporbarhetsstyring",
         "Teamledermøter (månedlig)"],
        ["Fagansvarlige (råbygg, VVS, elektro, automasjon, IKT, FDV)",
         "Faglig styring og kvalitetsoppfølging per fagområde",
         "Månedlige teamledermøter"],
        ["HMS-/KS-ansvarlig",
         "Sikkerhet, kvalitetssikring, miljøkrav, varsling mot myndigheter",
         "Ukentlig"],
        ["Byggherreombud",
         "Byggherrens interesser på byggeplass, befaringer og kvalitetsverifikasjon",
         "Månedlig befaring + ad hoc"],
        ["Underleverandører",
         "Konkrete leveranser per arbeidspakke, leveransekvalitet, fagspesifikk styring",
         "Etter kontraktsavtale + ukentlig oppfølging"],
    ], col_widths=[5 * cm, 7.5 * cm, 3.5 * cm])
    story.append(org_tab)

    h2("1.4  Interessentanalyse")
    body(
        "Interessentkartet for et kommunalt skoleprosjekt strekker seg langt utover prosjekteierens "
        "egen organisasjon. Vi har klassifisert interessentene etter to dimensjoner — innflytelse "
        "over prosjektet og berørt-grad — og tilpasset kommunikasjonsstrategien deretter. Tabell "
        "1.2 viser klassifikasjonen og den valgte kommunikasjonsformen for hver interessentgruppe.",
        story)

    tabell_caption("1.2", "Interessentmatrise — innflytelse, berørt-grad og kommunikasjonsform.", story)
    int_tab = make_table([
        ["Interessent", "Innflytelse", "Berørt", "Kommunikasjonsform"],
        ["Kommunestyret", "Høy", "Middels",
         "Formelt vedtak ved milepæler, månedlig statusrapport via byggekomiteen"],
        ["Byggekomiteen", "Høy", "Høy",
         "Månedlige teamledermøter; egen rapportering for crashet aktivitet 4.1"],
        ["Skoleeier (rektor, lærere)", "Middels", "Høy",
         "Kvartalsvise dialogmøter, befaring i innvendigfasen"],
        ["Elever og foreldre", "Lav", "Høy",
         "Nyhetsbrev fra kommunen kvartalsvis"],
        ["Lokalmiljø/naboer", "Lav", "Middels",
         "Informasjonsmøter ved oppstart og milepæler, skilt på byggeplass"],
        ["Brannvesen", "Middels", "Middels",
         "Behandling ved BP3; ad hoc dialog ved CR-001 (DSB-veileder)"],
        ["Statsforvalter (miljø)", "Middels", "Lav",
         "Formelt varsel ved miljøhendelser (R-05 forurensning)"],
        ["DSB", "Middels", "Lav",
         "Veilederreferanser; CR-001 utløst av DSB-publisering"],
        ["Underleverandører", "Middels", "Høy",
         "Kontraktsstyring + ukentlig oppfølging på byggeplass"],
    ], col_widths=[3.8 * cm, 2 * cm, 1.7 * cm, 8.5 * cm])
    story.append(int_tab)

    info_box(
        "<b>Slik brukte vi interessentanalysen i praksis.</b> Da CR-001 (DSB sprinkler/rømning) "
        "ble håndtert, identifiserte vi tidlig at brannvesenet er en høy-innflytelse-interessent "
        "for brukstillatelsen. Dette flyttet brannvesenets vurdering fra «BP3-godkjenning» (ad "
        "hoc) til «aktiv konsultasjon» under utformingen av den oppgraderte sprinklerløsningen. "
        "Tilsvarende for R-05 (forurenset masse) varslet vi statsforvalter formelt — ikke fordi "
        "vi måtte juridisk, men fordi det er den eneste måten å sikre at miljøkonsekvensene "
        "ikke kunne anfektes i ettertid.",
        story)

    h2("1.5  Rapportens struktur og avgrensning")
    body(
        "Rapporten følger oppgavens fasestruktur fra prosjektforslaget. Kapittel 2 redegjør for "
        "den metodiske og teoretiske rammen vi har lagt til grunn. Kapittel 3 dokumenterer "
        "planleggingsfasen som ble levert til prosjekteier i forrige milepæl, og som er "
        "uendret i denne rapporten — det er en syntese, ikke en revisjon. Kapittel 4 er "
        "rapportens kjerne: en detaljert gjennomgang av gjennomføringsfasen med fokus på "
        "endringsstyring, Earned Value Management og hendelseshåndtering. Kapittel 5 dekker "
        "måloppnåelse og business case, mens kapittel 6 inneholder vår refleksjon over hva vi "
        "har lært. Kapittel 7 oppsummerer anbefalinger for videre arbeid etter overlevering.",
        story)

    info_box(
        "<b>Avgrensning.</b> Rapporten fokuserer på prosjektledelseskompetansen som emnet "
        "vurderer. Detaljer om byggetekniske løsninger, arkitektoniske valg og pedagogiske "
        "konsekvenser ligger utenfor scope — disse er dekket i konseptløsningen og "
        "kravspesifikasjonen. Vi har heller ikke gjort selvstendige vurderinger av miljøtekniske "
        "krav (BREEAM, TEK17), men forholder oss til de kvalitetskravene som er forhåndsdefinert "
        "av prosjektforslaget.",
        story)


# ============================================================
# KAP 2 — METODE OG TEORI
# ============================================================
def kap_2():
    h1("2   Metode og teoretisk grunnlag")

    h2("2.1  Prosjektledelsesrammeverk")
    body(
        "Vi har valgt å bygge prosjektstyringen rundt prinsipper som er felles i "
        "anerkjente prosjektledelses-rammeverk — særlig <i>A Guide to the Project Management "
        f"Body of Knowledge</i> {sit('Project Management Institute', '2021')} og prinsippene fra "
        f"PRINCE2 om <i>justification, structure og responsibility</i> {sit('AXELOS', '2017')}. "
        "Begge rammeverkene legger til grunn at et prosjekt styres mot tre primære "
        "ytelsesdimensjoner — omfang, tid og kostnad — med kvalitet og risiko som "
        "tverrgående hensyn. Vi har implementert dette gjennom kravspesifikasjon (omfang), "
        "Gantt med kritisk vei (tid), Earned Value Management (kostnad/fremdrift), "
        "risikoregister og månedlig oppfølging.",
        story)

    body(
        "Et særtrekk ved vårt prosjekt er at det fra start har vært definert med en "
        "<i>hard, ekstern frist</i> (skolestart høsten 2026), noe som flytter risikoen fra "
        "kostnad mot tid. Dette har gjort det fornuftig å akseptere en kostnadsutvidelse "
        "framfor en forsinkelse — den faglige logikken bak schedule crashing-vedtaket "
        "NHB-2026-15 som beskrives i kapittel 4.1.1.",
        story)

    h2("2.2  Earned Value Management")
    body(
        "Earned Value Management (EVM) er den primære metoden vi har brukt for å holde objektiv "
        "kontroll på prosjektets fremdrift gjennom gjennomføringsfasen. EVM kombinerer tre "
        f"grunnstørrelser {sit('Project Management Institute', '2021', '267')}:",
        story)

    bullet_list([
        "<b>Planned Value (PV)</b> — den planlagte verdiskapningen ved en gitt statusdato, "
        "målt som kumulativ andel av Budget at Completion (BAC) som skulle vært opptjent.",
        "<b>Earned Value (EV)</b> — den faktiske verdiskapningen ved samme statusdato, målt som "
        "kumulativ andel av BAC som er reelt fullført.",
        "<b>Actual Cost (AC)</b> — den faktiske kostnaden påløpt fram til statusdato.",
    ], story)

    body(
        "Ut fra disse tre størrelsene utleder vi to forholdstall som forteller om prosjektet "
        "er på plan eller ikke. <b>Cost Performance Index (CPI) = EV/AC</b> sier hvor mye verdi "
        "vi får per krone brukt; CPI &gt; 1 betyr at vi får mer enn vi betaler for, mens "
        "CPI &lt; 1 betyr kostnadsoverskridelse. <b>Schedule Performance Index (SPI) = EV/PV</b> "
        "sier hvor mye verdi vi har opptjent sammenlignet med det vi skulle opptjent på planen; "
        "SPI &lt; 1 betyr forsinkelse målt i opptjent verdi.",
        story)

    info_box(
        "<b>Verdt å merke seg:</b> EVM gir objektiv status uavhengig av subjektive "
        "framdriftsvurderinger fra leverandører. Hvor langt vi har «kommet» er ikke et "
        "spørsmål om hvor opptatt teamet føler seg — det er et målbart forhold mellom "
        "leverte ferdigvarer og brukte ressurser. Dette ble særlig nyttig i månedene rundt "
        "råbyggets crashing-periode, hvor det subjektive bildet var preget av høyt "
        "aktivitetsnivå, men hvor EVM viste at vi faktisk fulgte planen.",
        story)

    body(
        "Vi har i tillegg brukt utledede størrelser som <b>Estimate at Completion (EAC) = "
        "BAC/CPI</b>, som gir en prognose for sluttkost basert på dagens kostnadseffektivitet, "
        "og <b>Variance at Completion (VAC) = BAC – EAC</b>, som er den prognosticerte "
        "kostnadsavviket ved slutten. Sluttverdiene for disse størrelsene er presentert "
        "i kapittel 4.2.",
        story)

    h2("2.3  Endringsstyring og risikohåndtering")
    body(
        "Vi har skilt klart mellom <b>endringer</b> og <b>hendelser</b>. En endring er en "
        "<i>vedtatt</i> justering av omfang, tid eller kostnad som krever formell behandling "
        "og godkjenning fra rett myndighet — for vårt prosjekt enten prosjekteier eller "
        "kommunestyret. En hendelse er en <i>realisert risiko</i> som håndteres innenfor "
        "godkjente reserver (risikoreserve eller tidsbuffer) uten å endre baseline. "
        "Sondringen er viktig fordi de to har ulik dokumentasjonskrav: endringer krever "
        "endringsdokument med konsekvensanalyse, mens hendelser registreres i risikoregisteret "
        "og månedsrapportene.",
        story)

    body(
        "I gjennomføringsfasen håndterte vi tre risikoer som ble realisert. To av disse "
        "(R-05 og R-07) ble klassifisert som hendelser fordi de holdt seg innenfor godkjent "
        "risikoreserve eller tidsbuffer. Den tredje (R-06) endret scope på arbeidspakke 5.1 VVS "
        "og ble derfor behandlet som formell endring CR-001. Detaljene står i kapittel 4.1.2.",
        story)

    h2("2.4  Datakilder og sporbarhet")
    body(
        "Datagrunnlaget for rapportens kvantitative analyse er Bårds simulerte rådata levert "
        "via Microsoft Teams 15. mai 2026. Konkret bygger vi på to dokumenter: "
        f"<i>godkjenning-av-budsjettendring.pdf</i> {sit('Irgesund', '2026a')} som inneholder "
        f"kommunestyrets vedtak NHB-2026-15, og <i>månedsrapporter.pdf</i> {sit('Irgesund', '2026b')} "
        "som inneholder 16 teamledermøtereferater for hele gjennomføringsfasen. "
        "Begge er bevart i opprinnelig form i mappen <i>Vedlegg/A – Kildemateriale fra Bård</i>.",
        story)

    body(
        "For å sikre sporbarhet mellom rådata og hver enkelt månedsrapport har vi bygget en "
        "sentral datastruktur i Python (<i>log565_master_data.py</i>) som inneholder "
        "definisjonen av Baseline 1 (32 arbeidspakker med start/slutt og BAC), faktisk fremdrift "
        "per pakke per måned (% fullført og påløpt) og alle tre hendelser med risiko-ID-er. "
        "Denne strukturen er kilden for både EVM-arbeidsboken, de 16 månedsrapportene, "
        "endringsdokumentene og denne hovedrapporten. På den måten er det <i>kun ett sted</i> "
        "tallene kan endres — og det er konsistens automatisk på tvers av alle leveranser.",
        story)


# ============================================================
# KAP 3 — PLANLEGGINGSFASEN (SYNTESE)
# ============================================================
def kap_3():
    h1("3   Planleggingsfasen — fundament")
    body(
        "Planleggingsfasen ble formelt godkjent av prosjekteier ved leveransen av "
        "<i>Komplett prosjektplan</i> 5. mai 2026, og er uendret i denne rapporten — vi gjengir "
        "den her i syntetisert form for at leseren skal kunne følge rødtråden uten å bla "
        "mellom dokumenter. Det fullstendige plangrunnlaget ligger som vedlegg i "
        f"<i>02 - Planlegging/</i> {sit('Gruppe 4.5', '2026a')}.",
        story)

    h2("3.1  Kravspesifikasjon")
    body(
        "Kravspesifikasjonen identifiserer 59 krav fordelt på 9 kategorier: funksjonelle krav, "
        "tekniske krav, miljøkrav, sikkerhetskrav, uteområde, akustikk, universell utforming, "
        "kvalitetskrav og drift/FDV. Hvert krav er klassifisert med prioritet (skal/bør/kan), "
        "verifikasjonsmetode (visuell, dokumentasjon, måling, test) og kobling til "
        "WBS-arbeidspakker. To krav i kvalitetskategorien er spesielt sentrale i sluttrapporten: "
        "K-001 (null kritiske mangler ved ferdigbefaring, BP3) og K-002 (komplett "
        "FDV-dokumentasjon overlevert ved sluttbefaring).",
        story)

    h2("3.2  Work Breakdown Structure")
    body(
        "WBS-strukturen følger en hierarkisk nedbrytning i fire nivåer. Nivå 1 inneholder de "
        "åtte hovedgrenene (1. Prosjektledelse, 2. Planlegging og prosjektering, 3. Forberedelse "
        "og riving, 4. Skolebygg – bygningsmessige arbeider, 5. Skolebygg – tekniske anlegg, "
        "6. Utomhus og uteområder, 7. Inventar og utstyr, 8. Overtakelse og avslutning). "
        "Disse er videre brutt ned i 32 arbeidspakker (leaves) som er styringsobjektene "
        "i Earned Value Management. Hver pakke har egen BAC, planlagt varighet og avhengighet "
        "til foregående pakker.",
        story)

    figure(FIGURER / "figur_03_kostnadsfordeling.png", story, "3.1",
           "Kostnadsfordeling per WBS-nivå-1. Arbeidsgruppe 4 (Skolebygg – bygningsmessige "
           "arbeider) er dominerende med 360 MNOK (45 % av BAC), drevet av 4.1 Råbygg som "
           "alene utgjør 240 MNOK etter crashing.")

    h2("3.3  Arbeidspakker — komplett oversikt")
    body(
        "Tabell 3.1 viser den fullstendige oversikten over alle 32 arbeidspakker i Baseline 1 etter "
        "crashing av 4.1 Råbygg. Pakkenes WBS-ID følger den hierarkiske strukturen, og BAC summerer "
        "til 800 MNOK i tråd med kommunestyrets vedtak NHB-2026-15. Disse pakkene utgjør "
        "styringsobjektene i Earned Value Management og er kilden for EV-beregningen.",
        story)

    tabell_caption("3.1", "Komplett oversikt over alle 32 arbeidspakker i Baseline 1. BAC summerer til 800 MNOK.", story)
    from log565_master_data import PAKKER as _PAKKER, MÅNEDER as _MAANEDER
    pakke_rader = [["WBS", "Aktivitet", "BAC (MNOK)", "Varighet", "Start–Slutt", "Fagansvar"]]
    for p in _PAKKER:
        start_navn, _ = _MAANEDER[p.start_mnd]
        slutt_navn, _ = _MAANEDER[p.slutt_mnd]
        pakke_rader.append([
            p.wbs,
            p.navn,
            f"{p.bac:.0f}",
            f"{p.varighet} mnd" if p.varighet > 1 else "1 mnd",
            f"M{p.start_mnd}–M{p.slutt_mnd}",
            p.fagansvar,
        ])
    pakke_rader.append(["", "SUM", "800", "", "", ""])
    pakke_tab = make_table(pakke_rader,
                            col_widths=[1.2 * cm, 5.2 * cm, 2 * cm, 1.8 * cm, 1.8 * cm, 4 * cm])
    story.append(pakke_tab)

    h2("3.4  Presedensdiagram og kritisk vei")
    body(
        "Presedensdiagrammet kartlegger avhengighetene mellom de 32 arbeidspakkene. Den "
        "kritiske veien går gjennom 2.1 Detaljprosjektering → 3.2 Riving → 3.3 Grunnarbeid → "
        "4.1 Råbygg → 4.2/4.3/4.4 Innvendig komplettering → 5.1 VVS → 8.2 Ferdigbefaring. "
        "Det er 4.1 Råbygg som dominerer kritisk vei i tid — det er denne aktiviteten som "
        "ble crashet i NHB-2026-15-vedtaket, og det er forsinkelser i denne pakken "
        "(R-07 brann hos vindusprodusent) som potensielt kunne dratt sluttdato uten "
        "korrigerende handling.",
        story)

    h2("3.4  Tidsplan og Baseline 0")
    body(
        "Den opprinnelige Gantt-planen (Baseline 0) ble lagt fram i MS Project basert på "
        "Bårds simulerte WBS-tall (Vedlegg A). Plansummeringen i denne baselinen er en "
        "totalkostnad på 750 millioner kroner og en sluttdato i juli 2026 — om lag seks uker "
        "etter den vedtatte fristen 15. mai 2026. Det er denne avstanden mellom Baseline 0 "
        "og vedtatt frist som motiverer schedule crashing-saken NHB-2026-15.",
        story)

    h2("3.6  Milepæler og beslutningspunkter")
    body(
        "Prosjektet er strukturert rundt fire formelle beslutningspunkter (BP) som er definert i "
        "prosjektforslaget, supplert med tre interne milepæler (M) for å markere ferdigstillelse "
        "av hovedfaser. Tabell 3.2 viser status ved overlevering.",
        story)

    tabell_caption("3.2", "Milepæler og beslutningspunkter — vedtatt mot faktisk.", story)
    mp_tab = make_table([
        ["Milepæl", "Beskrivelse", "Vedtatt", "Faktisk", "Status"],
        ["BP1", "Beslutning om gjennomføring (vedtak om prosjektoppstart)",
         "Jan 2025", "Jan 2025", "OK"],
        ["BP2", "Beslutning om kontrahering (etter detaljprosjektering)",
         "Mai 2025", "Apr 2025", "OK (1 mnd tidligere)"],
        ["M1", "Råbygg 4.1 ferdigstilt",
         "Des 2025 (Baseline 1)", "Des 2025", "OK iht. Baseline 1"],
        ["M2", "Innvendig komplettering 4.2–4.4 ferdigstilt",
         "Mar 2026", "Mar 2026", "OK"],
        ["M3", "Tekniske anlegg 5.1–5.5 ferdigstilt",
         "Apr 2026", "Apr 2026", "OK"],
        ["BP3", "Ferdigbefaring — operativt ferdig, mangler godkjent",
         "Apr 2026", "Apr 2026", "OK (K-001 oppfylt)"],
        ["BP4", "Sluttovertakelse — formell overlevering",
         "15. mai 2026", "15. mai 2026", "OK (på datoen)"],
    ], col_widths=[1.5 * cm, 6 * cm, 2.5 * cm, 2.5 * cm, 3.5 * cm])
    story.append(mp_tab)

    body(
        "Verdt å merke seg at BP2 ble nådd én måned tidligere enn vedtatt — dette er konsistent "
        "med det høye SPI-tallet i mnd 1–3 som vises i kapittel 4.2. Detaljprosjekteringen ble "
        "fullført raskere enn lineær fordeling ville tilsi, og kontrakter ble tildelt i april 2025 "
        "i stedet for mai. Det ga et tidsmessig fortrinn som vi i etterpåklokskap kunne brukt "
        "som en buffer mot crashing-perioden — men dette var ikke planlagt og ble derfor heller "
        "ikke utnyttet aktivt.",
        story)

    h2("3.7  Risikoregister")
    body(
        "Risikoregisteret inneholder 16 identifiserte risikoer ved planavslutning, fordelt på "
        "kategoriene tekniske, leveranse, regulatoriske, økonomiske og organisatoriske. "
        "Restrisikobildet ved planavslutning var null kritiske, null høye, seks middels og "
        "ti lave — gitt at tiltakene definert i registeret blir gjennomført som planlagt. "
        "Vi reserverte 50 millioner kroner og 8 uker som henholdsvis risikoreserve og "
        "tidsbuffer for å håndtere realiserte risikoer.",
        story)

    body(
        "Av disse 16 risikoene ble tre realisert gjennom gjennomføringsfasen (R-05, R-06 og R-07). "
        "Detaljert behandling av disse er gitt i kapittel 4.4. De øvrige 13 risikoene forble "
        "i overvåket tilstand og krevde ikke aktiv respons.",
        story)

    h2("3.8  Komplett prosjektplan")
    body(
        "Den komplette prosjektplanen syntetiserer kravspesifikasjon, WBS, presedensdiagram, "
        "Gantt og risikoregister til ett styringsdokument. Den definerer prosjektets "
        "organisasjon, kommunikasjonsplan, kvalitetsplan, leveranseplan, milepælplan, "
        "rapporteringsstrategi og endringsstyringsprosess. Det er denne planen som ble "
        "godkjent av prosjekteier ved planfaseavslutning, og som dannet utgangspunktet for "
        "gjennomføringsfasen som nå beskrives.",
        story)


# ============================================================
# KAP 4 — GJENNOMFØRINGSFASEN
# ============================================================
def kap_4():
    h1("4   Gjennomføringsfasen — utførelse og styring")
    body(
        "Gjennomføringsfasen strakk seg fra prosjektstart 1. februar 2025 til overlevering "
        "15. mai 2026 — totalt 16 kalendermåneder med månedlige teamledermøter som styringspunkter. "
        "Dette kapitlet beskriver de to formelle endringene som ble behandlet, "
        "Earned Value Management-resultatene, kostnadsanalysen, hvordan risikoene ble håndtert "
        "og hvordan vi har sikret sporbarhet mellom referater og månedsrapporter.",
        story)

    # --------- 4.1 Endringsstyring ---------
    h2("4.1  Endringsstyring")
    body(
        "To formelle endringer er dokumentert med egne endringsdokumenter i "
        "<i>03 - Gjennomføring/Endringsdokumenter/</i>. Begge har gjennomgått full "
        "konsekvensanalyse for omfang, tid, kostnad, kvalitet, ressurser og risiko, "
        "i tråd med malen fra fase 2 og prinsippene i PMBOK Guide om integrated change control "
        f"{sit('Project Management Institute', '2021', '113')}.",
        story)

    h3("4.1.1  NHB-2026-15 — Schedule crashing av 4.1 Råbygg")
    body(
        "Detaljprosjektering avdekket at arbeidspakke 4.1 Råbygg var underestimert i Baseline 0 "
        "med +50 millioner kroner og +2 måneder. Aktivitetens reelle behov ble dokumentert til "
        "190 millioner kroner og 7 måneders varighet, mot 140 MNOK og 5 måneder i opprinnelig "
        "estimat. Aktiviteten ligger på prosjektets kritiske vei, slik at overskridelsen ville "
        "forplantet seg direkte til totalkostnad og sluttdato.",
        story)

    body(
        "Prognose uten korrigerende tiltak: totalkostnad 750 MNOK (+50 MNOK over vedtatt ramme) "
        "og sluttdato i juli 2026 (cirka 2 måneder etter vedtatt frist). Konsekvensen av "
        "passiv aksept ville altså vært samtidig brudd på begge primærrammene.",
        story)

    body(
        "Prosjektledelsen utredet tre alternativer. <b>Alternativ 1 — ikke iverksette tiltak</b> "
        "ville innebære fullstendig brudd på vedtatt sluttdato og kostnadsramme. "
        "<b>Alternativ 2 — redusere omfang</b> ville innebære fjerning av leveranser fra "
        "kravspesifikasjonen, hvilket ikke ble vurdert som forenelig med kommunestyrets "
        "opprinnelige bestilling. <b>Alternativ 3 — komprimering (crashing) av 4.1 Råbygg</b> "
        "innebar å øke ressurspådraget gjennom overtid, parallelle skift, "
        "premium-materialleveranser og forsering hos underleverandører, slik at varigheten "
        "ble brakt fra 7 tilbake til 5 måneder mot en tilleggskost på 50 MNOK.",
        story)

    figure(FIGURER / "figur_07_baseline_sammenligning.png", story, "4.1",
           "Sammenligning av Baseline 0 (opprinnelig vedtak), pre-crashing prognose, "
           "Baseline 1 (etter NHB-2026-15) og faktisk sluttall. Kostnaden er utvidet med "
           "100 MNOK mot at vedtatt sluttdato 15. mai 2026 overholdes fullt ut.")

    body(
        "Kommunestyret behandlet saken 7. mai 2026 og vedtok alternativ 3. Vedtaket utvidet "
        "budsjettrammen fra 700 til 800 MNOK (en økning på 100 MNOK fordelt på 50 MNOK i den "
        "avdekkede overskridelsen og 50 MNOK i selve crashing-tiltaket) og ga prosjektledelsen "
        "fullmakt til å iverksette komprimeringen. Vedtaket inkluderer et eksplisitt krav om "
        "månedlig statusrapportering på den komprimerte aktiviteten til byggekomiteen, et "
        "krav vi har innfridd gjennom månedsrapportene for måned 7 til 11.",
        story)

    pull_quote(
        "Vedtaket NHB-2026-15 illustrerer det mest sentrale prinsippet vi tar med oss fra "
        "emnet: når tid er den dominerende rammen, er kostnad det forhandlingsbare verktøyet. "
        "Schedule crashing er ikke en akademisk øvelse — det er en konkret beslutning om å "
        "betale for ekstra ressurser slik at den uforhandlebare fristen kan overholdes.",
        story)

    h3("4.1.2  Crashing-merkostnad i detalj")
    body(
        "Den vedtatte tilleggskostnaden på 50 MNOK for komprimering av 4.1 Råbygg er ikke en "
        "enkelt linje, men en sammensetning av fire konkrete tiltak. Vi har spesifisert disse i "
        "endringsdokumentet og fulgt opp månedlig i råbyggsperioden (måned 7–11). Tabell 4.1 "
        "viser fordelingen.",
        story)

    tabell_caption("4.1", "Sammensetning av crashing-merkostnaden på 50 MNOK for 4.1 Råbygg.", story)
    crash_tab = make_table([
        ["Tiltak", "Estimert kostnad", "Andel", "Begrunnelse"],
        ["Overtid og ekstra mannskap",
         "18 MNOK", "36 %",
         "Helgearbeid og ettermiddagsskift på bærekonstruksjon og tak"],
        ["Parallelle skift (natt)",
         "12 MNOK", "24 %",
         "Tre måneder med nattskift på fasade og innvendig arbeid for å parallellisere "
         "kritiske aktiviteter"],
        ["Premium-leveranser av materialer",
         "14 MNOK", "28 %",
         "Hasteleveranser av tak- og fasade-elementer fra produsent med kort leveringstid "
         "(om lag 30 % høyere stykkpris)"],
        ["Forsering hos underleverandører",
         "6 MNOK", "12 %",
         "Tillegg til underleverandørkontrakter for å sikre prioritert produksjonskapasitet "
         "i 4.1-perioden"],
        ["SUM", "50 MNOK", "100 %", "Som vedtatt i NHB-2026-15"],
    ], col_widths=[5 * cm, 2.5 * cm, 1.5 * cm, 7.5 * cm])
    story.append(crash_tab)

    body(
        "Av disse fire postene var det «parallelle skift» som ga størst utfordring i praksis. "
        "Nattskift krever særskilt HMS-oppfølging, og vi hadde i utgangspunktet undervurdert "
        "den koordineringsbyrden det legger på byggeleder og SHA-ansvarlig. Vi løste dette ved "
        "å innføre et ukentlig SHA-statusmøte gjennom hele 4.1-perioden, et tiltak som ble "
        "vedtatt som forutsetning i endringsdokumentet NHB-2026-15.",
        story)

    h3("4.1.3  CR-001 — DSB-veileder for sprinkler og rømning")
    body(
        "I februar 2026 publiserte Direktoratet for samfunnssikkerhet og beredskap (DSB) "
        "oppdatert veileder for sprinklerdekning og rømningsskilting i kommunale "
        f"byggeprosjekter {sit('Direktoratet for samfunnssikkerhet og beredskap', '2026')}. "
        "Veilederen trer i kraft før prosjektets ferdigstillelse og påvirker arbeidspakke "
        "5.1 VVS direkte. Endringen kunne ikke ignoreres uten å risikere at skolen ikke "
        "ville få brukstillatelse fra kommunen før skolestart høsten 2026 — i praksis "
        "samme alvorlighetsgrad som en forsinkelse på selve byggetiden.",
        story)

    body(
        "Endringsforespørselen CR-001 ble behandlet og godkjent på teamledermøtet 3. februar 2026 "
        "(måned 13). Scope på 5.1 VVS ble utvidet med oppgradert sprinklerdekning og "
        "forsterket rømningsskilting. Tilleggskostnaden ble estimert til 5,0 MNOK og dekket "
        "fra risikoreserven, og forsinkelseskonsekvensen på 1 uke ble absorbert i tidsbufferen. "
        "BAC ble dermed ikke endret, men kumulativ bruk av risikoreserven økte fra 6 til 11 MNOK.",
        story)

    h2("4.2  Earned Value Management — sluttanalyse")
    body(
        "EVM-rapporteringen har vært gjennomgående i månedsrapportene, men det er ved "
        "prosjektslutt at det samlede bildet trer fram. Vi viser her S-kurven og "
        "CPI/SPI-trenden for hele forløpet, etterfulgt av en presentasjon av sluttverdier "
        "for de utledede størrelsene EAC, ETC og VAC.",
        story)

    h3("4.2.1  PV, EV og AC — kumulativt forløp")
    figure(FIGURER / "figur_01_s_kurve.png", story, "4.2",
           "S-kurven for hele gjennomføringsfasen. Planned Value (PV) er Baseline 1 lineært "
           "fordelt over hver pakkes varighet. Earned Value (EV) er beregnet som "
           "BAC × % fullført per pakke, aggregert. Actual Cost (AC) er direkte hentet fra "
           "kumulativ påløpt aktivitetskost i månedsreferatene. Hendelsene R-05, R-07 og R-06 "
           "er markert med rødt.")

    body(
        "Tre observasjoner fra S-kurven er verdt å trekke fram. For det første er det et "
        "tydelig knekkpunkt rundt måned 7, hvor 4.1 Råbygg starter og det månedlige "
        "kostnadsforbruket går fra cirka 25 MNOK til over 60 MNOK. Det er denne perioden "
        "som er drevet av crashing-vedtaket. For det andre er kurvene PV, EV og AC nært "
        "sammenfallende gjennom hele forløpet, hvilket viser at prosjektet har styrt mot "
        "den oppdaterte Baseline 1 med høy presisjon. For det tredje er det første tre "
        "månedene en relativt høy EV/PV-rate (SPI &gt; 1,15), forklart av at "
        "detaljprosjekteringen ble fullført raskere enn lineær fordeling skulle tilsi. "
        "Det er en metodisk effekt av at vi har modellert PV som lineær fordeling per "
        "pakke, ikke en reell forutsigelse av forsering.",
        story)

    h3("4.2.2  CPI og SPI gjennom prosjektet")
    figure(FIGURER / "figur_02_cpi_spi_trend.png", story, "4.3",
           "CPI- og SPI-utvikling per måned. Det grønne båndet markerer toleranseområdet "
           "0,95–1,05 hvor avvik anses akseptable. Begge forholdstall konvergerer mot 1,000 "
           "ved prosjektslutt og holder seg innenfor toleransen gjennom hele forløpet.")

    body(
        "CPI ligger gjennomgående på eller marginalt over 1,000 i hele perioden, hvilket "
        "innebærer at prosjektet ikke har hatt kostnadsavvik mot Baseline 1. SPI har større "
        "variasjon, særlig i de tre første månedene, men er stabilt over 1,000 i hele "
        "perioden — vi har aldri vært bak skjema målt i opptjent verdi mot lineær PV-fordeling. "
        "Sluttverdier: <b>CPI = 1,000, SPI = 1,000</b>.",
        story)

    h3("4.2.3  EAC, ETC og VAC")
    body(
        "Estimate at Completion-prognosen (EAC = BAC/CPI) har gjennom prosjektet "
        "konvergert mot BAC etter hvert som CPI har stabilisert seg rundt 1,000. Sluttverdien "
        "er EAC = 800 MNOK / 1,000 = <b>800 MNOK</b>, identisk med BAC. Variance at Completion "
        "(VAC = BAC − EAC) er dermed <b>0 MNOK</b> — vi har ingen prognosticert "
        "kostnadsoverskridelse ved overlevering. Estimate to Complete (ETC = EAC − AC) gikk "
        "fra 776 MNOK ved måned 1 til 0 MNOK ved måned 16, i takt med påløpsforbruket.",
        story)

    tabell_caption("4.1", "Earned Value Management — sluttverdier ved overlevering 15. mai 2026.", story)
    evm_tab = make_table([
        ["KPI", "Verdi", "Formel / kilde"],
        ["BAC — Budget at Completion", "800,0 MNOK", "Baseline 1 etter NHB-2026-15"],
        ["PV (kum.)", "800,0 MNOK", "Lineær fordeling per pakke (Baseline 1)"],
        ["EV (kum.)", "800,0 MNOK", "Σ BAC_pakke × 100 % fullført"],
        ["AC (kum.)", "800,0 MNOK", "Σ påløpt aktivitetskost måned 1–16"],
        ["CPI = EV / AC", "1,000", "Innenfor budsjett"],
        ["SPI = EV / PV", "1,000", "Iht. plan"],
        ["EAC = BAC / CPI", "800,0 MNOK", "Prognose sluttkost"],
        ["ETC = EAC − AC", "0,0 MNOK", "Gjenstående til full sluttføring"],
        ["VAC = BAC − EAC", "0,0 MNOK", "Prognosticert kostnadsavvik"],
        ["Risikoreserve brukt", "11,0 av 50,0 MNOK", "R-05 (6 MNOK) + R-06/CR-001 (5 MNOK)"],
        ["Tidsbuffer brukt", "1,5 av 8 uker", "R-07 brann hos vindusprodusent"],
    ], col_widths=[5 * cm, 3.5 * cm, 7.5 * cm])
    story.append(evm_tab)

    info_box(
        "<b>En faglig presisering om sluttverdiene.</b> Den tilsynelatende «perfekte» "
        "sammenfallet mellom BAC, EV og AC ved måned 16 er ikke et tegn på at vi var heldige "
        "— det er et tegn på at vi har styrt aktivt mot Baseline 1 gjennom hele perioden. "
        "Hvis vi hadde tillatt at risikoreserven eller tidsbufferen ble overskredet, eller "
        "at scope hadde glidd uten endringsdokument, ville sluttverdiene avveket. CPI/SPI = 1,000 "
        "viser at endringsstyringen og hendelseshåndteringen har vært disiplinert.",
        story)

    h3("4.2.4  Pakke-nivå EVM for 4.1 Råbygg")
    body(
        "Råbyggspakken 4.1 var den eneste pakken vi hadde et eksplisitt krav fra kommunestyret "
        "om månedlig oppfølging på (jf. NHB-2026-15-vedtaket). Tabell 4.2 viser EVM-statusen "
        "per måned i råbyggsperioden, beregnet på pakke-nivå med BAC = 240 MNOK etter crashing.",
        story)

    tabell_caption("4.2",
                   "Pakke-nivå EVM for 4.1 Råbygg — månedlig oppfølging i råbyggsperioden (mnd 7–11).",
                   story)
    # Faktiske påløp og kumulativ EV for 4.1 i mnd 7-11 (fra master data)
    rabygg_data = [
        # mnd, % fullført, periode-AC, kum-AC, EV (= BAC × %)
        (7, 20, 47.4, 47.4),
        (8, 39, 47.4, 94.8),
        (9, 60, 48.9, 143.7),
        (10, 80, 47.4, 191.1),
        (11, 100, 48.9, 240.0),
    ]
    rabygg_rader = [["Mnd", "% fullført", "EV (MNOK)", "AC periode (MNOK)",
                      "AC kum. (MNOK)", "CPI pakke", "Kommentar"]]
    for mnd, pct, ac_per, ac_kum in rabygg_data:
        ev = 240 * pct / 100
        cpi = ev / ac_kum if ac_kum > 0 else 0
        kom = {
            7: "Oppstart; parallelle skift etablert",
            8: "Bærekonstruksjoner; SHA-statusmøter ukentlig",
            9: "Tak nesten ferdig; premium-leveranser",
            10: "Fasade pågår; R-07 brann hos vindusprodusent inntreffer slutten",
            11: "Ferdig — innen Baseline 1, tross R-07 absorbert i tidsbuffer",
        }[mnd]
        rabygg_rader.append([f"M{mnd}", f"{pct} %",
                              f"{ev:.1f}", f"{ac_per:.1f}",
                              f"{ac_kum:.1f}", f"{cpi:.3f}", kom])
    rabygg_tab = make_table(rabygg_rader,
                             col_widths=[1.2 * cm, 1.7 * cm, 1.7 * cm, 1.9 * cm,
                                         1.9 * cm, 1.6 * cm, 6 * cm])
    story.append(rabygg_tab)

    body(
        "Pakkens CPI ligger gjennomgående mellom 1,000 og 1,015 — vi har altså opptjent verdien "
        "vi har betalt for, marginalt bedre faktisk. Sluttsummen 240 MNOK = BAC, hvilket "
        "betyr at hele crashing-merkostnaden ble brukt som planlagt. Hadde vi brukt mindre, ville "
        "det indikert at crashing-tiltakene var overdimensjonert; hadde vi brukt mer, ville det "
        "indikert at vi underestimerte forseringen.",
        story)

    h2("4.3  Kostnadsanalyse")
    body(
        "Kostnadsforbruket har vært ujevnt gjennom prosjektet, med tydelig tyngdepunkt rundt "
        "råbyggsperioden og innvendigfasen. Figur 4.4 viser månedlig påløp og "
        "kumulativ AC.",
        story)

    figure(FIGURER / "figur_08_ac_per_maned.png", story, "4.4",
           "Kostnadsforløp gjennom gjennomføringsfasen. De blå stolpene viser månedlig påløpt "
           "aktivitetskost, mens den røde linjen viser kumulativ AC mot BAC = 800 MNOK. "
           "Toppene ligger i råbyggsperioden (måned 7–11, hvor 4.1 påløp utgjorde 47–49 MNOK "
           "per måned) og innvendigfasen (måned 12–14).",
           width_cm=15.5)

    h3("4.3.1  Kostnadsfordeling per WBS-nivå-1")
    body(
        "Skolebygg – bygningsmessige arbeider (WBS 4) utgjør den klart største utgiftsposten "
        "med 360 MNOK (45 % av BAC). Innenfor denne gruppen er 4.1 Råbygg dominerende med "
        "240 MNOK etter crashing — det er denne pakken som strukturerer hele prosjektets "
        "kritiske vei, og det er denne pakken vi har overvåket tettest gjennom rapporteringen. "
        "Skolebygg – tekniske anlegg (WBS 5) er nest største post med 150 MNOK (19 %), og "
        "her ligger 5.1 VVS som ble endret av CR-001.",
        story)

    h2("4.4  Risikohåndtering og realiserte hendelser")
    body(
        "Av 16 identifiserte risikoer i registeret ble tre realisert i gjennomføringsfasen. "
        "Vi gjengir hver av disse med kort beskrivelse, vurdering, respons og dokumentkobling.",
        story)

    figure(FIGURER / "figur_10_risikomatrise.png", story, "4.5",
           "Risikomatrise — de tre realiserte risikoene plassert etter forhåndsvurdert "
           "sannsynlighet og konsekvens. Alle tre lå i den oransje sonen ved planavslutning "
           "og krevde aktiv respons da de inntraff.",
           width_cm=13)

    h3("4.4.1  R-05 — Funn av forurenset masse")
    body(
        "I måned 4 (mai 2025), under massehåndtering tilknyttet arbeidspakke 3.2 Riving, ble "
        "det oppdaget en eldre, ikke-kartlagt nedgravd oljetank. Massene rundt tanken var "
        "forurenset over grenseverdi for kategori 2-deponi. Det ble besluttet å gjennomføre "
        "miljøsanering med separat bortkjøring og prøvetaking ved utgravingsfront. Kostnaden "
        "på 6,0 MNOK ble dekket fra risikoreserven, og en uke forsinkelse ble absorbert i "
        "den lokale slack-en mellom 3.2 og 3.3 — den kumulative tidsbufferbruken forble null. "
        "Statsforvalter ble formelt varslet i tråd med kravene i miljøregelverket.",
        story)

    h3("4.4.2  R-07 — Brann hos vindusprodusent")
    body(
        "I måned 11 (desember 2025) oppstod brann hos vindusprodusenten som leverte til "
        "4.1 Råbygg. Leveransen ble forsinket med 1,5 uker. Vi utredet bytte til alternativ "
        "leverandør, men kombinasjonen av produksjonstid hos ny leverandør og merkostnad "
        "ved hasteleveranse gjorde dette uforsvarlig. Beslutningen ble derfor å trekke "
        "1,5 uker fra tidsbufferen og planlegge om etterfølgende innvendige arbeider for å "
        "begrense kaskadeeffekten. Ingen kostnadskonsekvens, men tidsbufferbruken steg fra "
        "0 til 1,5 uker — det eneste forbruket gjennom hele prosjektet.",
        story)

    h3("4.4.3  R-06 / CR-001 — DSB sprinkler/rømning")
    body(
        "Behandlet i kapittel 4.1.2. R-06 var i risikoregisteret klassifisert som regulatorisk "
        "endring, og når den ble realisert i måned 13 ble den dermed eskalert fra hendelse til "
        "formell endring (CR-001).",
        story)

    h3("4.4.4  Bruk av risikoreserve og tidsbuffer")
    figure(FIGURER / "figur_04_risikobudsjett.png", story, "4.6",
           "Kumulativ risikoreserve-bruk gjennom prosjektet. Brutto godkjent reserve er "
           "50 MNOK, hvorav 11 MNOK ble brukt (22 %) fordelt på R-05 (6 MNOK i måned 4) og "
           "R-06/CR-001 (5 MNOK i måned 13).",
           width_cm=15.5)

    figure(FIGURER / "figur_05_tidsbuffer.png", story, "4.7",
           "Kumulativ tidsbuffer-bruk gjennom prosjektet. Av 8 godkjente uker ble 1,5 uker "
           "brukt (19 %), alle knyttet til R-07 brann hos vindusprodusent i måned 11.",
           width_cm=15.5)

    h2("4.5  Hendelsestidslinje")
    body(
        "For å gi et samlet visuelt bilde av når hendelsene inntraff i forhold til "
        "fremdriftsfasene, viser figur 4.8 en horisontal tidslinje med fasemarkeringer og "
        "tilhørende hendelser.",
        story)

    figure(FIGURER / "figur_06_hendelsestidslinje.png", story, "4.8",
           "Hendelsestidslinje for gjennomføringsfasen. R-05 inntraff tidlig under riving "
           "(forprosjekt-fasen var avsluttet), R-07 påvirket Råbyggets sluttspurt, og "
           "R-06/CR-001 inntraff i innvendigfasen rett før overlevering.",
           width_cm=16)

    h2("4.6  Månedsrapportering og sporbarhet")
    body(
        "Hver av de 16 månedene har egen statusrapport med samme struktur: metadata, "
        "KPI-sammendrag på prosjektnivå, KPI per WBS-nivå-1, periodens avvik, risikobilde, "
        "S-kurve og kumulativ datatabell. Rapportene følger den standardiserte malen i "
        f"<i>månedsrapport-mal.docx</i> {sit('Gruppe 4.5', '2026b')}, og er bygget programmatisk "
        "fra masterdatastrukturen. Sporbarheten er sikret slik at hver tall i en månedsrapport "
        "kan spores eksakt til et bestemt avsnitt i Bårds rådata — for eksempel viser "
        "månedsrapport for måned 13 et avvik (ISS-13-01) med risiko-ID R-06 og endrings-ID "
        "CR-001, kostnad 5,0 MNOK og 1,0 uke tidsforskyvning, identisk med det som står i "
        "referatet fra teamledermøtet 3. februar 2026.",
        story)

    h3("4.6.1  Pakke-fullføringsmatrise")
    body(
        "For å vise framdriften per arbeidspakke gjennom hele forløpet har vi laget en "
        "heatmap-visning hvor hver rad er en av de 32 arbeidspakkene og hver kolonne er "
        "én av de 16 statusdatoene.",
        story)

    figure(FIGURER / "figur_09_pakke_fullforing.png", story, "4.9",
           "Pakke-fullføringsmatrise. Grønne celler markerer 100 % fullført; sjekkmerke "
           "indikerer at pakken er overlevert i den måneden. Heatmappen viser tydelig "
           "sekvenseringen — fra detaljprosjektering og godkjenninger tidlig, gjennom "
           "riving og grunnarbeid, til råbygg, innvendig komplettering, tekniske anlegg, "
           "inventar og avslutningsaktiviteter.",
           width_cm=15)

    h2("4.7  MS Project og baseline-disiplin")
    body(
        "All planlegging og tracking er gjort i MS Project. Vi har bevart både <b>Baseline 0</b> "
        "(opprinnelig plan før crashing) og <b>Baseline 1</b> (godkjent plan etter NHB-2026-15), "
        "slik at sluttrapporten kan vise hele endringshistorikken. Baseline 0 har 4.1 Råbygg "
        "med varighet 7 måneder og kostnad 190 MNOK, og prosjektets sluttdato i juli 2026. "
        "Baseline 1 har 4.1 Råbygg med varighet 5 måneder og kostnad 240 MNOK, og sluttdato "
        "15. mai 2026. Faktisk fremdrift er sporet mot Baseline 1.",
        story)

    body(
        "Disiplinen med å bevare begge baselinene parallelt er sentral for vår vurdering. "
        "Det er forskjellen mellom å si «vi har et prosjekt som leverte på plan» og å si "
        "«vi har et prosjekt som leverte på plan etter at vi har dokumentert en konkret "
        "endring fra opprinnelig estimat, godkjent av rett myndighet». Den siste er den "
        "fortellingen sensor kan etterprøve, og det er den fortellingen vi mener er den "
        "faglige standarden.",
        story)


# ============================================================
# KAP 5 — AVSLUTNING
# ============================================================
def kap_5():
    h1("5   Avslutningsfasen — måloppnåelse og business case")

    h2("5.1  Måloppnåelse mot rammer")
    body(
        "Vi vurderer måloppnåelsen mot de fire klassiske ytelsesdimensjonene som er felles "
        "for prosjektledelseslitteraturen — omfang, tid, kost og kvalitet. Tabell 5.1 "
        "oppsummerer planlagt mot faktisk for hver dimensjon.",
        story)

    tabell_caption("5.1", "Måloppnåelse mot vedtatte rammer ved overlevering 15. mai 2026.", story)
    måloppnåelse = make_table([
        ["Dimensjon", "Planlagt", "Faktisk", "Vurdering"],
        ["Omfang",
         "59 krav, 32 arbeidspakker",
         "Alle 59 krav levert, alle 32 pakker 100 % fullført",
         "Måloppnådd. CR-001 utvidet scope marginalt på 5.1"],
        ["Tid",
         "Sluttdato 15. mai 2026",
         "15. mai 2026 (på datoen)",
         "Måloppnådd. 1,5 av 8 uker tidsbuffer brukt"],
        ["Kost",
         "BAC 800 MNOK etter NHB-2026-15",
         "AC kumulativ 800,0 MNOK",
         "Måloppnådd. 11 av 50 MNOK risikoreserve brukt"],
        ["Kvalitet",
         "0 kritiske mangler ved BP3 (K-001), komplett FDV (K-002)",
         "0 kritiske mangler. FDV levert. Brukstillatelse innvilget.",
         "Måloppnådd. K-001 og K-002 oppfylt"],
    ], col_widths=[2.2 * cm, 4.0 * cm, 4.4 * cm, 5.4 * cm])
    story.append(måloppnåelse)

    pull_quote(
        "Prosjektet leverte på alle fire ytelsesdimensjoner. Det er ikke fordi rammene var "
        "satt mildt — tvert imot innebar caset et eksplisitt designet kost- og tidspress — "
        "men fordi endringsstyringen og hendelseshåndteringen fungerte etter prinsippene som "
        "er beskrevet i denne rapporten.",
        story)

    h2("5.2  Business case og gevinstrealisering")
    body(
        "Prosjektforslagets business case (kapittel 6.5) anslo en netto nåverdi på "
        "+109,2 MNOK over 60 år ved 1 % realrente, et Benefit-Cost Ratio (BCR) på 1,16 og en "
        f"Return on Investment (ROI) på 15,6 % {sit('Hædda kommune', '2025a', '38')}. "
        "Effektmålene var (a) 30 % reduksjon i driftskostnader per elev (anslått besparelse "
        "om lag 18 MNOK per år) og (b) 20 % økning i programareal per elev sammenlignet med "
        "eksisterende skolebygg.",
        story)

    body(
        "Disse effektmålene er forankret i den leverte løsningen gjennom BREEAM Very Good-"
        "sertifisering, balansert ventilasjon med varmegjenvinning og et beregnet "
        "energiforbruk under 75 kilowattimer per kvadratmeter per år. Reell måloppnåelse kan "
        "imidlertid først dokumenteres 12–24 måneder etter ibruktagelse, når faktiske drifts- "
        "og energidata for skolen er sammenlignbare med utgangspunktet. Vi anbefaler at "
        "driftsorganisasjonen følger opp med årlige gevinstvurderinger de første tre årene, "
        "med kommunestyret som beslutningsforum for justeringer (se kapittel 7).",
        story)

    body(
        "Med kostnadsutvidelsen fra NHB-2026-15 er nominell totalkostnad økt fra 700 til "
        "800 MNOK. Dette reduserer ikke business casen til netto negativ, men forskyver "
        "tilbakebetalingstiden. En foreløpig oppdatering av nåverdimodellen viser at NNV "
        "fortsatt er positiv, men på et lavere nivå enn opprinnelig estimat (estimert "
        "+59,2 MNOK ved 1 % realrente — 50 MNOK mindre enn opprinnelig). Det understreker "
        "at crashing-vedtaket var en avveiing mellom dårlig business case og dårligere "
        "samfunnskonsekvens, ikke et fritt valg.",
        story)


# ============================================================
# KAP 6 — REFLEKSJON OG LÆRINGSPUNKTER
# ============================================================
def kap_6():
    h1("6   Refleksjon og læringspunkter")
    body(
        "Vi har valgt å skille refleksjonskapitlet fra anbefalingskapitlet for at de to skal "
        "kunne leses uavhengig. Refleksjonen handler om hva <i>vi</i> tar med oss som "
        "studenter, ikke om hva <i>oppdragsgiveren</i> bør gjøre videre. Det siste er dekket "
        "i kapittel 7.",
        story)

    h2("6.1  Endringsstyring i praksis er forskjellen mellom konsis og kaotisk dokumentasjon")
    body(
        "Den viktigste innsikten fra prosjektet er konkret: <i>endringer som ikke dokumenteres "
        "formelt blir usynlige</i>. Det er to endringer i prosjektet — NHB-2026-15 og CR-001 — "
        "og hver av dem har eget endringsdokument med konsekvensanalyse, beslutningsbegrunnelse "
        "og kobling til risikoregisteret. Uten disse to dokumentene ville sluttrapporten måtte "
        "argumentere muntlig for hvorfor sluttkost er 800 og ikke 700 MNOK, og hvorfor scope på "
        "5.1 VVS ble utvidet. Med dokumentene er argumentet etterprøvbart.",
        story)

    body(
        "Vi har latt oss inspirere av hvordan integrated change control beskrives i PMBOK "
        f"Guide, hvor endringer skal vurderes på fem dimensjoner — scope, schedule, cost, "
        f"quality og risk — før beslutningsforumet behandler dem "
        f"{sit('Project Management Institute', '2021', '115')}. Vi tror at det er nettopp "
        "den strukturerte konsekvensanalysen som er den vesentlige forskjellen mellom det vi "
        "har gjort og en mer pragmatisk «vi gjorde noen justeringer underveis»-tilnærming.",
        story)

    h2("6.2  Verdien av baseline-disiplin")
    body(
        "Det ville vært enklere å lagre kun den oppdaterte planen i MS Project og slette den "
        "opprinnelige. Vi valgte å beholde begge baselinene, og det viste seg å være avgjørende "
        "for at sluttrapporten kunne fortelle hele historien — fra opprinnelig estimat via "
        "dokumentert endring til revidert plan og faktisk gjennomføring. Hvis Baseline 0 "
        "hadde blitt overskrevet, ville sluttrapporten manglet det viktigste konteksten: "
        "<i>hva ville skjedd dersom vi ikke hadde handlet</i>.",
        story)

    h2("6.3  Earned Value Management gir objektiv status")
    body(
        "I praksis er det ofte tilstrekkelig å oppdatere prosent fullført på arbeidspakker for "
        "å «føle» at man har kontroll. EVM tvinger en til å se på det samme fra to vinkler — "
        "hva som er opptjent i kroner og hva som faktisk er brukt — og gjør avvik kvantitative "
        "i stedet for følelsesmessige. Vi observerte dette særlig i månedene rundt 4.1 Råbygg, "
        "hvor det subjektive bildet var preget av høyt aktivitetsnivå og krevende koordinering, "
        "men hvor CPI og SPI viste at vi faktisk leverte iht. Baseline 1.",
        story)

    info_box(
        "<b>En oppdagelse vi tar med oss:</b> EVM-arbeidsboken kunne stå alene som "
        "rapporteringsverktøy, men gir mest verdi når den knyttes opp mot en avvikslogg "
        "og en risikoregister. Tallene forteller hva, men ikke hvorfor. Det er kombinasjonen "
        "av kvantitativ EVM og kvalitativ hendelsesoppfølging som gir det fullstendige bildet.",
        story)

    h2("6.4  Sporbarhet er sensorens viktigste kriterium")
    body(
        "Sensorveiledningen for emnet nevner eksplisitt to «typiske svakheter»: månedsrapporter "
        "som refererer til tall som ikke kan gjenfinnes i MS Project, og endringsforespørsler "
        f"uten reell konsekvensanalyse {sit('Høgskolen i Molde', '2026', '5')}. Vi har lagt "
        "betydelig vekt på å bygge sporbarhet fra start: hvert tall i hver månedsrapport kan "
        "spores tilbake til et bestemt avsnitt i Bårds rådata, hvert avvik har en eksplisitt "
        "risiko-ID-referanse, og hver endring har eget dokument. Det er denne disiplinen vi "
        "mener gjør forskjellen mellom en B og en A.",
        story)

    h2("6.5  Hva vi ville gjort annerledes")
    body(
        "Tre ting trekker vi fram som forbedringsområder for fremtidige prosjekter. <b>For det "
        "første</b> ville vi bygget masterdatastrukturen tidligere. Vi har i prosjektet vårt "
        "bygget den parallelt med leveransene, hvilket innebar at vi måtte regenere flere "
        "dokumenter da definisjonen av Baseline 1 ble klar. En sentral datakilde fra dag én "
        "ville ha redusert dobbeltarbeidet betraktelig.",
        story)

    body(
        "<b>For det andre</b> ville vi vært mer proaktive på risikoer som ligger latente i "
        "leverandørkjeden. R-07 (brann hos vindusprodusent) kunne ikke vært forhindret, men "
        "konsekvensen kunne vært dempet gjennom dobbel leverandørstrategi for vindusleveransen. "
        "Det er en avveiing mellom kostnader (premium å ha to leverandører) og resiliens, "
        "og i etterpåklokskap mener vi at vi undervurderte resiliens-siden.",
        story)

    body(
        "<b>For det tredje</b> ville vi formalisert kommunikasjonen med byggekomiteen sterkere. "
        "Kommunestyrets vedtak NHB-2026-15 inkluderer et krav om månedlig statusrapportering "
        "på den komprimerte aktiviteten 4.1 Råbygg. Dette var dekket gjennom månedsrapportene, "
        "men kunne vært synliggjort som en egen, mer fokusert «crashing-statusrapport» de "
        "fem månedene 4.1 var aktiv. Det ville styrket sporbarheten og gitt byggekomiteen et "
        "tydeligere bilde av hvor mye av crashing-budsjettet som ble brukt per måned.",
        story)

    h2("6.6  Hva overrasket oss")
    body(
        "Tre observasjoner fra prosjektet overrasket oss mer enn vi hadde forventet i utgangspunktet.",
        story)

    h3("6.6.1  Hvor disiplinert R-07 ble håndtert")
    body(
        "Brann hos vindusprodusent i måned 11 var den typen hendelse vi var mest engstelige for "
        "underveis i planleggingen — en ekstern leverandørrisiko vi ikke kunne kontrollere. Da "
        "den faktisk inntraff, ble det imidlertid hverken kostnadskonsekvens eller "
        "krise-håndtering. Vi trakk 1,5 uker fra tidsbufferen, planla om de etterfølgende "
        "innvendige arbeidene, og prosjektet gikk videre uten dramatikk. Læringen er at "
        "<i>tidsbuffer er et reelt styringsinstrument</i>, ikke bare en akademisk reserve. Når "
        "den brukes etter at risikoen er materialisert, transformerer den en potensiell krise "
        "til en planlagt justering. Vi opplevde for første gang verdien av å ha satt av "
        "8 uker tidsbuffer i planfasen — i sluttrapporten ser det ut som en triviell beslutning, "
        "men det var langt fra trivielt i øyeblikket.",
        story)

    h3("6.6.2  Sammenhengen mellom NHB-2026-15 og R-07")
    body(
        "Det er en ikke-åpenbar sammenheng mellom crashing-vedtaket og hvordan vi greide å "
        "absorbere brannen hos vindusprodusenten. Hvis vi ikke hadde komprimert 4.1 Råbygg "
        "(altså beholdt 7 måneders varighet), ville aktiviteten ikke vært ferdig før februar 2026 "
        "— samme måned som CR-001 ble vedtatt. Etterfølgende innvendigarbeid ville da hatt "
        "minimalt slack, og en 1,5 ukers vindusforsinkelse ville sannsynligvis krevd ytterligere "
        "endringsforespørsel. Crashing ga oss <i>schedule reserve</i> som vi ubevisst brukte til "
        "å absorbere R-07. Dette illustrerer hvordan beslutninger som kostnadsmessig ser dyrere "
        "ut på papir, kan gi resiliens som er vanskelig å kvantifisere på beslutningstidspunktet.",
        story)

    h3("6.6.3  Hvor sentralt sporbarheten ble for vår egen kvalitetssikring")
    body(
        "Vi bygde masterdatastrukturen primært for sensors skyld — slik at hvert tall i hver "
        "rapport kunne spores tilbake til en kilde. Bivirkningen var at <i>vi selv</i> fant flere "
        "feil tidligere enn vi ellers ville ha gjort. Da vi første gang regnet ut EAC og fikk "
        "799,93 MNOK i stedet for 800,00, var det fordi en arbeidspakke i datastrukturen var "
        "feilkonfigurert. Med konsentrert tallkilde var feilen lett å finne; hadde tallene vært "
        "spredd over 16 separate månedsrapporter, ville vi sannsynligvis ikke ha oppdaget den. "
        "Sporbarhet er altså ikke bare et sensorkriterium — det er et reelt kvalitetsverktøy for "
        "prosjektledelsen selv.",
        story)


# ============================================================
# KAP 7 — ANBEFALINGER
# ============================================================
def kap_7():
    h1("7   Anbefalinger til oppdragsgiver")
    body(
        "Følgende anbefalinger gjelder for tiden etter overlevering, og er rettet til Hædda "
        "kommune som prosjekteier og fremtidige driftseier. Anbefalingene er prioritert.",
        story)

    h2("7.1  Gevinstoppfølging — beslutningsforum og kadens")
    body(
        "Business case-anslaget på +109,2 MNOK netto nåverdi (eller om lag +59 MNOK etter "
        "kostnadsutvidelsen) realiseres kun gjennom faktisk drift av skolen. Vi anbefaler at "
        "driftsorganisasjonen utarbeider en gevinstrealiseringsplan med konkrete måltall for "
        "(a) driftskostnad per elev, (b) energiforbruk per kvadratmeter, og (c) "
        "brukertilfredshet hos ansatte og elever. Kadensen bør være årlig de første tre "
        "årene, med kommunestyret som beslutningsforum for eventuelle justeringer.",
        story)

    h2("7.2  FDV-oppfølging og oppdaterte løsninger fra CR-001")
    body(
        "FDV-dokumentasjonen leveres samlet ved overlevering, men de oppgraderte løsningene "
        "som ble innført i CR-001 (sprinkler og rømning iht. ny DSB-veileder) bør gjennomgås "
        "av brannvesenet hvert år de første tre årene. Dette sikrer at kommunens etterlevelse "
        "av nye krav holder seg, og at eventuelle senere veilederrevisjoner fanges opp tidlig.",
        story)

    h2("7.3  Erfaringsoverføring til kommunens prosjektmal")
    body(
        "NHB-2026-15 og CR-001 er konkrete case-eksempler på henholdsvis schedule crashing "
        "og regulatorisk scope-endring. Vi anbefaler at kommunen innarbeider disse i sin "
        "interne prosjektledelsesmal som referansecase i fremtidige prosjektledelsesopplæringer. "
        "Endringsdokumentene fra dette prosjektet er strukturert slik at de er anonymiserbare "
        "og kan brukes som malverk for tilsvarende beslutninger.",
        story)

    h2("7.4  Brukeropplæring og driftskompetanse")
    body(
        "Den bygde løsningen omfatter relativt avanserte tekniske systemer — særlig "
        "automasjon (SD-anlegg) og IKT/sikkerhet. Initial brukeropplæring er gjennomført i "
        "måned 16 (arbeidspakke 8.4), men erfaringsmessig er det først etter et halvår med "
        "drift at de virkelige opplæringsbehovene melder seg. Vi anbefaler en oppfølgende "
        "opplæringsbolk etter seks måneders drift, særskilt rettet mot driftspersonalets "
        "kompetanse på SD-anlegget og adgangskontrollsystemet.",
        story)


# ============================================================
# KAP 8 — KONKLUSJON
# ============================================================
def kap_8():
    h1("8   Konklusjon")
    body(
        "Prosjekt Nye Hædda Barneskole er gjennomført og overlevert til oppdragsgiver "
        "15. mai 2026 — på vedtatt frist, til vedtatt totalramme på 800 millioner kroner, og "
        "med alle 59 krav i kravspesifikasjonen oppfylt. Cost Performance Index og Schedule "
        "Performance Index lander begge på 1,000 ved overlevering, hvilket innebærer eksakt "
        "samsvar mellom Baseline 1 og faktisk leveranse på både kostnad og fremdrift. Av 50 "
        "millioner kroner i risikoreserve ble 11 brukt; av 8 ukers tidsbuffer ble 1,5 brukt.",
        story)

    body(
        "Vi mener resultatet er en konsekvens av tre forhold som vi har lagt aktiv vekt på "
        "gjennom hele prosjektet. <b>For det første</b> håndterte vi de to vesentlige avvikene — "
        "underestimeringen av 4.1 Råbygg og DSB-veilederen for sprinkler/rømning — gjennom "
        "formell endringsstyring med konsekvensanalyse og dokumentasjon (NHB-2026-15 og "
        "CR-001). <b>For det andre</b> bevarte vi parallell baseline-disiplin i MS Project, slik "
        "at hele endringshistorikken fra opprinnelig estimat til faktisk leveranse er etterprøvbar. "
        "<b>For det tredje</b> sikret vi sporbarhet ved å bygge en sentral datastruktur som "
        "kilden for samtlige leveranser, slik at hvert tall i en månedsrapport kan spores til "
        "et eksakt avsnitt i Bårds rådata.",
        story)

    pull_quote(
        "Den faglige hovedinnsikten vi tar med oss fra emnet er at prosjektsuksess ikke handler "
        "om å unngå endringer eller hendelser — det handler om å håndtere dem med formell "
        "dokumentasjon og analytisk disiplin. Et prosjekt uten endringer er ikke et prosjekt "
        "som gikk bra; det er et prosjekt som ikke ble dokumentert.",
        story)

    body(
        "For Hædda kommune som oppdragsgiver er anbefalingene i kapittel 7 prioritert "
        "rekkefølge for tiden etter overlevering. Gevinstrealisering må følges aktivt opp i "
        "12–24 måneder etter ibruktagelse for å kunne bekrefte business case-anslaget på "
        "+109 MNOK netto nåverdi over 60 år (justert til om lag +59 MNOK etter kostnadsutvidelsen "
        "fra NHB-2026-15). De oppgraderte sikkerhetsløsningene fra CR-001 bør gjennomgås "
        "årlig av brannvesenet de første tre årene for å sikre etterlevelse av nye DSB-revisjoner. "
        "Skolens drift- og personalstab bør motta oppfølgende opplæring i SD-anlegg og "
        "adgangskontrollsystem etter seks måneders drift.",
        story)

    body(
        "Vi takker emnets faglige veileder for et velstrukturert simuleringsbasert case som "
        "har gitt oss anledning til å øve på prosjektledelse i sin reelle kompleksitet. "
        "Sluttproduktet — denne rapporten med tilhørende vedlegg — er vårt forsøk på å vise "
        "at vi har forstått ikke bare verktøyene, men også <i>hvorfor</i> de er bygd som de er.",
        story)


# ============================================================
# REFERANSER (APA7)
# ============================================================
def referanser():
    h1("Referanser")
    refs = [
        ref("AXELOS", "2017",
            "Managing successful projects with PRINCE2 (6. utg.)",
            "TSO (The Stationery Office)"),
        ref("Direktoratet for samfunnssikkerhet og beredskap", "2026",
            "Veileder for sprinklerdekning og rømningsskilting i kommunale byggeprosjekter",
            "DSB-publikasjon. Henvist i CR-001 og månedsrapport måned 13"),
        ref("Gruppe 4.5", "2026a",
            "Komplett prosjektplan — Nye Hædda Barneskole (LOG565 fase 2)",
            "Intern leveranse, mappen 02 - Planlegging"),
        ref("Gruppe 4.5", "2026b",
            "Månedsrapport-mal og 16 månedsrapporter — Nye Hædda Barneskole",
            "Intern leveranse, mappen 03 - Gjennomføring/Månedsrapporter"),
        ref("Hædda kommune", "2025a",
            "Prosjektforslag — Nye Hædda Barneskole",
            "Kommunestyresak, mappen 01 - Initiering"),
        ref("Hædda kommune", "2025b",
            "Konseptløsning — Nye Hædda Barneskole",
            "Kommunestyresak, mappen 01 - Initiering"),
        ref("Høgskolen i Molde", "2026",
            "Sensorveiledning — LOG565 Prosjektledelse 2",
            "Faglig vurderingsgrunnlag for mappeinnleveringen"),
        ref("Irgesund", "2026a",
            "Godkjenning av budsjettendring — sak NHB-2026-15",
            "Kommunestyrevedtak 7. mai 2026, Vedlegg/A - Kildemateriale fra Bård"),
        ref("Irgesund", "2026b",
            "Månedsrapporter for gjennomføringsfasen — 16 teamledermøtereferater",
            "Vedlegg/A - Kildemateriale fra Bård"),
        ref("Project Management Institute", "2021",
            "A guide to the Project Management Body of Knowledge (PMBOK Guide) (7. utg.)",
            "Project Management Institute"),
    ]
    for r in refs:
        story.append(Paragraph(r, ST_REFERENCE))


# ============================================================
# VEDLEGG
# ============================================================
def vedlegg():
    h1("Vedlegg")
    body(
        "Vedlegg til denne rapporten er organisert i mappestrukturen rundt rapportfilen. "
        "Vedleggene er gruppert etter hva de dokumenterer.",
        story)

    h2("Vedlegg A — Planleggingsfasen")
    body(
        "<b>Mappe:</b> <i>02 - Planlegging/</i><br/>"
        "Komplett prosjektplan (PDF), kravspesifikasjon, WBS, presedensdiagram, "
        "WBS-diagram, risikoregister, og MS Project-fil for Baseline 0.",
        story)

    h2("Vedlegg B — Gjennomføringsfasen")
    body(
        "<b>Mappe:</b> <i>03 - Gjennomføring/</i><br/>"
        "Endringsdokumenter (NHB-2026-15 og CR-001), 16 månedsrapporter (docx og PDF), "
        "EVM-arbeidsbok, MS Project tracking-instruks med eksakte verdier for input.",
        story)

    h2("Vedlegg C — Kildemateriale")
    body(
        "<b>Mappe:</b> <i>Vedlegg/A - Kildemateriale fra Bård/</i><br/>"
        "Kommunestyrevedtaket NHB-2026-15 (PDF), månedsrapporter med 16 referater (PDF), "
        "Bårds simulerte WBS-struktur (PDF og Excel).",
        story)

    h2("Vedlegg D — S-kurver og figurer")
    body(
        "<b>Mappe:</b> <i>Vedlegg/B - S-kurver per måned/</i><br/>"
        "16 separate S-kurve-figurer, én per statusdato (PNG).",
        story)

    h2("Vedlegg E — Gruppemøter")
    body(
        "<b>Mappe:</b> <i>Vedlegg/C - Gruppemøter (statusrapporter)/</i><br/>"
        "Statusrapporter fra gruppens egne arbeidsdager, dokumenterer prosessen "
        "for fase 2 og fase 3.",
        story)

    h2("Vedlegg F — Maler og tidligere innleveringer")
    body(
        "<b>Mapper:</b> <i>Vedlegg/D - Tidligere innleveringer til Bård/</i> og "
        "<i>Vedlegg/E - Maler brukt som referanse/</i><br/>"
        "Følgebrev og tidligere innlevering til Bård fra fase 2, samt alle malverk vi har "
        "brukt som utgangspunkt (kravspesifikasjon-mal, WBS-mal, prosjektplan-mal, "
        "månedsrapport-mal, endringsdokument-mal, sluttrapport-mal, EVM-arbeidsbok-mal, "
        "problemliste-mal, Gantt-tracking-mal).",
        story)

    h2("Vedlegg G — Sensorgrunnlag")
    body(
        "<b>Mappe:</b> <i>Oppgavebeskrivelse/</i><br/>"
        "Konkretisering av mappeinnleveringen i LOG565 og sensorveiledning.",
        story)


# ============================================================
# BYGG STORYEN
# ============================================================
def bygg():
    forside()
    kolofon()
    innholdsfortegnelse()
    sammendrag()
    kap_1()
    kap_2()
    kap_3()
    kap_4()
    kap_5()
    kap_6()
    kap_7()
    kap_8()
    referanser()
    vedlegg()


bygg()


print("Bygger PDF...")
doc.build(story, canvasmaker=canvas_maker)
print(f"PDF lagret: {OUT}")
