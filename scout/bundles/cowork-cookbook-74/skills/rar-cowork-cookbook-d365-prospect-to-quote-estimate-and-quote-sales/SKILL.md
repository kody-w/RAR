---
name: "rar-cowork-cookbook-d365-prospect-to-quote-estimate-and-quote-sales"
description: "A Dynamics 365 F&SCM expert scoped to the Estimate and quote sales area (a level-2 subdomain of Prospect to quote) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales", "rar_sha256": "72ce4cbe6e452bd58d619d8e893ca092683efa65074edb5d08905c642c4a7bff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales`. The original RAPP
agent is preserved byte-for-byte in `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` and in the RCI capsule.

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

D365 Estimate and quote sales Expert — A Dynamics 365 F&SCM expert scoped to the Estimate and quote sales area (a level-2 subdomain of Prospect to quote) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote-estimate-and-quote-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` and embedded as the fenced Python below (sha256 72ce4cbe6e452bd5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` first:

```bash
python3 d365_prospect_to_quote_estimate_and_quote_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_prospect_to_quote_estimate_and_quote_sales_agent.py   # or on stdin
python3 d365_prospect_to_quote_estimate_and_quote_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Estimate and quote sales Expert — A Dynamics 365 F&SCM expert scoped to the Estimate and quote sales area (a level-2 subdomain of Prospect to quote) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote-estimate-and-quote-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales',
    "version": '2.0.1',
    "display_name": 'D365 Estimate and quote sales Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Estimate and quote sales area (a level-2 subdomain of Prospect to quote) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-prospect-to-quote-estimate-and-quote-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-prospect-to-quote-estimate-and-quote-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f137a183d15c28ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'prospect-to-quote/d365-prospect-to-quote-estimate-and-quote-sales', 'uses_skills': {'custom': ['d365-prospect-to-quote-estimate-and-quote-sales'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ProspectToQuoteEstimateAndQuoteSales(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProspectToQuoteEstimateAndQuoteSales'
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
    print(D365ProspectToQuoteEstimateAndQuoteSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
