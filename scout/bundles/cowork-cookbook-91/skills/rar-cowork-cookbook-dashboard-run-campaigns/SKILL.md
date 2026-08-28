---
name: "rar-cowork-cookbook-dashboard-run-campaigns"
description: "Produces a self-contained interactive HTML dashboard for run campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_run_campaigns", "rar_sha256": "9951a8436bf33882f57b884fb4988a4430e43ada396a80f3f962f317c16bf758", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_run_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_run_campaigns_agent.py` and in the RCI capsule.

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

Run campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for run campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-run-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 9951a8436bf33882…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_run_campaigns_agent.py` first:

```bash
python3 dashboard_run_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_run_campaigns_agent.py   # or on stdin
python3 dashboard_run_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for run campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-run-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_run_campaigns',
    "version": '2.0.1',
    "display_name": 'Run campaigns Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for run campaigns - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-run-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-run-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e839ef72bb218f1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-run-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRunCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRunCampaigns'
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
    print(DashboardRunCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
