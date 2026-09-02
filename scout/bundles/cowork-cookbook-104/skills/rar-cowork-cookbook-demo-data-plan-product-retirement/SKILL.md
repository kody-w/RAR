---
name: "rar-cowork-cookbook-demo-data-plan-product-retirement"
description: "Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_product_retirement", "rar_sha256": "7fae08421e4a34f27c98a2aa6d8ad9cc9104e001c8945e322fb7a6e18b3c3691", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_plan_product_retirement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-plan-product-retirement:27a378a962047d853082144f3621b50bd5e7acb1ce0a4decfdc2b6672f61187a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_plan_product_retirement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_plan_product_retirement_agent.py` is
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

Plan product retirement Demo Data Generator — Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-product-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 7fae08421e4a34f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_product_retirement_agent.py` first:

```bash
python3 demo_data_plan_product_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_product_retirement_agent.py   # or on stdin
python3 demo_data_plan_product_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product retirement Demo Data Generator — Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-product-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_product_retirement',
    "version": '2.0.0',
    "display_name": 'Plan product retirement Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-plan-product-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-product-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bfef5a0875b843bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-retirement'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-plan-product-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPlanProductRetirement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProductRetirement'
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
    print(DemoDataPlanProductRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
