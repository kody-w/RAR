---
name: "rar-cowork-cookbook-demo-data-develop-prototypes"
description: "Generates and creates realistic demo records for develop prototypes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_prototypes", "rar_sha256": "04563167abc5b832f1cfee73dae51d2d9f2cd6ba235477516d2e5e012c91dd9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_prototypes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-prototypes:be2d0e03064eca50096db46fcf44f9ff9c31f42c2d8d4b9f797e4e95b8b537b2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_prototypes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_prototypes_agent.py` is
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
