---
name: "rar-cowork-cookbook-teams-update-dispute-invoices"
description: "Drafts a Teams channel post on dispute invoices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_dispute_invoices", "rar_sha256": "6e15b58881d256c4e95ed5c8bd68d19bf2cf2823936b8288fbaf655b10fccdd9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_dispute_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-dispute-invoices:01e3bbf667c609674112a138f3c350f1af10b99c45034b67d977f45b0f8cd5cb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_dispute_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_dispute_invoices_agent.py` is
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

Dispute invoices Teams Channel Update — Drafts a Teams channel post on dispute invoices status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-dispute-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_dispute_invoices_agent.py` and embedded as the fenced Python below (sha256 6e15b58881d256c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_dispute_invoices_agent.py` first:

```bash
python3 teams_update_dispute_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_dispute_invoices_agent.py   # or on stdin
python3 teams_update_dispute_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispute invoices Teams Channel Update — Drafts a Teams channel post on dispute invoices status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-dispute-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_dispute_invoices',
    "version": '2.0.0',
    "display_name": 'Dispute invoices Teams Channel Update',
    "description": 'Drafts a Teams channel post on dispute invoices status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-dispute-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-dispute-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bd06f6bab003af2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/dispute-invoices'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-dispute-invoices', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDisputeInvoices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDisputeInvoices'
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
    print(TeamsUpdateDisputeInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
