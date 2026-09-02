---
name: "rar-cowork-cookbook-demo-data-consolidate-and-eliminate-financials"
description: "Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_and_eliminate_financials", "rar_sha256": "29f215cf93fd0c17a2e388b0586a6e3f7a8cc5db91499fa74149f6eee2952312", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_consolidate_and_eliminate_financials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-consolidate-and-eliminate-financials:eda86854a41610dbb17d1f3bb5bc1f1e9024afdcc7a5eef9c4ae82703b825510", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_consolidate_and_eliminate_financials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_consolidate_and_eliminate_financials_agent.py` is
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

Consolidate and eliminate financials Demo Data Generator — Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 29f215cf93fd0c17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 demo_data_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 demo_data_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Demo Data Generator — Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_and_eliminate_financials',
    "version": '2.0.0',
    "display_name": 'Consolidate and eliminate financials Demo Data Generator',
    "description": 'Generates and creates realistic demo records for consolidate and eliminate financials in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f35562681ac741e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConsolidateAndEliminateFinancials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateAndEliminateFinancials'
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
    print(DemoDataConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
