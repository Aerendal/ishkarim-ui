"""
extracted.py — kod wyekstrahowany z WORK.md dla obszaru ui.

Zawiera 14 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Artlist AI voice generator
from TTS.api import TTS
tts = TTS(model_name="tts_models/pl/mai_female", progress_bar=False)
tts.tts_to_file(text="Witaj w mojej grze.", file_path="output.wav")

# Source: HarfBuzz 12.3 i przyspieszenie renderowania tekstu
# cases.yaml – definicja targetu
targets:
  hb-12.3.0:
    hb_shape: hb-shape
    env:
      LD_LIBRARY_PATH: "${HB_PREFIX}/lib:..."

# Source: Interfejsy i wizualizacja przepływów wiedzy
if regression_score > threshold or embedding_model_stale:
    guarded_edit(config, {"retriever": "bm25"}, reason="auto-fallback")
    log_decision("hybrid→bm25", score, threshold)

# Source: New experimental UI  and retro finds
@dataclass
class GraphViewModel:
    nodes: list[dict]   # [{id, label, type}]
    edges: list[dict]   # [{from, to, label}]
    focus_node_id: str | None
    groups: list[str]
    schema_version: str = "1.0"
    model_hash: str = ""  # stable JSON hash

@dataclass
class TimelineViewModel:
    series: list[dict]  # [{name, points: [(t, value)]}]
    window: tuple[str, str]
    markers: list[dict]

# Source: New experimental UI  and retro finds
def ai_assist_loop(prompt: str, context: dict) -> dict:
    proposal = model.generate(prompt, context, output_format="diff")
    check = static_check(proposal)     # lint, schema, zakazane importy
    if not check.passed: return {"status": "rejected", "reason": check.errors}
    sandbox_result = run_in_sandbox(proposal, timeout_ms=5000, deny_net=True)
    scores = score(sandbox_result)     # perf, a11y, bundle_size
    return {"proposal": proposal, "scores": scores, "decision": "pending_human"}

# Source: Nowe odkrycia: retro UI i terminale
class JsonlLogger:
    def write(self, level, event, data, run_id=None):
        obj = LogEvent(ts=utc_now_iso(), level=level, event=event, data=data, run_id=run_id)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(obj), ensure_ascii=False) + "\n")

# Source: Nowe odkrycia: retro UI i terminale
manifest = {
    "run_id": run_id,
    "input_hash": sha256(json_args_bytes).hexdigest(),
    "output_hash": sha256(stdout_bytes).hexdigest(),
    "timeout": p.timeout_sec,
    "sandbox": use_sandbox,
    "entry": entry_path,
}

# Source: Retro TUI Textual, FTXUI, termdash
@dataclass(frozen=True)
class Profile:
    name: str
    sandbox_required: bool
    allow_unsafe_without_sandbox: bool
    max_timeout_seconds: int
    require_manifest: bool

def load_profiles(path: str = "config/profiles.yaml") -> Dict[str, Profile]:
    ...

# Source: Retro TUI Textual, FTXUI, termdash
@dataclass(frozen=True)
class Decision:
    allowed: bool
    approval_level: str        # "STANDARD" | "EXTENDED" | "DOUBLE_CONFIRM"
    sandbox_required: bool
    sandbox_backend: str       # "bubblewrap" | "none" | "blocked"
    timeout_seconds: int
    snapshot_db_required: bool
    snapshot_fs_required: bool
    rollback_plan: str
    errors: List[str]
    warnings: List[str]

def validate_and_classify_action(
    manifest: dict,
    profile: Profile,
    sandbox_policy: dict
) -> Decision:
    ...

# Source: Retro TUI Textual, FTXUI, termdash
@dataclass(frozen=True)
class SandboxAvailability:
    available: bool
    backend: str    # "bubblewrap" | "none" | "blocked"
    reason: str

def detect_sandbox_backend(
    requested: str,             # "auto" | "bubblewrap" | "none"
    allow_unsafe_without_sandbox: bool
) -> SandboxAvailability:
    # auto: jeśli bwrap exists → bubblewrap; else → blocked (lub unsafe jeśli DEV)
    ...

# Source: Retro TUI Textual, FTXUI, termdash
@dataclass(frozen=True)
class BindPlan:
    ro_binds: List[Tuple[Path, Path]]  # (src, dst) dla --ro-bind
    rw_binds: List[Tuple[Path, Path]]  # (src, dst) dla --bind
    chdir: Path
    deny_network: bool

def plan_binds(manifest: dict, policy: dict, repo_root: Path) -> BindPlan:
    # czyta manifest.permissions.fs_read / fs_write
    # weryfikuje prefixes (tylko ./relative, brak .., brak / /etc /usr)
    # minimalizuje prefixes (deduplikacja nadzbiorów)
    ...

# Source: Retro-pulpity z Textual i Plotext
class RingBuffer(Generic[T]):
    def __init__(self, maxlen: int):
        self._d: deque[T] = deque(maxlen=maxlen)
    def push(self, item: T) -> None: self._d.append(item)

# Source: Retro-pulpity z Textual i Plotext
@dataclass(frozen=True)
class RefreshPolicy:
    ui_ms: int = 250; chart_ms: int = 1000; telemetry_ms: int = 200
    ui_max_logs: int = 400; chart_max_points: int = 120

# Source: Retro-pulpity z Textual i Plotext
@dataclass(frozen=True)
class TaskRow: task_id: str; status: TaskStatus; title: str
@dataclass(frozen=True)
class LogEvent: ts: float; level: str; msg: str; src: str = "app"
