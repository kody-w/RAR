---
name: "rar-cowork-cookbook-teams-update-identify-common-issues"
description: "Summarizes the current state of common issues from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_common_issues", "rar_sha256": "dfb37f4a988bf912317a485052412d7a29edcdc68c6bed75e60f3dfe70a739b5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
