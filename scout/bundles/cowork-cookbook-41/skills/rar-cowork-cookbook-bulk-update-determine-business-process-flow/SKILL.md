---
name: "rar-cowork-cookbook-bulk-update-determine-business-process-flow"
description: "Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_determine_business_process_flow", "rar_sha256": "a55590ecbb668641f0930a447f2ce0eb7b515e432989a5d857289427ba047fdf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_determine_business_process_flow`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_determine_business_process_flow_agent.py` and in the RCI capsule.

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

Determine business process flow Bulk Field Update — Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 a55590ecbb668641…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_determine_business_process_flow_agent.py` first:

```bash
python3 bulk_update_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_determine_business_process_flow_agent.py   # or on stdin
python3 bulk_update_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Bulk Field Update — Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_determine_business_process_flow',
    "version": '2.0.1',
    "display_name": 'Determine business process flow Bulk Field Update',
    "description": 'Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd43c76b21ba53c6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDetermineBusinessProcessFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDetermineBusinessProcessFlow'
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
    print(BulkUpdateDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
