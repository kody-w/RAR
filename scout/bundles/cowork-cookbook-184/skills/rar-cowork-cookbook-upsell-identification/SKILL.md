---
name: "rar-cowork-cookbook-upsell-identification"
description: "Ranks your CRM accounts by expansion likelihood and, for the top candidate, returns a 5-slide expansion proposal deck, a 1-page internal account plan, and a draft exec outreach email held for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/upsell_identification", "rar_sha256": "c729638d25967d210b9abfec81b9c494c21c4a3433b3d0da0e138d4a9db8646c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/upsell_identification`. The original RAPP
agent is preserved byte-for-byte in `upsell_identification_agent.py` and in the RCI capsule.

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

Upsell identification — Ranks your CRM accounts by expansion likelihood and, for the top candidate, returns a 5-slide expansion proposal deck, a 1-page internal account plan, and a draft exec outreach email held for review.

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
  Upstream entry : https://coworkcookbook.com/recipes/upsell-identification
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "crm_account_snapshot": {
      "description": "Spreadsheet export of your accounts (e.g. CRM Account Snapshot.xlsx) to rank for expansion likelihood.",
      "type": "string"
    },
    "dynamics_365_sales_connection": {
      "description": "Dynamics 365 Sales plugin enabled in the Cowork session and bound to your CRM environment.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `upsell_identification_agent.py` and embedded as the fenced Python below (sha256 c729638d25967d21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `upsell_identification_agent.py` first:

```bash
python3 upsell_identification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 upsell_identification_agent.py   # or on stdin
python3 upsell_identification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Upsell identification — Ranks your CRM accounts by expansion likelihood and, for the top candidate, returns a 5-slide expansion proposal deck, a 1-page internal account plan, and a draft exec outreach email held for review.

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
  Upstream entry : https://coworkcookbook.com/recipes/upsell-identification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/upsell_identification',
    "version": '3.0.3',
    "display_name": 'Upsell identification',
    "description": 'Ranks your CRM accounts by expansion likelihood and, for the top candidate, returns a 5-slide expansion proposal deck, a 1-page internal account plan, and a draft exec outreach email held for review.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'upsell-identification',
        "upstream_url": 'https://coworkcookbook.com/recipes/upsell-identification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0197162bc9b1e6d5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/upsell-identification', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A 5-slide PowerPoint Expansion Pack, a 1-page Word internal account plan, and a draft executive outreach email - held for review before sending.'], 'confidence': 1.0, 'deliverable': 'A 5-slide PowerPoint Expansion Pack, a 1-page Word internal account plan, and a draft executive outreach email - held for review before sending.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'crm_account_snapshot': 'Spreadsheet export of your accounts (e.g. CRM Account Snapshot.xlsx) to rank for expansion likelihood.', 'dynamics_365_sales_connection': 'Dynamics 365 Sales plugin enabled in the Cowork session and bound to your CRM environment.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Find the best expansion opportunity in your book this week and arrive with a pitch already built. A 5-slide PowerPoint Expansion Pack, a 1-page Word internal account plan, and a draft executive outreach email - held for review before sending.', 'expected_output': 'A 5-slide PowerPoint Expansion Pack, a 1-page Word internal account plan, and a draft executive outreach email - held for review before sending.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "It's a new week and I want to find the best expansion opportunity in my book before the calendar fills up. Identify the top upsell candidate and build a tailored expansion pitch.\n\nStart by ranking my accounts by expansion likelihood - factor in renewal window, recent engagement, exec changes, relevant news, and recent meeting sentiment. For the top account, give me a tight summary of current state, value realized, unmet needs, and key decision makers.\n\nThen build an Expansion Pack:\n\nA 5-slide expansion proposal deck: value realized → gap → proposed add-on → ROI → close plan\n\nA 1-page internal account plan: stakeholders, timeline, risks, and next best actions\n\nFinally, draft an outreach email to the exec sponsor and champion - keep it warm, direct, and grounded in the value they've already realized. Show me the draft before sending.\n\nAttach: [CRM Account Snapshot.xlsx]", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A 5-slide PowerPoint Expansion Pack, a 1-page Word internal account plan, and a draft executive outreach email - held for review before sending.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Ranks your CRM accounts by expansion likelihood and, for the top candidate, returns a 5-slide expansion proposal deck, a 1-page internal account plan, and a draft exec outreach email held for review.', 'example_request': 'Find my top upsell candidate this week and build the expansion deck, account plan, and exec email.', 'inputs': [{'description': 'Spreadsheet export of your accounts (e.g. CRM Account Snapshot.xlsx) to rank for expansion likelihood.', 'name': 'CRM Account Snapshot'}, {'description': 'Dynamics 365 Sales plugin enabled in the Cowork session and bound to your CRM environment.', 'name': 'Dynamics 365 Sales connection'}], 'model': 'claude-opus-5', 'when_to_use': 'Use at the start of a week to pick the best upsell opportunity in your book and get the pitch materials built before outreach.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class UpsellIdentification(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'UpsellIdentification'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'crm_account_snapshot': {'description': 'Spreadsheet export of your accounts (e.g. CRM Account Snapshot.xlsx) to rank for expansion likelihood.', 'type': 'string'}, 'dynamics_365_sales_connection': {'description': 'Dynamics 365 Sales plugin enabled in the Cowork session and bound to your CRM environment.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(UpsellIdentification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
