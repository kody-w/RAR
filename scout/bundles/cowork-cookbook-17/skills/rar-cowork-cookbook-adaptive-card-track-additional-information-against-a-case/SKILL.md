---
name: "rar-cowork-cookbook-adaptive-card-track-additional-information-against-a-case"
description: "Produces a reusable Adaptive Card JSON snapshot of track additional information against a case status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_additional_information_against_a_case", "rar_sha256": "92d617fc3a44c443d5adb175865e5222d1ba8c0c4d8442bc9f7e51f951039bf1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 92d617fc3a44c443…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_additional_information_against_a_case_agent.py` first:

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
    "version": '2.0.0',
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
