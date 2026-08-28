---
name: "rar-cowork-cookbook-demo-data-manage-and-implement-encryption"
description: "Generates and creates realistic demo records for manage and implement encryption in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_and_implement_encryption", "rar_sha256": "ac44f11dfcb851dc5a11564a1065a9241389c21e4c0e90f0eef0b01dce36172f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 ac44f11dfcb851dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_and_implement_encryption_agent.py` first:

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
    "version": '2.0.0',
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
