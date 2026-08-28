---
name: "rar-cowork-cookbook-adaptive-card-allocate-goods"
description: "Produces a reusable Adaptive Card JSON snapshot of allocate goods status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_allocate_goods", "rar_sha256": "a18f1559c1bcec56b16ee76f13987028dddd0ef788ef31438eb4c27bc996adb4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_allocate_goods`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_allocate_goods_agent.py` and in the RCI capsule.

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
