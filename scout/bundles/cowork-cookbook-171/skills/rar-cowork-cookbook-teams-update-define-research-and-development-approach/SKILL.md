---
name: "rar-cowork-cookbook-teams-update-define-research-and-development-approach"
description: "Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_research_and_development_approach", "rar_sha256": "501188a747a77adfadc933cb1b2e30e043786866a0a43a1020e771a361991ec3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 501188a747a77adf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_research_and_development_approach_agent.py` first:

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
    "version": '2.0.0',
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
