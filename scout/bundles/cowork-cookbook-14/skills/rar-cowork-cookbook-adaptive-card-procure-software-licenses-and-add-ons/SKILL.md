---
name: "rar-cowork-cookbook-adaptive-card-procure-software-licenses-and-add-ons"
description: "Generates a read-only Adaptive Card JSON file summarizing procure software licenses and add-ons status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons", "rar_sha256": "e2e31401f89cb74ae7f5f74956e075fa96e8d767f6427856cbfdcc9deb2feeef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_procure_software_licenses_and_add_ons_agent.py` and in the RCI capsule.

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

Procure software licenses and add-ons Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing procure software licenses and add-ons status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-procure-software-licenses-and-add-ons
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
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to write, e.g. adaptive-card-procure-software-licenses-and-add-ons-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_procure_software_licenses_and_add_ons_agent.py` and embedded as the fenced Python below (sha256 e2e31401f89cb74a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_procure_software_licenses_and_add_ons_agent.py` first:

```bash
python3 adaptive_card_procure_software_licenses_and_add_ons_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_procure_software_licenses_and_add_ons_agent.py   # or on stdin
python3 adaptive_card_procure_software_licenses_and_add_ons_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procure software licenses and add-ons Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing procure software licenses and add-ons status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-procure-software-licenses-and-add-ons
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons',
    "version": '3.0.2',
    "display_name": 'Procure software licenses and add-ons Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing procure software licenses and add-ons status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-procure-software-licenses-and-add-ons',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-procure-software-licenses-and-add-ons',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06690257c5b13360',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/procure-software-licenses-and-add-ons'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-procure-software-licenses-and-add-ons', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to write, e.g. adaptive-card-procure-software-licenses-and-add-ons-2026-05-24-card.json.', 'snapshot_date': 'Date used in the card timestamp and output filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical procure software licenses and add-ons status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-procure-software-licenses-and-add-ons-2026-05-24-card.json' that visualizes the current state of procure software licenses and add-ons. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current procure software licenses and add-ons KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing procure software licenses and add-ons status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of procure software licenses and add-ons status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to write, e.g. adaptive-card-procure-software-licenses-and-add-ons-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of software license and add-on procurement status from D365 ERP, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardProcureSoftwareLicensesAndAddOns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProcureSoftwareLicensesAndAddOns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to write, e.g. adaptive-card-procure-software-licenses-and-add-ons-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename.', 'type': 'string'}},
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
    print(AdaptiveCardProcureSoftwareLicensesAndAddOns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
