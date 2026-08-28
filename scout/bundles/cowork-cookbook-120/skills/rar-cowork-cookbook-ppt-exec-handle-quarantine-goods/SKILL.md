---
name: "rar-cowork-cookbook-ppt-exec-handle-quarantine-goods"
description: "Generates an executive-ready PowerPoint deck on handle quarantine goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_quarantine_goods", "rar_sha256": "e15f9c6193e8a3375002313e7c9dc28b2c42d58a879922cdf26f10ffbcb0d011", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 e15f9c6193e8a337…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_quarantine_goods_agent.py` first:

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
    "version": '2.0.0',
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
