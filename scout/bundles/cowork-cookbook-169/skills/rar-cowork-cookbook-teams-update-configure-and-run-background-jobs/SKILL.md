---
name: "rar-cowork-cookbook-teams-update-configure-and-run-background-jobs"
description: "Summarizes the state of configure-and-run background jobs in Dynamics 365 F&SCM for a legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_run_background_jobs", "rar_sha256": "11d87852573cff7964b066619a2220d183272681086a7db171430f8301656a13", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_run_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_run_background_jobs_agent.py` and in the RCI capsule.

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

Configure and run background jobs Teams Channel Update — Summarizes the state of configure-and-run background jobs in Dynamics 365 F&SCM for a legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-configure-and-run-background-jobs-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 11d87852573cff79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_run_background_jobs_agent.py` first:

```bash
python3 teams_update_configure_and_run_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_run_background_jobs_agent.py   # or on stdin
python3 teams_update_configure_and_run_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and run background jobs Teams Channel Update — Summarizes the state of configure-and-run background jobs in Dynamics 365 F&SCM for a legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_run_background_jobs',
    "version": '3.0.3',
    "display_name": 'Configure and run background jobs Teams Channel Update',
    "description": 'Summarizes the state of configure-and-run background jobs in Dynamics 365 F&SCM for a legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.',
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
        "upstream_slug": 'teams-update-configure-and-run-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bdd25070fcd7b25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/configure-and-run-background-jobs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-run-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-configure-and-run-background-jobs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of configure and run background jobs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-configure-and-run-background-jobs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and run background jobs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the state of configure-and-run background jobs in Dynamics 365 F&SCM for a legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams update on background job status in USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-configure-and-run-background-jobs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams update on background job status in D365 ERP, with KPIs and quick-action buttons in an Adaptive Card.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConfigureAndRunBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndRunBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-configure-and-run-background-jobs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConfigureAndRunBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
