---
name: "rar-cowork-cookbook-demo-data-manage-service-pricing"
description: "Generates and creates realistic demo records for manage service pricing in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_service_pricing", "rar_sha256": "fc5da88a713765818fdf3aba548bfefe77c04c2b939628c1bd2a3c0ec93357b5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 fc5da88a71376581…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_service_pricing_agent.py` first:

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
    "version": '2.0.1',
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
