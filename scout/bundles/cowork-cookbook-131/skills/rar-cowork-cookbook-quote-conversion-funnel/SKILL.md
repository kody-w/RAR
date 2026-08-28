---
name: "rar-cowork-cookbook-quote-conversion-funnel"
description: "Analyzes won/lost/expired sales quotes by salesperson, product family, and reason; produces a funnel chart HTML and a workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_conversion_funnel", "rar_sha256": "5830d701b2ea70cc0ea7101501a201754646ca024946e95d5ae171c924fc4fdd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/quote_conversion_funnel`. The original RAPP
agent is preserved byte-for-byte in `quote_conversion_funnel_agent.py` and in the RCI capsule.

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
