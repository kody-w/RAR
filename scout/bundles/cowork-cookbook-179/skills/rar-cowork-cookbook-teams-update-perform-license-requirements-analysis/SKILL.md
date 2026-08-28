---
name: "rar-cowork-cookbook-teams-update-perform-license-requirements-analysis"
description: "Drafts a Teams channel post on perform license requirements analysis status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_license_requirements_analysis", "rar_sha256": "c2ed6dc93cb0c6f7a220777755431eb37de23b8aebf09854d2a8ea1e62bd2ca3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_perform_license_requirements_analysis_agent.py` and embedded as the fenced Python below (sha256 c2ed6dc93cb0c6f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_perform_license_requirements_analysis_agent.py` first:

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
    "version": '2.0.1',
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
