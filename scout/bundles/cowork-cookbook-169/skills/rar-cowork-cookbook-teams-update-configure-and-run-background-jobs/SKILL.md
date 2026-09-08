---
name: "rar-cowork-cookbook-teams-update-configure-and-run-background-jobs"
description: "Summarizes the state of configure-and-run background jobs in Dynamics 365 F&SCM for a legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_run_background_jobs", "rar_sha256": "11d87852573cff7964b066619a2220d183272681086a7db171430f8301656a13", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
