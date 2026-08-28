---
name: "rar-cowork-cookbook-account-360-briefing"
description: "Assembles everything Dynamics 365 Sales knows about a named account into a single briefing document you can read before a meeting."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/account_360_briefing", "rar_sha256": "6b90289931e0021b6271b1dde23f85aca32493ba196712c6194fd42c5d99c2b5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `account_360_briefing_agent.py` and embedded as the fenced Python below (sha256 6b90289931e0021b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `account_360_briefing_agent.py` first:

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
    "version": '2.0.1',
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
