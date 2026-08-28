---
name: "rar-cowork-cookbook-ppt-exec-assess-customer-credit-risk"
description: "Generates an executive-ready PowerPoint deck on assess customer credit risk status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assess_customer_credit_risk", "rar_sha256": "ff0c055a661479ed9fb8b362705fc497b1dbf521a95b4c5b00c6fd06c6976123", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_assess_customer_credit_risk`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_assess_customer_credit_risk_agent.py` and in the RCI capsule.

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

Assess customer credit risk Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on assess customer credit risk status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assess-customer-credit-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assess_customer_credit_risk_agent.py` and embedded as the fenced Python below (sha256 ff0c055a661479ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assess_customer_credit_risk_agent.py` first:

```bash
python3 ppt_exec_assess_customer_credit_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_assess_customer_credit_risk_agent.py   # or on stdin
python3 ppt_exec_assess_customer_credit_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess customer credit risk Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on assess customer credit risk status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assess-customer-credit-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_assess_customer_credit_risk',
    "version": '2.0.1',
    "display_name": 'Assess customer credit risk Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on assess customer credit risk status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-assess-customer-credit-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-assess-customer-credit-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c73e8bbbfba5bc0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/assess-customer-credit-risk'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-assess-customer-credit-risk', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.4, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecAssessCustomerCreditRisk(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAssessCustomerCreditRisk'
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
    print(PptExecAssessCustomerCreditRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
