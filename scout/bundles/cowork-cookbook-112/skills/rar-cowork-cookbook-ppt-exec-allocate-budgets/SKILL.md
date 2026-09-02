---
name: "rar-cowork-cookbook-ppt-exec-allocate-budgets"
description: "Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_allocate_budgets", "rar_sha256": "95aa0231a754f5af3a778c5c86357ba10e25cef4afd46eb691423cb808f59499", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_allocate_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-allocate-budgets:9405342f7130b2a5357c0de465e484d8cb7cd73128f546277a07d0adf26b6e8a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_allocate_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_allocate_budgets_agent.py` is
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

Allocate budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 95aa0231a754f5af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_allocate_budgets_agent.py` first:

```bash
python3 ppt_exec_allocate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_allocate_budgets_agent.py   # or on stdin
python3 ppt_exec_allocate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_allocate_budgets',
    "version": '2.0.0',
    "display_name": 'Allocate budgets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-allocate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cf00eb39599cf3b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/allocate-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-allocate-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecAllocateBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAllocateBudgets'
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
    print(PptExecAllocateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
