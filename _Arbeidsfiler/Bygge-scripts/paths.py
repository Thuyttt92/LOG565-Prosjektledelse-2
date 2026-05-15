# -*- coding: utf-8 -*-
"""Sentralisert sti-konfigurasjon for alle generate_*.py-scripts.

Etter mappestruktur-migreringen ligger script i _Arbeidsfiler/Bygge-scripts/.
Alle stier er beregnet ift. prosjektroten, som er 3 nivå opp.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# Toppmapper
INITIERING = ROOT / "01 - Initiering"
PLANLEGGING = ROOT / "02 - Planlegging"
GJENNOMFORING = ROOT / "03 - Gjennomføring"
AVSLUTNING = ROOT / "04 - Avslutning"
VEDLEGG = ROOT / "Vedlegg"
ARBEIDSFILER = ROOT / "_Arbeidsfiler"

# Vedlegg-undermapper
KILDEMATERIALE = VEDLEGG / "A - Kildemateriale fra Bård"
S_KURVER = VEDLEGG / "B - S-kurver per måned"
GRUPPEMOTER = VEDLEGG / "C - Gruppemøter (statusrapporter)"
TIDLIGERE_INNLEVERINGER = VEDLEGG / "D - Tidligere innleveringer til Bård"
MALER = VEDLEGG / "E - Maler brukt som referanse"

# Gjennomforing-undermapper
ENDRINGSDOK = GJENNOMFORING / "Endringsdokumenter"
MANEDSRAPPORTER = GJENNOMFORING / "Månedsrapporter"

# Spesifikke malfiler
MAL_MANEDSRAPPORT = MALER / "månedsrapport-mal.docx"
MAL_ENDRINGSDOKUMENT = MALER / "endringsdokument_mal.docx"
MAL_SLUTTRAPPORT = MALER / "sluttrapport-mal.docx"
MAL_EVM = MALER / "EVM-arbeidsbok-mal.xlsx"
MAL_PROBLEMLISTE = MALER / "problemliste-mal.xlsx"

# Spesifikke kildefiler
PDF_GODKJENNING = KILDEMATERIALE / "godkjenning-av-budsjettendring.pdf"
PDF_MANEDSRAPPORTER = KILDEMATERIALE / "månedsrapporter.pdf"
XLSX_WBS_SIMULERT = KILDEMATERIALE / "irgesundinger_19104_752249_WBS_struktur-simulated.xlsx"
