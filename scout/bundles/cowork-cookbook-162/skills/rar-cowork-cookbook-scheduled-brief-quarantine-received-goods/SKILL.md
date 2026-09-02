---
name: "rar-cowork-cookbook-scheduled-brief-quarantine-received-goods"
description: "Schedulable morning-brief email summarizing quarantine received goods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_quarantine_received_goods", "rar_sha256": "50a46d4395c0a78db6e2c56bedf357309d9ffb9e9747c7213da72fa7e3f9721c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_quarantine_received_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-quarantine-received-goods:518c07724978388b5829be669452b459746e5d7e874227af3c2ce99a5fb3f159", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_quarantine_received_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_quarantine_received_goods_agent.py` is
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
