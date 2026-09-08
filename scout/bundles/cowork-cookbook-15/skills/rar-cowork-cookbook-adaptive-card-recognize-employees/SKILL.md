---
name: "rar-cowork-cookbook-adaptive-card-recognize-employees"
description: "Generates a read-only Adaptive Card JSON file visualizing recognize-employees status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recognize_employees", "rar_sha256": "cc262b098b1ae0fd5cf308637f914b90d1770a8fc3844ce7860ea418b705d91d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recognize_employees`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recognize_employees_agent.py` and in the RCI capsule.

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

Recognize employees Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing recognize-employees status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
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
    "as_of_date": {
      "description": "Date used for the snapshot timestamp and output filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-recognize-employees-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 cc262b098b1ae0fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recognize_employees_agent.py` first:

```bash
python3 adaptive_card_recognize_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recognize_employees_agent.py   # or on stdin
python3 adaptive_card_recognize_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize employees Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing recognize-employees status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recognize_employees',
    "version": '3.0.2',
    "display_name": 'Recognize employees Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing recognize-employees status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-recognize-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recognize-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '11b80687d3d7ab61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/recognize-employees'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recognize-employees', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the snapshot timestamp and output filename, e.g. 2026-05-24.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-recognize-employees-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical recognize employees status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-recognize-employees-2026-05-24-card.json' that visualizes the current state of recognize employees. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current recognize employees KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing recognize-employees status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing recognize employees status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the snapshot timestamp and output filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-recognize-employees-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of recognize employees status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRecognizeEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecognizeEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the snapshot timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-recognize-employees-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardRecognizeEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
