---
name: "rar-cowork-cookbook-demo-data-record-asset-lease-right-of-use"
description: "Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_asset_lease_right_of_use", "rar_sha256": "23c24e8f7152d45c5a7e79043aedd81a65b38f81e73890612d489643eccfa21c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 23c24e8f7152d45c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_asset_lease_right_of_use_agent.py` first:

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
    "version": '2.0.0',
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
