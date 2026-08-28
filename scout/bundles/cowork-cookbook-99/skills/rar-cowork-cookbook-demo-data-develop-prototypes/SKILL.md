---
name: "rar-cowork-cookbook-demo-data-develop-prototypes"
description: "Generates and creates realistic demo records for develop prototypes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_prototypes", "rar_sha256": "16415524cf7a13f97c4a52d2fe3df97b06747f2dda4e9f5c253ce16f1b0689b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_prototypes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_prototypes_agent.py` and in the RCI capsule.

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

Develop prototypes Demo Data Generator — Generates and creates realistic demo records for develop prototypes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 16415524cf7a13f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_prototypes_agent.py` first:

```bash
python3 demo_data_develop_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_prototypes_agent.py   # or on stdin
python3 demo_data_develop_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop prototypes Demo Data Generator — Generates and creates realistic demo records for develop prototypes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_prototypes',
    "version": '2.0.1',
    "display_name": 'Develop prototypes Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop prototypes in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-develop-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '659d46e58fdb4ec4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/develop-prototypes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopPrototypes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopPrototypes'
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
    print(DemoDataDevelopPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
