---
name: "rar-cowork-cookbook-dashboard-finalize-project-contracts"
description: "Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_finalize_project_contracts", "rar_sha256": "9c3d0b8fb35c7163a8b3e00373e28ab61fa3f05a8918d57d2e92292e9df9b1c2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_finalize_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `dashboard_finalize_project_contracts_agent.py` and in the RCI capsule.

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

Finalize project contracts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 9c3d0b8fb35c7163…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_finalize_project_contracts_agent.py` first:

```bash
python3 dashboard_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_finalize_project_contracts_agent.py   # or on stdin
python3 dashboard_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_finalize_project_contracts',
    "version": '2.0.1',
    "display_name": 'Finalize project contracts Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for finalize project contracts - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4dbeaffd4a1eff25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardFinalizeProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardFinalizeProjectContracts'
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
    print(DashboardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
