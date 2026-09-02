---
name: "rar-cowork-cookbook-quote-conversion-funnel"
description: "Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_conversion_funnel", "rar_sha256": "5830d701b2ea70cc0ea7101501a201754646ca024946e95d5ae171c924fc4fdd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "quote_conversion_funnel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/quote-conversion-funnel:7b4889798ba4b78736319c5a3b210cff0e053c16528a39372531a7964b4420c1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/quote_conversion_funnel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `quote_conversion_funnel_agent.py` is
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

Quote Conversion Funnel Analysis (HTML) — Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/quote-conversion-funnel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `quote_conversion_funnel_agent.py` and embedded as the fenced Python below (sha256 5830d701b2ea70cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `quote_conversion_funnel_agent.py` first:

```bash
python3 quote_conversion_funnel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 quote_conversion_funnel_agent.py   # or on stdin
python3 quote_conversion_funnel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quote Conversion Funnel Analysis (HTML) — Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/quote-conversion-funnel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/quote_conversion_funnel',
    "version": '2.0.0',
    "display_name": 'Quote Conversion Funnel Analysis (HTML)',
    "description": 'Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'quote-conversion-funnel',
        "upstream_url": 'https://coworkcookbook.com/recipes/quote-conversion-funnel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c914c9e9393487ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/quote-conversion-funnel', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class QuoteConversionFunnel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'QuoteConversionFunnel'
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
    print(QuoteConversionFunnel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
