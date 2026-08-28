---
name: "rar-cowork-cookbook-demo-data-define-sales-teams"
description: "Generates and creates realistic demo records for define sales teams in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_sales_teams", "rar_sha256": "84464542dcdedeb8d853271c57d9a466560061fe68eddfa0f1a5653206a761a1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 84464542dcdedeb8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_sales_teams_agent.py` first:

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
    "version": '2.0.0',
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
