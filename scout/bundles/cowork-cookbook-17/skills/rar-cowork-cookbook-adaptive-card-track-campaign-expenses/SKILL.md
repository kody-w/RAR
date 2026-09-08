---
name: "rar-cowork-cookbook-adaptive-card-track-campaign-expenses"
description: "Generates a read-only Adaptive Card JSON file visualizing campaign expense tracking status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_campaign_expenses", "rar_sha256": "f0118e0800a2acf650d379f7dacb4e3828b657d7e8e7f1abfc9a1b36ad4c91b2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
