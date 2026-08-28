---
name: "rar-cowork-cookbook-ppt-exec-update-work-order-details"
description: "Generates an executive-ready PowerPoint deck on update work order details status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_update_work_order_details", "rar_sha256": "3b153d30361261ec4f239f87d9819250523bf325079a316969bf3866f7fb98bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 3b153d30361261ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_update_work_order_details_agent.py` first:

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
    "version": '2.0.0',
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
