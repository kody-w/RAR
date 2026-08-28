---
name: "rar-cowork-cookbook-demo-data-record-asset-lease-right-of-use"
description: "Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_asset_lease_right_of_use", "rar_sha256": "e13eeb8c0f522d562a7e8bffd7a9ffcacddad2e7b3947daaa342cb3a5463a162", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_asset_lease_right_of_use`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_asset_lease_right_of_use_agent.py` and in the RCI capsule.

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

Record asset lease right-of-use Demo Data Generator — Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 e13eeb8c0f522d56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_asset_lease_right_of_use_agent.py` first:

```bash
python3 demo_data_record_asset_lease_right_of_use_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_asset_lease_right_of_use_agent.py   # or on stdin
python3 demo_data_record_asset_lease_right_of_use_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record asset lease right-of-use Demo Data Generator — Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_asset_lease_right_of_use',
    "version": '2.0.1',
    "display_name": 'Record asset lease right-of-use Demo Data Generator',
    "description": 'Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-record-asset-lease-right-of-use',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10f595b76f4aad2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-asset-lease-right-of-use'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-record-asset-lease-right-of-use', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataRecordAssetLeaseRightOfUse(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordAssetLeaseRightOfUse'
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
    print(DemoDataRecordAssetLeaseRightOfUse().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
