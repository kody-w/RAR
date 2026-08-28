---
name: "rar-cowork-cookbook-demo-data-reopen-a-case"
description: "Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_reopen_a_case", "rar_sha256": "2504b7fda512e3548bb1b7279625ba6cfc6f9d4f39b08c611b3fc907f853208d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_reopen_a_case`. The original RAPP
agent is preserved byte-for-byte in `demo_data_reopen_a_case_agent.py` and in the RCI capsule.

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

Reopen a case Demo Data Generator — Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-reopen-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 2504b7fda512e354…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_reopen_a_case_agent.py` first:

```bash
python3 demo_data_reopen_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_reopen_a_case_agent.py   # or on stdin
python3 demo_data_reopen_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reopen a case Demo Data Generator — Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-reopen-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_reopen_a_case',
    "version": '2.0.1',
    "display_name": 'Reopen a case Demo Data Generator',
    "description": 'Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-reopen-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-reopen-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '667aa2c0f6c9ca7c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/reopen-a-case'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-reopen-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReopenACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReopenACase'
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
    print(DemoDataReopenACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
