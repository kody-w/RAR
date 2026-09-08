---
name: "rar-cowork-cookbook-teams-update-capture-details-about-a-case"
description: "Summarizes the current state of a case in Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_capture_details_about_a_case", "rar_sha256": "c9a02bc95d57455e0a8c6195834b43c6e0cde75be490241cfd54652dc851e08d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
