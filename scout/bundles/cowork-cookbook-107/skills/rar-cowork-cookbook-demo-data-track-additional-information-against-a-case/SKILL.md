---
name: "rar-cowork-cookbook-demo-data-track-additional-information-against-a-case"
description: "Generates and creates realistic demo records for track additional information against a case in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_additional_information_against_a_case", "rar_sha256": "def6fc2da257056950376e0f56964395f161b9eab5a4503f7dd659bcc513dc67", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_additional_information_against_a_case`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_additional_information_against_a_case_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 def6fc2da2570569…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_additional_information_against_a_case_agent.py` first:

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
    "version": '2.0.1',
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
