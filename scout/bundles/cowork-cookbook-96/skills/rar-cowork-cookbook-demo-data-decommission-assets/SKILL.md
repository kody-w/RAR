---
name: "rar-cowork-cookbook-demo-data-decommission-assets"
description: "Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_decommission_assets", "rar_sha256": "8776a17318a7ed46872d59d14eb7e06c689a4775fe89c7011556202d5e1a7b79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_decommission_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_decommission_assets_agent.py` and in the RCI capsule.

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

Decommission assets Demo Data Generator — Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-decommission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 8776a17318a7ed46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_decommission_assets_agent.py` first:

```bash
python3 demo_data_decommission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_decommission_assets_agent.py   # or on stdin
python3 demo_data_decommission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Decommission assets Demo Data Generator — Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-decommission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_decommission_assets',
    "version": '2.0.0',
    "display_name": 'Decommission assets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-decommission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-decommission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7efcbac5fb26e303',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/decommission-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-decommission-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDecommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDecommissionAssets'
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
    print(DemoDataDecommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
