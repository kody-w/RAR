---
name: "rar-cowork-cookbook-adaptive-card-install-and-commission-assets"
description: "Generates a read-only Adaptive Card JSON file visualizing install-and-commission-assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_install_and_commission_assets", "rar_sha256": "b36fc2f9ae0849ad002578079fbdf1ea8d79a5bee2ff43f188e95384bffc7a44", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_install_and_commission_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_install_and_commission_assets_agent.py` and in the RCI capsule.

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

Install and commission assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing install-and-commission-assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets
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
    "action_buttons": {
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and file naming.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-install-and-commission-assets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_install_and_commission_assets_agent.py` and embedded as the fenced Python below (sha256 b36fc2f9ae0849ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_install_and_commission_assets_agent.py` first:

```bash
python3 adaptive_card_install_and_commission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_install_and_commission_assets_agent.py   # or on stdin
python3 adaptive_card_install_and_commission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Install and commission assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing install-and-commission-assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_install_and_commission_assets',
    "version": '3.0.2',
    "display_name": 'Install and commission assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing install-and-commission-assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-install-and-commission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3a7041f239d60905',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/install-and-commission-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-install-and-commission-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-install-and-commission-assets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical install and commission assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-install-and-commission-assets-2026-05-24-card.json' that visualizes the current state of install and commission assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current install and commission assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing install-and-commission-assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of install and commission assets status in USMF for 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-install-and-commission-assets-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of install and commission assets status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardInstallAndCommissionAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardInstallAndCommissionAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-install-and-commission-assets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardInstallAndCommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
