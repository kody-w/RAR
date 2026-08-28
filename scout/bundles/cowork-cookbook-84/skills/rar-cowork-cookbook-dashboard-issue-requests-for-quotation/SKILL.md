---
name: "rar-cowork-cookbook-dashboard-issue-requests-for-quotation"
description: "Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_requests_for_quotation", "rar_sha256": "23c6214196458968743feabbb65a0be9fd9c408ad93449f5a4cf4eb7486c8ca9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_requests_for_quotation`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_requests_for_quotation_agent.py` and in the RCI capsule.

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

Issue requests for quotation Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 23c6214196458968…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_requests_for_quotation_agent.py` first:

```bash
python3 dashboard_issue_requests_for_quotation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_requests_for_quotation_agent.py   # or on stdin
python3 dashboard_issue_requests_for_quotation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for quotation Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_requests_for_quotation',
    "version": '2.0.1',
    "display_name": 'Issue requests for quotation Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-issue-requests-for-quotation',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d958454cfca363d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-quotation'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-issue-requests-for-quotation', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIssueRequestsForQuotation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueRequestsForQuotation'
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
    print(DashboardIssueRequestsForQuotation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
