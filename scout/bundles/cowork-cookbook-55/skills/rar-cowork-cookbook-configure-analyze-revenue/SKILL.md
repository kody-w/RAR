---
name: "rar-cowork-cookbook-configure-analyze-revenue"
description: "Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_revenue", "rar_sha256": "44363dc84157ead4f9dbe743e471f7047d7fdc65e347d762a2fae2fa799ce18a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-revenue:5156b62f87aa193c7e4a911e75cc1695a0cf2be5d78886f6c86aff867a430d21", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_revenue_agent.py` is
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

Analyze revenue Configuration Bulk Setup — Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 44363dc84157ead4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_revenue_agent.py` first:

```bash
python3 configure_analyze_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_revenue_agent.py   # or on stdin
python3 configure_analyze_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze revenue Configuration Bulk Setup — Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_revenue',
    "version": '2.0.0',
    "display_name": 'Analyze revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a96a08469286bf6d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-analyze-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeRevenue'
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
    print(ConfigureAnalyzeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
