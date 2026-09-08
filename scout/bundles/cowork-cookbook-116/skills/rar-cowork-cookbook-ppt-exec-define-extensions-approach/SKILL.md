---
name: "rar-cowork-cookbook-ppt-exec-define-extensions-approach"
description: "Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_extensions_approach", "rar_sha256": "10172870bd575cda52699046db7ee0b9831a6daba6bdc12f0c4e499235cb79e2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
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
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 10172870bd575cda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_extensions_approach_agent.py` first:

```bash
python3 ppt_exec_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_extensions_approach_agent.py   # or on stdin
python3 ppt_exec_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_extensions_approach',
    "version": '3.0.3',
    "display_name": 'Define extensions approach Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '41288af9c7ec030f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define extensions approach reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define extensions approach for a 15-minute monthly review. Produce 'ppt-exec-define-extensions-approach-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define extensions approach data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.', 'example_request': 'Build an exec PowerPoint on define extensions approach from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define extensions approach status from D365 F&SCM for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineExtensionsApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineExtensionsApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
