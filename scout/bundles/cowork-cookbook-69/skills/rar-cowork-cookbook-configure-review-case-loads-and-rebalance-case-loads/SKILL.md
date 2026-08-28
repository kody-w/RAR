---
name: "rar-cowork-cookbook-configure-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads", "rar_sha256": "0ef53a329900b005d6fc61f38ea76fcc45a5b40e00927076f5c22408ab74a58c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads`. The original RAPP
agent is preserved byte-for-byte in `configure_review_case_loads_and_rebalance_case_loads_agent.py` and in the RCI capsule.

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

Review case loads and rebalance case loads Configuration Bulk Setup — Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 0ef53a329900b005…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_review_case_loads_and_rebalance_case_loads_agent.py` first:

```bash
python3 configure_review_case_loads_and_rebalance_case_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_review_case_loads_and_rebalance_case_loads_agent.py   # or on stdin
python3 configure_review_case_loads_and_rebalance_case_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review case loads and rebalance case loads Configuration Bulk Setup — Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads',
    "version": '2.0.1',
    "display_name": 'Review case loads and rebalance case loads Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-review-case-loads-and-rebalance-case-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6ecb6de7afe720c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-case-loads-and-rebalance-case-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-review-case-loads-and-rebalance-case-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReviewCaseLoadsAndRebalanceCaseLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReviewCaseLoadsAndRebalanceCaseLoads'
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
    print(ConfigureReviewCaseLoadsAndRebalanceCaseLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
