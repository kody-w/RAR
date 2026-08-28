---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-suppliers"
description: "Generates an executive-ready PowerPoint deck on onboard new suppliers status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_suppliers", "rar_sha256": "ecd3b37ae8509af718011e7cba828dbf6328e99339bf06125bf65c1387c38366", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
