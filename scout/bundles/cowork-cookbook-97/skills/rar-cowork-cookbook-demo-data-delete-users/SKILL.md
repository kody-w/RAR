---
name: "rar-cowork-cookbook-demo-data-delete-users"
description: "Generates and creates realistic demo records for delete users in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_delete_users", "rar_sha256": "ca9ca9efc096aebc0d8e963ea1940d92c9cbee98bd5f1a46e7f8bfcb08391ad3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_delete_users`. The original RAPP
agent is preserved byte-for-byte in `demo_data_delete_users_agent.py` and in the RCI capsule.

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

Delete users Demo Data Generator — Generates and creates realistic demo records for delete users in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-delete-users
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_delete_users_agent.py` and embedded as the fenced Python below (sha256 ca9ca9efc096aebc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_delete_users_agent.py` first:

```bash
python3 demo_data_delete_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_delete_users_agent.py   # or on stdin
python3 demo_data_delete_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Delete users Demo Data Generator — Generates and creates realistic demo records for delete users in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-delete-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_delete_users',
    "version": '2.0.1',
    "display_name": 'Delete users Demo Data Generator',
    "description": 'Generates and creates realistic demo records for delete users in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-delete-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-delete-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6739b0b7ec67e9ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/delete-users'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-delete-users', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDeleteUsers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDeleteUsers'
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
    print(DemoDataDeleteUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
