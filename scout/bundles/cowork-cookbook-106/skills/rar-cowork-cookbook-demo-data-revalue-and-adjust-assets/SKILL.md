---
name: "rar-cowork-cookbook-demo-data-revalue-and-adjust-assets"
description: "Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_revalue_and_adjust_assets", "rar_sha256": "dd2201aaffb5423469ce69ed52b2ffa00ec4e7ccc991eb1bce0ff21cbadfec6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 dd2201aaffb54234…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_revalue_and_adjust_assets_agent.py` first:

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
    "version": '2.0.0',
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
