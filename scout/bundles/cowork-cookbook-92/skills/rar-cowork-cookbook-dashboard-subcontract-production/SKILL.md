---
name: "rar-cowork-cookbook-dashboard-subcontract-production"
description: "Produces a self-contained interactive HTML dashboard for subcontract production - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_subcontract_production", "rar_sha256": "e84d23bdaad57628f2ae5b97dfebee98029f2136d918d3b0df752be3cd109f47", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_subcontract_production`. The original RAPP
agent is preserved byte-for-byte in `dashboard_subcontract_production_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 e84d23bdaad57628…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_subcontract_production_agent.py` first:

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
    "version": '2.0.1',
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
