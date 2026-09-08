---
name: "rar-cowork-cookbook-find-the-deals-that-need-my-help"
description: "Rolls up the caller's team pipeline from Dynamics 365 Sales by risk signal and activity recency, returning a prioritized list of deals needing manager involvement plus a deep-dive report with root cause and a recommended"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_the_deals_that_need_my_help", "rar_sha256": "d4a63bf44156a4c8c3dd79d47d3489b411f4f6150c8107442a875ef5d90d11ab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/find_the_deals_that_need_my_help`. The original RAPP
agent is preserved byte-for-byte in `find_the_deals_that_need_my_help_agent.py` and in the RCI capsule.

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

Find the deals that need my help — Rolls up the caller's team pipeline from Dynamics 365 Sales by risk signal and activity recency, returning a prioritized list of deals needing manager involvement plus a deep-dive report with root cause and a recommended

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
  Upstream entry : https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help
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
    },
    "team_scope": {
      "description": "Whose pipeline to roll up \u2014 the manager's team in the bound Dynamics 365 Sales environment.",
      "type": "string"
    },
    "time_window": {
      "description": "The period to assess, e.g. this week.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_the_deals_that_need_my_help_agent.py` and embedded as the fenced Python below (sha256 d4a63bf44156a4c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_the_deals_that_need_my_help_agent.py` first:

```bash
python3 find_the_deals_that_need_my_help_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_the_deals_that_need_my_help_agent.py   # or on stdin
python3 find_the_deals_that_need_my_help_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find the deals that need my help — Rolls up the caller's team pipeline from Dynamics 365 Sales by risk signal and activity recency, returning a prioritized list of deals needing manager involvement plus a deep-dive report with root cause and a recommended

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
  Upstream entry : https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_the_deals_that_need_my_help',
    "version": '3.0.3',
    "display_name": 'Find the deals that need my help',
    "description": "Rolls up the caller's team pipeline from Dynamics 365 Sales by risk signal and activity recency, returning a prioritized list of deals needing manager involvement plus a deep-dive report with root cause and a recommended",
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
        "upstream_slug": 'find-the-deals-that-need-my-help',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a53bce5d0be5765c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/find-the-deals-that-need-my-help', 'uses_skills': {'custom': [], 'ootb': ['Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A prioritized list of team deals needing manager involvement, paired with a deep research report that digs into the at-risk opportunities - root cause, account context, and a recommended play for each.'], 'confidence': 1.0, 'deliverable': 'A prioritized list of team deals needing manager involvement, paired with a deep research report that digs into the at-risk opportunities - root cause, account context, and a recommended play for each.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'team_scope': "Whose pipeline to roll up — the manager's team in the bound Dynamics 365 Sales environment.", 'time_window': 'The period to assess, e.g. this week.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is A prioritized list of team deals needing manager involvement, paired with a deep research report that digs into the at-risk opportunities - root cause, account context, and a recommended play for each.', 'expected_output': 'A prioritized list of team deals needing manager involvement, paired with a deep research report that digs into the at-risk opportunities - root cause, account context, and a recommended play for each.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "Which deals need my direct involvement this week? Roll up my team's pipeline from Dynamics 365 Sales by risk signal and activity recency - stalled deals, slipped close dates, accounts gone quiet.\n\nThen run a deep research report on the flagged opportunities: pull the account history, recent engagement, and deal context, dig into the likely root cause behind each stall, and recommend a specific play I can run.\n\nDeliver the prioritized list up front, with the deep-dive report behind it.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A prioritized list of team deals needing manager involvement, paired with a deep research report that digs into the at-risk opportunities - root cause, account context, and a recommended play for each.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Rolls up the caller's team pipeline from Dynamics 365 Sales by risk signal and activity recency, returning a prioritized list of deals needing manager involvement plus a deep-dive report with root cause and a recommended", 'example_request': 'Which deals on my team need my direct involvement this week, and why is each one stuck?', 'inputs': [{'description': 'The period to assess, e.g. this week.', 'name': 'time_window'}, {'description': "Whose pipeline to roll up — the manager's team in the bound Dynamics 365 Sales environment.", 'name': 'team_scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a sales manager asks which team deals are stalled, slipping, or gone quiet this week and where their direct involvement is needed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class FindTheDealsThatNeedMyHelp(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindTheDealsThatNeedMyHelp'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'team_scope': {'description': "Whose pipeline to roll up — the manager's team in the bound Dynamics 365 Sales environment.", 'type': 'string'}, 'time_window': {'description': 'The period to assess, e.g. this week.', 'type': 'string'}},
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
    print(FindTheDealsThatNeedMyHelp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
