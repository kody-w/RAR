---
name: "rar-cowork-cookbook-ppt-exec-issue-blanket-purchase-orders"
description: "Generates an executive-ready PowerPoint deck on issue blanket purchase orders status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders", "rar_sha256": "e0e3b4f4b5ab4c5ffb58dd4a6b5788f37c0c278a5b776ed2102045d86eef8374", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_issue_blanket_purchase_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-issue-blanket-purchase-orders:05e4bba33fb44ffeb29f571c04480f85fd71ee8a3c1ad9c35bd0a1569104f316", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_issue_blanket_purchase_orders_agent.py` is
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

Issue blanket purchase orders Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on issue blanket purchase orders status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 e0e3b4f4b5ab4c5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_blanket_purchase_orders_agent.py` first:

```bash
python3 ppt_exec_issue_blanket_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_issue_blanket_purchase_orders_agent.py   # or on stdin
python3 ppt_exec_issue_blanket_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue blanket purchase orders Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on issue blanket purchase orders status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders',
    "version": '2.0.0',
    "display_name": 'Issue blanket purchase orders Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on issue blanket purchase orders status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-issue-blanket-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0aa7983974f72b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-blanket-purchase-orders'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-issue-blanket-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIssueBlanketPurchaseOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIssueBlanketPurchaseOrders'
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
    print(PptExecIssueBlanketPurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
