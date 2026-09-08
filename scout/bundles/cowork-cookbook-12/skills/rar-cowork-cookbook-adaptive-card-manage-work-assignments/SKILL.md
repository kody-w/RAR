---
name: "rar-cowork-cookbook-adaptive-card-manage-work-assignments"
description: "Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_work_assignments", "rar_sha256": "71034042d3fd39d28eafdc3d815a4a5b2beacda19c9d5793ea0bb3a5bd36ff05", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_work_assignments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_work_assignments_agent.py` and in the RCI capsule.

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

Manage work assignments Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments
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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 71034042d3fd39d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_work_assignments_agent.py` first:

```bash
python3 adaptive_card_manage_work_assignments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_work_assignments_agent.py   # or on stdin
python3 adaptive_card_manage_work_assignments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage work assignments Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_work_assignments',
    "version": '3.0.2',
    "display_name": 'Manage work assignments Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-work-assignments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22c3f6312d6d94fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/manage-work-assignments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-manage-work-assignments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage work assignments status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-work-assignments-2026-05-24-card.json' that visualizes the current state of manage work assignments. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage work assignments KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of work assignment status in USMF with 4 KPI tiles and 2 buttons.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of manage work assignments status for Teams, Outlook, or a dashboard, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageWorkAssignments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageWorkAssignments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageWorkAssignments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abPbRpblX+G8jhjbTelhI0hCHRUxIBaCC0BsBEhYDhn7vu/w+L9PgnzaXKruqo7+MpRsEkDm3fLec24q8ceL2TZBXr18eFFcM1vszSQJA7damJmzoPI+r2LwlccW+G9h51lThVbb5FX98u7FcWu7CosmzDMwfe9mbmU2br0wF5VrOu/zLBkXpGOCAZ27oMzKWRyVi7DwwsRd1G2amlU4hZm/eCgx6zr0s9TNmkXdmE1bL7wqTxf0mJlpaNcLbI0v2P+tUPzCy4F1Cx8IzRaJ65vJAkwKm/Hdog+bYHESD4sGqKjfgVEyuV9Uef/u4Y5pz6YugP1NntWvwAN3MNMCDH358Otv715C8Pvlwx8vdgKMAR59tn02nTcz03d1YCn5xdA5BomZ+WBoMYIgZuC6cCtgXwpuOa63eLv6uXYT793i3/897s3Kr3/58DFbvH0+vsx/5DZbNIG7aHKzblxnYZuFaYUJcOp1QSa9OdYgpE1bZXNwa7AGmf/6nPlVUl4s/jY/+/mp5NV3m58/vuTFvCjA7Y8vvyxA4D6+VO38+3WWUvz8y2uS92718y9f5dStFbl2MwsDVr9+ert+EwsGfh0aeotPishQb7oq1w4LFwj/xr/58zT9TdxbSD49B/+cF+8WP5Y8+/M3YO8zyywg98diQQzAzJfXKA+zn990VDlIDjOz3Z9/+Udi7cC14ySsm39K7q9PwQHIaxCtt5D88u6xfL8tlm++fZH5j9UWIGH+FU/A8M/qvgTqH8l+rOxfRCdhBiry81r+UNyPJiz/tvj1H/r2n014t/A+vtBuAsqmMq3E/bD445Eiv/7kfL35029/AtH/pRglbyv7IeFTamah59bNp0+//lQ/bv/0268/tQXIYtdMP7VV8iOZP4rrQ893EXwb9fP3c4H+axZneZ8tvtTQ4o+8+F/Vn68LzUxC5+v9+sPi20qcP8vF7MRnpc8QfFONNbD1mzj+8vIngJ8MeNM+MGpGn3/7twUf2lVe516zUOy8bRZggZswdWfj1SCsF+DvjBqVC+JahyCwb+NA/s8rPFuce4vf/4/9wPH39huOQ+YbsH2yAbLNsQXQ9mke8ukrCte/vy5UIDyvQj/MAMjKpCh+nEcChAaKi8qt3aoDYGWNjfse1PT7+ccizBa//1PyPz1EvRbj7w9wDp8IKFOHGf3qNnFfZz/1AKD80ysb0JM7uHYLtCS5DUzynjAPLMkTQDHNHJM6DpNk4YQAXwBNjQ/ZIG4fZmG///67ZdbBx+wJ19jiyV81BAZ8MWfx/j3wzUtCP2g+Zq4d5Iuf/vjzp8X/Xfxnsx7CZx0icPFtVYCFD8IDVdY+XF7MSwwg5LEqf/z5FmEgBjDnAqxh6IXuczLI0th1Podb4cj3KL5eWC4IMwhxWuRVMzNn2LwuDt7ii71A6fxoZokgr5uF4xZu5riZPQKpJnDnSySzHPAsSMXaA7zZ1u5D6+9WZT5MTEG5m83vC54SASflCfjfbOZjEJicZyEI/5dkeN4HQqqf6sXus4jXhTDn5aIwK7MIKvNNh2c+12Um8bfpQLi5yNz+YzYzsDuH6lEkz/D4c18R2m9L+v7RPdg56B4yp/6s23/rPZyF+mDQ6mNWvxWAWc1LYQNCAEr9NnRmWviPt5Sqg7xNnEf8gKWzpLdVcN5W5ZGDT+7/a5tSL5Rnn/J9i/OxRWFktfj/rhuaHSX3e5nZkypDLxhBle/PBZi7vtmQZ6MIRD90Porta5/yGYs+Q/LHLAlBNlXjfzxHPtx8G/OEubYCUZZJ+SEf5AxYgFnuI6XnFK2quRjMj9ln7J89eAAdsBrUP6iPOS0/K5yffrY0AEU+X3/tAx4pAEIOHAdpuyhaKwEp5bmuY5l2DKya1+jz2oH8ducS7YPQDr7zao4tSCMgfwGMCEEOAH54/YLHz6efTf9u4rPdmac8WsEWVGX1EADscGcD5yWZVwyY1zybbODnh4cQ4EZaNLPvFqgL4Onzplu5ZRvWYTMv7jOubgFA+P38/fR0vusOBSgFECyQ8EULovsokTnTUtDMABsASoCKScMMkDsIylsQHgLNdK53gKdv3edT4uP2m0Puo65mVvo8cXZknjMT/TNrzWz8FhbUH6UJkJfOIx56/5ppX7TNsmdorAG8AY2fnz47gtcnqT+7hsVnuR/+bhfz87+20XnQ9PX7BPiwCJqmqD9A0JNaPzPrKwAm6Glr/YVl388s+P7Jgu8fRPwNiHwn/On3h8W/ZuB3It4K5MMCeYVf4fnR+S3B3j4gHtT73f39an76MZPdr9gJ1OcpyLB59UZA61+I7vMQwHZ+BTAGDH4SXz3zZQ8o+oH0YCk+Zt9m/FxxgEgyf87QOv8GCR6MD7L/uXJfCAk8yhqg25k7Rd+dt2iP+qjdlw9ZmyTvXgD+uf/k1mwmnnRO7Xre1IEiAs1XE7qPqyf4fXqC3yfABVkz3/5+R8vlPagRkLzfQ+WMOmFmJy2onp/R99gvs5nNWMx2Pfdmczf3wKLhB1Ivjx9m8rqgXYB7Sf1tgr8R0kzI39ThM5QghDbw4d3CefAKyH0Qytm9uYbNGhQFqIcf2hIX4X/p4xei+M497D3+Y/ceVPPpSTV/L/U7nvqWlWbhZQsg493CffVfF1eFZ38o/0un/PfCddCazHKc/MPM0u/e8BF8g93Nu8WXjQoI1NvW8bHVz1qwK/913iTNufGYMv8Ac8DXl0lf/lnDcl9++5FdDxD9NCfxMxX/ap0wgyMgj3nd/hHdA+OBAU5ru29h+Keg4j0Ko+v3MP4eXT3GvUY16JH+PnjAygczAH6dHf4aya/+5I8d4OwP8L95/oPFHy+gWIAhjflWLm9bCDAcAOn7em6YIIAqQCG4ftY/ePbf21y8CakDE/S1QMoGgbEVvEIdzHMwwkG3ruk5NuZsEdxcmbiFWq5pOyZC2ISDbwjMNWHLwsADB1t7HowDeU8o+TS3huFs2KwSxOM9QCP362Nwy3nz6OnBHK4ve5kHNDwd++PFWq/mAlnVB/L5oSACsdbY2ZILazmtvXzQpGaU4uMlOyllebtdN1wyYgHqUdk51eRTvzpZ0lGsKVKSbtQwaafSDHA/yyjP2OBD65OwlOzljMcvtTKuZUn0CnjprTOHbyaI35/Ra4jAhV10KRszeoBsE/2oX4MpLgwt11Ysn9bIbnm9HDX8KG5wAlse8LGQW2XQDqZ6SO5jasrn7tKKS0e01okWFfohDdEUT6pumcaYhtHa/n7UDLwNNNHJM3tdkRKxgXA9mjbTRlQT9KThSRDS5ukYCpo5+CfVOadWyDSOVatQx8WBEg6yStPlxhSzQ7zttur+GJDDOVOMUDe0JA3U5V2k86V3wVR8C7mdB4e3aL1uMIvDpsEqBSal7kmt7Cu7ENMD31dJ0Dghu0vtMonc3OiOknHTNTZsiGZXHV184mxxYmg3H1CK1LS7VqWnnsetY7hFDF6LHTc9s+P1gG/iFJZQlG+YSjNUBpJcjd3KQ3a431IWTafbGW5aYzqsasGzoZGlTrICeA6aKLY9cwVp4LcRCbl7qV2boxrsbn5IWPQljmT5kKDHcQVfhDVGxMw0cQ6j35kdvXWThCz2RE6ghjPdxEpP7rruno5lsBJkVmPK1C5WPCubo3yIA5FEUr2939uaZ3C4pyF0PcaqQiSlxbJbhE7WpXNiNzlQWeBlOq4xBisEdClzZSmmUnGmqLQZy5G6CsukDqNjW93HQ4YzBVNqFqaHWzWKMZUf2vttb8gjbS/9/CRZwnVTa7u7gdaUv82vGSOu0JuChndVk9ILxKwCuNrBgnm/CnYp7ZsziUXHKoGR08AVOmXfAieM9ROy1NeyxoXV4Zb7ExQGZZkJQ1qdp+xkFYN8hgY34MertN1hxJrcMurgriQ+qHXvmN/uBL2tSmxonfBqaBZvbC7ScWWgWbBMUZB4zTE4rglNRRkSxm6nPBXOeSnz5U0o0gkTB9MdcfbUdxOv36AIg7hms0Xl8gpJjpExKw+aaIIKt5xF3Ey5vBySeI3xVKCg8ap21oeDjaPaYPYuU0fIJbbtXt9tj/yGsEj31u/rWgnze3sxhCjQWuN8SN1xUAaCKC6oWsrpvo9D+cjYWH8K08EhlR2u1zkcCytOkncbN9kddutT2bNNH3YUrUxs2tddgsSocTNS9MxgvLuV6d3NpastMhaZjqYxzBS7PVleZP9wZ6LY3Cd5qR3l/ZpGUxfht9FNVwaMvCGnYqmQQ26OdXSDO0gw7tqa2xqhKbWeUYkIxJ5aatsvuWUelylJtOvd4b7C0X4V389lTZ1MMid9hWDOUJHeE4g4pYnKlT6D9meEc3apZMphnSoTdzmZSqXEHE14EjKgyDU8re/k3S+umQ/fkiqWVoTty0Qz4ZHKQ4h8VLLjrpT1M3leQ5V82JaS06s8rjFmFJNLZIR1H7r2Ea7cI0bil4S1TS8G3BhrgVwlqMtB8XpreiftTGwsY2cw+wzXutzGe54bz4ITWwTMk4Oz7cnVydmITFPS7NJmj10XL6mUYteysmS1NdkIypBbae3sBtnLm7FTCmK9OtedTrvtSRqC0KBWYrrp2JMKqfUkNpTMaOr5fHe5FVp56yaQpq1fRmjm0y53z8Cz4xiFZoxNm0CJ3DGzu47M8DvnCkYvDSTncLYs5epOKVNhPWFtmGvuWh29A2HK8bU99VyO3KvD/VDtCaEuMZlZTjHBSlsoZn1GZUohOmC+MWJGeuJ8BIBpt8wYubuPg9d5B7E472SFiegTtXfuOkNOa/1w70OYhZcpmfjWmqOGilnB1I5UytyU91WojmN8OIW0gq6nNakpjlzxIGX566kllnFyNE6t3tmjaEscWsnShaXlJVtV7KrRHYa9N5AZVBvDtGvJqOvVzV4dkHpaQpczvDbbCRT5aBd6glIuW9bLUInk01JlBbiFd4GM09FeKgxIW0Fbm7JdyKzvAqpRe/oSxcfNerlsPShRPFkgWMIDrQtsKA6uWnSaysS5CUlGsEO920G2eBSGXAnRdaOdAkTnU9qHaF4aEEG9Gz3V4u1Bq2nLtU6tAqcsmdFdzGdhU6TAluMqNJltYR67q8TG4cjyuZ2GY1jDB3g6OUiQBCtpTCBOgPHTgGpatDmW8Em4wpNxE8nN0bfOSEgYe2GXqcs9pvoTdtgWzpDhKS7q+9YTjXM8XMEebnNfDTtXOoXn/QrmWH6/gc2g2dltgIxCcKQBzR2XKBHQ1uUsN1GmwRcVSrIeZkKy2/HsLkrvnDPW6bI9toc9c/QNKEyXUS1RWq7u9Zi7SvvTROfYBT+lrQUF8I1d7fKjQ1+a1q9QJj+GZMyc8E3RUWF2kCZAVifvVEiDdpb5q3jT9JtgHPR+11D3a9nniADFqojbli4d98lNW+l6N1IBWZ7z/U7kVoJHNW7IBrpihQNxIfcn7WgWKU9im8sYZlJpRJqd5unEHJiLb7vXdHPfds0Y81e7v1BbvT5Kq37HXDDcOyujdvYL9kw1+9rZNJmfrYIltUwbPTzczuFAWajMbi9Dgpf7omyVWheFEt3LW4FD7jRJwmomCp7ulFJs05QIC3E3XaMxlVdQPl53BMDTcbBruEzPyClEveIeUSrEg6okVD6v7iruY5JSKKeBYUqmkanDwCPX/n5XTqiyP8bXi0joYsFJWG/6ZrnzAnRZUU4oibCcTuf9dXQlT3GiQ2ciTFlG1ggpJu0S2XlPkhO/FYgOHRQhuMJ3xs40wtvXU84kVb4V4DIQJKreuCINE8R26C2IAVW6MgRIo9weiTGKww5odD3mSF1IoyqL1YUlA0XpxTXBst0pNYoRy+WrXFKCmbcmUzmETqlE7/E7QwslPKZPjTWMa2NqqSiSB+GKTX7hOfgtqkMpr3ZHnJ1gAyL7nk0Pe1PjJlE15dN4EynGVInlkgF92/3Sxc1uuN+G9urvD3q2Uycju6C2c4apnixPR+mwR9gCKv27hHV9ekZbSrnebGHJQB5ExJNSX86qGdD9lO5VNGvWS7VRVO4sb+mC6EfjmsYMNJI3EL9z4Jm1n8CbpcuvKlyVj9FRYsDevS5B3sZXXeFj3mCZwK0V9Dr62ylBSklliCt9HWyKnvlG6zZ3LAfFpWzUBjlMauoEHMMatL9OnZXHw7wuO9QWQXplJPyb2vcrR60hcu8DMGHj5nQfDDu3yfNWavHyEO6bfNxxlH/ldUTYK8NV29Wtnpyjs9OjskpU1qqdIALtaC6wjoIzKZ1hBy17xdTLXeAD8XzruqjdXK7TATvr8pUsc3THyCwuW4cDB4frC+vl/m6jMZrp173aJJCbHTtD6IrOXWYFvh1c/r4V02uwr4FsbcB1nM9ZfVOvTGvsWjqiupSYUv1shecddtUQw6JIYtAiYRUE/r7rl0i44tEjT5J0GfroOKjnfPClw9m8gO29emxk0MbXkSiLVhdSKGX3qndQsSuyjMbEHo/kJlQ2cTXu7i2xxo6FkLe5vtYdDW53jJVDsMGVCF/Wt10kpTfMXueeVhdZUDcW2crhZlnm22oVDSpVIGl1Ec9ZmqSYNfFpe9xoRR+al31H99seQU3urO0QREqWWiek6V4zNjdLwdFsvOzxQ30bciy7l3zsOK4Ac3JxwelrCfoTS73LW47PyI5auUGKet2elU6n9B7Z2Eal24jcLxl/Ddj9SvC+AlsFxHNHvReMzpfvKkmbB9CHcuvM2A3oil/3uRx4An2qMlI6k9X9nCImfg/vJ53Vlfa4bnRBPOoReVT6G4wOWjVdNITJruwlO1xzihKImJScHUxLXnoOdvg0rhu7pHK/yFXrAuCYpBDvAJLv1k2DQ+w3PZYnylG22ZYxjhskqbw9DFmtUTZbGMFWjM0xO87JWVzQCuqk3uKmDAs9r9UVuT2eONroRp/urtbZQmz4HJLmLkrOx6n1MH21taw6lyNSavf3seSSGL46VsAmktAmRY+SezyIT35Qouc1Ye1w9absi3zXuvWZxlADbMQO3Y0qdNK+joarQtdkZYcDo/ui1VNlGx32/GrJF4MKmRNSHNa+FV+LeGpCkVYZTHeyORm23Y1uQWp7BZpe2jBUN8tNXjRmUWzunBQ1Vke2RhFzk7I9Ng4bsMehgh2pwUuTWO1WhLi+qsGI+yN8JJT9YVwpZx3FyW2ThDpksIdIKFcEKu3lovMFDculeiP5gh2JCI1e7n7YsyKnqUZ3T9OIQk9GKiHYWsjXUG2X0MoLmiVoLtaH3c5i7DRBzOtui29UfZfeSl7CQMtI+V3OFNu0Y2Nnw1NOhTF8GXXmcb+cTLJyYWLqeQFG07tA62tRg/UlceHUyuNwXGSw0KTgSe73vUXreGzR+QZwBm5md2t9Op8CMU2hTdEnbe06+BK9hcsNj/hJaKzPUxW1ojnZa5wizGDyBHes8rUuIYaHrOMtLwd0ot2KcipRXlvx2/Phpt16SwpQIUNlF+w8tOXavEzBUMKROHUo0dBNcqyg3ZA2Br5PSYfC+s5l2pipldaB7ehsZNulT8ZHRJtAM10eW8qImGg41zZRHz2ld1l+hEJ/snFPWQ8TVuc6xOw2rVCem+WaH7dY7SpULXD3zVbL4elu8q6xtUnUFyE82kDRbtIu2ZFL0nIJhfI2OzSNfW/aNYvb421wLsbJ5O1yv7oGBe6E42mfL3ccBvfYbVoG53xN0GVzZ0VGNCXLCAUa472euYaX0a0JazmqYiXKLa0J1Xbil3fQJclwvsUsyXWCk2BacCO2I+gLedtdxUMNFiXmXG90ixawJhavlZs2qr4uDeuihlwBQTRkRYSO2KyC3O2JS3u7GzVDw6lpTafYtb2wE9gMkhuSKGBoM7EdVbf7zupzPYAdysf1ZJslXpEQ+gVd2S1vJSl/ADurQ5b1233TYUfd2bvLQ3g96jpaE31eFtLVHO81UTt7FOlo/1oGya3cgrZxiixeEa3ltK+8A5uI9Lm/TsJmE2IMuzxucSkZAhkd4kApxuPuTh9w3oNFLkv22mmg870twsT52lV+OOhVZWb8dXIkGQ/yODL7nLd2nDkcvUtQMWrXsMmRY+vLyt3VvVNV5x4LdtemvDtQ5W6cy5QNnkNsc5FaIkKvw7dR7C+DwAtnxM19hLaIiG4NzGUDWL3fcGdASzUtnMs+4zKsFaWoGlddm+KpysAOiuuHsIL5HHfYiY9ESacIO09XDbkjSFDIrAvSOt8s7ZquEQQ+WkdN71xA6TbLsXtuyunN8Xrtdg0WCJq2EuDB1L1wjDoHG+m0Xxd4vuGIXL7ct1Olyl09JagJ6G5SjSzu0g6Rba09cQfT9hHmIi/tRkIJlygCnLtTuXniNv1NyIYNSW5jDxoQKctX1sGlx9WggfHeNQwdmdN702BN3KcnuoGu19ISB1/v6uV6Mxp4gndtxrqe5mggeLRIL220vdn50OzSIu7oci3Y66Wzj9PUOHlV3t6lbc/RnWW56bJRVp2xGUTzBPa56UGAMYQY441DR4cCS+FIiw6G119WeVGT960qNZvcSXFHGCrtbsv5iq2mIu2LUDxlreiHN5FuMT5bjuGlLJeOx5VKNbCHzJRLWTDVgqtoN/IiJBd87WKqKXbrwjBYelZEUk10FWovThH+asqQxvVWAAn9pFHRnoOZE3e7Lc88LR0Yd93xJHdSTxfN2cR5GzeXy/GwrPj6ktmaGNYYpijjCKOnBmr81Ghz67Dt1njEd0RZoafuuMO6/BjvJhhjWitOGYQeyc1pQ9KYdnDRc31X8zFfDgnD5FDXYRYA0wa2TG2paZe1zZ5QonDSDA037tU3nK0JTAJbmf5arXEHhfNp6M660tSo1thrD0bra5LvTQKj+dhDcWtvNJKJHyPeJUaYpy8bJFWtCKEvS+5apW7emXAs27jrbXLEv8o5zkcAIndQi/o6sdyJKhrWugJF/U4Q6DHdKaDbz7enNt9f1/a+NeHzWa8P05JypBVoEy7DnqvakTCxC3UrsaxdH/kYys9rJb+qENegBj6ekc2e3FrQqCVa5WpRHvEMdyEJhkt9Znvfq37GWF7nLTVCXdlX4uhkDo31VKJedNQ2dkSDJsvSTh10i/HFRmOH++kgcuwWGTHjgu1xGzZQA7te+nPb9M5ASKKhggYtX8sHvcu3axZp1ASyjQYOifKMihNpnLH2ajfVbWrxdLnDjoe4UckLOxqjUGUCjt9XKII6on3qQCT9C3UX7S1IoxhU+H089tG66FiftNtIAxZHemPUGJ7KeSKyBmNsOcfzzalHspvlzUnJSQfPuqfBmj1udW1PGCvX0RDaVm9YIhKZuyMSPXMxrmM7FNmENxuvG6j2bG3fyR19DohmzYJdnTBsx9UOhsFsvd3g1ClYlQHoqtpKEFuRO1ebcDUgDbe9iGgTcZZrNtLZo6G7vsT1DbByMtQb3bHnrRFUOpsTxkG0NtgAkTzXSLpnuceTVRm3kZ28VXGWkWyLMVSGiPqR8klHqT18UncaQ16zIg/HA6QqU060nCDjW3PDhkO8oqM2uPWov7nvSklgd5gjjrFDFkfQuW9jp4evHCHmVr2ED80S8ggF0n34JG5tmFjBa6w9eunWlEdyrUeCtulu/h0r7HEjnyM2khXzUJoOeYVxge1tJNKwcbOEos6HD5znnxkcsv2BgBUDYXxZN73plpSiVY1LHlKLi8DUhLBbbbiuB9uGkVDUhiJJ8m8v716+Hoy9/Gtvgc1HNP9jp0HPQ53PL388jv1c0/nw0PXhX7Trt3cvlR0Cq55nX3XS+m8HSH85+Xr/T53izSLG5ytWn0+InyfbDdgEzpaGmdPWTTV+qvPk8RIImGG19fzaYj2/2WqD729PML9z52V+jRC4Pb9i9anJP729dPm4Pb/k4Tqh2bhvl/7bueC7F+ftvPYTtsY/uVUxO/32JgHwFXuFX9GXP/8fDJerBCsuAAA= -->
