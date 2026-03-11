# ishkarim-ui

> Interfejsy terminalowe i semantyczne: Textual TUI, retro dashboardy, visual knowledge graphs.

## Instalacja

```bash
pip install -e projects/ishkarim-ui
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-ui
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_ui as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **19 katalogów** obszaru `ui`:

- `Artlist AI voice generator`
- `Ciekawe rozwiązania projektowe`
- `HarfBuzz 12.3 i przyspieszenie renderowania tekstu`
- `Interfejsy i wizualizacja przepływów wiedzy`
- `Kolory przyjazne daltonistom dla stanów danych`
- `New experimental UI  and retro finds`
- `Nowe demo - retro UI i terminale`
- `Nowe eksperymentalne UI i retro‑wizualizacje`
- … i 11 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### Artlist AI voice generator

# WORK: Artlist AI voice generator
## 0-Metadane
- Katalog: Artlist AI voice generator
- Pliki: 13 (bez placeholderów)
- Tagi: TTS, voice-cloning, audio-pipeline, offline-AI, game-dev, NPC-dialogi, Python

### Ciekawe rozwiązania projektowe

# Ciekawe rozwiązania projektowe
## 0-Metadane
- Pliki: 10 (pliki .canvas z treścią > 120 B)
- Tagi: UI, animacje, React, CSS, design, canvas, front-end
- Status: done

### HarfBuzz 12.3 i przyspieszenie renderowania tekstu

# HarfBuzz 12.3 i przyspieszenie renderowania tekstu
## 0-Metadane
- Pliki: 9
- Tagi: `harfbuzz` `text-shaping` `benchmark` `opentype` `pango` `cairo` `regression-testing` `ci`
- Status: done


## Struktura projektu

```
ishkarim-ui/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 19 katalogów-źródeł
├── src/
│   └── ishkarim_ui/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_ui.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-ui/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
