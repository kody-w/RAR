---
name: "rar-cowork-cookbook-demo-data-track-project-time"
description: "Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_project_time", "rar_sha256": "472510e58316a77e5726dc8d50cfcb08d9546ad28fb902cf9b84233dfa2a79dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_project_time`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_project_time_agent.py` and in the RCI capsule.

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

Track project time Demo Data Generator — Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_project_time_agent.py` and embedded as the fenced Python below (sha256 472510e58316a77e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_project_time_agent.py` first:

```bash
python3 demo_data_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_project_time_agent.py   # or on stdin
python3 demo_data_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Demo Data Generator — Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_project_time',
    "version": '2.0.0',
    "display_name": 'Track project time Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6976d7294fae1d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTrackProjectTime(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackProjectTime'
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
    print(DemoDataTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
