---
name: "rar-cowork-cookbook-dashboard-convert-projects-to-fixed-assets"
description: "Produces a self-contained interactive HTML dashboard for convert projects to fixed assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_projects_to_fixed_assets", "rar_sha256": "f85f21437a8b5c36ae077115e00a5fc8f59a82ca375882f2b9a03344f1c60797", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_convert_projects_to_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_convert_projects_to_fixed_assets_agent.py` and in the RCI capsule.

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

Convert projects to fixed assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for convert projects to fixed assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-projects-to-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 f85f21437a8b5c36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_convert_projects_to_fixed_assets_agent.py` first:

```bash
python3 dashboard_convert_projects_to_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_convert_projects_to_fixed_assets_agent.py   # or on stdin
python3 dashboard_convert_projects_to_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert projects to fixed assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for convert projects to fixed assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-projects-to-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_convert_projects_to_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Convert projects to fixed assets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for convert projects to fixed assets - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-convert-projects-to-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-convert-projects-to-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '516678626665d46b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/convert-projects-to-fixed-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-convert-projects-to-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConvertProjectsToFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConvertProjectsToFixedAssets'
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
    print(DashboardConvertProjectsToFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
