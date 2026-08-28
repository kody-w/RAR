---
name: "rar-cowork-cookbook-adaptive-card-issue-requests-for-quotation"
description: "Produces a reusable Adaptive Card JSON snapshot of issue requests for quotation status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_issue_requests_for_quotation", "rar_sha256": "9962a0528ad7f70681bdc79d8fdfe4e45a1b1f0db3582eba9ed2082dc3929d17", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_issue_requests_for_quotation`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_issue_requests_for_quotation_agent.py` and in the RCI capsule.

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

Issue requests for quotation Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of issue requests for quotation status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-issue-requests-for-quotation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 9962a0528ad7f706…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_issue_requests_for_quotation_agent.py` first:

```bash
python3 adaptive_card_issue_requests_for_quotation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_issue_requests_for_quotation_agent.py   # or on stdin
python3 adaptive_card_issue_requests_for_quotation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for quotation Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of issue requests for quotation status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-issue-requests-for-quotation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_issue_requests_for_quotation',
    "version": '2.0.1',
    "display_name": 'Issue requests for quotation Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of issue requests for quotation status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-issue-requests-for-quotation',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-issue-requests-for-quotation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e61e072ee71a49d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-quotation'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-issue-requests-for-quotation', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardIssueRequestsForQuotation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIssueRequestsForQuotation'
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
    print(AdaptiveCardIssueRequestsForQuotation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
