---
name: "rar-cowork-cookbook-teams-update-define-benefit-offerings"
description: "Drafts a Teams channel post on define benefit offerings status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_benefit_offerings", "rar_sha256": "e5c45add41ce2e74a7aa870343010d0decfbff6fcacfeae537cc3f63b56349b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_benefit_offerings_agent.py` and embedded as the fenced Python below (sha256 e5c45add41ce2e74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_benefit_offerings_agent.py` first:

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
    "version": '2.0.1',
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
