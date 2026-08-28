---
name: "rar-cowork-cookbook-demo-data-consolidate-and-eliminate-financials"
description: "Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_and_eliminate_financials", "rar_sha256": "29f215cf93fd0c17a2e388b0586a6e3f7a8cc5db91499fa74149f6eee2952312", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 29f215cf93fd0c17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_and_eliminate_financials_agent.py` first:

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
    "version": '2.0.0',
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
