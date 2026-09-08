---
name: "rar-cowork-cookbook-adaptive-card-revalue-and-adjust-assets"
description: "Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_and_adjust_assets", "rar_sha256": "024b71b469273cb2ec84808eafe026d9469d3f9f5c67fa9d9225acf7318b2e80", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_revalue_and_adjust_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_revalue_and_adjust_assets_agent.py` and in the RCI capsule.

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

Revalue and adjust assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
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
      "description": "Date used for the snapshot and in the output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 024b71b469273cb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_and_adjust_assets_agent.py` first:

```bash
python3 adaptive_card_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_and_adjust_assets_agent.py   # or on stdin
python3 adaptive_card_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_and_adjust_assets',
    "version": '3.0.2',
    "display_name": 'Revalue and adjust assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07b946f18740ca43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the snapshot and in the output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical revalue and adjust assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-revalue-and-adjust-assets-2026-05-24-card.json' that visualizes the current state of revalue and adjust assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current revalue and adjust assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing revalue-and-adjust-assets status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing revalue and adjust assets status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the snapshot and in the output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of fixed asset revaluation/adjustment status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRevalueAndAdjustAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueAndAdjustAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the snapshot and in the output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
