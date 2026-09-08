---
name: "rar-cowork-cookbook-teams-update-review-access-policies"
description: "Summarizes review access policies from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_review_access_policies", "rar_sha256": "67b2758834ce09e10eebfe03c80328db8f70e0be8d8cda0a9474da11c37dba6c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
