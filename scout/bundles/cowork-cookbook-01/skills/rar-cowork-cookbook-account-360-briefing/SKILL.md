---
name: "rar-cowork-cookbook-account-360-briefing"
description: "Builds a read-only Account 360 briefing pack from Dynamics 365 Sales for one named account \u2014 profile, contacts, open and closed opportunities, activity timeline, and risks \u2014 as 'account-briefing.docx'. Call before a cust"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/account_360_briefing", "rar_sha256": "0304a970d3e1556cb5abde57bad9b2c0719ece0066c364176ae467490e97f45f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/account_360_briefing`. The original RAPP
agent is preserved byte-for-byte in `account_360_briefing_agent.py` and in the RCI capsule.

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

Account 360 Briefing Pack — Builds a read-only Account 360 briefing pack from Dynamics 365 Sales for one named account — profile, contacts, open and closed opportunities, activity timeline, and risks — as 'account-briefing.docx'. Call before a cust

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
  Upstream entry : https://coworkcookbook.com/recipes/account-360-briefing
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
    "account_name": {
      "description": "The exact Dynamics 365 Sales account name to brief on; ambiguous names return close matches instead of a brief.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `account_360_briefing_agent.py` and embedded as the fenced Python below (sha256 0304a970d3e1556c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `account_360_briefing_agent.py` first:

```bash
python3 account_360_briefing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 account_360_briefing_agent.py   # or on stdin
python3 account_360_briefing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Account 360 Briefing Pack — Builds a read-only Account 360 briefing pack from Dynamics 365 Sales for one named account — profile, contacts, open and closed opportunities, activity timeline, and risks — as 'account-briefing.docx'. Call before a cust

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
  Upstream entry : https://coworkcookbook.com/recipes/account-360-briefing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/account_360_briefing',
    "version": '3.0.2',
    "display_name": 'Account 360 Briefing Pack',
    "description": "Builds a read-only Account 360 briefing pack from Dynamics 365 Sales for one named account — profile, contacts, open and closed opportunities, activity timeline, and risks — as 'account-briefing.docx'. Call before a cust",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'account-360-briefing',
        "upstream_url": 'https://coworkcookbook.com/recipes/account-360-briefing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45d1966d91a95e4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/account-360-briefing', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: A Word document of roughly two to three pages, opening with a short summary and then the\ndetailed sections. Length scales with how much history the account actually has.'], 'confidence': 1.0, 'deliverable': 'A Word document of roughly two to three pages, opening with a short summary and then the\ndetailed sections. Length scales with how much history the account actually has.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'account_name': 'The exact Dynamics 365 Sales account name to brief on; ambiguous names return close matches instead of a brief.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces fifteen minutes of clicking through related-record tabs with a single document. Sellers walk into customer conversations with the full relationship history rather than whatever they could skim on the way in.', 'expected_output': 'A Word document of roughly two to three pages, opening with a short summary and then the\ndetailed sections. Length scales with how much history the account actually has.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, build a briefing pack on the account named below.\n\nACCOUNT: <type the account name here>\n\nUse search and describe to confirm the account, contact, opportunity, and activity tables and\nthe columns you need from each. Do not guess column or relationship names.\n\nThen assemble, for that account:\n- the account profile: industry, size, ownership, and any relationship or account-type fields\n  your environment carries\n- the contact roster, with role or job title, and a note of who has been most recently active\n- open opportunities: stage, estimated value, estimated close date, owner\n- closed opportunities: won and lost, with values and any loss reasons recorded\n- the recent activity timeline, most recent first, summarized rather than listed verbatim\n- anything that looks like a risk or an opening — dormant contacts, aging open deals,\n  repeated loss reasons\n\nProduce a Word document 'account-briefing.docx' organized under those headings, written to be\nread in about three minutes. Lead with a short 'what you need to know' summary.\n\nDo not modify any data. If the account name does not match a record, list the closest matches\nand stop rather than guessing which one I meant.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Edit the `ACCOUNT:` line in the prompt to name the account you want.', 'Paste the prompt into a new task and send it.', 'If Cowork returns a list of close matches instead of a brief, pick one and re-run with the'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "Traverses the account's related records and composes them into a readable narrative brief. The\nno-guessing rule on account matching prevents a briefing on the wrong customer."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only Account 360 briefing pack from Dynamics 365 Sales for one named account — profile, contacts, open and closed opportunities, activity timeline, and risks — as 'account-briefing.docx'. Call before a cust", 'example_request': 'Build me an account briefing pack on Contoso Ltd from Dynamics 365 Sales before my meeting.', 'inputs': [{'description': 'The exact Dynamics 365 Sales account name to brief on; ambiguous names return close matches instead of a brief.', 'name': 'account_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a single pre-meeting brief on one Dynamics 365 Sales account; it stops and lists close matches if the account name is ambiguous.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Edit the `ACCOUNT:` line in the prompt to name the account you want.', 'Paste the prompt into a new task and send it.', 'If Cowork returns a list of close matches instead of a brief, pick one and re-run with the'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class Account360Briefing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'Account360Briefing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'account_name': {'description': 'The exact Dynamics 365 Sales account name to brief on; ambiguous names return close matches instead of a brief.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(Account360Briefing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
