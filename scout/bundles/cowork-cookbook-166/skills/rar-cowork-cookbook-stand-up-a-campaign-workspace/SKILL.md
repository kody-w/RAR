---
name: "rar-cowork-cookbook-stand-up-a-campaign-workspace"
description: "Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_a_campaign_workspace", "rar_sha256": "f8b33a458645dc784515755234df00e5a5234f4db2815e4f28175d711d1c8ffd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stand_up_a_campaign_workspace`. The original RAPP
agent is preserved byte-for-byte in `stand_up_a_campaign_workspace_agent.py` and in the RCI capsule.

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

Stand up a campaign workspace — Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-a-campaign-workspace
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_a_campaign_workspace_agent.py` and embedded as the fenced Python below (sha256 f8b33a458645dc78…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_a_campaign_workspace_agent.py` first:

```bash
python3 stand_up_a_campaign_workspace_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stand_up_a_campaign_workspace_agent.py   # or on stdin
python3 stand_up_a_campaign_workspace_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stand up a campaign workspace — Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-a-campaign-workspace
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stand_up_a_campaign_workspace',
    "version": '2.0.1',
    "display_name": 'Stand up a campaign workspace',
    "description": 'Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'stand-up-a-campaign-workspace',
        "upstream_url": 'https://coworkcookbook.com/recipes/stand-up-a-campaign-workspace',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3fcf451ac77ad03',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/stand-up-a-campaign-workspace', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class StandUpACampaignWorkspace(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StandUpACampaignWorkspace'
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
    print(StandUpACampaignWorkspace().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
