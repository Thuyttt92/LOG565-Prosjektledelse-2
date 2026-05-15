# Innleveringsoversikt — LOG565: Nye Hædda barneskole

**Frist:** 1. juni 2026 kl 15:00 i WiseFlow.
**Format:** Zip-fil med alle leveranser.
**Mål:** Karakter A (≥ 90 poeng).

---

## Viktig endring 04.–05.05.2026 — alternativ simulering + crashing innebygd

**04.05** Lærer Bård har gjort om opplegget. Simuleringsappen er droppet:
- **Vi sender** WBS + Kravspesifikasjon + Risikoregister til Bård via "Oppgaver" i Canvas.
- **Bård returnerer** samme WBS-fil med tids- og kostnadsestimater per leveranse.
- Estimatene legges inn i Gantt (.mpp).
- **Etter innsending:** send personlig melding til Bård på Teams.

**05.05** Bård melder at Gantt med hans tall **bevisst overskrider rammene** for både tid og kostnad. Konkret: prosjektforslaget krever ferdigstillelse **15. mai 2026** (3 mnd buffer før skolestart august) innenfor **700 mill kr-rammen** (inkl. 50 mill risikoavsetning). Bårds simulering gir juli 2026 (~6 uker over) og ~750 mill kr (~50 mill over). Løsningen er **schedule crashing** (tid > kost). Bård sender gruppespesifikk crashing-instruks i Teams. Endringen skal dokumenteres formelt.

Dette erstatter "godkjenning fra 4 perspektiver" og data fra simuleringsportalen.

**Forberedt for crashing (klart i 03 - Gjennomføring/):**
- `Endringsdokument CR-001 - Schedule crashing.docx` — pre-fylt skjelett
- `MS_PROJECT_BASELINE_STRATEGI.md` — Baseline 0 → Baseline 1-strategi
- `Maler/problemliste-mal.xlsx` — ny mal for issue-tracking

---

## Mappestruktur (oppdatert 05.05.2026)

```
LOG565 - Prosjektledelse/
├── 00 - Oversikt/                Arbeidsdokumenter (denne filen, fremdriftsplan, dagsplan)
├── 01 - Initiering/              Prosjektforslag + Konseptløsning (vedlegg, ikke sensurert)
├── 02 - Planlegging/             FASE 2-LEVERANSER: prosjektplan-PDF, WBS-diagram,
│   │                             presedensdiagram, og senere Gantt (.mpp)
│   └── Maler og eksempler/       Maler/utkast som ikke skal leveres
├── 03 - Gjennomføring/           Fase 3: endringsdokument, baseline-strategi, månedsrapporter
│   └── Maler/                    EVM-arbeidsbok, månedsrapport-mal, problemliste-mal m.fl.
├── 04 - Avslutning/              Fase 4: sluttrapport
│   └── Maler/
├── Innleveringer til Bård/       NYTT: alt vi sender til Bård + alt vi får tilbake
│   ├── Sendt til Bård/           Følgebrev, kravspec, WBS, risiko, zip
│   └── Mottatt fra Bård/         Bårds simulerte WBS (irgesundinger_..._simulated.xlsx/pdf)
├── Arbeidsfiler/                 NYTT: interne ting som ikke leveres
│                                 Gantt-import-fil, preview-PNG osv.
├── _Foreldet (kan slettes)/      NYTT: filer erstattet av nyere versjoner — kan slettes
├── Pensum/                       Forelesningskapitler + MS Project how-to
├── Oppgavebeskrivelse/           Konkretisering + sensorveiledning (les ofte!)
└── Maler og eksempler MDV3/      Skolens eksempler (1.x og 2.x) — kun til referanse
```

---

## Statusmatrise

| # | Leveranse | Filtype | Status | Kommentar |
|---|---|---|---|---|
| **Fase 1 — Initiering (vedlegg)** | | | | |
| 1.1 | Prosjektforslag | PDF | ✅ Klar | Ligger i `01 - Initiering/` |
| 1.2 | Konseptløsning | PDF | ✅ Klar | Ligger i `01 - Initiering/` |
| **Fase 2 — Planlegging (sensureres, 40 poeng)** | | | | |
| 2.1 | Kravspesifikasjon | xlsx | ✅ Klar (59 krav, v1.1) | `Innleveringer til Bård/Sendt til Bård/` |
| 2.2 | WBS | xlsx | ✅ Klar (116 linjer, 4 nivåer) | `Innleveringer til Bård/Sendt til Bård/` |
| 2.3 | Risikoregister | xlsx | ✅ Klar (16 risikoer, 171 dager / 50 mill kr, v1.1) | `Innleveringer til Bård/Sendt til Bård/` |
| 2.4 | WBS-diagram | pptx | ✅ Klar (10 slides) | Bygget |
| 2.5 | Presedensdiagram | pptx | ✅ Klar (11 slides) | Bygget |
| 2.6 | Gantt | mpp | ⏳ Etter Bård | Trenger tids-/kostnadsestimater |
| 2.7 | Komplett prosjektplan | pdf | 🟡 Skjelett klart (14 kap) | Tall fylles inn etter Bård |
| **Fase 3 — Gjennomføring (sensureres, 35 poeng)** | | | | |
| 3.1 | Gantt med status tracking | mpp | ⏳ | Baseline 0 → Baseline 1 etter crashing — se `MS_PROJECT_BASELINE_STRATEGI.md` |
| 3.2 | Månedsrapport(er) | docx/pdf | 🟡 Mal klar (sim-refs fjernet) | KPI, S-kurve, EVM fylles fra Excel-arbeidsbok |
| 3.3 | Endringsdokument CR-001 (crashing) | docx | 🟡 Pre-fylt skjelett klart | Bårds spesifikke crashing-tall fylles inn |
| 3.4 | Problemliste | xlsx | 🟡 Mal klar | Tas i bruk når noe må logges |
| **Fase 4 — Avslutning (sensureres, 10 poeng)** | | | | |
| 4.1 | Sluttrapport | docx/pdf | ⏳ | Måloppnåelse, lærdom, refleksjon |

**Sporbarhet og profesjonalitet (15 poeng)** vurderes på tvers — ryddig dokumentdisiplin, konsistent språk, profesjonell layout.

---

## A-nivå sjekkliste (kvantitative terskler)

- [ ] Kravspesifikasjon ≥ 40 krav (mål 45+)
- [ ] WBS ≥ 60 leveranser (mål 65+)
- [ ] WBS i 4 nivåer
- [ ] Risikoregister med scoring og budsjett
- [ ] Baseline + tracking i MS Project
- [ ] Minst én månedsrapport med S-kurve + earned value
- [ ] Endringsstyring dokumentert (ved hendelser)
- [ ] Sluttrapport med refleksjon og erfaringsoverføring

---

## Sperreregler (overstyrer poengsum)

- Fase 2 må fullføres for å bestå.
- Prosjektplan må være godkjent (av Bård i ny ordning) før fase 3 starter — uten godkjenning er C taket.
- Alle 4 faser må dokumenteres for at A er oppnåelig.
- Fabrikkerte data trekker sterkt ned eller gir F.

---

*Oppdatert 05.05.2026.*
