---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-agents"
description: "Applies a bulk field update across configure and manage agents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_agents", "rar_sha256": "39e65d71d1dc860e69af9ada51b246139d7285c90202ad75633e3fd3fd7dd872", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
