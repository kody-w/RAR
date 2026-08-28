---
name: "rar-cowork-cookbook-dashboard-issue-requests-for-quotation"
description: "Produces a self-contained interactive HTML dashboard for issue requests for quotation - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_requests_for_quotation", "rar_sha256": "ea3268ea6554bbfbd9d46c19de8df7995a4b588b6beec3fd1939d63590375b56", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 ea3268ea6554bbfb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_requests_for_quotation_agent.py` first:

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
    "version": '2.0.0',
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
