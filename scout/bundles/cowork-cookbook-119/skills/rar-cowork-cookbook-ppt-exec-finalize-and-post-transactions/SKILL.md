---
name: "rar-cowork-cookbook-ppt-exec-finalize-and-post-transactions"
description: "Generates an executive-ready PowerPoint deck on finalize and post transactions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_finalize_and_post_transactions", "rar_sha256": "1bb5bd6ddf75e0e1cc62a4d74aa78007f3e824272a0d9f911711572b3abba855", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_finalize_and_post_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-finalize-and-post-transactions:921ed31e6b5926ce4cf0d558348a5936f877bf589b116c91fba443f053965db8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_finalize_and_post_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_finalize_and_post_transactions_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
