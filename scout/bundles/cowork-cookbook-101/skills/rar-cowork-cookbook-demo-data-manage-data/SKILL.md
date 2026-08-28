---
name: "rar-cowork-cookbook-demo-data-manage-data"
description: "Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_data", "rar_sha256": "920cdaaab25da0d9468996fcd7e6946d4a7302d35b38b600058df9dd15bc3551", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_data_agent.py` and in the RCI capsule.

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

Manage data Demo Data Generator — Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_data_agent.py` and embedded as the fenced Python below (sha256 920cdaaab25da0d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_data_agent.py` first:

```bash
python3 demo_data_manage_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_data_agent.py   # or on stdin
python3 demo_data_manage_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data Demo Data Generator — Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_data',
    "version": '2.0.1',
    "display_name": 'Manage data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7eb5736491f16430',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageData'
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
    print(DemoDataManageData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
