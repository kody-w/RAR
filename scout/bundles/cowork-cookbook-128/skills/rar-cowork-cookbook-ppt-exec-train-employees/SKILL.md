---
name: "rar-cowork-cookbook-ppt-exec-train-employees"
description: "Builds a read-only executive PowerPoint deck on train employees status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_train_employees", "rar_sha256": "ae5fd6e40d00eaf0ecf9f38ce5a7de5f1e5e1024505be2d70933b64e43007bdf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_train_employees`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_train_employees_agent.py` and in the RCI capsule.

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

Train employees Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on train employees status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-train-employees
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
      "description": "Prior period to trend the current numbers against.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-train-employees-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped to, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_train_employees_agent.py` and embedded as the fenced Python below (sha256 ae5fd6e40d00eaf0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_train_employees_agent.py` first:

```bash
python3 ppt_exec_train_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_train_employees_agent.py   # or on stdin
python3 ppt_exec_train_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Train employees Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on train employees status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-train-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_train_employees',
    "version": '3.0.3',
    "display_name": 'Train employees Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on train employees status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-train-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-train-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'faf09bff1b1e3870',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/train-employees'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-train-employees', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the current numbers against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-train-employees-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for train employees reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on train employees for a 15-minute monthly review. Produce 'ppt-exec-train-employees-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads train employees data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on train employees status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Make an executive PowerPoint on train employees for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-train-employees-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the current numbers against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready train employees deck for a short monthly review, sourced from Dynamics 365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecTrainEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTrainEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the current numbers against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-train-employees-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecTrainEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
