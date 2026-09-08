---
name: "rar-cowork-cookbook-teams-update-establish-support-subscription"
description: "Summarizes establish support subscription status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_support_subscription", "rar_sha256": "8ee02a7b3778b38428499b4c764c7aa488cf78d6c66b51a2c1550dfacdd12d40", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
