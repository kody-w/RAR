---
name: "rar-cowork-cookbook-demo-data-reopen-a-case"
description: "Generates and creates realistic demo records for reopen a case in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_reopen_a_case", "rar_sha256": "77bcace760aad2744760317fb9c49684256b0ca8bebd0c9b3ae023f9c6fa97ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 77bcace760aad274…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_reopen_a_case_agent.py` first:

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
    "version": '2.0.0',
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
