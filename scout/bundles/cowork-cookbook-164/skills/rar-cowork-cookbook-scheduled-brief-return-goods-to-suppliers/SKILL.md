---
name: "rar-cowork-cookbook-scheduled-brief-return-goods-to-suppliers"
description: "Schedulable morning-brief email summarizing return goods to suppliers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_return_goods_to_suppliers", "rar_sha256": "16f27320b6093dc8e91e080562da2d7c78280c0ea81560d540f8f91f90ac5db7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_return_goods_to_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-return-goods-to-suppliers:b2ce8cf9ab91d36f4f791d01c4a0e41543a39363846fb15fe6ddaec68d41a963", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_return_goods_to_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_return_goods_to_suppliers_agent.py` is
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

Return goods to suppliers Scheduled Email Brief — Schedulable morning-brief email summarizing return goods to suppliers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-return-goods-to-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_return_goods_to_suppliers_agent.py` and embedded as the fenced Python below (sha256 16f27320b6093dc8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_return_goods_to_suppliers_agent.py` first:

```bash
python3 scheduled_brief_return_goods_to_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_return_goods_to_suppliers_agent.py   # or on stdin
python3 scheduled_brief_return_goods_to_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to suppliers Scheduled Email Brief — Schedulable morning-brief email summarizing return goods to suppliers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-return-goods-to-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_return_goods_to_suppliers',
    "version": '2.0.0',
    "display_name": 'Return goods to suppliers Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing return goods to suppliers for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-return-goods-to-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-return-goods-to-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40d29fac9e80619d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/return-goods-to-suppliers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-return-goods-to-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefReturnGoodsToSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReturnGoodsToSuppliers'
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
    print(ScheduledBriefReturnGoodsToSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
