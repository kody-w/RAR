---
name: "rar-cowork-cookbook-ppt-exec-define-product-policies"
description: "Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_policies", "rar_sha256": "5ba8943fa2beee0e32c5d3b10b3b982de98bbf33fab41ad9e497cdb1216d5add", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_product_policies_agent.py` and in the RCI capsule.

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

Define product policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-policies
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
    "comparison_period": {
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 5ba8943fa2beee0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_policies_agent.py` first:

```bash
python3 ppt_exec_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_policies_agent.py   # or on stdin
python3 ppt_exec_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_policies',
    "version": '3.0.3',
    "display_name": 'Define product policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab6d8a95ebca75f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define product policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define product policies for a 15-minute monthly review. Produce 'ppt-exec-define-product-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define product policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on define product policies for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define product policies status for a short monthly review, without modifying any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineProductPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPiVpbmX2HejhjbrcxXuxDZUREjhCQEaEFICHBWpLXvC9olt//7XAGZtquyuqoi5tNgZwLSveee9XnOSfHrm9U2YVG9fXo7eVa+EKw0jUKvWli5u2CLvqgS8FYkNvizcIq8qSK7bYqqfvvw5nq1U0VlExU52L5uo9StF9ai8iz3Y5Gn48IbPKdtos5bqEXvVWoR5c3C9ZxkUeTg3Y9yb1FWhds6zaIs0siJvHrhV0W22Iy5lUVOvcApcsH/7xMrLVyrsRZ+ATRbBEBkvki9wEoXXt5Ezfhh0UdNuAAfU+/DYq+KHxZN5eXuB6CN+9FPreDDwnJmTeuHZVZZgrvRsKjTCJixKNO2XtSlZyXA9LxovPodGOgNVlamXv326ee/fniLwOe3T7++OalVg0tvatlwwMDNww71aYb6sgJsTq08AKvKEbg3B99LrwLaZ+ASsHzx+vZj7aX+h8V//mfSW1VQ//Tpc754vT6/zf9pbb5oQm/RFFbdeO7CsUrLjlJg8vuCSXtrrIGFTVvNdi1qEJ08eH/u/F1SUS7+Mt/78XnIe+A1P35+K4AK1uyRz28/LYBbP79V7fz5fZZS/vjTezrH7MeffpdTt3bsgVABYUDr9y+v7y+xYOHvSyN/8eWkcuzrrMpzotIDwv9g3/x6qv4S93LJl+fiH4vyw+L7kmd7/gL0feafDeR+XyzwAdj59h6DvPvxdUZVgNSxcsf78ad/JNYJQYamUd38S3J/fgoOQdIDb71c8tOHR/j+uoBetn2T+Y+PLUHC/DuWgOVfj/vmqH8k+xHZvxGdgqytv8Xyu+K+twH6y+Lnf2jb/7Thw8L//LbxUlC7lWWn3qfFr48U+fkH9/eLP/z1NyD6n4o5FW3lPCR8yaw88r26+fLl5x/qx+Uf/vrzD20Jstizsi9tlX5P5vf8+jjnTx58rfrxz3vB+Uae5EWfL77V0OLXovxf1W/vi7MFAOX36/WnxR8rcX5Bi9mIr4c+XfCHaqyBrn/w409vvwHkyYE17RO+AH78x38spMipirrwm8XJKdpmAQLcRJk3K6+HUb0A/8+oUXnAr3UEHPtaB/J/jvCsceEvfvk/zgPhPzovhIfLsvkyo/aXJzp/eaHzl6/o/Mv7QgdyiyoKohygr8ao6ufcCgAKz2eWlVd7VQdwyh4b7yMo54/zh0WUL375Z6K/PKS8l+MvD4SOnrinseKMeXWbeu+zdWYIkP9piwPo6skw3iItHKCNHwGwniG/LlJAOs3siTqJ0nThRgBVAG2ND9nAW59mYb/88ott1eHn/AnS+OLJZzUMFnxTZ/HxIzDLT6MgbD7nnhMWix9+/e2HxX8v/qddD+HzGSogi1csgIa7kyIvQG21GVgGwgQCC4DjEYtff3s5F4jJAQuByEX+TIjzZpCbied+9fRpy3zESGphe8DDwLtZWVQNQP5F1LwvRH/xTV9w6Hxr5oawqGfunWnPy50RSLWAOd88CThvUYMErH3ApW3tPU79xa6sh4oZKHKr+WUhsSpgoiIFf81qPhaBzUUeAfd/y4PndSCk+qFerL+KeF/IczYuSquyyrCyXmf41jMuM7G/tgPh1iL3+s/5TLne7KpHaTzdAxYBzzivkH6cYw4akwzggFt/Pfuxxpr5Un/wZvU5r19pb1VzKBxAA+DQoI3cmQz+65VSdVi0qfvwH9B0lvSKgvuKyiMHN/+gc+G+1+5s5nbnc4shKLH4/61Fmp3BCILGCYzObRacrGvXZ5DmTnEO5rO5BKc/1HoU5O8dzFeU+grWn/M0AhlXjf/1XPkI7WvNEwBboCrAHO0hH+QV0GSW+0j7OY2ranaP9Tn/ygrApMUDAoE3AUaAGppT9+uB892vmoYACObvv3cIjzSp3NkZILUXZWsD9y98z3NtC8SnCecofg0tqAFvLuM+jJzwT1bN7gepBuTPIY1AMQLmeP+G1M+7X1X/08ZnIzRveTSJLajc6iEA6OHNCs5hmoMK1GuejTmw89NDCDAjK5vZdhvUDrD0edGrvHsb1VEz4+TTr14JMPrj/P60dL7qDSUoF+AsUBRlC7z7KKMZYTLQ5gAdQGqCqsqiHNA+cMrLCQ+BVjZjAsDcV1/6lPi4/DLIe9TezFdfN86GzHvmFuCZ3VY+/hE69O+lCZCXzSse5/5tpn07bZY9w2cNIBCc+PXus1d4f9L9s59YfJX76e8mnx//veHoQeDGnxPg0yJsmrL+BMNP0v3Kue8AvOCnrvXMvx9nSPj4LP2Pr9L/+LX0/yT3afKnxb+n259EvGrj0wJ9R96R+dbhlVuvF3AF+3F9/UjMdz/nmvc7tILjiwwk1xy4ERD+Nx78ugSQYVABBAKLn7xYz3TaAwZ/EAGIwuf8j8k+FxvgmTyYk7Mu/gACj4YAJP4zaN/4CtzKG3C2O7ePgTePbI/SqL23T3mbph/eAER6/3xUmykpmxO6nuc74HPQjDXzrXnaA3VkVVFd5POAEhXufPHPk68KLleL590ZXp5bgNbBI3+/pdwDbmcLq2ZWtRnLWbfn0Da3eQ8oGpq/P0B5fLDSd8AmAPbS+o/5/eKsmbP/UIZPdwI3OsCYDzMzAHQBegB3znbOJWzVoCaAbt/V5cEcX57M8fcK/Yl7/kgyj8bg0XPMYPej9x68L4yTxP/03UO+Nb1/f4IJ+o1ZmFt8mqn3wwvQwDsYVD4svs0cwLTXFPgY2PMWDNg/z/POHNbHlvkD2APevm369m8Xtvf21+/p9UC9L3PqPRPob7WTZzQDaD97+h3U7PBMU6Dvs2CBxx+m/7Ny/oghGPURIT9ixEPMd70EmvjI678AXYIm/HtdDo/r8Dw6A5e9lHrueXx8NBNZO+dh1Lz0shYo+RGg99w6ZyDrwnR8bfmOBg8VAGsA7p19+3vQfndd8ZgbZ2WBq5vnP3P8+gZKyppbkldRvQYPsByA7Md6brhgADvgQPD9CRDg3r89krz216EFWmIggLQtekXgvoXZnuchHo45pIvbKGLj9orGXG9F27aPgwU2gVruyiNWS8e1UQylXNJyXSDvCTNf5q4ymnUiV0sfWa0wn0AxxAV6YITr0hRNOeQSQ6yVbZE2ubLs37cmUe6+DH0aNnvx23Q0O+Rl769vNkWAlVuiFpnni4VXqE2RB3soL9BE+YVm3c0bt2frrC9ZG7fq+Dg59zQaz8op3w9VX+yt406uN33MtELM5bf7XeVOnsRBIz7l7uYoBspGPtnCKkrRPgm8pV7ScKqQfkvrQ+fsS1NJuWhcKQWbtFppc0pzqjjs6JzP9zNU0Rrp3S8jjR7zUg/PhHUhhhUMHUryrBTEXjTM9rbR5AQP8rMMcRFrJay+XJ7RPKXOlrMM9yRqcqGaw/RpM8HT5OQHxEhOY2paV+KMRuwt4qPmdhoMoy1HeeAvbdOLvoifNXUqYenMpYd0XwQZEVlWZe6J/FhYqR7KfcZp7C3MPSqAomhrcpqtEPvkpO0vWemUQlKeKrr3NiWKQrDadRTltpOBbzGqxasljg/uXeYy9pryoTnuY7eMK/N2v+xjdtjudZZEdQnu77Qe7KOOCVe9cq1w6WYvl0gwONQ5IkUtYuCzHxjLAYLKanfqg+y23FMryTxwhT7lwjFeo+2N2hn3UzZsO94lAw3bKQzSSXYjUdAFjHDyJBK1DF+tQNTNW8gUI+tKtJhwEn0YrGO3i8rzCUn5tdyeOL5O7jrPlPsztLsXtCxbE52s8mHbcNm5rfXt+bjXOuviZhdPIVdXpNr3k6bJRre7i/siNaZGXQfRwTxtsmQsuHpE+26PHm65kDEwhprI3brUjX4t8qxwunNcHms5NbBa5Q3s4lHZSkrtUvTvR8pmuWS3v0/7SpRP+P007HNr4s+JzW3ocTirqbkb7upxRaw4UrYtfhIkPdrG5S4yNhBqonxgMf6mHxQLxFn3DhkXNplxs0V9wvcFzwxNfEzR6rhHmvjEpNBknW3klFxJ1EkzUb9WZ1yuo8rfHY/+je0UoetTwY1IFdnXSEffeO/QCbBwQDUp5P1gglaBx+6uuSNmR+Sg1thBMkMIXdnERZj2UtRlNZqLHCItpx7Wl07fm/U4VrvxtEQgOUagBvxx48nfZS2uDI47oHctwE2mVTvJhxi4J8OmOsFXOFL4BGqnJaW5hHKJGjSolJ2TmPX2RIUnTOvyW9RqMp8pbX0Qbu2J3VyooS8CekuwAWf4lbWRIQblo0u5Ie+mrhNnOzuNu1SqkcKqENwWxwJrryyzk7ir4e1Mw9wUbN6eK0pmNlBAsf0mJTkxyIm8ZDKY3TuMFNOezY497xnYLQ9DdMnBkuft897tojPidMb+ahncjRmZuyL1bBE7UnE1g50Zc3rs9PHowA6NJIY5onjAd3FB8YxuJBbklrxvLocem46Crne0spMxGmnJQ7xZXu+Rfhd3w/IqRrGWbMNBGi78lS95xiil6zGHdUlkZbhe3rMlttYrUgl0RmZSmjirV4lmLuIdidflCq/l09LnxLHjGV6UzjtC5kkr5xT1YtlUfNEvGQrwxeSyvZcIJe/RzvXANlw8DMwQJQ5qcPs8VTO0M+SEH0PbZRNYdyDiXntLywiPlDziKUYJMOdpOOOrW0WrnADpWIwOcWcjUJfblBFK35OO1HeYiYfhzr7y1ZG4bk6RYy+363vf584h7pP2mMYFJu/cpM7GQ3umzl1+llZZ0tvDdMY4VhbwGJLvsHFTYSVmVsiN0c9OY4eEHuduiOuUlt5InZM7xvQzUnF8UYyq5oosx+VxWaL0iqzw+JityHV7HZSNt5WOtyPGJwTMrsgJ1xC2c0uAkD4vNndzWWil1G16YQTJI7lGYlSKmmibaXnJGE06FZgUe8EhUna5eBrKndDHHGIl3K0+Ryu/U8+g6XEmMTI1XcvIDdMCSh2p+3FMD/1tqVTpIT9y7kFoN3EiZpFyEpiwJxMpqDI0ZcoD766Q7uqEB36898yFt6/wyUo5/rK/eAjdBa7h7PfrqnDkiwUNXnVOtprDtNWFb910N/a3bJxCd4qiZXbBJ6LVa/RWT0xZOrdTjrGGTsr7kivIo49EurtNN0UNwr3WJRzvoJCRK1dWxiA+nRNjeyAV9b6BFSlujlMKoLvJefx2OlPytJmmI52Yazba2FKe9w46CZq353gTIOG9vkabEF6voSs1jzogNSWc31O64x0AZRZ9ybR7+ngkwxuFliaDnw1kg6b7jTUwgMANwTuW/IaNuGydTAdXKON+Lw4xs5OXVHgL1WOmV6qlLfkLG7BLTN/6F3utjDbDAqcJGyO4LVPo0iLTcJ/KDHUob7wcNibUjs7kIgFXrC3NvCgFWeorf8MBjmgQSZFNUQxOA3mHWzqILNc/hmdb0KP1thlUXRvyKVuvGKkWjkZmTRsHp6htRmREeD1mhxySltR+YHZmKF3Ho4ghTAMgMUj83EkNCoIRGR1UcULKRGlAk4hcq915d7jtl1HrUAcnrFhKnC4wGoXOnaNuhniLWROvmLV24q96fz+zk4FxwwGq4tOoHUtDOTWWpTIsxyah4am95VkoIZq7287bCkihJEZ/anTJFT0ZMs6WpksXmUS4kWaP/J1Zp/rVve8h4a4PxWA6/LG+ssmQ8Vuos6BjitzNlONa9kreoIutpqrFEwfoqjTcsb2s4yN+bQ40NV2ywsru5F4PCbcibvxYrNt1Ia0jiSRBW1zqLH4c+T2HZ7fyUpT5SglKVUsKYe1GPchz6z54pXeZeDFcpq1TuGV0MhwN6qte2O0ikmX2RhEFjHa/HctoCMTqKpqCdiRg9AoVkABtjix63K1AqiLctGV8x8xiVSCuB767JBPXJTf27Ovnm1Y1ZepMfL4OwtbNsCVJ7LOBiLiNkjoajnYrlF3XbphQbsAferKbalISp36J8ynKjtfVaLJ3BOV4bIuL+8C41UhdG4O+3odKKgUnHpEoWd6COehanvBKM7SSla2CM9b6Za9sdJfwpbVrBAGaxpl+vN4cGb+stQlUXLQj8L7z6GqgNNES2kpvi6mGg6sRAmMtrYfY3aVsxdVtpxf5FoPS/jpIG3M0k1jooGY8hsdB3OvXFGjd3fZUeF1zQcRyaWjqeyObNPp8xQJ1W6kX2bus126PX/0V7JJ3Ab1dJfxo+5mTwLcWLpa2t1NqdD2CJj7k2lbeX4bdepVY6QChXC23Gmi59SQmJMjYo2fxZES8Ehi6JVv7mOHLJt+xhX1HkPMhc7ImZjN7d2GUM1NuzvvjmbpzQwzSCG+8jSTuQ3w6Yb53d51LuluKLHSTyJrixLRrT5ZZA6e31njYePV9lIo7v8ZEGz/rY3pERvXGgj6dDU8UF2BGsLuE2dFFavPcm83m2A1Xs9uYAnKpayJDjYE2oFK4MtK4aU5wU1zwJUpCl6G+SSm7SYJLuNlxlGauNyngIFXUyhgCfF4mutgLLjIlVRBAvh8HhKeWAeLrIUqDG6tko0BoG9x7rCmSdQP3zZCE8jTZh6wR6LPf8kJfcVXRLp3y5Ks3MMudd+fb4bCDjAxvklItzneSbpNLqhACIpepR9Zr/BLC56XAmzBUcoee0E0NEsxs7cQhKIQNHzGgGSUqIouXfbze0DcjWY+nRhDRQkUy9GKLEAdJVdldmCkjmULXSz8JRX29m1JjF5zVC0xtnbYPxUND3y6r+iYQjnqCER3pGKnj8U7ViC1+8bYczt8byVkBHm824xrJmpBjODhD4tDAy+vS2ukGNW799lBnSzuWEwiUGHVQBstEbhmZiYijDBgb3AZHV3Oa9IsD4fg62V7LHaGTl2JbFz3B1NJpI3H9XWSRSb3HTH6P5W2iYbJQeJjZxp5mkZdw8NShSx1M1hECIYlesZzdhGVOlXuQtxM4RzNKFPFsJ4TkteTwUiW3/GkZn1Y7U2t3/C5vLaO+7cXz2LnNEJSESZiKOWZXvDDxTXi8B+UwCHHCxF6Z7/ZHWUWV1HbIEwdGX4Z27hGLhesa8zwDrjQnSico9/PQpmR815pnMeINJlhOlewuU7lcphSe6xocrmmx0fITI4/XapQNDiX31iUy9nfYFV06C8P8PPRbtGzSA56rh54R0zg9iN3V5G684TSJf95QaEuUmU7R/lE9d1c5GYn75VbEG/vglg2G97eTGV3FNBySpJU3rSxh92tXFuaBzph1ZgVV3q77FZz6aMBkJ3IyxTN3IMpi1L0yXudGCYnbq7aGxXNN4yFBwES72ff9zUS3+A66rg+xiNNF2Sp2g6irm9GrW013UspUk5ImLKFucYk8QYNOowp+rLZ7y5H74+64Ic4ruLi6dlaSxIpOLpKhVFUyVV7Cb3b5lU2tbdyn/qrd0bCCwz3oQzBqwFX6hK2p6Sgru3pHcUtQ08oIOtpSMzd3dicIHEKcplgWJH51CRNblke9PmTQUneYIN/gFH1Ers0dOkqn5sSaJ6oRjH5A9Lxvpoi+DahAGqzKugyu1ORewehBy7nkMuZKVcgCVJqb5Xq3zK92VZrJdPca2tOLbgWmh9yB9Mkyte5IHbRACLAtYeG0bjhbodldDo7Ft0RSj1fasuE25xxMR+oOi+gLfssaho6VQbKWy7hvGS+ljjJHgdbcN1CI2WQ3Hb0XuKIN69aq9idcFdHzSoQBXxB2YZR3fN1VVicfVyZkp9U0kK3SXgp9MG9eat3vMATdfJJdnvhjLIvk9sZLq8AZ7lsnK1pCvO4UbIutWeV+H3UISVcHnjB4Ha5LAQmpc4v76EGTj60wOSs909WElaAdRZ4x+GIO9Wir3s4QNoQFjchRgjYn7a6CvAVWwlvQOnJ+dL8S4lLCVJhu4NgIMPp6wxAF6nYHss0A0Y1bsXRLjdZBZ87HhrEm89jX+e0a72VUbwrXLxVcytdqIJdXRHI0eKONDLlL4r478CpUDwIB5vROFyeyd+5y7tWT3KxJjKv4lGtYwrT8c64I9DBcWDCprjthB0FwkmpOtiTHXc90dh0ydRin6Ha1xC/nS152XAGghSH8wNJdOYwmdltKyKW9iMyNEiPE9FcChmPLo9U5Jr0fCWvVnnb37RnZb0Du0lTqp8tVJuBE2QW3oy4Gmn8ICN33WrZeSksi3BUHsWluVMidZba8nj3MaiyqSweLP056lDNJ0yFypAhu7sVonrpoLIi9BEu2muPJgdbTsVZZoa1PsplE4lnQ9mCU2JYkfsqE1AQAL3iSMag4HEdZtbudUM8+4lQW3zfs3tPFLBDz7spg9DmN+xWgyqGekjjCckMNllIqnhuCJG+Cie4U+BzQnrqdCmi5JI/Aq/ebKuailtgZxNYY24Vo7OrxlF231DZELpfzLoZBR0uKciXLEE6w0Ko8KW7l7+DzVpIQd+uEfCtSzVZUhJHMtPx+0FypoPCGXy/TZlvvaazIos6jJtAlXY7nOkMplOyxW3YqggnU3e2qQBQhY4RIjS3TQn57uWZVNerwEU3VMLPRobJznF0rFj3Z9hEm9kkuSySNRVOn2RKcYuQhMYXCOVYHZ6trUqdTtyt0U3o2uhc2FfqqEGfcmhRhaEOlihabGn0J+5CSnKgteS4SwIhjnkyPs1bBRscb+NDXV7WsLt1ILyvLQSpj6SvO4Eaa40CTqm7uZ1xR7fJe7nKSaNeWkvvj/QSmucsIJVhp1elqJBvb9HBEPa2Glb5KPUZzjaxZr9z2bkBnlLpIwCGHSjgox5OfeFcm6xhkeeqH0ZNPNLY656YobE0KjSMGzY8elquYKuSOqMAAoigwH2XVQaN9kkcEotgbIx1SQXrsqq0TV2HNFdPBz1JQu2HOdygJDjjX1j2N6RrZaW6FMwG5Vg5wv1lfWIhVbsfEc2FUn8czxeUVdgPJyXbf0nFy0RV4L4rQVq2biBBUfld7CZac0caoJjfAzq0hZ14QlxJZwNi+s1ia5rw22B4ve8GJppoVL4YJupGK5iQXXVOSehy2t/K08oxDOCxdGJpYmMNQOznDKb+m6maPu6WbbrGUUIzOajhvC+WSLNL+PbPOTTlUGd24eyy2U4ukoN3ZqA7XPbo0FVvs4h6rV1ZQ1pk04MhB7H0cSkabXh1xX8GMSTWUxjJ3rUR0q8Bb7cXekuLMguPbiON2lA2rnZd3/DVJ4SzY3FF1f+UPQ87G/Z0KNf3WR0N1a6w2PHkJ7gm5dNXcUCaXUmU2U5XTK5RqAzfV26Sr9yGs0l7n5bnYXTpjM3SwYl4yLA23mmCJsnYoAzpY5xMzWuvhiB9wwOHORanaoMPGuCVi0EQdNKUVCWx7m+7OssQg/FDZYz5YZ/nmb4g6pVqPuOEUech6BfGiHF03tB1nu3tqC+61FfgkWlfUNQtd2yHgLMaI0JciOaZ7yr2urDxvsLHDOXhUdgeBtyymz2xVc70lg8tqBrX9zs4NJ4AITZKCZjMI4lqpXQ7ZTjd1wBiHDU1CuoTYyXZzudULVBBudAzwSAspeMC3G9O1G++4gUx3o9mbrakSrcysrsQZrrI9lNvRHloh/koGjbuB2X3uFTZsytdo6au5uspLLvcRm8FIv/RCl2bDFg+cfulpWrMEzXYo3eP2njV2qNQwLBZ2DY9ouIUgv69xq0WoIaucDR6AWc9vzy2xqpwYMg4SdPDLjG/oSbAjFcea3i2zDb47bNvu4Kppc2rJ/Wr0qeYwyGs6pzkBNLwcg+5RWrg7uzIQI29/P4gbKANHgGK5XQzX51r0Zo1iHrcbPwWUhuQ3BjOa7Rq+qmNyOo3CDV2OGn6I+mWx0sGs2kf4cgWjh5Wlh9oyzvBOyE1yONB4fPQM85S4VSdTq41AHDLfXbeS2fBKEZUhstb1BLmsJ1P2vUMH0xaYlwMXAiNBDl82W1zb5cZpzd9KWPLsAm07uRhW62GL7hNIqgliC/euYK0NsU3mxy5/+cvbh7ffH/e9/cu/VZuf+Pw/e/D0fEb09ecnj+eYnuV+epz16V9X6a8f3ionAgo9H67VaRu8HkX9zaO1j//s8eS8e3z+/Ovro+nnY/XGCuYfRb9FudvWTTV+qYv08eMTsMNu6/mHlPWsoQPe//Qg9mXE8wFsFORfmuJL5TVR5b3NP3Ocf1PiuZHVfP0avB41gvWvR85fQLl/8apyNvP16wVgHf6OvONvv/1fvpoPHs4uAAA= -->
