---
name: "rar-cowork-cookbook-dashboard-retire-services"
description: "Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_services", "rar_sha256": "e8920a62d4d1c9faec7d43899c50e036662fd476112f92946a96bca8c15d7fad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_retire_services`. The original RAPP
agent is preserved byte-for-byte in `dashboard_retire_services_agent.py` and in the RCI capsule.

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

Retire services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_services_agent.py` and embedded as the fenced Python below (sha256 e8920a62d4d1c9fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_services_agent.py` first:

```bash
python3 dashboard_retire_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_services_agent.py   # or on stdin
python3 dashboard_retire_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_services',
    "version": '2.0.0',
    "display_name": 'Retire services Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-retire-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '84ce76aebdb86763',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/retire-services'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-retire-services', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRetireServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireServices'
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
    print(DashboardRetireServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
