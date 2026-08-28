---
name: "rar-cowork-cookbook-demo-data-manage-service-pricing"
description: "Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_service_pricing", "rar_sha256": "aca92e6679888627bf996af9da39192d0ea92ba5d09204f681936cb69aa923f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_service_pricing`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_service_pricing_agent.py` and in the RCI capsule.

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

Manage service pricing Demo Data Generator — Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-service-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 aca92e6679888627…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_service_pricing_agent.py` first:

```bash
python3 demo_data_manage_service_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_service_pricing_agent.py   # or on stdin
python3 demo_data_manage_service_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service pricing Demo Data Generator — Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-service-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_service_pricing',
    "version": '2.0.0',
    "display_name": 'Manage service pricing Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-service-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-service-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa378eb644197120',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-service-pricing'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-manage-service-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageServicePricing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageServicePricing'
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
    print(DemoDataManageServicePricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
