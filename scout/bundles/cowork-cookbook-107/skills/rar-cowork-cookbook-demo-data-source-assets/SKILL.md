---
name: "rar-cowork-cookbook-demo-data-source-assets"
description: "Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_source_assets", "rar_sha256": "b9955707403519ae967b9d3c4e84327425028dd9ae32fd1a78f0e1260caed721", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_source_assets_agent.py` and embedded as the fenced Python below (sha256 b9955707403519ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_source_assets_agent.py` first:

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
    "version": '2.0.0',
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
