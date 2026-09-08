---
name: "rar-cowork-cookbook-teams-update-identify-applicable-regulations-and-compliance-requirements"
description: "Summarizes the current state of applicable regulations and compliance requirements from Dynamics 365 F&SCM for a legal entity, returning a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "071629b476a8ef4ef38541922ce4463cc35910337f1c3faf57bb15e902b9cf9f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
