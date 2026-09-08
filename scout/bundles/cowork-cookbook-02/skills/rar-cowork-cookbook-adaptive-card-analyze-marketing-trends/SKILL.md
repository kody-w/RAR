---
name: "rar-cowork-cookbook-adaptive-card-analyze-marketing-trends"
description: "Generates a read-only Adaptive Card JSON file visualizing marketing trend status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_marketing_trends", "rar_sha256": "49f33b9b8715eacbf0d8c2249a6d4cb6ab67a8cde93eb339046d8142b6b6b0e8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abPiSJblX2Fem01GNhEP0IJQtLXZgHahDQmBREZZpPZ9X5CUU/99XEBEZlRldVeNzZfhxQtAcr9+13OuP9dvb1bXhkX99vlN86x8wVhpGoVevbByd0EU96JOwFuR2OB34RR5W0d21xZ18/bxzfUap47KNipyMJ3xcq+2Wq9ZWIvas9xPRZ6Oi71rgQG9tyCs2l3wmiwt/Cj1Fn3UdFYaTVEeLDKrTrx2/tTWHli2aa22axZ+XWQLcsytLHKaBbxFF/T/1Ahx8SH1AitdeHkbteNC10T654+Le9SGixAs69UfF/AndHFUuEULVmo+An3UPbOoi/vHh1XQJ3hhObPWC2BKW+TNOzDGG6ysBMPfPv/yl49vEfj89vm3Nye1GnDp7ZsZsxX73ErHyRO/aX2elZ79kVp5AMaWI3BoDr6XXu0XdQYuuZ6/eH370Hip/3Hx7/+e3K06aH7+/CVfvF5f3uYftcsXbegt2sJqWs9dOFZp2VEKbH1f7NO7NTbAvW1X57OjGxCPPHh/zvxdUlEu/nO+9+G5yHvgtR++vBXlHCBg95e3nxdFDdaru/nz+yyl/PDze1rcvfrDz7/LaTo79px2Fga0fv/6+v4SCwb+PjTyF181hSJea9WeE5UeEP4H++bXU/WXuJdLvj4HfyjKj4s/lzzb859A32fG2UDun4sFPgAz397jIso/vNaoi97LrdzxPvz8j8Q6oeckadS0/5TcX56Cn8n24eUSkIJzCP6yWL5s+y7zHy9bgoT5VywBw78t991R/0j2I7J/IzqNclCd32L5p+L+bMLyPxe//EPb/qsJHxf+lzfSS0Hd1Jadep8Xvz1S5Jef3N8v/vSXvwLR/60Yrehq5yHha2blke817devv/zUPC7/9JdffupKkMWelX3t6vTPZP6ZXx/r/ODB16gPP84F6+t5khf3fPG9hha/FeX/qP/6vrgAGHN/v958XvyxEufXcjEb8W3Rpwv+UI0N0PUPfvz57a8Af3JgTfcAqRl+/u3fFmLk1EVT+O1Cc4quXYAAt1Hmzcqfw6hZgH8zatQe8GsTAce+xoH8nyM8a1z4i1//l/PA9E/OC9NX1gvZvjoA2r5aT2z7+h2Svz4gufn1fXEG0os6CiIwBACqonzJrQCA8LxyWXuNV/cAreyx9T6Bov40f1hE+eLXf26Brw9Z7+X46wOjoycGqgQ341/Tpd77bOk19PKXXQ4gK2/wnA4skxYO0Ml/oj1QpUgB4bSzV5okStOFGwGEAaQ1PmQDz32ehf3666+21YRf8idgw4snmzUrMOC7OotPn4BxfhoFYfsl95ywWPz0219/WvzvxX816yF8XkMB9PGKC9DwQX+gzroMDAMhA0EGIPKIy29/fbkYiAE8ugBRjPzIe04GeZp47jd/a+z+E4RuF7YH/Ax8nJVF/WDPqH1fcP7iu75g0fnWzBNh0bQL1yuBq73cGYFUC5jz3ZN50S4akIyNP35cdI33WPVXu7YeKmag4K3214VIKICVihT8N6v5GAQmF3kE3P89G57XgZD6p2Zx+CbifSHNmbkordoqw9p6reFbz7gANvo2HQi3Frl3/5LPJOzNrnqUydM9wdxlRM4rpJ8evYRTZAAT3Obb2sGrE3EX5weH1l/y5lUCVj2HwgGUABYNusidieE/XinVhEWXug//AU1nSa8ouK+oPHLwRf9/27U0C+3ZtvzY8XzpoPUGWfz/3Bw9jGYYlWL2Z4pcUNJZNZ/BmPvBOWjPFnJeEGTks/B+71q+IdM3gP6SpxHIrHr8j+fIh8WvMU/Q62rgcXWvPuSD/AHBmOU+0ntO17qeC8P6kn9jgtmKB+wBrQEWgFqZU/TbgvPdb5qGoODn7793BY90AN4HxoMUXpSdnYL08j3PtS0nAVrN4foWRpDr3lyu9zBywh+smj0OUgrIXwAlIlB0gC3ev6Pz8+431X+Y+Gx+5imPxrADFVo/BAA9vFnBOSxzBIF67bP9BnZ+fggBZmRlO9tugxoBlj4verVXdVETtXOAn371SoDIn+b3p6XzVW8oQVkAZ4HkLzvg3Ue5PJPOnTUCiAGqJ4tyQPXAKS8nPARa2Vz7AFtfvehT4uPyyyDvUWMzR32bOBsyz5lp/5nAVj7+ESLOf5YmQF42j3is+7eZ9n21WfYMkw2AOrDit7vP/uD9SfHPHmLxTe7nv9vffPjXtkAP0tZ/TIDPi7Bty+bzavUk2m88+w5AavXUtfnOuZ9mSvz0osRP3yv90xNQfpD+NPzz4l/T8AcRrwr5vNi8r9/X8y3hlWGvF3AI8elgfkLmu19y1fsdSMHyRQZSbA7fCEj+O+t9GwKoL6gB9IDBTxZsZvK8A75+wD6IxZf8jyk/lxxglTyYU7Qp/gAFD/oH6f8M3Xd2ArfyFqztzo1j4M1btkeBNN7b57xL049vAAu9f3arNtNQNid3M+/yQBmBZqyNvMe3J/x9fcLfV8AMeTtf/nG3yxZ3UCUgfX8Eyxl3otxJO1A/HwCW/jzr2Y7lrNhzrzZ3dw80Gv5Eqvz4YKXvC9IDyJc2f0zxFz3N9PyHSnz6EvjQATZ8XLgPkgHZD3w5mzdXsdWAsgAV8ae6JGX039r4nS5+MA8QyZ+b96Cgr08K+nup5ExWP7AUEFp1ACw+Lrz34P1BWn8q93vH/PdCr6BBmeW4xeeZqz++kBG8g13Ox8X3DQtw0GsL+djz5x3Ynf8yb5bmnHhMmT+AOeDt+6Tvf+qwvbe//JleD/j8OmfvMwf/VjtphkVAG3O8/hHnA+WBAm7neC83/HMg8QlaQ9tPa/QThDwGvscNaJX+3ntAzQcpAGqdLf7dlb8bVDy2grNBwAHt8y8Xv72BKgGatNarTl57CTAcYOinZu6bVgBPwILg+7Pywb3/y13GS0oTWqC/BWIQ3IdhG7d32Ab1LMf21+7OgSAEt7Yu4thby95i1s5xPRz2bBjG18jW3W0QyN6Cn7W3A/KeKPJ1bhGjWbNZrZf3vN9vg0vuy6SnCbO/vm9qHqDwtOy3N3uLzKWBNNz++SJW+MbewoI98sZy2vqFapWEmMhEHMMyCVcuk3bLQcoRvTTzSsvow9k78G0SUyIR7J1M1NILGpFDmGfaysGKwz7aF6Nxk9zs5jpFQnXJ0ldKvzeEOvVcLNA0IYbPSx0S651x0LdXs4ku6zQZmCSM8CPHo6xI5FA4cLnIrdjeX6FCT2v8mF3DmN9Hl+lolUm22yITtlvmtgQdU3PUu5ZI01rBDynZ1gQjG1fZKC/xZPPGsT6NoreSmdBTWHuNKoYZanVrjrQWlC4mnuFyi/sx4Ud66NiNw4zHcskdcJlF8pXXqxx9ibnzTlGWYBm1RH2EUAS4vC8pct+5fMbf6ORqMezu7inCiPp9LqD4zlNQUWFXE+Kvlb6P7rrGi8ldqAkwOJu0HL3cSqGoJCk66tllqjIeC68Ie7hd7X2P32WzhsWbjWK3vT+67fpEEjFZNMPlwNueCGcldzaz6t76PVHuZXG30Qzmnpqpd7woJzJCdbuIY3kPK6LdctulUdiOkatlIfnOasQpLhWD5HI5MFlC3iGlIScnzGv9OOpRaY7K3lVKIr0aKJdp1al27FxFLGvDovy6jxRrH0zFvt51FBI3+yUs91WL2AlMjnF5liiWrpCkoJYRUyIirVqjKiZhv98kemeaXSNS6PpOrqDtGJw1PC1sml5uyHRbuRqzgU6Xar27nG8uVtnrDHM5Er/mZ06nQ167qpcbUR1wzTqVtXVgB27kLxU71hQCs5y39CInaSUCixl+IFUkuW2olXsJTybUMNWOO2WUv1sb0TY07ds18yZqPdyrgy7Z1pp3qzvRCic44O0Wulg4VTKymx+6QbNpC3et5KYi1UhvOX2FFMeqnJwb75V9gvqVkWuru1FsxJRaUdpKTqQDtdO7tcLZdHy3rhhTKCl+XUpTo2XHSRzyBt3nYbb12K1tZ1dDn47qtCPShuPLIzH0Z6i65nRsWYMMZehSmJZMqzkicqexFYytcngnm/1UCY5yj+ObUq/DZQZ7ZIrUuClnGm/JLUwUSVjLGOsQqpLJUS/Wh0IbFX17wIZAJFGCFG3F7fd8L1pRyUmHNYbxze4onaVbkhC3ViaHNoQm1wqGLInUkjsNHn+6XuOIGPz9RvIa0jqpB70OEQqpGYRp95lykDqTqD2DjdBJ4MpmUsi4hnj/hAcXNsBWIlrdNlVZbm78iSj4nKqIa3Q9XJz8lBgswVOFwokYtvElLhvHa7c9WGgtRqdkQ11PGXYwMEm0BCuJLz7UwDlj7Dc9eqgDPM1P6Ibi9aGk0WB96+72uVHvV7WgDoxInBiCg1dnsYho3MqyK5sRB5250PpRlfuVeuLvan9sjydXueCkzWC8xuV1QEZEqnmk6snNQMYbKFsW2HqDglCs1mfryN4OhWr07ETcBVXcVSfzrsj+8UBUaEGsOyvquYKUkCPDUYrvLTmk8wTLUAsQ7ukO47ERGiFAC59VB8EM1spxQghB3lfLy43sEDm4Q85OZbBjOCmU2xF04R3VcJJxONrT1u3s0SlCtrw2oHbWtOqgHqlu7K/Vjl9PTbgkPa9zNiFf1SI5kQAv+L6F3XwMuLEr0kKUyZ17ObfmUPBb9aZi5/uhO3XnrEwSPEByXtotEWaDrRM7XaE7iCewkZMkhr/bdwxkE23KFwOBe9mz5OiCteJxHy/LzD0hNWWSKa6fOKX31BapUvOY5vzIldOOEwieuUXSRCyrnXRv0thWU5uXDxLDnb0VXAXQ7qzwjnE0M2dMytyiB0hcJpnEnynmaJ/HK1kpchhcVXdNK/yhJAMdEaObSm+3qz0XxS60jSHS0NRT3d3nbGXhDFWJC0HDraagbEhEVLBeK9lQ+Bx8GcdLDQXkdhNg6C1yWg0NWgQ+ocUw5HjpGvxu5eckkq/F9JJmR//EO32xLtZEn5RnV2j3pu5pyJBwV//iKTi7X2qY3YYHZuObkIzg3oHkS7+G7rq0UeC7KdftmGB3q4LzrES4lhD2DHQTVgHaGGJsHdf0tb/ERWNuyWh1II7mdt6l7PaGCNPMePY8QWyJeyXuDdbjeP9gT7pUQTRGgOafyiZ7pA4HrgnPR5bnTg7ATCZT5XxHdt2K1b2pZCcTwyVurY/IfuK22x3HX7SVeblIdAxR1xtioGLj9NxmKNTasHfng2Ujl2ntGDdW2lPD/s5YzgCzrdjV5ilyS7cJ1ZEbQm689kp67TMW1rkexZiyQKatwAoFR7FydCdMLe2XdmtwOHX2TmvxHJxXdCsdrECs1YyqueO+7PudHDp1UR+zfEVKJ3ts91x6b+315grR6vHIK7S1WwtJWUa0uGaEPUiIirFKl4/iZVVEqLCnTY1en09RFqPxDUI6d+TujVptOSKt9cy/70MHyZNhqRgjK9DHgRUAD8JxiDgcpSMjrIm44q2PhOxGaXbhdzBlnSJuvzybVStdxptnS4zdBG0b7XWPL0xo3BnwBfQnY0GrI0ALEXSCWJkX5UHBs2uRMSOn2/RuAKBIeXhan9esenEU1Nxdy1spTYUX781AjhwUL8ZpYzKxP9BbBrqixQXRiqW3BvWxTFRIoLe5rma1BOUDFxhLpcGnlETFUSsjBaK9+0ZOLhHH6fw2Yg/xDSlBsSO5yeWjejJh2FwmPunT5YEp2GVuIE1ZcXv3wtpiYZ0HfYsHkBS5oXE+Rmoft0qBw2unMQmyA2jFYDa9XlLEYKojfUl31RoPzlUQnxCy0tH98Rzi+GpKJkEhe0ePj0IawZIpYmf9ZCG+k1YHNZvU8XCWRKqgMH08cPkJLtZr/1LdolTwWlplEm5TRV1BpJcdIklwuLvTG+1EXq+yJNCEMPjc0YcyWKKibd0yIr+CU+00gpYQ4m5DvbrfvTA9Xc3EdqmzjEshm/POkht6BcYQlSaZ0c35W4hbsERuSC0Ixame/HwZuRvoTpYHiuIFosvupZLFu7sJFQqLsRcQ7uNhOdrNalj65ZVBeV2CCyPMGpS9qXCNSSmrOC05MmcsTCLQfpwx/gAn9uCwuJ7IXepjU35gs83EiKl5pip6c9qfMu1aUgPHrQWeQK10VzKHMhfq0zqnW528DvuIGqNzUNtQuTppoDWGcvOoevlpS3iiJnsUh3tn073rNnrarbERMoazAA1n2U5j0z5RsaSlpzBiwo2/q64yFaOnbqi46NgVI80Se0e2rGjgHQjlACnonXfDQKrWeWqvjpTV9sMAexPBOpsYgZrLGo2Z5CqCQK2gzragIjPdw/FU7SPGWnHmnbihLHzY1buEkrdFfNTJjHDvPbxe9TDW46HXrUJc2cIAsieFX0b28urVJNNtLLi74vq2wqyu1fDEIAVSwJgO0RAPZ85HwaOIFa2JSkDskqNAwtAxyQ5SKN774s6M1+Ptxq4ifG8fNlM1ulIligkqMHJ0bT1KWup3WjkSAs7SJJ32JRc26sEfy3V4xGIHH62zU3dUkebWxUxOV4FdsVhp0vrIh2pLHs+tVyz5sDbuoS4hRGx2eLKVxyW+vWMUU7WXMs7TYQI167jcOksNmsh0V/KU4MLH3dq0ysq1U4S5WWh78irCici4zDRhg95odIsNpXnORtQh0aO1sYhxOheuMHXdtXDcEzvFXtZwVXtnEdQ09dQ/nq60KE0GizEJD2EiLUQcZRcH06H8yqOEo635VXSQM8diLtcltRf3Y7NZBpv4cCmyy3GpBbRTw3ZTA1p0ZPbIn8/2xm1F/qLvW0tHufCs3fmuCSRBcfdrH+0QZensOsGQEp27WYBfGmyMUctIbqgp+pjqrhgYWhPWTo9MId4XKLrJe49JVraMjjV23SiI7gfR6QKZZJBV65CW6tN1s7/XOr1xOSlJ2aG/licWrqT0Xi09PTy5HLOVddjqb/a06fpoI8hceWsOgy3VmngHBR8NHIsRd8DXxBTq18iPJgmXmbufbO6ASzYOvtbZHquyHUcNBtFf91fKFusKqfWdgpimI5s2pN2g6GwIkOBIMaRfr1FfHw63xJYMi/JqF4HNS013ar7tTbLJVz6p9o7kS0JfmD3TyTrOOvw6gPW6Fa6pp2JUo9a7TAouZoXlurxNw/Nq2JZsvV4VJ4nDMl4Ye2S/JYWQK33VWdp7B6qHVN95EFbcI2csatDBF9dLej7ELN7cEEi8HbaDVF51quHX1GWsjxg1CAJ0NPScgSV8zDb3O8fUqyXrMdMRNZecRVFNut6GUqX0ubzfpkeLWa/2eBWgFddGx37DGZbTuZUNdbiiHfors7bvFaK1q0k5gL7edHkD9L8c5A0K4hc4i+6UFG5sLVlfg1jCG/budlsmgOT5CO6KbKltvp34M1718tITprNyala2oBputt0Qg4ixQx13ijYl22XstQ46bRXXgF1ptJrCwkeAY1qiXow2jGtGpBHXCTX3kjQ02JDVLj4Z4X7ZeR1ndIh1sy7GfTooxglLPddQhZOH5LpfcKsRHgPygFFF7irqeFVXJ04aCeHibdTOjI7FZMricltTPabV68YIT8pqN3I5YWy8xuvhPdsPlI+11ojFZWAu7Q2bqEfysJRWqrm92kOx3w0IcqgPqxVmKCuGzAlYBoDfbjYr+nyXBUMNB8yFJw3N+vNJPh9BM3ncbi21ROzoLrAIMipKG3VKjhOputnmN+sueIG3Rq5TohmduQo4XvQTrERgPMl86Bo7WXUz3M7enUQD0koVl5fBzt7rt2xdYf45l5ndMEDEmcEOPcN2y1WyUR3odut5DOnqJt03YbSZwiWOgYaqRmsqMW4DefNDy3WlMBy2bCmujU7nduaKhixeWVaIatvdHs4Ej1YdyVsN5oYstulhbGtU0lb2tG3c/n7TTVjQrRNJRarCxkh79rux2co2EvHisWtbFQ0H9wSayGy4zX/qSkuP3deXuGp1sKuRmLYbOLzHGqvdBZC+E/v9WYb7TnBOMJJNKWEwNGszGn3MuSQNxDgZVirk+fotqSk5uN1X53WrLbsjnW5cQcfjq1+d2FymKF+mySg/2BoPTw4U8/B9pSF1dFVs+XSW80iNURuKwSZG9foJ3rVbfLlycRhzfEJaGlnaJFm20yBhzZ/zI85m/Ga5XJrBKnHZ8ObqELvM7uhFtS8d1+VMDqfKKa63SNfleKElhd1MgF+M4iZNELsfZJy3Bb5krpcdIyehtRvIbONgOHyA3MFiULItxu5aS8xknc/60VnrlzwQOj3I/TiuiS1RD5jYVrdO4WXAoMele6iMrG38VUCh9SS3ErvEjldvTUayZcs7egcvRyFoVdMKh4Aq7zh9G3GyTqdNZgTUKdXatWHEHkRSTaBM6mpiL6MVZGKIKHbO6KcNg586GBvVy94t9BraS6IHL29E2KwyyVrCcdWX06WXpTVSYxV6BBt787bzz91mxFrG5URYzBDJRqUBLdem1uIwuqsCfGInanlBbWx1pY+AvtorD5ub9lSgRJdDbQexduEYG9lZ5tfmdhCWh01IVPfDeSPHeLsGfYSHbraFTFmSvBnK/I5W8jHv5FDzJAJfuke8ZHfbuNo1eX5YJdV+mxEX/qriJ6000rhX26GiuOnoZyUD221GC8tdL+556GDCw1KzKaRax8u7cjoHABXul3sfxJnOs/lleREl7cZtNhFCixfGcaoaUlScN3dIEiPOeIewaNjp13GrXTUjG9Qeh4jbdaNCJZpc+F7u8aju7F44sHVxWEuAHrnW3kc06D4J7Lg6kKzLeTG5FlXY0rtBJRDHhf1tce+HS3tFaR9VT14uaC5sGbcbXnpkKnS1aoSr6ExoPVt1WWpbjoX2gqK1xebSOphPbT09bagtDpNiYmxQm7Hakw6dGXOF0YkpY/31JnVeWYLySMVpQ9fXNLLj47Qy2WaMRCbmAIohkNPiEFI2vmaU2ODxnI8m+217HrODtivvxe6YFZS+bZjGguxrapYK4fckmUnc0sl2dXTJr/hmamUMN07KGI+xgkZgY7F24GWdcr7frc9Ds5I9/epeDDniRm07qtoBp8g+olKdjXlZgFYWiBVOhQd/HTLp+tzvj5cGv92GhoGydbuZmqEzMixVzmwulMYBWUnbzsN4CNkIUCOP8hhD9AXu40yqQuHomh7DJBpdbQWw0cR01IdSaKtaFxpj0QDsUmBLvm6wLe3E/gFbB9oVDRiiFFFmA+dC07i2hSl5d7gOE1uQAUPCCncK9OgOx5QKDG/twdyDPe/GY2muzRIYW47hmohjc+SWRFffpRtqT3XZbUD/OqBH+VZ0IZbSO7aKvaYRjIt7gqkNjoJYwMHqdrmtRAIe4a2FAyYTIWO1rDuhPd/6yQjwGGLh4Kog3c3dS5IEErbulqdd4R0LO62Eajpj9TBul9tOdG11RcZ4jU61ZLUm75Mr87ocDCy2Osw1LqQiHndWW16FdjcRl6hf9e5JrbM4igQ47GlXykQB09B+O6YQzO9ycZ+nB53fV4cOdUXkbO8vlEifjdMZdYySL+8uLHSV5UnukZjSgVW8zAeQ1oaKpkbFtmPbk1LylFRJk4ClsedSh97HGPvQh3gPYavmsm3aQ+yzitJJYotVF1Q5xs5JTovY9bB0R0ucL3aE4CGJzruDcIoLAmLDoie77tbtfM8I9B3pBJ6M9Cd2lPaGfQFbTo/QhxwfZLsmJ/M6GHea7t1bvMWE+O7vCJSLNkfaJfb7/X++fXz7/Ujs7V98DGw+m/l/dgz0PM359sTH48TPs9zPj7U+/6uK/eXjW+1EQK3nsVeTdsHr6OhvDr0+/XMneLOM8fmU1bdj4ed5dmsF89PIb1Hudk1bj1+bIn08+wFm2F0zP7vYzI+3OuD9j8eXPxj09jhtdryy/doWL6ve5ucL5wc7PDeyWu/1NXgdCH58c1+PFX2Ft+hXry5nk18PDwBL4ff1O/T21/8D613grjkuAAA= -->
