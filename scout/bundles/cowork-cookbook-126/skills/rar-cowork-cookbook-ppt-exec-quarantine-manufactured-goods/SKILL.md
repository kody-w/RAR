---
name: "rar-cowork-cookbook-ppt-exec-quarantine-manufactured-goods"
description: "Generates an executive-ready PowerPoint deck on quarantine manufactured goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_quarantine_manufactured_goods", "rar_sha256": "a34a42d27a5acd9f03a7d9cdfc10ca89a124d9d7b65399e94993ed67f973da16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 a34a42d27a5acd9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_quarantine_manufactured_goods_agent.py` first:

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
    "version": '2.0.0',
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
