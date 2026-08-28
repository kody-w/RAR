---
name: "rar-cowork-cookbook-scheduled-brief-conduct-research"
description: "Schedulable morning-brief email summarizing conduct research for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_research", "rar_sha256": "5befe67460a0673a4020ba508f7fe19598a89cb55cfc1446e3abbde94b1ab995", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_research_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_research_agent.py` and embedded as the fenced Python below (sha256 5befe67460a0673a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_research_agent.py` first:

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
    "version": '2.0.1',
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
