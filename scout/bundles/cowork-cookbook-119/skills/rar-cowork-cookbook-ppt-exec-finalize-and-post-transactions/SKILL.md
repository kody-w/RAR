---
name: "rar-cowork-cookbook-ppt-exec-finalize-and-post-transactions"
description: "Generates an executive-ready PowerPoint deck on finalize and post transactions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_finalize_and_post_transactions", "rar_sha256": "1bb5bd6ddf75e0e1cc62a4d74aa78007f3e824272a0d9f911711572b3abba855", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 1bb5bd6ddf75e0e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_finalize_and_post_transactions_agent.py` first:

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
    "version": '2.0.0',
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
