---
name: "rar-cowork-cookbook-configure-define-posting-policies"
description: "Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_posting_policies", "rar_sha256": "9835b61c526e13885e6f2466bab5b0c56f579e4493e80bc91e40fae8ad1e4287", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_posting_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_define_posting_policies_agent.py` and in the RCI capsule.

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

Define posting policies Configuration Bulk Setup — Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-posting-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 9835b61c526e1388…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_posting_policies_agent.py` first:

```bash
python3 configure_define_posting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_posting_policies_agent.py   # or on stdin
python3 configure_define_posting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define posting policies Configuration Bulk Setup — Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-posting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_posting_policies',
    "version": '2.0.0',
    "display_name": 'Define posting policies Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-posting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-posting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bd7de4a8d7e0be2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-posting-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-define-posting-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefinePostingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefinePostingPolicies'
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
    print(ConfigureDefinePostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
