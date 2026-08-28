---
name: "rar-cowork-cookbook-ppt-exec-manage-trade-allowances"
description: "Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_trade_allowances", "rar_sha256": "492c89ea49d57473f457e286b850b357042c230bb578021e2de8da0b08838111", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_trade_allowances_agent.py` and in the RCI capsule.

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

Manage trade allowances Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 492c89ea49d57473…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_trade_allowances_agent.py` first:

```bash
python3 ppt_exec_manage_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_trade_allowances_agent.py   # or on stdin
python3 ppt_exec_manage_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage trade allowances Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_trade_allowances',
    "version": '2.0.1',
    "display_name": 'Manage trade allowances Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b860577c9b0c2cd8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-trade-allowances'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-manage-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageTradeAllowances(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageTradeAllowances'
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
    print(PptExecManageTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
