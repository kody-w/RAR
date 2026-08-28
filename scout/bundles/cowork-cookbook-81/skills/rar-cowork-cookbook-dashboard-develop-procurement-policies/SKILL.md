---
name: "rar-cowork-cookbook-dashboard-develop-procurement-policies"
description: "Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_procurement_policies", "rar_sha256": "0d755f965ade775a9a99fe24557260cc3fa4bb44eec6f9e7e2995b3b56736cfa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_procurement_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_procurement_policies_agent.py` and in the RCI capsule.

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

Develop procurement policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 0d755f965ade775a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_procurement_policies_agent.py` first:

```bash
python3 dashboard_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_procurement_policies_agent.py   # or on stdin
python3 dashboard_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_procurement_policies',
    "version": '2.0.1',
    "display_name": 'Develop procurement policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a685a2333c559952',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopProcurementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopProcurementPolicies'
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
    print(DashboardDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
