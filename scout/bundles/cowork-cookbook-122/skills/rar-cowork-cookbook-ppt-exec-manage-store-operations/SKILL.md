---
name: "rar-cowork-cookbook-ppt-exec-manage-store-operations"
description: "Generates an executive-ready PowerPoint deck on manage store operations status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_store_operations", "rar_sha256": "ce1c7e4b0e734d574cd8d106547c19ad65fbdd918182384ed85cdf5ad0fb2adb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_store_operations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-store-operations:64f5945ae9f8bb957e5554acd3f933bdacc275808fdf2a8e1895db7bb6cca48a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_store_operations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_store_operations_agent.py` is
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

Manage store operations Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage store operations status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-store-operations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 ce1c7e4b0e734d57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_store_operations_agent.py` first:

```bash
python3 ppt_exec_manage_store_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_store_operations_agent.py   # or on stdin
python3 ppt_exec_manage_store_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage store operations Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage store operations status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-store-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_store_operations',
    "version": '2.0.0',
    "display_name": 'Manage store operations Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage store operations status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-manage-store-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-store-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '553ccd3668f3ee6e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-store-operations'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-manage-store-operations', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageStoreOperations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageStoreOperations'
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
    print(PptExecManageStoreOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
