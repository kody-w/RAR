---
name: "rar-cowork-cookbook-ppt-exec-update-work-order-details"
description: "Generates an executive-ready PowerPoint deck on update work order details status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_update_work_order_details", "rar_sha256": "3b153d30361261ec4f239f87d9819250523bf325079a316969bf3866f7fb98bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_update_work_order_details_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-update-work-order-details:5de725fdfd89d325b6b38f101193fef69795831186457963816b8fd266decb3d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_update_work_order_details`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_update_work_order_details_agent.py` is
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
