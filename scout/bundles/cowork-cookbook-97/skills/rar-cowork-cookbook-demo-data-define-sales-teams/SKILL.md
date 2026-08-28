---
name: "rar-cowork-cookbook-demo-data-define-sales-teams"
description: "Generates and creates realistic demo records for define sales teams in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_sales_teams", "rar_sha256": "67b4b71b9005fc491425951cd5647a92c0e4dd677cc2ebcb9dee5faab267c090", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Demo Data Generator — Generates and creates realistic demo records for define sales teams in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-sales-teams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 67b4b71b9005fc49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_sales_teams_agent.py` first:

```bash
python3 demo_data_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_sales_teams_agent.py   # or on stdin
python3 demo_data_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Demo Data Generator — Generates and creates realistic demo records for define sales teams in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_sales_teams',
    "version": '2.0.1',
    "display_name": 'Define sales teams Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define sales teams in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16f50584532604d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineSalesTeams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineSalesTeams'
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
    print(DemoDataDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
