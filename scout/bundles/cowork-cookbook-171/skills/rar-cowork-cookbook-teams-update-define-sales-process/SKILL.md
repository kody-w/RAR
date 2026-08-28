---
name: "rar-cowork-cookbook-teams-update-define-sales-process"
description: "Drafts a Teams channel post on define sales process status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_sales_process", "rar_sha256": "2224e5b937e8920f8c3544a825c193f7c63c306c09b5affbc7e2bd6fdec964a2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_sales_process`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_sales_process_agent.py` and in the RCI capsule.

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

Define sales process Teams Channel Update — Drafts a Teams channel post on define sales process status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-sales-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_sales_process_agent.py` and embedded as the fenced Python below (sha256 2224e5b937e8920f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_sales_process_agent.py` first:

```bash
python3 teams_update_define_sales_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_sales_process_agent.py   # or on stdin
python3 teams_update_define_sales_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales process Teams Channel Update — Drafts a Teams channel post on define sales process status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-sales-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_sales_process',
    "version": '2.0.1',
    "display_name": 'Define sales process Teams Channel Update',
    "description": 'Drafts a Teams channel post on define sales process status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-sales-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-sales-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0bf152177d37eb54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-process'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-define-sales-process', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineSalesProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineSalesProcess'
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
    print(TeamsUpdateDefineSalesProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
