---
name: "rar-cowork-cookbook-adaptive-card-issue-requests-for-quotation"
description: "Produces a reusable Adaptive Card JSON snapshot of issue requests for quotation status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_issue_requests_for_quotation", "rar_sha256": "9da0fbaee17034f0bf0b85ade4a96aabccb409f23033fcb60b3d42ff75516e41", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 9da0fbaee17034f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_issue_requests_for_quotation_agent.py` first:

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
    "version": '2.0.0',
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
