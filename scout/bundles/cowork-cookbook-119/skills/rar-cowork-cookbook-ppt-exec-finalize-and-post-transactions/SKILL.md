---
name: "rar-cowork-cookbook-ppt-exec-finalize-and-post-transactions"
description: "Generates an executive-ready PowerPoint deck on finalize and post transactions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_finalize_and_post_transactions", "rar_sha256": "9c0ed9c8c1da16e8b9804230c59913f71160dbeb723480a0f89722e4fe70ae74", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_finalize_and_post_transactions`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_finalize_and_post_transactions_agent.py` and in the RCI capsule.

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

Finalize and post transactions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on finalize and post transactions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-finalize-and-post-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 9c0ed9c8c1da16e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_finalize_and_post_transactions_agent.py` first:

```bash
python3 ppt_exec_finalize_and_post_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_finalize_and_post_transactions_agent.py   # or on stdin
python3 ppt_exec_finalize_and_post_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize and post transactions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on finalize and post transactions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-finalize-and-post-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_finalize_and_post_transactions',
    "version": '2.0.1',
    "display_name": 'Finalize and post transactions Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on finalize and post transactions status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-finalize-and-post-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-finalize-and-post-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da9a7847b9cf13b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/finalize-and-post-transactions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-finalize-and-post-transactions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecFinalizeAndPostTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecFinalizeAndPostTransactions'
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
    print(PptExecFinalizeAndPostTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
