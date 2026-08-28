---
name: "rar-cowork-cookbook-demo-data-decommission-assets"
description: "Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_decommission_assets", "rar_sha256": "7c6954bcbdf7c20592569a7a14d8a83541c99826189ce536184c60d4210f60fb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 7c6954bcbdf7c205…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_decommission_assets_agent.py` first:

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
    "version": '2.0.1',
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
