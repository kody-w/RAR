---
name: "rar-cowork-cookbook-ppt-exec-analyze-accounts-receivable"
description: "Generates an executive-ready PowerPoint deck on analyze accounts receivable status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_accounts_receivable", "rar_sha256": "bdb95713da68eead750bc6bdcea9a05d2156841a4eb49dd5a56e7432abe16b91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_analyze_accounts_receivable_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-analyze-accounts-receivable:1f31eb3f83f6a9008ae8aacc21f4eed3db679ff86412c47db601df769ae93e60", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_analyze_accounts_receivable`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_analyze_accounts_receivable_agent.py` is
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
