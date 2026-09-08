---
name: "rar-cowork-cookbook-adaptive-card-define-sales-teams"
description: "Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_sales_teams", "rar_sha256": "34fd94c017a473aa96c22ac7df8acb4983d8f11bb7aef2e3e7e1d4fad880f36e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
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
    "action_buttons": {
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date the snapshot represents, used in the timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "Number of KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 34fd94c017a473aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_sales_teams_agent.py` first:

```bash
python3 adaptive_card_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_sales_teams_agent.py   # or on stdin
python3 adaptive_card_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_sales_teams',
    "version": '3.0.2',
    "display_name": 'Define sales teams Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c85f8ef5bec40be8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the snapshot represents, used in the timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'Number of KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define sales teams status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-sales-teams-2026-05-24-card.json' that visualizes the current state of define sales teams. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define sales teams KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of define sales teams status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the timestamp and filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Number of KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of define sales teams status pulled from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineSalesTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineSalesTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'Number of KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6eZOjWJLnV9HGmG1lDZnBLVCOtdmKQyBxSOKQkCrborhBnOKGmvru+5AiM6u6s6e7zfafVR4h4D2//efu8fjtxW6bqKhePr/ovp0vBDtN48ivFnbuLdiiL6oE/CgSB/xbuEXeVLHTNkVVv3x88fzareKyiYscbBf83K/sxq8X9qLybe9TkafjYu3ZYEHnL1i78hY7fa8ugjj1F11ct3YaT3EeLjw/iHN/Udsp2Nz4dlYv6sZu2noRVEW24MbczmK3XuBLcrH53zqrLIICCLgIAd18kfqhnS78vImb8eOij5toEQH2fvVxIR22iwZwqz8utLWwqIr+40Mv251lXgBFmiKvX4Eq/mBnJVj48vmXv358icH3l8+/vbipXYNbL1+VmHXgHsLqs6zGLCrYnNp5CFaVIzBkDq5LvwICZuAW0GzxfvWh9tPg4+I//zPp7Sqsf/78JV+8f768zH+0Nl80kb9oCrtufG/h2qXtxCnQ6nWxTnt7rIFZm7bKZwPXwA95+Prc+Z1SUS7+Mj/78GTyGvrNhy8vRTk7Bmj85eXnBbDcl5eqnb+/zlTKDz+/pkXvVx9+/k6nbp2b7zYzMSD169v79TtZsPD70jhYvOkHnn3nVfluXPqA+B/0mz9P0d/JvZvk7bn4Q1F+XPyY8qzPX4C8z0hzAN0fkwU2ADtfXm9FnH9451EVIDrs3PU//PyPyLqR7yZpXDf/Et1fnoSfwfXh3SQ/f3y4768L6F23bzT/MdsSBMy/owlY/pXdN0P9I9oPz/4N6RQEbP3Nlz8k96MN0F8Wv/xD3f6nDR8XwZcXzk9BxlS2k/qfF789QuSXn7zvN3/66++A9D8loxdt5T4ovGV2Hgd+3by9/fJT/bj9019/+aktQRSDRHxrq/RHNH9k1wefP1nwfdWHP+8F/M08yYs+X3zLocVvRfm/qt9fFycAX973+/XnxR8zcf5Ai1mJr0yfJvhDNtZA1j/Y8eeX3wHy5ECb9gFPM/D8x38slNitiroImoXuFm2zAA5u4syfhTeiuF6AvzNqVD6wax0Dw76vA/E/e3iWuAgWv/4f94Hln9x3LIftd0x7cwGovT0h+O0BwW8PCP71dWEAukUVh3EOAFZbHw5fcjsEQDvzLCu/9qsO4JQzNv4nkM6f5i+LOF/8+s9Ivz2ovJbjrw80jp+4p7HbGfPqNvVfZ+3OEQD3py4uKEz+4LstYJAWLpAmeKI6EKJIQXFpZkvUSZymCy8GqAIK1PigDaz1eSb266+/OnYdfcmfII0vnpWrhsGCb+IsPn0CagVpHEbNl9x3o2Lx02+//7T478X/tOtBfOZxAMXi3RdAwkepA7nVZmAZcBNwLACOhy9++/3duIAMqJkL4Lk4iP3nZhCbie99tbQurj9h5HLh+MDCwLpZWVTNXDPj5nWxDRbf5AVM50dzbYiKugE1tfRzz8/dEVC1gTrfLJkXDSi1TVwHoFy2tf/g+qtT2Q8RM5DkdvPrQmEPoBIVKfhvFvOxCGwu8hiY/1scPO8DItVP9YL5SuJ1oc7RuCjtyi6jyn7nEdhPv8y1+307IG4vcr//ks8l159N9UiNp3nCuaOI3XeXfnr0DW6RARzw6q+8w/euw1sYj7pZfcnr97C3q9kVLigDgGnYxt5cDP7rPaTqqGhT72E/IOlM6d0L3rtXHjHI/X1noj87kz/3NV9aDEGJxf+/LdCs7FoQNF5YGzy34FVDuzydMPd8s7OebSJg8OD8SLjvHcpXFPoKxl/yNAYRVY3/9Vz50Pd9zRPg2gpYWltrD/ogboATZrqPsJ7DtKrmhLC/5F9RH4i9eEAckBpgAMiROTS/MpyffpU0Aok+X3/vAB5hAGwPFAehuyhbJwVhFfi+59huAqSanfXViSDG/TlN+yh2oz9pNVsYhBKgvwBCxCDZQGV4/YbEz6dfRf/TxmejM295NIEtyMzqQQDI4c8Czi6Z/QbEa54tNtDz84MIUCMrm1l3B+QG0PR506/8exvXcTO79mlXvwQY/Gn++dR0vusPJUgHYCwQ9GULrPtIkznkMhAgQAYQeiBrsjgHZR0Y5d0ID4J2Nuc8wNT3vvNJ8XH7XSH/kVtzPfq6cVZk3jOX+Gfs2vn4R2gwfhQmgF42r3jw/dtI+8Ztpj3DYw0gDnD8+vTZC7w+y/mzX1h8pfv572aYD//emPMo0OafA+DzImqasv4Mw8+i+rWmvgJwgp+y1t/q66e5CH565venR35/euT3n+g+Vf68+Pdk+xOJ99z4vEBfkVdkfiS/x9b7B5iC/cRcPhHz0y+55n+HTsC+yEBwzY4bQUH/Vue+LgHFLqwAyIDFz7pXz+WyBxX6AfTAC1/yPwb7nGygjuThHJx18QcQeBR8EPhPp32rR+BR3gDe3twehv48kj1So/ZfPudtmn58AQDo//NRbC452RzQ9Ty/gdQBzVYT+4+rJ+S9vUPefOfPA+wcmdgn/G+gcUYZ0DIDWYuvVbDyZvmasZwFek5ic+9m129F8OYBI/09bQ7cfQZrDlqcqHjU67mFAqZ8VOFvbdCcTAD6s0cOP2w2a/5Dhg/AG5q/57Z/fLHT1wXnA3BN6z9m0Xvlmyv/H5L96TTgLBeY7OPCe1QxkGBAgNmaM1DYNcg8kHQ/lCUp4zdQWPMfSKO2mQOCBEDqt2I0GzXO3bQFEPQB/0T+/EOaj7L29ixrPzDpXAv/WPkercqjCwL9xQNvPi781/B1YerK5ocMvrXif0/9DLqgmaBXfJ4bgo/vMPxxjgVw9W0SAqZ6n00fv0bIWzD2/zJPYXMwPrbMX8Ae8OPbpm+/O3H8l7/+SK4HVr99df4PTDpjMDDo7Ll/1F7McVsVXuv+KHgAk0f9AFV4lve7Ib6LUzwmxFkcIH7z/IXGby8guQCyNfZ7er2PGGA5gNtP9dxawQCAAENw/YQK8OzfHj7e99eRDZpfQAAnAm9FuAhK2QSF2/Zq6WKY7VJeQNuuQ6xo3KMDFHUcyvYDzMd9ykc9IrA9mkYCfOkDek/AeZv7x3iWiVxRAbJaYQGBYogHRMAIz6OX9NIlKQyxV45NOuTKdr5vTeLce1f0qdhsxW9z0ANhnvr+9uIsCbBSJOrt+vlh4RXq+BjsjLIFW+QqHsOdZab+QZXrclOXan3JPGafNmIRT7Jmt/2GS/RdgWrG1lWKZXux10FRQn0OGdBUJtcuMa5G7uBN061D/TSS9Xil4dgbiH41Da07ViepVBlGls3iKnMGce+3cSrJAyocN/79tmE9RixSGO6QgKhS5coQpsDEW2vtaCqPx8E5cHOa9LthV23MbjD9ZIxVC75nx1tRq6dmk6Y58IDrlIewRKQmuC25HuZrmF7u8aREs2x/MuwwI6KLU+wuo6QdB4uI5fQ8bE51LcP7HbSjcRnRGTTQ+E7EaWtvlKR55HVdZ+sNU27Ta2ra+i4PEeFG0nAAhIV8FTcQeIOgQYd3RM9DEGYWWmkWbMsqZZxBl3CC6vN5edoIgsHotYVwKi1xLDFZZ85pEaE+5dmRGiA7dIbrvj9yY7Uu3CFjcsdTDjUnuKMNUi0lzAvT53GrE+e1tROKxjsKZ2CIqw1tCaNW5ImldPuWLpfwzWXyUsYphY7OLLvbaUdtF7FUc0PWCiyf7IGtr5fxHFoRY4XxwRHHJDpKuhrE7r1jnXMN79SUNqjjRtisN0GKZLyaUFiJkiQetYZ7kKRSQY6uU8V6aNhbPQ/7067a8bG+abmCjUbmhIZh32brgMTPpuBY4XnTR456JHOZW1r6PWZWQp5LjlzZBpTgDsn7YwJduXW9lXRMrrbaEV+eGbm+Kd5tLblrZpIwHTKJnCVIBp9onRWNoz9wPBERhH6wYx+7o1tF1sWDz+8MXYZsa+zDwrmaWzWRSSox2eSCRYmxTIuNvUcLkAVXMNTcd/rWu0MaG2OYhHqDk1+vpMRuqK1LEQXOmBtom3TmNLHwIMmoQ8jINVeSG+/CLOhA17Tp9/uto0a97ZNicchWGKbKtI5JnLTKlBWXRzfbd5QedxG1wAv/fPD9HlSEuyUmktGNKYORunetvZGHbpSSMX4tsLBIYQ5+PTgTWVNmCvWreL9LIOgsLrkTscfru6rZ+jZNSLxmLR1Fl/UqkcTWLaSD5XGwwE7jkU+E7Xjgt6x/tRpijZI38ypDhZBfyc0hUpMQu26LpeOES+fi1/g+lECUJ7bOI1ZsbtKCCO94z4lWuUYJsduPAR4EG5CTaMGTxL6Z1rozCvRBiUfJUaaBWK5iKzmoO43Yw9N+KVj3zUYp+9FLIf5yPcQdd8VMRT7ylXaXB/WokfiEHVKFii97iGL85RZuTohta3c9WC0JQnQSbnPB6g6MXaNj9Ufn5uX5kTzxu8uQU1CNXMveMWqtP52r2szqwGWCWJ2QaeT94FzdkWo6RhkKJXDhjrJ+XJ3WKZNdBtMU4eC4jzAwU0lj4SfBLs37pZXKikEY16qzz5C616xcREJr8Igu3RurHjrh18s2d0KGc48Ul9SpiLXSWBcbZd1mBn8Q1nneBckRP5yIzbmw+HrqqVVlRUZkZ1dfWN0yhi6hjTGIyYUh6fskqr3HRDaBIypmVLG9cy6cfCTk2zV20D5eb+yrAW1OxNqTmDjE1RMYP2NlZ6dSgyrOoR1IQiYLhBKStkDW4gGHzmmuGt0kRoFmXo/y1XXFgpymxhyK3VK7apTRM82x5fLd6AaW62SR73iMC8EJtvJpCZbxJKNDDlEJd+Byxqu2w31DTHgbF559NwZlS0mabTb48WZSW7NnUwdBE89O9Gp/SDRuIo/ntaZ4srPlguPk1GOhbrY6fckwydWylSVvoFW2K4TJv9BKwinX9jii04nI8Iu+SSJD9bjiqpfA9uxQHYmG7wrXjOrtZX/ltjpZwwCpBitwI4fLdiy7Khmf7Yf9ErddcdvakHuFLszmOhTFvomOKwBSm2V7Vlzblf3B5lxQ7fN1wJzz+5SnykGBuykiobaqpeNGlSvFhHo9Dpj0VKQ8n6+2Ca6hx6UsMhIbs61WwxDKc6DwO17DCXzuyM4A1R1pVcxYX4Nc7XYOhHqZmfuaCdH0cGBO9bFYj+PuSosqDbFnvmFP8sm/U6wSXnT5CMdqYTvSIUf7RmO7ZHO7TTZRS4yxHMSMs9bX4GToddgWZSGWkikgYd5LXL70juRuzcbHmkVGyctitne2481XFdhRqdHAxhMt0nBko0o9GNiabf0VdeuT9CSv2jMVc2K9rdteTA+1AkuoFumVyNFyfEdXqC/WXtQzwhHXlsf6NFA6fMf4rWOfAS66nnLRkFM1NaeMjFqJ5gORQNWN4EdHpIE2YUEnmH3hYviswRaP8xxrmkpQRF1B8Xxq80OyW9+qjNaFYekxUMdiwaZrAc6o6SVsvLzsinvN7pjtNqFPE6q3MZZsiengw8sNn5u703jU0vzSHu7D7hh5R2RrTbqb8fHOItoGEZhcSvtE3mnkOglLFtKW+Y0W0qz2WTEu+ImtbFNEEFrruO1pSyEriS635Vlu67tE7tc144Rrx0RgG+q8MaNt5ZwzF1lYl4odaU2KWz3w9WZ3xKowPp/9FTaRRh75TGCQaBFvRqKxBSqJvNzS6RNn4haj+9ItDbhtdmJR4sCs+aN1UF3TZZ3JwY7VscVGlYV5Hq+QbEcopOQdARLThqSM6R3WiTSRSBGzyTFqMlDQNQ6NQGti3DYdARqeQ3mob+ZwNdTbWgM9RKvco+FwdSDkur7eTJDwMr23qPtO2K+hS3oQ/M10vG/qE49uLE2Kma5qtgWMI25NsKsa73FhoHYRIQvjJU5EZUNL+CmILEkr3OjEnkNyB618qxypMo/wbhul+/6iwifG71Ee03lcFG6mWqAgp0ZDU2773TrSp15e5pJwT5VJv3VmXNyOvI1qKsIYFpqxRt5jF3a8E1Ei7EuVi9IQj9yNuN+ssXOXZTxtngJKE3hGJjJfVE85LXKJHLGTFPaXu2PtMmlF7rTiIOKUFt34XnV2tpYeLbJT1qxZ7VVBtvM9pqBblFmzKcOe+2oXSjpZwEimFtxAGkuyGi9HHDe8G4yTUHZxktuR8hhfoMbkkFJ+Vy8T2yVtBbkcWkG3Eas8KIkoaM2mF+/l9uQJMAy5vH/NkdKsS1ZPtD0+smZ8PG3vyvqculwuMG21YxQ6LNu4v58OXgOZPrXtIPIAY0tziHS8x3jTc26Cj+nHyJ54LIStk9pfycxN2vLKJtnR1C7CClm3BYB8ntiEQ9WlA081icTze4wMasPYTmSWGOZ5i2dte7+oxC4h1ajp6s1lA8X6VjhJzTkFTXTCYQKvqry2GfnjJISgd7bQtSKvtmZ2DTb6hkxZMlWyTo0rt3JZRtl39+x+Xd0xXWGXGkwsofxGXOhxbGsMWZMnzNgbvuyQpRDrYqisov6E9TEp9BO/goLOGrJGud1XHgb5Vsbux2EPTbezNIIuRWSmzZYw0xIP6vhOXjlPQPTKPvveaQyQIeYbn7rlWxuj3KO3XOLMJuy34mbJ4KkYKYxGjJpnLnndSEKdQr3yvBZ3F35dm7hyuBJI4Tk6d0HkOjIkMk5hhjmG9T4cLXpv1mJECyCIl4EwOskxq9aWauYyGmYwv9JhZB95QXwxnWLsqMv9QF8slN5ajh+Wjoy1K43M0cM+2+iVZ9r0sgdTJXaSRTm+ravMVQ3EuWP3EgazQgBzK3XJLQO087dxaSST4t6QVpgmTrn556NkMlgwRpA78Syk4uyq42rQqUZnBD2F65G3OCWqu3Evu2xGdYQeM2eTwJwMSLSi2WMPgo0N9/c2E8Re8A/HVSxwXn8EzRuXb8XJPCtGkmGUwfu8svUPelOcuHJwLhCYMc9s2MuxiaS2RGD31XXlJ9R2XZ2Wywi7Xv3rtBtczzDJMDLH9bVDbkMKWihBrOtGhCVQrKpMl47ISjcuvbo6co0xynwh42Td1SiO4K2+Cs0wyRkzHKuDTzdX4tyiSVOFuHExg1AjhFsh0Bnb34Rrsj2ja7HiGXKl8aQM56daKo4tY6lDe/fNSW63eKuYuV1eiw5tlQyTJV4szuupzMgiu6gYwle3LQ5v+C1sbqoLYTiqbgy0cl+5vJiohpK6HrEXum6tKvW6xWOQkRJrq1xKCBsk7G/9hq96l+qyDcxwUhIUY3U87zKsuvSb8zx1EEo3svc25Wy2Ydwuv5bwMIDQapvkKKNVcCZdB2Xaa52udhIMhvk4Vi+kMUDkROOwFAuIQqcVna/XoDeluou7xFRjHy2NEj4m3iHfWfuRi9ZQy0VKEzKNTQ6eWfon2YrHYoNnMXfWEgNiEsttmS0V8rsMUmojp13itl3zbCHWLjbu3ZWNbjJMO7pC3a3Wjuqky8RdupeMS71zOLoJNVDmubYTUbVG+VgYS/Z+2RE7jd/fJBEkYLLxnPy+J46YLAf0NCgqgm310xnCSDU1tRXjMSWjTKRE7ZFOPRS76USxNGtDUaHexItdnTqYEU31HLFBg5I4N+yvYAjIKdLZUjV+3mO7/OKrvjcMppf7eIW2G3V1paSAK0/GKavwVusBbgdKDCvY6XSwgthw3R0qJEMVRlh9MipIiTivxkrP0ogaMhsrm3BXXXdHmQgwsZY8obPyWCJWd9RQY5lI4eR+PSwjYXnZ7R3QdkPaWlJU/VQl/MDbxOribA+nLRNgTVVcYCFEOoLc5hqY5Go/p7b5oAmgXfT15a3sLtAV5cx1GhWwUA92JthDGa5U4iJ2OxieRBwWOIeF9+PBUFAU3hj9gXG8eBB9SR5HLliubd2EWTLZDMPN6KlNfdYGJEkCYy2u4X53snIAX5VURhGtyYGmFQ7BKaq45ZKsgc80fZmQ7IILFUB153xpuVSrqaS9NsRh36PXQkkyAr8GaafwboSm8SQPEXcQoT2Sb1I/sT1IHuiyUHbbRtvBoPdbLqlV0ye3epLtIaQNqgEppmn0Lk5ovRT1jtnmLEyVworCwOC2ZBHLskSt5v2DJp1vRzrXoLgoSR2qRGqvnq+chl56bbdW9d2a9oMWU1tqOxFDE29rrbSXqHjmNiiaRGdql52qO3ZOCY9V/b3LxuPqeFaoa6ZRB8w+VaB/1nrQ7WeXrpMsQi/H7qALbc2q5wSUW0GT5f4qlg50C1W2nNjjdnUhY78tlzsJKVv5hKa3Trrub6yt0HdNPVr78LhpiM5XubOSB2tL0ffyxQuXTD16zNlqOknCkJIBM50z4BRMrbDzkB2i9bIadPw0aGDgYSie7E1/wvl77kTKEUxXVnTxEmwDnellum12eGAYN9BeiIWH+PUVN2kk0hEVJ7FtWSXbiqS46JLZSYP22M2RlgdLPy7bSzRJraeuSvngNpw7YMjVkk/Zzat39zu/l/aH/ChiWtj5N6Njl3HVU0VaXyHZ3i/TToD3JLqU9bOIQoxv01OlaYE1GMY5dpeydq2Sk5FPd7x0wx7lotvVCJfOkC5XjixODLI2rxvOIxLrpuHcug6D6wRlUpSeNMW59Tq2d+P4vgFxelhl42gPPWO1a9sDCUxxQ4jlTbsEgqTVdGl0lV5N6akRBg4+0K5wt1yCbjdsmlnRylV8b38wzreWxw8rACG+H3FT49j+HUwsRO5Qw+QsVyPLp9gyWy4JzGujATbpyTarUd9dep/emtha9Xfl3Ycz0jUFoHex521VQodKHIlyv8ebfRr7KgaxHrRqRHqMcBeyppCa5ONmPLpRejVI7h4Fp3YA0XjZGJk5He747XyDDoHMLse1cU5HQybIwrxR6IE+Rgd1mtB1dOMgXbIME7oqehSXUynWxzKRDhcytepztNQHctgdhusm6iyxIgq1QRJQNhvQVaHn/UVIfYwsaTWBm5M/nMjs0ESc2rN2TG5l16zDcl8EdVWzh5W2plzx0uNMAgYSCkwE0LVzOoGx8SJDKrpu3b7Yn5rqTKmHRsHohhkrAt3ep4NS9Ga1XDpNecpypXEkDHcyqUHh8nopnaOCVnfxeqHqEVMmu0fvWT0QuOz2bs52E3UkjQm/jctTUlV+IZs4f7JIX4T0WBGqLSnclhgdrTAi7QA0l5R2lncBmq7vkT5iqk7vyC3NxqVrjuqm1kHDUpVmHu3xKB2FJDANXx8ktAuW5Qh7UFeK5ZEECZwVCQWtG+hO6qC5T3nIOYxWussrNkK0TBfPoN84bEOP7us4dE/aAMGUhadwudkeIL1AWyFdMmOeV/VeDTEaS/et16ojhK8iqmLJTiIOm01zmvDVnhJ2LkjFATEhQm6j2h1Uw7hOFdP3dHhUPYNE5MoOKxrxsUEmkVMdZJxeWZ1JNxV+8okM4tDdJQyMowCmJ+lQ4eKdLGgcxbSDu7yFAq5vwmRT+9tovUNvdRa2traiETbk9zgT04fRcBqyQEiNKdNAmngNcb2uvsg9mluUVTDw6aYj5344cZg09YfTGXUIW7PQyTUsPEtXyTJu92WDrwVYs6AG6jEMghmPopaiBBcI00Cr7YoliQ0XdOsywuh75GCjabHaSTx5qm1J1tXB5YKKV0wlyct9MNa5XyN3NKlo8d43y8GibnY7+bjFHRSJtpvyrDb0xF7jDu68o1Zm3GTLeNLtPC5TZZq7Hqg29fETnStcnhUEvz6xOJ1l7q4MpXjPllKxy1yr3JW9h8vt3fZVT2KndBAPfhbMbVV00LW4WLZiczyUO169q5NMpTff45kuoASH6aJlR3owtl2d/XDoqjTH98l5tdrSYqq1hagjQwuGeYjNEjGxok3n6xJ/vzSFhuw0rodOkWXtcejQdaFJc27o74nuiI/N2nJO27TLoNOQQ/HeqYayVgkyZuNze9ZczxmIA7028ThAsCu7Xq//8vLx5ftR2cu//PbZfLLz/+yA6XkW9PWFk8cZoG97nx+8Pv/rIv3140vlxkCg5yFanbbh+5HT3xyhffpn7xfMu8fnC11fj4mfB+mNHc6vOb/EudfWTTW+1UX6eN0E7HDaen41sp7fnnXBzz8eYv5JieeDen635K0p3u5t0cyHbHE+v0vie7H97TJ8P1j8+OK9v8T0hi/JN78qZ2Xf31qYPfCKvGIvv/9f64xFPZAuAAA= -->
