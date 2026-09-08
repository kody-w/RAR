---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-portfolio"
description: "Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an unsent email draft to the owner and a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_portfolio", "rar_sha256": "56fafcea5bb56ced0d2b8b0eaa3016efab7be5d18e817346cff653e877e755c9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_product_portfolio_agent.py` and in the RCI capsule.

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

Develop product portfolio Scheduled Email Brief — Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an unsent email draft to the owner and a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio
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
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 56fafcea5bb56ced…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_portfolio_agent.py` first:

```bash
python3 scheduled_brief_develop_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_product_portfolio_agent.py   # or on stdin
python3 scheduled_brief_develop_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product portfolio Scheduled Email Brief — Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an unsent email draft to the owner and a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_product_portfolio',
    "version": '3.0.3',
    "display_name": 'Develop product portfolio Scheduled Email Brief',
    "description": 'Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an unsent email draft to the owner and a Teams',
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
        "upstream_slug": 'scheduled-brief-develop-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4ea2c866c57f915b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-portfolio'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-develop-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop product portfolio stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop product portfolio for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product portfolio, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an unsent email draft to the owner and a Teams', 'example_request': 'Give me the 7am product portfolio brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly product portfolio brief from D365 ERP, drafted as an email to the responsible owner and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopProductPortfolio(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProductPortfolio'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
