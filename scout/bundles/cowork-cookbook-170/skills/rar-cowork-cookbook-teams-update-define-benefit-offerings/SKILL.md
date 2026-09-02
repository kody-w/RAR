---
name: "rar-cowork-cookbook-teams-update-define-benefit-offerings"
description: "Drafts a Teams channel post on define benefit offerings status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_benefit_offerings", "rar_sha256": "2748a2065eb8f346e5378004c2d88ee3483454481925607aa2a30e09ebded7a1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_benefit_offerings_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-benefit-offerings:5075310dd741ecc5be34c59445e4934158d710d3942ba6eca71aa05247615bbd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_benefit_offerings`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_benefit_offerings_agent.py` is
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

Define benefit offerings Teams Channel Update — Drafts a Teams channel post on define benefit offerings status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-benefit-offerings
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_benefit_offerings_agent.py` and embedded as the fenced Python below (sha256 2748a2065eb8f346…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_benefit_offerings_agent.py` first:

```bash
python3 teams_update_define_benefit_offerings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_benefit_offerings_agent.py   # or on stdin
python3 teams_update_define_benefit_offerings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define benefit offerings Teams Channel Update — Drafts a Teams channel post on define benefit offerings status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-benefit-offerings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_benefit_offerings',
    "version": '2.0.0',
    "display_name": 'Define benefit offerings Teams Channel Update',
    "description": 'Drafts a Teams channel post on define benefit offerings status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-benefit-offerings',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-benefit-offerings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '92fb1bcaccc0522b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-benefit-offerings'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-define-benefit-offerings', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineBenefitOfferings(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineBenefitOfferings'
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
    print(TeamsUpdateDefineBenefitOfferings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
