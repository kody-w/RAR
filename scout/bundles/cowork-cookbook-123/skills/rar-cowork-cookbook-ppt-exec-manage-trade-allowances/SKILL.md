---
name: "rar-cowork-cookbook-ppt-exec-manage-trade-allowances"
description: "Generates an executive-ready PowerPoint deck on manage trade allowances status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_trade_allowances", "rar_sha256": "b027249edeee3b1cc616f0a55b7c945d4e662387093ca195abe18a328c5ec4bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 b027249edeee3b1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_trade_allowances_agent.py` first:

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
    "version": '2.0.0',
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
