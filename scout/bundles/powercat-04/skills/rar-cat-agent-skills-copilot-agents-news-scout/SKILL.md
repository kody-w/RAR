---
name: "rar-cat-agent-skills-copilot-agents-news-scout"
description: "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agents_news_scout", "rar_sha256": "6fc2a0fa301aa19d483c4c839feed41debd86262eb0fa2852fdcaccdebed450e", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Elliot Margot", "tags": ["news", "copilot", "agent", "digest", "automation", "weekly", "teams"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_agents_news_scout`. The original RAPP
agent is preserved byte-for-byte in `copilot_agents_news_scout_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Copilot & Agents News Scout — A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agents_news_scout_agent.py` and embedded as the fenced Python below (sha256 6fc2a0fa301aa19d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agents_news_scout_agent.py` first:

```bash
python3 copilot_agents_news_scout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agents_news_scout_agent.py   # or on stdin
python3 copilot_agents_news_scout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot & Agents News Scout — A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_agents_news_scout',
    "version": '2.0.0',
    "display_name": 'Copilot & Agents News Scout',
    "description": "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.",
    "author": 'Elliot Margot',
    "tags": ['news', 'copilot', 'agent', 'digest', 'automation', 'weekly', 'teams'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'copilot-agents-news-scout',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fc3502443ed8b977',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CopilotAgentsNewsScout(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotAgentsNewsScout'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(CopilotAgentsNewsScout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
