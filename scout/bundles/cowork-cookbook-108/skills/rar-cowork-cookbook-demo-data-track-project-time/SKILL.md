---
name: "rar-cowork-cookbook-demo-data-track-project-time"
description: "Generates and creates realistic demo records for track project time in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_project_time", "rar_sha256": "610d08f5fd1ff30562c0acba645b732237f96e17dc8f2467f3521c3fc4411db9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_project_time_agent.py` and embedded as the fenced Python below (sha256 610d08f5fd1ff305…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_project_time_agent.py` first:

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
    "version": '2.0.1',
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
