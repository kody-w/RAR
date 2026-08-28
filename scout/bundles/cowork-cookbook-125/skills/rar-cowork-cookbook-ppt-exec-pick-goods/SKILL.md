---
name: "rar-cowork-cookbook-ppt-exec-pick-goods"
description: "Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pick_goods", "rar_sha256": "a6394f774c30b72aaef16f6ebf7d801358032f1233737f26fed221bd337f83d1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_pick_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_pick_goods_agent.py` and in the RCI capsule.

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

Pick goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pick-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pick_goods_agent.py` and embedded as the fenced Python below (sha256 a6394f774c30b72a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pick_goods_agent.py` first:

```bash
python3 ppt_exec_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_pick_goods_agent.py   # or on stdin
python3 ppt_exec_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_pick_goods',
    "version": '2.0.1',
    "display_name": 'Pick goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed2b35a31ac857e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPickGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPickGoods'
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
    print(PptExecPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
