---
name: "rar-cowork-cookbook-demo-data-track-campaign-expenses"
description: "Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_campaign_expenses", "rar_sha256": "78f4c9408ed2b328cbf4c90e0e5556db971b03deae1d8024759fd6d6d44acc0c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_campaign_expenses`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_campaign_expenses_agent.py` and in the RCI capsule.

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

Track campaign expenses Demo Data Generator — Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 78f4c9408ed2b328…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_campaign_expenses_agent.py` first:

```bash
python3 demo_data_track_campaign_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_campaign_expenses_agent.py   # or on stdin
python3 demo_data_track_campaign_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track campaign expenses Demo Data Generator — Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_campaign_expenses',
    "version": '2.0.1',
    "display_name": 'Track campaign expenses Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-campaign-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e1c70144438bac5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/track-campaign-expenses'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-track-campaign-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTrackCampaignExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCampaignExpenses'
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
    print(DemoDataTrackCampaignExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
