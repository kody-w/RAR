---
name: "rar-cowork-cookbook-teams-update-audit-workplace-for-safety"
description: "Summarizes workplace safety audit status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_audit_workplace_for_safety", "rar_sha256": "c5f9087a66a48ff946e88d529cc962861368760acb3323dc7b46de25ac22ac49", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_audit_workplace_for_safety`. The original RAPP
agent is preserved byte-for-byte in `teams_update_audit_workplace_for_safety_agent.py` and in the RCI capsule.

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

Audit workplace for safety Teams Channel Update — Summarizes workplace safety audit status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-audit-workplace-for-safety
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-audit-workplace-for-safety-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_audit_workplace_for_safety_agent.py` and embedded as the fenced Python below (sha256 c5f9087a66a48ff9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_audit_workplace_for_safety_agent.py` first:

```bash
python3 teams_update_audit_workplace_for_safety_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_audit_workplace_for_safety_agent.py   # or on stdin
python3 teams_update_audit_workplace_for_safety_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit workplace for safety Teams Channel Update — Summarizes workplace safety audit status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-audit-workplace-for-safety
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_audit_workplace_for_safety',
    "version": '3.0.3',
    "display_name": 'Audit workplace for safety Teams Channel Update',
    "description": 'Summarizes workplace safety audit status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-audit-workplace-for-safety',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-audit-workplace-for-safety',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ee859601e642a8b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/audit-workplace-for-safety'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-audit-workplace-for-safety', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-audit-workplace-for-safety-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of audit workplace for safety. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-audit-workplace-for-safety-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads audit workplace for safety, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes workplace safety audit status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.', 'example_request': "Draft a Teams post and Adaptive Card on the workplace safety audit status in USMF — don't post it, just save them.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-audit-workplace-for-safety-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on safety audit status pulled from D365 ERP, without posting it automatically.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAuditWorkplaceForSafety(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAuditWorkplaceForSafety'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-audit-workplace-for-safety-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAuditWorkplaceForSafety().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
