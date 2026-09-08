---
name: "rar-cowork-cookbook-teams-update-conduct-post-sale-follow-up"
description: "Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_post_sale_follow_up", "rar_sha256": "abb709b04aff55579fbf712f72ae0b63bb9543040b6b648f4b0900a4b07991d2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_post_sale_follow_up`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_post_sale_follow_up_agent.py` and in the RCI capsule.

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

Conduct post-sale follow-up Teams Channel Update — Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 abb709b04aff5557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 teams_update_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 teams_update_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Teams Channel Update — Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_post_sale_follow_up',
    "version": '3.0.3',
    "display_name": 'Conduct post-sale follow-up Teams Channel Update',
    "description": 'Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '454bf84372283b4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of conduct post-sale follow-up. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-conduct-post-sale-follow-up-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct post-sale follow-up, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.', 'example_request': "Draft a Teams update on post-sale follow-up in USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update on post-sale follow-up status from D365 F&SCM, saved as artifacts for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConductPostSaleFollowUp(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductPostSaleFollowUp'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
