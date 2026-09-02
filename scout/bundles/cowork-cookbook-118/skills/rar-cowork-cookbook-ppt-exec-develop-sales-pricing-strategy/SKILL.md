---
name: "rar-cowork-cookbook-ppt-exec-develop-sales-pricing-strategy"
description: "Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy", "rar_sha256": "7d381d19c23f443f9d77fd889f7f0a6a1ce93cae5fac230a9008c1f2458c44f2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_sales_pricing_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-sales-pricing-strategy:d373aa4c2e0ec9e5b62787a93e086d3fa40f732a98d10b5c3da5eba97012d89c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_sales_pricing_strategy_agent.py` is
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

Develop sales pricing strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 7d381d19c23f443f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_sales_pricing_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_sales_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_sales_pricing_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_sales_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales pricing strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy',
    "version": '2.0.0',
    "display_name": 'Develop sales pricing strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-develop-sales-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '911a101f3fbfd1c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-pricing-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-develop-sales-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopSalesPricingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopSalesPricingStrategy'
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
    print(PptExecDevelopSalesPricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
