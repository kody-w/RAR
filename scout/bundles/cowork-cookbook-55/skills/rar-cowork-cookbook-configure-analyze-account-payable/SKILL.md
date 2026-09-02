---
name: "rar-cowork-cookbook-configure-analyze-account-payable"
description: "Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_account_payable", "rar_sha256": "9a6d355cbe7a8d14f8b8dd980820c460de047c7675eb488fcad373c4535ee2e5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_account_payable_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-account-payable:8739abdcc569f7ad1aa141c61a143142c959adaf6817fd0d6e8383940b55a234", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_account_payable`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_account_payable_agent.py` is
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

Analyze account payable Configuration Bulk Setup — Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 9a6d355cbe7a8d14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_account_payable_agent.py` first:

```bash
python3 configure_analyze_account_payable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_account_payable_agent.py   # or on stdin
python3 configure_analyze_account_payable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze account payable Configuration Bulk Setup — Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_account_payable',
    "version": '2.0.0',
    "display_name": 'Analyze account payable Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-account-payable',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-account-payable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1da31eed370b12ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-account-payable'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-account-payable', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeAccountPayable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAccountPayable'
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
    print(ConfigureAnalyzeAccountPayable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
