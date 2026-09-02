---
name: "rar-cowork-cookbook-dashboard-identify-strategic-initiatives"
description: "Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_strategic_initiatives", "rar_sha256": "1879d9a5d2aa2f702d6f06df68a82d70885214928866005d734a6dd06f3ce0a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_identify_strategic_initiatives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-identify-strategic-initiatives:7b52d3317f2b72180a9862b9ce6d411e791a0a384e47a3b2f8df2e034d1da167", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_identify_strategic_initiatives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_identify_strategic_initiatives_agent.py` is
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

Identify strategic initiatives Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 1879d9a5d2aa2f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_strategic_initiatives_agent.py` first:

```bash
python3 dashboard_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_strategic_initiatives_agent.py   # or on stdin
python3 dashboard_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_strategic_initiatives',
    "version": '2.0.0',
    "display_name": 'Identify strategic initiatives Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad51f0be9fc19d9c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIdentifyStrategicInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyStrategicInitiatives'
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
    print(DashboardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
