---
name: "rar-cowork-cookbook-adaptive-card-identify-training-needs"
description: "Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_training_needs", "rar_sha256": "7e182e5695f7b7c370b53ee518ddf2a16844fef6b0badd4854b63b4727b7eb2f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
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
      "description": "Date the snapshot represents; used in the card timestamp and file name.",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 7e182e5695f7b7c3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_training_needs_agent.py` first:

```bash
python3 adaptive_card_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_training_needs_agent.py   # or on stdin
python3 adaptive_card_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_training_needs',
    "version": '3.0.2',
    "display_name": 'Identify training needs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4a6286d600d2999c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the snapshot represents; used in the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical identify training needs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-identify-training-needs-2026-05-24-card.json' that visualizes the current state of identify training needs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current identify training needs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing identify training needs status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents; used in the card timestamp and file name.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.', 'name': 'output_file_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of identify training needs status pulled from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardIdentifyTrainingNeeds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyTrainingNeeds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the snapshot represents; used in the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
