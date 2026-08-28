---
name: "rar-cowork-cookbook-quote-aging-and-follow-up"
description: "Lists your outstanding quotes by age, flags the ones past their expiry or overdue for follow-up, and totals the value sitting unanswered."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_aging_and_follow_up", "rar_sha256": "361f6ca455b56cba62caf585a8468d468bb60ab7f5181257fab8910b80d459ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `quote_aging_and_follow_up_agent.py` and embedded as the fenced Python below (sha256 361f6ca455b56cba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `quote_aging_and_follow_up_agent.py` first:

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
    "version": '2.0.0',
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
