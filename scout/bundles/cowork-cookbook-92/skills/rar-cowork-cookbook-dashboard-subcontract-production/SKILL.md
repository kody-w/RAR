---
name: "rar-cowork-cookbook-dashboard-subcontract-production"
description: "Produces a self-contained interactive HTML dashboard for subcontract production - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_subcontract_production", "rar_sha256": "1768b894f7265e37724248b9fbc6b022c6f50221c882fc9788e43b106de95752", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
