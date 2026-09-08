---
name: "rar-cowork-cookbook-adaptive-card-develop-frontline-team"
description: "Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_frontline_team", "rar_sha256": "e2922b37983ad758fc4d30d0b1e7f3e9c4362b53779d1c09a25184180a0ed3c4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
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
      "description": "D365 F&SCM legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename, e.g. 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 e2922b37983ad758…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_frontline_team_agent.py` first:

```bash
python3 adaptive_card_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_frontline_team_agent.py   # or on stdin
python3 adaptive_card_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_frontline_team',
    "version": '3.0.2',
    "display_name": 'Develop frontline team Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c53e5fd3aacb89bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.', 'snapshot_date': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop frontline team status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-frontline-team-2026-05-24-card.json' that visualizes the current state of develop frontline team. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop frontline team KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON of develop frontline team status from D365 USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of develop frontline team status pulled from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopFrontlineTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFrontlineTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
