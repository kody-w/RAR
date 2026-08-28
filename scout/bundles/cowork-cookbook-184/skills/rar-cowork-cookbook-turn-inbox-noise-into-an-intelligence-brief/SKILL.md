---
name: "rar-cowork-cookbook-turn-inbox-noise-into-an-intelligence-brief"
description: "Cut through a week of newsletters to the stories that actually matter to your work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_inbox_noise_into_an_intelligence_brief", "rar_sha256": "efb1391aed1a739b4fa40305d79b8bf8acceacdb93baecb99dc5647a9485dcf1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "intermediate", "read_only", "automation"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_inbox_noise_into_an_intelligence_brief_agent.py` and embedded as the fenced Python below (sha256 efb1391aed1a739b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_inbox_noise_into_an_intelligence_brief_agent.py` first:

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
    "version": '2.0.1',
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
