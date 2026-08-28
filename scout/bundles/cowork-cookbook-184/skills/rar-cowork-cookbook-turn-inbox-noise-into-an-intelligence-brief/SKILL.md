---
name: "rar-cowork-cookbook-turn-inbox-noise-into-an-intelligence-brief"
description: "Cut through a week of newsletters to the stories that actually matter to your work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief", "rar_sha256": "516be93d42ea2b0be80566acf353e4fdfff2733151a6abfb36727bf0e9a8688f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "intermediate", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief`. The original RAPP
agent is preserved byte-for-byte in `turn_inbox_noise_into_an_intelligence_brief_agent.py` and in the RCI capsule.

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
