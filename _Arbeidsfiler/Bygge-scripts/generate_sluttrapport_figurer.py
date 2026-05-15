# -*- coding: utf-8 -*-
"""Genererer alle figurene som brukes i Komplett prosjektrapport.

Output: _Arbeidsfiler/sluttrapport_figurer/figur_NN_navn.png
"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
import numpy as np

from paths import ROOT, ARBEIDSFILER
from log565_master_data import (
    BAC, RISIKORESERVE, TIDSBUFFER_UKER, MÅNEDER, PAKKER, HENDELSER,
    AC_KUM, RISIKORESERVE_BRUKT_KUM, TIDSBUFFER_BRUKT_KUM_UKER,
    alle_måneder, beregn_evm,
)

OUTDIR = ARBEIDSFILER / "sluttrapport_figurer"
OUTDIR.mkdir(parents=True, exist_ok=True)

# Konsekvent fargepalett
NAVY = "#0F2A47"
PRIMARY = "#1F4E79"
ACCENT = "#4472C4"
SUCCESS = "#548235"
DANGER = "#C00000"
WARN = "#BF8F00"
MUTED = "#6B7280"


# =============================================================================
# Figur 1: S-kurve sluttvisning (PV/EV/AC kumulativt)
# =============================================================================
def figur_1_s_kurve():
    alle = alle_måneder()
    måneder_nr = [a.måned for a in alle]
    pv = [a.pv_kum for a in alle]
    ev = [a.ev_kum for a in alle]
    ac = [a.ac_kum for a in alle]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.plot(måneder_nr, pv, marker="o", linewidth=2.4, label="PV — Planlagt verdi (Baseline 1)", color=PRIMARY)
    ax.plot(måneder_nr, ev, marker="s", linewidth=2.4, label="EV — Opptjent verdi", color=SUCCESS)
    ax.plot(måneder_nr, ac, marker="^", linewidth=2.4, label="AC — Faktisk kost", color=DANGER)

    # BAC-linje
    ax.axhline(y=BAC, color=MUTED, linestyle=":", alpha=0.6, linewidth=1.2)
    ax.text(0.5, BAC + 12, f"BAC = {BAC:.0f} MNOK", fontsize=9, color=MUTED, weight="bold")

    # Markér hendelser
    hendelse_mnd = {4: ("R-05", "Forurenset masse"),
                    11: ("R-07", "Brann hos vindusprodusent"),
                    13: ("R-06 / CR-001", "DSB sprinkler/rømning")}
    for hm, (rid, htxt) in hendelse_mnd.items():
        evm_h = beregn_evm(hm)
        ax.annotate(f"{rid}\n{htxt}", xy=(hm, evm_h.ev_kum),
                    xytext=(hm + 0.3, evm_h.ev_kum + 90),
                    fontsize=8, ha="left", color=DANGER,
                    arrowprops=dict(arrowstyle="->", color=DANGER, lw=0.9))

    ax.set_xlabel("Måned i gjennomføringsfasen", fontsize=11)
    ax.set_ylabel("Kumulativ verdi (MNOK)", fontsize=11)
    ax.set_title("S-kurve — PV / EV / AC for hele prosjektforløpet (mnd 1–16)",
                 fontsize=13, fontweight="bold", color=NAVY)
    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"M{m}\n{MÅNEDER[m][0].split()[0][:3]}" for m in måneder_nr], fontsize=8)
    ax.set_ylim(0, BAC * 1.15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", framealpha=0.95, fontsize=10)
    plt.tight_layout()
    out = OUTDIR / "figur_01_s_kurve.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 2: CPI/SPI-trend per måned
# =============================================================================
def figur_2_cpi_spi_trend():
    alle = alle_måneder()
    måneder_nr = [a.måned for a in alle]
    cpi = [a.cpi for a in alle]
    spi = [a.spi for a in alle]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.plot(måneder_nr, cpi, marker="o", linewidth=2.4, label="CPI = EV/AC", color=PRIMARY)
    ax.plot(måneder_nr, spi, marker="s", linewidth=2.4, label="SPI = EV/PV", color=SUCCESS)

    # Referanselinje på 1.0
    ax.axhline(y=1.0, color=MUTED, linestyle=":", alpha=0.7, linewidth=1.2)
    ax.text(16.3, 1.0, "1.0\n(plan)", fontsize=9, color=MUTED, va="center")

    # Acceptable area mellom 0.95-1.05
    ax.axhspan(0.95, 1.05, alpha=0.1, color=SUCCESS)
    ax.text(0.5, 1.05, "Toleranseområde 0.95–1.05", fontsize=8, color=SUCCESS, va="bottom")

    # Markér hendelser
    for hm in [4, 11, 13]:
        ax.axvline(x=hm, color=DANGER, linestyle="--", alpha=0.4, linewidth=0.9)

    ax.set_xlabel("Måned", fontsize=11)
    ax.set_ylabel("Forholdstall (CPI / SPI)", fontsize=11)
    ax.set_title("CPI- og SPI-utvikling gjennom gjennomføringsfasen",
                 fontsize=13, fontweight="bold", color=NAVY)
    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"M{m}" for m in måneder_nr], fontsize=9)
    ax.set_ylim(0.85, 1.35)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", framealpha=0.95, fontsize=10)
    plt.tight_layout()
    out = OUTDIR / "figur_02_cpi_spi_trend.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 3: Kostnadsfordeling per WBS-nivå-1
# =============================================================================
def figur_3_kostnadsfordeling():
    WBS_NIVA1 = [
        ("1. Prosjektledelse", [p for p in PAKKER if p.wbs.startswith("1.")]),
        ("2. Planlegging og Prosjektering", [p for p in PAKKER if p.wbs.startswith("2.")]),
        ("3. Forberedelse og Riving", [p for p in PAKKER if p.wbs.startswith("3.")]),
        ("4. Skolebygg —\nBygningsmessige arbeider", [p for p in PAKKER if p.wbs.startswith("4.")]),
        ("5. Skolebygg —\nTekniske Anlegg", [p for p in PAKKER if p.wbs.startswith("5.")]),
        ("6. Utomhus og Uteområder", [p for p in PAKKER if p.wbs.startswith("6.")]),
        ("7. Inventar og Utstyr", [p for p in PAKKER if p.wbs.startswith("7.")]),
        ("8. Overtakelse og Avslutning", [p for p in PAKKER if p.wbs.startswith("8.")]),
    ]
    navn = [n for n, _ in WBS_NIVA1]
    bac = [sum(p.bac for p in pakker) for _, pakker in WBS_NIVA1]
    farger = ["#1F4E79", "#4472C4", "#70AD47", "#C00000", "#ED7D31", "#7030A0", "#BF8F00", "#595959"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Stolpediagram
    y_pos = np.arange(len(navn))
    ax1.barh(y_pos, bac, color=farger, edgecolor=NAVY, linewidth=0.6)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(navn, fontsize=9)
    ax1.invert_yaxis()
    ax1.set_xlabel("BAC (MNOK)", fontsize=11)
    ax1.set_title("BAC per WBS-nivå-1", fontsize=12, fontweight="bold", color=NAVY)
    for i, v in enumerate(bac):
        ax1.text(v + 5, i, f"{v:.0f}", va="center", fontsize=9)
    ax1.set_xlim(0, max(bac) * 1.15)
    ax1.grid(True, alpha=0.3, axis="x")

    # Kakediagram
    wedges, texts, autotexts = ax2.pie(bac, labels=navn, colors=farger,
                                        autopct="%1.1f%%", startangle=90,
                                        textprops={"fontsize": 8},
                                        wedgeprops={"edgecolor": "white", "linewidth": 1.5})
    for at in autotexts:
        at.set_color("white")
        at.set_fontweight("bold")
        at.set_fontsize(9)
    ax2.set_title("Andel av total BAC = 800 MNOK", fontsize=12, fontweight="bold", color=NAVY)

    plt.tight_layout()
    out = OUTDIR / "figur_03_kostnadsfordeling.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 4: Risikobudsjett-bruk over tid
# =============================================================================
def figur_4_risikobudsjett():
    måneder_nr = list(range(1, 17))
    brukt = [RISIKORESERVE_BRUKT_KUM[m] for m in måneder_nr]
    gjenværende = [RISIKORESERVE - b for b in brukt]

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.fill_between(måneder_nr, 0, brukt, color=DANGER, alpha=0.7, label="Brukt risikoreserve")
    ax.fill_between(måneder_nr, brukt, [RISIKORESERVE] * 16, color=SUCCESS, alpha=0.4, label="Gjenværende risikoreserve")

    # Markér hendelser
    for hm, label, kostnad in [(4, "R-05", 6.0), (13, "R-06 / CR-001", 5.0)]:
        ax.axvline(x=hm, color=NAVY, linestyle="--", alpha=0.6, linewidth=1.2)
        ax.annotate(f"{label}\n+{kostnad:.0f} MNOK", xy=(hm, RISIKORESERVE_BRUKT_KUM[hm]),
                    xytext=(hm + 0.3, RISIKORESERVE_BRUKT_KUM[hm] + 8),
                    fontsize=9, color=NAVY, ha="left", fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.8))

    ax.axhline(y=RISIKORESERVE, color=MUTED, linestyle=":", linewidth=1, alpha=0.7)
    ax.text(16.3, RISIKORESERVE, f"Godkjent\n{RISIKORESERVE:.0f} MNOK", fontsize=9, va="center", color=MUTED)

    ax.set_xlabel("Måned", fontsize=11)
    ax.set_ylabel("Kumulativ risikoreserve-bruk (MNOK)", fontsize=11)
    ax.set_title("Risikobudsjett — kumulativ bruk gjennom prosjektet (sluttsaldo 11 / 50 MNOK = 22 %)",
                 fontsize=12, fontweight="bold", color=NAVY)
    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"M{m}" for m in måneder_nr], fontsize=9)
    ax.set_ylim(0, RISIKORESERVE * 1.1)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", framealpha=0.95, fontsize=10)
    plt.tight_layout()
    out = OUTDIR / "figur_04_risikobudsjett.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 5: Tidsbuffer-bruk over tid
# =============================================================================
def figur_5_tidsbuffer():
    måneder_nr = list(range(1, 17))
    brukt = [TIDSBUFFER_BRUKT_KUM_UKER[m] for m in måneder_nr]

    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.fill_between(måneder_nr, 0, brukt, color=DANGER, alpha=0.7, label="Brukt tidsbuffer (uker)")
    ax.fill_between(måneder_nr, brukt, [TIDSBUFFER_UKER] * 16, color=SUCCESS, alpha=0.4,
                    label="Gjenværende tidsbuffer (uker)")

    # Hendelse mnd 11 (brann hos vindusprodusent — den ene som faktisk brukte tidsbuffer)
    ax.axvline(x=11, color=NAVY, linestyle="--", alpha=0.6, linewidth=1.2)
    ax.annotate("R-07: brann hos vindusprodusent\n+1.5 uker fra tidsbuffer",
                xy=(11, 1.5), xytext=(11.3, 4),
                fontsize=9, color=NAVY, ha="left", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.8))

    ax.axhline(y=TIDSBUFFER_UKER, color=MUTED, linestyle=":", linewidth=1, alpha=0.7)
    ax.text(16.3, TIDSBUFFER_UKER, f"Godkjent\n{TIDSBUFFER_UKER} uker", fontsize=9, va="center", color=MUTED)

    ax.set_xlabel("Måned", fontsize=11)
    ax.set_ylabel("Kumulativ tidsbuffer-bruk (uker)", fontsize=11)
    ax.set_title("Tidsbuffer — kumulativ bruk gjennom prosjektet (sluttsaldo 1,5 / 8 uker = 19 %)",
                 fontsize=12, fontweight="bold", color=NAVY)
    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"M{m}" for m in måneder_nr], fontsize=9)
    ax.set_ylim(0, TIDSBUFFER_UKER * 1.1)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", framealpha=0.95, fontsize=10)
    plt.tight_layout()
    out = OUTDIR / "figur_05_tidsbuffer.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 6: Hendelsestidslinje
# =============================================================================
def figur_6_hendelsestidslinje():
    fig, ax = plt.subplots(figsize=(12, 4.5))

    # Bakgrunns-tidslinje
    ax.axhline(y=0.5, color=PRIMARY, linewidth=4, alpha=0.5)
    måneder_nr = list(range(1, 17))
    for m in måneder_nr:
        ax.plot(m, 0.5, "o", color=PRIMARY, markersize=8)

    # Fase-skillinger
    faser = [(1, 4, "Forprosjekt", "#BDD7EE"),
             (4, 7, "Forberedelse\nog riving", "#F4B084"),
             (7, 12, "Råbygg (4.1)\n— crashet", "#FFD966"),
             (12, 16, "Innvendig +\ntekniske anlegg", "#C6E0B4"),
             (16, 17, "Overtakelse", "#D9D9D9")]
    for start, slutt, navn, farge in faser:
        ax.axvspan(start - 0.5, slutt - 0.5, alpha=0.5, color=farge)
        ax.text((start + slutt) / 2 - 0.5, 0.05, navn, ha="center", va="bottom", fontsize=9, color="#333")

    # Hendelser
    hendelser_data = [
        (4, "R-05\nForurenset masse i 3.2 Riving\n+6 MNOK risikoreserve\n+1 uke (absorbert i slack)", 1.0),
        (11, "R-07\nBrann hos vindusprodusent (4.1)\nKostnad 0\n+1,5 uker fra tidsbuffer", 1.0),
        (13, "R-06 / CR-001\nDSB-veileder sprinkler/rømning (5.1)\n+5 MNOK risikoreserve\n+1 uke", 1.0),
    ]
    for mnd, tekst, y in hendelser_data:
        ax.annotate(tekst, xy=(mnd, 0.5), xytext=(mnd, y),
                    fontsize=9, ha="center", va="bottom",
                    arrowprops=dict(arrowstyle="->", color=DANGER, lw=1.4),
                    bbox=dict(boxstyle="round,pad=0.4", facecolor="#FDE7E7",
                              edgecolor=DANGER, lw=1))

    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"M{m}\n{MÅNEDER[m][0].split()[0][:3]} {MÅNEDER[m][0].split()[1][2:]}"
                        for m in måneder_nr], fontsize=8)
    ax.set_xlim(0.3, 16.7)
    ax.set_ylim(-0.05, 1.3)
    ax.set_yticks([])
    ax.set_title("Hendelsestidslinje — gjennomføringsfasen", fontsize=13, fontweight="bold", color=NAVY)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    plt.tight_layout()
    out = OUTDIR / "figur_06_hendelsestidslinje.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 7: Baseline 0 vs Baseline 1 vs Faktisk (kost/tid-sammenligning)
# =============================================================================
def figur_7_baseline_sammenligning():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Kost-sammenligning
    scenarioer = ["Baseline 0\n(opprinnelig vedtak)", "Pre-crashing\nprognose",
                  "Baseline 1\n(etter crashing)", "Faktisk\n(sluttall)"]
    kostnader = [700, 750, 800, 800]
    farger = ["#4472C4", "#ED7D31", "#70AD47", NAVY]
    bars = ax1.bar(scenarioer, kostnader, color=farger, edgecolor="white", linewidth=2)
    for bar, val in zip(bars, kostnader):
        ax1.text(bar.get_x() + bar.get_width() / 2, val + 8, f"{val} MNOK",
                 ha="center", fontsize=10, fontweight="bold")
    ax1.set_ylabel("Totalkostnad (MNOK)", fontsize=11)
    ax1.set_title("Kostnad — Baseline 0 → 1 → Faktisk", fontsize=12, fontweight="bold", color=NAVY)
    ax1.set_ylim(0, 900)
    ax1.grid(True, alpha=0.3, axis="y")
    ax1.tick_params(axis="x", labelsize=9)

    # Tid-sammenligning
    sluttdatoer = ["15. mai 2026", "Juli 2026", "15. mai 2026", "15. mai 2026"]
    forsinkelse_uker = [0, 7, 0, 0]  # ift. opprinnelig vedtak
    bars2 = ax2.bar(scenarioer, forsinkelse_uker,
                    color=[c if u == 0 else DANGER for c, u in zip(farger, forsinkelse_uker)],
                    edgecolor="white", linewidth=2)
    for bar, val, dato in zip(bars2, forsinkelse_uker, sluttdatoer):
        if val == 0:
            ax2.text(bar.get_x() + bar.get_width() / 2, 0.3, "Innen frist",
                     ha="center", fontsize=9, fontweight="bold")
        else:
            ax2.text(bar.get_x() + bar.get_width() / 2, val + 0.2, f"+{val} uker",
                     ha="center", fontsize=10, fontweight="bold")
        ax2.text(bar.get_x() + bar.get_width() / 2, -1.4, dato,
                 ha="center", fontsize=8, style="italic", color=MUTED)
    ax2.set_ylabel("Forsinkelse mot vedtatt frist (uker)", fontsize=11)
    ax2.set_title("Tid — sluttdato vs opprinnelig frist 15. mai 2026",
                  fontsize=12, fontweight="bold", color=NAVY)
    ax2.set_ylim(-2.5, 10)
    ax2.grid(True, alpha=0.3, axis="y")
    ax2.tick_params(axis="x", labelsize=9)

    plt.tight_layout()
    out = OUTDIR / "figur_07_baseline_sammenligning.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 8: AC per måned (stolpe) med kumulativ linje
# =============================================================================
def figur_8_ac_per_maned():
    måneder_nr = list(range(1, 17))
    ac_kum = [AC_KUM[m] for m in måneder_nr]
    ac_periode = [ac_kum[0]] + [ac_kum[i] - ac_kum[i-1] for i in range(1, 16)]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    bars = ax.bar(måneder_nr, ac_periode, color=ACCENT, edgecolor=NAVY, linewidth=0.6,
                  label="Påløpt per periode (MNOK)")
    for bar, val in zip(bars, ac_periode):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 2, f"{val:.0f}",
                ha="center", fontsize=8)

    ax2 = ax.twinx()
    ax2.plot(måneder_nr, ac_kum, marker="o", color=DANGER, linewidth=2.4,
             label="Kumulativ AC (MNOK)")
    for m, val in zip(måneder_nr, ac_kum):
        if m in [4, 7, 11, 13, 16]:
            ax2.text(m, val + 25, f"{val:.0f}", ha="center", fontsize=8, color=DANGER, fontweight="bold")

    ax.set_xlabel("Måned", fontsize=11)
    ax.set_ylabel("Påløpt per periode (MNOK)", fontsize=11, color=ACCENT)
    ax2.set_ylabel("Kumulativ AC (MNOK)", fontsize=11, color=DANGER)
    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"M{m}" for m in måneder_nr], fontsize=9)
    ax.set_ylim(0, max(ac_periode) * 1.2)
    ax2.set_ylim(0, BAC * 1.1)
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_title("Kostnadsforløp — påløpt per måned og kumulativt",
                 fontsize=13, fontweight="bold", color=NAVY)
    # Felles legende
    l1, lab1 = ax.get_legend_handles_labels()
    l2, lab2 = ax2.get_legend_handles_labels()
    ax.legend(l1 + l2, lab1 + lab2, loc="upper left", framealpha=0.95)
    plt.tight_layout()
    out = OUTDIR / "figur_08_ac_per_maned.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 9: Pakke-fullføringsgrad ved utvalgte statusdatoer
# =============================================================================
def figur_9_pakke_fullforing():
    """Heatmap som viser %-fullført per pakke (y) per måned (x)."""
    from log565_master_data import hent_pct_fullført, PAKKE_BY_WBS
    måneder_nr = list(range(1, 17))
    pakker_sortert = sorted(PAKKER, key=lambda p: (int(p.wbs.split(".")[0]), int(p.wbs.split(".")[1])))
    data = np.zeros((len(pakker_sortert), 16))
    for i, p in enumerate(pakker_sortert):
        for j, m in enumerate(måneder_nr):
            data[i, j] = hent_pct_fullført(p.wbs, m)

    fig, ax = plt.subplots(figsize=(11, 9))
    im = ax.imshow(data, cmap="RdYlGn", aspect="auto", vmin=0, vmax=100)
    ax.set_xticks(np.arange(16))
    ax.set_xticklabels([f"M{m}" for m in måneder_nr], fontsize=9)
    ax.set_yticks(np.arange(len(pakker_sortert)))
    ax.set_yticklabels([f"{p.wbs} {p.navn[:30]}" for p in pakker_sortert], fontsize=8)
    ax.set_title("Fullføringsgrad (%) per arbeidspakke gjennom prosjektet",
                 fontsize=13, fontweight="bold", color=NAVY)
    cbar = plt.colorbar(im, ax=ax, shrink=0.7)
    cbar.set_label("% fullført", fontsize=10)

    # Tegn 100%-tall i grønne celler
    for i in range(len(pakker_sortert)):
        for j in range(16):
            val = data[i, j]
            if val >= 100:
                ax.text(j, i, "✓", ha="center", va="center", fontsize=10, color="white", fontweight="bold")
    plt.tight_layout()
    out = OUTDIR / "figur_09_pakke_fullforing.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


# =============================================================================
# Figur 10: Risikomatrise (sannsynlighet × konsekvens) for de 3 realiserte
# =============================================================================
def figur_10_risikomatrise():
    fig, ax = plt.subplots(figsize=(8, 7))

    # Bakgrunn — risikomatrise 5x5
    risikofarger = [
        ["#C6EFCE", "#C6EFCE", "#FFEB9C", "#FFEB9C", "#FFC7CE"],
        ["#C6EFCE", "#FFEB9C", "#FFEB9C", "#FFC7CE", "#FFC7CE"],
        ["#FFEB9C", "#FFEB9C", "#FFC7CE", "#FFC7CE", "#FF0000"],
        ["#FFEB9C", "#FFC7CE", "#FFC7CE", "#FF0000", "#FF0000"],
        ["#FFC7CE", "#FFC7CE", "#FF0000", "#FF0000", "#FF0000"],
    ]
    for i in range(5):
        for j in range(5):
            ax.add_patch(Rectangle((j, 4 - i), 1, 1, facecolor=risikofarger[i][j],
                                    edgecolor="white", linewidth=2))

    # Plasser risikoer (sannsynlighet × konsekvens)
    risikoer = [
        ("R-05", "Forurenset masse", 2, 4, "Realisert M4"),
        ("R-06 / CR-001", "DSB sprinkler", 3, 4, "Realisert M13"),
        ("R-07", "Leverandørbrann", 2, 3, "Realisert M11"),
    ]
    for rid, tittel, sann, kons, status in risikoer:
        ax.plot(sann + 0.5, kons + 0.5, "o", markersize=22, color=NAVY,
                markeredgecolor="white", markeredgewidth=2.5)
        ax.text(sann + 0.5, kons + 0.5, rid.split(" ")[0], ha="center", va="center",
                fontsize=8, color="white", fontweight="bold")
        ax.annotate(f"{tittel}\n({status})", xy=(sann + 0.5, kons + 0.5),
                    xytext=(sann + 1.3, kons + 0.7),
                    fontsize=8, color=NAVY,
                    arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7, alpha=0.5))

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_xticks(np.arange(0.5, 5.5, 1))
    ax.set_yticks(np.arange(0.5, 5.5, 1))
    ax.set_xticklabels(["1\nSvært lav", "2\nLav", "3\nMiddels", "4\nHøy", "5\nSvært høy"], fontsize=9)
    ax.set_yticklabels(["1\nSvært lav", "2\nLav", "3\nMiddels", "4\nHøy", "5\nSvært høy"], fontsize=9)
    ax.set_xlabel("Sannsynlighet (1-5)", fontsize=11)
    ax.set_ylabel("Konsekvens (1-5)", fontsize=11)
    ax.set_title("Risikomatrise — realiserte risikoer i gjennomføringsfasen",
                 fontsize=13, fontweight="bold", color=NAVY)
    ax.set_aspect("equal")
    plt.tight_layout()
    out = OUTDIR / "figur_10_risikomatrise.png"
    plt.savefig(out, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  {out.name}")


def main():
    print("Genererer figurer for Komplett prosjektrapport...")
    figur_1_s_kurve()
    figur_2_cpi_spi_trend()
    figur_3_kostnadsfordeling()
    figur_4_risikobudsjett()
    figur_5_tidsbuffer()
    figur_6_hendelsestidslinje()
    figur_7_baseline_sammenligning()
    figur_8_ac_per_maned()
    figur_9_pakke_fullforing()
    figur_10_risikomatrise()
    print("Ferdig.")


if __name__ == "__main__":
    main()
