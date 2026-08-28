---
name: "rar-cowork-cookbook-bulk-update-manage-authentication"
description: "Applies a bulk field update across manage authentication records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_authentication", "rar_sha256": "1ee000ceafef49755eee4363390c477811278da18aec6e89703a89c289e43543", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 1ee000ceafef4975…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_authentication_agent.py` first:

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
    "version": '2.0.1',
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
