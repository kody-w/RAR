---
name: "rar-cowork-cookbook-adaptive-card-track-additional-information-against-a-case"
description: "Produces a reusable Adaptive Card JSON snapshot of track additional information against a case status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_additional_information_against_a_case", "rar_sha256": "92d617fc3a44c443d5adb175865e5222d1ba8c0c4d8442bc9f7e51f951039bf1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_track_additional_information_against_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-track-additional-information-against-a-case:f3f3cf22cca75a1c64cfa7f6f52422397da1f2df07e168321b64d10b3c40f56a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_track_additional_information_against_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_track_additional_information_against_a_case_agent.py` is
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
