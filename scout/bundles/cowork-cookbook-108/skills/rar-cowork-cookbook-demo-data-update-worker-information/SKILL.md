---
name: "rar-cowork-cookbook-demo-data-update-worker-information"
description: "Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_update_worker_information", "rar_sha256": "2d3874a04f372e320838b95812833da16b32b66d6244586ffbd6acdf9c5a4856", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 2d3874a04f372e32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_update_worker_information_agent.py` first:

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
    "version": '2.0.0',
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
