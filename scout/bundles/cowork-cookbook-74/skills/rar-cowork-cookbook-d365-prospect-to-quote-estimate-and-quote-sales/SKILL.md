---
name: "rar-cowork-cookbook-d365-prospect-to-quote-estimate-and-quote-sales"
description: "A Dynamics 365 F&SCM expert scoped to the Estimate and quote sales area (a level-2 subdomain of Prospect to quote) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales", "rar_sha256": "94920b9fede510ee10b9e5f4c4112f86027cf6f1099e3c4761326c8abde42e2d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_prospect_to_quote_estimate_and_quote_sales_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-prospect-to-quote-estimate-and-quote-sales:f43ceda97964a03d70bf2218f2dcd29a1e7a1bdedd688c9c32b79abc469a5d34", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` is
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
