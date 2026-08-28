---
name: "rar-cowork-cookbook-sales-target-attainment-tracker"
description: "Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_target_attainment_tracker", "rar_sha256": "8744aee0d8203a8998fcca61ff01f9d1f1c058d65ea9b1d9fef9391e5ee609e7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/sales_target_attainment_tracker`. The original RAPP
agent is preserved byte-for-byte in `sales_target_attainment_tracker_agent.py` and in the RCI capsule.

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

Sales Target Attainment Tracker — Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-target-attainment-tracker
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_target_attainment_tracker_agent.py` and embedded as the fenced Python below (sha256 8744aee0d8203a89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_target_attainment_tracker_agent.py` first:

```bash
python3 sales_target_attainment_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_target_attainment_tracker_agent.py   # or on stdin
python3 sales_target_attainment_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Target Attainment Tracker — Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-target-attainment-tracker
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/sales_target_attainment_tracker',
    "version": '2.0.1',
    "display_name": 'Sales Target Attainment Tracker',
    "description": 'Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'sales-target-attainment-tracker',
        "upstream_url": 'https://coworkcookbook.com/recipes/sales-target-attainment-tracker',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdb5fea7012d7cfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/sales-target-attainment-tracker', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:pipeline'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class SalesTargetAttainmentTracker(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SalesTargetAttainmentTracker'
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
    print(SalesTargetAttainmentTracker().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
