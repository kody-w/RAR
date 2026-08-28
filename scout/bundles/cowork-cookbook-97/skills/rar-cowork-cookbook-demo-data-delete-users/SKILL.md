---
name: "rar-cowork-cookbook-demo-data-delete-users"
description: "Generates and creates realistic demo records for delete users in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_delete_users", "rar_sha256": "8a0707a5c46df05b942796b6240ac2b82227efb083480b882362276a14e63ea3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_delete_users_agent.py` and embedded as the fenced Python below (sha256 8a0707a5c46df05b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_delete_users_agent.py` first:

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
    "version": '2.0.0',
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
