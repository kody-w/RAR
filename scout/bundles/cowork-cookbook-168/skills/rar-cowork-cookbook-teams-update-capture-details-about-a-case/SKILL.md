---
name: "rar-cowork-cookbook-teams-update-capture-details-about-a-case"
description: "Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_capture_details_about_a_case", "rar_sha256": "5176fda4b97810fe61f50368fb5f6dd7aa26bc51f4542bdc3af3d4fe263ebabf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_capture_details_about_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-capture-details-about-a-case:c1fe61c69e5d0663f2a75b478c4232e86d7fd6497e3f90e3ceb21c30f9ef011c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_capture_details_about_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_capture_details_about_a_case_agent.py` is
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

Capture details about a case Teams Channel Update — Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 5176fda4b97810fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_capture_details_about_a_case_agent.py` first:

```bash
python3 teams_update_capture_details_about_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_capture_details_about_a_case_agent.py   # or on stdin
python3 teams_update_capture_details_about_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Capture details about a case Teams Channel Update — Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_capture_details_about_a_case',
    "version": '2.0.0',
    "display_name": 'Capture details about a case Teams Channel Update',
    "description": 'Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-capture-details-about-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6c7ead08e3c572b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/capture-details-about-a-case'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-capture-details-about-a-case', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCaptureDetailsAboutACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCaptureDetailsAboutACase'
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
    print(TeamsUpdateCaptureDetailsAboutACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
