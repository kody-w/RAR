---
name: "rar-cowork-cookbook-ppt-exec-handle-quarantine-goods"
description: "Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_quarantine_goods", "rar_sha256": "8968502ee9398b4982f78d4ee848c3e1161615e35f84661517329505d1cf39c0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_handle_quarantine_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_handle_quarantine_goods_agent.py` and in the RCI capsule.

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

Handle quarantine goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 8968502ee9398b49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_quarantine_goods_agent.py` first:

```bash
python3 ppt_exec_handle_quarantine_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_handle_quarantine_goods_agent.py   # or on stdin
python3 ppt_exec_handle_quarantine_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle quarantine goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_handle_quarantine_goods',
    "version": '2.0.1',
    "display_name": 'Handle quarantine goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-handle-quarantine-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7dcaac7889ce705',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/handle-quarantine-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-handle-quarantine-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecHandleQuarantineGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecHandleQuarantineGoods'
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
    print(PptExecHandleQuarantineGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
