---
name: "rar-cowork-cookbook-demo-data-analyze-asset-leases"
description: "Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_leases", "rar_sha256": "d7b8351476427c0f6f0a69afdf36bfc3a73401339545f863168874d60b7eef85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 d7b8351476427c0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_leases_agent.py` first:

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
    "version": '2.0.0',
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
