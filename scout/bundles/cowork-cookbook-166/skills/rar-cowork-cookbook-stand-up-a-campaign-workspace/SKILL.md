---
name: "rar-cowork-cookbook-stand-up-a-campaign-workspace"
description: "Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_a_campaign_workspace", "rar_sha256": "35eba29ffd98e987ee4f9eb74a5bae0ae286df7ff6e9a499dd002ee7e0f5fa10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "stand_up_a_campaign_workspace_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/stand-up-a-campaign-workspace:d3b7d5ca7b9b99b747e90d697351dc75417df7b8630868e1c385b6d9feb520e4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/stand_up_a_campaign_workspace`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `stand_up_a_campaign_workspace_agent.py` is
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
