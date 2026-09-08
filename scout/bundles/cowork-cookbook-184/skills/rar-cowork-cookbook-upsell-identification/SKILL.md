---
name: "rar-cowork-cookbook-upsell-identification"
description: "Ranks your CRM accounts by expansion likelihood and, for the top candidate, returns a 5-slide expansion proposal deck, a 1-page internal account plan, and a draft exec outreach email held for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/upsell_identification", "rar_sha256": "c729638d25967d210b9abfec81b9c494c21c4a3433b3d0da0e138d4a9db8646c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
