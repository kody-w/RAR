---
name: "rar-cowork-cookbook-bulk-update-create-solution-blueprint"
description: "Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_solution_blueprint", "rar_sha256": "b7c692f677651c9e1f0577def0e3e57cd4789adb313ca51d97a310f4cc70ac8e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_create_solution_blueprint`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_create_solution_blueprint_agent.py` and in the RCI capsule.

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

Create solution blueprint Bulk Field Update — Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 b7c692f677651c9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_solution_blueprint_agent.py` first:

```bash
python3 bulk_update_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_solution_blueprint_agent.py   # or on stdin
python3 bulk_update_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Bulk Field Update — Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_solution_blueprint',
    "version": '2.0.0',
    "display_name": 'Create solution blueprint Bulk Field Update',
    "description": 'Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '618b2fb15dd02960',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCreateSolutionBlueprint(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateSolutionBlueprint'
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
    print(BulkUpdateCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
