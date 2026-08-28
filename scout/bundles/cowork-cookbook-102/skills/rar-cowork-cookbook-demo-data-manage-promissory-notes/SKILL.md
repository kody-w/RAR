---
name: "rar-cowork-cookbook-demo-data-manage-promissory-notes"
description: "Generates and creates realistic demo records for manage promissory notes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_promissory_notes", "rar_sha256": "93fad87255161a4c777e24f3bb75ca39df7887707f8f01aaa0483395c06b5ab8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 93fad87255161a4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_promissory_notes_agent.py` first:

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
    "version": '2.0.1',
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
