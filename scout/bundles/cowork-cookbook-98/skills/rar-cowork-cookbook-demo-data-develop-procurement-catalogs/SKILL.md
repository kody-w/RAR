---
name: "rar-cowork-cookbook-demo-data-develop-procurement-catalogs"
description: "Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_procurement_catalogs", "rar_sha256": "3f83185db7af5c5b424f034b710593bcc670805703d6673e8de2cf1e4ca4dd10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 3f83185db7af5c5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_procurement_catalogs_agent.py` first:

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
    "version": '2.0.0',
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
