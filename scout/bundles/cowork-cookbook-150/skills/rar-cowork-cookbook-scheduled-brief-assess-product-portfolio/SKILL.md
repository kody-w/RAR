---
name: "rar-cowork-cookbook-scheduled-brief-assess-product-portfolio"
description: "Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_assess_product_portfolio", "rar_sha256": "e937889491bf7b0c9c6d7ccf7419e20f730b60c7ad66e0c2a4908c225090b2f2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
