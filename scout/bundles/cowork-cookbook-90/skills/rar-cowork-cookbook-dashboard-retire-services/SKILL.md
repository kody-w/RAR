---
name: "rar-cowork-cookbook-dashboard-retire-services"
description: "Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_services", "rar_sha256": "825663f3752cc3d9fad4915eaa3a518dab94ec3a5f99f7c202202df048a2de27", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_services_agent.py` and embedded as the fenced Python below (sha256 825663f3752cc3d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_services_agent.py` first:

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
    "version": '2.0.1',
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
