#!/usr/bin/env python3
"""
demo.py — demo ishkarim-ui

Interfejsy terminalowe dla systemów AI — Textual TUI, retro dashboardy, visual knowledge graphs

Uruchomienie:
    python projects/ishkarim-ui/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_ui as m

docs = m.load_knowledge_index()
textual_docs = [d for d in docs if "textual" in d["name"].lower() or "tui" in d["name"].lower()]
graph_docs   = [d for d in docs if "graph" in d["name"].lower() or "visual" in d["name"].lower()]

print(f"Interfejsy AI — {len(docs)} katalogów wiedzy")
print(f"  Textual/TUI:     {len(textual_docs)}")
print(f"  Visual/Graph:    {len(graph_docs)}")
print()
print("Przykładowe projekty:")
for d in docs[:5]:
    print(f"  [{d['maturity']:8s}] {d['name'][:65]}")

