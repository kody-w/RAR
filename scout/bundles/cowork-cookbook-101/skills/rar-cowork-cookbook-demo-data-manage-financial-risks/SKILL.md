---
name: "rar-cowork-cookbook-demo-data-manage-financial-risks"
description: "Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_financial_risks", "rar_sha256": "2fc792f3457bad9ecb3ff996396de6a14c908db743bf40f11dfe9943893d9eb1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_financial_risks`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_financial_risks_agent.py` and in the RCI capsule.

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

Manage financial risks Demo Data Generator — Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-financial-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 2fc792f3457bad9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_financial_risks_agent.py` first:

```bash
python3 demo_data_manage_financial_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_financial_risks_agent.py   # or on stdin
python3 demo_data_manage_financial_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage financial risks Demo Data Generator — Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-financial-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_financial_risks',
    "version": '2.0.1',
    "display_name": 'Manage financial risks Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-financial-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-financial-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9554c2f8201ad4b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/manage-financial-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-manage-financial-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageFinancialRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageFinancialRisks'
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
    print(DemoDataManageFinancialRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
