---
name: "rar-cowork-cookbook-d365-plan-to-produce"
description: "Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce", "rar_sha256": "62fd7b4d6731679d1ad1aab84483b19b210170b33832937703fb0b42895b718d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_plan_to_produce`. The original RAPP
agent is preserved byte-for-byte in `d365_plan_to_produce_agent.py` and in the RCI capsule.

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

D365 Plan to produce Expert — Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_agent.py` and embedded as the fenced Python below (sha256 62fd7b4d6731679d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_agent.py` first:

```bash
python3 d365_plan_to_produce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_plan_to_produce_agent.py   # or on stdin
python3 d365_plan_to_produce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Plan to produce Expert — Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_plan_to_produce',
    "version": '3.0.3',
    "display_name": 'D365 Plan to produce Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-plan-to-produce',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-plan-to-produce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '286961260ee3ad34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'plan-to-produce/d365-plan-to-produce', 'uses_skills': {'custom': ['d365-plan-to-produce'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Plan to produce Expert** skill for this conversation. From now on, scope your help to the plan to produce domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.', 'example_request': 'Act as the D365 Plan to produce expert and walk me through production order scheduling in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 Finance & Supply Chain help limited to the Plan to produce end-to-end process, working against the USMF legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365PlanToProduce(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365PlanToProduce'
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
    print(D365PlanToProduce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebOi2LbnV7HPi+jKemQeEJAhX9yIBplEUWRSqKzIYgYZZVCgur57b9TMqrq37u13I/qfNvMcZQ9rXuu39tn++ub2XVI1b5/f9NAtF6Kb52kSNgu3DBbr6l41GXirMg/8LPyq7JrU67uqad8+vgVh6zdp3aVVOW/3qzpsF10SzutuYdO688yiqxbcWLpF6rcLjFgthP+pr5WFmruPqbqpgt4PFx9Wix26cJvQbT8uMGSxw+YpP2zbsP3xI5CmvYdNWsaLvp1/B5XfF2HZhcEC/E67NATbTF0RFnkYu/lzcHwKUs5itB8fGiVVGbbdpyCMGzcIF9VD+PYdKBMOblHnYfv2+aefP76l4PPb51/f/NxtwdAbBySfRTYq9Skw2AEeYzBVj8B+JXiuwyaqmgIMBWG0eD19aMM8+rj4z//M7m4Ttz9+/lIuXq8vb/M/rS8fNusqt53V8d3a9dIcSP++YPK7O7aLJuz6pmwX7qLtZhu8P3f+TqmqF3+b5z48mbzHYffhyxtwR/NwwZe3HxdVA/g1/fz5faZSf/jxPa+ATT/8+Dudtvcuod/NxIDU719fzy+yYOHvS9No8VVX+fWLVxP6aR0C4n/Qb349RX+Re5nk63Pxh6r+uPhryrM+fwPyPgPMA3T/miywAdj59n6p0vLDi0dTAY+7pR9++PGfkfWT0M/ytO3+W3R/ehJOQhAwzYeXSUBIzi74eQG9dPtO85+zrUHA/DuagOXf2H031D+j/fDs35HOUxDr3335l+T+agP0t8VP/1S3f7Xh4yL68saFeQpy3/Xy8PPi10eI/PRD8PvgDz//Bkj/X8noVd/4DwpfC7dMI5C0X7/+9EP7GP7h559+6GsQxaFbfO2b/K9o/pVdH3z+ZMHXqg9/3gv4m2VWVvdy8T2HFr9W9f9ofntfWG6eBr+Pt58Xf8zE+QUtZiW+MX2a4A/Z2AJZ/2DHH99+A+WmBNr0/mMa1I//+I+FkvpN1VZRtwB1te8WwMFdWoSz8EaStov0WWmbcC60KTDsax2I/9nDs8RVtPjlf/mPEv7Jf5VwOACF7BELX7vq66v4/vK+MACtqknjtATFU2NU9UvpxqByznzqJmzD5gZqkzd24SeQwp/mD4u0XPzyV+S+Pna+1+Mvj5KbPuubtt7Mta3t8/B91uKUhOVLZh9AQTiEfg+I5pUPJIjSfC7ogHGV30BtnDVuszTPF0EKqgfAn/FBG1jl80zsl19+8dw2+VI+izG2eAJTC4MF38VZfPoEVInyNE66L2XoJ9Xih19/+2Hxvxf/ateD+MxDBUjwsjmQUNYPewBX8QOFgDuAA0GBeNj8199eBgVkSoCkwENplL6gEcRgFgbfrKtLzCd0RSy8EFgVWLSoq6ab8S3t3hebaPFdXsB0npoxIKnabhGEdVgGYemPgKoL1PluybLqFjPyttH4EYBl+OD6i9e4DxELkMxu98tCWasAcap8huDmhUBgc1WmwPzfff8cB0SaH9oF+43E+2I/R92idhu3Thr3xSNyn34BSPNtOyDuLsrw/qWc8TScTfVIgad5wCJgGf/l0k+zzwFgFyDfg/Yb78cad8ZF44GPzZeyfYU36BWAVXxQ7gHTuE+Duej/1yuk2qTq8+BhPyDpTOnlheDllUcMzqj+D50IP4BM7RZfehRZ4ov/n7uaWUVGFDVeZAyeW/B7Q7Ofpp8budlFz95vpgni75lmv/cf32rMt1L7pcxTEEfN+F/PlQ+HvdY8y1ffAMk1RnvQB9ECTD/TfQTzHJxNM6eB+6X8VtOB+ItHAQMWBZkPMmO23jeG8+w3SROQ3vPz7/j+cH4TzAYAAbuoey8HwRSFYeC5fgakauaEfLkRRHY4J+c9Sf3kT1rNRgUBBOgvgBApSDFQ99+/19nn7DfR/7Tx2cbMWx4tXg/ysXkQAHKEs4Cza+5pB8qS2z37ZqDn5wcRoEZRd7PuHognoOlzMGzCa5+2aTc7/mnXsAbV9tP8/tR0Hg1BiPpzlIBQr3tg3UdyzBFUzP5P5/oAcqVISwDawCgvIzwIusWc6aCSvrrKJ8XH8Euh8JFRM9p82zgrMu+ZAXwRAdHByPjHgmD8VZgAesW84sH37yPtO7eZ9lwUWxDFgOO32SfSvz/B+tkNLL7R/fwPB5MP/97Z5QG/5p8D4PMi6bq6/QzDT8j8hpjvoCTBT1nbB3p+muHuU1d9eiX5n2g91fy8+Pfk+ROJVz58XizfkXdkntq94un1AuqvP7H2J3ye/VJq4e9FErCvChBQs7NGANffEe3bEgBrcQNqCVj8RLh2BsY7wOJHSQeW/1L+McDnBAOIUcZzQLbVHxL/Ae0g2J+O+o48YKrsAO9gbvjicD5ZPdKhDd8+l32ef3wDRTP8JyeqGVGKOXLb+ewF7DtX4jR8PD0KwdDNH/987jw8Prj5+4ILQdHJ2z9G1wsHZhz8QxI8FQMKzcX94yIA5mhn3AKKzcznBHJbEJEgGGcFurGeJX4evuZ27Xsv94/SnAC8zjUsqD7PSPPxlengHej6cfG9lQZcX4ebx+Gz7MG58ae5jZ/N8NgyfwB7wNv3Td/P3F749vM/yAUEe5QPUIRnWr8L+fvS6tH+zyoA0t3ztPrrGzC5C2zgvoz+6h/BcpBtn9oZT2EQi4A5eH5GDZj7b3WWrz1t4oIuB2wi0CggPTwgSGxJkHSwdMF/16NwnMK8Je2hS2RJIh6GURhKYySJYJGHeDhK0SuPXFIBoPeMt69zo5DOcsxCAPU/gZANf58GQ8FLgafAs3W+N7Kzoi89fn3zCByslPB2wzxfa5i2PPhEelqyg88INAz3/cFMG80NNmJANTmiaEMas7JLJz2HW6q9zkf5tBQy/Q6TTCrGxoovSVb1G8g5W7sdR+eHNJa7bB/rARagwWUFK1SLXy57HI4MJ4c2CFXsNXm922cNo9TcZZUp15bfwTR1bXFuJZurq2zrA59RzlnxG/q49mnoZt/o5liPR90I4YNKQRIqIYdkR4WETHFqvRrUgd4JOL3SRaYuSyWh1YSFy+UkG5R5NQ8RomQE549Neqx8VrX0VHYCKLhh1GXTlOMGXt7roZBTG/XdjZaW/nHcEW5yFi1oy590qo5JcTdRUN9PGUFH53qkhDSKzvJE45tqFznMmsCtSOjbbIM3O1lRNEvH1ypsnrdXudRriDBUZQ2LlJRZdRY1Dgkawt7S9WbrJEc2OzlxiE45GihYHg6TnLbbfBq6mEt2yn5IONiGGsGNc/S+y9JQVpBqbTg25+cWSgvVEEbuREeI5O64PkLsuF1mmXhMpDPBrCAzNSvB1pOsh0WGKzMmcdSzkG2GTd7LRGPLS3y6Z5M4SB1j2iZjQWffP6LHU2BUtKVy4ck+hZaeV3EFWXwu8ZWyxA9Cqg9afF1ZrUXgbCDUiZ0Tp524Vzh4n2IVwrQ2bxOVRNUKnI/XM3vKPH2pFiZ+7seSXqWqfrwXHqfEY9bIG/1+WW5u0hRfh0Kf6nNyTPKNd+jSxAxZbCDk3rlVZx5OW2YVsEYZw9f6YFf8cWrZJD3eNrdVfWsgJqmDWDRpFM9NMbe3SWO4SZefmGVtF5TsdD1RY5tuq6UXf7VjXdJy9yuzcNnkMAqHQ6hW1w3BU5EcOHJHrW/OTmXVi4Ln58PQUNvoxHOD5vFU0qISKy8ziG2xW5Fco/RsabVatsT6Eie24Kzunkxn8VQkkEAd8npdQKHQlma42+/1hB7kC3EQV/1aiVAH2g80yZHiyHUXFbLVS4lTILo4mmkVriUzvd0m0X4DdxmBtiysIybeBulGVWrzBFyyHKL9+XqfBqZWB96ODtj5KHEUc9+nJ5lDh0a+UNtlSVCbm7rjqZ4mjCRDrQpWNhVuxFfNHuO+lU7VUcSFm1FsqruqXofJo6jjzjcO8XFKVu3GSQ6cmjgS4Rp1EWxWk12EyaAJaxkJhfMpiQw9KVpmQ5k4e5Kd4Xjfb3qFEC+Beb/c3MikLC4/kbtxS7DocLPwtIuOSu/RY7eFDjWPGga814a86HbwYF260/k4nCTZH7IVZMmDILQHVuLYSDzwWFk4qqYMk3nDiLiqekpeydFwFDqYyY61ruTHuzE25JRImoEj5s3ZwIa8SzCVs2xudR0NUG2Ldm+cz+rKhxwdUc1en45YcL2eNPtyPijTyejHKN0al/DG6WtrfRAG5lAaPuQ3SqdfEgdqjlKv2oQHnZ3pBPm+pa6abLUxt5dcpdYbiGVRs6aFDlHuDkVyOblRJ5nf92uhDcjtKi/CKZK4TqnLdWTHO/22yZaT6VZVLd0tvNQFFxsVTFMVdwUbWr6WGG6ER75aoTZcQw6RVidpR+JeEDom1p3G0kFdRzOM4XJjrzuiyXDI0npXXkaGiAWUREP03RrKTj6looCTPJ1qe7IprGMS6qHvUmPvknzm5HLi6qltmF5lHQ+8FqmBeG1bhmhxNbFvas3arDKMXbiR+3EV9TF3SNY9z7q9eOja0tZatYejcxO7sVbGmxJlpBTd2ScyHgh9f2CSfMWPJWsI12q/c5b9UU5DRuL4zSrVBsHZmizDsrWjOjRX9/s7crlKGtvKJgEbadoIKtEHye4cg5ivKgFKVg5k0Sl93rGhj+hIfswrjfL3N40CLaI2aGsuI/aYh6/2tymjqrI4jsaZPbCblVohFbK+0RyfRh5XmWF/v9H3C3RdNS28OibXbmUHe1ERxUA3ookkl6SqltNA7g6WoWITkXh801JpfZzWN1hY31ldyI6el6EQV1w0OM/ibXlKV5bJe4J3uTRal23ca9Mh9/25U88XmYKKCwn56q1YO8W0Y8r9dEFWcWZiSYFfS2slrPR0JWRWJkVtxZ5rh6lMdSuellGx7KftjvfLrd4N7m2tHpZ2PfCT1Q86laSGdyEaBMG6YZtHjZSvM5hgt5u1MCot4Q5CtKcUpgX1ZBJ3N77fGPISUQ5n2r43BSVGFVtPjC6sjWqj9XyZkXHRQ6Rzzkj+HB5NxSgmWqD3Bze2b3J4V0otxltLdpZdeV/drqgmbllc2jHcusPyyLEMnJEi5tJv92PMYEyXHoN+G+n0cWexS8UUVhZxGrRNv2F2rW065WaF4Nk+IuBzFAuMudQ12z1vKgax+RhXmWWx7cbdOE6JLWLXO87oKzk3tc0hWJm2feVN34ouRdo295bn9sj5FF2RQ7fkS+keB3TCIAfZHpQEl5ZBXzMQpEpCfN00Is6slKWZMdEFNBVWlQrjfV8XaJ5ElwoOt3Xq7eJUSAa3K7IztyNPzJ3Z805Dn4Sc9y5CEx/dui1OuhAiLrCmeIzV+1GvIpz21oSOjYZQ3I8svTZ2pojfZRfdwLbsSBa97jU9TO6bIy+N2bjcb7HkMGgRnhRDc1vRm6jodzp3YJdQZwYN6wDEM7WE3okmdYYiv4s3N8da91e9mRy5l7tQIkVGNRAaoQJ0MOc/+yEbPzeTsICt8ynMTMM3rklq3lTVyKD9TkNobNWCdNo0g6ttL65Y9vHpuFop28i5ogYi65nC5xmW6+uNah4qnjrnzirLG7cV7rubvVnG6hqt0bhrqZ5gepdJ3UNS3iXWwrmtIwrk9s7j0n2pNCIFE9f4DleHtPYn9rwcM4rjYsNObIeTyWpvZ/YOksYVZLQW6Chj92AguO0PPbPTkdM9H2IOv/LKJlWuhBgfcGe764t7uTb4uBB0i8v2x+lG+Ruowu955guWLkxhTjHMmRSv/HVdVI62icWL2q+4vLeTg1DCncs7MobpUhP5NXbRiBXehKKJWRlTr1P2wkoaQblS0qHMNjcMA4QbYS4Z6855rXLwD6kD3dpcjkZcwPmK7rZoX0VHVsxNk1pG56MQQNZOLiYYaa5GW525/a239gKI0kmFmDRyT/0opIpbjhrfc4oYyTJ2QhCNQMlN5qK2ubW1bJQxBPXPcne50ieiVWoxbN3cRnhBTyXbdcsUddI00z1EwIlN0iV6mi91M22roVQpaifAt1KQ94PZ0rujhUjFXsrLmlaxg6lc3G5kSh02DS5C2LpAWk73KD4ul2luG50ZqmQRS6pUZ0i7hvjT1YKRlBV2SBIpkp3fx+0gn+TOHvQq9ypnf4091pDMU7TN27y7iW7u0cbyzjaRl2QVaUtKB87Opn8wZCbIIyUKWK1u1/tMz0k4dXJimhCOMjZG02fq6HWIKcs8yzhntsiS6+htDZ8WY3wIhcDr6dEpSHm6VErmlpFPEtzR5ydjv6rD43I3mYKuWGUFQ/Imwe/C0vbkwO/d5X3HB5dhXRa00lIuqVUpLY07nEzYXNaTnkA6ACJcaijq2tAUVFhL8mXDXDaSGZd8zZeMMxaFnt9KZER52pAqxy2HcD6HRHAR8k0B3xDkQjg8p49L6cA6Zo2g7UTkinbYH3qW7jJhrGXQpF/Jk3OPgSU2dm1u/KPonOwENfUrQfZrimeouK43ULm9ChG6FPRESFQqpVz1Gkj7i+aK3FQ6RUYFYuhNl2CLsTB1XKEn955C6hLSU1I5aei1XmOIdERaQsNrdstE43XF0YnNsxSKem7mnQ87L3c355NzUQCyNp4KIpJCZQ+2NoSV432kHBwBbreg3T5d6CoVM7bcH/gDIUPrxtRrcNjRVpkzXA82ifb7E2P6wdDyDocj2X7bonRMX7DWavLU7/arJWm6hOCLEH84UHeFxSOGzBBunQcBUTduzZU+cbl5ZcTtQKtM3bydFhV41ymeSwxxgpwtFQMIugyBBNuyLhsOKvkcY6/WCdpe+rCr8OtwgOGc87VA8ipR2dd07rnxxRkoGh59I1mf+LHCScPZw+e4wMuqci10f2X0BBPxckde7TUyhSDhEHYfT2UmlzId77yikU9YCLWNckaQIOlODYN2rlNeYjevI/i2FOApv/NmurRgmC+prpzO2mDp1wLt+C6YxrNdDSJZXBqOHSfQWnK4PzEYdrQdBmbOjGhce8I5M4cz7ulafcVTKLtk7GgcjOaAri26vu4He5W7RH0CUd8sYTcLJe8Y7qudJhaMsu7OpVIP3iTxiOx7yFrtRQqicN4IibBABSzKOtGMXca/UQNa3npMv2rayKzI4C4KK9Sd9tlN7Y81J5obB4WPW7LLSKK+ni1r1Q6ld5a0jvVv2ha9NL1WRcPpTFWwdZkIMSU37Olc8aPNmKN9KLGpuXT9hER8pwgAFk59q1kgzSWq2KqeeuoCabytO1N1aT12eazdEBdn8tQKi1bcvsWdAyeFt7NSgO5zOJx1PtyIMrrJdWuryRc+koQE0qs433GKzFyWUyETROCb++pIcxZUeIzrHhAl70qHH9ijXa9FLPWhG3Ng8ohDO1ni6sMe41BnG+Y+0lR3hyUoDx6pUCmN5dohGMqE2XDrLq+WO2miQ6jSrWSJ9GAyh/3RVMMk9qpeCoPOLCTYq9zaRI6279zw3M3gK36R3KWChDoWnu101TOpCnBxM6jBwZlQYL81FRwgplijbGgEbEzGu/J8VkDvaY3IMsY6gd9qzqRZp37d6xyH7uK82dlrCV+lp7g/TzcJInW1v1HL6yXESFANDq6OeKTXOfRx29wDKwt1yI2ikNya5uG4dG85pWqOrx4Jig8VglrziuCGTVA5NWILGQcRKmFepcTkh0JlYR/X88D0oP0xurDMKaTvDNYzbghS8izdp2ZX9NN6Cuuc7rCm7PtGEGhwnIVRqieNfW+qWIZfnWnqb6VcFidfXwYKeSv7FCKlvZhnKL1chRh+W2GZMjVne7sts/FckqVX34LObQHOZZYMMd0V18XC3GbCqclXol8Ttluer02lVbjTWHXr9dLttITE8CRCUheQ5aFKL9drD/pqeBSO2zrLdWGUrrol0raHRr6bbBW9hMYWWnG8f4q4wbeZsN/iDkspeJVOQS95CXfYJct9ctpRjGsczT66MfF96V+Pp70UxvA61U8OuqtvUZwyaj2RbHX2aMosCEJHjTNx1y8QCuLITVrxtreMgxNNFqYQCATMcDQqibzZqdfrtmYuTRndQ2tpV+SkXdwxKQRdVknskIpusKL3Ma3rxBXoqetjeNnpe0w/1xpdhwCwCmvT3TECM81mXHUnpNG1cieOXQcaWIuA77d9Vtfidhg4SvFRJ+KczrUd+aaE+xFTjDWOoJF7EVQVshBLAcZbyh6Ppy6J7Wmt4tajI22OcN7Y3T2n2vsh7pZ+m9z0cu2uxbwKM3w3uRgdZLK31JaVexJsrQRGTAayplv9oKJBiVt9H9bLpUojurOENXR/tjwHTk7eHVp1BKTYhz1cK+PVaRE2O+WpUHO9w5B4Irvs0iQgGB52KxL2XZOo4Ps5YuvzTssOhI8O5HXpRHBIdnlL7iLxEHPs6kb0mAtqHdnR2p4++hWdorSbOMJym1wOlCrmNZ+4xGVXncWleIaGEDOmsbrZsMJmXUizI9qFV26lUFyvD6xbxL6cDQAo+9qhKwVboprqEyWjhBm33uyiVksZvZH2GxYUM9B9r2NeweQWnJ1ElDwEpzNLHMxmUHHuKglLLC0Op548n2gGnBMIknU4zFXxfssS052AG2ILFfBFD70lDKFCFATXm7YfLzfKDlYSCsE7dFUQk3abvHh1WRYkbks45HDM1XFUsTkHF5G2KA6Dm7renQidFiknUENaIvI7PAzQsj0SwcVq2B0RkcqEHUgfcKo6cDhv1jfx7Fqxp4oug273kqQlRdNst1gdXs4qP/Y3Bwujc+RvjjdaMtcYqlnyOmY6vY2IyWEthDHLvkrHDaq7ZEWHEqs5VEiy6ZDh3KVPzvcinmz2erQE9k6rYxwwtYwGIZUF98wMwhu6B+0Lj8LRDbpEzdEVJejghr7beRh/m3xhu4rpHSteYWy3OZBm73CbbqKMuF7ygarEu8oXW4IMfIyjeijaTPh+ZBE8pVX4jG8hQmau9GW87FUikly1TyLPbkJ5bURXge64AVeh3r9IvG1UDMP87W9vH9/m66DXpc6//DrI/Nf5/2cXAc+/53+7C37cnYRu8PnB6/O/FuPnj2+NnwIhnpcabd7Hr6uCv7vS+PRX133zjvH5TYpvN1LPe63OjecvD76lZdC3XTN+bav8ceMLdnjz/X7Ytl9ft//fL3m+Pr7VAh6rLgmb15XPny9Q0nK+yg2D1O2+Pcavi52Pb8HrOwhfZ43Dpp6Ve10gAp2wd+Qde/vt/wB+rsII5CkAAA== -->
