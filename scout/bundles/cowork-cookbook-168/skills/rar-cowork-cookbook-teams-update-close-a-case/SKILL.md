---
name: "rar-cowork-cookbook-teams-update-close-a-case"
description: "Summarizes close-a-case status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_a_case", "rar_sha256": "a786719ea7f218c6234d4b95d5180eafdefd46aec7297e19250966eab87bcce4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
