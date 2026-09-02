---
name: "rar-cat-agent-skills-copilot-agents-news-scout"
description: "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agents_news_scout", "rar_sha256": "6fc2a0fa301aa19d483c4c839feed41debd86262eb0fa2852fdcaccdebed450e", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_agents_news_scout_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-agents-news-scout:c1c3f93ced021b490cd44b9875e94a9bd5db54b8e3866d9195c258061b767431", "kind": "skill"}, "version": "2.0.0", "author": "Elliot Margot", "tags": ["news", "copilot", "agent", "digest", "automation", "weekly", "teams"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_agents_news_scout`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_agents_news_scout_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
