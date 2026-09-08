---
name: "rar-cowork-cookbook-adaptive-card-develop-brand-kit"
description: "Generates a read-only Adaptive Card JSON file summarizing develop brand kit status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_brand_kit", "rar_sha256": "7ab30c7320211a2e501eac79a0348d39c06f47e7e4558fa4020339ffe8fb33bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
