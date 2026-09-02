---
name: "rar-cowork-cookbook-demo-data-define-sales-teams"
description: "Generates and creates realistic demo records for define sales teams in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_sales_teams", "rar_sha256": "84464542dcdedeb8d853271c57d9a466560061fe68eddfa0f1a5653206a761a1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_sales_teams_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-sales-teams:67979d065b647315a976f8a7076e6c1d2aad0e80b4af04ffd6b4bb53d1b17a14", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_sales_teams`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_sales_teams_agent.py` is
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
