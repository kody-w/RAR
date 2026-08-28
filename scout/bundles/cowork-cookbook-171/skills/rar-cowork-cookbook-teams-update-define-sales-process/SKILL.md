---
name: "rar-cowork-cookbook-teams-update-define-sales-process"
description: "Drafts a Teams channel post on define sales process status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_sales_process", "rar_sha256": "80b9e3787c8862fe5e7ff754b0a631841dc5dd30b3e0b7f4b2f439eb85c73ff3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_sales_process_agent.py` and embedded as the fenced Python below (sha256 80b9e3787c8862fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_sales_process_agent.py` first:

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
    "version": '2.0.0',
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
