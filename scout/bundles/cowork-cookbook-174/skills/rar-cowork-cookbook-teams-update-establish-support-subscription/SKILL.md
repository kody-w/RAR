---
name: "rar-cowork-cookbook-teams-update-establish-support-subscription"
description: "Summarizes establish support subscription status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_support_subscription", "rar_sha256": "8ee02a7b3778b38428499b4c764c7aa488cf78d6c66b51a2c1550dfacdd12d40", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_establish_support_subscription`. The original RAPP
agent is preserved byte-for-byte in `teams_update_establish_support_subscription_agent.py` and in the RCI capsule.

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

Establish support subscription Teams Channel Update — Summarizes establish support subscription status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-support-subscription
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
    "as_of_date": {
      "description": "Date used for the status snapshot and the card filename.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-establish-support-subscription-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_establish_support_subscription_agent.py` and embedded as the fenced Python below (sha256 8ee02a7b3778b384…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_establish_support_subscription_agent.py` first:

```bash
python3 teams_update_establish_support_subscription_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_establish_support_subscription_agent.py   # or on stdin
python3 teams_update_establish_support_subscription_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support subscription Teams Channel Update — Summarizes establish support subscription status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-support-subscription
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_establish_support_subscription',
    "version": '3.0.3',
    "display_name": 'Establish support subscription Teams Channel Update',
    "description": 'Summarizes establish support subscription status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b',
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
        "upstream_slug": 'teams-update-establish-support-subscription',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-establish-support-subscription',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9dbecad55b4fbb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-subscription'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-establish-support-subscription', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the status snapshot and the card filename.', 'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-establish-support-subscription-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of establish support subscription. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-establish-support-subscription-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads establish support subscription, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes establish support subscription status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b', 'example_request': "Draft a Teams post and Adaptive Card on establish support subscription status for USMF as of 2026-05-24 — don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the status snapshot and the card filename.', 'name': 'as_of_date'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-establish-support-subscription-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on establish support subscription status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEstablishSupportSubscription(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstablishSupportSubscription'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the status snapshot and the card filename.', 'type': 'string'}, 'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-establish-support-subscription-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateEstablishSupportSubscription().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
