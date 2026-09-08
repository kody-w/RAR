---
name: "rar-cowork-cookbook-teams-update-audit-workplace-for-safety"
description: "Summarizes workplace safety audit status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_audit_workplace_for_safety", "rar_sha256": "c5f9087a66a48ff946e88d529cc962861368760acb3323dc7b46de25ac22ac49", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
