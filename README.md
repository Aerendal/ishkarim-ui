# ishkarim-ui

> **Interfejsy terminalowe dla systemów AI — Textual TUI, retro dashboardy, visual knowledge graphs**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- TUI dashboard dla monitorowania stanu agentów
- Retro-styled UI dla narzędzi CLI — czytelne, bez zależności webowych
- Wizualizacja grafu wiedzy w terminalu (ASCII/Textual)

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-ui

# Demo (10 sekund)
python projects/ishkarim-ui/demo.py
```

## Użycie w kodzie

```python
import ishkarim_ui as m

# Wszystkie 19 katalogi wiedzy obszaru 'ui'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_ui.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Inspektor wyników wyszukiwania RAG dla dewelopera bez GUI
- Dashboard monitorowania agentów w środowisku serverowym (SSH/bastion)
- Prototypowanie interfejsu użytkownika przed inwestycją w web frontend

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 19 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_ui.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_ui_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_ui.py --quick
```

## Struktura projektu

```
ishkarim-ui/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 19 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_ui/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_ui.py         ← testy jednostkowe
│   └── test_ui_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_ui.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 19 katalogów wiedzy obszaru `ui`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
