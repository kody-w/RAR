---
name: "rar-cowork-cookbook-adaptive-card-manage-lead-identification-process"
description: "Generates a read-only Adaptive Card JSON file visualizing lead identification process status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_lead_identification_process", "rar_sha256": "197d241ac80053aac57622dfc5bd2457198e5741c6b72a4a396a7540bb578ec1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_lead_identification_process`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_lead_identification_process_agent.py` and in the RCI capsule.

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

Manage lead identification process Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing lead identification process status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process
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
      "description": "Dynamics 365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-lead-identification-process-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 197d241ac80053aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_lead_identification_process_agent.py` first:

```bash
python3 adaptive_card_manage_lead_identification_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_lead_identification_process_agent.py   # or on stdin
python3 adaptive_card_manage_lead_identification_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage lead identification process Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing lead identification process status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_lead_identification_process',
    "version": '3.0.2',
    "display_name": 'Manage lead identification process Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing lead identification process status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-lead-identification-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'feef456b6e035eaf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-manage-lead-identification-process', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-lead-identification-process-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage lead identification process status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-lead-identification-process-2026-05-24-card.json' that visualizes the current state of manage lead identification process. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage lead identification process KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing lead identification process status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON of the lead identification process status in USMF for Teams.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-lead-identification-process-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of lead identification process status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageLeadIdentificationProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageLeadIdentificationProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-lead-identification-process-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageLeadIdentificationProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
