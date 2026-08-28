---
name: "rar-cowork-cookbook-demo-data-perform-preventative-maintenance"
description: "Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_perform_preventative_maintenance", "rar_sha256": "3ee8ac0d6a48234115269cee2ab45e74069b0485ec83bf93f7ba2062f5155bc7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 3ee8ac0d6a482341…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_perform_preventative_maintenance_agent.py` first:

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
    "version": '2.0.1',
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
