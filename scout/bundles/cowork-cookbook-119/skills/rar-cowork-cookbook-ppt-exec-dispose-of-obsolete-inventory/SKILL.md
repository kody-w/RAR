---
name: "rar-cowork-cookbook-ppt-exec-dispose-of-obsolete-inventory"
description: "Builds a read-only executive PowerPoint deck on obsolete inventory disposal from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_dispose_of_obsolete_inventory", "rar_sha256": "bab469b397619ec1bbbfe2546535afc9f93e3f61f27895705a355727481249b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
