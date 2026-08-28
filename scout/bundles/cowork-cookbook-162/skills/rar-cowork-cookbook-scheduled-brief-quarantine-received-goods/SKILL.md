---
name: "rar-cowork-cookbook-scheduled-brief-quarantine-received-goods"
description: "Schedulable morning-brief email summarizing quarantine received goods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_quarantine_received_goods", "rar_sha256": "2a2bb03f27f5a8e350d2a96b1a107c170f5f03c696b9a373555a9683a9d4804d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_quarantine_received_goods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_quarantine_received_goods_agent.py` and in the RCI capsule.

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

Quarantine received goods Scheduled Email Brief — Schedulable morning-brief email summarizing quarantine received goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-quarantine-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 2a2bb03f27f5a8e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_quarantine_received_goods_agent.py` first:

```bash
python3 scheduled_brief_quarantine_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_quarantine_received_goods_agent.py   # or on stdin
python3 scheduled_brief_quarantine_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine received goods Scheduled Email Brief — Schedulable morning-brief email summarizing quarantine received goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-quarantine-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_quarantine_received_goods',
    "version": '2.0.1',
    "display_name": 'Quarantine received goods Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing quarantine received goods for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-quarantine-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-quarantine-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8d03978679218fed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/quarantine-received-goods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-quarantine-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefQuarantineReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefQuarantineReceivedGoods'
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
    print(ScheduledBriefQuarantineReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
