---
name: "rar-cowork-cookbook-demo-data-analyze-asset-utilization"
description: "Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_utilization", "rar_sha256": "93c4b56c6cd7f5e841b420c1efa9862466cd16fff1544ffa915a77e3e1c0f4b3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_asset_utilization`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_asset_utilization_agent.py` and in the RCI capsule.

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

Analyze asset utilization Demo Data Generator — Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 93c4b56c6cd7f5e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_utilization_agent.py` first:

```bash
python3 demo_data_analyze_asset_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_asset_utilization_agent.py   # or on stdin
python3 demo_data_analyze_asset_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset utilization Demo Data Generator — Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_asset_utilization',
    "version": '2.0.1',
    "display_name": 'Analyze asset utilization Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-analyze-asset-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e7e20b22ea04aa6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-utilization'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-analyze-asset-utilization', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeAssetUtilization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAssetUtilization'
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
    print(DemoDataAnalyzeAssetUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
