---
name: "rar-cowork-cookbook-scheduled-brief-perform-license-requirements-analysis"
description: "Schedulable morning-brief email summarizing perform license requirements analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis", "rar_sha256": "e6b05bc104cb1be26efe0f85f39c631590c9334e3522583f3b313904961e6207", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_license_requirements_analysis_agent.py` and in the RCI capsule.

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
