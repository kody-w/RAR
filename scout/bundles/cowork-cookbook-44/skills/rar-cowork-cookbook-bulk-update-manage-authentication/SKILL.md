---
name: "rar-cowork-cookbook-bulk-update-manage-authentication"
description: "Applies a bulk field update across manage authentication records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_authentication", "rar_sha256": "4f9d0ff585e0456c19e782d715153b11e894fa77e7bb7713319ea6ea0569fd9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_authentication`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_authentication_agent.py` and in the RCI capsule.

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
