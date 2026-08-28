---
name: "rar-cowork-cookbook-demo-data-merge-cases"
description: "Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_merge_cases", "rar_sha256": "ecf7f76578d245210568234cbc781874d0cec8bfd833bf0a5406db3d885b607d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Demo Data Generator — Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_merge_cases_agent.py` and embedded as the fenced Python below (sha256 ecf7f76578d24521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_merge_cases_agent.py` first:

```bash
python3 demo_data_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_merge_cases_agent.py   # or on stdin
python3 demo_data_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Demo Data Generator — Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_merge_cases',
    "version": '2.0.0',
    "display_name": 'Merge cases Demo Data Generator',
    "description": 'Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23620edfb71957ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMergeCases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMergeCases'
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
    print(DemoDataMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
