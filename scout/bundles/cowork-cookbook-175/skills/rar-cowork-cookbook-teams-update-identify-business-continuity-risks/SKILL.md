---
name: "rar-cowork-cookbook-teams-update-identify-business-continuity-risks"
description: "Drafts a Teams channel post on identify business continuity risks status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_business_continuity_risks", "rar_sha256": "5217997c4d7618df5e885d7ec05c122799f0fe78370b355ffeae1bdc74cbb48b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_business_continuity_risks_agent.py` and embedded as the fenced Python below (sha256 5217997c4d7618df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_business_continuity_risks_agent.py` first:

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
    "version": '2.0.0',
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
