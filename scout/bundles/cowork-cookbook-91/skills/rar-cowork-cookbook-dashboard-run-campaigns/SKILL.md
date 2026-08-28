---
name: "rar-cowork-cookbook-dashboard-run-campaigns"
description: "Produces a self-contained interactive HTML dashboard for run campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_run_campaigns", "rar_sha256": "a765a4003e1bc370811f3d079a303d542ed81823ec8ec2aa830f5b8803cb8e4b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 a765a4003e1bc370…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_run_campaigns_agent.py` first:

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
    "version": '2.0.0',
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
