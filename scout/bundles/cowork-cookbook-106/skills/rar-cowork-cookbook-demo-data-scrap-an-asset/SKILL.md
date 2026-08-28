---
name: "rar-cowork-cookbook-demo-data-scrap-an-asset"
description: "Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_an_asset", "rar_sha256": "14567b7653013a36d8091b607a8c1a3dce3ccaa7181d475298a5ab14c25e63d0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_scrap_an_asset`. The original RAPP
agent is preserved byte-for-byte in `demo_data_scrap_an_asset_agent.py` and in the RCI capsule.

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

Scrap an asset Demo Data Generator — Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 14567b7653013a36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_an_asset_agent.py` first:

```bash
python3 demo_data_scrap_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_scrap_an_asset_agent.py   # or on stdin
python3 demo_data_scrap_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap an asset Demo Data Generator — Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_scrap_an_asset',
    "version": '2.0.1',
    "display_name": 'Scrap an asset Demo Data Generator',
    "description": 'Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-scrap-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-scrap-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81759bb7d868f0bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/scrap-an-asset'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-scrap-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataScrapAnAsset(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataScrapAnAsset'
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
    print(DemoDataScrapAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
