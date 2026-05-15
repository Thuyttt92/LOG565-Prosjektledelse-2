# -*- coding: utf-8 -*-
"""Bygger en superenkel guide for manuell innskriving i MS Project.

Skrevet for å være lett å lese selv med migrene:
- Korte setninger
- Forklaringer på HVORFOR
- Mye luft
- En ting om gangen
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER

from _pdf_helpers import make_table

PATH = r"C:\Users\Gusta\OneDrive\Documents\Privat\Studier\Bachelore i Logistikk\LOG565 - Prosjektledelse\02 - Planlegging\GANTT - Manuell innskriving (enkel guide).pdf"

BLUE = colors.HexColor("#1F4E79")
LIGHTBLUE = colors.HexColor("#2E75B6")
GREEN = colors.HexColor("#548235")
ORANGE = colors.HexColor("#C65911")
GREY = colors.HexColor("#595959")
LIGHTYELLOW = colors.HexColor("#FFF2CC")
LIGHTGREEN = colors.HexColor("#E2EFDA")
LIGHTGREY = colors.HexColor("#F2F2F2")

styles = getSampleStyleSheet()

st_title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24, leading=28,
                          alignment=TA_CENTER, textColor=BLUE, spaceAfter=8)
st_subtitle = ParagraphStyle("sub", fontName="Helvetica", fontSize=13, leading=17,
                             alignment=TA_CENTER, textColor=GREY, spaceAfter=20)
st_step_title = ParagraphStyle("steptitle", fontName="Helvetica-Bold", fontSize=18, leading=22,
                                textColor=BLUE, spaceBefore=18, spaceAfter=6)
st_h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=17,
                       textColor=LIGHTBLUE, spaceBefore=12, spaceAfter=4)
st_body = ParagraphStyle("body", fontName="Helvetica", fontSize=11.5, leading=16,
                         alignment=TA_LEFT, spaceAfter=6)
st_action = ParagraphStyle("action", fontName="Helvetica-Bold", fontSize=11.5, leading=16,
                           alignment=TA_LEFT, spaceAfter=14, textColor=colors.black,
                           leftIndent=10)
st_why = ParagraphStyle("why", fontName="Helvetica-Oblique", fontSize=10.5, leading=14,
                        alignment=TA_LEFT, spaceAfter=12, spaceBefore=4,
                        textColor=GREY,
                        leftIndent=10, rightIndent=10, backColor=LIGHTYELLOW,
                        borderPadding=8, borderColor=colors.HexColor("#E0C84B"),
                        borderWidth=0.5)
st_tip = ParagraphStyle("tip", fontName="Helvetica", fontSize=10.5, leading=14,
                        alignment=TA_LEFT, spaceAfter=10, spaceBefore=4,
                        textColor=GREEN,
                        leftIndent=10, rightIndent=10, backColor=LIGHTGREEN,
                        borderPadding=8)
st_warn = ParagraphStyle("warn", fontName="Helvetica-Bold", fontSize=11.5, leading=16,
                         alignment=TA_CENTER, textColor=ORANGE,
                         backColor=LIGHTYELLOW, borderPadding=12,
                         borderColor=ORANGE, borderWidth=0.5,
                         spaceBefore=8, spaceAfter=8)


def doc_body():
    s = []

    # === FORSIDE ===
    s.append(Spacer(1, 1.5*cm))
    s.append(Paragraph("Bygg Gantt i MS Project", st_title))
    s.append(Paragraph("Enkel manuell guide — skriv inn alt selv", st_subtitle))

    s.append(Paragraph("Hva er dette?", st_h2))
    s.append(Paragraph(
        "Dette er en helt enkel oppskrift. Du skal lage et Gantt-diagram i MS Project ved å "
        "skrive inn 44 rader for hånd. Det tar ca. 45 minutter. Du trenger ikke få noe til å fungere "
        "i bakgrunnen — bare følg denne PDF-en steg for steg.",
        st_body))

    s.append(Paragraph("Hva er et Gantt-diagram?", st_h2))
    s.append(Paragraph(
        "Et Gantt-diagram er en tidsplan vist som horisontale stolper. Hver stolpe er en aktivitet. "
        "Lengden på stolpen viser hvor lenge aktiviteten tar. Piler mellom stolpene viser hva som "
        "må være ferdig før noe annet kan starte.",
        st_body))

    s.append(Paragraph("Hva ender vi opp med?", st_h2))
    s.append(Paragraph(
        "Et komplett Gantt-diagram for byggingen av Nye Hædda barneskole. Det starter 1. februar 2025 "
        "og slutter rundt slutten av juli 2026. Total kostnad: 750 millioner kroner. Det er dette tallet "
        "Bård har bygget inn i oppgaven — og det viser at vi ligger over budsjett OG over tidsfristen, "
        "noe vi skal løse med 'crashing' senere.",
        st_body))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Tips for migrenedagen:</b> Ta ett steg om gangen. Det er greit å ta pause mellom hver del. "
        "Du kan ikke ødelegge noe — MS Project lagrer ikke noe automatisk.",
        st_tip))

    s.append(PageBreak())

    # === STEG 1: SETUP ===
    s.append(Paragraph("Steg 1: Klargjør MS Project", st_step_title))
    s.append(Paragraph("Åpne et tomt prosjekt og still inn et par grunninnstillinger.", st_body))

    s.append(Paragraph("1.1 — Start MS Project", st_h2))
    s.append(Paragraph("Åpne programmet. Velg <b>Fil &rarr; Ny &rarr; Tomt prosjekt</b>.", st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> Vi begynner med blank tavle og legger inn alt selv. "
        "Da slipper du å bekymre deg for at importen feiler.",
        st_why))

    s.append(Paragraph("1.2 — Sett startdato til 1. februar 2025", st_h2))
    s.append(Paragraph(
        "Klikk på <b>Prosjekt</b>-fanen ovenfor. Klikk <b>Prosjektinformasjon</b>. "
        "I dialogen som åpnes, skriv <b>01.02.2025</b> i feltet <b>Startdato</b>. Klikk OK.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> Bårds simulering antar at byggeprosjektet starter denne datoen. "
        "Hvis vi ikke setter den, bruker MS Project dagens dato — og da blir hele tidslinjen feil.",
        st_why))

    s.append(Paragraph("1.3 — Sett at varighet måles i måneder", st_h2))
    s.append(Paragraph(
        "Klikk <b>Fil &rarr; Alternativer &rarr; Tidsplan</b>. Finn raden "
        "<b>Standardvarighet er angitt i</b>. Endre den til <b>Måneder</b>. Klikk OK.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> Alle Bårds estimater er i måneder. Hvis varigheten måles i dager, "
        "tolker MS Project '15.5' som 15,5 dager i stedet for 15,5 måneder, og hele Gantt-en kollapser.",
        st_why))

    s.append(Paragraph("1.4 — Sett at nye oppgaver er automatisk planlagt", st_h2))
    s.append(Paragraph(
        "I samme dialog (<b>Fil &rarr; Alternativer &rarr; Tidsplan</b>), finn raden "
        "<b>Nye oppgaver opprettes som</b>. Endre til <b>Automatisk planlagt</b>. Klikk OK.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> 'Manuelt planlagt' betyr at MS Project ikke regner ut datoene selv. "
        "Vi vil ha automatisk — så programmet flytter aktiviteter til riktig tidspunkt når vi "
        "kobler dem sammen i Steg 4.",
        st_why))

    s.append(Paragraph(
        "Ferdig med Steg 1. Du har nå et tomt prosjekt klart til å fylle inn.",
        st_tip))

    s.append(PageBreak())

    # === STEG 2: SKRIV INN ===
    s.append(Paragraph("Steg 2: Skriv inn alle 44 rader", st_step_title))
    s.append(Paragraph(
        "Nå skal du fylle inn tabellen rad for rad. Bare 4 kolonner: navn, varighet, kostnad, ressurs. "
        "Du trenger ikke tenke på rekkefølge eller piler ennå — det fikser vi senere.",
        st_body))

    s.append(Paragraph("Hvilke kolonner må vises?", st_h2))
    s.append(Paragraph(
        "Disse 4 kolonnene skal være synlige (de er det normalt etter installasjon):",
        st_body))
    s.append(Paragraph("&bull; <b>Oppgavenavn</b> (Task Name)", st_action))
    s.append(Paragraph("&bull; <b>Varighet</b> (Duration)", st_action))
    s.append(Paragraph("&bull; <b>Ressursnavn</b> (Resource Names)", st_action))
    s.append(Paragraph(
        "Du trenger også en <b>Fast kostnad</b>-kolonne (Fixed Cost). Hvis den ikke synes: "
        "høyreklikk på en kolonneoverskrift &rarr; <b>Sett inn kolonne</b> &rarr; velg <b>Fast kostnad</b>.",
        st_action))

    s.append(Paragraph(
        "<b>Hvorfor 'Fast kostnad' og ikke 'Kostnad':</b> Kostnad-kolonnen regnes ut fra timepriser og "
        "ressurser. Vi vil bare skrive inn et tall direkte — derfor bruker vi Fast kostnad. "
        "Det er den enkleste måten.",
        st_why))

    s.append(Paragraph("Slik skriver du inn", st_h2))
    s.append(Paragraph(
        "Klikk i første celle under <b>Oppgavenavn</b>. Skriv navnet. Trykk <b>Tab</b> for å hoppe til "
        "neste kolonne. Skriv inn varighet (f.eks. <b>15.5mo</b> for 15,5 måneder). Tab. Skriv ressursnavn. "
        "Trykk <b>Enter</b> for å gå til neste rad.",
        st_body))
    s.append(Paragraph(
        "<b>Fast kostnad</b> skriver du inn i samme rad — bare tall, ingen mellomrom. "
        "Skriv f.eks. <b>25000000</b> for 25 millioner. MS Project formaterer det selv.",
        st_body))

    s.append(Paragraph(
        "<b>Tips:</b> Skriv <b>15.5mo</b> for måneder. Skriv <b>0mo</b> for milepæler. "
        "Da blir raden automatisk en milepæl (vist som en diamant ◆).",
        st_tip))

    s.append(PageBreak())

    # === TABELL: 44 RADER ===
    s.append(Paragraph("Tabellen — skriv inn disse 44 radene", st_step_title))
    s.append(Paragraph(
        "Skriv inn radene i samme rekkefølge som under. ID-nummeret får du automatisk (1, 2, 3 ...).",
        st_body))

    rows = [
        ["ID", "Oppgavenavn", "Varighet", "Fast kostnad", "Ressurs"],
        ["1", "Prosjektledelse og Administrasjon", "15.5mo", "25 000 000", "Prosjektleder"],
        ["2", "Prosjektstyring", "15.5mo", "10 000 000", "Prosjektleder"],
        ["3", "Kontraktsoppfølging", "13.0mo", "7 000 000", "Prosjektleder"],
        ["4", "Interessenthåndtering", "14.0mo", "4 000 000", "Prosjektleder"],
        ["5", "Risiko- og Kvalitetsstyring", "14.5mo", "4 000 000", "HMS-/KS-ansvarlig"],
        ["6", "Planlegging og Prosjektering", "3.0mo", "70 000 000", "Prosjekteringsleder"],
        ["7", "Detaljprosjektering", "3.0mo", "50 000 000", "Arkitekt"],
        ["8", "Offentlige Godkjenninger", "2.5mo", "12 000 000", "Arkitekt / PL"],
        ["9", "Konkurransegrunnlag", "2.0mo", "8 000 000", "Innkjøpsleder"],
        ["10", "Forberedelse og Riving", "3.0mo", "70 000 000", "Entreprenør"],
        ["11", "Miljøsanering", "0.5mo", "12 000 000", "Miljørådgiver"],
        ["12", "Riving", "1.0mo", "18 000 000", "Entreprenør"],
        ["13", "Grunnarbeid", "1.5mo", "40 000 000", "Grunnentreprenør"],
        ["14", "Skolebygg – Bygningsmessige arbeider", "9.5mo", "310 000 000", "Totalentreprenør"],
        ["15", "Råbygg", "7.0mo", "190 000 000", "Totalentreprenør"],
        ["16", "Innvendig Komplettering – 1. Etasje", "2.5mo", "35 000 000", "Totalentreprenør"],
        ["17", "Innvendig Komplettering – 2. Etasje", "2.5mo", "35 000 000", "Totalentreprenør"],
        ["18", "Innvendig Komplettering – 3. Etasje", "2.5mo", "35 000 000", "Totalentreprenør"],
        ["19", "Gymsal", "1.5mo", "15 000 000", "Totalentreprenør"],
        ["20", "Skolebygg – Tekniske Anlegg", "3.0mo", "150 000 000", "Tekniske entreprenører"],
        ["21", "VVS", "3.0mo", "55 000 000", "VVS-entreprenør"],
        ["22", "Elektro", "3.0mo", "45 000 000", "Elektroentreprenør"],
        ["23", "Heis og Vertikal Transport", "1.5mo", "12 000 000", "Heisleverandør"],
        ["24", "Automasjon (SD-anlegg)", "1.5mo", "13 000 000", "Automasjonsentreprenør"],
        ["25", "IKT og Sikkerhet", "2.0mo", "25 000 000", "IKT-leverandør"],
        ["26", "Utomhus og Uteområder", "2.0mo", "25 000 000", "Landskapsentreprenør"],
        ["27", "Lekearealer", "1.5mo", "7 000 000", "Landskapsentreprenør"],
        ["28", "Sport og Fritid", "1.5mo", "6 000 000", "Landskapsentreprenør"],
        ["29", "Infrastruktur", "2.0mo", "8 000 000", "Anleggsentreprenør"],
        ["30", "Grøntanlegg", "1.0mo", "4 000 000", "Landskapsentreprenør"],
        ["31", "Inventar og Utstyr (FF&amp;E)", "0.5mo", "70 000 000", "Innkjøpsleder"],
        ["32", "Løst Inventar", "0.5mo", "30 000 000", "Innkjøpsleder"],
        ["33", "Spesialutstyr", "0.5mo", "25 000 000", "Innkjøpsleder"],
        ["34", "AV-løsninger", "0.5mo", "15 000 000", "IKT-leverandør"],
        ["35", "Overtakelse og Avslutning", "1.5mo", "30 000 000", "Prosjektleder"],
        ["36", "Testing og Prøvedrift", "0.5mo", "10 000 000", "Prosjektleder"],
        ["37", "Ferdigbefaring (BP3)", "0.5mo", "8 000 000", "Prosjektleder"],
        ["38", "Dokumentasjon", "0.5mo", "5 000 000", "FDV-ansvarlig"],
        ["39", "Brukeropplæring", "0.25mo", "4 000 000", "Driftssjef"],
        ["40", "Prosjektevaluering", "0.25mo", "3 000 000", "Prosjektleder"],
        ["41", "MILEPÆL: BP2 – Godkjent prosjektplan", "0mo", "0", "Prosjekteier"],
        ["42", "MILEPÆL: BP3 – Godkjent ferdigstillelse", "0mo", "0", "Prosjekteier"],
        ["43", "MILEPÆL: Hard frist 15. mai 2026", "0mo", "0", "Prosjektforslag kap 4.3"],
        ["44", "MILEPÆL: Skolestart august 2026", "0mo", "0", "Hædda kommune"],
    ]
    t = make_table(rows, header=True,
                   col_widths=[0.9*cm, 6.5*cm, 1.8*cm, 3.0*cm, 4.6*cm])
    s.append(t)

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "Ta gjerne en pause her. Det er litt jobb. Du gjør det bra.",
        st_tip))

    s.append(PageBreak())

    # === STEG 3: INNRYKK ===
    s.append(Paragraph("Steg 3: Lag struktur (innrykk)", st_step_title))
    s.append(Paragraph(
        "Nå har du 44 rader på rad og rekke. Vi må fortelle MS Project hvilke rader som hører "
        "sammen som underaktiviteter. Det gjør vi ved å 'innrykke' radene.",
        st_body))

    s.append(Paragraph("Hva betyr 'innrykk'?", st_h2))
    s.append(Paragraph(
        "Tenk på det som en disposisjon i et Word-dokument: kapitler har underkapitler. I MS Project "
        "blir hovedaktiviteten (f.eks. 'Skolebygg — Bygningsmessige arbeider') en <b>sammendragslinje</b> "
        "som automatisk regner ut total varighet og kostnad fra underaktivitetene. Helt magisk.",
        st_body))

    s.append(Paragraph("Slik innrykker du", st_h2))
    s.append(Paragraph(
        "Marker en eller flere rader (klikk på radnummeret til venstre, hold Shift, klikk siste rad). "
        "Klikk på <b>Oppgave</b>-fanen ovenfor. Klikk på <b>grønn høyrepil</b> (Innrykk). "
        "Snarvei: <b>Alt + Shift + Høyrepil</b>.",
        st_action))

    s.append(Paragraph("Hvilke rader skal innrykkes?", st_h2))
    indent_rows = [
        ["Marker rader", "Disse blir underaktiviteter av..."],
        ["2 til 5", "1 — Prosjektledelse og Administrasjon"],
        ["7 til 9", "6 — Planlegging og Prosjektering"],
        ["11 til 13", "10 — Forberedelse og Riving"],
        ["15 til 19", "14 — Skolebygg – Bygningsmessige"],
        ["21 til 25", "20 — Skolebygg – Tekniske Anlegg"],
        ["27 til 30", "26 — Utomhus og Uteområder"],
        ["32 til 34", "31 — Inventar og Utstyr"],
        ["36 til 40", "35 — Overtakelse og Avslutning"],
    ]
    s.append(make_table(indent_rows, header=True, col_widths=[4.5*cm, 11.5*cm]))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Ikke innrykk radene 41–44.</b> Det er milepæler som skal stå på toppnivå.",
        st_action))

    s.append(Paragraph(
        "<b>Hvordan ser jeg at det virket:</b> Hovedaktivitetene blir <b>fete</b> og får en sort/mørkeblå "
        "stolpe i Gantt-en til høyre. Det er sammendragslinja. Hvis den ikke ble fet — sjekk innrykket på nytt.",
        st_why))

    s.append(PageBreak())

    # === STEG 4: AVHENGIGHETER ===
    s.append(Paragraph("Steg 4: Sett avhengigheter (piler mellom aktiviteter)", st_step_title))
    s.append(Paragraph(
        "Nå skal vi fortelle MS Project hvilken rekkefølge ting skal skje i. Du kan ikke begynne å "
        "bygge råbygget før grunnarbeidet er ferdig — den slags.",
        st_body))

    s.append(Paragraph("Hva er en 'foregangsoppgave'?", st_h2))
    s.append(Paragraph(
        "En foregangsoppgave er en aktivitet som må være ferdig <b>før</b> denne kan starte. "
        "I MS Project skriver vi inn ID-nummeret på foregangsoppgaven i en egen kolonne. "
        "MS Project tegner deretter en pil mellom dem og flytter aktivitetene til riktig tidspunkt.",
        st_body))

    s.append(Paragraph("Vis Foregangsoppgaver-kolonnen", st_h2))
    s.append(Paragraph(
        "Hvis kolonnen <b>Foregangsoppgaver</b> ikke synes: høyreklikk på en kolonneoverskrift &rarr; "
        "<b>Sett inn kolonne</b> &rarr; velg <b>Foregangsoppgaver</b> (Predecessors).",
        st_action))

    s.append(Paragraph("Skriv inn disse verdiene", st_h2))
    s.append(Paragraph(
        "Gå til hver rad listet under, og skriv inn ID-nummeret(ne) i Foregangsoppgaver-kolonnen. "
        "Hvis det er flere, skill med semikolon (<b>;</b>).",
        st_body))

    pred_rows = [
        ["Rad", "Aktivitet", "Foregangsoppgaver"],
        ["10", "Forberedelse og Riving", "6"],
        ["11", "Miljøsanering", "6"],
        ["12", "Riving", "11"],
        ["13", "Grunnarbeid", "12"],
        ["14", "Skolebygg – Bygningsmessige", "10"],
        ["15", "Råbygg", "13"],
        ["16", "Innv. Komplettering – 1. Etasje", "15"],
        ["17", "Innv. Komplettering – 2. Etasje", "15"],
        ["18", "Innv. Komplettering – 3. Etasje", "15"],
        ["19", "Gymsal", "15"],
        ["20", "Skolebygg – Tekniske Anlegg", "15"],
        ["21", "VVS", "15"],
        ["22", "Elektro", "15"],
        ["23", "Heis og Vertikal Transport", "15"],
        ["24", "Automasjon (SD-anlegg)", "15"],
        ["25", "IKT og Sikkerhet", "15"],
        ["26", "Utomhus og Uteområder", "10"],
        ["27", "Lekearealer", "13"],
        ["28", "Sport og Fritid", "13"],
        ["29", "Infrastruktur", "13"],
        ["30", "Grøntanlegg", "13"],
        ["31", "Inventar og Utstyr", "14"],
        ["32", "Løst Inventar", "14"],
        ["33", "Spesialutstyr", "14"],
        ["34", "AV-løsninger", "14"],
        ["35", "Overtakelse og Avslutning", "20;31"],
        ["36", "Testing og Prøvedrift", "20;31"],
        ["37", "Ferdigbefaring (BP3)", "36"],
        ["38", "Dokumentasjon", "36"],
        ["39", "Brukeropplæring", "37"],
        ["40", "Prosjektevaluering", "37;38;39"],
        ["41", "MILEPÆL: BP2", "9"],
        ["42", "MILEPÆL: BP3", "37"],
    ]
    s.append(make_table(pred_rows, header=True, col_widths=[1.2*cm, 10*cm, 4.8*cm]))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Hva betyr 20;31 (med semikolon)?</b> At aktiviteten venter på <b>både</b> rad 20 og rad 31. "
        "MS Project starter den når den seneste av de to er ferdig.",
        st_why))

    s.append(Paragraph(
        "Etter at du har skrevet inn alle: stolpene i Gantt-diagrammet til høyre flytter seg "
        "automatisk og får piler mellom seg. Det er da magien skjer.",
        st_tip))

    s.append(PageBreak())

    # === STEG 5: SJEKK TOTALER ===
    s.append(Paragraph("Steg 5: Sjekk at tallene stemmer", st_step_title))
    s.append(Paragraph(
        "Vi sjekker raskt at totalvarighet og totalkostnad er det vi forventer. "
        "Hvis ikke — har vi gjort en feil et sted.",
        st_body))

    s.append(Paragraph("Åpne Statistikk-vinduet", st_h2))
    s.append(Paragraph(
        "Klikk <b>Prosjekt</b>-fanen &rarr; <b>Prosjektinformasjon</b>. "
        "Klikk på <b>Statistikk</b>-knappen nederst i dialogen.",
        st_action))

    s.append(Paragraph("Sjekk at disse stemmer", st_h2))
    sjekk = [
        ["Felt", "Forventet verdi"],
        ["Start", "01.02.2025"],
        ["Slutt", "ca. 31.07.2026 (juli 2026)"],
        ["Total kostnad", "750 000 000 kr"],
        ["Varighet", "ca. 18 måneder"],
    ]
    s.append(make_table(sjekk, header=True, col_widths=[6*cm, 10*cm]))

    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Hvis total kostnad er 1 500 millioner istedenfor 750:</b> Innrykket i Steg 3 ble ikke gjort, "
        "så både hovedaktiviteter og underaktiviteter teller. Marker underaktivitetene og innrykk dem.",
        st_why))
    s.append(Paragraph(
        "<b>Hvis sluttdato er januar 2026 eller for tidlig:</b> En foregangsoppgave er ikke satt riktig. "
        "Sjekk Steg 4 på nytt.",
        st_why))
    s.append(Paragraph(
        "<b>Hvis sluttdato er februar 2025 (alt slutter samme dag):</b> Du brukte sannsynligvis 'd' (dager) "
        "i stedet for 'mo' (måneder) i varighetene. Skriv om varighetene.",
        st_why))

    s.append(Paragraph(
        "Hvis tallene stemmer — du har bygget Gantt-diagrammet riktig.",
        st_tip))

    s.append(PageBreak())

    # === STEG 6: VISUELLE TING ===
    s.append(Paragraph("Steg 6: Gjør det penere å se på", st_step_title))
    s.append(Paragraph(
        "Disse stegene er ikke kritiske, men gir Gantt-en det A-nivå-utseendet sensor liker.",
        st_body))

    s.append(Paragraph("6.1 — Aktiver kritisk linje (røde stolper)", st_h2))
    s.append(Paragraph(
        "Klikk <b>Format</b>-fanen ovenfor. Huk av <b>Kritiske oppgaver</b>. De røde stolpene som dukker opp "
        "er den lengste veien gjennom prosjektet — det er disse som bestemmer sluttdatoen.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> 'Kritisk sti' er et nøkkelbegrep i prosjektledelse. Sensor leter etter at du viser "
        "den. Hvis du forsinker noe på kritisk sti, forsinker du hele prosjektet.",
        st_why))

    s.append(Paragraph("6.2 — Sett frist på 15. mai 2026", st_h2))
    s.append(Paragraph(
        "Høyreklikk på rad 35 (Overtakelse og Avslutning) &rarr; <b>Oppgaveinformasjon</b> &rarr; "
        "<b>Avansert</b>-fanen. Skriv <b>15.05.2026</b> i <b>Frist</b>-feltet. OK.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> Dette er den harde fristen fra prosjektforslaget. En grønn pil dukker opp i Gantt-en. "
        "Hvis prosjektet overskrider — som det vil gjøre — vises en rød varseltrekant. Det er <b>med vilje</b>: "
        "det er denne overskridelsen vi skal løse med crashing senere.",
        st_why))

    s.append(Paragraph("6.3 — Vis kostnadstabell", st_h2))
    s.append(Paragraph(
        "Klikk <b>Visning</b>-fanen &rarr; <b>Tabeller</b> &rarr; <b>Kostnad</b>. "
        "Du ser nå alle kostnadene tydelig.",
        st_action))

    s.append(PageBreak())

    # === STEG 7: BASISPLAN ===
    s.append(Paragraph("Steg 7: Lås planen (Basisplan 0)", st_step_title))
    s.append(Paragraph(
        "Dette steget er det viktigste for A-karakter. Vi <b>låser</b> den opprinnelige planen som "
        "et frosset øyeblikksbilde. Senere — når Bård sender crashing-instruks — endrer vi planen og "
        "lager Basisplan 1. Da kan vi sammenlikne før/etter, og det er det sensor vil se.",
        st_body))

    s.append(Paragraph("Sett Basisplan 0", st_h2))
    s.append(Paragraph(
        "Klikk <b>Prosjekt</b>-fanen &rarr; <b>Angi basisplan</b> &rarr; <b>Angi basisplan...</b> "
        "I dialogen som åpnes: la den stå på <b>Basisplan</b> (det er 0). "
        "Velg <b>Hele prosjektet</b>. Klikk OK.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> En basisplan er et lagret øyeblikksbilde. Sensorveiledningen sier eksplisitt at "
        "'riktig bruk av basisplan' gir poeng. Vi setter Basisplan 0 nå (før crashing), Basisplan 1 senere "
        "(etter crashing). Da kan vi vise hele historien i sluttrapporten.",
        st_why))

    s.append(Paragraph("Steg 8: Lagre filen", st_step_title))
    s.append(Paragraph(
        "Klikk <b>Fil</b> &rarr; <b>Lagre som</b> &rarr; <b>Bla gjennom</b>. "
        "Naviger til <b>02 - Planlegging</b>-mappen. Skriv filnavn <b>Gantt - Nye Hædda barneskole</b>. "
        "Klikk Lagre.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> .mpp er MS Projects egne filformat. Det er denne fila som leveres til Bård "
        "(og senere lastes inn i Wiseflow).",
        st_why))

    s.append(Paragraph("Steg 9: Ta et skjermbilde av Gantt-en", st_step_title))
    s.append(Paragraph(
        "Klikk <b>Visning</b> &rarr; <b>Zoom</b> &rarr; <b>Hele prosjektet</b>. "
        "Maksimer MS Project-vinduet. Trykk <b>Windows + Shift + S</b> &rarr; tegn et rektangel rundt Gantt-en. "
        "Åpne Paint, lim inn (<b>Ctrl + V</b>), klikk Lagre som &rarr; PNG. "
        "Lagre som <b>Gantt - Baseline 0 - Opprinnelig estimat.png</b> i mappen <b>02 - Planlegging</b>.",
        st_action))
    s.append(Paragraph(
        "<b>Hvorfor:</b> PDF/PNG av Gantt-en er det som vises i Komplett prosjektplan-dokumentet "
        "og i sluttrapporten. Dette er den visuelle dokumentasjonen for sensor.",
        st_why))

    s.append(PageBreak())

    # === FERDIG ===
    s.append(Paragraph("Du er ferdig!", st_step_title))
    s.append(Paragraph(
        "Du har nå bygget et komplett Gantt-diagram med 44 aktiviteter, satt Basisplan 0, og lagret det. "
        "Det er det viktigste steget i fase 2.",
        st_body))

    s.append(Paragraph("Sjekkliste — kryss av når du er ferdig", st_h2))
    sjekk2 = [
        ["☐", "Startdato 01.02.2025"],
        ["☐", "44 rader er skrevet inn"],
        ["☐", "Sluttdato er rundt juli 2026"],
        ["☐", "Total kostnad er 750 000 000 kr"],
        ["☐", "Hovedaktiviteter er fete sammendragslinjer"],
        ["☐", "Piler mellom aktiviteter er synlige"],
        ["☐", "Røde stolper viser kritisk sti"],
        ["☐", "Grønn pil på frist 15.05.2026"],
        ["☐", "Basisplan 0 er satt"],
        ["☐", ".mpp-fila er lagret i '02 - Planlegging'"],
        ["☐", "PNG av Gantt er lagret i '02 - Planlegging'"],
    ]
    s.append(make_table(sjekk2, header=False, col_widths=[1.2*cm, 14.8*cm]))

    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("Hva skjer videre?", st_h2))
    s.append(Paragraph(
        "Bård sender deg en personlig melding på Teams med en 'crashing-instruks'. "
        "Den forteller hvilken aktivitet du skal forkorte, og hvor mye ekstra det koster. "
        "Da fyller du ut endringsdokumentet (CR-001) som ligger i <b>03 - Gjennomføring</b>, "
        "og du oppdaterer planen — deretter setter du Basisplan 1.",
        st_body))

    s.append(Paragraph(
        "Si fra til meg (Claude) når du har sluttdato og totalkostnad på skjermen, "
        "så fortsetter vi til neste del.",
        st_tip))

    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "<b>Ta vare på deg selv på migrenedagen.</b> Det er bedre at du tar dette i små porsjoner "
        "enn at du presser deg syk. Du ligger godt an på tid.",
        st_warn))

    return s


def main():
    doc = SimpleDocTemplate(PATH, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=1.8*cm, bottomMargin=1.8*cm,
                            title="Bygg Gantt manuelt — enkel guide",
                            author="LOG565 — Nye Hædda barneskole")
    doc.build(doc_body())
    print(f"Lagret: {PATH}")


if __name__ == "__main__":
    main()
