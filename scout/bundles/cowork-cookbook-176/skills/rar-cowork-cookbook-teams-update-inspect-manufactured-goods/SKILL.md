---
name: "rar-cowork-cookbook-teams-update-inspect-manufactured-goods"
description: "Drafts a Teams channel post on inspect manufactured goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_inspect_manufactured_goods", "rar_sha256": "ce1424896aed2c8203664811f25b51a20103e4dad0cb9cc80b6301008733b8d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_inspect_manufactured_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-inspect-manufactured-goods:6782d9211b1608f2d74309ab8764bb6358fb0271db971188541dc4b82f72e2c8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_inspect_manufactured_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_inspect_manufactured_goods_agent.py` is
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
