---
name: "rar-cowork-cookbook-dashboard-develop-service-policies"
description: "Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_service_policies", "rar_sha256": "bd1fec93f49df4ba3c2d70ee52840796c8702218bc413d42fd2d2c04cca23c46", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_service_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_service_policies_agent.py` and in the RCI capsule.

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

Develop service policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 bd1fec93f49df4ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_service_policies_agent.py` first:

```bash
python3 dashboard_develop_service_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_service_policies_agent.py   # or on stdin
python3 dashboard_develop_service_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_service_policies',
    "version": '2.0.1',
    "display_name": 'Develop service policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-service-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-service-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55ec86ed89e4face',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-service-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopServicePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopServicePolicies'
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
    print(DashboardDevelopServicePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
