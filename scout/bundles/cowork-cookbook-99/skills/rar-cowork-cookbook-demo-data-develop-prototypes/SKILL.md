---
name: "rar-cowork-cookbook-demo-data-develop-prototypes"
description: "Generates and creates realistic demo records for develop prototypes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_prototypes", "rar_sha256": "04563167abc5b832f1cfee73dae51d2d9f2cd6ba235477516d2e5e012c91dd9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 04563167abc5b832…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_prototypes_agent.py` first:

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
    "version": '2.0.0',
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
