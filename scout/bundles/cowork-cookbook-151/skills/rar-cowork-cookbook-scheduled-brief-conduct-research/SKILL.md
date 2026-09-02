---
name: "rar-cowork-cookbook-scheduled-brief-conduct-research"
description: "Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_research", "rar_sha256": "3789e0d755f8a80417eaaf867365c0db90f81a5a5bc47e9f0b59eae9e303243e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_conduct_research_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-conduct-research:6cb0bd6f49e091b32c1ddcb189b62ab0ae1897e345815702ede1a0781a71dfda", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_conduct_research`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_conduct_research_agent.py` is
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

Conduct research Scheduled Email Brief — Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-research
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_research_agent.py` and embedded as the fenced Python below (sha256 3789e0d755f8a804…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_research_agent.py` first:

```bash
python3 scheduled_brief_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_research_agent.py   # or on stdin
python3 scheduled_brief_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Scheduled Email Brief — Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_research',
    "version": '2.0.0',
    "display_name": 'Conduct research Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af99ca48f33971cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConductResearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductResearch'
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
    print(ScheduledBriefConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
