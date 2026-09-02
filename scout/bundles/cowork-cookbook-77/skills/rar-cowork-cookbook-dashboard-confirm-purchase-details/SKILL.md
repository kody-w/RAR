---
name: "rar-cowork-cookbook-dashboard-confirm-purchase-details"
description: "Produces a self-contained interactive HTML dashboard for confirm purchase details - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_confirm_purchase_details", "rar_sha256": "515cb13c00dc7ace79ffa93a97254b58e09da5b7972f9a06034d4940e96a029b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_confirm_purchase_details_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-confirm-purchase-details:fc8ba5fcc45acff2dc999db437b49d24314f78e78bf91660fcd92b6e11583055", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_confirm_purchase_details`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_confirm_purchase_details_agent.py` is
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
