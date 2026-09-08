---
name: "rar-cowork-cookbook-scheduled-brief-end-product-sales"
description: "Builds a morning brief on end product sales from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended actions, then saves an email draft to the owner pl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_end_product_sales", "rar_sha256": "fb86e949fc70e0a0afa396cd1bc8b132af5696db22ec8762a2d017837d5fef8b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916e7OiWLbnV3HOjZiqumYenoLkjY4YBFRQUEAQqOzI4v1+g4B167vPRs2squ7s290R89eYkaHA3uu9fmuts/n1ze67qGzePr2pvl0sdnaWxZHfLOzCWzDlUDYp+CpTB/xfuGXRNbHTd2XTvn148/zWbeKqi8sCbN/0cea1C3uRl00RF+HCaWI/WJTFwgekqqb0erdbtHbmt4ugKfMFOxV2HrvtAiNWC045L37M/NDOwPIu7qaFporbnxZD3EWLrqwWq0Xc+Xm7cKZFnFe2230AIpa5ncWA3q1ddJG/ID969rRoSqAC4G/f/MYO/Q8PVRrfLfMcSOJ7C7AZiNx+mPcUQKIboABU93M7zhZeYwcd4PggWA4FMEWVAWX90c4rIPvbp5//+uENiJC9ffr1zc3stp1t50a+12e+t5mV5grv/NRXndUFuzO7CMGyagK2LsB15TdB2eTglgds9Lr6sfWz4MPiP/8zHewmbH/69LlYvD6f3+Z/Sl88xOpKu+2AIq5d2U6cAWu9L+hssKcW6Nn1TTG7oQWuKsL3587fKQFT/mV+9uOTyXvodz9+fiuBCPZslc9vPy3KBvBr+vn3+0yl+vGn96wc/ObHn36n0/ZO4gOHAmJA6vcvr+sXWbDw96VxsPiinjnmxQu4Iq58QPwP+s2fp+gvci+TfHku/rGsPiy+T3nW5y9A3mcwOoDu98kCG4Cdb+9JGRc/vng05c0v7ML1f/zpH5EFfnXTLG67f4nuz0/CkW97wFovk/z04eG+vy6WL92+0fzHbCsQMP+OJmD5V3bfDPWPaD88+zekQcKAJPjqy++S+96G5V8WP/9D3f6nDR8Wwec31s/iOUedzP+0+PURIj//4P1+84e//gZI/1Myatk37oPCl9wu4sBvuy9ffv6hfdz+4a8//9BXIIp9O//SN9n3aH7Prg8+f7Lga9WPf94L+GtFWgCgWHzLocWvZfW/mt/eFzpAJ+/3++2nxR8zcf4sF7MSX5k+TfCHbGyBrH+w409vvwHoKYA2/RPCAH78x38sxNhtyrYEsKW6Zd8tgIO7OPdn4S9R3C7iJzo2PrBrGwPDvtaB+J89PEtcBotf/o/7gPuP7gvuofYrqH15QPkXgJ5fXjj+5YHjv7wvLjNKNnEYFwC5Ffp8/lwAzC26mWnV+K3f3ABQOVPnfwT5/HH+sYiLxS//lPaXB5n3avrlgd/xE/kUhp9RrwU732f9rjOCP7VxZwgffbcHHLLSBeIEMaDzAejdltkNoOZsizaNMwDyMcAVUMWmZ23oi08zsV9++cWx2+hz8YRpbPEsby0EFnwTZ/HxI9AryOIw6j4XvhuVix9+/e2HxX8v/qddD+IzjzOoFy9vAAkF9SQtQHb1oDJ1wFHAtQA6Ht749beXdQGZuQgB38XBXOvmzSA6U9/7amp1T39EV8TC8YGJ/bk8lk03V8C4e1/wweKbvIDp/GiuDlHZdgvPr+aKWLgToGoDdb5ZsijnUt3FbTB9WPSt/+D6i9PYDxFzkOZ298tCZM6gFpXZXC6bV20Cm8siBub/FgjP+4BI80O72Hwl8b6Q5nhcVHZjV1Fjv3gE9tMvoAZ93Q6I24vCHz4Xc9X1Z1M9kuNpHrAIWMZ9ufTj7PPFXOqBY9uvvB9r7LliXh6Vs/lctK/Atxv/0RsAUaZF2MfeXA7+6xVSbVT2mfewH5B0pvTygvfyyiMGub9rb751Awvu0VM8moLF5x6FEXzx/3OfNJuD3u0UbkdfOHbBSRfFfLppbh1ndz67zVluEKvPlPy9i/mKVF8B+3ORxSDmmum/nisfzn2teYJg3wA5FVp50AeRBaSY6T4Cfw7kppnVtj8XXysD0HLxgEFgb4ASIItmHb4ynJ9+lTQCUDBf/94lPIzTeLOdQHAvqt7JQOAFvu85tpsCqZo5eV9uBlngz4k8RLEb/Umr2XEg2AD92ekxSEdgvvdvaP18+lX0P218NkPzlkej2AMvNQ8CQA5/FnD24BwJQLzu2akDPT89iAA18qqbdXdA9uQfXjf9xq/7uAUx8/QzsKtfAZj+OH8/NZ3v+mMFEgYYC6RF1QPrPhJpjp4ctDpABoAlIK/yuAClHxjlZYQHQTufUQGg7qs3fVJ83H4p5D+yb65ZXzfOisx75jbgmQV2Mf0RPC7fCxNAL59XPPj+baR94zbTngG0BSAIOH59+uwX3p8l/9lTLL7S/fR3o9CP/9609Cji2p8D4NMi6rqq/QRBz8L7te6+gwyEnrK2v9fgjw+Y+Agy8+MLIz4+MOJPhJ86f1r8e8L9icQrOT4tkHf4HZ4fHV/B9foAWzAfN+ZHfH76uVD839EVsAdI083on00zAn0thV+XgHoYNgC8wOJnaWznijoAeHnUAuCGz8Ufo33ONlBqinCOzrb8Awo8egIQ+U+vfStZ4FHRAd7e3EOG/vs8es3it/7bp6LPsg9vAEv9f2Fgm8tSPod0O495wOKgJeti/3H1QIixm3/+eQQ+PX7Y2fuC9QEaZe0fw+5VTOZi+ofseCoJlHMBhw8LD5imnYsfUHJmPmeW3YJQBVE6K9NN1Sz9c7abu8FHKfjyLAV/L9CfSsf2f6uMuPhT7QDQV/f+jK9gDLX7DBgU3JoryneZfetL/57TFTQE816v/DTXxg8vvAHfYJb4sPg2FgAVX4PazMEvejAD/zyPJLPNH1vmH2AP+Pq26dvfGhz/7a/fk2suP38vk+K3Fahfj473WaEG0K0Bi/vx7QWtjyoGIvdZ0x4p9l3Nv6bh9xT3n03Gs4y/vPwwgf8evi8G30/navuq9qAYdQvSzr/DBbB5gDEoabNNfjf27yqXj5FsFgiYqHv+BeHXNxCnNggc+xWpr54eLAfY9bGdOxkIJDNgCK6faQee/fvd/otAG9mg2QQUAmdN+BROBS4J+7AN24GNUYTrIY67dhAMtYMVQRGeg6K+uyYJ1EY9GCHXGOmtAj9YO4DeM3u/zC1HPAu1osgApig0wBEU9kBMorjnrYk14a5IFLYpx145K8r+w9Y0LryXpk/NZjN+Gzxmi7wU/vXNIXCwco+3PP38MBCFOD4KOdPRgIwVFU+hYGhxpxA+kd90f3W4WGPBXWmr84d2gq9NzYiTwME2DtA6Dckw34V74hC0wjK9YVIOxrcMXRc91ew2NHxL70J6X0EcmYwZWSQunmgnxUozc3NMBzETdgatOFvFVpjWqC59xd9EwKTsIOiE3fD8GpUUzR8MS9j2Hc4jzvpQ5lsi21jWOjvdpGbv1i7L30kI0qXRL/Bcqfb2RCesu8Juo+MaDrI8jyZ26ibhrN22GrG9d8k26SKPyMQ2LOTWES6paVMHQpqO3gHacfbUYHwaxzHlX5GpV3awE8kWU/Fe0g10i49X1R9zj3F3m9ELcZ7LySkShXOzZ9pp8OVcrzK+XO/DUfeCwqKWlH/0CLUbl7cruV5S67VM3sLpchpsQlaclST2AlFcVbM2YR7wMU61UKCFYFSMc86kQeIb7GAdLcgK/d6zLwdeCWle0aycHSHXJdNKNa/x4X4KAi7fLLm2vGPHQSN3fg2LqiaEzWA7XMapxo5Dl8zSKEk3K5Cu6m6yhzbRtTUHdjSPglwdFVpcHnVbZlvdrA2xCJlk2shtUieWaK6z+JgT8KkrMSoVD9PZ43LLv7mplKwHn/ZIl1gesKy/iOfDKdNgWTOaWI3DHJ+KcNC3jbD31fOazX3fMqJr2l2KC31ektLBkxpU7b3xjGk7o45g3tnxlX7s1Qrus/pMGMGN04maJdJDG0bV4cLDg8AElsenq/OW3Ck8xEfySm0cQk8S12VICxWmDY4dD/SxgLfbdtPpl27UttHNZFgm95Xz/eIfcybqitRypv0IM5m5i4qLHXVbm0HKYbe2pL6vqysv8ff1VEZd2BmHbjKrNt1sqFRw15ynaBV6TJdyPtnkcCAzG3fWpqGGJqQH4QVdR/7haO5TIR9w4Swm4u5+XTq7anl0LKKwEsLZXIbRPUvrXmpEMa/yKlTFg3/ebBkc9670YF2YEiYNsjD7s0kgpyEoNsYZ+HrJQ4PVQqerNEETs0+XxZEkrAA/GaGxg7Ub16vidVOVdAEnuoFFLJ9Pe9XOkXRlMSmWDwMduXucoVPzTGHsPqDteHXEN5hxEWr30CVHP2VQuzo5TbeBJ5do2ysXusKw2d346n7cIHUqdXSs4LR/3LhZRiwNvinwwqJzaMPX7K26m1djuqiemLR3Uood9OzSennFhmnZmbWdWSFpX488mnXsDs6zZPJK8xRWpyS9pC6cTGtIWNUAaqYAnYwTGKnsg93Uo7kHrb/bDmWHjl1eOKSrW969hbIxZ9GVzu5NeU+iMSVxCXdlYy/umVKkS3msRI2+LXNL0QIC2fLY2eR3FGP5qzZVDwfzrrgUfNnHhRxiybGhbuZZ6hOPFgI5j47I9cpG/qmT2USCc7RaY/oqU1sI2fBMyR4Npr3SfH6Pz7t0L27wQk3ZEznlZxWvRTgTyD1HK972TsL9tKaywy5CzBV0duHt8thO9XXpHygGuxw18Xxb37zhxEZhljthE3UUfjieUX4bCSVpso1iTo5BFxtEpuNOrFabyqUNFT5OWa/yjVCLkkhiJzCSxaSEhFhTt5KpHeSAXRu6XU7+zts7kFYqujag6B4zdhlEam2989JU0+D1hgAlcV2vHBHWnF3ky1DsLaE2Gj3K29/LSl+ywuAQy3hz2uOTfikL5OwvhSgjm3MGh1AlTapRsG4iD9cQ3vQnF6UF19r692TFqWuIW4XchZuuK+B+wY8U/sio28vRaE1UgCNGqifMociV1FJ3wtqp6gFtTQAHwiW/eNmK7c0xOtUIV6X1/tT2BH2Qac2NYEbE+EhTrj0rs3yJuX1LhXeDMw9OywzbKqKonhsy7VQwg47vb3Sk87B2toeqHyQ9pq7NTmZHqcUHofckfgy7slYRc1QLLw+wanKDAhnVjLnUl8vmXHJVAdu6fbpM8nDQSIQtRVeQV4VwTW4+JK0Zsl+VniTtOPbUQKvTEvLPjQXf2TU2rZcZvEzdwsmEItWV81lk75nDibTYxtfb5u7frKusmTbofTBdVkSW8RWf5om4att11gv1sVltIXyN9hO73x354r5rUg2rq+pKG1cNZ5FMZO1NqB5Yt23B137Lde1WSPLJU7ahpnc77upiGXdfEjf4cj83p75nMi2+dsyUDCRz5NszW++nIM0gPcycbHUoxI6cMinqzwM9yaLCXHpPUBShX+1lR74cecetZEWGo3g0bqnAG7uCSsLtMZS7OjpSgYDaG5EG9Ss2psMQcb3jeWGHHZZcj+d4hMv5pVjy+/ow0sI16uTmuFL4Za74OwURD1rU3Boyn2SBuJZ31sydVX20Al609kzcuYQIpXAo6lYGLSOZRtit23KCvra2mbtd8VMrqZYMsLWnJ2XpNOa0Xe0P6ni3bFaAOJbH1D23DkqY08lBSdV7bJ5u5eDhl/Ewaso6Wh8hPkb43My8QmaZNOVomDfRTtLHW+AIJ76UKz8ONVfQzElt5XMXCIfJGqcp0iNR6Wn0LumqvMclSlIlTu7RY80bbn5sCRTLSzOfTm2JqOOqU0eVLmRsR4+0J67ujrEtYlyw01SwrNUxw2ON8tPtedNXbLmhTSy20huyLpZ+y7n73rbsiMgFQR93e+bGHRKOL0bQV8ZbwaAnwREzWhFHmlTicKyDTXSE0Ji/TJIsdcyNbLuJD21tT3KVfR+zio1B8+DEGgMGhoCcDmGBwavWYrCoilAPRckVzutjy3C7/sjjAUkr2vp60xKrJTa1kY1eUU22XkRYf7QQGT+JdqGad7t20p3c93I+AmCveq5JJ5DkwqkaSq621psgKMvT5nrvdicqZmlQbkp9w6qZs8+HKWjZVSnUrb0XaU7OwmOOs0qQbSQuJrZp57VLB3FvDUSmuG/2RBizRqaO2toOBvGkNhwr6oI23VRXWU12P9HNAaiMXmDchKGod9iasTeqlxs5dvI0tLbCHeghePW6tThJDaT9Kh072j+f/NiGc5qlcMyCqCWklgIog07P95AoRMs7BV3QHImpKWVB1xZzKoEjVsCle0KpjD2iqQO64m+N4cJOWBD1pMVcxstUnaUIDQBftWiFd3Htona+zqy0Kb23ho5OZbVE1gN+7ZL9fZxyW6YsU2rrkLHkI6N1utImGt82Ir3nEE4Vtp5MO+ZOuAsa0x3AcMG6+W7ZexaimcGVIHeFkqRiutPwAMjBW9t2t684xeF1GrnWyslzc+XCwJJatL3WDIKNa1BjL9Vmv10n7rYZXO+GEJGWpVB6yLYbjzPEK8lqJ4Ij9utEpfrsWMdm1+rLNVsa52HTq8p2pAQKFFvUbGzC9i7i8VzXeINeNZtrl8jGlJm0UQ7hhr63VgkduJ2+x+B80sPWY/n9Jmam+1h63WVdNWbiihfLUDJ8PDEH6rDSxZifTvetbt1djgFNWDtqF/zEjGN/VavcOhKwAEWddJPHehQPFG/CXrm1yvYsQ5xD++Eh2Q5eQYOJaBdxdXpqYU+Cqb7fifWpRv1Y7SnBS228H5M+jfQ9qWfrZoVzg6dwshAp2NHF7iSjUclN4ceriZLZubEtiW52ydVS2eNQnuCGZnrc1100VaKuUgQ499vLMlqWtwutYAy84xNZ3dl3l7+YUc4kPWLl/QEzcWI4OHLvI5w8KOqNO4eSN0XJVku1va7w2P1IyqSTxR4mRxux3WxT98Dl3l64FwbRSJu7VR1TFV7Wm8Rq9jcBkUO0Mrtmc9NyZleiXmOuZVHYORgqi1kkZrk8dOxIXq7nOJ0mUZEvOG2cDhJcnbY30MFQHQKtjSDx+ybmDjlh+qsV0tQ4Erg+HC77Fd6VV8pbJvFxM7DXy86idQTNGUMb1rVCbe9JoF7IfWUKYIYQd+blWFEXoxk5PnJzcheZOzbRO88UxuOexcOxQ9qL1THBac/USRtghwSxrNiZSuUQbSeW2zJq7JpCnUZWutzr9o25oruuqrtTk7AGNuyz1cYlO4E/yqmZ6deQ8gKvqKdVezv2Tg2H6rmGBaofcEcHTedeCM2eXzbOCnTgzhVT0egMJ/gd0WlNzVPNGiyvsldwkNJLzZaaoOQhUrhqB8mvdAQT9g1/zQzNhjqtOBnXDuH7PqEYBfNdVzJO8XWFubl5gJ22FUOcVKiRT7jEqAUqvnODeCdqEmxJS7SR6ZwTO/oQK7uUxQKLIYotr56MlOW5+7AWakNSNlUV8HvbNm8ata71DKT/Kb3YhVMhxClVvNZMY4twVUxyjoiVXvZ32xv7naWDDtS+WnB9sLzYH1f73gGghADAbfpoa7r9Te2qsjgL2IHqjLijatLAXAmMXO0pqYykw5H4drmf6ik65zXlWNgR4dfn46rttj7qJKcDjrSBDYYX6Ajax1TCYTbpSwpxFfhU5YPRIII3yFmiNkcyADO9mdS4aJwNXdUpp+2WUmpcMeN6wTH2rHbX7bUI3GIZZaGRhWLhgokfEUuGodmMudp63BKrXafpvHEalp1Ddia11eM7lXWnyKoyS4ZqNSpJTDNMSun7M5/ya/ewusKNs0bXSzIc5OsuWVtLery27d2m/Ps4FG4HQWfkttxsna2tp9nNaYK1fmZl0XObbrmSrtKdtfOovHIY4tUXxKimvZTc5NxLiYuLn/V2tyqhUhmk29Y8p3C3xpmdJjVHLpCHIPRV05Ca+5iQlTii0o46w2g7/xlJaZ0laXb4+ToMYLRc7RSZ2KIGTt53hejWZjgucWccgxt02uywLgWxkefH0/0gb7dZs+T8280n7cPkje725g6BsEIz1ONNXx4nFfQveUwU0tj78eXW9y7a2Hq3irFRM9giWRuZSRBpfUY8fQJdvgt5Ub+8nIp1MFyEcAP+4wEYM04oebrjYHDl0aqyiXF7VWg4BfBIWrXeVEt9qxMRahxSRkEpGQVjLepNZ8O/YlfRTOj7cmyXgS/fxqtxwCn+Sow8Yqt8pFtcedukflZ4bGhsq5QJLXy8cFAAZqXrOpX2OnW7gDnyZIobAXVji659JWSdsafqXauc+2MWCXupO23vEcnf7vaJOIt3YUtAXRBP1vl8vkkUhhGhe3RUle5X9Yq4+uPJ1bGSGg/lEr1w+zXSro9SnQ+3u7G3SzHoYe5eohC1xTlv67DdpHQqucx7uB+5o79JMUl27xwJZ21LpJZl6PtK4DuLPku1kIGxoI1jmyDYKgXZB512lDaduZ0HY0oTHlMsxJwwa44ms1+thS62+5t1Zm+6u7SszNglvZuV9Kq5A1hkw7ZmHO0eLu3jhuLce5I4XK2YdoSWrTd4UjpQpypLVrlBc0pGd0hdeB7K0m0YQCp0weR1XcbiiIv7/UFr6sQba5bAh/bUu3RHhrs0aG5RiK+Q6q735hqtbCg4SrfgfLiu7NhSINQ3vBq0SmeyHkurW8HHpLvzeGUL3RSsyv4E3NPtrl5/cRBjizXcQHoB5uqxbMBwH+tdTridnw0qjEwE6FjTQ7P3NCRki9jZGe6pMyyj6+yyN7NLde3hQaPO1rVdr1a1gh7JDEmhqNxnup8HCc5vqZzfXeVDcpqKmNWZ5a2Lt+0pzPbWBbqWSyoW8WR9O2I00yWGLAZZHjFHSVyaPbPzjaLWmd1+nWpoXK1hN2O3Rq5yiCwmPlHa03SILGm/DpOklKERPXbpGb2YnUTxtTit96l0ZE/HCZS8Zq2kUKe7o45apD9Fe5ntDGda+Qwta7lLt027PVOqTIp700niqaSGbhOW0K3plDO2lh2lVwxU0/bVBBcenBFaYBuhpZI1rOM2VziEjvuIjzXqJTOklWV7592UNUVDbi9qK4WF0eIgxpZnFnTxNUNM5n0fyG2ygQLiItzuCN0vb3CSL0vWTrPEtSp/zwHTKqBBAX0jZJPZTYQAeMUqdbsKY8VSEr3Va18bDljabveRgRh1RoVecr3E2HErEBcPt120y9q9UbhTS2DXMDiTRk1sUN2HPQjROGqd5JC+rjbkchgc6ba6T/XYnkdYyVX9qhIymcrAE1ddtiFgi/MSsVbdgQk0Gff60O1SXOqjtidXGoFdSqgHJSHs7iudt85Hos7yPhA9lKxY2PdLJcYoFsGnOLbiwNkpdr9T8jhqcPeU+c565REtiih+tHP2q7BF7kjtu0izM9cXSMDT1pSqkmWsltohx8Jdw71DkHTWewqYtiNumBiUZDiVoUxCKPdE7ZNrGpcYaTDbHnUar5Cye77dH4S7tF52x9i+T1hxNLwmCuRk0jxKsVjEPuOn7YYyeS3QkX1wwe7d7VK55SXTikBzrAEqG2zHQSv6BlGpR+qBBeAnXCVXGguvZ7y3ElqSpH2jN/0q6oX1Np4IG+k5TDVQQ8YsKqvEM+tCkSVSoBshpRPOBxusPwygXo2OT9lVFRsxtLSjxjiOyBBT1S3wJH7w7qpJIcSmkltMwoTblKzpznM773iP0vVO3dBbuYcOVaE6JlMmYa3WDMTEq9I7scroIZ4zNhV/dU/8itTuuCFbrWCrsL6/DMvDhhL4/qb0VuC2oG+TiSUkeh3Xc2eoKZZjEd/hnQS5IrpCYqyr9uG6phCauPZnhMz1wQCzOCvyHVnr8vayl5hdciz9XXyl3PXxRi6tJXsJpWlT3hOqVe+wYt20tXGsMtGCNveYgMgjjTLrscwaEDHGde0zgS3CDBtJG5qm//L24W0+WH0dj/7rr2fNRzH/z06Enoc3X9+3eJwM+rb36cHr078h018/vDVuDCR6nnu1WR++Don+5tTr4z89X5+3T893nr4e+z4Pkjs7nF8GfosLr2+7ZvrSltnjfQuww+nb+f3BdpbPBd9/PNz8GzWeZ5txWHzpyi+N38WN/za/5De/TeF7sd19vQxfp4Fg/etU9wtGrL74TTWr+zq2B1pi7/A79vbb/wXxZwsj2S0AAA== -->
