---
name: "rar-cowork-cookbook-account-360-briefing"
description: "Assembles everything Dynamics 365 Sales knows about a named account into a single briefing document you can read before a meeting."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/account_360_briefing", "rar_sha256": "8ee31292f79ce49b2e8db5d4558a0af466b628c2ff2dff52bb8ca308cd4f6dd9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/account_360_briefing`. The original RAPP
agent is preserved byte-for-byte in `account_360_briefing_agent.py` and in the RCI capsule.

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
