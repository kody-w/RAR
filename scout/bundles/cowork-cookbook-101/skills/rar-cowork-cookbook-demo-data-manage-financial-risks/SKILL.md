---
name: "rar-cowork-cookbook-demo-data-manage-financial-risks"
description: "Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_financial_risks", "rar_sha256": "9f217f8844e605dd8ea205a8cfeb617a5e4b52f410fa5dd719f7a91e0989c966", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_financial_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-financial-risks:c0d569f668aad0c20d6b22f400db26128b53da7b84a971b9de81286996ab99ae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_financial_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_financial_risks_agent.py` is
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

Manage financial risks Demo Data Generator — Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-financial-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 9f217f8844e605dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_financial_risks_agent.py` first:

```bash
python3 demo_data_manage_financial_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_financial_risks_agent.py   # or on stdin
python3 demo_data_manage_financial_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage financial risks Demo Data Generator — Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-financial-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_financial_risks',
    "version": '2.0.0',
    "display_name": 'Manage financial risks Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage financial risks in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-financial-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-financial-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9554c2f8201ad4b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/manage-financial-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-manage-financial-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageFinancialRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageFinancialRisks'
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
    print(DemoDataManageFinancialRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
