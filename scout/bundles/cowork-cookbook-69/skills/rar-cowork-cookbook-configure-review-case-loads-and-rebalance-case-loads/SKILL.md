---
name: "rar-cowork-cookbook-configure-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads", "rar_sha256": "31ede094fd178e13f0fe84bac8e5ef061380d0139e27c88808e5b40e1b4f4386", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 31ede094fd178e13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_review_case_loads_and_rebalance_case_loads_agent.py` first:

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
    "version": '2.0.0',
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
