---
name: "rar-cowork-cookbook-configure-define-posting-policies"
description: "Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_posting_policies", "rar_sha256": "9835b61c526e13885e6f2466bab5b0c56f579e4493e80bc91e40fae8ad1e4287", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_posting_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-posting-policies:4e4d2604cfab9dd760aa8867b7764214e2920be1e98ff9beac1d99d313e0de6b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_posting_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_posting_policies_agent.py` is
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
