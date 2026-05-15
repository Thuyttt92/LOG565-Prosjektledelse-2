# -*- coding: utf-8 -*-
"""
Migrerer mappestrukturen til en A-oppgave leveringsverdig form.

Strategi:
  - Numererte fasemapper (00-04) inneholder kun leveranser
  - Vedlegg/ samler støttemateriale med tydelige A/B/C/D/E-prefiks
  - _Arbeidsfiler/ samler intern bygging/script + referansemateriale
  - Sletter overflødige utkast og duplikater (etter brukerbekreftelse)

Hver operasjon logges. Kjør én gang fra prosjektroten:
    python .build_scripts/migrate_mappestruktur.py
"""
from __future__ import annotations
import shutil
import sys
import io
from pathlib import Path

# UTF-8 stdout for Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

# =============================================================================
# Operasjonslogger
# =============================================================================
operasjoner: list[tuple[str, str]] = []  # (handling, sti)


def mkdir(rel: str) -> Path:
    p = ROOT / rel
    p.mkdir(parents=True, exist_ok=True)
    operasjoner.append(("mkdir", rel))
    return p


def move(src_rel: str, dst_rel: str) -> None:
    """Flytt fil eller mappe. dst_rel kan være målmappe eller målfil."""
    src = ROOT / src_rel
    dst = ROOT / dst_rel
    if not src.exists():
        operasjoner.append(("skipped (mangler)", src_rel))
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and dst.is_dir():
        dst = dst / src.name
    try:
        shutil.move(str(src), str(dst))
        operasjoner.append(("move", f"{src_rel}  →  {dst.relative_to(ROOT)}"))
    except PermissionError as e:
        operasjoner.append(("FAILED (fil i bruk?)", f"{src_rel}  ← {e.strerror}"))
        print(f"  !! ADVARSEL: {src_rel} kunne ikke flyttes (sannsynligvis åpen i en app)")


def delete(rel: str) -> None:
    p = ROOT / rel
    if not p.exists():
        operasjoner.append(("skipped (mangler)", rel))
        return
    try:
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
        operasjoner.append(("delete", rel))
    except PermissionError as e:
        operasjoner.append(("FAILED (fil i bruk?)", f"{rel}  ← {e.strerror}"))
        print(f"  !! ADVARSEL: {rel} kunne ikke slettes (sannsynligvis åpen i en app)")


def rmdir_if_empty(rel: str) -> None:
    p = ROOT / rel
    if not p.exists():
        return
    try:
        p.rmdir()
        operasjoner.append(("rmdir", rel))
    except OSError:
        operasjoner.append(("kept (ikke tom)", rel))


# =============================================================================
# Steg 1: Opprett ny mappestruktur
# =============================================================================
def steg_1_opprett_mapper():
    print("=== STEG 1: Oppretter ny mappestruktur ===")
    # Behold 00 - Oversikt? Den inneholder DAGSPLAN, FREMDRIFTSPLAN etc. — flyttes til _Arbeidsfiler
    mkdir("Vedlegg")
    mkdir("Vedlegg/A - Kildemateriale fra Bård")
    mkdir("Vedlegg/B - S-kurver per måned")
    mkdir("Vedlegg/C - Gruppemøter (statusrapporter)")
    mkdir("Vedlegg/D - Tidligere innleveringer til Bård")
    mkdir("Vedlegg/E - Maler brukt som referanse")
    mkdir("_Arbeidsfiler")
    mkdir("_Arbeidsfiler/Bygge-scripts")
    mkdir("_Arbeidsfiler/Bygge-scripts/s_kurver")  # for arbeidsmappe — symlink ikke nødvendig
    mkdir("_Arbeidsfiler/Skjermbilder underveis")
    mkdir("_Arbeidsfiler/Referansemateriale (ikke leveranse)")
    mkdir("_Arbeidsfiler/Planleggingsnotater")
    mkdir("03 - Gjennomføring/Endringsdokumenter")


