---
name: "rar-cowork-cookbook-ppt-exec-pick-goods"
description: "Generates an executive-ready PowerPoint deck on pick goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pick_goods", "rar_sha256": "9db7c2224f880d0fd74740a5b3722678515c3b042133b6abf8ab20a66ef5110d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pick_goods_agent.py` and embedded as the fenced Python below (sha256 9db7c2224f880d0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pick_goods_agent.py` first:

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
    "version": '2.0.0',
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
