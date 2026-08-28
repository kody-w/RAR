---
name: "rar-cowork-cookbook-teams-update-define-research-and-development-approach"
description: "Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_research_and_development_approach", "rar_sha256": "497c9eb0c6b5d427d8d2eb5f830b09b76a02359eb00c553c1f069924847127b2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_research_and_development_approach`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_research_and_development_approach_agent.py` and in the RCI capsule.

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

Define research and development approach Teams Channel Update — Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 497c9eb0c6b5d427…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_research_and_development_approach_agent.py` first:

```bash
python3 teams_update_define_research_and_development_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_research_and_development_approach_agent.py   # or on stdin
python3 teams_update_define_research_and_development_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define research and development approach Teams Channel Update — Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_research_and_development_approach',
    "version": '2.0.1',
    "display_name": 'Define research and development approach Teams Channel Update',
    "description": 'Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-research-and-development-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94e153f3b2d0769b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/define-research-and-development-approach'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-define-research-and-development-approach', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineResearchAndDevelopmentApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineResearchAndDevelopmentApproach'
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
    print(TeamsUpdateDefineResearchAndDevelopmentApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
