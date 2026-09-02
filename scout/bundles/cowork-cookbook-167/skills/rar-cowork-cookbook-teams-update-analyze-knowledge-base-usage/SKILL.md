---
name: "rar-cowork-cookbook-teams-update-analyze-knowledge-base-usage"
description: "Drafts a Teams channel post on analyze knowledge base usage status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_knowledge_base_usage", "rar_sha256": "2d6242b267bfee0cb531a651789a0e0f53b9e011bc857ffe419f673453088471", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_analyze_knowledge_base_usage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-analyze-knowledge-base-usage:108cfae4fbb4f2704eca249ae86bec43df748e3166c261de4d0708752aeb92dd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_analyze_knowledge_base_usage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_analyze_knowledge_base_usage_agent.py` is
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
