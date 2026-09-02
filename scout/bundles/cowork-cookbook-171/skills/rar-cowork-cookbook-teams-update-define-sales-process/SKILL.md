---
name: "rar-cowork-cookbook-teams-update-define-sales-process"
description: "Drafts a Teams channel post on define sales process status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_sales_process", "rar_sha256": "80b9e3787c8862fe5e7ff754b0a631841dc5dd30b3e0b7f4b2f439eb85c73ff3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_sales_process_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-sales-process:e0a1758ac25f08d3ea2ac581952978007de611d782b8ea96f54ae4755140a90c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_sales_process`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_sales_process_agent.py` is
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
