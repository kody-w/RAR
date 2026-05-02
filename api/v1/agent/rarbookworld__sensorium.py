"""sensorium_agent.py — single sacred agent. Ingests raw moment, normalizes shape."""
try:
    from agents.basic_agent import BasicAgent  # RAPP layout
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent      # flat / @publisher layout
    except ModuleNotFoundError:
        class BasicAgent:                       # last-resort standalone
            def __init__(self, name, metadata): self.name, self.metadata = name, metadata
import json, os, urllib.request, urllib.error

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/sensorium",
    "version": "0.1.0",
    "display_name": "Sensorium",
    "description": "Normalizes a raw moment (code commit, voice memo, bookmark, agent run, location, conversation, decision, reading note) into a structured JSON shape.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "ingest"
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT"
    ],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

SOUL = """You are the Sensorium of the MomentFactory pipeline. You receive a raw
moment from any source (code commit, voice memo transcript, web bookmark, agent
run output, location ping with note, conversation snippet, decision moment,
reading note) and return a normalized JSON shape the rest of the pipeline can
consume.

Your output MUST be valid JSON with exactly these keys:
  source_summary  — one sentence, what the moment IS
  key_facts       — list of 3-7 concrete facts pulled verbatim from the source
  voice_signature — list of 2-4 short phrases that capture HOW the source was written
  surface_area    — what kind of thing this moment touches (people, code, place, idea)

Be a passive recorder. Do NOT interpret, judge, or embellish. If the source is
sparse, your output is sparse — never invent. If a key_fact is just a number or
a filename, that is fine — verbatim is the contract."""


class SensoriumAgent(BasicAgent):
    def __init__(self):
        self.name = "Sensorium"
        self.metadata = {
            "name": self.name,
            "description": "Normalizes a raw moment into structured shape for the MomentFactory pipeline.",
            "parameters": {"type": "object",
                "properties": {
                    "source": {"type": "string", "description": "Raw moment text"},
                    "source_type": {"type": "string", "description": "code-commit | voice-memo | web-bookmark | agent-run | location | conversation | decision | reading-note"},
                },
                "required": ["source"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, source="", source_type="unknown", **kwargs):
        return _llm_call(SOUL,
            f"source_type: {source_type}\n\n"
            f"--- SOURCE ---\n{source}\n--- END ---\n\n"
            "Return ONLY the JSON shape. No prose before or after.")


def _llm_call(soul, user_prompt):
    msgs = [{"role": "system", "content": soul}, {"role": "user", "content": user_prompt}]
    ep, key = os.environ.get("AZURE_OPENAI_ENDPOINT", ""), os.environ.get("AZURE_OPENAI_API_KEY", "")
    dep = os.environ.get("AZURE_OPENAI_DEPLOYMENT") or os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "")
    if ep and key:
        url = ep if "/chat/completions" in ep else ep.rstrip("/") + f"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview"
        if "/chat/completions" in ep and "/openai/v1/" not in ep and "?" not in url:
            url += "?api-version=2025-01-01-preview"
        return _post(url, {"messages": msgs, "model": dep},
                      {"Content-Type": "application/json", "api-key": key})
    if os.environ.get("OPENAI_API_KEY"):
        return _post("https://api.openai.com/v1/chat/completions",
                      {"model": os.environ.get("OPENAI_MODEL", "gpt-4o"), "messages": msgs},
                      {"Content-Type": "application/json",
                       "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    return '{"source_summary":"(no LLM configured)","key_facts":[],"voice_signature":[],"surface_area":[]}'


def _post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            j = json.loads(r.read().decode("utf-8"))
        c = j.get("choices") or []
        return (c[0]["message"].get("content") or "") if c else ""
    except urllib.error.HTTPError as e:
        return f"(LLM HTTP {e.code}: {e.read().decode('utf-8')[:200]})"
    except urllib.error.URLError as e:
        return f"(LLM network error: {e})"