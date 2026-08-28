---
name: "rar-cowork-cookbook-teams-update-dispute-invoices"
description: "Drafts a Teams channel post on dispute invoices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_dispute_invoices", "rar_sha256": "c44c0bf3b721b557701716146c547976e8d43ec31c02a3724ac861b7a2c5349b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_dispute_invoices_agent.py` and embedded as the fenced Python below (sha256 c44c0bf3b721b557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_dispute_invoices_agent.py` first:

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
    "version": '2.0.1',
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
