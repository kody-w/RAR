---
name: "rar-cowork-cookbook-demo-data-manage-promissory-notes"
description: "Generates and creates realistic demo records for manage promissory notes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_promissory_notes", "rar_sha256": "cd73c3e8df67b17a22c6d21afaa48b4bf79307dc7e89f60a5e98c59e92fcd313", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_promissory_notes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-promissory-notes:67e2775051f7a446fb0bde78fc670c2547e1643552cda1866805984d8c2746d9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_promissory_notes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_promissory_notes_agent.py` is
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

Manage promissory notes Demo Data Generator — Generates and creates realistic demo records for manage promissory notes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 cd73c3e8df67b17a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_promissory_notes_agent.py` first:

```bash
python3 demo_data_manage_promissory_notes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_promissory_notes_agent.py   # or on stdin
python3 demo_data_manage_promissory_notes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage promissory notes Demo Data Generator — Generates and creates realistic demo records for manage promissory notes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_promissory_notes',
    "version": '2.0.0',
    "display_name": 'Manage promissory notes Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage promissory notes in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-promissory-notes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'efee26e0bc080c2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/manage-promissory-notes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-manage-promissory-notes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataManagePromissoryNotes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManagePromissoryNotes'
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
    print(DemoDataManagePromissoryNotes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
