---
name: "rar-cowork-cookbook-dashboard-convert-projects-to-fixed-assets"
description: "Produces a self-contained interactive HTML dashboard for convert projects to fixed assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_projects_to_fixed_assets", "rar_sha256": "0ae95dca49486076eaaa90e03cfdc3d6201e54d52c376a4f3bcb021ba298151b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_convert_projects_to_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-convert-projects-to-fixed-assets:f3b1e24be36e436eca04fa655874fc539295c4ad0da70349ca122fad160bef97", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_convert_projects_to_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_convert_projects_to_fixed_assets_agent.py` is
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
