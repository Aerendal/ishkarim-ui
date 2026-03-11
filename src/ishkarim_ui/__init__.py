"""
ishkarim_ui — moduł z obszaru ui.

Interfejsy terminalowe i semantyczne: Textual TUI, retro dashboardy, visual knowledge graphs.

Źródła: 19 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "ui"



MODULES: list[str] = [
    'Artlist AI voice generator',
    'Ciekawe rozwiązania projektowe',
    'HarfBuzz 12.3 i przyspieszenie renderowania tekstu',
    'Interfejsy i wizualizacja przepływów wiedzy',
    'Kolory przyjazne daltonistom dla stanów danych',
    'New experimental UI  and retro finds',
    'Nowe demo - retro UI i terminale',
    'Nowe eksperymentalne UI i retro‑wizualizacje',
    'Nowe odkrycia: retro UI i terminale',
    'Nowości: retro UI i terminale',
    'Nowości: retro‑UI i terminale',
    'Projektowanie interfejsów głosowych i opóźnień reakcji',
    'Reguła UX Widoczny Kręgosłup Decyzji',
    'Retro 9-Slice UI Lab',
    'Retro TUI Textual, FTXUI, termdash',
    'Retro-futuristic dashboard plan',
    'Retro-pulpity z Textual i Plotext',
    'Tui vs Tiu',
    'mini.nvim 0.17.0 z nowym modułem cmdline',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "ui"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
