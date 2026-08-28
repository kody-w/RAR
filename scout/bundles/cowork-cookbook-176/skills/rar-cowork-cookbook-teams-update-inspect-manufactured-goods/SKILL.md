---
name: "rar-cowork-cookbook-teams-update-inspect-manufactured-goods"
description: "Drafts a Teams channel post on inspect manufactured goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_inspect_manufactured_goods", "rar_sha256": "ce1424896aed2c8203664811f25b51a20103e4dad0cb9cc80b6301008733b8d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_inspect_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 ce1424896aed2c82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_inspect_manufactured_goods_agent.py` first:

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
    "version": '2.0.0',
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
