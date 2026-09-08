---
name: "rar-cowork-cookbook-teams-update-review-access-policies"
description: "Summarizes review access policies from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_review_access_policies", "rar_sha256": "67b2758834ce09e10eebfe03c80328db8f70e0be8d8cda0a9474da11c37dba6c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_review_access_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_review_access_policies_agent.py` and in the RCI capsule.

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

Review access policies Teams Channel Update — Summarizes review access policies from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing is

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-review-access-policies
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-review-access-policies-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 67b2758834ce09e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_review_access_policies_agent.py` first:

```bash
python3 teams_update_review_access_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_review_access_policies_agent.py   # or on stdin
python3 teams_update_review_access_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review access policies Teams Channel Update — Summarizes review access policies from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing is

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-review-access-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_review_access_policies',
    "version": '3.0.3',
    "display_name": 'Review access policies Teams Channel Update',
    "description": 'Summarizes review access policies from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing is',
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
        "upstream_slug": 'teams-update-review-access-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-review-access-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b1896dcb6ba38fa0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-access-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-review-access-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-review-access-policies-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of review access policies. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-review-access-policies-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads review access policies, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes review access policies from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing is', 'example_request': "Draft a Teams update on review access policies for USMF with an Adaptive Card - save it, don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-review-access-policies-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'When you need a drafted Teams channel update on review access policies status from D365 F&SCM, saved as artifacts for your own review before posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReviewAccessPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReviewAccessPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-review-access-policies-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateReviewAccessPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
