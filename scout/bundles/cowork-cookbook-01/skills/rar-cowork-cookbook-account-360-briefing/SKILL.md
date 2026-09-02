---
name: "rar-cowork-cookbook-account-360-briefing"
description: "Assembles everything Dynamics 365 Sales knows about a named account into a single briefing document you can read before a meeting."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/account_360_briefing", "rar_sha256": "8ee31292f79ce49b2e8db5d4558a0af466b628c2ff2dff52bb8ca308cd4f6dd9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "account_360_briefing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/account-360-briefing:f7b2a437a8c6ca0748c29c434207fdcb58bca6c2fb533295e32e35dccfc4a867", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/account_360_briefing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `account_360_briefing_agent.py` is
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

Account 360 Briefing Pack — Assembles everything Dynamics 365 Sales knows about a named account into a single briefing document you can read before a meeting.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/account-360-briefing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `account_360_briefing_agent.py` and embedded as the fenced Python below (sha256 8ee31292f79ce49b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `account_360_briefing_agent.py` first:

```bash
python3 account_360_briefing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 account_360_briefing_agent.py   # or on stdin
python3 account_360_briefing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Account 360 Briefing Pack — Assembles everything Dynamics 365 Sales knows about a named account into a single briefing document you can read before a meeting.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/account-360-briefing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/account_360_briefing',
    "version": '2.0.0',
    "display_name": 'Account 360 Briefing Pack',
    "description": 'Assembles everything Dynamics 365 Sales knows about a named account into a single briefing document you can read before a meeting.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'account-360-briefing',
        "upstream_url": 'https://coworkcookbook.com/recipes/account-360-briefing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4bf8117712cb471',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/account-360-briefing', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class Account360Briefing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'Account360Briefing'
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
    print(Account360Briefing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
