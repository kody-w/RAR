---
name: "rar-cowork-cookbook-demo-data-develop-product-roadmap"
description: "Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_product_roadmap", "rar_sha256": "0c0aa92ea717ef90abf1b1ad490398b7efb8705e35cea0f60c1cb5fd95fb0233", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_product_roadmap`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_product_roadmap_agent.py` and in the RCI capsule.

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

Develop product roadmap Demo Data Generator — Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 0c0aa92ea717ef90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_product_roadmap_agent.py` first:

```bash
python3 demo_data_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_product_roadmap_agent.py   # or on stdin
python3 demo_data_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Demo Data Generator — Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_product_roadmap',
    "version": '2.0.1',
    "display_name": 'Develop product roadmap Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50578c0979f70e71',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopProductRoadmap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProductRoadmap'
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
    print(DemoDataDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
