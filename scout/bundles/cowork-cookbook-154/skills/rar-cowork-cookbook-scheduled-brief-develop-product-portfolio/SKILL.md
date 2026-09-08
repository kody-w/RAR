---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-portfolio"
description: "Builds a product-portfolio morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an unsent email draft to the owner and a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_portfolio", "rar_sha256": "56fafcea5bb56ced0d2b8b0eaa3016efab7be5d18e817346cff653e877e755c9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjxpbmX9G8/cF2q6rEIgRUx40YECAkJCTEJnA5yuwg9n1x+79PIumtsu/17enbMZ9GFRUSkHm2POd5Tr7Jb29W24R59fb5TfasbLGzkiQKvWphZe5im/d5FYOvPLbB/4WTZ00V2W2TV/XbhzfXq50qKpooz8B0uo0St15Yi6LK3dZpPhZ51fh5EuWLNK+yKAsWdhV5/sKv8nTBjJmVRk69QDfYgr1eFq7VWAs/B4oXiRdYycLLmqgZPy+avFhgi6jx0nphj4soLSyn+QDsy1Mribx60dWLJvQW+EfXGhdVDuwHqqzOq6zA+/DwI/OGZgFmAUPrD4siaYGZ2aLNaqBj4aVWlCzcyvIboOshKu+zVwSsheJZ6eysN1hpkXj12+eff/nwBqxI3j7/9uYkVl3PsXNCz20Tz6VnFxmv85K8uDwDcXmPA5CSWFkAhhcjiHkGrguvAj6n4JYLIvO6+rH2Ev/D4t//Pe6tKqh/+vwlW7w+X97mf9c2e9jZ5FbdeO7CsQrLjhIQrk8LKumtsV5UXtNW2bwcNViyLPj0nPldEojq3+ZnPz6VfAq85scvbzkwwZrj9OXtpwVYjC9vVTv//jRLKX786VOS917140/f5dStffecZhYGrP709XX9EgsGfh8a+Yuv8oXdvnRVnhMVHhD+B//mz9P0l7hXSL4+B/+YFx8Wfy159udvwN5nUtpA7l+LBTEAM98+3fMo+/Glo8o7L7Myx/vxp38mFqyvEydR3fy35P78FBx6lgui9QrJTx8ey/fLYvny7ZvMf662AAnzr3gChr+r+xaofyb7sbJ/JxrUDqio97X8S3F/NWH5t8XP/9S3/2rCh4X/5Y3xkmguVzvxPi9+e6TIzz+432/+8MvvQPT/VYyct5XzkPA1tbLI9+rm69eff6gft3/45ecf2gJkMSjnr22V/JXMv4rrQ8+fIvga9eOf5wL9ahZnADkW32po8Vte/K/q908LDQCV+/1+/Xnxx0qcP8vF7MS70mcI/lCNNbD1D3H86e13AEEZ8KZ9ghrAj3/7t8Upcqq8zgGOyU7eNguwwE2UerPxShjVi+gJlBVAp6qOQGBf40D+zys8W5z7i1//t/OA/Y/OC/ZX9Tu4fX0A+Ff3CW9fX0D/9RvQ//ppoczwWUVBlAEIv1KXy5cMwDCAWaC8qLzaqzoAWPbYeB9BXX+cfyyibPHrf1vH14e4T8X46wOgoycSXrf7GQVrIOHT7K8eetnLOwdAvTd4Tgs0JbkDzPIjgOMfQBzqPOkAis6xqeMoASwQAZwB7DY+ZIP4fZ6F/frrr7ZVh1+yJ2yjiyft1Ssw4Js5i48fgX9+EgVh8yXznDBf/PDb7z8s/nPxX816CJ91XACPvFYHWHiQz+ICVFubgmFg4cBSAyh5rM5vv7+iDMTMLAXWMvJnGpwng2yNPfc95DJPfUSwzcL2QKi9mTlBEGdyjJpPi72/+GYvUDo/mtkizOtm4XqFl7le5oxAqgXc+RbJLG8WNUjJ2h8/LNrae2j91a6sh4kpKHur+XVx2l4AN+XJzKfVi6vA5DyLQPi/JcTzPhBS/VAv6HcRnxbinJ+LwqqsIqyslw7feq7L3CC8pgPhFqD2/ks2s7E3h+pRLM/wgEEgMs5rST/Oaw76lxQgg1u/636MsWYGVR5MWn0BLcGzEKxqXgoHEANQGrSRO9PDf7xSqg7zNnEf8QOWzpJeq+C+VuWRg68u4L0fWnzvh751Cwv20Xw8mobFlxaB4PXi/+c+ag4Ltdtd2R2lsMyCFZWr8VyuubWcpTy7UWDww4dHaX7vbt4R7B3Iv2RJBHKvGv/jOfKxyK8xT3BsKxDkK3V9yAcZBsyZ5T4KYE7oqpo9t75k74wBHF084BHkAEALUE2zM+8K56fvloYAEj48l+nVPTwSpnJnh0GSL4rWTkAC+p7n2pYTA6uquYhfywyqwZsLug8jJ/yTV/OKgaQD8hfAiAiUJYjjp28o/nz6bvqfJj6bpHnKo4FsQQ1XDwHADm82cF6KPmoAlFnNs5MHfn5+CAFupEUz+26DKgKePm96lVe2UQ3Spv7wiqtXANj+OH8/PZ3vekMBCgcEC5RH0YLoPgpqTqAUtEDABoApoL7SKAMtAQjKKwgPgVY6owNA31fP+pT4uP1yyHtU4cxl7xNnR+Y5c3vwLAQrG/8IIspfpQmQl84jHnr/PtO+aZtlz0BaAzAEGt+fPvuIT89W4NlrLN7lfv6HrdKP/9pu6kHu6p8T4PMibJqi/rxaPQn5nY8/ARhbPW2tv3PzxwcofHzx5sd/AI8/KXj6/nnxrxn5JxGvIvm8gD9Bn6D50fGVZK8PiMn2I218XM9Pv2RX7zvaAvUAdJqZDZJxBqN3anwfAvgxqAB6gcFPqqxnhu0BqT+4ASzHl+yPWT9XHaCeLJiztM7/gAaPHgFUwHP1vlEYeJQ1QLc795iB92nems3m197b56xNkg9vAFa9f2FjN9NVOqd4PW8LQfRB69ZE3uPqgRhDM//885b5/PhhJZ8WjAfQKan/mIYvkplJ9g/V8nQWOOkADR9mtAcgADIUODsrnyvNqkHqgqydnWrGYvbiuQecu8YHJ3x9csI/GsTMLPJH2pjBr2xB9X1YeJ+CTwtVPnF/Kfdbq/qPQnXQE8xy3PzzTI8fXlAzE4gFrr7tFIA3r73brMHLWrAt/nnepczhfUyZf4A54OvbpG9/hrC9t1/+yq6Zgv7RpqtXF4DEHk3wk6V60LCB4HogIZ7L8GAykKxPXntU1196/l6Bf+W49+wznnz9WtBHCB7B7D0vnrn2ReuAh5oFbqV/oQWoeeAwYLM5Jt+D/d3l/LFLmw0CIWqef1T47Q2kpDV3BK+kfLX5YDiArY/13MysQP0CheD6WWng2f98A/ASVIcW6DuBJGzjW77jWZhtYxvHcyEXsQkb8iwLheCN51s2bnuYCxMeAePoeuP4/gZDPQLHPRzDHBLIexbu17l1i2bjMBL3IZJE/DWMQK7r+cjadYkNsXEwHIEs0gbKMNKyv0+No8x9efz0cA7nt73IHJmX47+92Zs1GMmv6z31/GxXJAxu4vZ45JfVxs/7nubV6HD11gnKrrK1cUYHWrIj1OAbxd4aW14+2mxKShjniG06nOggYDA2mw6XuFzm6WA26dDg9dmJLWM9sG7i3uCVXm1C/EJA5gW+1VqBZXviLpU9dIgtDashwEbrGFmrMGuWUEAgUO1Go4dpYTfc8RV5U/rCvfbm3moOxPIc+2aenZtUEKWVh50T78JAsVOSzB7HiU3OrcmucK5HQTKKS7qnt1VljJwcFC5/sCKKJi7hFlfR/A5LXkgeajE6pLKMp3qdXPnuLoeInPXkfXmlsV3sQPBx7Jwq0ZrdWt4qpTSyvbzxDqkR18eaS/d1xRoUEno0eT3eHQ5OD/JG0yOnWBeDVickYkBeN0WD12THYbPyfVO9XDoE92rfv7A6RZwgwYh2x33jprnoovFugCCLPRVixbunyb7G9Qm+xDljCaRS3pbeLuTt+7W2yp1BUbG2NCR82fEVlhLwSTrGrs4d4bW+P0xZs4MwpG5YG5NCQwprGKHxfYwzMjHtrmWVbHYoh0EbC3XGcnOEBZPel7FV95N8sXDqfhlRvZZw7iok1ZGg90SgHtlNjMr0/mhGQusymdeszG1KBJcrl9IUt7ZjbE3ubCRByQTlHKS2tMYy8yAu0XoM7vE9udBQLewEkeO3SUTCey7WW3i8FTYRQ/2FWArIXbHgJLdFdqkds03pSrsmPaRKsS7TDXFxVpWob2R+E5/TPjhs5bqOhJFXm00M0ddMvMU2e1+Hau6DcN3BCuMDfohsFDpGJwOlzryspRpDwvqavxlHMZAvbLwuVrtxUqGJM7q4PxF0lHMS2lRSglSUAJGMRyUtamoVJMeG592u7SBXnEWKemqGfTlyy73oD5IGW+pa3qzkFS2soLqGV3l32PVq5lH8kjxhpoc6+1SCjpcaFTlGXtlIQwg3k4vNLDFCfhxERiQIEerw7SnN9YKqLae7ER7iUiMO6YdDhuD45rY+05bNHfrV8XTLVqm/NNH7dEBcFQ9XsaOYK6K+ECQaYF6JINtknY5y1IvU/kjuMY0Zrr1yuFcVsz1acRA0ZO2wUskQ15184jEk4LpAvBqJaIzWIcbPnIfFdaTb4i5jMCTGzTOmW/ZWPbDx0fCpUrBpqGC5dotom+0puu+FiLhId3aPsmQew+uDOJLkwd6OiK5PZurSN7uevAEfuIhrlmJX7Y9pYlhnPUgMYc0rcruF2OZq7ZRGUAqMxdlmT5660rOuIlc3jCqgUGym90N5rlMRkrul6agpaiL3e0O257o7FP4ooCDR20Ep9zKZGXuFLqY7PV0GPnR3kXQ2IGDnDVdOQw1vNJFf+dJ+1zD2YXuXKZETsXXpbQwlyvc5dD+imy5XLy0DUHHlUE5AqlkO3+6VKq1xt/BLRhQ9W60upCrH5UmyWG3bM4OREKnH7cU1E3nCcM4xBm0cTbdly5IOxV5qy2OG3t2YXLewyJTQ1EZYbhNXDNXPBKHiSb9l5NPpEqFuLzFhnLW3oCqW2vq4vyAWFwoGbvCVtC4mSXazzWmXhOEld0891EohiGWatqNRlwfVWqOhRzpJBbkTV9+a0pSug0T4WHuzMpMwCYc/V8LWqrKhZZYtUZ/PtIScjpezQTdruS9aRehi9hBtUPG88pwbIo0NcvRRZbnjxoy1jTWrSPzJ6XstKbRjGK6VSYGuwaqg7xGdsKjAc96ddS7ajuKxRkVVzhe2nTm6keysttse4K+ROVhNmVuJNql7ElG2kGpVHbNmDVDP6zq14TOpl+OEOm3boL5xgSXa3GV9xRjxUlCHtSV2uu5KibC/GTSrsePh4MielwVbVrJaVPX7qlQEzkRo6dqFLtqpcZHR6iErJMaXsDG/UufkPjQCihxhp0YFMY8ofXAoDnEaA47qNSqTezaCluLlWCO+32XJLpfdm24U5L42iV2iR6oTXATpsLoTAnXSDltdU+6rKyGuG1Lse9yCDPW06VzBD/nl2mq7PnB9e4Wvl8YZrscaHa2GEesVoR4pbm+HdBNKXH+CAVg33EkzO/Ge1wah7EyFCAaYVmyToFsOlCCoG0I3fS4M71QrEJKEY1bZFDqNEFgPeqK+8sSYk6rgPnL73FGRzaDrnFfw5xunWaJhyjQdO00bb4ROOwjn7XD2lkuhUcuU05TCIPvLaXm5l2dBiq0TXCdVQ5px7VYTf0wIn1UHaorpJZYc+ZOHjl44bE0vWU7nZH/f7iJRX3qQNIoXXDSPvIzZjaqSxA1GdvudGdSbrbml85qJ2KrVEFybTsMZjUWG3air4aZc9ZwRECwVMOa8ra96shb3O30si1W/UQ8BjcSxtxLVY3KT97RicGDO2UvTvdNfr/XRj4orzfGHE3QR9fPtAnIEo5brlBOQk94Up6hYVpncU1Cel/2uh5eSuk/lJtgbpE8N6TEZBd28HluegdYSaBqTNjbiSyKqqkmFeS2IEUKJV75k+aKuvVLYbBp3l51OwaqJKNU7SEMfLnfnodOscX/ZYkXEiHTLIMqBGukLmd7ydDfuQb2ToGNT2NrbaIVF5bF83ELrRh9l9l6Ydwl0cJGMkVUJcYbCKFdmS6upYOJSTviQKUjLkMrNNawJbjc0+n24sIbnY0omHCwz5m47pxYmRqNkgqfk3Eq4rbKbREUPw0Nn7g3kKoHENpaxy/h0SXu5uCQ1UmenXbDMQ1H3zoVaRwMz7ZVhzI/rS2uPk7SZBEI/nhmKqVdNk6GDfoxi1uAcTUN9RC1zlmzjDKZhKq7odCVm5uB5vLdp+Ph44LzLJLL8FdbWzPnmn1Cptxq1vmuIzxwOPHXq9S1Mb+lLBgNJhYlUonc9yDtjjwg0VsikOhnYBbo6EMeh3D3dsqG2508HXsYFWRR2cCfu1GSJCBiarVZoitOawBoVJxbaNI5bJux5Q6oHtWe2pBjy2UFdVlad7Jjd6GaMFREuaWZ7atwdRsO0IQxGraLtEYq7XgWDiwfOqiEfEVKIXhNYGVZ9Xe9wMGKFk3ia20kWTG7hydxV1o/uSkFaSCInlT9iK+qQkEMedHXMLyn0mFzKwjGdc4f6DmTTF1jUZFUUqJguYdjb02zajHQQTppmlDx/O4LGJtsV9BTVOkXSSNeeBP1kgbawDE37klFoqOUFRullAUjJNCi9P/bu7rRJ8JqejtTQ0qcwK0wo6QH9d9Pk6v04lRDfNFQNyWlZqMyS7XN/2R5xckl4KYYqO7VWbmmj7E3SWhYF4ua6Y6qGet2eMdNVts61KhH+3PCbaRNJo7/hxyiv46q9uGhE75vVVlMLVw3wZuSXuzXLEYwC76OKGblwB7Z6QrvTQlRUy021vjjjsdASHs8PW9vc6mHudZhzKBPOYHh1M6nr4sw4MXVbwidZwtxcKm/JGXeUyL1vyUaI9x5tKcdwPx4mlnMObax5yrKUz7K02V2V8OyYSbzhoECsXH95gRM0OenHEI6mndgQ+TkJjtkQ3fE8FMqNuAqsrmOk9CZftM0F2XgoL9waHXXMEzRpmHms72kMZ8YqMio4JvINmVL4sd0eEyg2kmG33UDXc4g3J48q8CzPDmBf3qxB/59t7TARYaLb+Ocr3q1ChqEr2TBKX4e1miyMeMvyFbvKI+Gk1qx7DekIMG2IQPB2vxHEW+vrdxbBUPiCImDLUXNwbZfFwK9bkH+psJdpRvElt4GutYytnO0q7gbVoNDoIAZOJrq3so2ViCqOsUqsSloxo6w7LKOtqMP2LvNNIwjvxaZJMLYNTklb9902aBNE7hsGxhV9L8PTeLpK2Zq6nbdODHV7nEr9DqfdFY8j0zFahlHUpVnqkVpLwGCXDOV9uwmaWl/el5Ffba87QPDxcFMtX3SkG1JS2e3iAVSsW3K4u2dsdMb0xkCZTPdUD6nFeej1a9NvbFudop16OdzvsW6KmYoRWL2JxAE30AtcwJp63Z3UY3Nl11Uv0H2YpVai20uDG1dFG0xNobWoB7mrZYl3V8XElM1RUwGiJgnXxduatiJo7C8UmZ9FZNohV213lO1S21BRhS2RJe6QW8ix9HSATHRaKSwpZzsZqfuzloVL5SJRR20XmhpD8yuTn6Scw+/3azOeInriJNI64Nqm9FnRZG/dtIz2d7JdHRqoOncWEcfJcKX69tKCXthChkyp8AxAQiwYt/LWFsUuxnHpfvRjm2ToGIdPGe1mCZs568PZUohteY4F11lREcvVWo9ftSpAmdh2bW6aZEMwWAxuIkTYDKf8khXjAb5lWu5niZRnA3k0YefsYevduXKwzNXQasouoGv0/Y3JrP3dGtX5AN22cBoryJJbX+6QFVsrULC55vH+ShXqlV1NdeISa2bIO3iETdQ8l1Ol7EZiQ+D3NPfOcIxWS0FcKmu1z3Q9rXZuB4ckXXN8EiooaWnmufPvgwy7suZybYlOyKRiA6mIW4JihrbdO3nX36w4liC2vYmxol/7A7XqKUq76oJvxxbMGY5sZyv4UsARq9323bpiiRt1yqGSSJagfSyOqDQZ2dTe7pd7XWvmASYp+4Qsz1NSRMudUjYgeUinRfYQyVf3C3bHVytGIUHLIJyOIr1cGau1ZUgkh1/dbsWPcguYog9X3BF4bnACtM+yIcunc8Qc2j1fIYox+dCx2d1Kl49uN1IKSVWsWLZzBp8SZHV18Cas2xQnsj6lsAgNNUi1RKlt1DLI5fkckDZx63mEQjgkg7Ap7E6OuY+GtreZ6OatRrlojwY5smtEJxEp0K9U4fIrr4FhEV7DkX+xNoGlT6TYpsGIGXwoQFmk7Tfskg29au+l+FSGjYymlam5jniernuYr8otgekJkRV+kZD6GV077ekYHE57OpWAiz1BNx1S6C7vEhK71pGmMXYhrSnwOowHEzM3ZFF4rnorQ/hWOsx1N+nzX0UQEhFvyyuiE86dmpZTXdiO3A2n2w5a7q3luE+s6/5q2qyVXaPlPXXHWEuqmA4MCmwwJm/Zbs18cw5LD5pO8IE97fakmG3jPoivOYsRqJiPrkN1tNweVbcraWfcmjY+TFSqn2HhvEoKkiRr9da1K5vBlDMclvv42KW6raK9yci7kdZFQjufzbu/1nlNvN7SbplImn+sjLuBruoDzosHk+GW92aL4mG7bge2cEIIPxvOhcPZsGv03DJv8K0AN4iBSWHHNPCgOpTpss1x81Ql3TTEMNiTcRlRradeRABjN8UVDl3aXfskr6Z2NU5rQjMusWbCYQ54xKLOFjHZtz3BCEEmntY8EvX+9XYiemQ4xo4orQn53JMcN5JMlfRiegvUoAymHGnbsdZFg7qk9xVyLmMoEU0md1GPzX1tRyrbI9y7quXmWgU629MSvd/ooesUvfEheNIhrERtZONqMLLiaBSvTytcxVvHQ6/mVblMRebYadWcYGoVmnfFD45yZvWE2dogCM0qZm+uf0dV9N6r8LicT0AQyW3DQVSHaeNbdXwGm704DJlbZO0y99Kgu5vbbMtluLuHaSv2UCGaiMNgmDwN9S2Zkts9nqKyDauBUNOlFNFaXOYSom7lXTBVqDHYjHG4IupKrPjGv174LuxbJ9hBosuWy7OqX8kwGS/9PeOwTSLd+SUNCri8iBllGNZZE5SYGMUq2lTdCeOIqemHPSg+OKx54bBS080GoI9K37GSPnXONdXQIvE584Jrt/rmZh7a5GZN4bJOFHZwZ7W9Qh0FnL6v1GgY97UPQybrYXpfqn42oNgNw0z82pi3jaaiRQ9lJpIghm/dakw+pqiWK3wI9knrThMh3Jbvxx1RkwJy13R4SgilwGS9VyrUOY1X/5bUZgk2iubZVHJHpwMbDePRdrzc7qpwj2UljzQH9nZ2bsNSFDjWEFNzZLserZHeWi6lTDqPAEVWlUJzNDPCokwc1jkhRDmuVs12KSPHSq73zMi4/Rq7GxfDbK+DMHX+puhHd9kVgXyfEqYLzphaExbs8dmx45M7M2TkIdVuTTGcopqQLOlYgm0bpWhgZ+93K3dJkuumTFW1qqUugEpuAykBuUFSqIHvGdbeEPx+UawbU1cBoevk7eJQG9dIcJmXLlcFj9u1O0w8LLrZueYZZjxQMHm6Ga1byt0k27bVCRF5J/qdDONxdrTIFdceVgEzyocL2BWETirfLWzKl2dPvLuxgm4raOJzPkgZ9Lj3AzXq0Si+inuytQeH4o857IlqhuCy7aA1eyKytbo3Lrd7QSimp9cb3GYkG1I32zuiC7k3SD4HK51+5jPNlVEW+KusV6hpYJq5EkHTgW4s0Hqjy9vRR+2MnG6bpredS1v7twsdo8fh0vOyciBR61iylQyyvEzjpmoudYcec7wmRrjhh7M/1vebbsFWryz5Xd9MZYvuYAfBW3XnGdr6vkwND+1TSoy6FdwwawuDCDoi9nmFWiUWB66yMvS8U1uQOpBPJ0YsUDQsYKudZQhNsA0IWNUlfuPeXL7o8Q1o5j3Sqg9beo1KElHFJySwYkYONm1GypeAjVIywWKxL26ifBfJ0bBVb22syNY7smCrXgr2cm26eMUF0/VywDRbOCAgRWz0VOWN6a6zvoTbQqNuJw86Wac2JKzCh8m+W60wfBCcayuJmePnld5GR7FMlT1PC+uJ2Gfi1GU1o1bIgevc/r7BbwqkELQ1mec1e6Upivrb24e3+Vz1dTr6r7+1NR/L/D87HXoe5Ly/fvE4LfQs9/ND1+f/gW2/fHirnAhY9jwTq5M2eB0c/d2J2Mf/9rH7LGZ8vhr1fgr8PF9urGB+l/gtyty2bqrxa50nj9cxwAy7refXDuvZVgd8//EA9O/cep5/RkH2tcm/Vl4TVd7b/G7g/LKF50aAP16XwevEEIx/vTL0Fd1gX72qmN1+neYDb9FP0Cf07ff/A5QsYHkYLgAA -->
