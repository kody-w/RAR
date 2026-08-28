---
name: "rar-cowork-cookbook-teams-update-perform-license-requirements-analysis"
description: "Drafts a Teams channel post on perform license requirements analysis status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_license_requirements_analysis", "rar_sha256": "f3628584b3580db957379f38296a396e94a50f0b1edd9a5b3669c9712c056256", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_perform_license_requirements_analysis`. The original RAPP
agent is preserved byte-for-byte in `teams_update_perform_license_requirements_analysis_agent.py` and in the RCI capsule.

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

Perform license requirements analysis Teams Channel Update — Drafts a Teams channel post on perform license requirements analysis status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-license-requirements-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_perform_license_requirements_analysis_agent.py` and embedded as the fenced Python below (sha256 f3628584b3580db9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_perform_license_requirements_analysis_agent.py` first:

```bash
python3 teams_update_perform_license_requirements_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_perform_license_requirements_analysis_agent.py   # or on stdin
python3 teams_update_perform_license_requirements_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform license requirements analysis Teams Channel Update — Drafts a Teams channel post on perform license requirements analysis status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-license-requirements-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_perform_license_requirements_analysis',
    "version": '2.0.0',
    "display_name": 'Perform license requirements analysis Teams Channel Update',
    "description": 'Drafts a Teams channel post on perform license requirements analysis status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-perform-license-requirements-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-perform-license-requirements-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1a86bbc20a12c9d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/perform-license-requirements-analysis'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-perform-license-requirements-analysis', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePerformLicenseRequirementsAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePerformLicenseRequirementsAnalysis'
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
    print(TeamsUpdatePerformLicenseRequirementsAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
