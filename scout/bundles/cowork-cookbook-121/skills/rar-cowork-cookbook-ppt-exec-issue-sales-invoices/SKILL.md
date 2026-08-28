---
name: "rar-cowork-cookbook-ppt-exec-issue-sales-invoices"
description: "Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_sales_invoices", "rar_sha256": "41c5aae10db60cd3bccc3aa3798cded0ce3f03cd3646f22e02ae839341eb0d7b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_issue_sales_invoices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_issue_sales_invoices_agent.py` and in the RCI capsule.

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

Issue sales invoices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 41c5aae10db60cd3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_sales_invoices_agent.py` first:

```bash
python3 ppt_exec_issue_sales_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_issue_sales_invoices_agent.py   # or on stdin
python3 ppt_exec_issue_sales_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue sales invoices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_issue_sales_invoices',
    "version": '2.0.1',
    "display_name": 'Issue sales invoices Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-issue-sales-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e9dfce03a79d933',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-sales-invoices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-issue-sales-invoices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecIssueSalesInvoices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIssueSalesInvoices'
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
    print(PptExecIssueSalesInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
