---
name: "rar-cowork-cookbook-ppt-exec-rate-loads"
description: "Builds a read-only executive PowerPoint deck on rate loads from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_rate_loads", "rar_sha256": "fff2defc3f43601fd6affffaee9c381c777ec3ba63eb4652592331984847f7eb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
