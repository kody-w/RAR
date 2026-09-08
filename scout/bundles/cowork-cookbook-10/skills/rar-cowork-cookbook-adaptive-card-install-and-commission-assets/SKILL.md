---
name: "rar-cowork-cookbook-adaptive-card-install-and-commission-assets"
description: "Generates a read-only Adaptive Card JSON file visualizing install-and-commission-assets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_install_and_commission_assets", "rar_sha256": "b36fc2f9ae0849ad002578079fbdf1ea8d79a5bee2ff43f188e95384bffc7a44", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
