---
name: "rar-cowork-cookbook-campaign-narrative-architecture-board"
description: "Turn a campaign narrative into a structured visual the team can pressure-test before any copy gets written - so the story holds together across every audience, channel, and asset."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_narrative_architecture_board", "rar_sha256": "cd11bbd026ebac6308b3cea4564b341615b46400720aedb6c5afbca2c29a7c6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "campaign_narrative_architecture_board_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/campaign-narrative-architecture-board:81828cc3960ce0849496ce617da39d5b3dd46eb37bcf7e63edaa76cb318594e1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "miro"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/campaign_narrative_architecture_board`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `campaign_narrative_architecture_board_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_narrative_architecture_board_agent.py` and embedded as the fenced Python below (sha256 cd11bbd026ebac63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_narrative_architecture_board_agent.py` first:

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
    "version": '2.0.0',
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
