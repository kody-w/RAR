---
name: "rar-cowork-cookbook-demo-data-delete-users"
description: "Generates and creates realistic demo records for delete users in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_delete_users", "rar_sha256": "8a0707a5c46df05b942796b6240ac2b82227efb083480b882362276a14e63ea3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_delete_users_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-delete-users:56e0b88777d25376c751bc7db737ec18fb1137c2d207ab065dd38209bba9bb33", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_delete_users`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_delete_users_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
