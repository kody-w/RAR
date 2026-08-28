---
name: "rar-cowork-cookbook-demo-data-develop-brand-kit"
description: "Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_brand_kit", "rar_sha256": "98cb3c02395682f6fb71b42bf4fd750341f020bf0ae0350e4ac12b081abf343a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_brand_kit`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_brand_kit_agent.py` and in the RCI capsule.

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

Develop brand kit Demo Data Generator — Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-brand-kit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 98cb3c02395682f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_brand_kit_agent.py` first:

```bash
python3 demo_data_develop_brand_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_brand_kit_agent.py   # or on stdin
python3 demo_data_develop_brand_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop brand kit Demo Data Generator — Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-brand-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_brand_kit',
    "version": '2.0.1',
    "display_name": 'Develop brand kit Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-develop-brand-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-brand-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40d440249a059588',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-brand-kit'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-brand-kit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopBrandKit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopBrandKit'
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
    print(DemoDataDevelopBrandKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
