---
name: "rar-cowork-cookbook-teams-update-close-a-case"
description: "Summarizes close-a-case status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_a_case", "rar_sha256": "a786719ea7f218c6234d4b95d5180eafdefd46aec7297e19250966eab87bcce4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_close_a_case`. The original RAPP
agent is preserved byte-for-byte in `teams_update_close_a_case_agent.py` and in the RCI capsule.

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

Close a case Teams Channel Update — Summarizes close-a-case status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-a-case
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-close-a-case-2026-05-24-card.json.",
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
    },
    "scope": {
      "description": "Optional scope or date qualifier for the close-a-case status summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_close_a_case_agent.py` and embedded as the fenced Python below (sha256 a786719ea7f218c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_close_a_case_agent.py` first:

```bash
python3 teams_update_close_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_close_a_case_agent.py   # or on stdin
python3 teams_update_close_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close a case Teams Channel Update — Summarizes close-a-case status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_close_a_case',
    "version": '3.0.3',
    "display_name": 'Close a case Teams Channel Update',
    "description": 'Summarizes close-a-case status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.',
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
        "upstream_slug": 'teams-update-close-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-close-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c068dd37da08436',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/close-a-case'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-close-a-case', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-close-a-case-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'scope': 'Optional scope or date qualifier for the close-a-case status summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of close a case. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-close-a-case-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads close a case, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes close-a-case status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.', 'example_request': "Draft a Teams post and Adaptive Card on close-a-case status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-close-a-case-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional scope or date qualifier for the close-a-case status summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on close-a-case status from D365 F&SCM, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCloseACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCloseACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-close-a-case-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional scope or date qualifier for the close-a-case status summary.', 'type': 'string'}},
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
    print(TeamsUpdateCloseACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
