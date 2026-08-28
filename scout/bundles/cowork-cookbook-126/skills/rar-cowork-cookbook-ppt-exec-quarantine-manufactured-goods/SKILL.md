---
name: "rar-cowork-cookbook-ppt-exec-quarantine-manufactured-goods"
description: "Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_quarantine_manufactured_goods", "rar_sha256": "f072bc58e2ce2c1cbdf44e76d2a600065d211abde84a7b461c865b0a485cbf68", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_quarantine_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_quarantine_manufactured_goods_agent.py` and in the RCI capsule.

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

Quarantine manufactured goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 f072bc58e2ce2c1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_quarantine_manufactured_goods_agent.py` first:

```bash
python3 ppt_exec_quarantine_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_quarantine_manufactured_goods_agent.py   # or on stdin
python3 ppt_exec_quarantine_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine manufactured goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_quarantine_manufactured_goods',
    "version": '2.0.1',
    "display_name": 'Quarantine manufactured goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-quarantine-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37479011b49685be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/quarantine-manufactured-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-quarantine-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecQuarantineManufacturedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecQuarantineManufacturedGoods'
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
    print(PptExecQuarantineManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
