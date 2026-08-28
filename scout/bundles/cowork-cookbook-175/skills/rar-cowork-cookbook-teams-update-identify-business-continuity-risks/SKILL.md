---
name: "rar-cowork-cookbook-teams-update-identify-business-continuity-risks"
description: "Drafts a Teams channel post on identify business continuity risks status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_business_continuity_risks", "rar_sha256": "60220091396cfba236c04a71b64caa09656d6e10928f637b412f4a847ff61057", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_business_continuity_risks`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_business_continuity_risks_agent.py` and in the RCI capsule.

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

Identify business continuity risks Teams Channel Update — Drafts a Teams channel post on identify business continuity risks status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-business-continuity-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_business_continuity_risks_agent.py` and embedded as the fenced Python below (sha256 60220091396cfba2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_business_continuity_risks_agent.py` first:

```bash
python3 teams_update_identify_business_continuity_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_business_continuity_risks_agent.py   # or on stdin
python3 teams_update_identify_business_continuity_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify business continuity risks Teams Channel Update — Drafts a Teams channel post on identify business continuity risks status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-business-continuity-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_business_continuity_risks',
    "version": '2.0.1',
    "display_name": 'Identify business continuity risks Teams Channel Update',
    "description": 'Drafts a Teams channel post on identify business continuity risks status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-identify-business-continuity-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-business-continuity-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b75da058babeecdd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-business-continuity-risks'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-identify-business-continuity-risks', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateIdentifyBusinessContinuityRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyBusinessContinuityRisks'
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
    print(TeamsUpdateIdentifyBusinessContinuityRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
