---
name: "rar-cowork-cookbook-demo-data-develop-product-roadmap"
description: "Generates and creates realistic demo records for develop product roadmap in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_product_roadmap", "rar_sha256": "c903bdbc815fa19b10b51e129769d42097a000d1d3b045d9733b56fed8e59d5b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 c903bdbc815fa19b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_product_roadmap_agent.py` first:

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
    "version": '2.0.0',
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
