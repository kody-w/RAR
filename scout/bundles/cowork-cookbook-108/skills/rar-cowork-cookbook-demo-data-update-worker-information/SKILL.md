---
name: "rar-cowork-cookbook-demo-data-update-worker-information"
description: "Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_update_worker_information", "rar_sha256": "982587aeacf038c2758f4d43c6b8bee5134afe79587de968f4ac6ca044c9ef77", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_update_worker_information`. The original RAPP
agent is preserved byte-for-byte in `demo_data_update_worker_information_agent.py` and in the RCI capsule.

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

Update worker information Demo Data Generator — Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 982587aeacf038c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_update_worker_information_agent.py` first:

```bash
python3 demo_data_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_update_worker_information_agent.py   # or on stdin
python3 demo_data_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Demo Data Generator — Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_update_worker_information',
    "version": '2.0.1',
    "display_name": 'Update worker information Demo Data Generator',
    "description": 'Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac1e81581db13289',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataUpdateWorkerInformation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataUpdateWorkerInformation'
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
    print(DemoDataUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
