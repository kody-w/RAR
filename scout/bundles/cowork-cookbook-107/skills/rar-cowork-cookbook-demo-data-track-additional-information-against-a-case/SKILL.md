---
name: "rar-cowork-cookbook-demo-data-track-additional-information-against-a-case"
description: "Generates and creates realistic demo records for track additional information against a case in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_additional_information_against_a_case", "rar_sha256": "444a4b91826be5471802881a52309f1304d6a4096aee2390a90b97b48f5f7158", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_track_additional_information_against_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-track-additional-information-against-a-case:22b03a0e0c70e7dbf1d0ad6724ecdc54ea33a65eb616f57b120689f358663c2b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_track_additional_information_against_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_track_additional_information_against_a_case_agent.py` is
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

Track additional information against a case Demo Data Generator — Generates and creates realistic demo records for track additional information against a case in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 444a4b91826be547…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_additional_information_against_a_case_agent.py` first:

```bash
python3 demo_data_track_additional_information_against_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_additional_information_against_a_case_agent.py   # or on stdin
python3 demo_data_track_additional_information_against_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track additional information against a case Demo Data Generator — Generates and creates realistic demo records for track additional information against a case in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_additional_information_against_a_case',
    "version": '2.0.0',
    "display_name": 'Track additional information against a case Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track additional information against a case in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-additional-information-against-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8d594495244bfec9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/track-additional-information-against-a-case'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-track-additional-information-against-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTrackAdditionalInformationAgainstACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackAdditionalInformationAgainstACase'
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
    print(DemoDataTrackAdditionalInformationAgainstACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
