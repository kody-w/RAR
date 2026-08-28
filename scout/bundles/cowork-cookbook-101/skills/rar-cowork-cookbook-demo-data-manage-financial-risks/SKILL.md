---
name: "rar-cowork-cookbook-demo-data-manage-financial-risks"
description: "Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_financial_risks", "rar_sha256": "9f217f8844e605dd8ea205a8cfeb617a5e4b52f410fa5dd719f7a91e0989c966", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 9f217f8844e605dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_financial_risks_agent.py` first:

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
    "version": '2.0.0',
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
