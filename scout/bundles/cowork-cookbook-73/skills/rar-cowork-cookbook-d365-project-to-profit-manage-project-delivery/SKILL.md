---
name: "rar-cowork-cookbook-d365-project-to-profit-manage-project-delivery"
description: "Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit_manage_project_delivery", "rar_sha256": "c377831220674567bd495927bcad481e5d6f0a9d153c64a08ad1ec37492e1141", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_project_to_profit_manage_project_delivery`. The original RAPP
agent is preserved byte-for-byte in `d365_project_to_profit_manage_project_delivery_agent.py` and in the RCI capsule.

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

D365 Manage project delivery Expert — Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_manage_project_delivery_agent.py` and embedded as the fenced Python below (sha256 c377831220674567…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_manage_project_delivery_agent.py` first:

```bash
python3 d365_project_to_profit_manage_project_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_project_to_profit_manage_project_delivery_agent.py   # or on stdin
python3 d365_project_to_profit_manage_project_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage project delivery Expert — Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_project_to_profit_manage_project_delivery',
    "version": '3.0.3',
    "display_name": 'D365 Manage project delivery Expert',
    "description": 'Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-project-to-profit-manage-project-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '021d741b0818292c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'project-to-profit/d365-project-to-profit-manage-project-delivery', 'uses_skills': {'custom': ['d365-project-to-profit-manage-project-delivery'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage project delivery Expert** skill for this conversation. From now on, scope your help to the project to profit domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.', 'example_request': 'Act as the D365 Manage project delivery expert and help me with project delivery in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when the user needs Dynamics 365 F&SCM guidance limited to the Manage project delivery subdomain of Project to profit, using USMF conventions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ProjectToProfitManageProjectDelivery(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProjectToProfitManageProjectDelivery'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365ProjectToProfitManageProjectDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPixrLmX2HeGzFuX7pfbSChvnEiRkIrIAkkQCD3ibb2fd/l8X+fEtBt+xyfO+M782no6ADVkpX5VOaTWW/plzezbYK8evv8prlmtuDNJAkDt1qYmbPY5n1exeArjy3wf2HnWVOFVtvkVf328c1xa7sKiybMs3m6nRduvWgCdx7XuVVtzj2LJl+YC2bMzDS06wWGrxfcf9e20kIyM9N3F0WVR67dLBw3CcGkceEOhVs1iw8Isjhgc7ft1jUQ3GYOUOv4Gg6kgi4vbH78CFSte7cKM39h+maY1c0icX0zWbhZEzbj4qJJ3KILzYdqzKwAqx4XRdL6Yfa+2AKDF15e/bMiZevWswX1O7DVHcy0SNz67fNPf//4FoLfb59/ebMTswZNb7PUl2bn/PjQ62neq5F5yQSCEjPzwYxiBKhn4BkYC1ZPQZPjeovX04faTbyPi3//97g3K7/+8fOXbPH6fHmb/6lt9jCnyc26cZ2FbRamFSbA3PcFlfTmWC8qt2mrrAbg180Mzvtz5m+S8mLxt7nvw3ORd99tPnx5A5tYPTbuy9uPCwDLl7eqnX+/z1KKDz++JzkA+8OPv8mpW+sBHBAGtH7/+np+iQUDfxsaeouv2pHdvtaqXDssXCD8d/bNn6fqL3EvSL4+B3/Ii4+LP5c82/M3oO/TLS0g98/FAgzAzLf3KA+zD681qrxzMzOz3Q8//iuxduDacRLWzf+R3J+eggPXBF774QUJ8NV5C/6+WL5s+y7zXy9bAIf5K5aA4d+W+w7Uv5L92Nl/EJ2EGQi2b3v5p+L+bMLyb4uf/qVt/9mEjwvvy9srPkwrcT8vfnm4yE8/OL81/vD3X4Ho/60YLW8r+yHha2pmoQfi9+vXn36oH80//P2nH9oCeLFrpl/bKvkzmX+G62OdPyD4GvXhj3PB+pcszvI+W3yPocUvefHfql/fF1czCZ3f2uvPi99H4vxZLmYjvi36hOB30VgDXX+H449vvwIWAlRXtfajG/DHv/3bQgrtKq9zr1kANm6bBdjgJkzdWflzENaL8MnPlTvTcwiAfY17cd+sce4tfv4f9oP4P9kv4occwG9fX4O+NvnXJ/XOIAOO+97xjTl/fl+cwSp5FQKGBTysUsfjl3lk1swaFJVbu1UHWMsaG/cTCO5P849FmC1+/msLfX3IfC/Gnx/pKnxyoroVZz6s28R9ny3XAzd72WmDDOcOrt2C5ZLcBrp5ISD1jwCROk86wKczSnUcgpzghIBxQKYbH7IBkp9nYT///LNl1sGX7Eng2OKZAmsIDPiuzuLTJ2Ckl4R+0HzJXDvIFz/88usPi/+5+M9mPYTPaxxBUnntE9BwpynyAsRdm4JhYAvBpgNSeezTL7++oAZiMpAcASahF76SMPDb2HW+4a4J1Cd0jS8sF+ANsE6LvGrmlBk27wvRW3zXFyw6d815I8jrOR0WLsi8mT0CqSYw5zuSWd4s5hxfe+PHRVu7j1V/tqpHCnZTQABm8/NC2h5BlsqTOWNXr6wFJudZCOD/7hXPdiCk+qFe0N9EvC/k2VMXhVmZRVCZrzU887kvIDt9m/4oMjK3/5LNqdmdoXqEzRMeMAggY7+29NO856BGSYFXOfW3tR9jzDmXnh85tfqS1a+QMKt5K+z8URX4bejMieI/Xi5VB3mbOA/8gKazpNcuOK9defjgo+z4VxUP+6x4vrQojKwW/x/XUTMSFM+rLE+dWWbBymf1/tyhubKcd/JZjM6rzaIe0fhbafONvr6x+JcsCYG7VeN/PEc+9vU15smMbQW2QaXUh3xgEjB8lvvw+dmHq2qOFvNL9i1dABAWD24EgAOCAAE0I/Rtwbn3m6YBYIH5+bfS4eEjlTPTBfDrRdFaCfA5z3Udy7RjoFU1x+1rl0EAuHMM90FoB3+waoYboAbkL4ASIYhEkFLev1P4s/eb6n+Y+KyQ5imP6vG50bMAoIc7KzgTWR82gL3M5lnIAzs/P4QAM9KimW23gLsBS5+NbuWWbViHzUyST1zdAtD1p/n7aencOvuaPccOiIiiBeg+Ymj2pBTUP0AH4A0gpNIwA/UAAOUFwkOgmc6EAJznVbA+JT6aXwa5DzeaE9m3ibMh85y5Nlh4QHXQMv6eN85/5iZAXjqPeKz7j572fbVZ9sydNeA/sOK33mcR8f6sA56FxuKb3M//dFL68NcOU4/MfvmjA3xeBE1T1J8h6JmNvyXjd8Bc0FPX+pGYP70i7lOTf3rG8qdnvvze8S0U/7DKE4DPi7+m6R9EvCLl8wJ5h9/huevw8rTXBwCz/UTfP63m3i+Z6v7GsmD5PAWuNm/jCCqB7ynx2xCQF/0K8A8Y/EyR9ZxZe5DMHzkB7MmX7PeuP4ceSDmZP7tqnf+OEh61AQiD5xZ+T12gK2vA2s6Mje/Op7xHoNTu2+esTZKPb4Br3b92upszVTq7ej0fDwH+MweH7uPpwRxDM//848lZefwwk/cF4wKWSurfu+Mrv8z59XdR87QX2Dkni48LB6BUz/kQ2DsvPkecWQMXBt4729WMxWzI8yA4l47f68p/1kYHaXsmPSf/PGewjy9qAN/gLPBx8b2sB6u+DlqP83HWgjPsT/ORYobhMWX+AeaAr++Tvv/VwHLf/v5PegHFHnwDWHuW9ZuSvw3NH0eR2QQgunmenH95A5CbAAPzBfqrlgXDQXh+quc8DQEXBYuD56czgb7/yyr3Ja0OTFBXAXE2RhAbDEFRGCdWa5ywnBW5JlHCsk1ntUHctYN7sEk6yBqz8ZUJb0wHccGkFYm6CLJCgLyng36dS5Nw1nBWDwDzCfi4+1s3aHJepj1NmXH7XlTPELws/OXNwldgpLCqRer52UIkYhE6YY3ybVnh7b2uqWqvdap2MzFhU1r34Cjop/PdEqUVih6CbTuKAptORey3AXGKeMrAWQvb3uLUs1FD3FxaNEb3tHU6dnp7kLJdNkFGPzWKs84Rx4PadbW53lO7lNmktKHSok7xvUISu8JW7RAV3W4LKbUHDefsbuSFuCobNuXNu3wWT6W723NiMJgNKWY2Lot7sfNwaEMqmArHpYYdxrWYrYi4NpniMohcn8Z2xSmT7VwZHkbqK7xL1bBK9DZeoScej8+XVXC39FN95Q75PSSXigARejIU48WJrJpwu0E2bvwaXuXNmbcdUDJYpA8N9j6WbF7YwG4nNM0SOnYZNqzc8aocu2UP1Z7nCfQmSXx2FA73oksb2lb3IJeGHA1sv0ZuaTYXqZK4Q6q1CF9fiUwiN1A9HHTler5w7Kbs94J0DT27wyJ5vaGUNjT71jvyKaWwG2TYCoKCxHljr0T/5GtyHxOMLx8I1oTLFM1Jocy4pmi6k1NxeKFuzYCt4j08jdvtXlIzEEu6CArgqwbHLZtM/mnP6jWmqVICV/oKa4seXe6FgRoK37Io6qbRN9LeqUeTbg9yhBiJNRLbaQpOzeXI4etGPYwYy6oXj0ltDTlU90hXtfWt0OOwv537Y4LpF06qUDq6y+zyesjw1lF5blNJGTNc5QRq1pBm6aYmGBwZUBqfGAZ/ZZVSuLKHY73DnUjxN7VIb9fn1jGZXklvdbrLvJPCJYeq3EaDOJXFanUddJOhxsRVFTdb3kSOMcnBYCYjXNvrFI9MXT2Wun/NCd3fWmSKlFieiQFWreW9aN0rp0z4c5KluSjUwdSlUbn324FP8Mw1b8vdFYTV1kt3fZXeg84+42Tgbnf3zN6nJxgoiskco0Im32xEy+BiI+PGSyZuYQWbfOiM3WOyZNLdiienNVJNYoFYxRrr0GNW+XaVAZq8rwMvhDeEUShb+x7y7lKEyGGI1lOS6sveDTJp7UFRBG1zJSLRMlrxpXagZKuYmjuXJt0BMYi7vbON1WVdmnfWro47Vpd6Xt0ETCtnLuTzQcUWuH64NMJxrAWqinvYKOLYimKojiXEmmzOjsNTE0jc6ZIyVbjXRv9yJ2llp7LcqRX6c9havsECkLeW3fP6Jui4IUWN8Wj3e6UzYkdd0leeRqA7cYEr8syWfmrTuRgy5lBSZWu6Ja1NTqjasJiECbmtOFKfRrmpk6j10ZKgcU12y3TcZNcYWtlnzdaHRkdSslDqFim8UcRoPG+HcylqTnU/nuli8unpOAjBlU9P8r0/CNKETuJZ6pOpVPBbvRcyEYOZO+WW/jnMqRKumB7v6jQhL3x8lbcn2ow3YElHsffSbXleZ11YHfj02HnHwtQuPK2akmefImRdcddbJEj0ZJz21xvNQSNZbCVfb3YaP24ZDOtCzjoiyS6Hj5W/w61l0mgV27RdFxIjNtCFwhGDAwWOwGyPoqKE2Ar3i3p5H11em4pQIZnQkA8icoyDS7oVluq05BB828jaUFhx6aiDKuUTdXNZQkYvx2HJNyiST+VeErMMErXpQkRytvZNM7BtBxkgZJ04DVLxjm8UmSAfeQWVEfsqxZnE0JPeOQV1Q0/IEc6Wh6mWrMAQkfXAp4FyL9WgksfyzFC9kKgp2thaTu2LzDnhIBAiv6yHvuOIFK+rDXU7KGf4esA2F5RVpYmzUrmbDhp1OLAypTImNTUeFUROFGMVsV5xjYjvtpc4poNrXEQriDlVVEtvj/d70RzpI3Md8RSr4ELe6tQpzxNVnMLbCIesFjIqupxwJtMctVJ6JVSoPcaTZy01OUx2lfWtFvndNc+PyXCCJIvg8FZXJN6+MVHfMjvTrsNzYgxtlAdX4TxiRneuAZ9Po8+vteLQa+52ch11p5YctPNT3FwLd5sKRSQTY7RcQmuZFg9Dg7IsMRU0fbwR+O5YkVeY1CMI6tcUeYQgH3YEK+GyBFkp5lXoW1QUT+txZ4XUhZj02uAvFnPFiYsyEtE9GjxypAfmbF1JOvKv62ggoaOKbTaON63JpXqWUePOr3chpfCp2qDlobieNS8mZFU+OIZ/3gnxHmzMzh/P9ubAeqfjZvQD5rIhFNesNeQe6tfdqTjB+NlA7xgXDtMmtG7Ugcjjtd/cZXBsCvGtgTrH6Yr726j3bVQdJExWRE2BA3gi84wNmU60olt6kO8ncnOTddG0NTaDYTalMvrEcenubrWQPrWIhLHclu0laIA8VRf3+5FYBcXSp85JexmOl2DvkPreuOy5+5ag2iA1Vua+g8VtcRLZkAS5fnPZBNzNrCkmj5fLgtqVgV+OGl4WLEMd27MW9Lyl97h6gRCk2cX7Nr/XCB+v6pW+vW8EQFVcSrIHqY4xpsA3YnzhNegsWczkXjleCS4Zd1/huW2wukbtUedwTZzqhk7n1KaM4+CbChvbhN/tBRicBnbSKhruVSgbLb9ap/4tj6YUixM+FG9Wgi6r5Y1TFLQpyqxoU8bWC+wqFMIJXiK5TB1U2lwijSk2+yE/qcvASfzDqStV4bCMdpoAS5xxENDpVN6hK6lXg8Iah+MmGBAWUcYw8mtdPql7ZFexJy23QfFy5nvuHNDhLrNEk1fP8Ea2l7Fz9nYl3efykjy5VWAEJ++knpEsLC3hkIf1xObOsPW9m2yoVbMm7eygMNS53jQoCEvxOi1DdtuW1a2zAJkoOqFNOIxT5s2HZMzA79eswLqDgdCj49HrtGRws13SJNOlmG/JaGmqJVEEcR0l6WlHmzlJZdN6f62vAlpxrgqIUqHLK2dpMV5u+9Gro6N/vdqoYlBwoq9sInEyv+jh2rrJG2TTNSFIGZp4uUYpqa99g6H7FY2Kuqn2y+3uVrTiZr1T5NNRH/U4YtJjH1iXdMPCArUCJ33+zAgSHBRHJSDi8RTQQcjSPk3iXChKo+inMitc7DuHM6dyzNmVv+lXyBaULFQaIzkvmSJ9HUj7UOKX8wVUGFN9q3g43bkZmd6bHe91YXK65pN7353YfOeJ6/sNctDD0RdAKaXZ4z3UCn/b+oc4GGDT9IudjSaiN624FZuTzR5t1lrPVHqpTIh3uyf2eEjSaQ3t9qh2VzloQ1i1qa7rwg4awDmKX0nghMuH8ehXW/5kapWpopXjHoXxbOy3mr5TDAyT4rQTnAavR4RNVKQ2VsMBvR/2BbvvYeTgOHqSelvTrFlkMOsi2ys8dbpKesmy8LAz9oSsaG0C77JWhvaiHwgGCV96Qe65nN64HTyyZUZgLn9qjCW10cYrA51hmvTRmtDuktjF3LYzmavqQuecAnCoK9JWogj26M7Zluo2bHcnP6Uv57vB3euOu9YXw1ERWySOTrAPLuORy6bI2h/txnQvGLe5rXb7zb0k8khjBQgga5mZ1MqnqFwdCDwiQmLH8tW6NxjZ1t1o7+L8SiRQlbe2JAQPSytr/N2hp3bC3mbruLpPBmbFPqBhicrGKdnUa29LSyh92FE+o0AjcqMlDMPjsjIRogyLrsz2SApOU5LInGsZxjvPMUlO2/fr4TJ6vJ7Lxg5VlWjNtNPqbgBvtJaVZbly7SYxdd0VyeGwixJUorY9U6q3SC/PoZQcJnnbyZDSAEoccP7a1bfJo4cOqs7n7Z7F9rdBy/0z4ujTkabMo0GRAQ5yOLFLVFpUThO8q3cxbm2Xls7QUtxzQ8Hfrucx55RqednWUhQ5aYFsUdE+UT1Mh+F1r/LXA1U0JxXDI9Yt7YPbO0y5woe7XVzXbld1wTrNUxUy+BiD5CEVcAnT+FVrYGKqB8NYRBLRdJyX2Ap9X67gITskhQzt7r4nnUhAkVUviFs6twS2Tu/6GRE9WLC7ndbYpKdcY2WKqVvuhEd7w+zvbWFMF9O52eOq2fI4CcqRynPoJTdSwwrLPWGV67YdrXB6va71Zk+YJHRJa3DILJaY2233K5PatO3YWDfPU/rauDsDHB2qPJBwJDUiRNnujFZEDnoTedWE0xdGddHO6VOrbbj+urkAllVsPrL67IhWaqkxBZZVy9Nps6vz25U+WoKVdxSfT/FJvhA8QuExioa3BBzhaKtzxaaXto6OTSHXRfJJdqbzVceCuTA6w6OjdrxlI83BSM6x26odcTtCS1pY4eSOOxCkBYXFUtgfAnM9dt7IR8JJ5sY5UySr4AQK08Gm6PAI9wFZs/z52AtUAI4memr2DLLk4dDUWxEq2PXWjqMEx5pT5unmGbQat6a9hmt8Txj6JKgIIlRGiNDmifFLxDukZ7knhNqwFSP27jIxQWdkN9zxLjgXtIsVe9pg2BNsLDdEta4qpGJXt2K9XXmBYXkyNWXdMTQKRrmJy3qppqIbE2gB68vreoSvtxtzbpY3WcVxv1OcwtvhN9zwrhHq0WpQ+nEaU6PI3saVkmJYdaqUqQUF7H1P82jDnPyqSPaaIemu7namecsMDi+dK55RsFoj6IGdUGi63yyCkoOVsdwnTudt9ZXfDLVnsi3FCdVW5faVGCelFI3kRl2L0/4mClRPj2mBkqR9ke+DI1zJFt+WmgzbRZOv4pEWT8g2xSLtToegkkLXiX0anK6k7ZEiKgvBQFFll64D7YcN5HX5hbxj5EnioMJKeKS2tqZ7kPts1/k7nxb2YoojrLCZmkwXDDmwIc/Z++X1pg7hroH8a6m3uSipKQZqeJ7YEuxFxvmzTQa9dO7O+ohbapJ4hXfvzwMBmKL0ewfpD12XKml1WO9NxGoGdq+qwy5xna272jPo8RxVW3yb9auwjeub0GbB4KLtbomVzBXFpS6wuXWGuueTYNY3mS5SQpM8VTjmReUmI8/n8LlLbeGsSp2K2xIjlT3NmjvHHZAcVsQ7FzMQfsQveOqoLKjX1eOd0DjyYiHiyhNuOKqQEyWkjBngTS7JawvJ1qTJsZ1Jrg4YkbZuKIuOMjHHdtMRBmHnQ3OZ7jbWWR58Y6R2nVf2hq3XTQ0R0Y5L9CWEkNZ+BRGXhoRNO6f3u1sLRVK5PhCbpbGfDkWlrYIredJUdgx6f4QjoYEqcN5BcPpKajLPOLZp3Y4+UV9PAzbp7p5vN31lX9ThenNp0i32HcuG12JbsHKxjelaxuWlrMcofSETacKn1eXiTbgtsud6D98jUFYWY6R1NZbTSwGIki976e6dTrnjeGvB33N81Jy1dYTrEa9cESLJPX+pKLvDEqNZC5lSLzG6lm0yRK5vuQhKHDksCTXbgMNvcnMHD9MT9xigq23DL/nDzKzGttTrqKVbN9DIJc3LAHwMRPq4jEhFIa4weyNhy7qC0FfMi7BDkcxBMzS0QAG3PlmNJm5IZmw4nmxTwrwa+ZRkho5a5lg6Hq4rex1mZHMdTLWNGp5gNKaJMJqB39T8jtK9tQlh3nTdDVnDoErAyi0iDyyytK1oOvHCJZYSdSl31FwNpsOG7u5yaJsn6NxTSMP0Ke1CycpbZYdlTLYaDldbauNjtqLcMSvjrdg+1wS2rGweu1X4nc03q8LV9p5LUAcPb+GAXK5A5T5tkrVqIGa/FqPdoaL42F3HzDHlEljxSWwDQWhXVyR+PeMZRDewkOSNThKV4GD76uxVJNESN6xPenwvHoUEuqKYZi2zKyhZup7hji1/y83DHa0utYEEq5WpinqXhwQ3NacrZHpWnhSXW+1lQSzrS3VEO+8iEJIkdJoqEil138f9xbq5LnB3FpVR9Wjvu0hyfXp7P9p1sKS1A+NKKgtbONRyPmW30XWNap7V7BqMLEH93AkJRW5WjrRCbk54dhyklfaURw2YzMVHJ4dCOBeqI9ORhnqDsY11w/COQgdTKK3DOrTv0FKPXIOEsvFG9rKxAqieeMyCJUGeelMeNpokY6Fmuai29En6hh97xmyGC2pCmikQ3Sq8D7CT1ccjmoSZbsO4r25Sd9MxU4PxzQ2tdhsFP3XTTd73jpDJFCGDzOUPk4xM3Epq9C7z1dumJUtvPWqXIKiG48ov6/B04nMdimErkGtQAQalhm8hJiSLpmXowUGmW3Tz84sk7F0mlsgEZu6+BTI2bCvnTcCeUHtS/KWmrEzR7VyBt5huK3gF1q9rOZfpaL00Xdt0rCMbTS63X/vkQeXT5SkhOWfvSQGrr9e7lY6HfJKduFqJDI9sWyNYet6NNUh+TeH24MbHFqe6eyJmJ3d7GbJlJ2VZT3repdrsuM6VJ5yIzrC1oZWbZq1kkaAo6m9vH9/m+6bXrdF/8VWW+e/8/8+uFJ43A98uqB/3M67pfH6s9fm/quDfP75VdgjUe16p1Enrv64j/uFC5dNfu52cZY3PN0e+3ZQ9r+Ea05/fu3wLM6etG6BKnSePq2sww2rr+f2s+uvrBYfvl09fH2/xgMe8Cdzq2fxHS9/mN6jmW2nXCc3GfT36ryunj2/O612LrzNOblXMhr9uPIG92Dv8jr39+r8A5EtSo0ArAAA= -->
