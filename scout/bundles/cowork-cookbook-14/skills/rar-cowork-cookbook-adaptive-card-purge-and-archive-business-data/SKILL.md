---
name: "rar-cowork-cookbook-adaptive-card-purge-and-archive-business-data"
description: "Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_purge_and_archive_business_data", "rar_sha256": "ee31c9ae3d083f6bd241eda447e5d5c63631cff4c08d22c189b3e2d38752a822", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_purge_and_archive_business_data`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_purge_and_archive_business_data_agent.py` and in the RCI capsule.

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

Purge and archive business data Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data
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
      "description": "Date/timestamp shown in the card header and used in the filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 ee31c9ae3d083f6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_purge_and_archive_business_data_agent.py` first:

```bash
python3 adaptive_card_purge_and_archive_business_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_purge_and_archive_business_data_agent.py   # or on stdin
python3 adaptive_card_purge_and_archive_business_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purge and archive business data Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_purge_and_archive_business_data',
    "version": '3.0.2',
    "display_name": 'Purge and archive business data Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-purge-and-archive-business-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53ab1d529c84ee7f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/purge-and-archive-business-data'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-purge-and-archive-business-data', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date/timestamp shown in the card header and used in the filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical purge and archive business data status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-purge-and-archive-business-data-2026-05-24-card.json' that visualizes the current state of purge and archive business data. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current purge and archive business data KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing purge and archive business data status for USMF as of today.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp shown in the card header and used in the filename.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of D365 purge/archive business data status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPurgeAndArchiveBusinessData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPurgeAndArchiveBusinessData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp shown in the card header and used in the filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardPurgeAndArchiveBusinessData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
