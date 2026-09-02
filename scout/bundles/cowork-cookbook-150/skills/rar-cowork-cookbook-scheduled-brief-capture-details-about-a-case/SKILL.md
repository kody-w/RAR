---
name: "rar-cowork-cookbook-scheduled-brief-capture-details-about-a-case"
description: "Schedulable morning-brief email summarizing capture details about a case for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_capture_details_about_a_case", "rar_sha256": "d4c6adc65589f37ef0e63d648c16ab6545e8c27303af4d51c95da3dfe9881b1b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_capture_details_about_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-capture-details-about-a-case:1fa2b87d17200e8e6049caf30cbd22fb1a880e6e71d320b6181a0cbda9176484", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_capture_details_about_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_capture_details_about_a_case_agent.py` is
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
