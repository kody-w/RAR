---
name: "rar-cowork-cookbook-ppt-exec-assess-customer-credit-risk"
description: "Generates an executive-ready PowerPoint deck on assess customer credit risk status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assess_customer_credit_risk", "rar_sha256": "79fe949db112201dcab770783115ca46fe4ecff34fddefb0341d58b050bce40b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_assess_customer_credit_risk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-assess-customer-credit-risk:137399cb5c40f1e79527c38c5eb3dc8f0dfb4fe3ed41121656478a55e0a95bef", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_assess_customer_credit_risk`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_assess_customer_credit_risk_agent.py` is
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
