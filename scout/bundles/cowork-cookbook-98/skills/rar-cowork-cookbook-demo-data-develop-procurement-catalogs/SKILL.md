---
name: "rar-cowork-cookbook-demo-data-develop-procurement-catalogs"
description: "Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_procurement_catalogs", "rar_sha256": "af70ac1fa809ba1c5fbb6d38115c86261ca1bb750bc5c5a69895b4ef0442dd7b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_procurement_catalogs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_procurement_catalogs_agent.py` and in the RCI capsule.

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

Develop procurement catalogs Demo Data Generator — Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 af70ac1fa809ba1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_procurement_catalogs_agent.py` first:

```bash
python3 demo_data_develop_procurement_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_procurement_catalogs_agent.py   # or on stdin
python3 demo_data_develop_procurement_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement catalogs Demo Data Generator — Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_procurement_catalogs',
    "version": '2.0.1',
    "display_name": 'Develop procurement catalogs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-procurement-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb4b9266c32525ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-catalogs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-develop-procurement-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopProcurementCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProcurementCatalogs'
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
    print(DemoDataDevelopProcurementCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
