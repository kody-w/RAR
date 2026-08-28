---
name: "rar-cowork-cookbook-dashboard-define-routing-rules"
description: "Produces a self-contained interactive HTML dashboard for define routing rules - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_routing_rules", "rar_sha256": "b6538831ce5b5deee15191d751747bbabfd76d8ecbc722827a61ca79c8736c28", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_routing_rules`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_routing_rules_agent.py` and in the RCI capsule.

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

Define routing rules Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define routing rules - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-routing-rules
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_routing_rules_agent.py` and embedded as the fenced Python below (sha256 b6538831ce5b5dee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_routing_rules_agent.py` first:

```bash
python3 dashboard_define_routing_rules_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_routing_rules_agent.py   # or on stdin
python3 dashboard_define_routing_rules_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define routing rules Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define routing rules - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-routing-rules
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_routing_rules',
    "version": '2.0.1',
    "display_name": 'Define routing rules Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define routing rules - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-routing-rules',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-routing-rules',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93a95a0c44568b22',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-routing-rules'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-define-routing-rules', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardDefineRoutingRules(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineRoutingRules'
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
    print(DashboardDefineRoutingRules().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
