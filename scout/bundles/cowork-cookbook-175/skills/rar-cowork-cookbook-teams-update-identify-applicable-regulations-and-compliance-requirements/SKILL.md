---
name: "rar-cowork-cookbook-teams-update-identify-applicable-regulations-and-compliance-requirements"
description: "Summarizes the current state of applicable regulations and compliance requirements from Dynamics 365 F&SCM for a legal entity, returning a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "071629b476a8ef4ef38541922ce4463cc35910337f1c3faf57bb15e902b9cf9f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` and in the RCI capsule.

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

Identify applicable regulations and compliance requirements Teams Channel Update — Summarizes the current state of applicable regulations and compliance requirements from Dynamics 365 F&SCM for a legal entity, returning a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-applicable-regulations-and-compliance-requirements
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
      "description": "Date the update reflects, used in the card filename.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` and embedded as the fenced Python below (sha256 071629b476a8ef4e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` first:

```bash
python3 teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py   # or on stdin
python3 teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify applicable regulations and compliance requirements Teams Channel Update — Summarizes the current state of applicable regulations and compliance requirements from Dynamics 365 F&SCM for a legal entity, returning a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-applicable-regulations-and-compliance-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements',
    "version": '3.0.3',
    "display_name": 'Identify applicable regulations and compliance requirements Teams Channel Update',
    "description": 'Summarizes the current state of applicable regulations and compliance requirements from Dynamics 365 F&SCM for a legal entity, returning a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-identify-applicable-regulations-and-compliance-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-applicable-regulations-and-compliance-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3d0d2080a635f9d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/identify-applicable-regulations-and-compliance-requirements'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-identify-applicable-regulations-and-compliance-requirements', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the update reflects, used in the card filename.', 'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of identify applicable regulations and compliance requirements. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-identify-applicable-regulations-and-compliance-requirements-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify applicable regulations and compliance requirements, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of applicable regulations and compliance requirements from Dynamics 365 F&SCM for a legal entity, returning a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not', 'example_request': 'Draft a Teams update on compliance requirements status for USMF with an Adaptive Card I can review.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Date the update reflects, used in the card filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on regulatory/compliance status from D365 ERP data, with a triage Adaptive Card saved for their review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateIdentifyApplicableRegulationsAndComplianceRequirements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyApplicableRegulationsAndComplianceRequirements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the update reflects, used in the card filename.', 'type': 'string'}, 'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateIdentifyApplicableRegulationsAndComplianceRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
