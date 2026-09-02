---
name: "rar-cowork-cookbook-teams-update-identify-business-continuity-risks"
description: "Drafts a Teams channel post on identify business continuity risks status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_business_continuity_risks", "rar_sha256": "5217997c4d7618df5e885d7ec05c122799f0fe78370b355ffeae1bdc74cbb48b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_identify_business_continuity_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-identify-business-continuity-risks:c610f0cb43df95ec03af3e2acad983755a4b57c6d380e9b43f3883d118eaa996", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_identify_business_continuity_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_identify_business_continuity_risks_agent.py` is
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
