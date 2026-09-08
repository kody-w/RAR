---
name: "rar-cowork-cookbook-teams-update-define-accounts-payable-policies"
description: "Summarizes accounts payable policy status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_accounts_payable_policies", "rar_sha256": "11d950fbf3aed4637a15bcd1d22752a73e7197e089c6235dd62d92ae7972ffb3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
