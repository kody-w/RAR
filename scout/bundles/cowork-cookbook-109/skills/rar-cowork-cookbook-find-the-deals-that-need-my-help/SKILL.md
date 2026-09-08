---
name: "rar-cowork-cookbook-find-the-deals-that-need-my-help"
description: "Rolls up the caller's team pipeline from Dynamics 365 Sales by risk signal and activity recency, returning a prioritized list of deals needing manager involvement plus a deep-dive report with root cause and a recommended"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_the_deals_that_need_my_help", "rar_sha256": "d4a63bf44156a4c8c3dd79d47d3489b411f4f6150c8107442a875ef5d90d11ab", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
