# -*- coding: utf-8 -*-
"""Engangsskript: oppdaterer paths i alle generate_*.py etter migrering.

Erstatter den gamle inline-ROOT-definisjonen med 'from paths import ...'.
"""
from pathlib import Path
import re

HER = Path(__file__).resolve().parent

# (filnavn, gammel blokk, ny blokk)
oppdateringer = [
    ("generate_endringsdokumenter.py",
     'ROOT = Path(__file__).resolve().parent.parent\nMAL = ROOT / "03 - Gjennomføring" / "Maler" / "endringsdokument_mal.docx"\nOUTDIR = ROOT / "03 - Gjennomføring"',
     'import sys\nsys.path.insert(0, str(Path(__file__).resolve().parent))\nfrom paths import ROOT, MAL_ENDRINGSDOKUMENT as MAL, ENDRINGSDOK as OUTDIR\nOUTDIR.mkdir(exist_ok=True)'),

    ("generate_manedsrapport.py",
     'ROOT = Path(__file__).resolve().parent.parent\nMAL = ROOT / "03 - Gjennomføring" / "Maler" / "månedsrapport-mal.docx"\nOUTDIR = ROOT / "03 - Gjennomføring" / "Månedsrapporter"\nOUTDIR.mkdir(exist_ok=True)\nS_KURVER = ROOT / "Arbeidsfiler" / "s_kurver"',
     'sys.path.insert(0, str(Path(__file__).resolve().parent))\nfrom paths import ROOT, MAL_MANEDSRAPPORT as MAL, MANEDSRAPPORTER as OUTDIR, S_KURVER\nOUTDIR.mkdir(exist_ok=True)'),

    ("generate_evm_arbeidsbok.py",
     'ROOT = Path(__file__).resolve().parent.parent\nOUT = ROOT / "03 - Gjennomføring" / "EVM-arbeidsbok - Nye Hædda barneskole.xlsx"',
     'sys.path.insert(0, str(Path(__file__).resolve().parent))\nfrom paths import ROOT, GJENNOMFORING\nOUT = GJENNOMFORING / "EVM-arbeidsbok - Nye Hædda barneskole.xlsx"'),

    ("generate_s_kurver.py",
     'ROOT = Path(__file__).resolve().parent.parent\nOUTDIR = ROOT / "Arbeidsfiler" / "s_kurver"\nOUTDIR.mkdir(exist_ok=True)',
     'sys.path.insert(0, str(Path(__file__).resolve().parent))\nfrom paths import S_KURVER as OUTDIR\nOUTDIR.mkdir(exist_ok=True)'),

    ("generate_msproject_instruks.py",
     'ROOT = Path(__file__).resolve().parent.parent\nOUT = ROOT / "03 - Gjennomføring" / "MS Project tracking-instruks.xlsx"',
     'sys.path.insert(0, str(Path(__file__).resolve().parent))\nfrom paths import GJENNOMFORING\nOUT = GJENNOMFORING / "MS Project tracking-instruks.xlsx"'),

    ("generate_sluttrapport.py",
     'ROOT = Path(__file__).resolve().parent.parent\nUTKAST = ROOT / "04 - Avslutning" / "Sluttrapport - Nye Hædda barneskole - UTKAST.docx"\nOUT = ROOT / "04 - Avslutning" / "Sluttrapport - Nye Hædda barneskole.docx"',
     'sys.path.insert(0, str(Path(__file__).resolve().parent))\nfrom paths import AVSLUTNING, MAL_SLUTTRAPPORT\n# UTKAST-versjonen er slettet etter migrering. Bruker sluttrapport-mal hvis regenerering.\nUTKAST = MAL_SLUTTRAPPORT\nOUT = AVSLUTNING / "Sluttrapport - Nye Hædda barneskole.docx"'),
]


def main():
    for filnavn, gammel, ny in oppdateringer:
        fil = HER / filnavn
        if not fil.exists():
            print(f"  MANGLER: {filnavn}")
            continue
        innhold = fil.read_text(encoding="utf-8")
        if gammel in innhold:
            innhold = innhold.replace(gammel, ny)
            fil.write_text(innhold, encoding="utf-8")
            print(f"  OPPDATERT: {filnavn}")
        elif "from paths import" in innhold:
            print(f"  Allerede oppdatert: {filnavn}")
        else:
            print(f"  IKKE FUNNET match i: {filnavn}")


if __name__ == "__main__":
    main()
