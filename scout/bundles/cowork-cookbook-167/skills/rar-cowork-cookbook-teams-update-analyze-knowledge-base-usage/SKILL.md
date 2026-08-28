---
name: "rar-cowork-cookbook-teams-update-analyze-knowledge-base-usage"
description: "Drafts a Teams channel post on analyze knowledge base usage status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_knowledge_base_usage", "rar_sha256": "26f002c1bc24ff2374ecabda2a265e36c2bf4b60b4368b61ec078e798dde4f10", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_knowledge_base_usage_agent.py` and embedded as the fenced Python below (sha256 26f002c1bc24ff23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_knowledge_base_usage_agent.py` first:

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
    "version": '2.0.1',
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
