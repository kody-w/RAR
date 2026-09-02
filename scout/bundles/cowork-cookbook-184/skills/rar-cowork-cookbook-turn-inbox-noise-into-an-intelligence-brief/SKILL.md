---
name: "rar-cowork-cookbook-turn-inbox-noise-into-an-intelligence-brief"
description: "Cut through a week of newsletters to the stories that actually matter to your work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief", "rar_sha256": "516be93d42ea2b0be80566acf353e4fdfff2733151a6abfb36727bf0e9a8688f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "turn_inbox_noise_into_an_intelligence_brief_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/turn-inbox-noise-into-an-intelligence-brief:813d0f7274043afcdff2797cee0fd8f670b684d45416b3a635fba36b18b0efea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "intermediate", "read_only", "automation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `turn_inbox_noise_into_an_intelligence_brief_agent.py` is
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

Turn inbox noise into a curated intelligence brief — Cut through a week of newsletters to the stories that actually matter to your work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-inbox-noise-into-an-intelligence-brief
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_inbox_noise_into_an_intelligence_brief_agent.py` and embedded as the fenced Python below (sha256 516be93d42ea2b0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_inbox_noise_into_an_intelligence_brief_agent.py` first:

```bash
python3 turn_inbox_noise_into_an_intelligence_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_inbox_noise_into_an_intelligence_brief_agent.py   # or on stdin
python3 turn_inbox_noise_into_an_intelligence_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn inbox noise into a curated intelligence brief — Cut through a week of newsletters to the stories that actually matter to your work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-inbox-noise-into-an-intelligence-brief
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief',
    "version": '2.0.0',
    "display_name": 'Turn inbox noise into a curated intelligence brief',
    "description": 'Cut through a week of newsletters to the stories that actually matter to your work.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'work_management', 'intermediate', 'read_only', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'turn-inbox-noise-into-an-intelligence-brief',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-inbox-noise-into-an-intelligence-brief',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '975136ef2dfbc0be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/curate-information-briefs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-inbox-noise-into-an-intelligence-brief', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TurnInboxNoiseIntoAnIntelligenceBrief(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnInboxNoiseIntoAnIntelligenceBrief'
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
    print(TurnInboxNoiseIntoAnIntelligenceBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