# =============================================================================
# Steg 2: Slett gamle utkast og overflødige filer
# =============================================================================
def steg_2_slett():
    print("=== STEG 2: Sletter utkast og overflødige filer ===")
    # Sluttrapport-utkast (vi har ferdig versjon)
    delete("04 - Avslutning/Sluttrapport - Nye Hædda barneskole - UTKAST.docx")
    # Gamle utkast i planlegging
    delete("02 - Planlegging/Maler og eksempler/Kravspesifikasjon Hedda skole - eldre utkast.xlsx")
    delete("02 - Planlegging/Maler og eksempler/WBS_struktur - tidlig utkast.md")
    # Backup-fil av Gantt-guide
    delete("02 - Planlegging/GANTT_BYGGE_GUIDE_ENG.md.bak")
    # Den engelske guide-versjonen er overflødig (vi har norsk)
    delete("02 - Planlegging/GANTT_BYGGE_GUIDE.md")
    delete("02 - Planlegging/GANTT_BYGGE_GUIDE.pdf")
    # EVM-arbeidsbok PREVIEW (vi har den ferdige)
    delete("03 - Gjennomføring/Maler/EVM-arbeidsbok-PREVIEW.pdf")
    # Strateginotat (intern arbeidsfil)
    delete("03 - Gjennomføring/MS_PROJECT_BASELINE_STRATEGI.md")
    # Sample-PDF for mnd 13 i Arbeidsfiler (vi har den i Månedsrapporter)
    delete("Arbeidsfiler/Månedsrapport mnd 13 - Februar 2026.pdf")


# =============================================================================
# Steg 3: Flytt MS Project-fil og MS Project-relaterte filer
# =============================================================================
def steg_3_msproject():
    print("=== STEG 3: MS Project filer ===")
    # Hædda barneskole GANTT.mpp → 02 - Planlegging
    move("Hædda barneskole GANTT.mpp",
         "02 - Planlegging/MS Project - Plan (Baseline 0).mpp")


# =============================================================================
# Steg 4: Flytt screenshots og bilder fra root
# =============================================================================
def steg_4_skjermbilder():
    print("=== STEG 4: Skjermbilder og bilder ===")
    move("nytt gantt statistikk bilde.jpg",
         "_Arbeidsfiler/Skjermbilder underveis/")
    move("Skjermbilde 2026-05-15 131015.jpg",
         "_Arbeidsfiler/Skjermbilder underveis/")
    move("Skjermbilde 2026-05-15 131257.jpg",
         "_Arbeidsfiler/Skjermbilder underveis/")
    move("Skjermbilde 2026-05-15 131333.jpg",
         "_Arbeidsfiler/Skjermbilder underveis/")
    # Gantt PREVIEW-bilde (intern)
    move("Arbeidsfiler/Gantt - Baseline 0 - PREVIEW.png",
         "_Arbeidsfiler/Skjermbilder underveis/")


# =============================================================================
# Steg 5: Endringsdokumenter inn i egen undermappe
# =============================================================================
def steg_5_endringsdokumenter():
    print("=== STEG 5: Endringsdokumenter → undermappe ===")
    move("03 - Gjennomføring/Endringsdokument NHB-IRGESUND - Schedule crashing.docx",
         "03 - Gjennomføring/Endringsdokumenter/")
    move("03 - Gjennomføring/Endringsdokument CR-001 - Sprinkler-romning.docx",
         "03 - Gjennomføring/Endringsdokumenter/")


