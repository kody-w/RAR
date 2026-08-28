---
name: "rar-cowork-cookbook-demo-data-source-assets"
description: "Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_source_assets", "rar_sha256": "80408e64a725c0a5985a005a23aa5dc2cc12686b4a6fe2cb554e03969eda4032", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_source_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_source_assets_agent.py` and in the RCI capsule.

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

Source assets Demo Data Generator — Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_source_assets_agent.py` and embedded as the fenced Python below (sha256 80408e64a725c0a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_source_assets_agent.py` first:

```bash
python3 demo_data_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_source_assets_agent.py   # or on stdin
python3 demo_data_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Demo Data Generator — Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_source_assets',
    "version": '2.0.1',
    "display_name": 'Source assets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6024437174700283',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataSourceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataSourceAssets'
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
    print(DemoDataSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
