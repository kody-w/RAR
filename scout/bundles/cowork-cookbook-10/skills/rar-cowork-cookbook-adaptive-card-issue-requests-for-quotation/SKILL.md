---
name: "rar-cowork-cookbook-adaptive-card-issue-requests-for-quotation"
description: "Produces a reusable Adaptive Card JSON snapshot of issue requests for quotation status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_issue_requests_for_quotation", "rar_sha256": "9da0fbaee17034f0bf0b85ade4a96aabccb409f23033fcb60b3d42ff75516e41", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_issue_requests_for_quotation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-issue-requests-for-quotation:0dcc2c3db188b6beceb9ed1b26b01a1ebae357936c3dae340b9f96d05cd9902b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_issue_requests_for_quotation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_issue_requests_for_quotation_agent.py` is
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
