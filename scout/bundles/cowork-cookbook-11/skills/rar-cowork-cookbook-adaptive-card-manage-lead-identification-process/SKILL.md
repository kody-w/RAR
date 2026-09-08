---
name: "rar-cowork-cookbook-adaptive-card-manage-lead-identification-process"
description: "Generates a read-only Adaptive Card JSON file visualizing lead identification process status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_lead_identification_process", "rar_sha256": "197d241ac80053aac57622dfc5bd2457198e5741c6b72a4a396a7540bb578ec1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
