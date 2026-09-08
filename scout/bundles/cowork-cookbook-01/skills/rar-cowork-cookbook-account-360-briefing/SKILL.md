---
name: "rar-cowork-cookbook-account-360-briefing"
description: "Builds a read-only Account 360 briefing pack from Dynamics 365 Sales for one named account \u2014 profile, contacts, open and closed opportunities, activity timeline, and risks \u2014 as 'account-briefing.docx'. Call before a cust"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/account_360_briefing", "rar_sha256": "0304a970d3e1556cb5abde57bad9b2c0719ece0066c364176ae467490e97f45f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
