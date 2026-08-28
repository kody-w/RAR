---
name: "rar-cowork-cookbook-demo-data-perform-preventative-maintenance"
description: "Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_perform_preventative_maintenance", "rar_sha256": "5d1c969b6f17401395309c9fa4c760cfcca99f6b375ee6b89b4c07a1d9ca5154", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_perform_preventative_maintenance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_perform_preventative_maintenance_agent.py` and in the RCI capsule.

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

Perform preventative maintenance Demo Data Generator — Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 5d1c969b6f174013…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_perform_preventative_maintenance_agent.py` first:

```bash
python3 demo_data_perform_preventative_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_perform_preventative_maintenance_agent.py   # or on stdin
python3 demo_data_perform_preventative_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform preventative maintenance Demo Data Generator — Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_perform_preventative_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform preventative maintenance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-perform-preventative-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cfaaba227dbd5cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-preventative-maintenance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-perform-preventative-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPerformPreventativeMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPerformPreventativeMaintenance'
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
    print(DemoDataPerformPreventativeMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
