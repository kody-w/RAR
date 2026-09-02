---
name: "rar-cowork-cookbook-quote-aging-and-follow-up"
description: "Lists your outstanding quotes by age, flags the ones past their expiry or overdue for follow-up, and totals the value sitting unanswered."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_aging_and_follow_up", "rar_sha256": "361f6ca455b56cba62caf585a8468d468bb60ab7f5181257fab8910b80d459ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "quote_aging_and_follow_up_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/quote-aging-and-follow-up:64b012e9764b0f09fb0455a6899a7b908abf06128feef6f861476958ebf92c74", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/quote_aging_and_follow_up`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `quote_aging_and_follow_up_agent.py` is
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
