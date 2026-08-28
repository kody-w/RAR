---
name: "rar-cowork-cookbook-demo-data-manage-and-implement-encryption"
description: "Generates and creates realistic demo records for manage and implement encryption in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_and_implement_encryption", "rar_sha256": "f863d6d54f8aab84fe3dd1381a2b568f1ae10e27adb834955a15fa7d0e264166", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_and_implement_encryption`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_and_implement_encryption_agent.py` and in the RCI capsule.

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

Manage and implement encryption Demo Data Generator — Generates and creates realistic demo records for manage and implement encryption in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-and-implement-encryption
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 f863d6d54f8aab84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_and_implement_encryption_agent.py` first:

```bash
python3 demo_data_manage_and_implement_encryption_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_and_implement_encryption_agent.py   # or on stdin
python3 demo_data_manage_and_implement_encryption_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage and implement encryption Demo Data Generator — Generates and creates realistic demo records for manage and implement encryption in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-and-implement-encryption
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_and_implement_encryption',
    "version": '2.0.1',
    "display_name": 'Manage and implement encryption Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage and implement encryption in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-and-implement-encryption',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-and-implement-encryption',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '61b343d2c5a69a71',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-and-implement-encryption'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-and-implement-encryption', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageAndImplementEncryption(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageAndImplementEncryption'
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
    print(DemoDataManageAndImplementEncryption().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
