---
name: "rar-cowork-cookbook-configure-furlough-workers"
description: "Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_furlough_workers", "rar_sha256": "9de55d9a04d6ab274a6ead3d44a3d6501e048d256023e002eaddd44bb6324544", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_furlough_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-furlough-workers:7c6a7198d0f3cff6da7c268a9bd16607b8a92589e863b683d855bd9064630228", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_furlough_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_furlough_workers_agent.py` is
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

Furlough workers Configuration Bulk Setup — Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-furlough-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 9de55d9a04d6ab27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_furlough_workers_agent.py` first:

```bash
python3 configure_furlough_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_furlough_workers_agent.py   # or on stdin
python3 configure_furlough_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Furlough workers Configuration Bulk Setup — Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-furlough-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_furlough_workers',
    "version": '2.0.0',
    "display_name": 'Furlough workers Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-furlough-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-furlough-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'be24cf5d32508078',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/furlough-workers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-furlough-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureFurloughWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureFurloughWorkers'
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
    print(ConfigureFurloughWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
