---
name: "rar-cowork-cookbook-scheduled-brief-analyze-knowledge-base-usage"
description: "Schedulable morning-brief email summarizing analyze knowledge base usage for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage", "rar_sha256": "41ccb25544809711232ed8593cb5aee7ac186bbf8e4bd1d93af1836e9215f3ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_knowledge_base_usage_agent.py` and in the RCI capsule.

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
