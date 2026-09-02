---
name: "rar-cowork-cookbook-adaptive-card-allocate-goods"
description: "Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_allocate_goods", "rar_sha256": "a18f1559c1bcec56b16ee76f13987028dddd0ef788ef31438eb4c27bc996adb4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_allocate_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-allocate-goods:de40382f11a5ba4b61c97be9cd2ae26bd465d4ba2d74f1b526d5ea0defe9d2f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_allocate_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_allocate_goods_agent.py` is
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

Allocate goods Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-allocate-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_allocate_goods_agent.py` and embedded as the fenced Python below (sha256 a18f1559c1bcec56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_allocate_goods_agent.py` first:

```bash
python3 adaptive_card_allocate_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_allocate_goods_agent.py   # or on stdin
python3 adaptive_card_allocate_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate goods Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-allocate-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_allocate_goods',
    "version": '2.0.0',
    "display_name": 'Allocate goods Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-allocate-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-allocate-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02aa0e3f940f63e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/allocate-goods'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-allocate-goods', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardAllocateGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAllocateGoods'
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
    print(AdaptiveCardAllocateGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
