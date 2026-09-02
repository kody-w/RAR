---
name: "rar-cowork-cookbook-scheduled-brief-cross-dock-produced-goods"
description: "Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_cross_dock_produced_goods", "rar_sha256": "d4404811302058a61c14031f21f418a4ca56118b792978fffb5d6a94b587948c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_cross_dock_produced_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-cross-dock-produced-goods:66880ec96a5d11431ba388bb1da3facb6e57cf33d85cb6a59354d924722a4232", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_cross_dock_produced_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_cross_dock_produced_goods_agent.py` is
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

Cross dock produced goods Scheduled Email Brief — Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 d4404811302058a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_cross_dock_produced_goods_agent.py` first:

```bash
python3 scheduled_brief_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_cross_dock_produced_goods_agent.py   # or on stdin
python3 scheduled_brief_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Scheduled Email Brief — Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_cross_dock_produced_goods',
    "version": '2.0.0',
    "display_name": 'Cross dock produced goods Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddff51b800003739',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefCrossDockProducedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCrossDockProducedGoods'
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
    print(ScheduledBriefCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
