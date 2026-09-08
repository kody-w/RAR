---
name: "rar-cowork-cookbook-scheduled-brief-end-product-sales"
description: "Builds a morning brief on end product sales from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, then saves an email draft to the owner pl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_end_product_sales", "rar_sha256": "fb86e949fc70e0a0afa396cd1bc8b132af5696db22ec8762a2d017837d5fef8b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_end_product_sales`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_end_product_sales_agent.py` and in the RCI capsule.

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

End product sales Scheduled Email Brief — Builds a morning brief on end product sales from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, then saves an email draft to the owner pl

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-end-product-sales
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 fb86e949fc70e0a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_end_product_sales_agent.py` first:

```bash
python3 scheduled_brief_end_product_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_end_product_sales_agent.py   # or on stdin
python3 scheduled_brief_end_product_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
End product sales Scheduled Email Brief — Builds a morning brief on end product sales from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, then saves an email draft to the owner pl

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-end-product-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_end_product_sales',
    "version": '3.0.3',
    "display_name": 'End product sales Scheduled Email Brief',
    "description": 'Builds a morning brief on end product sales from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, then saves an email draft to the owner pl',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-end-product-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-end-product-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a64525dd843a0ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/end-product-sales'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-end-product-sales', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where end product sales stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on end product sales for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads end product sales, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on end product sales from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, then saves an email draft to the owner pl', 'example_request': 'Draft my 7am weekday end product sales brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a sales owner wants a recurring (daily/weekly, e.g. weekday 7am) end product sales brief drafted as an unsent email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefEndProductSales(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefEndProductSales'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ScheduledBriefEndProductSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
