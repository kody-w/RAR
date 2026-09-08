---
name: "rar-cowork-cookbook-adaptive-card-track-campaign-expenses"
description: "Generates a read-only Adaptive Card JSON file visualizing campaign expense tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_campaign_expenses", "rar_sha256": "f0118e0800a2acf650d379f7dacb4e3828b657d7e8e7f1abfc9a1b36ad4c91b2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_campaign_expenses`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_campaign_expenses_agent.py` and in the RCI capsule.

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

Track campaign expenses Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing campaign expense tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-campaign-expenses
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
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
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
      "description": "Name of the generated Adaptive Card JSON file.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 f0118e0800a2acf6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_campaign_expenses_agent.py` first:

```bash
python3 adaptive_card_track_campaign_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_campaign_expenses_agent.py   # or on stdin
python3 adaptive_card_track_campaign_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track campaign expenses Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing campaign expense tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-campaign-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_campaign_expenses',
    "version": '3.0.2',
    "display_name": 'Track campaign expenses Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing campaign expense tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-track-campaign-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-campaign-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df919e2749bb7625',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/track-campaign-expenses'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-track-campaign-expenses', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the generated Adaptive Card JSON file.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical track campaign expenses status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-track-campaign-expenses-2026-05-24-card.json' that visualizes the current state of track campaign expenses. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current track campaign expenses KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing campaign expense tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing campaign expense tracking status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the generated Adaptive Card JSON file.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of campaign expense status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardTrackCampaignExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackCampaignExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated Adaptive Card JSON file.', 'type': 'string'}},
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
    print(AdaptiveCardTrackCampaignExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
