"""
Master datastruktur for LOG565 fase 3 — Nye Hædda Barneskole.

Én sentral kilde for:
  - Baseline 1 (post-crashing): BAC per arbeidspakke + planlagt start/slutt
  - Faktisk fremdrift: %-fullført per pakke per måned, påløpt per pakke per måned
  - Hendelser: per måned, koblet til risikoregister og CR
  - EVM-beregninger: PV, EV, AC, CPI, SPI, EAC, VAC per måned

Kilder:
  - godkjenning-av-budsjettendring.pdf (NHB-2026-15 vedtak)
  - månedsrapporter.pdf (16 teamledermøtereferater fra Bård)
  - irgesundinger_19104_752249_WBS_struktur-simulated.xlsx (Bårds WBS)
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

# =============================================================================
# PROSJEKTRAMMER
# =============================================================================
BAC = 800.0  # MNOK — Baseline 1 (post-crashing, sak NHB-2026-15)
RISIKORESERVE = 50.0  # MNOK — separat fra BAC
TIDSBUFFER_UKER = 8  # ut over sluttdato før forsinkelse er reell
PROSJEKTSTART = "01.02.2025"
SLUTTDATO = "15.05.2026"
PROSJEKTLEDER_GRUPPE = "Gruppe 4.5"
SAKSNUMMER_NHB = "NHB-2026-15"

# Måned-mapping (mnd nr → (måned-navn, statusdato))
MÅNEDER = {
    1: ("Februar 2025", "28.02.2025"),
    2: ("Mars 2025", "31.03.2025"),
    3: ("April 2025", "30.04.2025"),
    4: ("Mai 2025", "31.05.2025"),
    5: ("Juni 2025", "30.06.2025"),
    6: ("Juli 2025", "31.07.2025"),
    7: ("August 2025", "31.08.2025"),
    8: ("September 2025", "30.09.2025"),
    9: ("Oktober 2025", "31.10.2025"),
    10: ("November 2025", "30.11.2025"),
    11: ("Desember 2025", "31.12.2025"),
    12: ("Januar 2026", "31.01.2026"),
    13: ("Februar 2026", "28.02.2026"),
    14: ("Mars 2026", "31.03.2026"),
    15: ("April 2026", "30.04.2026"),
    16: ("Mai 2026", "31.05.2026"),
}

# =============================================================================
# BASELINE 1 — Arbeidspakker (post-crashing)
# =============================================================================
@dataclass
class Pakke:
    """En arbeidspakke på leaf-nivå i WBS (32 totalt)."""
    wbs: str
    navn: str
    bac: float  # MNOK
    start_mnd: int  # første måned med arbeid (Baseline 1)
    slutt_mnd: int  # siste måned (Baseline 1) — pakken når 100% senest dette mnd
    fagansvar: str = ""

    @property
    def varighet(self) -> int:
        return self.slutt_mnd - self.start_mnd + 1


# Baseline 1: 4.1 Råbygg er crashet (varighet 5 mnd, BAC 240 MNOK).
# Andre pakker er som Bårds WBS-simulert (= pre-crashing baseline for de andre).
# Total BAC: 800 MNOK
PAKKER: list[Pakke] = [
    # 1. Prosjektledelse og Administrasjon (BAC 25, hele prosjektet)
    Pakke("1.1", "Prosjektstyring",                 10.0,  1, 16, "Prosjektleder"),
    Pakke("1.2", "Kontraktsoppfølging",              7.0,  1, 14, "Prosjektleder"),
    Pakke("1.3", "Interessenthåndtering",            4.0,  1, 15, "Prosjektleder"),
    Pakke("1.4", "Risiko- og Kvalitetsstyring",      4.0,  1, 15, "HMS-/KS-ansvarlig"),
    # 2. Planlegging og Prosjektering (BAC 70, mnd 1-4)
    Pakke("2.1", "Detaljprosjektering",             50.0,  1,  4, "Arkitekt"),
    Pakke("2.2", "Offentlige Godkjenninger",        12.0,  1,  3, "Arkitekt/PL"),
    Pakke("2.3", "Konkurransegrunnlag",              8.0,  1,  3, "Innkjøpsleder"),
    # 3. Forberedelse og Riving (BAC 70, mnd 4-6)
    Pakke("3.1", "Miljøsanering",                   12.0,  4,  4, "Miljørådgiver"),
    Pakke("3.2", "Riving",                          18.0,  4,  5, "Entreprenør"),
    Pakke("3.3", "Grunnarbeid",                     40.0,  5,  7, "Grunnentreprenør"),
    # 4. Skolebygg — Bygningsmessige arbeider (BAC 360 etter crashing av 4.1)
    Pakke("4.1", "Råbygg",                         240.0,  7, 11, "Totalentreprenør"),  # CRASHET: 5 mnd, 240 MNOK
    Pakke("4.2", "Innvendig Komplettering – 1. Etasje", 35.0, 12, 14, "Totalentreprenør"),
    Pakke("4.3", "Innvendig Komplettering – 2. Etasje", 35.0, 12, 14, "Totalentreprenør"),
    Pakke("4.4", "Innvendig Komplettering – 3. Etasje", 35.0, 12, 14, "Totalentreprenør"),
    Pakke("4.5", "Gymsal",                          15.0, 12, 13, "Totalentreprenør"),
    # 5. Skolebygg — Tekniske Anlegg (BAC 150)
    Pakke("5.1", "VVS",                             55.0, 12, 15, "VVS-entreprenør"),  # +1 uke pga CR-001
    Pakke("5.2", "Elektro",                         45.0, 12, 15, "Elektroentreprenør"),
    Pakke("5.3", "Heis og Vertikal Transport",      12.0, 12, 13, "Heisleverandør"),
    Pakke("5.4", "Automasjon (SD-anlegg)",          13.0, 12, 13, "Automasjonsentreprenør"),
    Pakke("5.5", "IKT og Sikkerhet",                25.0, 12, 13, "IKT-leverandør"),
    # 6. Utomhus og Uteområder (BAC 25, mnd 7-8)
    Pakke("6.1", "Lekearealer",                      7.0,  7,  8, "Landskapsentreprenør"),
    Pakke("6.2", "Sport og Fritid",                  6.0,  7,  8, "Landskapsentreprenør"),
    Pakke("6.3", "Infrastruktur",                    8.0,  7,  8, "Anleggsentreprenør"),
    Pakke("6.4", "Grøntanlegg",                      4.0,  7,  7, "Landskapsentreprenør"),
    # 7. Inventar og Utstyr (BAC 70, mnd 14-15)
    Pakke("7.1", "Løst Inventar",                   30.0, 14, 15, "Innkjøpsleder"),
    Pakke("7.2", "Spesialutstyr",                   25.0, 14, 15, "Innkjøpsleder"),
    Pakke("7.3", "AV-løsninger",                    15.0, 14, 15, "IKT-leverandør"),
    # 8. Overtakelse og Avslutning (BAC 30, mnd 15-16)
    Pakke("8.1", "Testing og Prøvedrift",           10.0, 15, 15, "Prosjektleder"),
    Pakke("8.2", "Ferdigbefaring (BP3)",             8.0, 15, 16, "Prosjektleder"),
    Pakke("8.3", "Dokumentasjon",                    5.0, 15, 16, "FDV-ansvarlig"),
    Pakke("8.4", "Brukeropplæring",                  4.0, 16, 16, "Driftssjef"),
    Pakke("8.5", "Prosjektevaluering",               3.0, 16, 16, "Prosjektleder"),
]

# Sanity check
assert abs(sum(p.bac for p in PAKKER) - BAC) < 0.01, \
    f"Sum BAC = {sum(p.bac for p in PAKKER):.1f}, forventet {BAC}"
assert len(PAKKER) == 32, f"Antall pakker = {len(PAKKER)}, forventet 32"

PAKKE_BY_WBS = {p.wbs: p for p in PAKKER}

# =============================================================================
# FAKTISK FREMDRIFT — fra månedsrapporter.pdf
# =============================================================================
# Struktur: per måned, dict av WBS → (% fullført, påløpt i perioden MNOK)
# "Øvrige aktive arbeidspakker (samlet)" angitt under nøkkel "_øvrige" som total MNOK
#
# Pakker som ikke er listet i en gitt måned: implisitt 0 fremdrift i den måneden
# (de er enten ikke startet eller allerede ferdige).

FREMDRIFT_PER_MND: dict[int, dict[str, tuple[float, float]]] = {
    1: {  # Februar 2025
        "2.1": (30, 14.8), "2.2": (36, 4.3), "2.3": (45, 3.6),
        "1.1": (6, 0.6), "1.2": (7, 0.5), "1.3": (6, 0.3), "1.4": (6, 0.2),
    },
    2: {  # Mars 2025
        "2.1": (64, 17.0), "2.2": (76, 4.9), "2.3": (97, 4.1),
        "1.1": (12, 0.7), "1.2": (15, 0.5), "1.3": (14, 0.3), "1.4": (13, 0.3),
    },
    3: {  # April 2025
        "2.1": (97, 16.5), "2.2": (100, 2.8), "2.3": (100, 0.3),
        "1.1": (19, 0.6), "1.2": (22, 0.5), "1.3": (21, 0.3), "1.4": (20, 0.3),
    },
    4: {  # Mai 2025 — Hendelse R-05 (forurenset masse, 6.0 MNOK risikoreserve)
        "3.1": (100, 12.0), "3.2": (43, 7.8), "2.1": (100, 1.6),
        "1.1": (25, 0.7), "1.2": (30, 0.5), "1.3": (28, 0.3), "1.4": (27, 0.3),
    },
    5: {  # Juni 2025
        "3.3": (29, 11.6), "3.2": (100, 10.2),
        "1.1": (32, 0.6), "1.2": (38, 0.5), "1.3": (35, 0.3), "1.4": (34, 0.3),
    },
    6: {  # Juli 2025
        "3.3": (98, 27.6),
        "1.1": (38, 0.7), "1.2": (46, 0.5), "1.3": (42, 0.3), "1.4": (41, 0.3),
    },
    7: {  # August 2025 — Råbygg crashing-perioden starter
        "4.1": (20, 47.4), "6.1": (67, 4.7), "6.2": (67, 4.0), "6.3": (50, 4.0),
        "6.4": (100, 4.0), "3.3": (100, 0.9), "1.1": (45, 0.7), "1.2": (53, 0.5),
        "_øvrige": 0.6,  # 1.3, 1.4 samlet
    },
    8: {  # September 2025
        "4.1": (39, 47.4), "6.3": (100, 4.0), "6.1": (100, 2.3), "6.2": (100, 2.0),
        "1.1": (51, 0.6), "1.2": (61, 0.5), "1.3": (57, 0.3), "1.4": (55, 0.3),
    },
    9: {  # Oktober 2025
        "4.1": (60, 48.9),
        "1.1": (58, 0.7), "1.2": (69, 0.5), "1.3": (64, 0.3), "1.4": (62, 0.3),
    },
    10: {  # November 2025
        "4.1": (80, 47.4),
        "1.1": (64, 0.6), "1.2": (76, 0.5), "1.3": (71, 0.3), "1.4": (68, 0.3),
    },
    11: {  # Desember 2025 — Hendelse R-07 (brann vindusprodusent, 1.5 uker tidsbuffer)
        "4.1": (100, 48.9),
        "1.1": (71, 0.7), "1.2": (84, 0.5), "1.3": (78, 0.3), "1.4": (76, 0.3),
        "4.2": (0, 0.0), "4.3": (0, 0.0), "4.4": (0, 0.0),
        "_øvrige": 0.0,
    },
    12: {  # Januar 2026 — start innvendig komplettering + tekniske anlegg
        "5.1": (34, 18.7), "5.2": (34, 15.3),
        "4.2": (41, 14.3), "4.3": (41, 14.3), "4.4": (41, 14.3),
        "5.5": (52, 12.9), "4.5": (69, 10.3), "5.4": (69, 9.0),
        "_øvrige": 10.0,  # 1.1, 1.2, 1.3, 1.4, 5.3, 6-pakker som drives ned, etc.
    },
    13: {  # Februar 2026 — CR-001 sprinkler godkjent (5 MNOK fra risikoreserve, 1 uke)
        "5.1": (65, 16.9), "5.2": (65, 13.8),
        "4.2": (78, 12.9), "4.3": (78, 12.9), "4.4": (78, 12.9),
        "5.5": (98, 11.7), "4.5": (100, 4.7), "5.4": (100, 4.0),
        "_øvrige": 5.3,
    },
    14: {  # Mars 2026
        "7.1": (93, 28.0), "7.2": (93, 23.3), "5.1": (99, 18.7), "5.2": (99, 15.3),
        "7.3": (93, 14.0), "4.2": (100, 7.8), "4.3": (100, 7.8), "4.4": (100, 7.8),
        "_øvrige": 1.7,
    },
    15: {  # April 2026
        "8.1": (100, 10.0), "8.2": (93, 7.5), "8.3": (93, 4.7),
        "7.1": (100, 2.0), "7.2": (100, 1.7), "7.3": (100, 1.0),
        "1.1": (96, 0.6), "5.1": (100, 0.6),
        "_øvrige": 0.7,
    },
    16: {  # Mai 2026 — siste måned
        "8.4": (100, 4.0), "8.5": (100, 3.0), "8.2": (100, 0.5),
        "1.1": (100, 0.4), "8.3": (100, 0.3),
    },
}

# =============================================================================
# HENDELSER (fra månedsrapportene)
# =============================================================================
@dataclass
class Hendelse:
    """En hendelse registrert i et månedsmøte."""
    måned: int
    risiko_id: str  # f.eks. "R-05"
    cr_id: Optional[str]  # f.eks. "CR-001", eller None hvis ikke CR
    tittel: str
    pakke_påvirket: str  # WBS-ID
    kostnad_mnok: float  # uttrekk fra risikoreserve
    tidsforskyvning_uker: float
    tidsbuffer_brukt: bool  # om tidsforskyvningen ble registrert mot tidsbufferen
    beskrivelse: str
    beslutning: str
    ansvarlig: str
    frist: str  # dato

HENDELSER: list[Hendelse] = [
    Hendelse(
        måned=4,
        risiko_id="R-05",
        cr_id=None,
        tittel="Funn av forurenset masse under 3.2 Riving",
        pakke_påvirket="3.2",
        kostnad_mnok=6.0,
        tidsforskyvning_uker=1.0,
        tidsbuffer_brukt=False,  # 1 uke absorbert i slack (kum tidsbuffer-bruk forblir 0)
        beskrivelse=(
            "Ved rivning og massehåndtering knyttet til Riving (3.2) ble det funnet en eldre, "
            "ikke-kartlagt nedgravd oljetank. Massene rundt tanken er forurenset over grenseverdi "
            "for kategori 2-deponi. Det kreves miljøsanering, separat bortkjøring og prøvetaking "
            "ved utgravingsfront."
        ),
        beslutning=(
            "Risikobudsjett-uttrekk på 6,0 MNOK godkjent for miljøsanering og deponi. Forsinkelse "
            "på ca. 1 uke absorbert i slack. Hendelsen rapporteres formelt til Statsforvalter."
        ),
        ansvarlig="Prosjektleder",
        frist="14.06.2025",
    ),
    Hendelse(
        måned=11,
        risiko_id="R-07",
        cr_id=None,
        tittel="Brann hos vindusprodusent forsinker 4.1 Råbygg",
        pakke_påvirket="4.1",
        kostnad_mnok=0.0,
        tidsforskyvning_uker=1.5,
        tidsbuffer_brukt=True,
        beskrivelse=(
            "Brann hos vindusprodusent forsinker leveranse til Råbygg (4.1) med 1,5 uke. "
            "Alternativ leverandør utredet; produksjonstid og merkostnad gjør bytte uforsvarlig."
        ),
        beslutning=(
            "Tidsbuffer reduseres med 1,5 uke. Status følges opp ukentlig. Etterfølgende "
            "innvendige arbeider planlegges om for å begrense kaskadeeffekten."
        ),
        ansvarlig="Prosjektleder",
        frist="14.01.2026",
    ),
    Hendelse(
        måned=13,
        risiko_id="R-06",
        cr_id="CR-001",
        tittel="Regulatorisk endring — DSB-veileder for sprinkler/rømning på 5.1 VVS",
        pakke_påvirket="5.1",
        kostnad_mnok=5.0,
        tidsforskyvning_uker=1.0,
        tidsbuffer_brukt=False,  # iht. referat opprettholdt kum buffer-bruk på 1,5 uker
        beskrivelse=(
            "DSB har publisert oppdatert veileder for sprinklerdekning og rømningsskilting i "
            "kommunale byggeprosjekter. Veilederen trer i kraft før prosjektets ferdigstillelse. "
            "Endringen påvirker VVS (5.1) og kan ikke ignoreres uten å risikere brukstillatelse."
        ),
        beslutning=(
            "Endringsforespørsel CR-001 godkjent. Scope justert: sprinklerdekning utvidet og "
            "rømningsskilting forsterket. Tilleggskost 5,0 MNOK fra risikoreserve, +1 uke i "
            "installasjonssekvensen, absorbert i tidsbuffer."
        ),
        ansvarlig="Prosjektleder",
        frist="14.03.2026",
    ),
]

# Kumulative tidsbuffer-tall fra referatene (kan ha mindre inkonsistens vs hendelsesregistreringer)
TIDSBUFFER_BRUKT_KUM_UKER: dict[int, float] = {
    1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0,
    11: 1.5, 12: 1.5, 13: 1.5, 14: 1.5, 15: 1.5, 16: 1.5,
}

RISIKORESERVE_BRUKT_KUM: dict[int, float] = {
    1: 0.0, 2: 0.0, 3: 0.0, 4: 6.0, 5: 6.0, 6: 6.0, 7: 6.0, 8: 6.0, 9: 6.0, 10: 6.0,
    11: 6.0, 12: 6.0, 13: 11.0, 14: 11.0, 15: 11.0, 16: 11.0,
}

# Kumulativ direkte aktivitetskost (innenfor BAC), fra referatene
AC_KUM: dict[int, float] = {
    1: 24.2, 2: 52.1, 3: 73.4, 4: 96.6, 5: 120.1, 6: 149.4,
    7: 216.1, 8: 273.6, 9: 324.3, 10: 373.4, 11: 424.1,
    12: 543.3, 13: 638.4, 14: 763.0, 15: 791.8, 16: 800.0,
}


# =============================================================================
# %-FULLFØRT PER PAKKE PER MÅNED — interpolert der referater er ufullstendige
# =============================================================================
def hent_pct_fullført(wbs: str, måned: int) -> float:
    """Returnerer % fullført for en pakke ved slutten av gitt måned.

    Strategi:
      1. Før pakkens start_mnd → 0%
      2. Etter pakkens slutt_mnd → 100% (planlagt fullført)
      3. Hvis eksakt datapunkt finnes → bruk det
      4. Hvis 100% er registrert et tidligere mnd → 100%
      5. Ellers lineær interpolasjon mellom nærmeste kjente datapunkter,
         med 0% ved start_mnd-1 og 100% ved slutt_mnd som anker.
    """
    p = PAKKE_BY_WBS[wbs]

    # 1. Før pakken er startet
    if måned < p.start_mnd:
        return 0.0
    # 2. Etter pakkens planlagte slutt
    if måned > p.slutt_mnd:
        return 100.0

    # 3. Direkte oppslag
    data = FREMDRIFT_PER_MND.get(måned, {}).get(wbs)
    if data is not None:
        return float(data[0])

    # 4. Hvis pakken er rapportert 100% i et tidligere måned, returnér 100%
    for m in range(p.start_mnd, måned):
        d = FREMDRIFT_PER_MND.get(m, {}).get(wbs)
        if d is not None and d[0] >= 100:
            return 100.0

    # 5. Lineær interpolasjon mellom kjente datapunkter, med 0%@(start-1)
    #    og 100%@(slutt) som ytre anker.
    forrige_mnd, forrige_pct = p.start_mnd - 1, 0.0
    for m in range(måned - 1, p.start_mnd - 2, -1):
        d = FREMDRIFT_PER_MND.get(m, {}).get(wbs)
        if d is not None:
            forrige_mnd, forrige_pct = m, d[0]
            break
    neste_mnd, neste_pct = p.slutt_mnd, 100.0
    for m in range(måned + 1, p.slutt_mnd + 1):
        d = FREMDRIFT_PER_MND.get(m, {}).get(wbs)
        if d is not None:
            neste_mnd, neste_pct = m, d[0]
            break

    if neste_mnd <= forrige_mnd:
        return min(100.0, max(0.0, forrige_pct))
    frac = (måned - forrige_mnd) / (neste_mnd - forrige_mnd)
    return min(100.0, max(0.0, forrige_pct + frac * (neste_pct - forrige_pct)))


# =============================================================================
# EVM-BEREGNING
# =============================================================================
@dataclass
class EVMMåned:
    """Earned Value Management metrics for en gitt måned."""
    måned: int
    måned_navn: str
    statusdato: str
    pv_kum: float  # MNOK — Planned Value
    ev_kum: float  # MNOK — Earned Value
    ac_kum: float  # MNOK — Actual Cost (innen BAC)
    cpi: float
    spi: float
    eac: float  # Estimate at Completion = BAC/CPI
    etc: float  # Estimate to Complete = EAC - AC
    vac: float  # Variance at Completion = BAC - EAC
    pct_complete: float  # EV/BAC × 100
    risikoreserve_brukt_kum: float
    risikoreserve_brukt_uker_kum: float  # = tidsbuffer brukt
    status_rag: str  # Rød/Gul/Grønn


def beregn_pv(måned: int) -> float:
    """Planned Value kumulativt ved slutten av gitt måned (Baseline 1, lineær).

    For hver pakke P: PV_P(T) = BAC_P × min((T-start+1)/varighet, 1) for T>=start.
    """
    pv = 0.0
    for p in PAKKER:
        if måned < p.start_mnd:
            continue
        if måned >= p.slutt_mnd:
            pv += p.bac
        else:
            pv += p.bac * (måned - p.start_mnd + 1) / p.varighet
    return pv


def beregn_ev(måned: int) -> float:
    """Earned Value kumulativt: Σ (BAC_pakke × %fullført_pakke / 100)."""
    ev = 0.0
    for p in PAKKER:
        pct = hent_pct_fullført(p.wbs, måned)
        ev += p.bac * pct / 100.0
    return ev


def beregn_evm(måned: int) -> EVMMåned:
    """Beregn alle EVM-metrikker for en gitt måned."""
    pv = beregn_pv(måned)
    ev = beregn_ev(måned)
    ac = AC_KUM[måned]
    cpi = ev / ac if ac > 0 else 0.0
    spi = ev / pv if pv > 0 else 0.0
    eac = BAC / cpi if cpi > 0 else BAC
    etc = eac - ac
    vac = BAC - eac
    pct = (ev / BAC) * 100
    rr = RISIKORESERVE_BRUKT_KUM[måned]
    tb = TIDSBUFFER_BRUKT_KUM_UKER[måned]

    if spi >= 0.95 and cpi >= 0.95:
        rag = "Grønn"
    elif spi >= 0.85 and cpi >= 0.85:
        rag = "Gul"
    else:
        rag = "Rød"

    navn, statusdato = MÅNEDER[måned]
    return EVMMåned(
        måned=måned, måned_navn=navn, statusdato=statusdato,
        pv_kum=pv, ev_kum=ev, ac_kum=ac, cpi=cpi, spi=spi,
        eac=eac, etc=etc, vac=vac, pct_complete=pct,
        risikoreserve_brukt_kum=rr, risikoreserve_brukt_uker_kum=tb,
        status_rag=rag,
    )


def alle_måneder() -> list[EVMMåned]:
    return [beregn_evm(m) for m in range(1, 17)]


# =============================================================================
# QA / SANITY
# =============================================================================
if __name__ == "__main__":
    print(f"Total BAC: {sum(p.bac for p in PAKKER):.1f} MNOK ({len(PAKKER)} pakker)")
    print()
    print(f"{'Mnd':>3} {'Navn':<16} {'PV':>7} {'EV':>7} {'AC':>7} {'CPI':>6} {'SPI':>6} {'%':>5} {'RR':>5} {'TB':>5} RAG")
    print("-" * 80)
    for evm in alle_måneder():
        print(f"{evm.måned:>3} {evm.måned_navn:<16} {evm.pv_kum:>7.1f} {evm.ev_kum:>7.1f} "
              f"{evm.ac_kum:>7.1f} {evm.cpi:>6.3f} {evm.spi:>6.3f} {evm.pct_complete:>5.1f} "
              f"{evm.risikoreserve_brukt_kum:>5.1f} {evm.risikoreserve_brukt_uker_kum:>5.1f} {evm.status_rag}")
    print()
    print(f"Hendelser: {len(HENDELSER)} (R-05 mnd 4, R-07 mnd 11, R-06/CR-001 mnd 13)")
