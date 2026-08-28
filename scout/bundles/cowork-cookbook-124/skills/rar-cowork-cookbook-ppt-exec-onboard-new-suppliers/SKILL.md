---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-suppliers"
description: "Generates an executive-ready PowerPoint deck on onboard new suppliers status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_suppliers", "rar_sha256": "bb6f6c55aad62c343d8829fcda4a9b8171ce9b99c2d5b3c7429bd56fb0fe47ec", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_onboard_new_suppliers`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_onboard_new_suppliers_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 bb6f6c55aad62c34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_suppliers_agent.py` first:

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
    "version": '2.0.1',
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
