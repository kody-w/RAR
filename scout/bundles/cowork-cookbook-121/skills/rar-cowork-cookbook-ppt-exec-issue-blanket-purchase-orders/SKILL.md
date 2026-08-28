---
name: "rar-cowork-cookbook-ppt-exec-issue-blanket-purchase-orders"
description: "Generates an executive-ready PowerPoint deck on issue blanket purchase orders status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders", "rar_sha256": "e0e3b4f4b5ab4c5ffb58dd4a6b5788f37c0c278a5b776ed2102045d86eef8374", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
