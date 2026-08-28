---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-agents"
description: "Applies a bulk field update across configure and manage agents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_agents", "rar_sha256": "5ce4703fe853ce358fe4b153585f10373204507c8a8ff896356e4ae4fac98758", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_manage_agents`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_manage_agents_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_manage_agents_agent.py` and embedded as the fenced Python below (sha256 5ce4703fe853ce35…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_manage_agents_agent.py` first:

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
    "version": '2.0.1',
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
