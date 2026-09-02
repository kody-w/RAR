---
name: "rar-cowork-cookbook-scheduled-brief-perform-license-requirements-analysis"
description: "Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis", "rar_sha256": "e6b05bc104cb1be26efe0f85f39c631590c9334e3522583f3b313904961e6207", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_perform_license_requirements_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-perform-license-requirements-analysis:e594e8160c48f241cb2e66a47d651a0fccdfcfd61f6f3142329989c378ce3016", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_perform_license_requirements_analysis_agent.py` is
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

Perform license requirements analysis Scheduled Email Brief — Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_license_requirements_analysis_agent.py` and embedded as the fenced Python below (sha256 e6b05bc104cb1be2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_license_requirements_analysis_agent.py` first:

```bash
python3 scheduled_brief_perform_license_requirements_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_license_requirements_analysis_agent.py   # or on stdin
python3 scheduled_brief_perform_license_requirements_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform license requirements analysis Scheduled Email Brief — Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis',
    "version": '2.0.0',
    "display_name": 'Perform license requirements analysis Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-license-requirements-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5bd46b873664530e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/perform-license-requirements-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-perform-license-requirements-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPerformLicenseRequirementsAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformLicenseRequirementsAnalysis'
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
    print(ScheduledBriefPerformLicenseRequirementsAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
