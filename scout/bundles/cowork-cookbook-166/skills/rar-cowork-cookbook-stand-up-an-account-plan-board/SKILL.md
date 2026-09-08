---
name: "rar-cowork-cookbook-stand-up-an-account-plan-board"
description: "Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_an_account_plan_board", "rar_sha256": "44fca67437db27adb8290b44c6cf4a59ce3e426a0a5816b436da3ad6db453d69", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stand_up_an_account_plan_board`. The original RAPP
agent is preserved byte-for-byte in `stand_up_an_account_plan_board_agent.py` and in the RCI capsule.

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

Stand up an account plan board — Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.

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
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
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
    "customer_name": {
      "description": "The account/customer name the plan is being built for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_an_account_plan_board_agent.py` and embedded as the fenced Python below (sha256 44fca67437db27ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_an_account_plan_board_agent.py` first:

```bash
python3 stand_up_an_account_plan_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stand_up_an_account_plan_board_agent.py   # or on stdin
python3 stand_up_an_account_plan_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stand up an account plan board — Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.

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
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stand_up_an_account_plan_board',
    "version": '3.0.3',
    "display_name": 'Stand up an account plan board',
    "description": 'Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'stand-up-an-account-plan-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/stand-up-an-account-plan-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b947b5555e94eba3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/stand-up-an-account-plan-board', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.'], 'confidence': 1.0, 'deliverable': 'A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The account/customer name the plan is being built for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Move from a scattered account plan to a structured working board the full account team can run against. A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.', 'expected_output': 'A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': "I'm building out the account plan for [Customer Name] and need to give the account team a single working board. Pull recent emails, meetings, and CRM notes related to the account to identify key stakeholders, active workstreams, and outstanding next steps\n\nThen build a Monday.com board with the structure: Workstream name, owner, status, next step, due date. Group by workstream and pre-fill what you can infer.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.', 'example_request': 'Build an account plan board in Monday.com for Contoso from our recent emails, meetings, and CRM notes.', 'inputs': [{'description': 'The account/customer name the plan is being built for.', 'name': 'customer_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a scattered account plan turned into a single structured Monday.com board the account team can work from.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class StandUpAnAccountPlanBoard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StandUpAnAccountPlanBoard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The account/customer name the plan is being built for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(StandUpAnAccountPlanBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaSLbmX2He+6GqLvYrtEu+0REDaAEJEEhISCpXuLRLaN+XmvrvkwJsV3VX970dMZ8G24GWzCfP+pyTTn57s9omzKu3T2+KZ2UL3kqSKPSqhZW5i23e51UMvvLYBv8WTp41VWS3TV7Vbx/eXK92qqhoojwD0zdtlLj1wloc88y1xncnTxeW4+Rt1iyKBEDbuVW5Cz8H2IvMSj134bR1k6dgMXtcFC1YOAsWled4YIaXWlFSf1iknteAx+DqIZB8XGR549WLJl9ELhgY+eOibqzYC/PE9Sowbha5birPSsFN3mePh5k3NGCcV7yA3NZbuBYAel9sgcaLPvSyGaeaFwMj/iT5O9DVG6y0SLz67dPPv3x4i8D126ff3pzEquvZdA0AVYt1tn5OO4NZm1ldMBNcBmBIMQIzZ+C+8CpggxQ8cj1/8br7sfYS/8PiP/8z7q0qqH/69DlbvD6f3+Y/cpstmtADeltADWA6q7DsKIma8X2xTnprrIHlmrbKZg8A9YEa78+Z35HyYvG3+d2Pz0XeA6/58fNbDkSwZh9+fvtpAZzz+a1q5+v3GaX48af3JO+96sefvuPUrX33nGYGA1K/f3ndv2DBwO9DI3/xRTmz29dawLlR4QHwP+g3f56iv+BeJvnyHPxjXnxY/DXyrM/fgLzPOLQB7l/DAhuAmW/v9zzKfnytUeWdl1mZ4/340z+DdULPiZOobv5HuD8/gUPPAmH448skP314uO+XxfKl2zfMf77sHHH/jiZg+Nflvhnqn2E/PPt30CDrQD599eVfwv3VhOXfFj//U93+1YQPC//zG+MlUQfizk68T4vfHiHy8w/u94c//PI7gP5vYZS8rZwHwpfUyiLfq5svX37+oX48/uGXn39oiycVfGmr5K8w/8quj3X+ZMHXqB//PBesr2ZxBihm8S2HFr/lxf+qfn9faFYSud+f158Wf8zE+bNczEp8XfRpgj9kYw1k/YMdf3r7HdBOBrRpncdrwB//8R+LY+RUeZ37zUIBxNMsgIObKPVm4a9hVC/A35k1Kg/YtY6AYV/jQPzPHp4lzv3Fr//beTD9R+fF9FA9E9qXtvhiZV9eVPgIjS8PEv/1fXEFqHkVBVFmJQt5fT5/zqxgJm6wYlF5tVd1gKXssfE+gmT+OF8somzx678G/vLAeC/GXx8sHT05T97uZ76r28R7nzW7zWT91MMBVO0NntMC+CR3gCx+BFj6A9C4zpMO8OVshTqOAMe7EWAUULrGBzaw1KcZ7Ndff7WtOvycPQkaXTxrWg2BAd/EWXz8CJTykygIm8+Z54T54offfv9h8X8W/2rWA3xe4wyqxMsPQEJBkU4LkFdtCoYBFwGnAtJ4+OG331+mBTCgcC2A1yI/8p6TQVzGnvvVzspu/RHBiYXtAfsC26ZF/ixeUfO+2PuLb/KCRedXc10I87pZuF7hZaB0OiNAtYA63ywJKuuiBsFX++OHRVt7j1V/tSvrIWIKEtxqfl0ct2dQhfJkLsHVqyqByXkWAfN/i4LncwBS/VAvNl8h3henORIXhVVZRVhZrzV86+mXuTV4TQfgoEvw+s/ZXGu92VSPtHiaBwwClnFeLv04+xw0JyngALf+uvZjjDXXyuujZlafs/oV8lY1u8IBJQAsGrSROxeC/3qFVB3mbeI+7AcknZFeXnBfXnnE4KPiL9ri73uFV5fzuUVWMLb4/7gnmo2w5nmZ5ddXllmwp6tsPJ0zd4mzuM/GEnQoD/0eifi9a/nKTF8J+nOWRCDSqvG/niMfLn2NeZJeWwHryGv5gQ/iCZhoxn2E+xy+VTUnivU5+1oJgFaLB+0BjwNuALkzW+jrgvPbr5KGgADm++9dwSM8gGeAXUBIA0fYCQg33/Nc23JiIFU1p+zLyyD2vTl9+zBywj9ptQDoIMQA/gIIEYEkBMZ//8bOz7dfRf/TxGfzM095NIYtyNjqAQDk8GYBZ4/1UQOIy2qeTTnQ89MDBKiRFs2suw1yBmj6fOhVXtlGddTM/Pi0q1cAZv44fz81nZ96QwHSBBgLJEPRAus+0mcOgRS0NkAGwCAgm9IoA6UeGOVlhAcgiGCgDoidVy/6RHw8finkPXJurlFfJ86KzHPmsr/wqzlDsvGPlHH9qzABeOk84rHu30fat9Vm7Jk2a0B9YMWvb5/9wfuzxD97iMVX3E//sOv58d/bGD2KtvrnAPi0CJumqD9B0LPQfq2zMyFAT1nrZ8392BYfrezjK9U+zqn28UESf0J9Kvxp8e9J9ieIV2Z8WsDvq/fV/OrwiqzXBxhi+3FjfMTmt58z2ftOqGD5PAWhNbttnInqa/X7OgSUwKDygnnwsxrWcxGdCeVB/8AHn7M/hvqcaqC6ZMEcmnX+Bwp4tAEg7J8u+1alwKusAWu7c8MYePMO7ZEYtff2KQOs+eFtZtP/Zmc2V6F0juV63suBrAG9VxN5j7sHNQzNfPnnba70uLCS9wXjNTMf/zHeXrVjrp1/SIungkAxB6zw4cmxc60DCs6Lzyll1SBGQXjOijRjMUv+3MTNbd/XkvDlqdPfSzTnxyteoG/VYx76zPu5zABr2t6cwjYoSM0/Xehb8/mPi9xA7Z/p080/zWXww4tkPjzwPyy+9f5Avddu7LFrzlqw0f153nfM9n5MmS/AHPD1bdK3/0uwvbdf/kEuINiDuQD/z1jfhfw+NH/sV2YVAHTz3F7/9gZ8awFjWy/vvhpeMBwk+sd6LvYQCH6wOLh/hil492+2wq/ZdWiBZgxMxzDfsQgSQ0nXRkjLtSmEXtkY5hCOj1k47XiohyGEtbJwCiZsDCVcC7VcwrUxHHUJGuA9Q/3L3M9Es0Q4TformkZ8DEZWruv5COa6FEERDk4iK4u2LdzGacv+PjWOMvel5lOt2YbfuvLZHC9tf3uzCQyM3GH1fv38bKElbNs3yJYre1kl1JBAzUaNKhm9weQBts2DUGKWvAnioZTalR5uo4G7l0ohmvswRLkVczmTe8jQyWiJT1M89ZMrN8WpDVR4WPfebRTiyaTIgwPjKbnLPGK/klZwqLaX8MqqpqyVmoWv02V1EPvoeIOgjjtT1qAo2iiqh0lc3e/OEuYRfiiJKSiPiiO5d1ZTk2tlj6pY05HYxbGS8PBur/Aij+7VUry5kUDovIH20SYmzzoWr1bkXpXCYznEWxjNGyWE3TEdb8OBYVopalslQffO3ukQXRcZ+IzrqeRMWyRshX3ExLs9R7hhnN+rSh2Fa8wf6Ktf3FfmWSd7zIfIiHD0yaauEzz42RmqIiNquES8Wel6VXXOSix8j5JIWCuM+/bMjUUokGFK2YF4d527LMJiLUQQHRx1sWHbiDVU9kaI0daiCD+7MriKrLdXzc31w6TuOey2XR8P8iGetFthWNJw6Gq21QrlIORRdwyzq+N01xtlx6dxhOkJ6+pMnZiTsI/JYLACdeA9jmjY8CY05nUQ87HtN8ecl5D0phRck1uBdrg2JOutnYrNkGB/FDlEWW35cUuXLuiLMDKemDEq9RPLpgSe5moZnQvsyCnWKGcloaE5vq0uLVzeL0jLry1st9QtulqJzUW8TZezqex8rSxUVeqOY3JOKVpbXisajyD50tV0Umz5uDoJ+MbiPJPfCVaz5I4+ezfKJKk1qehbae9SEGscDsbWGJP4tJFvOVkWqFGxwdRs5Eg57zOsgHbhNiw8bnmRCA2jRGKjHA+XSWgUdNsw1uqy8eqU1mm1YPkGHzUjbyDRXd4QU2PVbK/nAQpxLFYGzZAW3B3jXKRxBOiox3fDM7pegKxLx9S6vQpNxqiXYp8XBIP7mn/fkjtNiihdGB35ik31+XygWOqUe9pecY5j5W+I1Fk2VwcSC8k6bVLibpKsQPEc3WwbQ+Ba8Qy1/hJH79MJaQQ6XLIOU0B0e6YUsncypz2FfMuZ68SQmm4Tx6Ht9eL9GBVqVdfX03jZn/Bma6dBf04PZGFCHX+V9/h4JVW3bUdLimwzbMcNc6gkPW82yOhYxyJlHVHaHBO9VC2FckScsS/52j/uLreNA7EBy0LsZAQIZuoyF9nRwZD1kMlipR0d4+h706HPrKNuU67Li6iUcaUk5seSOa6RWgwERXa2JX/qCi0PWezS7qlLh545I9m0FCNDZBtxzDmOLTVpD53EgtCR68kMEjre8iQIEicRQlrSzOIurvQlwRzZ2lpS6njU4JsQcNvbWln3fUoTZrO9nFO1H477pRhkybpYcfZY74OBKBN+cxqiou5SOkBNe3VPVOWy1e+FpyZ9HZ60dihOBCqfLLor8XWki1sN38B3ssRFyrmcDHbdmptsT2/gxkpSW1aIDY2kbMky586ChCSmb4YVRxiy9XZ+vnM0YyfCEGVvTya77bCkw8xroGYitN+iG4TnyHtoEEe4UJBhdwsHhw85tBQ267LvM0qC8qi9CO0pSqN2vAVF61i7G1K5wHfYEc9hm29QXdzvMm6lJia1Io8TfqllTh0mfRcuJSeFtKOZbmJNuayoNVbbMT1SQSYWp+rSHeqNlzElpNRL5rzaRbbfhwhPnY1gCujDflB2eL9ro9w1S2Vd70lLvqlNZ9wVq+fXJ2lawbXrxMpBOq80ZiLV21o+Kilq3HaBhA0MviHUdB/ejPsexq7EAbFkr7On/nopsuNAmfu0HtUw1U/Z0qS1420IiXRFNTIRT5nBxbYeKT0Tx8fwKoy7hFNPubRWNhJJpmfDkfNsVfbrm2Ab0NW6G+KV8b0V1gVO7Yjipqid5npb9l6lRYzprBsM5ZrifL0HN6cShNpVBXM6Zr5eYEsfQgHrc4e9fzwue8XyN4OWlzuGhlOLvGA5wwVBwNSU451pfVUEKI8emCrHLoEFLztJh8gzse2gOCOXakkz3PnaCSXNGyZJ6jbYOR+d6AZtUMff1GlxUa61Vnaadkkuxx2394JU5U5N1vPYLb/rirgS/LE59QpwQtLFThcVecrecslhV2s7Ei9rVr4Y2j1KAum09QlkaC87yORjdzD1wNAEfWtLRruqsUMqRw5KlJTJagp/PWROdFVwc6CQrJjGW22s+8Zpt4B+4E2MLhP6GpO3bWLBw9IL0abQz47dBj11ERV+oOI82d7Q1kwn5CiZl/VojJ23p8+EewwcC6rLeOtfMXillOPxhppcZydUaPqA2Y7BmjkS++LGOy7XnmwpO5Nr6zpiK9BPua12sQxFNRRJPuYFsMuu9C4X+8iSWBMfNhdJ39yZ/U1BcG195S+CZbAsoTkpv+WyZdOUrBo1/rm+KyKzEXcj36XcQCxldV/q+yCtTqfC8pqNF3aRXPaKiYeNOyg5iChMk2Su23PGKZs8LlNgtsLZ4qjf1za5XRfO1bjkSafiUWuKQZHBtSxVe48UsCI0urU/JWgecePKNfkJLrxMKin1flndkG4YdBrS/FN5E+UY3xkrPt/lQetZSp3HmIWwFyt0s1CzzuJpd11mgnIgzoLIEJps6pE+usSNDi/n3ZTHW603leO+yIVoyH2jim8XYy2yQoYOJyXjhHUBu5dQ8qIVr3aQtQ/Pe3ybrgiISRAs2lTRGREuwy733atDB0JRRZtd1sGwa3YC7WdAz/UkUcdThwzaKVxdQSugeQKaNAg8cIkT3gVtXYi92U444elZmLUHmWZGgxw804q0Nm2D2xrF69KXU2RCTlZ8ZBN2SsbtnlHPOUv5GxOPk8yquYHLWC26J0KZtmdsm5I9ZERETofpbuPvx3DcI3EtcJIGesmdfYtK4wAY4VpVbgAkk49BgTCTAa+kWkGuWhLlLE8KFXWybfkcw6d0bQlnez+osB8bjlL7oBc89cXhyMVtLkZkORC5Djt1xLRiohOykef6EWxMNLkDXGNgVONzMQZbPO9PG9tbCkUboDGyF+9XVxAJ4SJVyuaWmxnGyhTtqspKjf1WTjjJjS8N6IKMk0qVWXuvBfaQwOEFtVhcTGwNtHVW0hyCQ3FH77jWRLVtHo9bSKj35i4IY33aubelsZT2doxayG0K951SqNwlDFzDF5LtsCcUoT8xElxgm3POMbKwthJZC73Eu2TTwbfPg3NopA1XQ7fr7R4cFbpiS+Gy9iNN2MJWJEslwjQStYbPGz5JVlZy96wE2XRBe40Slw7NSszvgrHBhb2VbpDrmlmytkWmhLwyc+EU4KGdk9euzOEtr102peTxqUItjUszLfUhoLrkjHK0Q/F2gg43AjEaS3BIzDtsIQ4PoF1e6verdB+zGkeLdJvFl4OrX5EJErPjTsaJ9ArzLTHhjKZYTtitd+1OLesErrhGxwcNZbilepREFllOyt5dlhgNC35LH8RrPHDM7tAEN7FG8SO0U5BjciZUqNjYGnvlpPsKi6ewBps1YeAPx8v5pPP2huRD1dFESd8dmNSFYarXD1hZj1FCW1p4H9K1QpF6FIaVsh6jg64hgBWTnnISqi4TKsFOckok40oF9LLMj2Nax7B302xawMKtFSe9uWldSpUGKXQPRqnWmcuj5y0l3WVzKXZ9GeqQRVO0FOryLvEgbBxr3xo2u86dltahwxooy9mG50wQvCYJ+jAsYMEOYdCSyaqju4jlJeJvqF5U5TtPJdW0bfUR9F6O1BMwW68F0YrTNVNImrYpehMWBuhGxxdggvsA2rea9ZD1pShZOdxXu6a/W+XOZPuCOoYKZXBCVQ/HeyoZ1w6JHbEP3S2OyxgmbesEwTsB9JIweVXKPnNyNgiqIdOE4QavwkxHM74PLwfQMfT9NRt7Kk0iQs6jYzBoel8GY5ncpZrsSxxengjaIaXz1ThtdiXXZRhNY1GxCgyyE9hNqxSr8g6lKh/1xilp2QTUXLloDw2/ZBjxSBbkyOL0CuJ4itdySWZImTClvVQqFYIhbtXF6V6NPXfNKxyjZqxPyMsldCBu8s5iwwHP7qV53RwJsuSnUw3ijTkzVG+wgr0J10pu7ww1RS4F2Lsk03kjm+flLTulGYRD9hmnjd3JrHQipAg21rn40Jh3/XyLkIiFT82ZxcdIKAcharcyBPkmBV1NylpNFYMXS7lTEcvPiybOIs+lcPy8IU9Eau3O8lqfzESoEDSlhiw3GC+FdbhwYZKX8di6YxhsIBgBzIB6XHHNdM2ne3yD9N4qoRF9hED7F3O5jRwqXac8DTdXO2JX7xhdI4n4fkn9De9113RApD0nqWteLq53xFp2l/UahSqv0WB7NZIhxmc6dVjyKIcbhxux2tAWcfFFOWDvjm0EO3wFF5NsmFu7xELKbqwbtL2FReN3RhPz/uDWG/qaGTh/VrzgREtIdup4uO6cQz+61265xwaCwPwrCMMeajsfwpgzsq9ivFetA75k71RTHBjD7FpEo92wVhI7Ytm9DKuquiMjxGZzaRokpo0Yy/UnYVCy2PUr+nrA1lMaNPs4BD0ittkqmXkevROkCRmUxEiRpnBqp1jMcPi9lD1AaWdvWGOcxUeCgOi4PXGZdMQdxfAcySPOwPWOcgKlD7nsaFzpLUVY3XloWcHgQ9rhgYGg/Y2pz1e7qY83pceFNKXEYl2fB14fx12B9MREmDA+rjRfZ671KJ9kYhlenEpZKlGHI8tqZx9PO5pV2Uxdj3tWHzGJR1HQnkuTtBQUYxuU5G2TK5rKeSfzePNuXmdZWYKL3GWaymy9Clu4SU+827l3rYuPIxrGmOimdC3YUQ2xuJtfMZBWBqgHYLsb1nLvpjrOm1g9uJeIyq/c8UqjBJbbihw3OujI2yIgc5yVpOiqclOEgZIonqsLfBfQYTfG9wjZGVKgHwOuJOgjVbgHMc7O8M33ISI7Q+nSnrDLUqRVvuiuIT010/XSdRcucrlCwLHTbudMHWUzddpXE4oaOTdWhGVgrr+MwxrncbxsbbyN7oXdHGr5gsamNsG7/XCkBfvQNPxNW1aSGhVRcE9hFZZJHrjP4vF7lY+tlx150p32seiMduetAa+ul8v0fNvBnH/vMzFGHQ9xT4U7LK9yqd7aWtLUrQPjHVJecNoKsmaNb9uoR/M0k4KqUcxNWGZ6P+44GGEO8FK6MSmTr/PUsqom7273lN3ge2h5wBNRmG4yocurOwE6/xb0zdUOPd1XqEhP613KWJOtxqBoB7fOLQlR9OAKm1zJoVyoudLSBHho6SCt7+R0jURF3DEIHlAEfLDuzWVF6PEWv6fJeT+YOAdc7uqxc6U19NDYN3eTKWPZSyAGPOiKrUoTb8STLoPqeohYpI4Ur6ZyNl4V8KGEJCTUQiyUC6RtLjDNbbAVg5PIBKd6gXZ6mqOp2tL6gKk7z1TWrXJIj/Z2s2ccgTgvReJyXZcUEbuuvLRUf8rwi3brRTOStrYfJNvYG0xoezxwxc3L2aPhj7JMEN2gbVXJlbTDIXbGkx2ThzzHOQrtxmh7DifyYLT51Kv2rjgUnGuD/tR2tuNRDOtp6l2hkzoyqhC9hUC5zDerUx/p+5BcRzttJTAu44cb81qyteGDlnIcm2mVQ+c7knZQpFfXRt7hprqL+lVlIslS9a1dzSmnFJVz+XSjmz3lWQho2sypSqnGFdu7nVg44atiqd3rk0EfdqdYHwj7dnMvCKKAXpvnYuNEXgj75Hm53WWJgGflGakEFd0o+nSJ820p3a57Iu0I1GnwDuNiT0Fjfrid9r6ArYnm2qcbb2kSV0HZ4pWEmnpb4EYben6cKXzm2qDJDQmy7m4N2nJoh2PeRUg6Yr88lZvlsj+4hOdEtA9KNA9RjelZ1kl1WTOPYLZNmXHN+0dGyGm/61AIspbYTlq30bmV7ku0R3J9Z0rMmkBQjShdShhpVKhIJMFN7WieD0SZLFt/RY94wSS6Z2winT5wll3lgaoLU7XpRyq4nNxrAsqOFVTLlYfKB3yl1X7KKJXeqVRVoJqMpUsGFoza3R2Wt+3dwlFseduc7m58RbcVNtxXwX6zsbN0f9nKBokHe6T1Srev10yzMjumjxHSso/ouT0eMzza3845WlBX2eNrkrSZy4GoLeWO3sTcGy7+pqzQ6sxUYluSkbWkbbywnRjVEBsjXAxaSrmf01A2oks09AqU5vtzu6sv50MWqKeB2qY7eyw4yC40p+BUF17BlWOeE4hzGRelTuzgwNOSi1EYSfQatoPptukQa3JseLQlIsbxNBvGq1LbVzxlSW5370nluGvXReB1266LLH3vknEHTJ6lebhy6dMOT5XTZn1SOp8rs61lbPdZVEbjGhotsqAlZiNrK5ucimKveNKK4tVpZV/s+GApsbZjekiU8cPezS6esHPqw1SCygt2aorgrEjK1tM+2E4of4K8o0ej0cWsdgGVu8mevHn7E8m7K+0YLrfOsSZFV+aujLNNMyHvmLG2BuzmQ9RE8QlL1hs5OxN7Diqjq5WvtuKkLHlKFyjvvCK8ZY+5RKT4vEp4d6g/5wM0+GnMrtfrv/3t7cPbfNr3OrP7H/5GaD7v+H927PI8Ifl6/P84s/Is99NjrU//U4F++fBWOREQ53msVCdt8DqG+btDpY//+qx3njs+f3Lz9RjyeajZWMH8C9S3KHPbuqnGL3WePA7+wQy7recfrtXzbxsd8P3HA7e8Cb3q+aCeT/e/NPmXss0b723+Udl8mu+5kfXtNngdsH14Sx+/W5nPomblXmfGQCf0ffWOvv3+fwFaH0xDPiwAAA== -->
