---
name: "rar-cowork-cookbook-demo-data-manage-and-implement-encryption"
description: "Generates and creates realistic demo records for manage and implement encryption in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_and_implement_encryption", "rar_sha256": "ac44f11dfcb851dc5a11564a1065a9241389c21e4c0e90f0eef0b01dce36172f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_and_implement_encryption_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-and-implement-encryption:9d264c646ef700fab900f0c16d03ada70e0ff382f30489c477ae04cd256c4a8e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_and_implement_encryption`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_and_implement_encryption_agent.py` is
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
