---
name: "rar-cowork-cookbook-find-my-best-expansion-accounts"
description: "Ranks your Dynamics 365 Sales accounts by how closely their Fabric IQ year-over-year revenue and consumption trends match accounts that doubled spend, and builds a one-page expansion brief for the top 3."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_my_best_expansion_accounts", "rar_sha256": "0300c183c5e886c99877ac3729d7a3cd60426c79277eba944123217782c2bf7c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