# =============================================================================
# Steg 6: Vedlegg-strukturen
# =============================================================================
def steg_6_vedlegg():
    print("=== STEG 6: Vedlegg/ ===")
    # A — Kildemateriale fra Bård (var i Innleveringer til Bård/Mottatt fra Bård/)
    move("Innleveringer til Bård/Mottatt fra Bård/godkjenning-av-budsjettendring.pdf",
         "Vedlegg/A - Kildemateriale fra Bård/")
    move("Innleveringer til Bård/Mottatt fra Bård/månedsrapporter.pdf",
         "Vedlegg/A - Kildemateriale fra Bård/")
    move("Innleveringer til Bård/Mottatt fra Bård/irgesundinger_19104_752249_WBS_struktur-simulated.pdf",
         "Vedlegg/A - Kildemateriale fra Bård/")
    move("Innleveringer til Bård/Mottatt fra Bård/irgesundinger_19104_752249_WBS_struktur-simulated.xlsx",
         "Vedlegg/A - Kildemateriale fra Bård/")

    # B — S-kurver
    for m in range(1, 17):
        move(f"Arbeidsfiler/s_kurver/s_kurve_mnd_{m:02d}.png",
             "Vedlegg/B - S-kurver per måned/")

    # C — Gruppemøter
    move("Gruppe 4.5 møter/PROSJEKTSTATUS_2026-05-04.pdf",
         "Vedlegg/C - Gruppemøter (statusrapporter)/")
    move("Gruppe 4.5 møter/PROSJEKTSTATUS_2026-05-05.pdf",
         "Vedlegg/C - Gruppemøter (statusrapporter)/")
    move("Gruppe 4.5 møter/PROSJEKTSTATUS_2026-05-15.pdf",
         "Vedlegg/C - Gruppemøter (statusrapporter)/")

    # D — Tidligere innleveringer til Bård
    move("Innleveringer til Bård/Sendt til Bård/Følgebrev til Bård.md",
         "Vedlegg/D - Tidligere innleveringer til Bård/")
    move("Innleveringer til Bård/Sendt til Bård/Kravspesifikasjon - Nye Hædda barneskole.xlsx",
         "Vedlegg/D - Tidligere innleveringer til Bård/")
    move("Innleveringer til Bård/Sendt til Bård/Risikoregister - Nye Hædda barneskole.xlsx",
         "Vedlegg/D - Tidligere innleveringer til Bård/")
    move("Innleveringer til Bård/Sendt til Bård/Til Bård - Nye Hædda barneskole.zip",
         "Vedlegg/D - Tidligere innleveringer til Bård/")
    move("Innleveringer til Bård/Sendt til Bård/WBS - Nye Hædda barneskole.xlsx",
         "Vedlegg/D - Tidligere innleveringer til Bård/")
    # Gantt-import xlsx (intern arbeidsfil) — flytt til _Arbeidsfiler
    move("Arbeidsfiler/Gantt-import (Bårds simulering) - Nye Hædda barneskole.xlsx",
         "_Arbeidsfiler/Planleggingsnotater/")

    # E — Maler brukt som referanse (samle fra alle Maler-mappene)
    move("02 - Planlegging/Maler og eksempler/gantt-plan-eksempel.mpp",
         "Vedlegg/E - Maler brukt som referanse/")
    move("02 - Planlegging/Maler og eksempler/Kravspesifikasjon-mal.xlsx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("02 - Planlegging/Maler og eksempler/Presedensdiagram_eksempel.pptx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("02 - Planlegging/Maler og eksempler/prosjektplan-mal.docx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("02 - Planlegging/Maler og eksempler/WBS-mal.xlsx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("02 - Planlegging/Maler og eksempler/WBSdiagram_eksempel.pptx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("03 - Gjennomføring/Maler/endringsdokument_mal.docx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("03 - Gjennomføring/Maler/EVM-arbeidsbok-mal.xlsx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("03 - Gjennomføring/Maler/gantt-tracking-mal.mpp",
         "Vedlegg/E - Maler brukt som referanse/")
    move("03 - Gjennomføring/Maler/månedsrapport-mal.docx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("03 - Gjennomføring/Maler/problemliste-mal.xlsx",
         "Vedlegg/E - Maler brukt som referanse/")
    move("04 - Avslutning/Maler/sluttrapport-mal.docx",
         "Vedlegg/E - Maler brukt som referanse/")


# =============================================================================
# Steg 7: _Arbeidsfiler — bygge-scripts og referansemateriale
# =============================================================================
def steg_7_arbeidsfiler():
    print("=== STEG 7: _Arbeidsfiler/ ===")
    # Bygge-scripts: alt i .build_scripts/ + Arbeidsfiler/*.py
    for f in [".build_scripts/_pdf_helpers.py",
              ".build_scripts/_status_style.py",
              ".build_scripts/build_gantt_manuell.py",
              ".build_scripts/build_huskeliste.py",
              ".build_scripts/build_kravspec.py",
              ".build_scripts/build_msproject_import.py",
              ".build_scripts/build_presedens.py",
              ".build_scripts/build_prosjektplan_pdf.py",
              ".build_scripts/build_prosjektstatus_20260504.py",
              ".build_scripts/build_prosjektstatus_20260505.py",
              ".build_scripts/build_prosjektstatus_20260515.py",
              ".build_scripts/build_prosjektstatus_20260515_kveld.py",
              ".build_scripts/build_risk.py",
              ".build_scripts/build_team_oppsummering.py",
              ".build_scripts/build_wbs.py",
              ".build_scripts/build_wbs_diagram.py"]:
        move(f, "_Arbeidsfiler/Bygge-scripts/")
    # generate-scripts fra Arbeidsfiler/
    for f in ["Arbeidsfiler/generate_endringsdokumenter.py",
              "Arbeidsfiler/generate_evm_arbeidsbok.py",
              "Arbeidsfiler/generate_manedsrapport.py",
              "Arbeidsfiler/generate_msproject_instruks.py",
              "Arbeidsfiler/generate_s_kurver.py",
              "Arbeidsfiler/generate_sluttrapport.py",
              "Arbeidsfiler/log565_master_data.py"]:
        move(f, "_Arbeidsfiler/Bygge-scripts/")

    # Planleggingsnotater (00 - Oversikt)
    move("00 - Oversikt/DAGSPLAN_05_MAI.md",
         "_Arbeidsfiler/Planleggingsnotater/")
    move("00 - Oversikt/FREMDRIFTSPLAN_LOG565.md",
         "_Arbeidsfiler/Planleggingsnotater/")
    move("00 - Oversikt/INNLEVERINGSOVERSIKT.md",
         "_Arbeidsfiler/Planleggingsnotater/")
    move("00 - Oversikt/PRIO_06_MAI.md",
         "_Arbeidsfiler/Planleggingsnotater/")

    # Referansemateriale: Pensum + MDV3-maler
    for fil in ["Pensum/How_To_Plan_Your_Project_With_Microsoft_Office.pdf",
                "Pensum/Kap_1_og_2_Hva_er_praktisk_prosjektledelse.pptx",
                "Pensum/Kap_3_og_5_Forprosjekt_og_prosjektmandat.pptx",
                "Pensum/Kap_4_Prosjektmodeller.pptx"]:
        move(fil, "_Arbeidsfiler/Referansemateriale (ikke leveranse)/")

    # MDV3-maler — flytt hele mappa
    move("Maler og eksempler MDV3",
         "_Arbeidsfiler/Referansemateriale (ikke leveranse)/")


# =============================================================================
# Steg 8: Fjern tomme mapper
# =============================================================================
def steg_8_rydd_tomme():
    print("=== STEG 8: Fjern tomme mapper ===")
    tomme_kandidater = [
        "00 - Oversikt",
        "02 - Planlegging/Maler og eksempler",
        "03 - Gjennomføring/Maler",
        "04 - Avslutning/Maler",
        "Arbeidsfiler/s_kurver",
        "Arbeidsfiler/__pycache__",
        "Arbeidsfiler",
        "Gruppe 4.5 møter",
        "Innleveringer til Bård/Sendt til Bård",
        "Innleveringer til Bård/Mottatt fra Bård",
        "Innleveringer til Bård",
        "Pensum",
        ".build_scripts/__pycache__",
        ".build_scripts",
    ]
    for r in tomme_kandidater:
        rmdir_if_empty(r)


def hovedkjøring():
    steg_1_opprett_mapper()
    steg_2_slett()
    steg_3_msproject()
    steg_4_skjermbilder()
    steg_5_endringsdokumenter()
    steg_6_vedlegg()
    steg_7_arbeidsfiler()
    steg_8_rydd_tomme()

    print()
    print("=" * 60)
    print(f"FERDIG — {len(operasjoner)} operasjoner")
    print("=" * 60)
    # Tell per type
    from collections import Counter
    typer = Counter(op[0] for op in operasjoner)
    for t, n in sorted(typer.items()):
        print(f"  {t}: {n}")


if __name__ == "__main__":
    hovedkjøring()
