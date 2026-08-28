---
name: "rar-cowork-cookbook-scheduled-brief-capture-details-about-a-case"
description: "Schedulable morning-brief email summarizing capture details about a case for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_capture_details_about_a_case", "rar_sha256": "d4c6adc65589f37ef0e63d648c16ab6545e8c27303af4d51c95da3dfe9881b1b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 d4c6adc65589f37e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_capture_details_about_a_case_agent.py` first:

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
    "version": '2.0.0',
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
