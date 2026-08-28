---
name: "rar-cowork-cookbook-ppt-exec-analyze-accounts-receivable"
description: "Generates an executive-ready PowerPoint deck on analyze accounts receivable status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_accounts_receivable", "rar_sha256": "8a88b8d4eee8d3fec8a05f1e1daa786c9abfdcd6c74b1a6ba18a661a518a8529", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_accounts_receivable`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_accounts_receivable_agent.py` and in the RCI capsule.

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

Analyze accounts receivable Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze accounts receivable status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-accounts-receivable
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 8a88b8d4eee8d3fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_accounts_receivable_agent.py` first:

```bash
python3 ppt_exec_analyze_accounts_receivable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_accounts_receivable_agent.py   # or on stdin
python3 ppt_exec_analyze_accounts_receivable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze accounts receivable Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze accounts receivable status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-accounts-receivable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_accounts_receivable',
    "version": '2.0.1',
    "display_name": 'Analyze accounts receivable Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on analyze accounts receivable status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-analyze-accounts-receivable',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-accounts-receivable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd6e6ff1b1316c51',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-accounts-receivable'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-analyze-accounts-receivable', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecAnalyzeAccountsReceivable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeAccountsReceivable'
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
    print(PptExecAnalyzeAccountsReceivable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
