---
name: "rar-cowork-cookbook-teams-update-perform-license-requirements-analysis"
description: "Drafts a Teams channel post on perform license requirements analysis status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_license_requirements_analysis", "rar_sha256": "f3628584b3580db957379f38296a396e94a50f0b1edd9a5b3669c9712c056256", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_perform_license_requirements_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-perform-license-requirements-analysis:7e96f00dfe76a0ed8b780cd9d61d61ff0d8cbbc894de7e732167069d131fdd3e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_perform_license_requirements_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_perform_license_requirements_analysis_agent.py` is
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
