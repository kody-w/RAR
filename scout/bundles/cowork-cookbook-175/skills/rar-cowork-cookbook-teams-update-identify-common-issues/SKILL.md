---
name: "rar-cowork-cookbook-teams-update-identify-common-issues"
description: "Summarizes the current state of common issues from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_common_issues", "rar_sha256": "dfb37f4a988bf912317a485052412d7a29edcdc68c6bed75e60f3dfe70a739b5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_common_issues`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_common_issues_agent.py` and in the RCI capsule.

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

Identify common issues Teams Channel Update — Summarizes the current state of common issues from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-common-issues
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-identify-common-issues-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the summary, e.g. USMF.",
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
    "topic": {
      "description": "The issue area to summarize, e.g. 'identify common issues'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_common_issues_agent.py` and embedded as the fenced Python below (sha256 dfb37f4a988bf912…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_common_issues_agent.py` first:

```bash
python3 teams_update_identify_common_issues_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_common_issues_agent.py   # or on stdin
python3 teams_update_identify_common_issues_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify common issues Teams Channel Update — Summarizes the current state of common issues from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-common-issues
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_common_issues',
    "version": '3.0.3',
    "display_name": 'Identify common issues Teams Channel Update',
    "description": 'Summarizes the current state of common issues from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-identify-common-issues',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-common-issues',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7bf04ed21bcc7cd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/identify-common-issues'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-identify-common-issues', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-identify-common-issues-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the summary, e.g. USMF.', 'topic': "The issue area to summarize, e.g. 'identify common issues'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of identify common issues. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-identify-common-issues-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify common issues, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of common issues from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing', 'example_request': "Draft a Teams update on common issues in USMF from D365 with an Adaptive Card JSON — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': "The issue area to summarize, e.g. 'identify common issues'.", 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-identify-common-issues-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on D365 common-issues status, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateIdentifyCommonIssues(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyCommonIssues'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-identify-common-issues-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': "The issue area to summarize, e.g. 'identify common issues'.", 'type': 'string'}},
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
    print(TeamsUpdateIdentifyCommonIssues().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
