---
name: "rar-cowork-cookbook-scheduled-brief-capture-details-about-a-case"
description: "Schedulable morning-brief email summarizing capture details about a case for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_capture_details_about_a_case", "rar_sha256": "fed48383f42362da33433b941840d91a3dc650d00c2b71af38dba2fc2e1f0e2f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_capture_details_about_a_case`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_capture_details_about_a_case_agent.py` and in the RCI capsule.

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

Capture details about a case Scheduled Email Brief — Schedulable morning-brief email summarizing capture details about a case for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 fed48383f42362da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_capture_details_about_a_case_agent.py` first:

```bash
python3 scheduled_brief_capture_details_about_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_capture_details_about_a_case_agent.py   # or on stdin
python3 scheduled_brief_capture_details_about_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Capture details about a case Scheduled Email Brief — Schedulable morning-brief email summarizing capture details about a case for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_capture_details_about_a_case',
    "version": '2.0.1',
    "display_name": 'Capture details about a case Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing capture details about a case for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-capture-details-about-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9d64c53b0da9301',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/capture-details-about-a-case'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-capture-details-about-a-case', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCaptureDetailsAboutACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCaptureDetailsAboutACase'
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
    print(ScheduledBriefCaptureDetailsAboutACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
