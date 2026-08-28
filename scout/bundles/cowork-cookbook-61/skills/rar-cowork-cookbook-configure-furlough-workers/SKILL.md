---
name: "rar-cowork-cookbook-configure-furlough-workers"
description: "Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_furlough_workers", "rar_sha256": "9f10188046a36ad880ab69e89f920797223088ef8a7c930529c311b97e352406", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_furlough_workers`. The original RAPP
agent is preserved byte-for-byte in `configure_furlough_workers_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 9f10188046a36ad8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_furlough_workers_agent.py` first:

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
    "version": '2.0.1',
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
