---
name: "rar-cowork-cookbook-quote-aging-and-follow-up"
description: "Lists your outstanding quotes by age, flags the ones past their expiry or overdue for follow-up, and totals the value sitting unanswered."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_aging_and_follow_up", "rar_sha256": "95631a6e6f600da8ddec5a965da62049b58dcee867f25f5b822234259d2da353", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/quote_aging_and_follow_up`. The original RAPP
agent is preserved byte-for-byte in `quote_aging_and_follow_up_agent.py` and in the RCI capsule.

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

Quote Aging and Follow-Up Tracker — Lists your outstanding quotes by age, flags the ones past their expiry or overdue for follow-up, and totals the value sitting unanswered.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/quote-aging-and-follow-up
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `quote_aging_and_follow_up_agent.py` and embedded as the fenced Python below (sha256 95631a6e6f600da8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `quote_aging_and_follow_up_agent.py` first:

```bash
python3 quote_aging_and_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 quote_aging_and_follow_up_agent.py   # or on stdin
python3 quote_aging_and_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quote Aging and Follow-Up Tracker — Lists your outstanding quotes by age, flags the ones past their expiry or overdue for follow-up, and totals the value sitting unanswered.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/quote-aging-and-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/quote_aging_and_follow_up',
    "version": '2.0.1',
    "display_name": 'Quote Aging and Follow-Up Tracker',
    "description": 'Lists your outstanding quotes by age, flags the ones past their expiry or overdue for follow-up, and totals the value sitting unanswered.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'quote-aging-and-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/quote-aging-and-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b1c2b414f2038b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/quote-aging-and-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class QuoteAgingAndFollowUp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'QuoteAgingAndFollowUp'
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
    print(QuoteAgingAndFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
