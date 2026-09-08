---
name: "rar-cowork-cookbook-find-my-best-expansion-accounts"
description: "Ranks your Dynamics 365 Sales accounts by how closely their Fabric IQ year-over-year revenue and consumption trends match accounts that doubled spend, and builds a one-page expansion brief for the top 3."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_my_best_expansion_accounts", "rar_sha256": "0300c183c5e886c99877ac3729d7a3cd60426c79277eba944123217782c2bf7c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/find_my_best_expansion_accounts`. The original RAPP
agent is preserved byte-for-byte in `find_my_best_expansion_accounts_agent.py` and in the RCI capsule.

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

Find my best expansion accounts — Ranks your Dynamics 365 Sales accounts by how closely their Fabric IQ year-over-year revenue and consumption trends match accounts that doubled spend, and builds a one-page expansion brief for the top 3.

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
  Upstream entry : https://coworkcookbook.com/recipes/find-my-best-expansion-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_my_best_expansion_accounts_agent.py` and embedded as the fenced Python below (sha256 0300c183c5e886c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_my_best_expansion_accounts_agent.py` first:

```bash
python3 find_my_best_expansion_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_my_best_expansion_accounts_agent.py   # or on stdin
python3 find_my_best_expansion_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find my best expansion accounts — Ranks your Dynamics 365 Sales accounts by how closely their Fabric IQ year-over-year revenue and consumption trends match accounts that doubled spend, and builds a one-page expansion brief for the top 3.

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
  Upstream entry : https://coworkcookbook.com/recipes/find-my-best-expansion-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_my_best_expansion_accounts',
    "version": '3.0.3',
    "display_name": 'Find my best expansion accounts',
    "description": 'Ranks your Dynamics 365 Sales accounts by how closely their Fabric IQ year-over-year revenue and consumption trends match accounts that doubled spend, and builds a one-page expansion brief for the top 3.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'find-my-best-expansion-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-my-best-expansion-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0631684e1417b804',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/find-my-best-expansion-accounts', 'uses_skills': {'custom': [], 'ootb': ['Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A ranked expansion shortlist plus a one-page expansion brief per top account - the spend-growth signals, the likely expansion play, and the stakeholders to engage.'], 'confidence': 1.0, 'deliverable': 'A ranked expansion shortlist plus a one-page expansion brief per top account - the spend-growth signals, the likely expansion play, and the stakeholders to engage.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Surface the accounts most likely to grow - and arrive at each one with the expansion case already built. A ranked expansion shortlist plus a one-page expansion brief per top account - the spend-growth signals, the likely expansion play, and the stakeholders to engage.', 'expected_output': 'A ranked expansion shortlist plus a one-page expansion brief per top account - the spend-growth signals, the likely expansion play, and the stakeholders to engage.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': 'Which of my accounts match the pattern of accounts that doubled spend last year? Pull my account base from Dynamics 365 Sales and use Fabric IQ to read year-over-year revenue and consumption trends.\n\nIdentify the accounts whose signals match my historical doublers and rank them by expansion likelihood with a one-line "why" for each.\n\nThen, for the top 3, build a one-page expansion brief: the spend and usage signals driving the match, the most likely expansion play, the key stakeholders to engage, and a recommended first move.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A ranked expansion shortlist plus a one-page expansion brief per top account - the spend-growth signals, the likely expansion play, and the stakeholders to engage.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Ranks your Dynamics 365 Sales accounts by how closely their Fabric IQ year-over-year revenue and consumption trends match accounts that doubled spend, and builds a one-page expansion brief for the top 3.', 'example_request': 'Which of my accounts match the pattern of accounts that doubled spend last year, and brief me on the top 3?', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want to find which existing accounts are most likely to expand and get the expansion case (signals, play, stakeholders, first move) prepared.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class FindMyBestExpansionAccounts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindMyBestExpansionAccounts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(FindMyBestExpansionAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
