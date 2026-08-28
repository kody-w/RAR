---
name: "rar-cowork-cookbook-teams-update-inspect-manufactured-goods"
description: "Drafts a Teams channel post on inspect manufactured goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_inspect_manufactured_goods", "rar_sha256": "91fc94df8b884f924e305a34fcad3841f68d00b9cefd5cded3b67b7f83cd6a86", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_inspect_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_inspect_manufactured_goods_agent.py` and in the RCI capsule.

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

Inspect manufactured goods Teams Channel Update — Drafts a Teams channel post on inspect manufactured goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-inspect-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_inspect_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 91fc94df8b884f92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_inspect_manufactured_goods_agent.py` first:

```bash
python3 teams_update_inspect_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_inspect_manufactured_goods_agent.py   # or on stdin
python3 teams_update_inspect_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect manufactured goods Teams Channel Update — Drafts a Teams channel post on inspect manufactured goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-inspect-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_inspect_manufactured_goods',
    "version": '2.0.1',
    "display_name": 'Inspect manufactured goods Teams Channel Update',
    "description": 'Drafts a Teams channel post on inspect manufactured goods status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-inspect-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-inspect-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b830a4deac1f1b5b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/inspect-manufactured-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-inspect-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateInspectManufacturedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateInspectManufacturedGoods'
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
    print(TeamsUpdateInspectManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
