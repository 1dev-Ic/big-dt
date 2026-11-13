# BigDT — ASCHMA SSHIA Data Tool

BigDT is a mobile data collection and reporting application developed in 2023 for the Adamawa State Contributory Health Management Agency (ASCHMA). It supported monthly health facility reporting by Monitoring and Evaluation (M&E) Officers across Adamawa State’s 21 Local Government Areas (LGAs).

The tool was designed to help officers record facility-level information, review submitted records, and compile LGA summaries for reporting to ASCHMA. It covers reporting from primary health centres (PHCs) and secondary health centres (SHCs), including enrolment, capitation and claims, service utilisation, referrals, and mortality indicators.

## Project history

BigDT was used by the 21 LGA M&E Officers from 2023 through 2025. The programme ended in 2025 after funding became unavailable. This repository preserves the application source and build configuration for reference and future maintenance.

## Features in the application

- Capture monthly PHC and SHC facility reports.
- Record health facility and LGA reporting information.
- Review saved facility records in tabular views.
- Summarise submitted data across PHC and SHC reporting areas for an LGA.
- Store records in a local SQLite database.
- Android packaging configuration using Buildozer.

## Technology

- Python
- Kivy and KivyMD
- SQLite
- Buildozer / python-for-android configuration

## Repository contents

- `main.py` — application screens, data entry, local storage, and summary logic.
- `helpers.py` — interface layouts and helper definitions.
- `buildozer.spec` — mobile application packaging configuration.
- `ASCHMA/` — application data and database directory structure.
- `img/` — application branding assets.

## Build notes

The repository includes a Buildozer specification targeting Android. Android builds generally require Buildozer and its Android SDK/NDK toolchain on a supported build environment. From the project directory, a configured Buildozer environment can build a debug APK with:

```bash
buildozer android debug
```

The source targets Kivy 2.1.0 and includes KivyMD, Pillow, and SQLite-related requirements in `buildozer.spec`. Toolchain versions and dependencies may need updating to build successfully on a current system.

## Operational status and maintenance

The 2023–2025 field deployment has ended. The checked-in source currently presents PDF export, Excel export, and server submission as unfinished actions. Those capabilities or the original operational workflow may need to be restored and validated before reuse. Review the code, data handling, and build configuration before deploying a maintained version.

## Acknowledgement

Developed for the Adamawa State Contributory Health Management Agency (ASCHMA) to support LGA-level health facility monitoring and reporting.
