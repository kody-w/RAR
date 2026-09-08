---
name: "rar-cowork-cookbook-teams-update-capture-details-about-a-case"
description: "Summarizes the current state of a case in Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_capture_details_about_a_case", "rar_sha256": "c9a02bc95d57455e0a8c6195834b43c6e0cde75be490241cfd54652dc851e08d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_capture_details_about_a_case`. The original RAPP
agent is preserved byte-for-byte in `teams_update_capture_details_about_a_case_agent.py` and in the RCI capsule.

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

Capture details about a case Teams Channel Update — Summarizes the current state of a case in Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-<topic>-<date>-card.json.",
      "type": "string"
    },
    "case_topic": {
      "description": "The case or subject to capture and summarize.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 c9a02bc95d57455e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_capture_details_about_a_case_agent.py` first:

```bash
python3 teams_update_capture_details_about_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_capture_details_about_a_case_agent.py   # or on stdin
python3 teams_update_capture_details_about_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Capture details about a case Teams Channel Update — Summarizes the current state of a case in Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_capture_details_about_a_case',
    "version": '3.0.3',
    "display_name": 'Capture details about a case Teams Channel Update',
    "description": 'Summarizes the current state of a case in Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anything.',
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
        "upstream_slug": 'teams-update-capture-details-about-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '153480898070874f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/capture-details-about-a-case'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-capture-details-about-a-case', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-<topic>-<date>-card.json.', 'case_topic': 'The case or subject to capture and summarize.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of capture details about a case. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-capture-details-about-a-case-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads capture details about a case, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of a case in Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anything.', 'example_request': "Draft a Teams update and Adaptive Card on the case status in D365 USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The case or subject to capture and summarize.', 'name': 'case_topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-<topic>-<date>-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card about a D365 case status, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCaptureDetailsAboutACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCaptureDetailsAboutACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-<topic>-<date>-card.json.', 'type': 'string'}, 'case_topic': {'description': 'The case or subject to capture and summarize.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateCaptureDetailsAboutACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
