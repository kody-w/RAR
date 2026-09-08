---
name: "rar-cowork-cookbook-adaptive-card-analyze-marketing-trends"
description: "Generates a read-only Adaptive Card JSON file visualizing marketing trend status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_marketing_trends", "rar_sha256": "49f33b9b8715eacbf0d8c2249a6d4cb6ab67a8cde93eb339046d8142b6b6b0e8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_marketing_trends`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_marketing_trends_agent.py` and in the RCI capsule.

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

Analyze marketing trends Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing marketing trend status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-marketing-trends
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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-marketing-trends-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_marketing_trends_agent.py` and embedded as the fenced Python below (sha256 49f33b9b8715eacb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_marketing_trends_agent.py` first:

```bash
python3 adaptive_card_analyze_marketing_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_marketing_trends_agent.py   # or on stdin
python3 adaptive_card_analyze_marketing_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze marketing trends Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing marketing trend status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-marketing-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_marketing_trends',
    "version": '3.0.2',
    "display_name": 'Analyze marketing trends Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing marketing trend status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
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
        "upstream_slug": 'adaptive-card-analyze-marketing-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-marketing-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1033dabe435e2c5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/analyze-marketing-trends'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-analyze-marketing-trends', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-marketing-trends-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical analyze marketing trends status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-analyze-marketing-trends-2026-05-24-card.json' that visualizes the current state of analyze marketing trends. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current analyze marketing trends KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing marketing trend status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON of marketing trend status from D365 USMF with 4 KPI tiles and 2 buttons.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-marketing-trends-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of marketing trend status pulled from the D365 ERP plugin, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAnalyzeMarketingTrends(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeMarketingTrends'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-marketing-trends-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAnalyzeMarketingTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
