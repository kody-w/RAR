---
name: "rar-cowork-cookbook-dashboard-confirm-purchase-details"
description: "Produces a self-contained interactive HTML dashboard for confirm purchase details - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_confirm_purchase_details", "rar_sha256": "f3155cc278c60ded23ec59510aee16f980753f46c5f385127feaf5d156a40ce2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 f3155cc278c60ded…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_confirm_purchase_details_agent.py` first:

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
    "version": '2.0.1',
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
