---
name: "rar-cowork-cookbook-stand-up-an-account-plan-board"
description: "Move from a scattered account plan to a structured working board the full account team can run against."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_an_account_plan_board", "rar_sha256": "b21eefb05b5ed5f1cb631b5ba79e0c2b8f179c1d0e46b6d1d23b0e49665946d4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "stand_up_an_account_plan_board_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/stand-up-an-account-plan-board:42afed95addd231d2e171e6a78cd199156eb5ab15cc89817aa1ad9fafe818184", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/stand_up_an_account_plan_board`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `stand_up_an_account_plan_board_agent.py` is
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

Stand up an account plan board — Move from a scattered account plan to a structured working board the full account team can run against.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_an_account_plan_board_agent.py` and embedded as the fenced Python below (sha256 b21eefb05b5ed5f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_an_account_plan_board_agent.py` first:

```bash
python3 stand_up_an_account_plan_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stand_up_an_account_plan_board_agent.py   # or on stdin
python3 stand_up_an_account_plan_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stand up an account plan board — Move from a scattered account plan to a structured working board the full account team can run against.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stand_up_an_account_plan_board',
    "version": '2.0.0',
    "display_name": 'Stand up an account plan board',
    "description": 'Move from a scattered account plan to a structured working board the full account team can run against.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'stand-up-an-account-plan-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/stand-up-an-account-plan-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b54c1bf96f15e534',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/stand-up-an-account-plan-board', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class StandUpAnAccountPlanBoard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StandUpAnAccountPlanBoard'
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
    print(StandUpAnAccountPlanBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
