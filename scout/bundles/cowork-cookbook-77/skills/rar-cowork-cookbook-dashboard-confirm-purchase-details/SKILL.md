---
name: "rar-cowork-cookbook-dashboard-confirm-purchase-details"
description: "Produces a self-contained interactive HTML dashboard for confirm purchase details - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_confirm_purchase_details", "rar_sha256": "515cb13c00dc7ace79ffa93a97254b58e09da5b7972f9a06034d4940e96a029b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_confirm_purchase_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_confirm_purchase_details_agent.py` and in the RCI capsule.

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

Confirm purchase details Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for confirm purchase details - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 515cb13c00dc7ace…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_confirm_purchase_details_agent.py` first:

```bash
python3 dashboard_confirm_purchase_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_confirm_purchase_details_agent.py   # or on stdin
python3 dashboard_confirm_purchase_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Confirm purchase details Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for confirm purchase details - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_confirm_purchase_details',
    "version": '2.0.0',
    "display_name": 'Confirm purchase details Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for confirm purchase details - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-confirm-purchase-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52a3b064cdf99266',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/confirm-purchase-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-confirm-purchase-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConfirmPurchaseDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfirmPurchaseDetails'
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
    print(DashboardConfirmPurchaseDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
