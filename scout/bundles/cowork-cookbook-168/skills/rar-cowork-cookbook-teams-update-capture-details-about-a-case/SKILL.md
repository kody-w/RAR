---
name: "rar-cowork-cookbook-teams-update-capture-details-about-a-case"
description: "Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_capture_details_about_a_case", "rar_sha256": "40b89195c6ec7519d7c5b96dd3730cea0ec16340129ddb2d0881c21c94408724", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_capture_details_about_a_case`. The original RAPP
agent is preserved byte-for-byte in `teams_update_capture_details_about_a_case_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 40b89195c6ec7519…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_capture_details_about_a_case_agent.py` first:

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
    "version": '2.0.1',
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
