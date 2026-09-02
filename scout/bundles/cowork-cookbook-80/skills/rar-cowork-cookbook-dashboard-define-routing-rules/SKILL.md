---
name: "rar-cowork-cookbook-dashboard-define-routing-rules"
description: "Produces a self-contained interactive HTML dashboard for define routing rules - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_routing_rules", "rar_sha256": "210461c031a617f848f5e5b92ffd89fc1b4d477b3850a92e9a5d0faf0ec227b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_routing_rules_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-routing-rules:eca28cf5db6b8033c584c75b94f01acf7929f770bba49db8c4a9432bb0275a01", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_routing_rules`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_routing_rules_agent.py` is
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
