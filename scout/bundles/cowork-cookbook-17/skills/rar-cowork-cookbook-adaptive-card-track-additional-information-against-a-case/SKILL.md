---
name: "rar-cowork-cookbook-adaptive-card-track-additional-information-against-a-case"
description: "Produces a reusable Adaptive Card JSON snapshot of track additional information against a case status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_additional_information_against_a_case", "rar_sha256": "c5d0bf1fa62c08b05826ad69a0bac3c2f96e1fd6856875ec491c7757107d8b80", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_additional_information_against_a_case`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_additional_information_against_a_case_agent.py` and in the RCI capsule.

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

Track additional information against a case Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track additional information against a case status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-additional-information-against-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 c5d0bf1fa62c08b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_additional_information_against_a_case_agent.py` first:

```bash
python3 adaptive_card_track_additional_information_against_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_additional_information_against_a_case_agent.py   # or on stdin
python3 adaptive_card_track_additional_information_against_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track additional information against a case Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track additional information against a case status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-additional-information-against-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_additional_information_against_a_case',
    "version": '2.0.1',
    "display_name": 'Track additional information against a case Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of track additional information against a case status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-track-additional-information-against-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-additional-information-against-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19921f398c04c9b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/track-additional-information-against-a-case'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-track-additional-information-against-a-case', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardTrackAdditionalInformationAgainstACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackAdditionalInformationAgainstACase'
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
    print(AdaptiveCardTrackAdditionalInformationAgainstACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
