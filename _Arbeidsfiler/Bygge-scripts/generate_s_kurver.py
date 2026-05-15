"""
Genererer S-kurver (PV/EV/AC) som PNG-bilder for hver av de 16 månedsrapportene.

For hver måned T: viser S-kurven for hele prosjektet (mnd 1-16) med en
vertikal "statuslinje" som markerer T. Fremtidige måneder (T+1 til 16) vises
som "planlagt" der vi har data, men EV/AC nullstilles etter T.
"""
from __future__ import annotations
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

sys.path.insert(0, str(Path(__file__).parent))
from log565_master_data import BAC, MÅNEDER, alle_måneder, beregn_evm

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import S_KURVER as OUTDIR
OUTDIR.mkdir(exist_ok=True)


def s_kurve_for_måned(måned: int) -> Path:
    """Generer S-kurve for månedsrapport mnd T.

    Viser PV (planlagt) for hele prosjektet, EV (faktisk fremdrift målt
    som verdi) og AC (faktisk kostnad) fra mnd 1 til T.
    """
    alle = alle_måneder()
    måneder_nr = [a.måned for a in alle]
    periode_navn = [MÅNEDER[m][0].split()[0][:3] + "\n" + MÅNEDER[m][0].split()[1] for m in måneder_nr]

    pv = [a.pv_kum for a in alle]
    ev = [a.ev_kum if a.måned <= måned else None for a in alle]
    ac = [a.ac_kum if a.måned <= måned else None for a in alle]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.plot(måneder_nr, pv, marker="o", linewidth=2, label="PV (planlagt verdi)", color="#1F4E78")
    ev_x = [m for m, v in zip(måneder_nr, ev) if v is not None]
    ev_y = [v for v in ev if v is not None]
    ac_x = [m for m, v in zip(måneder_nr, ac) if v is not None]
    ac_y = [v for v in ac if v is not None]
    ax.plot(ev_x, ev_y, marker="s", linewidth=2, label="EV (opptjent verdi)", color="#2E7D32")
    ax.plot(ac_x, ac_y, marker="^", linewidth=2, label="AC (faktisk kost)", color="#C62828")

    # Statuslinje
    ax.axvline(x=måned, color="#666666", linestyle="--", alpha=0.6, linewidth=1)
    ax.text(måned, BAC * 0.05, f" Statusdato\n mnd {måned}", fontsize=9, color="#666666",
            ha="left", va="bottom")

    # BAC-linje
    ax.axhline(y=BAC, color="#999999", linestyle=":", alpha=0.6, linewidth=1)
    ax.text(0.5, BAC + 10, f"BAC = {BAC:.0f} MNOK", fontsize=9, color="#666666")

    # Markér hendelser
    hendelse_mnd = {4: "R-05\nMiljø", 11: "R-07\nBrann", 13: "R-06\nCR-001"}
    for hm, hl in hendelse_mnd.items():
        if hm <= måned:
            evm_h = beregn_evm(hm)
            ax.annotate(hl, xy=(hm, evm_h.ev_kum), xytext=(hm, evm_h.ev_kum + 60),
                        fontsize=7, ha="center", color="#C62828",
                        arrowprops=dict(arrowstyle="->", color="#C62828", lw=0.8))

    ax.set_xlabel("Måned")
    ax.set_ylabel("Kumulativ verdi (MNOK)")
    ax.set_title(f"S-kurve — Nye Hædda Barneskole — Statusdato {MÅNEDER[måned][0]}",
                 fontsize=12, fontweight="bold")
    ax.set_xticks(måneder_nr)
    ax.set_xticklabels([f"{m}\n{MÅNEDER[m][0].split()[0][:3]}" for m in måneder_nr], fontsize=8)
    ax.set_ylim(0, BAC * 1.15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", framealpha=0.9)
    plt.tight_layout()

    out = OUTDIR / f"s_kurve_mnd_{måned:02d}.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def main():
    print("Genererer S-kurver for 16 måneder…")
    for m in range(1, 17):
        out = s_kurve_for_måned(m)
        print(f"  mnd {m:>2}: {out.name}")
    print("Ferdig.")


if __name__ == "__main__":
    main()
