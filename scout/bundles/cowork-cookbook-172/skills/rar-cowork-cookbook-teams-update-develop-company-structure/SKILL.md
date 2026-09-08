---
name: "rar-cowork-cookbook-teams-update-develop-company-structure"
description: "Summarizes company structure status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyt"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_company_structure", "rar_sha256": "6361e4530f248a29700279d8971b87d1d3243a1d579f4470db87354927dfb3fc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_company_structure`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_company_structure_agent.py` and in the RCI capsule.

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

Develop company structure Teams Channel Update — Summarizes company structure status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyt

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-company-structure
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-develop-company-structure-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_company_structure_agent.py` and embedded as the fenced Python below (sha256 6361e4530f248a29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_company_structure_agent.py` first:

```bash
python3 teams_update_develop_company_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_company_structure_agent.py   # or on stdin
python3 teams_update_develop_company_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop company structure Teams Channel Update — Summarizes company structure status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyt

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-company-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_company_structure',
    "version": '3.0.3',
    "display_name": 'Develop company structure Teams Channel Update',
    "description": 'Summarizes company structure status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyt',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-company-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-company-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5f96729afad0b002',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-company-structure'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-develop-company-structure', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-company-structure-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop company structure. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-company-structure-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop company structure, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes company structure status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyt', 'example_request': "Draft a Teams update on develop company structure for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-company-structure-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update plus Adaptive Card on develop-company-structure status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopCompanyStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopCompanyStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-company-structure-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDevelopCompanyStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
