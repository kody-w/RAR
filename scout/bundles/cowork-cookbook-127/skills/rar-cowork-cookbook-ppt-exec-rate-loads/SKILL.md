---
name: "rar-cowork-cookbook-ppt-exec-rate-loads"
description: "Builds a read-only executive PowerPoint deck on rate loads from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_rate_loads", "rar_sha256": "fff2defc3f43601fd6affffaee9c381c777ec3ba63eb4652592331984847f7eb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_rate_loads`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_rate_loads_agent.py` and in the RCI capsule.

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

Rate loads Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on rate loads from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-rate-loads
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
      "description": "Prior period to trend current rate loads against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull rate load data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-rate-loads-2026-05-24.pptx.",
      "type": "string"
    },
    "review_context": {
      "description": "Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_rate_loads_agent.py` and embedded as the fenced Python below (sha256 fff2defc3f43601f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_rate_loads_agent.py` first:

```bash
python3 ppt_exec_rate_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_rate_loads_agent.py   # or on stdin
python3 ppt_exec_rate_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rate loads Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on rate loads from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-rate-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_rate_loads',
    "version": '3.0.3',
    "display_name": 'Rate loads Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on rate loads from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-rate-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-rate-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd800fe2746dee411',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/rate-loads'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-rate-loads', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current rate loads against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull rate load data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-rate-loads-2026-05-24.pptx.', 'review_context': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for rate loads reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on rate loads for a 15-minute monthly review. Produce 'ppt-exec-rate-loads-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads rate loads data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on rate loads from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build me an executive rate loads PowerPoint for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull rate load data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-rate-loads-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_context'}, {'description': 'Prior period to trend current rate loads against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive rate-loads deck for a short monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecRateLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRateLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current rate loads against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull rate load data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-rate-loads-2026-05-24.pptx.', 'type': 'string'}, 'review_context': {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecRateLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
