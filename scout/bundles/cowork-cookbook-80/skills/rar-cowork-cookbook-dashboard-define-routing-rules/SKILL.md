---
name: "rar-cowork-cookbook-dashboard-define-routing-rules"
description: "Produces a self-contained interactive HTML dashboard for define routing rules - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_routing_rules", "rar_sha256": "210461c031a617f848f5e5b92ffd89fc1b4d477b3850a92e9a5d0faf0ec227b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_routing_rules_agent.py` and embedded as the fenced Python below (sha256 210461c031a617f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_routing_rules_agent.py` first:

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
    "version": '2.0.0',
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
