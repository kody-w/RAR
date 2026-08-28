---
name: "rar-cowork-cookbook-ppt-exec-assess-customer-credit-risk"
description: "Generates an executive-ready PowerPoint deck on assess customer credit risk status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assess_customer_credit_risk", "rar_sha256": "79fe949db112201dcab770783115ca46fe4ecff34fddefb0341d58b050bce40b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assess_customer_credit_risk_agent.py` and embedded as the fenced Python below (sha256 79fe949db112201d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assess_customer_credit_risk_agent.py` first:

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
    "version": '2.0.0',
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
