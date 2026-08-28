---
name: "rar-cowork-cookbook-demo-data-manage-promissory-notes"
description: "Generates and creates realistic demo records for manage promissory notes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_promissory_notes", "rar_sha256": "cd73c3e8df67b17a22c6d21afaa48b4bf79307dc7e89f60a5e98c59e92fcd313", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_promissory_notes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_promissory_notes_agent.py` and in the RCI capsule.

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
