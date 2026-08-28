---
name: "rar-cowork-cookbook-campaign-narrative-architecture-board"
description: "Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_narrative_architecture_board", "rar_sha256": "a051b1df07933c677bdb2f8bcef35a71344b8571af463fb888e75718ff8611db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/campaign_narrative_architecture_board`. The original RAPP
agent is preserved byte-for-byte in `campaign_narrative_architecture_board_agent.py` and in the RCI capsule.

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

Build a campaign narrative architecture board — Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/campaign-narrative-architecture-board
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_narrative_architecture_board_agent.py` and embedded as the fenced Python below (sha256 a051b1df07933c67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_narrative_architecture_board_agent.py` first:

```bash
python3 campaign_narrative_architecture_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_narrative_architecture_board_agent.py   # or on stdin
python3 campaign_narrative_architecture_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a campaign narrative architecture board — Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/campaign-narrative-architecture-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/campaign_narrative_architecture_board',
    "version": '2.0.1',
    "display_name": 'Build a campaign narrative architecture board',
    "description": 'Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'miro'],
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
        "upstream_slug": 'campaign-narrative-architecture-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/campaign-narrative-architecture-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a763243606223948',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/campaign-narrative-architecture-board', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CampaignNarrativeArchitectureBoard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignNarrativeArchitectureBoard'
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
    print(CampaignNarrativeArchitectureBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
