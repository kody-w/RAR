---
name: "rar-cowork-cookbook-bulk-update-manage-authentication"
description: "Applies a bulk field update across manage authentication records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_authentication", "rar_sha256": "4f9d0ff585e0456c19e782d715153b11e894fa77e7bb7713319ea6ea0569fd9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_authentication_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-authentication:875bd6270b260b5ff357cf91684881e3b6f5318309839212e2f83ebf602089e4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_authentication`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_authentication_agent.py` is
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

Manage authentication Bulk Field Update — Applies a bulk field update across manage authentication records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-authentication
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 4f9d0ff585e0456c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_authentication_agent.py` first:

```bash
python3 bulk_update_manage_authentication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_authentication_agent.py   # or on stdin
python3 bulk_update_manage_authentication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage authentication Bulk Field Update — Applies a bulk field update across manage authentication records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-authentication
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_authentication',
    "version": '2.0.0',
    "display_name": 'Manage authentication Bulk Field Update',
    "description": 'Applies a bulk field update across manage authentication records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-manage-authentication',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-authentication',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9497497e00ec50d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-authentication'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-authentication', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageAuthentication(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageAuthentication'
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
    print(BulkUpdateManageAuthentication().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
