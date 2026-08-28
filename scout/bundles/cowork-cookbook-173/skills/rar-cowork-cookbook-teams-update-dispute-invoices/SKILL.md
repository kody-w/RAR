---
name: "rar-cowork-cookbook-teams-update-dispute-invoices"
description: "Drafts a Teams channel post on dispute invoices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_dispute_invoices", "rar_sha256": "6e15b58881d256c4e95ed5c8bd68d19bf2cf2823936b8288fbaf655b10fccdd9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_dispute_invoices`. The original RAPP
agent is preserved byte-for-byte in `teams_update_dispute_invoices_agent.py` and in the RCI capsule.

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
