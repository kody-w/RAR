---
name: "rar-cowork-cookbook-demo-data-define-recovery-objectives"
description: "Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_recovery_objectives", "rar_sha256": "e8f340486f30b7864fdf6fe69a95251002a3b298a42c0c1aa8380c33a2987327", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_recovery_objectives`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_recovery_objectives_agent.py` and in the RCI capsule.

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

Define recovery objectives Demo Data Generator — Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 e8f340486f30b786…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_recovery_objectives_agent.py` first:

```bash
python3 demo_data_define_recovery_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_recovery_objectives_agent.py   # or on stdin
python3 demo_data_define_recovery_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define recovery objectives Demo Data Generator — Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_recovery_objectives',
    "version": '2.0.0',
    "display_name": 'Define recovery objectives Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-define-recovery-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '425a1557d7a88d3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-recovery-objectives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-recovery-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineRecoveryObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineRecoveryObjectives'
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
    print(DemoDataDefineRecoveryObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
