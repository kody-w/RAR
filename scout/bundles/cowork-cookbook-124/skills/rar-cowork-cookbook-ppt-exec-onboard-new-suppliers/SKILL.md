---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-suppliers"
description: "Generates an executive-ready PowerPoint deck on onboard new suppliers status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_suppliers", "rar_sha256": "ecd3b37ae8509af718011e7cba828dbf6328e99339bf06125bf65c1387c38366", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_onboard_new_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-onboard-new-suppliers:0e45f646003bfb69163344168b4ed61a16ab6c19161dc0e165fd4d3b9ee94e83", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_onboard_new_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_onboard_new_suppliers_agent.py` is
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

Onboard new suppliers Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on onboard new suppliers status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 ecd3b37ae8509af7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_suppliers_agent.py` first:

```bash
python3 ppt_exec_onboard_new_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_onboard_new_suppliers_agent.py   # or on stdin
python3 ppt_exec_onboard_new_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new suppliers Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on onboard new suppliers status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_onboard_new_suppliers',
    "version": '2.0.0',
    "display_name": 'Onboard new suppliers Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on onboard new suppliers status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-onboard-new-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-onboard-new-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '42a325107f039a81',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/onboard-new-suppliers'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-onboard-new-suppliers', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecOnboardNewSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecOnboardNewSuppliers'
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
    print(PptExecOnboardNewSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
