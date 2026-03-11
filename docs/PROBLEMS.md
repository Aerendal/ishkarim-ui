# PROBLEMS — ishkarim-ui

> Interfejsy terminalowe dla systemów AI — Textual TUI, retro dashboardy, visual knowledge graphs

## ✅ Co ten projekt rozwiązuje

- ✅ TUI dashboard dla monitorowania stanu agentów **w terminalu bez przeglądarki**
- ✅ Retro-styled UI dla narzędzi CLI — czytelne, bez zależności webowych
- ✅ Wizualizacja grafu wiedzy w terminalu (ASCII/Textual)
- ✅ Interaktywna inspekcja chunków RAG, offsetów FTS5, śladów JSONL
- ✅ Cross-platform (Linux/Mac/Windows) bez Electron/Chromium

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Webowe GUI — to czyste TUI, terminal only
- ❌ Wykresy statystyczne złożone — bardzo ograniczone możliwości w terminalu
- ❌ Multi-user concurrent access do dashboardu
- ❌ Mobile/touch interfaces

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **Textual 7.x** ma breaking API changes względem 0.x — migracja ręczna
- ⚠️ **Renderowanie emoji/unicode** zależy od konfiguracji terminala i czcionki
- ⚠️ **Wydajność** przy >10k nodes w ASCII graph znacznie spada
- ⚠️ **Brak accessibility** — screen readery w TUI są niestandardowe

---

## 🎯 Przypadki użycia

- 🎯 Inspektor wyników wyszukiwania RAG dla dewelopera bez GUI
- 🎯 Dashboard monitorowania agentów w środowisku serverowym (SSH/bastion)
- 🎯 Prototypowanie interfejsu użytkownika przed inwestycją w web frontend
- 🎯 Narzędzie diagnostyczne dla klientów bez dostępu do przeglądarki

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
