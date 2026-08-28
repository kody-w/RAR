---
name: "rar-cowork-cookbook-scheduled-brief-retire-knowledge-base-articles"
description: "Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles", "rar_sha256": "30deb6641fe728a6aa2ba09e2da8f54f5c25d1ad18bccde60520f7f754073b01", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Retire knowledge base articles Scheduled Email Brief — Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 30deb6641fe728a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_knowledge_base_articles_agent.py` first:

```bash
python3 scheduled_brief_retire_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_knowledge_base_articles_agent.py   # or on stdin
python3 scheduled_brief_retire_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire knowledge base articles Scheduled Email Brief — Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles',
    "version": '2.0.0',
    "display_name": 'Retire knowledge base articles Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-retire-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e074cebdafcd5db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/retire-knowledge-base-articles'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-retire-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefRetireKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireKnowledgeBaseArticles'
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
    print(ScheduledBriefRetireKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
