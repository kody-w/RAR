---
name: "rar-cowork-cookbook-demo-data-revalue-and-adjust-assets"
description: "Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_revalue_and_adjust_assets", "rar_sha256": "92c51529d6487767d0579bf43e344638709e7e8b47f19d42547bd7c44a8c607d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_revalue_and_adjust_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_revalue_and_adjust_assets_agent.py` and in the RCI capsule.

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

Revalue and adjust assets Demo Data Generator — Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 92c51529d6487767…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_revalue_and_adjust_assets_agent.py` first:

```bash
python3 demo_data_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_revalue_and_adjust_assets_agent.py   # or on stdin
python3 demo_data_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Demo Data Generator — Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_revalue_and_adjust_assets',
    "version": '2.0.1',
    "display_name": 'Revalue and adjust assets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '245435da6cb52210',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataRevalueAndAdjustAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRevalueAndAdjustAssets'
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
    print(DemoDataRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
