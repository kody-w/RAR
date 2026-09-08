---
name: "rar-cowork-cookbook-adaptive-card-procure-software-licenses-and-add-ons"
description: "Generates a read-only Adaptive Card JSON file summarizing procure software licenses and add-ons status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons", "rar_sha256": "e2e31401f89cb74ae7f5f74956e075fa96e8d767f6427856cbfdcc9deb2feeef", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
