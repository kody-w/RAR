---
name: "rar-cowork-cookbook-demo-data-scrap-an-asset"
description: "Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_an_asset", "rar_sha256": "13ebdae6702a16dc9c525108969694fcb437a3b0274d65f83e6aaff19f6cd873", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 13ebdae6702a16dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_an_asset_agent.py` first:

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
    "version": '2.0.0',
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
