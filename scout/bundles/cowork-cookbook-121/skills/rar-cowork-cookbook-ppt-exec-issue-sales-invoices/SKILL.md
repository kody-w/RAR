---
name: "rar-cowork-cookbook-ppt-exec-issue-sales-invoices"
description: "Generates an executive-ready PowerPoint deck on issue sales invoices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_sales_invoices", "rar_sha256": "26f50d1a0f6cd7bcbed79a2c824dabe89bfec11e13d36392b5417f282998534a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_issue_sales_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-issue-sales-invoices:f0beb741e154e5113ca4638855cf10cc38d3155cdc6f5a056cf721ab7d549fc8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_issue_sales_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_issue_sales_invoices_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 26f50d1a0f6cd7bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_sales_invoices_agent.py` first:

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
    "version": '2.0.0',
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
