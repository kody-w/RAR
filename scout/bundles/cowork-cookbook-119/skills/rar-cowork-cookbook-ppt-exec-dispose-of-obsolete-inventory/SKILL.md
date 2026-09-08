---
name: "rar-cowork-cookbook-ppt-exec-dispose-of-obsolete-inventory"
description: "Builds a read-only executive PowerPoint deck on obsolete inventory disposal from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory", "rar_sha256": "bab469b397619ec1bbbfe2546535afc9f93e3f61f27895705a355727481249b3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_dispose_of_obsolete_inventory_agent.py` and in the RCI capsule.

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

Dispose of obsolete inventory Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on obsolete inventory disposal from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-dispose-of-obsolete-inventory
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-dispose-of-obsolete-inventory-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_dispose_of_obsolete_inventory_agent.py` and embedded as the fenced Python below (sha256 bab469b397619ec1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_dispose_of_obsolete_inventory_agent.py` first:

```bash
python3 ppt_exec_dispose_of_obsolete_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_dispose_of_obsolete_inventory_agent.py   # or on stdin
python3 ppt_exec_dispose_of_obsolete_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispose of obsolete inventory Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on obsolete inventory disposal from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-dispose-of-obsolete-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory',
    "version": '3.0.3',
    "display_name": 'Dispose of obsolete inventory Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on obsolete inventory disposal from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-dispose-of-obsolete-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-dispose-of-obsolete-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f17775843fd7aa7e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/dispose-of-obsolete-inventory'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-dispose-of-obsolete-inventory', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-dispose-of-obsolete-inventory-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for dispose of obsolete inventory reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on dispose of obsolete inventory for a 15-minute monthly review. Produce 'ppt-exec-dispose-of-obsolete-inventory-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads dispose of obsolete inventory data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on obsolete inventory disposal from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive deck on obsolete inventory disposal for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-dispose-of-obsolete-inventory-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready deck on obsolete inventory disposal status for a short monthly review, sourced from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDisposeOfObsoleteInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDisposeOfObsoleteInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-dispose-of-obsolete-inventory-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDisposeOfObsoleteInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
