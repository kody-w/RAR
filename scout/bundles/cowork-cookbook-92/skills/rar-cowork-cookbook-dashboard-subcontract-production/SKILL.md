---
name: "rar-cowork-cookbook-dashboard-subcontract-production"
description: "Produces a self-contained interactive HTML dashboard for subcontract production - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_subcontract_production", "rar_sha256": "1768b894f7265e37724248b9fbc6b022c6f50221c882fc9788e43b106de95752", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_subcontract_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-subcontract-production:0ba65a5ec4eefcc2352defad23963557f03c877ee516e53651e09943b5c87d3e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_subcontract_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_subcontract_production_agent.py` is
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

Subcontract production Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for subcontract production - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-subcontract-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 1768b894f7265e37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_subcontract_production_agent.py` first:

```bash
python3 dashboard_subcontract_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_subcontract_production_agent.py   # or on stdin
python3 dashboard_subcontract_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract production Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for subcontract production - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-subcontract-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_subcontract_production',
    "version": '2.0.0',
    "display_name": 'Subcontract production Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for subcontract production - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-subcontract-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-subcontract-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a81b70dee073398b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/subcontract-production'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-subcontract-production', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardSubcontractProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSubcontractProduction'
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
    print(DashboardSubcontractProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
