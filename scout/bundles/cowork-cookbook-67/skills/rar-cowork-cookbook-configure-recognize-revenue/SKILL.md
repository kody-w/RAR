---
name: "rar-cowork-cookbook-configure-recognize-revenue"
description: "Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_revenue", "rar_sha256": "b04cb7c51491f2e3c8ac4b01a79a18066f9381395f8d61596a7306d41573cf5b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_recognize_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-recognize-revenue:47537d57e161bd8a0c6a9799ca9e6ab9208f15335fcbeae99bcc0577f1131c39", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_recognize_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_recognize_revenue_agent.py` is
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

Recognize revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 b04cb7c51491f2e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_revenue_agent.py` first:

```bash
python3 configure_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_recognize_revenue_agent.py   # or on stdin
python3 configure_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_recognize_revenue',
    "version": '2.0.0',
    "display_name": 'Recognize revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d9e500aa7ba0505',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRecognizeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecognizeRevenue'
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
    print(ConfigureRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
