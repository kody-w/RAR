---
name: "rar-cowork-cookbook-demo-data-manage-supplier-risk"
description: "Generates and creates realistic demo records for manage supplier risk in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_supplier_risk", "rar_sha256": "cfb169b1bc4974c594bb356ad2353dbf1100b0636f6d59efd61300f3b6c64c36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_supplier_risk`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_supplier_risk_agent.py` and in the RCI capsule.

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

Manage supplier risk Demo Data Generator — Generates and creates realistic demo records for manage supplier risk in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 cfb169b1bc4974c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_supplier_risk_agent.py` first:

```bash
python3 demo_data_manage_supplier_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_supplier_risk_agent.py   # or on stdin
python3 demo_data_manage_supplier_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier risk Demo Data Generator — Generates and creates realistic demo records for manage supplier risk in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_supplier_risk',
    "version": '2.0.0',
    "display_name": 'Manage supplier risk Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage supplier risk in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-supplier-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17ef1b17ea6d8436',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-risk'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-manage-supplier-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageSupplierRisk(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageSupplierRisk'
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
    print(DemoDataManageSupplierRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
