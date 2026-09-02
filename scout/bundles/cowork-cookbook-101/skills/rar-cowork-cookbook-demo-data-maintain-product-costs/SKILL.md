---
name: "rar-cowork-cookbook-demo-data-maintain-product-costs"
description: "Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_product_costs", "rar_sha256": "c3a01655635641b863c1169a21fcb613782c3282db877ceaf8540a591e568197", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_maintain_product_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-maintain-product-costs:a5ad569854291b42fa33bfe260e2f103ac098c251adfbcb3d63363228dc9aba1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_maintain_product_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_maintain_product_costs_agent.py` is
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

Maintain product costs Demo Data Generator — Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-product-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 c3a01655635641b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_product_costs_agent.py` first:

```bash
python3 demo_data_maintain_product_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_maintain_product_costs_agent.py   # or on stdin
python3 demo_data_maintain_product_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain product costs Demo Data Generator — Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-product-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_maintain_product_costs',
    "version": '2.0.0',
    "display_name": 'Maintain product costs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-maintain-product-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-maintain-product-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '213e696742c445b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/maintain-product-costs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-maintain-product-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMaintainProductCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMaintainProductCosts'
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
    print(DemoDataMaintainProductCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
