---
name: "rar-cowork-cookbook-ppt-exec-manage-store-operations"
description: "Generates an executive-ready PowerPoint deck on manage store operations status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_store_operations", "rar_sha256": "52f301f50172249ee1b8d875f2829c34b04141c019640414aa1d0dd115fb6593", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_store_operations`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_store_operations_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 52f301f50172249e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_store_operations_agent.py` first:

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
    "version": '2.0.1',
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
