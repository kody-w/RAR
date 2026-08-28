---
name: "rar-cowork-cookbook-scheduled-brief-return-goods-to-suppliers"
description: "Schedulable morning-brief email summarizing return goods to suppliers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_return_goods_to_suppliers", "rar_sha256": "16f27320b6093dc8e91e080562da2d7c78280c0ea81560d540f8f91f90ac5db7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
