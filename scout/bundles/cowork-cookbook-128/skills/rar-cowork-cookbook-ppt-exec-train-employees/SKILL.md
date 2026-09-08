---
name: "rar-cowork-cookbook-ppt-exec-train-employees"
description: "Builds a read-only executive PowerPoint deck on train employees status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_train_employees", "rar_sha256": "ae5fd6e40d00eaf0ecf9f38ce5a7de5f1e5e1024505be2d70933b64e43007bdf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
