---
name: "rar-cowork-cookbook-teams-update-define-benefit-offerings"
description: "Drafts a Teams channel post on define benefit offerings status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_benefit_offerings", "rar_sha256": "2748a2065eb8f346e5378004c2d88ee3483454481925607aa2a30e09ebded7a1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_benefit_offerings`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_benefit_offerings_agent.py` and in the RCI capsule.

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
