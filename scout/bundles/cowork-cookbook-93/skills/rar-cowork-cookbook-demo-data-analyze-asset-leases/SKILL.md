---
name: "rar-cowork-cookbook-demo-data-analyze-asset-leases"
description: "Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_leases", "rar_sha256": "a0b3b9f4f1db5087df99b7bb72d7ed36eb3343e0b0bba7525533edcd19a5bfbc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_asset_leases_agent.py` and in the RCI capsule.

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

Analyze asset leases Demo Data Generator — Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 a0b3b9f4f1db5087…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_leases_agent.py` first:

```bash
python3 demo_data_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_asset_leases_agent.py   # or on stdin
python3 demo_data_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Demo Data Generator — Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_asset_leases',
    "version": '2.0.1',
    "display_name": 'Analyze asset leases Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '545fbb21e2912353',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAnalyzeAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAssetLeases'
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
    print(DemoDataAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
