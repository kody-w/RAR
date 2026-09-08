---
name: "rar-cowork-cookbook-adaptive-card-develop-brand-kit"
description: "Generates a read-only Adaptive Card JSON file summarizing develop brand kit status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_brand_kit", "rar_sha256": "7ab30c7320211a2e501eac79a0348d39c06f47e7e4558fa4020339ffe8fb33bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_brand_kit`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_brand_kit_agent.py` and in the RCI capsule.

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

Develop brand kit Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop brand kit status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit
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
      "description": "Dynamics 365 legal entity to read from (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-brand-kit-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename.",
      "type": "string"
    },
    "subject_area": {
      "description": "The process or area to visualize, e.g. develop brand kit.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 7ab30c7320211a2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_brand_kit_agent.py` first:

```bash
python3 adaptive_card_develop_brand_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_brand_kit_agent.py   # or on stdin
python3 adaptive_card_develop_brand_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop brand kit Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop brand kit status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_brand_kit',
    "version": '3.0.2',
    "display_name": 'Develop brand kit Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing develop brand kit status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-brand-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a10092b375db394e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-brand-kit'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-develop-brand-kit', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to read from (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-brand-kit-2026-05-24-card.json.', 'snapshot_date': 'Date used in the card timestamp and output filename.', 'subject_area': 'The process or area to visualize, e.g. develop brand kit.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop brand kit status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-brand-kit-2026-05-24-card.json' that visualizes the current state of develop brand kit. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop brand kit KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing develop brand kit status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON showing develop brand kit status from D365 USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'The process or area to visualize, e.g. develop brand kit.', 'name': 'subject_area'}, {'description': 'Date used in the card timestamp and output filename.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-brand-kit-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a shareable Adaptive Card snapshot of develop brand kit status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopBrandKit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopBrandKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-brand-kit-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename.', 'type': 'string'}, 'subject_area': {'description': 'The process or area to visualize, e.g. develop brand kit.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopBrandKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
