---
name: "rar-cowork-cookbook-sales-target-attainment-tracker"
description: "Compares actual closed-won performance against recorded sales targets and reports attainment, gap to target, and the pipeline coverage available to close it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_target_attainment_tracker", "rar_sha256": "61a05f8683189cac5bf4ff1e4f87e9c77c74383ffe40ff15c180f48dd3377b11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_target_attainment_tracker_agent.py` and embedded as the fenced Python below (sha256 61a05f8683189cac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_target_attainment_tracker_agent.py` first:

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
    "version": '2.0.0',
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
