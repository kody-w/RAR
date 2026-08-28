---
name: "rar-cowork-cookbook-ppt-exec-manage-store-operations"
description: "Generates an executive-ready PowerPoint deck on manage store operations status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_store_operations", "rar_sha256": "ce1c7e4b0e734d574cd8d106547c19ad65fbdd918182384ed85cdf5ad0fb2adb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
