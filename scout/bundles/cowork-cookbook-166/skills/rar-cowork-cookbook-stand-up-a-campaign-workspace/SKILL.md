---
name: "rar-cowork-cookbook-stand-up-a-campaign-workspace"
description: "Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_a_campaign_workspace", "rar_sha256": "35eba29ffd98e987ee4f9eb74a5bae0ae286df7ff6e9a499dd002ee7e0f5fa10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_a_campaign_workspace_agent.py` and embedded as the fenced Python below (sha256 35eba29ffd98e987…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_a_campaign_workspace_agent.py` first:

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
    "version": '2.0.0',
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
