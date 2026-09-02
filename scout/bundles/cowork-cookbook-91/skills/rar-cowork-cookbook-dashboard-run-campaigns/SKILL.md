---
name: "rar-cowork-cookbook-dashboard-run-campaigns"
description: "Produces a self-contained interactive HTML dashboard for run campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_run_campaigns", "rar_sha256": "a765a4003e1bc370811f3d079a303d542ed81823ec8ec2aa830f5b8803cb8e4b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_run_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-run-campaigns:87330af3e143530c0e70a33e0b04672037a9146a1254c268bb9a7fcda2fdc342", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_run_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_run_campaigns_agent.py` is
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
