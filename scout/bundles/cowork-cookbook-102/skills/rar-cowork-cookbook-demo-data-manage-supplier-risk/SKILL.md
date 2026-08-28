---
name: "rar-cowork-cookbook-demo-data-manage-supplier-risk"
description: "Generates and creates realistic demo records for manage supplier risk in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_supplier_risk", "rar_sha256": "bf64a72bacfc50e48868caf5d9acb245144f63ea0e8766906232c0f78becc02d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 bf64a72bacfc50e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_supplier_risk_agent.py` first:

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
    "version": '2.0.1',
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
