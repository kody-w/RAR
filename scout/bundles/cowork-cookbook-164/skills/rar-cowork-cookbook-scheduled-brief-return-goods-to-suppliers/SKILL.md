---
name: "rar-cowork-cookbook-scheduled-brief-return-goods-to-suppliers"
description: "Schedulable morning-brief email summarizing return goods to suppliers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_return_goods_to_suppliers", "rar_sha256": "7da7db307252e2de7af262bcd45edb773cc538679fc6e16dcbb2c3e6e95ba3a3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_return_goods_to_suppliers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_return_goods_to_suppliers_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_return_goods_to_suppliers_agent.py` and embedded as the fenced Python below (sha256 7da7db307252e2de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_return_goods_to_suppliers_agent.py` first:

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
    "version": '2.0.1',
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
