---
name: "rar-cowork-cookbook-scheduled-brief-analyze-knowledge-base-usage"
description: "Schedulable morning-brief email summarizing analyze knowledge base usage for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage", "rar_sha256": "41ccb25544809711232ed8593cb5aee7ac186bbf8e4bd1d93af1836e9215f3ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_knowledge_base_usage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-knowledge-base-usage:6f707bda5294e3a58ce04a723632dccf7e8985189912855f8fff9853ec37661a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_knowledge_base_usage_agent.py` is
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

Analyze knowledge base usage Scheduled Email Brief — Schedulable morning-brief email summarizing analyze knowledge base usage for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-knowledge-base-usage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_knowledge_base_usage_agent.py` and embedded as the fenced Python below (sha256 41ccb25544809711…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_knowledge_base_usage_agent.py` first:

```bash
python3 scheduled_brief_analyze_knowledge_base_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_knowledge_base_usage_agent.py   # or on stdin
python3 scheduled_brief_analyze_knowledge_base_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze knowledge base usage Scheduled Email Brief — Schedulable morning-brief email summarizing analyze knowledge base usage for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-knowledge-base-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage',
    "version": '2.0.0',
    "display_name": 'Analyze knowledge base usage Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze knowledge base usage for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-knowledge-base-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-knowledge-base-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a3716dd62ed1c02',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-knowledge-base-usage'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-analyze-knowledge-base-usage', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefAnalyzeKnowledgeBaseUsage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeKnowledgeBaseUsage'
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
    print(ScheduledBriefAnalyzeKnowledgeBaseUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
