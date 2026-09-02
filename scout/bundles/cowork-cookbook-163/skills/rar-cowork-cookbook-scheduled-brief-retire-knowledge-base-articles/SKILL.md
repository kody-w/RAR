---
name: "rar-cowork-cookbook-scheduled-brief-retire-knowledge-base-articles"
description: "Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles", "rar_sha256": "30deb6641fe728a6aa2ba09e2da8f54f5c25d1ad18bccde60520f7f754073b01", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_retire_knowledge_base_articles_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-retire-knowledge-base-articles:2130d194f47c371ce553b95dbddbc17e85f82452798e165e2660922a341b9c83", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_retire_knowledge_base_articles_agent.py` is
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
