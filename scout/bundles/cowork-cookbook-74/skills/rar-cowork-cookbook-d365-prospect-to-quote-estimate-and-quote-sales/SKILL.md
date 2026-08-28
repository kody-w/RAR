---
name: "rar-cowork-cookbook-d365-prospect-to-quote-estimate-and-quote-sales"
description: "A Dynamics 365 F&SCM expert scoped to the Estimate and quote sales area (a level-2 subdomain of Prospect to quote) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales", "rar_sha256": "94920b9fede510ee10b9e5f4c4112f86027cf6f1099e3c4761326c8abde42e2d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` and embedded as the fenced Python below (sha256 94920b9fede510ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` first:

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
    "version": '2.0.0',
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
