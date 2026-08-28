---
name: "rar-cowork-cookbook-bulk-update-measure-adoption-and-success"
description: "Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_adoption_and_success", "rar_sha256": "ca77966ec9c5898ff5462058b73d9761ca0dfafcd393dbda9fab8a9e14d015c4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Bulk Field Update — Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 ca77966ec9c5898f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_adoption_and_success_agent.py` first:

```bash
python3 bulk_update_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_adoption_and_success_agent.py   # or on stdin
python3 bulk_update_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Bulk Field Update — Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_adoption_and_success',
    "version": '2.0.1',
    "display_name": 'Measure adoption and success Bulk Field Update',
    "description": 'Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb7a04f62dee1a46',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMeasureAdoptionAndSuccess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureAdoptionAndSuccess'
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
    print(BulkUpdateMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
