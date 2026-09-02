---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-agents"
description: "Applies a bulk field update across configure and manage agents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_agents", "rar_sha256": "39e65d71d1dc860e69af9ada51b246139d7285c90202ad75633e3fd3fd7dd872", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_configure_and_manage_agents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-configure-and-manage-agents:4c65df6684c91ef2b9745e3f7cec5e83b989eb0e7861fe23a784e065898c4e77", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_configure_and_manage_agents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_configure_and_manage_agents_agent.py` is
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

Configure and manage agents Bulk Field Update — Applies a bulk field update across configure and manage agents records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-agents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_manage_agents_agent.py` and embedded as the fenced Python below (sha256 39e65d71d1dc860e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_manage_agents_agent.py` first:

```bash
python3 bulk_update_configure_and_manage_agents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_manage_agents_agent.py   # or on stdin
python3 bulk_update_configure_and_manage_agents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage agents Bulk Field Update — Applies a bulk field update across configure and manage agents records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-agents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_manage_agents',
    "version": '2.0.0',
    "display_name": 'Configure and manage agents Bulk Field Update',
    "description": 'Applies a bulk field update across configure and manage agents records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-configure-and-manage-agents',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-agents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31a6320d1aa14cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-agents'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-manage-agents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConfigureAndManageAgents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManageAgents'
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
    print(BulkUpdateConfigureAndManageAgents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
