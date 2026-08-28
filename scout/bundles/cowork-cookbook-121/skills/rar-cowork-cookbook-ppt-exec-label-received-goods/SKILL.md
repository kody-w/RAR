---
name: "rar-cowork-cookbook-ppt-exec-label-received-goods"
description: "Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_label_received_goods", "rar_sha256": "3dea183de03d6152f408cd71b6a7f67dc2825fe4079c23711864068ddf42dec2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_label_received_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_label_received_goods_agent.py` and in the RCI capsule.

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

Label received goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 3dea183de03d6152…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_label_received_goods_agent.py` first:

```bash
python3 ppt_exec_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_label_received_goods_agent.py   # or on stdin
python3 ppt_exec_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_label_received_goods',
    "version": '2.0.1',
    "display_name": 'Label received goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2d2caad3af5620a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecLabelReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecLabelReceivedGoods'
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
    print(PptExecLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
