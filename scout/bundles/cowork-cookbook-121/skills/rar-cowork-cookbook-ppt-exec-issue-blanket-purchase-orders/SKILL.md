---
name: "rar-cowork-cookbook-ppt-exec-issue-blanket-purchase-orders"
description: "Generates an executive-ready PowerPoint deck on issue blanket purchase orders status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders", "rar_sha256": "e14ec44bc4489a4aed0c6f22d6b629e812caa529f2e5ae88aa935db58a5148fa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_issue_blanket_purchase_orders_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 e14ec44bc4489a4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_blanket_purchase_orders_agent.py` first:

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
    "version": '2.0.1',
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
