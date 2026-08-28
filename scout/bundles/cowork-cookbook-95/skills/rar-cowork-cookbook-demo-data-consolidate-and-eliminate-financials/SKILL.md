---
name: "rar-cowork-cookbook-demo-data-consolidate-and-eliminate-financials"
description: "Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_and_eliminate_financials", "rar_sha256": "7e938a1bdf4554cca8493c4f19e60c3b47b268370310a0376ff42c2394cb0fad", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_consolidate_and_eliminate_financials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_consolidate_and_eliminate_financials_agent.py` and in the RCI capsule.

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

Consolidate and eliminate financials Demo Data Generator — Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 7e938a1bdf4554cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 demo_data_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 demo_data_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Demo Data Generator — Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_and_eliminate_financials',
    "version": '2.0.1',
    "display_name": 'Consolidate and eliminate financials Demo Data Generator',
    "description": 'Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f35562681ac741e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConsolidateAndEliminateFinancials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateAndEliminateFinancials'
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
    print(DemoDataConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
