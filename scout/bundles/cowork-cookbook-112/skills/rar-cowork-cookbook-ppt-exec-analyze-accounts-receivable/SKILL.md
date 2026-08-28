---
name: "rar-cowork-cookbook-ppt-exec-analyze-accounts-receivable"
description: "Generates an executive-ready PowerPoint deck on analyze accounts receivable status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_accounts_receivable", "rar_sha256": "bdb95713da68eead750bc6bdcea9a05d2156841a4eb49dd5a56e7432abe16b91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 bdb95713da68eead…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_accounts_receivable_agent.py` first:

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
    "version": '2.0.0',
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
