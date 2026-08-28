---
name: "rar-cowork-cookbook-prep-for-next-customer-meeting"
description: "Walk into your next call already knowing the account cold - no scramble through CRM tabs and email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_next_customer_meeting", "rar_sha256": "63282130984dc20fefb6c3e6a51fd8d550b57217cc64148535580b27421be04a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prep_for_next_customer_meeting`. The original RAPP
agent is preserved byte-for-byte in `prep_for_next_customer_meeting_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_next_customer_meeting_agent.py` and embedded as the fenced Python below (sha256 63282130984dc20f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_next_customer_meeting_agent.py` first:

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
    "version": '2.0.1',
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
