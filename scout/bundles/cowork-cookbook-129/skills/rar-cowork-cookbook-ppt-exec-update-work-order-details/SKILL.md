---
name: "rar-cowork-cookbook-ppt-exec-update-work-order-details"
description: "Generates an executive-ready PowerPoint deck on update work order details status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_update_work_order_details", "rar_sha256": "0e8c80b5bfa6baf0c7f29c95b5fefb779e5a4a16ed3b0003d441919e68fa173b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_update_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_update_work_order_details_agent.py` and in the RCI capsule.

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

Update work order details Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on update work order details status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-update-work-order-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 0e8c80b5bfa6baf0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_update_work_order_details_agent.py` first:

```bash
python3 ppt_exec_update_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_update_work_order_details_agent.py   # or on stdin
python3 ppt_exec_update_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update work order details Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on update work order details status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-update-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_update_work_order_details',
    "version": '2.0.1',
    "display_name": 'Update work order details Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on update work order details status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-update-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-update-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a365e1a6282c2a0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-work-order-details'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-update-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecUpdateWorkOrderDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecUpdateWorkOrderDetails'
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
    print(PptExecUpdateWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
