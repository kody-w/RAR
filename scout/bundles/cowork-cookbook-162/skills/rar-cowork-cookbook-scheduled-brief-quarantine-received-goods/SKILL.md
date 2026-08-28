---
name: "rar-cowork-cookbook-scheduled-brief-quarantine-received-goods"
description: "Schedulable morning-brief email summarizing quarantine received goods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_quarantine_received_goods", "rar_sha256": "50a46d4395c0a78db6e2c56bedf357309d9ffb9e9747c7213da72fa7e3f9721c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 50a46d4395c0a78d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_quarantine_received_goods_agent.py` first:

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
    "version": '2.0.0',
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
