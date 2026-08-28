---
name: "rar-cowork-cookbook-demo-data-manage-data"
description: "Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_data", "rar_sha256": "18b640aff93f1838fa91017497ed3cca3535782236795cc5b7a82dd299961a0f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_data_agent.py` and embedded as the fenced Python below (sha256 18b640aff93f1838…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_data_agent.py` first:

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
    "version": '2.0.0',
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
