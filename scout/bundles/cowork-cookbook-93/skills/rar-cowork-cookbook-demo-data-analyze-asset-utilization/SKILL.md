---
name: "rar-cowork-cookbook-demo-data-analyze-asset-utilization"
description: "Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_utilization", "rar_sha256": "551d95be8bc0d93906c68b0e3e28d3ee93e4463a4927da2f8af5c690ed51a223", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 551d95be8bc0d939…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_utilization_agent.py` first:

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
    "version": '2.0.0',
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
