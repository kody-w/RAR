---
name: "rar-cowork-cookbook-teams-update-define-accounts-payable-policies"
description: "Summarizes accounts payable policy status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_accounts_payable_policies", "rar_sha256": "11d950fbf3aed4637a15bcd1d22752a73e7197e089c6235dd62d92ae7972ffb3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_accounts_payable_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_accounts_payable_policies_agent.py` and in the RCI capsule.

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

Define accounts payable policies Teams Channel Update — Summarizes accounts payable policy status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-accounts-payable-policies
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
      "description": "Filename for the generated Adaptive Card JSON artifact.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_accounts_payable_policies_agent.py` and embedded as the fenced Python below (sha256 11d950fbf3aed463…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_accounts_payable_policies_agent.py` first:

```bash
python3 teams_update_define_accounts_payable_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_accounts_payable_policies_agent.py   # or on stdin
python3 teams_update_define_accounts_payable_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts payable policies Teams Channel Update — Summarizes accounts payable policy status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-accounts-payable-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_accounts_payable_policies',
    "version": '3.0.3',
    "display_name": 'Define accounts payable policies Teams Channel Update',
    "description": 'Summarizes accounts payable policy status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-accounts-payable-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-accounts-payable-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b02c092b82b634e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/define-accounts-payable-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-define-accounts-payable-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define accounts payable policies. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-accounts-payable-policies-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define accounts payable policies, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes accounts payable policy status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on accounts payable policies for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update and Adaptive Card on define accounts payable policies status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineAccountsPayablePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineAccountsPayablePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineAccountsPayablePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
