---
name: "rar-cowork-cookbook-scheduled-brief-analyze-knowledge-base-usage"
description: "Schedulable morning-brief email summarizing analyze knowledge base usage for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_knowledge_base_usage", "rar_sha256": "3b31e4552f7e820c74bf285db5259ec0e7703024e0a964cf02292a8e3527ad31", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_knowledge_base_usage_agent.py` and embedded as the fenced Python below (sha256 3b31e4552f7e820c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_knowledge_base_usage_agent.py` first:

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
    "version": '2.0.1',
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
