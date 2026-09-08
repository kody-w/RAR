---
name: "rar-cowork-cookbook-teams-update-develop-company-structure"
description: "Summarizes company structure status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyt"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_company_structure", "rar_sha256": "6361e4530f248a29700279d8971b87d1d3243a1d579f4470db87354927dfb3fc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
