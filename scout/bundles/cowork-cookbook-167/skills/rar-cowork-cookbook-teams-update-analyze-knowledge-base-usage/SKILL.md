---
name: "rar-cowork-cookbook-teams-update-analyze-knowledge-base-usage"
description: "Drafts a Teams channel post on analyze knowledge base usage status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_knowledge_base_usage", "rar_sha256": "2d6242b267bfee0cb531a651789a0e0f53b9e011bc857ffe419f673453088471", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_knowledge_base_usage`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_knowledge_base_usage_agent.py` and in the RCI capsule.

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

Analyze knowledge base usage Teams Channel Update — Drafts a Teams channel post on analyze knowledge base usage status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-knowledge-base-usage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_knowledge_base_usage_agent.py` and embedded as the fenced Python below (sha256 2d6242b267bfee0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_knowledge_base_usage_agent.py` first:

```bash
python3 teams_update_analyze_knowledge_base_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_knowledge_base_usage_agent.py   # or on stdin
python3 teams_update_analyze_knowledge_base_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze knowledge base usage Teams Channel Update — Drafts a Teams channel post on analyze knowledge base usage status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-knowledge-base-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_knowledge_base_usage',
    "version": '2.0.0',
    "display_name": 'Analyze knowledge base usage Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze knowledge base usage status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-knowledge-base-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-knowledge-base-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d183b1479be8862',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-knowledge-base-usage'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-analyze-knowledge-base-usage', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAnalyzeKnowledgeBaseUsage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeKnowledgeBaseUsage'
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
    print(TeamsUpdateAnalyzeKnowledgeBaseUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
