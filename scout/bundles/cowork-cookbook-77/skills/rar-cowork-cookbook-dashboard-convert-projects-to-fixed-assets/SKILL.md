---
name: "rar-cowork-cookbook-dashboard-convert-projects-to-fixed-assets"
description: "Produces a self-contained interactive HTML dashboard for convert projects to fixed assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_projects_to_fixed_assets", "rar_sha256": "0ae95dca49486076eaaa90e03cfdc3d6201e54d52c376a4f3bcb021ba298151b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 0ae95dca49486076…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_convert_projects_to_fixed_assets_agent.py` first:

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
    "version": '2.0.0',
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
