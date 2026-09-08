---
name: "rar-cowork-cookbook-scheduled-brief-assess-product-portfolio"
description: "Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_assess_product_portfolio", "rar_sha256": "e937889491bf7b0c9c6d7ccf7419e20f730b60c7ad66e0c2a4908c225090b2f2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_assess_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_assess_product_portfolio_agent.py` and in the RCI capsule.

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

Assess product portfolio Scheduled Email Brief — Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 e937889491bf7b0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_assess_product_portfolio_agent.py` first:

```bash
python3 scheduled_brief_assess_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_assess_product_portfolio_agent.py   # or on stdin
python3 scheduled_brief_assess_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess product portfolio Scheduled Email Brief — Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_assess_product_portfolio',
    "version": '3.0.3',
    "display_name": 'Assess product portfolio Scheduled Email Brief',
    "description": 'Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams',
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
        "upstream_slug": 'scheduled-brief-assess-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81f84f4fa436bf53',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/assess-product-portfolio'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-assess-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where assess product portfolio stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on assess product portfolio for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads assess product portfolio, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams', 'example_request': 'Draft my weekday 7am product portfolio brief from D365 USMF and email it to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly product portfolio brief emailed (as a draft) to the responsible owner, with a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAssessProductPortfolio(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAssessProductPortfolio'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefAssessProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
