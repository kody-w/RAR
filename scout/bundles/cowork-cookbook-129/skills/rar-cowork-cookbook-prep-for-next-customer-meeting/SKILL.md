---
name: "rar-cowork-cookbook-prep-for-next-customer-meeting"
description: "Walk into your next call already knowing the account cold - no scramble through CRM tabs and email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_next_customer_meeting", "rar_sha256": "39769fdbab6ded7312db55e5d89a3b4fc099a6b7154a77bc691ce95e9c9d6e96", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prep_for_next_customer_meeting_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/prep-for-next-customer-meeting:8c0f34320b2d5b0b23a9670709093eeec8faf537ae18128494113ede2322933b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/prep_for_next_customer_meeting`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prep_for_next_customer_meeting_agent.py` is
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

Prep for my next customer meeting — Walk into your next call already knowing the account cold - no scramble through CRM tabs and email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-next-customer-meeting
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_next_customer_meeting_agent.py` and embedded as the fenced Python below (sha256 39769fdbab6ded73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_next_customer_meeting_agent.py` first:

```bash
python3 prep_for_next_customer_meeting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prep_for_next_customer_meeting_agent.py   # or on stdin
python3 prep_for_next_customer_meeting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prep for my next customer meeting — Walk into your next call already knowing the account cold - no scramble through CRM tabs and email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-next-customer-meeting
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prep_for_next_customer_meeting',
    "version": '2.0.0',
    "display_name": 'Prep for my next customer meeting',
    "description": 'Walk into your next call already knowing the account cold - no scramble through CRM tabs and email.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'beginner', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prep-for-next-customer-meeting',
        "upstream_url": 'https://coworkcookbook.com/recipes/prep-for-next-customer-meeting',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2438ecf80198b98a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prep-for-next-customer-meeting', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PrepForNextCustomerMeeting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepForNextCustomerMeeting'
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
    print(PrepForNextCustomerMeeting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
