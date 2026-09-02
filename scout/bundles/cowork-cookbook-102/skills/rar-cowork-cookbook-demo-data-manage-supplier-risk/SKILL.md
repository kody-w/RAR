---
name: "rar-cowork-cookbook-demo-data-manage-supplier-risk"
description: "Generates and creates realistic demo records for manage supplier risk in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_supplier_risk", "rar_sha256": "cfb169b1bc4974c594bb356ad2353dbf1100b0636f6d59efd61300f3b6c64c36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_supplier_risk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-supplier-risk:a59c3630724e9a2a0aa58bcaafe18774eed88b1ad4fef495183530c31e58f901", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_supplier_risk`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_supplier_risk_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
