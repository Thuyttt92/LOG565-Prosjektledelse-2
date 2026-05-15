# Prioritert dagsplan — 6. mai 2026

Plukket opp etter en lang dag 5. mai. Siterer status: Gantt skal bygges, pakken til Bård venter på sending, og Bårds crashing-instruks står på huk.

---

## 🟥 HØY PRIORITET (gjør først)

### 1. Sjekk om Bård har sendt crashing-instruks via Teams
**Tid:** 2 min
Bare åpne Teams og se etter melding fra Bård. Hvis ja → vi har konkrete tall (aktivitet + merkostnad) som låser opp endringsdokument CR-001 og Baseline 1.

### 2. Lever pakken til Bård i Canvas
**Tid:** 5 min
Fra forrige økt — vi har enda ikke bekreftet at zip-en er lastet opp.
- Fil: `Innleveringer til Bård/Sendt til Bård/Til Bård - Nye Hædda barneskole.zip`
- Kanal: Canvas → LOG565 → Oppgaver (eller Teams direkte hvis ingen Canvas-oppgave finnes)
- Etter opplasting: send Teams-melding til Bård (mal i `00 - Oversikt/DAGSPLAN_05_MAI.md` Steg 3)

### 3. Bygg Gantt-diagrammet i MS Project
**Tid:** 30–60 min
**Verdi:** 12 sensor-poeng (det største enkeltpunktet på A-listen)
- Følg `02 - Planlegging/GANTT_BYGGE_GUIDE.pdf` fra steg 1 til 11
- Import-fil: `Arbeidsfiler/Gantt-import (Bårds simulering) - Nye Hædda barneskole.xlsx`
- Når ferdig, si til Claude: *"Gantt er bygget — Baseline 0 er satt, sluttdato XX, total kostnad YY mill kr."*

---

## 🟧 MEDIUM PRIORITET (etter at HØY er gjort)

### 4. Når Bård sender crashing-instruks (ventet samme uke)
- Åpne `03 - Gjennomføring/Endringsdokument CR-001 - Schedule crashing.docx`
- Fyll inn plassholderne med Bårds spesifikke tall:
  - WBS-aktivitet som crashes
  - Innsparing i tid (uker)
  - Merkostnad (mill kr)
  - Dato og signatur
- I MS Project: oppdater den crashede aktiviteten + sett Baseline 1
- Lagre Bårds Teams-melding som vedlegg/skjermbilde

### 5. Oppdater Komplett prosjektplan-PDF med konkrete tall
Krever at Gantt og endringsdokument er ferdig. Si til Claude og jeg gjør jobben.

### 6. Test Bård-anbefaling: at gruppen øver Gantt selv
Hvis du har tid: send GANTT_BYGGE_GUIDE.pdf til de to studiekameratene i Teams og foreslå at hver av oss bygger sin egen versjon. Læringen sitter mye bedre i praksis.

---

## 🟨 LAV PRIORITET (når alt over er på plass)

### 7. Reviewe sluttrapport-utkast
- Fil: `04 - Avslutning/Sluttrapport - Nye Hædda barneskole - UTKAST.docx`
- Pre-fylt med alt vi vet i dag (versjon 0.9). Plassholdere [PLASSHOLDER] markerer felter som krever fase 3-data.
- Kun les gjennom — ikke endre noe enda. Vi finpusser etter fase 3.

### 8. Bli kjent med EVM-arbeidsboken
- Fil: `03 - Gjennomføring/Maler/EVM-arbeidsbok-mal.xlsx`
- PDF-preview: `03 - Gjennomføring/Maler/EVM-arbeidsbok-PREVIEW.pdf`
- Den har sample-data (8 mnd, BAC 100 mill kr) som demonstrasjon. Når Baseline 1 er satt mater vi inn de virkelige tallene.

---

## 📅 Senere (ikke i morgen, men på radaren)

| Frist | Hva |
|---|---|
| 17. mai | Fase 2 låst — komplett prosjektplan sendes til Bård for godkjenning |
| 18.–26. mai | Fase 3: simulert tracking + 1-2 månedsrapporter med S-kurve og EVM |
| 27.–29. mai | Fase 4: ferdigstille sluttrapport |
| 1. juni 15:00 | INNLEVERING I WISEFLOW |

---

## Slik starter du i morgen

Si til Claude noe sånt som:

> "God morgen — jeg er tilbake. Status fra i går: [hva du har gjort av punktene over]. Hva nå?"

Da plukker Claude opp tråden, oppdaterer prosjektets memory om eventuelle fremskritt, og foreslår neste konkrete handling.

---

## Snarveier til viktige filer

| Fil | Hvor |
|---|---|
| Gantt-byggeguide (PDF, 14 sider) | `02 - Planlegging/GANTT_BYGGE_GUIDE.pdf` |
| Gantt-import-fil (klar for MS Project) | `Arbeidsfiler/Gantt-import (Bårds simulering) - Nye Hædda barneskole.xlsx` |
| Endringsdokument CR-001 (skjelett) | `03 - Gjennomføring/Endringsdokument CR-001 - Schedule crashing.docx` |
| Sluttrapport (utkast) | `04 - Avslutning/Sluttrapport - Nye Hædda barneskole - UTKAST.docx` |
| Prosjektstatus til teamet (i dag) | `Gruppe 4.5 møter/PROSJEKTSTATUS_2026-05-05.pdf` |
| MS Project baseline-strategi | `03 - Gjennomføring/MS_PROJECT_BASELINE_STRATEGI.md` |

---

*Opprettet 05.05.2026 kveld. God natt.*
