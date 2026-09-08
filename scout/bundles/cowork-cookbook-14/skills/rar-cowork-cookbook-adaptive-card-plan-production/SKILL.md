---
name: "rar-cowork-cookbook-adaptive-card-plan-production"
description: "Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_production", "rar_sha256": "626759fefe2206be38f46f9de75ea5f6b78f211dc1359e2e17488b901942f417", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_production`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_production_agent.py` and in the RCI capsule.

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

Plan production Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
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
      "description": "Date the snapshot represents, used in the card timestamp and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_production_agent.py` and embedded as the fenced Python below (sha256 626759fefe2206be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_production_agent.py` first:

```bash
python3 adaptive_card_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_production_agent.py   # or on stdin
python3 adaptive_card_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_production',
    "version": '3.0.2',
    "display_name": 'Plan production Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ecd839853f4c020',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the snapshot represents, used in the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical plan production status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-plan-production-2026-05-24-card.json' that visualizes the current state of plan production. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current plan production KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing plan production status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a plan production status snapshot as an Adaptive Card to embed in Teams, Outlook, or a dashboard, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPlanProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abOjSJblX9G8NpvMbCJC7IgYa7MBJLHvICFVlEWyg1jFIgly6r+PI72IyKzKqu42my+jWJ4A9+t3Pef6c35788cha7q3z2927Ncr3i/LPIu7lV9HK665N10BfjRFAP6twqYeujwYh6br3z68RXEfdnk75E0NpvNxHXf+EPcrf9XFfvSxqctpxUQ+GHCLV5zfRSvJ1rVVkpfxqh+ryu/yOa/TVTh2XVwPq7YECrRdE43hInPVD/4w9quka6rVdqr9Kg/7FUYSq/3/tDl1lTRAy1UKhNerMk79cgWE5MP0YXXPh2wlG+JqAEv1H8Aoi+FXXXP/8DTLf4kHdgxN3X8ClsQPv2rB0LfPf/nrh7ccfH/7/NtbWPo9uPX2zYbFBAPoaHxXEUwF1ykY007Ai8t1G3dAsQrciuJk9X71cx+XyYfVv/97cfe7tP/l85d69f758rb8scZ6NWTxamj8foijVei3fpCXwJpPK6a8+1MPfDqMXb14twdBqNNPr5k/JDXt6j+WZz+/FvmUxsPPX96adokK0PXL2y8r4LEvb924fP+0SGl//uVT2dzj7udffsjpx+ASh8MiDGj96ev79btYMPDH0DxZfbWNHfe+VheHeRsD4b+zb/m8VH8X9+6Sr6/BPzfth9WfS17s+Q+g7yvNAiD3z8UCH4CZb58uTV7//L5G14Cs8Osw/vmXfyY2zOKwKPN++C/J/ctLcAYSG3jr3SW/fHiG768r6N227zL/+bJLkv93LAHDvy333VH/TPYzsn8nusxrUJLfYvmn4v5sAvQfq7/8U9v+1YQPq+TL2zYuQb10flDGn1e/PVPkLz9FP27+9Ne/AdH/qRi7GbvwKeFr5dd5EvfD169/+al/3v7pr3/5aWxBFsd+9XXsyj+T+Wd+fa7zBw++j/r5j3PB+m5d1M29Xn2vodVvTfs/ur99Wh38Mo9+3O8/r35ficsHWi1GfFv05YLfVWMPdP2dH395+xvAnRpY8wKWBXb+7d9Wah52Td8kw8oOm3FYgQAPeRUvyjtZ3q/A3wU1uhj4tc+BY9/HgfxfIrxo3CSrX/93+ATyj+E7kK/9d0T7GgJIeybF1x+4++unlQOENl2e5jVAVYsxjC+1ny4QDRZsu7iPuxsAqWAa4o+glj8uX1Z5vfr1X8r9+hTxqZ1+faJw/kI8ixMXtOvHMv602HXMAJy/rAgBHcSPOByB9LIJgSrJC8+BBk0JOGVYfNAXeVmuohzgCeCl6Skb+OnzIuzXX38N/D77Ur/gGVu9CKtfgwHf1Vl9/AhsSso8zYYvdRxmzeqn3/720+r/rP7VrKfwZQ0DkMR7FICGT4YDVTVWYBgIEAgpgIxnFH7727tngRhAlSsQszzJ49dkkJVFHH1zsy0wH1GCXAUxcC9wbdU23bBQZT58WonJ6ru+YNHl0cIKWdMPqyhu4zqK63ACUn1gzndP1s2w6kHq9QkgyLGPn6v+GnT+U8UKlLc//LpSOQNwUFOC/xY1n4PA5KbOgfu/J8HrPhDS/dSv2G8iPq20JQ9Xrd/5bdb572sk/isuC1u/TwfC/VUd37/UC9XGi6ueRfFyT7o0Enn4HtKPz3YhbEC7UEf9t7XT92YjWjlPxuy+1P17wvvdEooQEABYNB3zaKGB//WeUn3WjGX09B/QdJH0HoXoPSrPHDT+rhGxX43IH3uZLyMKI/jq/9u2ZzGU4XlrxzPObrvaaY51egVgafMWxV6dIRD9XPNZbD/6km/Y8w2Cv9RlDrKpm/7Xa+TT3PcxL1gbO+Bli7Ge8kHOgAAscp8pvaRo1y3F4H+pv2H9YsET2IDWoP5BfSxp+W3B5ek3TTNQ5Mv1D95/pgBwPTAcpO2qHYMSpFQSx1HghwXQaonVtxiC/I6XEr1neZj9warFtyCNgPwVUCIHhQb44NN3/H09/ab6Hya+2ptlyrP1G0FVdk8BQI94UXAJyRIxoN7w6qqBnZ+fQoAZVTsstgegLoClr5txF1/HvM+HJbgvv8YtAN+Py8+Xpcvd+NGCUgDOAgnfjsC7zxJZMq4CzQvQAaAEqJgqrwGZA6e8O+Ep0K+Wegd4+t5tviQ+b78bFD/ramGhbxMXQ5Y5C7G/stavp9/DgvNnaQLkVcuI57p/n2nfV1tkL9DYA3gDK357+uoAPr1I/NUlrL7J/fwP25af/3s7myctu39MgM+rbBja/vN6/aLSb0z6CQDT+qVr/51VPy7s93Ep648/yvoPQl/2fl799xT7g4j3wvi8Qj7Bn+DlkfKeWO8f4AfuI3v6iC9Pv9RW/AMzwfJNBTJridoEaPw7wX0bAlgu7QC2gMEvwusXnrwDan4iPAjBl/r3mb5UGiCQOl0ys29+hwBPpgdZ/4rYdyICj+oBrB0tHWEaL3uwZ1308dvneizLD28A9+L/bO+1ME215HK/bNeAr0F3NeTx8+qFdl/f0W6588ft6pKU6Efs71BxARgQOKBp8438umjRbpjaRZ3X1mtp1vz+a5N8jYCL/lH2Ftx95WkNOpusedL00jYBRz7J93v3s4h/FhMA/epZw0+3Lcb/6apPwHsM/7ik/vzil59W2xiAa9n/voreWW9h/d8V+ytuIF4h8NuHVfQkMVBgQIHFpQtQ+D2oPFB0f6pL0eZfAanWf6KN0NwB2AAU+M5Gi2PzOixHgEA/Yx+JX/5U5JPPvr747E/c+oMEf098i+jrCFDpwyr+lH5auba6/1Pp35vvfxR9BN3PIidqPi+NwId3CP7wJOcPq+97H+Cm993o89cG9Qg2+n9Z9l1LNj6nLF/AHPDj+6TvvyoJ4re//pleT5z++i3w/6idtuAv4Kclav+ss1gS91kb8bsb/iUafURhlPwIEx9R/Pn806UH7dc/Og1o9yQdQN2LoT88+MOO5rmZXOwAawyv33389gbKEigw+O+F+b4bAcMBRn/sl15sDYALLAiuXxADnv339invk/vMB60ymE2iJEXQCejsUBQmgxjbJDiZ0FFMEbFPJGRAbRIUQaIQwQg6RmOEwjebgIYRGkcTHKGAvBdKfV26zXxRiKCpBKbp5TEKR1GcoHgUbcgNGRIUCvt04BMBQfvBj6lFXkfvVr6sWlz4fcv0BKaXsb+9BSS+lArei8zrw61pJCAxJZgkD5rJpLH8llMLnbtcMP08lriPzhJdN9hQHm2JLNrMPG5NCewsGfPuq8zUINJByCWj4pIzRczjo4FTyesn2z6No2tymB8Z9WbAlAGZBD6672+jNBkirIhqbmfaw02y/TW0Z1iFZFJWXQnD47xb04S/zkv3UVBZZHOHdQGnUO1byk0fDYiGlOhI8fIJjBgjjIwTp5b3ldKoj7myzJycppLey52hoTKMYHlAakzuxuvYfsTrm5ITInJqnep4bDRcrGSCrlRWLPlHhV+6q5aL63mgFLPpW/t0ihKqL8OL42MP1Rz33aYfJ1mTduPJYHskvs0ltIlvAfTwS3yTBDTkxWOsQJZY5E46XKYJlR0i36ryww9ssWbm9aPca+qccP19VB9uekBuLMbDs4FsaNg0CAX1RStnLucjsVUFXT8bmLjJ1cn19zKCe6I017tTee+No+Nzh4MZPdalUuSXUYVHVenFK3psqPg44+hNu5nRrrHENWeb8E43zXE+0czWmFA3ZI9ieQ4ucDrd7hbf5ph9aMXiSO6GOJC1HKYLdZq9aHfEOfaqcjfybuYxDFEwtOlnEmmP21qWdqi5OTb5lNuu7m4EjpBOInw06/QMubFpReJOm9uChzS6Yo8ISVqhNVzTZCpnyN2drjJQ+9jiUzURmLvutCNpC5tSrdK7xNl9n8uT4NJkdeM6eeqsjW1MspuFE+ZaShaGHHVGFWifdRj+yEMTjiW+tIz5cCp4rWObG7eTMmGtaURi9hqAGnLabej5yppqELhS5MPcoJxAsiY9Wh6RXcvrDWTJuYvKSPwIyvOZELk9JdoU3lCsS0BicXOpWV4/5I4IcAU+ebuOgrnbY8/f81gWfKHQqjuuaeHFFWaUCngClZy9VPkzemKd+6wa20gcZkO7Sh3xAADei/u7fcOpLkGB+41bZOPQhYQrNla34Xrf0bhAMTwNBfdZWouq6lwD40YM0OUcb0OqQH3WseGxOGaFI6NgD+hc0/RCSdwc380ZgW4hxAjsqF6i6zoMmMi7831vX8VEU1Ff4LoTpFY+tefKrQPV1JmTfNhjdZAFysnhrqTDwPluV/pQZjLxXb8xGxLiY4kg5eq+H+6lwLJZkM/i0YGQAj175wpVdjMcb9g0k24ZTTetOw2HvNVi2ZQus5Mh5+ZUDSUP9E13voPDW9wQcfesb2j7dl9XB0wvy2ucQZSuMfVpjZZSC6qzvmJnCPc3h3O50ZvJ7E+OSznk4XEN3DTrB5tJ5IM4ujtohxmaRlktcbJJc4dKdyMtkbjo9hq5z487b5ZVkfeoxESt6nHgxEk0xJtU1CnsZd2OwemovV31QYvP7sWgTShzzBsn2zcBw6HgrG5UUz8Zs9YmUrFp9+gop70o6Qw9WcxO3tbzJSpGSi87UmJ0wrpkN4Kr98fHZLmJo2+ne5pDB2Fi7JBrN/ldiNY3i+UpLJNgW6l8MXB5kJG7C6z7CIHqe9JyoP1+Ygd2va9Gf7rosnkqq5NF3jjtSAlCeqsGUFEmCUIUrhOCPIaIvoZjbiMPPut3l0sooAl9rdS1YRuKIfusRXKYHtbyA9Eeo38mrDWPR1AQcTSukNjQahDHm0FP5JrKtP4hD4NbbUS8eCj5ZJttBduvikHeRdtgOpj4th5NstAuOuedpzDXk4Sz77lVdRfice1jt/elR3ue9heBvlhFinUz1KHdZj46RJEm8lk8TiV3PvOePbubRkL2akvo5oGvNawTq2qXF9GaxblyLvRcvDlBwxThucLs+I7nttoecBbixgcEI3LjJ/eI8IKRoe53seHzDEf3CsaT49He+xMToj2oGd0pU0Eta56s94Ks3m40SaheMNHxTnUKtRgfDrqVSmRX8o23ll3MpixyL6Squg7lBE2Ekb53x2gY7+nsy8VOoNv7zGEzRXb0Bko6h9Tryx3Wrocqtty7ep+Nx6E3TeaRlp0oRNOG5tWSc8cLYjfylKUnXdsIWJszaHStWZKq8BybfGU+l+lxb4obPCC2Ci67FujvmTi9mnUmieTMMrtQUNwpm2xW2DU3CLa1OmF0D1HFZr75WrVpVXUqJL00N0oVSlxbFdU2uhhjTVInAbVdr0BNZqLMrdw/HjZ1Yad+F6jXYLPenAr9Rt9ygpkzxiz2RzK/yie6s2aHY+JBGYqdrvI7MbRpopHx0jxm2bFpQ8x8YMYxaMwRj9Jd3ZD7iA0FJGEo1wxFa2el83oX0ftTqrbmEXaYze0Mb3r5EmL04agaNHsIhd3OZf0jcvA2hwOkpocC0ASIh34y/bs2YqNB2I1JXq6VzPY9ub8fTTkoBGQirk7hMdF+vX/c1oxEuMfd48yiFnnSzbE42/ia7SQZ7PdPF1pNCzTLiN5wj+F0FU98/Ni7p7MlVyd0TVRSfmcbtnYs2pfbgNxgfni/s+Z6zzQnuwGRRIQjPRIWZCZ1VtTciT5SqKOUIWNQB0S88hPjBjvS7WJvD9G2nzdxdcV5x9xc23MrO3V0YU6pnocE1HCOnWCXEDhH6/vZvD1qFqebKdxCdmVyTHs7ydwjkfqjgmgMdeo31trjSgX0OGk9c03JjZYcZxvR5hNELCnYhbgoz+Fsz16O44MW1/yo2JzsrGn+tm7PqMgkp4t2PWoP2JfGzH3sPA/ERakrsoexHXo7T4/Uua8NOjhHG3c6jSzH1Rxyp8i5utIpgjbQ2TUlGeu9c05oinWnsX0BpWd1xJXU8f2J67ddlZkyIJljJnvntDjVZmWeWdBbcHW+kSy1GAKk6UX4zvVuVDIuOgdpgcWCw3iHvaqtrZmoN26/o4ysae+ufzM3/sYZ4gNN42a4G+bWD+ljfA91s4EV9coBlhnC6tTNRcnnG327cfgLf488yWcHDdOzA3MwWx1RZr/Wy82BcddqGnO7Mjs6inuZLahVA1O4kCXi+NUtvfUVZWwSZ9BTTJKzikwpGK8BGet0ck5E+DHBnng2Rt28Nv0UEaLqXlwpBgRu+iS7Nvh4Bx085pS7GYs2nt2djqfC49OtPSZKantuE/HJHGJQe29KIVJxN6ZO3YaABNj1w12r4D4na9NjNnwpdLtzH3led819FZ902zv0D9M2SB3mIJIldoI15yfufnpg/r28P+5ZdlJ7Ws5Oku7cHM0sxJ2HCfvATEZIcgnK07KMOcoHHk4F59DR4mHnKTyjyH4usUpQpQKtC1WetdGta+12u49B/SuFDrmcvUYNqEAu3PqMRO6DchA57bIdfBlITYA3RFGGDtGn02W8Yb509getuBSNI0YoIlMkHRuafSUEhKQLeodXWCYkd3/oto2PM+Rp57B8IQo9nLbpJjEAz9IqCEmo3yAHqXMO30f67REwVohUw+xnHhpwyOGYUNYFvlWbx/Ho0rOdEpI72scmjUcF9m6pGJnqHietZkfunNJPGeVwbss0Rk4q03ueuvUZuAkopznjPHqPp6RvZskJ1wepup3E/UkPKDTCGzhBMEwitGnErekY+Gh34+DCgKS56rZqt79rXD5zcyJL+4Dfw8oo2Bx11XccEXNYyzIVcrgOakgnIQ2hQXQuHg+tyztun95P1Fq4b4W4wel5byNCQPT3Ch/SiKf7/QhfduGBAoR5aTweKh0bgRXZblWI2nEVXjH7OdlUm+i8qeYSz0cW3xGHUCao03CPzU2rjPagtujVpWy91C06I2nPtESH2TqMZBSJ5vQ5TNlFhIc70ygCu1NAz5he0etVRBxWw6u9HNv4bn0csZM4VREOwOOKTqDdjM8OP6cgDygxu9kPVCVbykS8ULNGC9lhnaRMj+lckvLInm8obx805QzlhiFv16M03u8b0k3Oe3HkgRFTHIWgqUYrJCbqyaPC6JZGja+nvF3p05Y/NiYmsViw44YoEyS1LtxQv7b6FtWksU1c6gw4B1bh+VydOw3ZGDzayTvlsmVPgn2AA3F/jnfu3uLxoyDeTU5UTdgajn7X4qiAVBf2cuVu1+tlt1kLBZalZY8f5AfN5FQrBWt+DV3Zhyp2eF2b1MRJsHiAL9fNeD/xByyaTvZePlBqRHrISCheNmQeO4bBsLuRlORoKNi7TYiSpMZ0Z31l686uQUJKe3Mqq0XS8iBQnjE7TIcHhxk5jByA3OQi9PRl6LJoazJaJFC7+QoRrE84RLsNDcZROtM48noZdhtBVbmrpZwsKjcIS2Hrg1UZUX4RjyykhP5pp1uKrZbiHGWcD1F7iZiLoaKT9sbsjmzPrk344RGJRFk790a3EV843Q3s5Sn+atfnIbkLrGtoDgsPm/01y6ztGdPq0m6FyDY4QPHhY7MH6D2eDnuYC2FmIAtdc7o1IGFDwi5nvkExK9gX6hZTEYF9XE/0BFfZjOqKmutotabah6I1tKrQ/W1Po+fuYEhz7/AjhG+U7NamDXsVzPOBIivPlONZPt7cKp6MZm8diAZQHtS3Rr2BD1qGZiOx7gUdIQc92ekSVV7BjlpBkAS62kMTB+fWox7mJTGpyOGMdbPRptnSvImUjbVFNgeTe6gEZqaaXBl1zGLX3X7gUTMPWG3XTnDDKxCcRoqAlzixhiGNKmE9wMYNfH6cM+w+eqcKJ9egAQtCJJLck5FdKQV0t7J25IdEYAalW9NDvMaZ+HA8T9Ytvt4MfEzYmxyceNdH94mXdMTxYmaMGA9yWMNY2D9OJS/qBEnB5pkONlzkrnHB8b2ug29q651OgR+LY9bQTFhMEHXJLuXaPl9Cf/CjvTwT8+16yBKElm4sgQrdmas41J+VjUakoLWee/uU9AaDr++jHR61oGqx5nbJy/Re5Ah/WAeJ43lJie6KcH7E2Ia142gYimm3rUW3vhxOxA6/VrhnWBJGOX50Xjugs6Lwq5Q5BCTbRUIVVwNpSBtkPgLR23NokJoi5prIXi1RuMwbJCuxs58I2sbaxdr2eGyg+6nqksKfT+o0RPwE3+jmeH0gxYEXrttHHcCTcYZork1OViVsjcduJnCKW/OHcX8nzOGRWuS9sO3Ollh/y9CGQXImpgiqxFyQS7UnYBJvArspNMzNEuW4vTJCoptwwu+32cyCad4cohcJu0uOOeSuEaBmoteDVRHnh6VWrWgkiAPFW/aOxyMJNQar35Rc6ondAVJgoXfqXUMZoX0dRjNjMZUyuIlse+D1ByaznTaiVcd7c2cwly7ESbCPSaemCQaltxgsPe9nWGAeRiSdFanljxFyQYvR2ty3FRLi+Jwc80dAEtuhmcZjrfHz2fF2cgiHic4IxpYd17xw3CN777LeK+kcxmBvKMURdMhGr6p6o8S3IUzU6DWFPL+pNIYM0Xz2mmthPKLBPrPZVWB2s7BH0a2CkOjRqPYN1+iy3M2GwV+qHUuI65FGK/fCNTm+FtJtAQCd9jpJshNHqcoDlbNGyMFgX5mixiUejOCAYgXSeaVCQukmppBjpD+2Bg0l6OiFjTnoOwfsPSoS3+AFMwRrXBfZ26h3FzSPQ6LzEG/AoF0dJbHjY5N5RDRBjygbbAlxiGK2thcUppLcq7UIT6wWs+21nyNyE9DknuzQIlbBZqKrBUKI2EsQrhnaPzx4CrknBpEJqNsj9WNdBOY5TwlHmwTQWQJwiSZ9FEz7AreQ7yYxxIfHtVcSKSs/uqowptks92gLtkPFDr9hJrwPFZwhSs4i4LVc8Y1axGR7FTrqkh9j66i0dVLszISrUf4R2qDQUMVRz/soQORNF+4mhMz6bRkO0g34Iu+qw82Lha5h3f06rMWeYnIe2XIcxa/ZLRaF8UWDDQu7umNy5vAwRBL49Lg9tOFI7BMiM+OLYmuY753PdBtvS6XqrHOWeHneegCEKXvQdC3EyqxFN+e+Ayn+4PLyHGx5w3zM5/1Gr5CyczWteIw6lJ35rY6h1ezVV/ZAo5Kn0yaKtGJFTdO6Y3jxYJnTSYBpmqcGAMKGurWP0O3IzK3y0Jjy0MRFo8yepuwttMFcPOR7Hw2OQ+PWrYZl7cy7XurE4Qy8G5LEeo7irhHOLtVeqLrheU4PaG8qhBs2pWy/lmO3OsK1YHFnaTiLrRHmLPYAlcY+5lrA1mWiC1AhZgYhXnKCw5qtfI7BjpBfB7PvkhKGCSXSEzNtH+yjd4fk1u/qIY4FS0riB7bdHKG2u11D9xG5ymlWtPtdLWyNFCTQkGG6R4BCPnmIeDmtVb72jGNGUG7/oB/G5pLbj+xYpapUzbB3HJFhdohb13NHAuFFY9w5W1FJQitnnE5gJXaDb+mR2aawjLE5hk5O0BMwHBkNfjea9YW5hoYXyziggTZSSCaxL1dfOflXa70nGqETuAs0NhdCT3RQ65f4SF6vc+x6j+0NRYLSCIlwWKtK2F/HR8JjW8oqgluaRo/NTDK+7Rtjd4jC9mCGBxPpwoNW3RBhO2D0/QRdegHXDfRW6z1yRdJ8I4z3nmyP1OU40LqTbG87ZROw3VHKNnMe5bekO3pZW2xhX8HmixWlo65Eo39LxnoSsk29EapGcncMIiMb/hpKYyrmsXyVxW2kd1AN4xqx9yzjdqyKTMKpC9Y6hqWxqDm0omUmIC6NUPRZFel4GU3pDb0aHkZkg4jM0Q0ako4LFSM0MRq/U1gsxVUTb6dsL7PouME6WAXttApN2xDP8/21yVoLZiPgeQ/CPG0dK7cbMHobppEudo4Hl1uPciTZ2G2a2YFOtGAVSW+d6JCzFI93IfSKb4Q1s9kaxGFOzJRh3j68/Thce/uvvaS2HOn8PztZeh0CfXs35XlkGPvR5+dan/+L+vz1w1sX5kCb17lZX47p+0HT352affyXJ3/L1On1xte3s+TXgfvgp8v7z295HY390E1f+6Yc32cEY7+8NdkvioXg5+9PO/+g/uLppotDvx++Ds3X95PQvF7eN4mjfDktf12m7+eIH96i91ecvmIk8TXu2sXQ95cbgH3YJ/gT+va3/wumSstIpy4AAA== -->
