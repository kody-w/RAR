---
name: "rar-cowork-cookbook-adaptive-card-recognize-employees"
description: "Generates a read-only Adaptive Card JSON file visualizing recognize-employees status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recognize_employees", "rar_sha256": "cc262b098b1ae0fd5cf308637f914b90d1770a8fc3844ce7860ea418b705d91d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebOjVpbnV9G8jhjbTeZj37KjIgYkJEACLSwSOB1pdhD7JkBuf/e5SO9l2uWsrqqI+WfkRQLuPfv5nXPe5bcXp+/isnn59KIFTrHYOFmWxEGzcAp/sSyHsknBV5m64L+FVxZdk7h9Vzbty4cXP2i9Jqm6pCzA9k1QBI3TBe3CWTSB438si2xacL4DFtyCxdJp/IWs7dVFmGTB4pa0vZMl96SIwGqvjIrkHnwM8iorpwDQaDun69tF2JT5YjUVTp547QKnyMX6f2tLZRGWQMJFBAgXiyyInGwRFF3STR8WQ9LFixjwD5oPi+1BWnSAXfthceI2i6YcPjwUc7xZ6AXQpCuL9hXoEowO4B20L59+/uXDSwJ+v3z67cXLnBbcennXYlbi9C6t8C4s2J45RQTWVROwZQGuq6ABIubglh+Ei7erH9sgCz8s/vM/08FpovanT5+Lxdvn88v8z6kvFl0cLLrSabvAX3hO5bhJBvR6XXDZ4EwtsFXXN8Vs4xa4oohenzu/USqrxd/mZz8+mbxGQffj55eymn0DdP788tMC2O7zS9PPv19nKtWPP71m5RA0P/70jU7bu9fA62ZiQOrXL2/Xb2TBwm9Lk3DxRTsIyzdewJ1JFQDif9Bv/jxFfyP3ZpIvz8U/ltWHxfcpz/r8Dcj7DDYX0P0+WWADsPPl9VomxY9vPJoSxIdTeMGPP/0jsl4ceGmWtN2/RPfnJ+FneP34ZpKfPjzc98sCetPtK81/zLYCAfPvaAKWv7P7aqh/RPvh2b8jnSUFSKp3X36X3Pc2QH9b/PwPdfufNnxYhJ9fVkEGcqZx3Cz4tPjtESI//+B/u/nDL78D0v+UjFb2jfeg8CV3iiQM2u7Ll59/aB+3f/jl5x/6CkRx4ORf+ib7Hs3v2fXB508WfFv145/3Av5GkRblUCy+5tDit7L6X83vrwsTIJj/7X77afHHTJw/0GJW4p3p0wR/yMYWyPoHO/708jvAngJo0z8Aaoae//iPhZJ4TdmWYbfQvLLvFsDBXZIHs/B6nLQL8O+MGk0A7NomwLBv60D8zx6eJS7Dxa//x3vA+UfvDc5h5w3VvngA1r58ReEvX1H419eFDgiXTRIlBcDYE3c4fC6cCGDtzLRqgjZobgCo3KkLPoJ8/jj/WCTF4td/SvvLg8xrNf36QOTkiXynpTSjXttnweus3zkGAP/UxgPVKRgDrwccstID4oRPZAdSlBmoMN1sizZNsmzhJ4AjqFLTgzaw16eZ2K+//uo6bfy5eMI0vniWrxYGC76Ks/j4EegVZkkUd5+LwIvLxQ+//f7D4r8X/9OuB/GZxwEUjDdvAAkf9Q5kV5+DZcBRwLUAOh7e+O33N+sCMqBwLoDvkjAJnptBdKaB/25qTeQ+YiS1cANgYmDevCqbbi6cSfe6kMLFV3kB0/nRXB3isu0WflAFhR8U3gSoOkCdr5Ysym7RghBsQ1Ay+zZ4cP3VbZyHiDlIc6f7daEsD6AWlRn43yzmYxHYXBYJMP/XQHjeB0SaH9oF/07idaHO8bionMap4sZ54xE6T7/M9fttOyDuLIpg+FzMZTeYTfVIjqd5ormtSLw3l358NA9emQMk8Nt33tFb6+Ev9EflbD4X7VvgO03w6C+AKNMi6hN/Lgf/9RZSbVz2mf+wH5B0pvTmBf/NK48Y/FrwF9/aE+3Znvy5u/ncYwhKLP4/boRmdbnN5iRsOF1YLQRVP1lPN8yt3+yuZ7cIGDw4P1LuW5fyjkTvgPy5yBIQU830X8+VD4Xf1jxBrm+ArU/c6UEfRA5ww0z3EdhzoDbNnBLO5+Id+YHYiwfMAakBCoAsmYPzneH89F3SGKT6fP2tC3jYFxgfKA6Cd1H1bgYCKwwC33W8FEg1e+vdiyDKgzlRhzjx4j9pNVsYBBOgvwBCJCDdQHV4/YrGz6fvov9p47PZmbc8GsEe5GbzIADkCGYBZ5fMfgPidc9OG+j56UEEqJFX3ay7C7IDaPq8GTRB3Sdt0s2ufdo1qAAMf5y/n5rOd4OxAgkBjAXCvuqBdR+JMsdcDgIEyACwAuRNnhSgtAOjvBnhQdDJ56wHqPrWez4pPm6/KRQ8smuuSe8bZ0XmPXOZf8auU0x/BAf9e2EC6OXzigffv4+0r9xm2jNAtgDkAMf3p89+4PVZ0p89w+Kd7qe/jDI//nvTzqNIG38OgE+LuOuq9hMMPwvre119BfAEP2Vtv9bYj3Md/PidBP8T4afOnxb/nnB/IvGWHJ8W6CvyisyPdm/B9fYBtlh+5K2PxPx0Rrdv6AnYlzmIrtlzEyjqX0vd+xJQ76IGoAxY/Cx97VwxB1CkH1gP3PC5+GO0z9kGSkkRzdHZln9AgUfNB5H/9NrXkgQeFR3g7c89YhTMk9kjN9rg5VPRZ9mHF4CAwb8ykc11J59jup0HOZA9oOfqkuBx5bRfyvCLD9SYr/48xq7A3bmY+d8CqwANSQykmwMcwHH+yKu3THpoM8v0YRG8Rq8LDMGojwj5ESNm2bupmoV9jmpzc/cAp7H7K9v944eTvS5WAQDCrP1jxL/VqblO/yExn/YFdvWAbh8W/qPkAJmBRLPac1I7LcgSoMd3ZXmUiy/PcvEdO8w15o8VZcbZugeJ/qapoSnr79L92t3+legZtBUzHb/8NFfYD2+oBr7BRPJh8XW4ANq8jXuP2bzowST98zzYzI59bJl/gD3g6+umr3+RcIOXX74n18NhX94d9lfp1BnSAOTPxv1H5RoIDwTwe+/d4f80wT9+C4nHmtdrC3qbvxoOSPjAclARZ2W/WfGbLuVjYpt1Abp3zz8w/PYCohwI0Tlvcf7W8oPlAPo+tnOjAwMsAAzB9TNrwbN/fxh4I9DGDuhFAQXPwyjMRVjGRZ0ACX3SC3GEoXA6ZFHCZREfpWnEYUIPZwjCC2iGQgKHQBmXRkifRX1A75n8X+Z2LpmFIlk6RFgWCwkUQ3w/CDHC9xmKoTySxhCHdR3SJVnH/bY1TQr/TdOnZrMZv84lj1x/Kvzbi0sRYKVItBL3/CxhFnUpfOdO8gW6U2F5cuqzrWx3I0Mqxu1EOdidNFp606XNJK/OWbvhjo4ssVwkKJtmpdRrzYyZSCfTAttTAe1pSjnZlC/vlL43jkvc8Q8F0+G7Dp8OG3aQWxVJqQTWkjV+tu995evJjUu2RtkXhs2ZVK0YMiIEyQVm6ABOMmNMxfhoCWXs8Z2A6IHM2uwQ3juIXZ9bU4PXJ0rfSqjJmm27LntmQi6p49q+Tfbx4cAi+WBQwvlK0+S5uTN3eK+r2NYnszjnmK2c7I08kUxlmV1aGZK3a7Mfx7CcCuIK7y9It0ymQoZ2LaX1pwr1dEHTTktFXlZWZmXG+SQXJbZZjSwL0GZ0+oJGGWY9wcHtCtMhyEKXMiSEOnKX08YYdVc92vRl59rb5L6Souq8pU45tD7Fnt003K0IVuctPkkqA6uRSna4JfHVKTYCa+KuXaGvyGPK17rpmcptSXJ7hTGXl82wHLdo1pTcBG2v95U5itswls/WxXEN73YxGTfas1XA2kUqDceTvM0SRLgiyIHZjd6olYYz5VfzxAdR4mvrTXvTTkqFNGcCq6sBY8uDpruhgCE8n2n8BfXk08EJ/DwM9jbpIvRympKTmh7WlNSWwqYXK0sQNIc6SkhnRVup8o6n0CIkuYoOrG92y9xENnErXO7G3p1GVK5Mm4Ou+pipGd5VsOZ2SHQgHV+Jo7OQyfbaTLclzarcGjsV+zFa7/nlabfRIIMolgTJ43dGW4r6MRhXAhEThHZwkgCrUUnZaeIhEGRd20HOZRqi0rUNSU13JJ0Zy9TC4lSnsnLt7NESZIINpoxa1iS/hk5agmFb1B/dwrbJ7XJNSx5NljhvrCEpvRnNXYPH7Q4NiR3iFkp6FbbwErSEHGMEw15y1XhwAlIsD7mPYeqO0bDtasvmCrsq4qsTuMqAe4ha4mVwPkDBEDmJYzGFCuUOrNECSYvnarNireUGyq+YdfCW7gGtru2NiWLyULUQVNwYczeo4cbKZEGjPHrDK5W7ZM8BJa4um/O6aNo4bFY2KXDaSrFFTVgd2ivucQ40bqUMRlanzgP+3UxHt03PvlpMfpequVsd10sk1zqecxpSWmqIdzQbigcBw9HKCi/skL4VUQIaE2RpQOIZTeRu5AMx1+1MzW2LCYNxN4iiUDPihWzWKxXN6xwhbAWDhdIN67NaOmZEGrEgphttxeJ3bZ+2q5sDnaENJDhLZ0eg3i5AQ08Yh/1dwjTyRh62HcoQXVTeRdqqE62WdJYWMX8sR3QgUqtJa5XbLtEVE+0Yuw82oXbVJxRFyn031WZYqXwbGTByWp4FW5e1dLejb6Uo7UJcStpczMXJtpl9Zms3ARIwh8ay61VPTewOaXJZs5fpKudEeKCZUtDZgRt7GXSITC5iGTwx5VKJ8lJHJIEXmz40WuywZtbn8rJp9YFm12HSSZWuwCLPXwXYuC0rIlIVrqVM+54Te2JovR0s0vI4qEbX8mjprceKVynmxC07pYKXDcNvU2403LzutPEkrjstvlCYnOMWw66ZwfXvp9zYCquigQ/aPa9wshhvZa2UABL3+uCR+NRYd4SVmJapyg0+iPw9rfaHBlKnI3zox70bYBfvFuRwS1OXMOKJDRNYkR5hSGrRK8am8ZOw70yb6QW1k3tHY8pTq8KyuYr2ub10iP5MyGwhT5LNMrvdUt4E8S3lm5E8D9Z9UxUypui0utmtgtuBgr176q1cND2KGgBhq3Qt+b7V3BZdBmWV7WUkr4wKW9lndEiNK5kq5lFaKhehyCpjSCR15zaH0kJlVGjvx4azrMJ32f0yuqhh78EKNxEEYqzsgXAmFU3YCwAM1ed7i1n3YSdN0S2t9cy/a/khD/GRZfpdBx37ZZ6N+Ta0ZP2QTnWqXZcrKtPcki5V/hqv10deVPDw5qz4jvbV/RRdNbt111AX3uAoZ2F4V5QGrJFWGO7NTmvpyblF+dmHtl2y5DbOcXdJ2V5M7XFdalXdoOfSzFbL0RM5eVitTJPt81VNmETCDo6L29nREY8yQ7jkSiZqSo7XZnzgfFvn8lZfLaMeEtPt6UhU14xTct6tUMXh7LNyHO06UEze5Jq9bV9l8aoOJzwlY6lTVCuDxiIE/UQlmVrmZj0SjfRyt215UqdXh6kV3LLuBnZJlF1N71Tkig0cckTGrXEzT3e9qylR0jWDLi3P9Y5HIStGN7uR8X7DCn2zZn1O8GNrkPfMtUk1aDoOCmiJGmJjJW6yiRNFCAm6K3fCOnOkISFX1yZHp80JCvm+WGLQ1PabarlcO8cKNwNpDWLkhGkFUV+2vi6o1mW1IXCmNWzyqOgyrwZBQtSlcFgKsX5M9G49WZCUhDWGHiUBqUVpbNfrFF7u08ZeecENcfttRu32y0T3Nrdq8Ec93o7KaMT1nWgno86tHjmVu5ZccXzJjZV26vqJxWprlMazt+Y6S4vGNNscLnbIb/nonCVJv7Q6h8b1feYnIoGiSrFJpIub41zT6+vEt9yTcdB9b0OWwcFshSt5Z9BI4VYn3mNQ377J7NiSSbakdwqyY6whODhGwcFplUnRzmW35XV/cTsxsbkcDclVut3Udrperw/n9SlaKznKiLiRI9fpRFlOFY+RVFiSmYPowEswhCuxMtZ8UvKQ6JKIcBe50NPy62FDHNdrfLt0kqZUj9BlpHPDpSn/7PHB5BKgArLpwKx1C2DnqqA6gk7goQ4lZD9Q9vaopPABR0ev39iET0+KrbeblYceL616Uq2YHbMSXTmqyxlKimjWPTlKRt0uoWqKMwCJSEmjUi0h/KYzjj5noMAmKcmoOdfWLWHz10w/lralYjh/ukeMGssEdrwFScMO0rGVPYFekrkCR5YRX6SzZax1UXfG/Xi5bT1nNxD70dgoLo96Wb1BcC/fIMt4mdIIiGzPtWIjPHLpajhm7XaypjR3Dqx8dTgmMKDeaXNOZRHcgu8MozPqdCLsnoNgj+Tp+wrWsYu2DUmKQy04ATWYMOVQSEXsVK0Pl7qybG91wO977aDcqWNjCjFoLQ7O+rQ/StvU2BwPWs9dwZByyizsfOTvra5Hu67C2u1IT1eSOhIneSrxdNBs+cR5XitGO/wqV+oOO0eHscQzd6Xoq5Fh4A3o6/cgjllmKu/ODjQ+t54f9kSVEW610+3aE1mhM6R1gjupZjORI1+Iq6+nusDqqjWU8mAKiN8IfOjkWz2DZAdFLASPrrZJK1xVWDE/hDuqCAsXJRwnlPfhztPz23S2uHB/sgavZlV+FW8PU7fqgIWiQ41lA6YQF7I7ueJlP8JNZHRd2WWgTYe2tXHLroIcKtTUtrVbVHxeNF7qB6uJMUo44ORad5mtZVGBLOS7gU873TWtJku9dieoNwGXSVmAyi16QkTP50dJtqoVFSqrgVKZ7WoX8pjQiRWzDga0Djc1nUg5eSbWurtRQGN822AivMRx8WRkCeFb1nSize16BAkDSZHoR3izwy7xqcTJtZavT03nOYylHHzUtcn0jh4KoViKJeHQt9VuJZrlsWQbnU2tjeyQyvGypdosC6KxlDOisMxxw4mwHja7pVGa3XrtSkq8OVQZfLlp6f2e4Pw6YSFp5O81KJG6B20xNJROoBrFXGZenUlEwHRpVxZ5P3ONWsSrWOHUiLM9A221Nkdp3QgkRUoOWleaq5bnB8xBsZYXuItUVTZjXFmTurOkbNhUo9ckjNlNAPqgkfFXBnqMiGlf9cgdzVIo3ehtq27grROaTa5JEcKeDtYoMFWGFeS6NnGRmS6YRlPWYXc5Lo8aHZUGaWbFbXUOzKa3T5dCFw4Rz212w0Zd7iZ9q6VWbvDh+baMT7JIbug099QamcINk7VNT5Cyb0Bty5W249ddGhw2GL4TbhW3TO3rslyeD+dIbKb4PCj59jiok8lfr6qCbg8hSp13SA7ziRM0fo0PJEwFqBtlBGEmI3sEGdMduLwXtBrjFI3fc90YQVdOmI6pZLWcSgdJ6NWRa5YGzmOVeIWD/bT0ln3iDaIjhxmc1z1hn26koUIJzOpGqazPKtKTksusbkpCoJRWbZGB9cpExCv4mJxIPIn22obnCG13lexd4p5pzU2LDNfdXnN0iOgG3AHz32g2fKuXHiFfhOPEkbLCF4Ja4Bm+8U8VBZ/PY2bDMbSsNPJymFYeJG6Gti3v58uugFR1uV2ZeJyHErPNIpU9o8gAVdW9doJeMJS63rlodwpIQuRqBypQzWx1rFlfzMONVa95KNqXDVzhydXMsQvFiO4+LtUrGXZoTce4jLcmZRS0H/hEU2RUoK6hPrjvXR5XfM3C8OJSeG4mkNCZ8k+kdnM8J4+I2mCdVgXt3VHP4zvX3UX1WPUFmVuisr71qdQebqbvFzx2ZXHQta10x0egIY9LwidM7YYbIXG33WO0ro3dPp0sVPDO9XI8Km5BBZrssedxuU1rd0dhDIRGDGh7YdLcFBNkqlekcFsGku53r1EuPlvdxXt1c2GhVUFRTnemNDUdvY4PO55FCpiBzzBxDAndxk4m2bc3ovb48uSSbhjemaSRVLrkq0BvM3LbpPK6GCk5YlagVEZQTnlYaGz7zaX2r05UpzKu8w7ImPudZ3hZvjIpqK4MKxVsVuJynaO5mxPpak1G9THQb+Vhc1/z1f6MFah9j2+K5xyvYzu4cRTebiBVL3K/d5Zeusth6biTrM5T4YBFUZSk3FFZj8FRvRHnFNctqx14TFfXdJYo1WFUzpMO15iO9Y6tkhNyMi6ry206rY/Uvjp6jQNpxo1ioKvo5pxhXwCBoy5Fp3AXEXoY9MuWVmgilstt03U2FfOmPhBZOtqkTflVHVxSADKHfe2ttM1dwyzEwVhMPUNH7Mx4V05n7m3s+sJ4gUa21IixJC1QxAxbiFoeCfKClW1rredCdKLGK8f6uqKj5Ck8N81WFJC7f+QYGTeuzlB7cbRzxnWgrs5KEW4LWdvvLD+i+Hby4LPYF5ma2UYKQ2BEIJjDKnZX1l0cro5JVO6qrA+ohwf8PsguETTWZYbdlXUunqjzxVRjuGr35FF2VBi6ExPEVNPGXx3WqIbvOURd+bGZbCl2td2fJyLni2pn+2pJ3fthvKd5kUoMVhdu6DjTbXe8cH6XmxNORpgbaFJ87+OrTSzZ0lrjBEENfVQz4UjbuXvF9L7cdeKUt1SEmBWsRqv8pmCoISKoIYx1sT5jZ4cVDZmquq0uKapHHDYWmK9KO7gFw+gNPmduLkfWj9cWEwzcYSdiR6gCIGum4ZrwpOAqSk3tn3ayTtu9onXeMALJbiYr5XfGWjf0vg+SvHMY6nJoDqLvG7jeDvcBLtQmw7fKTilrGx0CvGoyWA8Q283o+9XI7ugtsAwaw/D65h6hXe/QOhY322iMO79DXY/b40eC3DpkJ3XncdMSYiBsXW5zEDD05sFuLx5cBz2LyXqTOQR2NRCjCHSsqKrDhg/CfRZo18DW6BQWyaNPZtKSlHpramXkig5FiRNNxSvL5l6fMpQGvQV8uGW86XJVDWpIB3nG9sSWBSINt3xtU9FxjGF5vWpqWEjlI2mQSAwoo5zgaff7NrZVmomu1/IIT9juqh2gndWpndTcnKqI3Qgze0NNA/5eKWQGd2Zw93FJAePNPurDBBdETzgmTSu5XcMIB/Y+UsrhOIp2pbEKIsY25tzIBO5PancmV/6lpSak8bEMO4fOJSI1tkZOlo8HKrplbnnhmFU17nKo6zbotelcUsO2JnKVLWqkzntXul0ZrFWduFJ6dcSZnTS4CIRAFsPaw00jtyRebzCVFy+QYbI3qVjWy41eQtlNgv1OpmkydTTcnKYzK3tyKZQdwMq5xedLSg92F7MS1J6qHXNH6BlpM3ElqgOWekHviljjTY3fOD5t7C0StgQQe8IFWlvdis7wFR3HxB0q7utxR1lXabVbb6QCOe4DTj9FjhoRW5qlYQxOx2J50EQT13Z0XBm7rBJXx9B1E9rcWzkVujnKoqcQy46b6wQ1pNsUZ9frnSOV0rVoobh+2VtUZTIZFpeGeyqdstSoDdoZZ3h7sct1S+2w3Z0j1R539meUpjeeDvM0kmp7MtosK2W9QfFCaSPWdehD0fPn8S6WYrRZ4QfpGBnJgF+FkypBvDt6nLgr0UDMpC5P8QqyPJvUx+lIhXihE5uEUWwUw6nhAjrlTGwZ88hqEbRC9dt5vylMX8MFlKXv0I1WLxcTc++hX4bQOQ8hHy6mAhr9aNnQ6uB6t2t47CH+hO+Gg6U2comRXYYOucmPpn7uRmAEODVUPByqZO1fDsQ57MAkbN/NmkeJPWu76NTh6w6Manm+DqQLcl9hvX1VY5FmHeaAXHm6za7IpUmyLdoxO+8OyVrmq9Dhyq9Iy18ewYRZmzqkIIN54niBNQVd2yFTSx3cGDf8UOhR25mk4tqvwqwdN0hhc5jRiTxsHaZU06aNjdIT0CAZ6JLV/Rwb4gsLwdQausnHEh7vOn7Vm4DIIHec/+xWOQp66dmAb4L1/dBG+EE+LzPjhBAUV8WDs4vgJr/d1jjOHEK+Pu5xzqhoiIpdskynZgydFoHrwwo5YZeVZ935cWfuU0jpCUKEh36v8MrtYAgcx/3tby8fXr4deL38629lzUcs/89Oep6HMu+vYTyO8gLH//Tg9enfkOmXDy+NlwCJnudZbdZHb4c/f3ea9fGfnsrN26fnq07vR7LP8+XOieaXgF+Swu/brpm+tGX2eA0D7HD7dn5tsJ3fLPXA9x9PI/+kBriOkyb40pVAoQ78epnf65tfsAj8ZD52fl5Gbyd8H178tzd7vuAU+SVoqlnVt5N8oCH+irxiL7//XzpIR3qsLQAA -->
