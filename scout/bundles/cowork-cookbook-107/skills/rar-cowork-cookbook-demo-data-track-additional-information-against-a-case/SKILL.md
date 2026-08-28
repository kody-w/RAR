---
name: "rar-cowork-cookbook-demo-data-track-additional-information-against-a-case"
description: "Generates and creates realistic demo records for track additional information against a case in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_additional_information_against_a_case", "rar_sha256": "444a4b91826be5471802881a52309f1304d6a4096aee2390a90b97b48f5f7158", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
