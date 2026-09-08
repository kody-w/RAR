---
name: "rar-cowork-cookbook-scheduled-brief-process-customer-returns-and-exchanges"
description: "Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges", "rar_sha256": "6785bb1f5c23db6c97b563d52d4d7a7641663c94452c87ff3660ab3770e61f4c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and in the RCI capsule.

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

Process customer returns and exchanges Scheduled Email Brief — Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges
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
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 6785bb1f5c23db6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_customer_returns_and_exchanges_agent.py` first:

```bash
python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py   # or on stdin
python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer returns and exchanges Scheduled Email Brief — Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges',
    "version": '3.0.3',
    "display_name": 'Process customer returns and exchanges Scheduled Email Brief',
    "description": 'Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-process-customer-returns-and-exchanges',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b621ea25fcb00d78',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/process-customer-returns-and-exchanges'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-process-customer-returns-and-exchanges', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where process customer returns and exchanges stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on process customer returns and exchanges for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process customer returns and exchanges, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.', 'example_request': 'Draft my daily returns and exchanges brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call for a daily or weekly returns/exchanges brief covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefProcessCustomerReturnsAndExchanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProcessCustomerReturnsAndExchanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefProcessCustomerReturnsAndExchanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzG9uS2HFHRQwgJLEIBAItpCuc7PsidsjJ/z4XSa+dWZXVPVXdn0a2QwjuPft5zjm+/PpmtU1YVG+f306elS92VppGoVctrNxdsEVfVAn4KhIb/Fs4Rd5Ukd02RVW/fXhzvdqporKJihxsZ9oodeuFtciKKo/yYGFXkecvinzhtHVTZIBm5TVtldcP2t7ghFYeePXCr4pssRlzK4uceoHg2ILTjgvXaqyFXwBBFkHUefki9QIrXXh5EzXjh4VbWX4zU1p4mRWli6ZYNKG3KPoc8PmxtjrPne89l31Y5EWzqMHenz48mH8TZKF7VlZ/rDzLHRd1m2VWNX4CqnmDlZWpV799/vmvH94icP32+dc3J7XqeraUE3pum3ouM6t4rArHq2v2paX2pE3nLveuIiCYgguwsxyBsXPwu/QqoFwGbrnASK9fP9Ze6n9Y/Pu/J71VBfVPn7/ki9fny9v8R2vzh5pNYdUN0NCxSsuOUmCRTws67a2x/p1qNfBVHnx67vxOqSgXf5mf/fhk8inwmh+/vBVABGv25Je3nxbA6l/eqna+/jRTKX/86VNa9F7140/f6dStHXtOMxMDUn/6+vr9IgsWfl8a+YuvpyPHvnhVnhOVHiD+O/3mz1P0F7mXSb4+F/9YlB8Wf0551ucvQN5nNNqA7p+TBTYAO98+xUWU//jiURUgsqzc8X786R+RBa52kjSqm/8nuj8/CYcgnoC1XiYBQTe74K8L6KXbN5r/mG0JAuaf0QQsf2f3zVD/iPbDs39DOo1ykIrvvvxTcn+2AfrL4ud/qNt/tuHDwv/ytvFSkNqVZafe58WvjxD5+Qf3+80f/vobIP1fkjkVbeU8KHzNrDzyvbr5+vXnH+rH7R/++vMPbQmiGCT617ZK/4zmn9n1wecPFnyt+vGPewF/I09yADyLbzm0+LUo/1f126fF2Uoj9/v9+vPi95k4f6DFrMQ706cJfpeNNZD1d3b86e03gEY50KZ1Ho8Bfvzbvy0OkVMVdeE3i5NTtM0COLiJMm8WXg+jegH+zqhRecCudQQM+1oH4n/28Cxx4S9++d/OA+8/Oi+8X9bvOPf1geVzvsxI9/Ud0L++wOYrwNSv3wD9l08LfYbiKgqiHEC2Rh+PX3IrAPA7S1JWXu1VMz7bY+N9BEn+cb5YRPnil3+N4dcH7U/l+MsD3KMnRmosP+NjDch9mi1xCUEReertzGVj8JwWsE0LB8joRwDsPwAL1UXaAXydrVYnUZou3AggECh447NwtPnnmdgvv/xiW3X4JX8COrJ4VsJ6CRZ8E2fx8SNQ1k+jIGy+5J4TFosffv3th8X/Wfxnux7EZx5HUGxefgMSCidFXoA8bDOwDLgUBAEAmYfffv3tZXJAZi5/wMuRH3nPzSCOE899t/9pT3+EMXxhe8DuwOZZWVTNXKyj5tOC9xff5AVM50dzHQmLulm4Xunlrpc7I6BqAXW+WfJRWkGw1j4oy23tPbj+YlfWQ8QMAILV/LI4sEdQtYpHoa5eVQxsLvIImP9bdDzvAyLVD/WCeSfxaSHPkbsorcoqw8p68fCtp1/mHuG1HRC3FrnXf8nnku3Npnqk0dM8YBGwjPNy6cfZ56ClATU/d+t33o811lxb9UeNrb7k9StFrGp2hQNKBmAatJE7F47/eIVUHRZt6j7sBySdKb284L688ojBV6vwX3VE3/qLBfdobh5txuJLC6/W6OL/nz5rtgi922ncjta5zYKTde329NTcaM4effamQJCHhI+s/N7yvMPaO7p/ydMIhF01/sdz5cO/rzVPxGwrIK1Gaw/6ILiACjPdR+zPsVxVc9ZYX/L3MgK0WDwwE1gXAEXyVPad4fz0XdIQoMH8+3tL8YiVyp3tAOJ7UbZ2CmLP9zzXtpwESDUb492pIBG8OZf7MHLCP2g1ewLEG6A/uzgCvgC2//QN2p9P30X/w8Zn5zRveXSVLUjf6kEAyOHNAs4e6qMGoJjVPPt6oOfnBxGgRlY2s+42SCCg6fOmV3n3NqqjZgbLp129EsD3x/n7qel81xtKkDPAWCAzyhZY95FLc6xmoC8CMgA4AamVRTnoE4BRXkZ4ELSyGRgA8L5i50nxcfulkPdIwLnAvW+cFZn3zD3DM8ytfPw9fuh/FiaAXjavePD920j7xm2mPWNoDXAQcHx/+mwuPj37g2cDsnin+/nvBqcf/7nZ6lHxjT8GwOdF2DRl/Xm5fFbp9yL9CSDY8ilr/b1gf3yAwsdX/fz4jgwfX0b9CCT4+A0Z/sDtaYjPi39O4j+QeGXM58X60+rTan4kvSLu9QEGYj8yt4/o/PRLrnnfURewLzIQcrM7R9AhfCuR70tAnQwqAFFg8bNk1nOl7UFxf9QI4Jsv+e9TYE7Bl54fgNd+Bw2PXgGkw9OV30oZeJQ3gLc7d6GBN0+Dj4SpvbfPeZumH94Agnr/2hQ4V7BsDv16HieBd0Cf10Te49cDSYZmvvzjYK08Lqz002LjAdRK69+H56vuzHX3d1n01Bvo6wAOH2aMB+AAIhfoPTOfM9CqQUiDaJ71a8ZyVug5MM4t5qMGfH3WgL8XaDPXjt+XiRkU7y3Iyg8L71PwaWGcDts/pfutr/17ohfQJjwqSfF5rpgfXhAEvsEs8mHxbawA2rwGvcecnrdghv55Hmlm8z62zBdgD/j6tunbf1bY3ttf/0yuuZz9vUyaV5egyX50zM+K14MeDhjXA7HxdMOj8IG4fVbHR9b9qebvmfmP3QsC0H0kyTvEPIi9LNp7XuJa43vNB0WqWRBW9iesAK8HSINSNxvmu8W/61085rpZKmCn5vnfEL++gbi05mbgFZmvwQAsB5j2sZ6bnCXIZ8AQ/H5mHnj2PzQyvKjWoQWaU0AWJ0jMttc+5sCIa+MORdgYjrgY7KIuYRE4usZxxKFQFIMdkvB9BMdXlo0QxMrD1z7qAHrPrP4693fRLClGEf6KomAfXcMr1/V8GHVdEidxByPglUXZFmZjlGV/35pEuftS/6nubNtv08tsppcVfn2zcRSs3KM1Tz8/7JJa28SNsIfmClV4e6sTOm00KRW4tT7uDc1DHHcnBvqNckvu0m+95KQIu1uZtPt9VVy3dAXz12zXlQcSO6wOsngpEVv3O3g0e3SLKJOQTNjygJmk5WE94m23WTGmIuee0/SyvvBqel4npsmW5VYlSEXWZe++ZfxQS87rIhKGpjwPfIoa9fku+EskziFhuz85Wlk0zfmuDW1oSvu6OoWrqI2yvtJzr0QOZijaBNpjfkQcRznaqelwKip1T7tXvDGEXdFw+P4k3jGYG7izkxqaYO1u8Vjoa8MSCNbeHu/y6VrIG18+6kIkyWK6jYhrzGaTd4gkV7TrpiwupxUHXyjEKSOsJ3cTscSwbqozyO2mFbGFbfCNLPvhXKsbQlnRwSrE4bu+vbAbyKrhg6VmDpEduOV9h6CRrkRklcgrJclDM1BK/XjlzgJZKv1NxRlWDih/whRTuR787dFUjuIWJ+8ciwZaTuPwoVhd79nYBznXnCpxJwhy3THintJaDVcuE7qq5aVGXDNVLbhhE96U/UXbaRvaRq8RpCuMWpWWmG7EJc2RGZOaaSbeThgXe7Yij6spOVji3uSytWqrvacqhg6nCZ4P43SsLteb4qBn6bwRrEi6y1t+K/WOFKVB3LkTt77cgjt+51PksqVJ3GS62MdCw/WirNpxvrFfX0L/XsWHO2Yo+n48H9NVa3YnBBk46B572HivefFUVx1vqTlsjzYfQdQkRsdAS6zSqG+IvhOozTFe6cm6Ka6sJcimyZCU4Wi3XZirzCYKHW05ab5034ZNlplES/sGm9zgrNDxtNhau3VJZ0sTzGGZMIruoKRnUbf7ArZWk1JEZ4GlOMYnC4IxMIhPWjITxeV4vp6QoRtCVzzGogzRHZJsek3iiNAZd4xJnjEtWHUwVfksCp/Ny5WkkhrjL+HF8/bw1cp2p3VeqqujsbQhy8LjsTntAjHRsFA96EKtojs8C3X6uiet7kRy6LAeSCxeDjm8SSTSZqc9qU51vhrUpY7Acu+IxIWN0Hw0xB408NvQ5C4uLAoBQ1+cM34+THWaKM060Flu9APtFuWUTzt+r9OwYK4O132d69MhzznG1AM2QLFNY/UIyAheMZhQFOHe5T36bMHxRYVpj+G36+WJVidSbwKaCBPrhKzKWqowBjtmZ9iMo0Gm9jErOmJBKl1jW9k5XRNb9VIXNVuIEn1ni1GkY9qU2cLaVcKu5XSMRWOEXdZUVNdkYne03dUlbp3Cu60CnfFlTmvxBg+b3CHgm2u267U7Xi/SGtMZhUejAKYBwOSbYM8RnLPNriNrq5XM9b6rhOmeuGf0lgqqNbs8G5eQCxyK3SqiLt5F3t7C1PLq0KdJvYCRL2GT4FSNqCP124sEKVEDuxsh150johOX5MykRu1JOo8KNT5oPkGfFII37jR29lY9d42Na8IWSbwxtx4udYis5UubzSVFVj3czMpuMLvsPuUR4mSCamobXimQmpNuWrq9FizRT/1W0Ye0Qq3jLhPslcLXKK73t5DE64O8Yovd7jzSskVxqxQ+9aZAaZxF3pFl0LTTeFsjeE1YtCAuY6i5x2dzA2VY7w4lfT2T7TVE9anyB2TCzdTc9qncsV7Rom3t8/x4d70V0R4i/7QUwinHmqN+avFEHzfhsRUOt6TUrDg2zxTf6/E1OFNwIme8dAhklWykg8Y3qkr6pSMgF2mVMYIw+tGgkmw2sr29O4UkqhwEjj7yJynkRXEYwtQcWBuFmrN9heU9TWQGs530VXi/MHEot2kkkMJOTk7rfs2xdQCv5WXK857BHFO2E2BD03ZQwCYnM0Nwr4cmTUxllOHOU0gJ7aFOV6mLwjGkoVHEGLK02xSXA221lCut81HopQB2rlt4VYkHWJeENFZYnVCW3abAoKUdxbxwKnz+gK30FaRHd01UTgRxWMEDpuLS9jBG/KRQy2VtaEm3P9YFs0ZGkb34y5g8jMZyifBnqSTJyCbwguCqmgwrPs46fwsNzGlfq/bN2JMb+YRlRnQXum5bbW/mKrBq9KgiBivrV3h3Y6vWDy4Zg8YwUbH5hg+mcD0qfo+XWSpfBDKqOLKslJbsT2w4ihuetwxHD21dLJuxTgPUGYNqb+BMkfK3yT4ZB35VbrDLpC2rLujO4hBeb+sNT264/WZpDfcUUyrFy1rSb5xzWFtWfETqG7cNuY6vq1FMUFXx9c4QUctpJEY6R2tzGwyddcSFKb+E4y2QzsvTtVkdTCe/pbJBL2mfN1Qm3HA5XEDTeS0PeyThI2GFQacQDmp1dyl0w512DjPciSqBVQ2p+OsyS2qrl1DxsCttqrwIqXpSGKN/ZGYl3sJpK+1Dk7pvOcoQ4+3q0J4u8k09msJwwtjqfFVceynl5khXaCVJjBnCeowyKqhoKHbkelXSUEETzBLa71a8rJtcxHhmT+fnteFqWn7LLG2tTgEHc8ebEVxb61Z0VJqwjjO1Gx4+CCqKMPsbMvjlaTSEPVqkzKWH6b2c9aUaQiyUn2ONk5r+RssbPsL2No5FmXlvRTDZpWdb5j2lbA9MRAPrXfF7edoOqIKF+0GuIRFAUaCTy3Ls6exe0tQ1c5O1TGVrpz4c/KwWt4x5OF2a6AiznqaMfLK58xy9jndlXO6adR+qem2cRR49WATkn/xJ35ZDUuhgVOhXO4JjjnU8RYYc4rbe2VSC5rctrBa9jUPjXXKpnb2jA2JFcbwPD/4xNJKAc2Lz3k3MNjnpGGftR/2sqKcM9fYy7LR5ibtEJJqGE3bbMr3zkAVBzHLTJVIQy3B20u4OFSZJnLWqwFh3jc4nXLzURm2fExBgJVtzVrph4aHTbrB3XdLXLUvJmLotyoNsnSysXxmmDZU8RJoCeZThuw+avsHJK9Q4tFoV04hS8TdvT/sYO4ki3WsKJYf7WLA8+CrzGr1y8hJdF8vcsQ44EzGRn3abDMw5zuqqlvSGLtJaHDk8La3jWO1XDEqad6pSGyNFNm66RCgkK67rNJjcUvFMLYomd9Lxq1UqLLUZlevECmdn2KpGsodpbCwQorqZztVHfGdlM8e1B5Msl9KncX2aGC6oNM3kRXVIjPOWWEulrmykLU3h1RiRKu1iU91Gl2sUrQ/ygVp7nMVcYqvYWFZaml52YkK6ZThHF/Nh2NcBzaCHKXXVTQKdz6erEHZVospptqeyg+2ITSzmPRZwEEc2HgQdiYgyGup2vyuWk2FirjgKDqiyuMmdPYFTr6G1R7HUYMm2mrJGaYnQSgmjCyyRCLW9QSItRRauZjAX8w7TO2EUbJTtRa22ZHgriFFlW7B0rhC5yPA7dmnNNXf3abUQWcdlzc3e2QfBLjx1h/BeYc79YByZKQrk410VpFZZRZnc79VJ9PYYmSen1omFrRx024nXNs62aqQ6THiarXFW99XB1w6ZUYmkxN+ODYNAR+pOTJeJ66s1FtsILRrpTdBIs9Fw3kBbakB3FbFqT7LA4Rbtme5VkpfuHW5NmdJXPSaR+SbZ9ccsZY9reYQatxu4LUSeaiWJQ4bQEP6wJbttijAyc2G3Rz4wNutxXxGbVaQFzUANbnoPgDEFAd8WxPrs6mSg80K09wQ2xTam44cXRaGbumkMMkpO4onlV3rgrJVRO3Y4csJiCy1qAm4jdrUXClzXAH6SnGEjkkVcu4Cocm3KhaZFmDheZtGdK3ZRfK2mHYRXuFCzTjwmQ9/vaduSbkVpm/e15hVHK9CPkjhtm2Mbkl7Ut4bAhlwZy0TVOKVpedId1nR1YxLx4RQUleklK1td7lbrEa9YIGop3Fh7ye4CrpJYNSM6V1lCclfkoIvl7nf05mHY2s7wuE0RSe6IAs9l11gG2jq6btoTD5+juuBwl4mau5saRSKijH7Ib2EPHzDktoaJK6UXAUYfTtKhu0E2P/JUEuh5wuwuyIZLzhwR9Pk+N/HSLs5QzWANytmh2qwFPdnT9yV7sEz7ivm6dNPlg3PJChE6ZWd9IkP7IoqOJNkmXgS0mK3iypCqzs2cyfCHkLIU0abLwDNpO77XcIwxw17Yg1G/OMOnNXx0A53w2JBuVLaxeE6oEpIQNiQjNgElK1PBL7GSPkhmkXCpC2lVr5B33D5LVtjo7ACmP9I84rSgXVDikvKp5GGI3HaFeEAE65TK1O6yGXEh6myv4UFRvIrQYa3tjrSo+oAc7uy6Zbw68lIsmGnn91rNpjwmC4XRHqupuVSRtZXkVA9cgF8uGOqR7TSk5gUj4mJYeWcHX94wK8MrxN1B8OZ2bhQX48W8goxUZ83WvhG7JQfFq/N+hLZK36xN5ISwiBQOSxFHmL7i2aVtXhGqFAf4Mp32LeawVXHNTL/pjTNiet29Io7qzmtbFBUFojtK62AtHVbYWZZh07wPlI3waDCwmRiVVO+dLlfDjUeSOoOBTbwSDg/vDkTqgulYcTw0gTE48TGb0o8Fe7pMVl4dqdyXLEalWbEXTpNiquUtt6uT17XDcCH9CLegJRhuExNrckZaHTEwHHedS2lR2PrQAeLxaWV0V7iEzy4CDKdvKflo2oHBESbV2kN/1OHldD0uIeYIi3FSTgCclvhxud+zt0OWl62CuRdZkq2U6zHhdHbv2nitxo08dWrqNpDu0J25KrByqd5XlleuWmFyttwRChqBy4jsiLOsvscOoicvTSFfpgWyLS7VUheh2050fftaoEdlWJsk0tOKet/jV96cQG+uXMnTbd9uUbRblZNzaohMgLkGieKgTxhk5JftsKbWa8wNd3l3AI2VAF0ROzlkNzACyPxNLJkqR3NJM5cr/UKdZcIiB7uvpLKCCSEt3L1aKG6x1LNuTULlfk8qV0VfgcTmRp67jqiSIkgVVMqE+Jx23DaEffGK0xlUYME8XDzYiy1rnw7iVqUmvKJXTI0OFDfBkK+1y16BkTBBWRen3MGOZEgYMSMf2LUycOWpZAX5FnNoXU6hulavbKDhWMxS0AG9Nqhqbdz17ToVk3tRuTAr4ltfHKRwbw07Xwmu3EkqlZXAo6BuMj2V6avU93akUISUN3WUCWZdZNlCBAEFV8k6BOYNkzDCrslst1vjR+dkCU0xMMsDcWRHHIy2ZNtj6QGmrz2WYylFTMkOmyB6l9tdQbRVbbAIZ+/ibB8XXZm5WIRqZUqOdkaz5IV3xmpj6wcDu24LO1HgWMRsa2W3dQQmO6Jo4yPTSQgNg+aoElF2jy5JJWiuSJ1DpxPh92Rvxx7SGSTrrNcJDKdkLtOts0Nv8Ih0GrGjGHgtJQdFd6Arh7ZZb3rx8XaDbjC93aUqTbUYiQs3dZ/EIHQv5qjsIikmPZrRpsRYn2ojAu0RYW2RljeoXtIRGy17kpdTQvUiErZMiNjkSH6FK8svYN6H/CpajUS619dUZFYo6fG+3J38e4ZspqykbLxrsbKfrnBedkhwEQBmZFnsH4OuLCmeseU1R1BSqJbVdWWnPm9aFnGX6J1/WIvkSrp5ztW21pc9ZymMRWJrczUi9rRCcu2Yj1cA/76s7XcX/3Id0KRy+IG9lREZ4kmqdReFyq6bWtDu56VTHdvbsN/6A9keaOkSuvQAaTdDc+/IineZVopXoGiLpOGpauK5ea/edq3GI6dglJEir25Ftl2t/J7Z7lclFa7sbLfEY8cVlvydMUks0CU1cVNn3Ba3SVquXWJ7lGlK4Q4I7RW5fz0OKismesAkbt9A921ucvDhuMJ2oNFAMeNYDdMFoMvtqDXlFTsb+7I3Yhvewhcf3zTbE5NqlcFT8BqVgE0UyoPrchw6aX9qCsS8tH53P2/FEWZlb4izUUJJuTpeBNlNhlaB4tue6XRCN8sB7x0yGM+9b2zbS9R0kZNDVORIfOKkGqQ0ATLZvXTDaSTFh53M+wJK7y4hrgedywaGu92f0zs+sohr7dLQpw9InCcK4yF2qw7K0Pl4M4gu1JV5FE6nbplEcpU7y+li0xDmjhDoBQ7LkhzqDXTnx406MKvAN2kCDQWLcQYQ5sf0ijTLYtBzyhgxHLreJLH0Ghg9bW5EY7sWzhMNiGV91VX9aPSeV5lV12quQl0gUP4Tp6DCC3VL0BOoa2N+2cYDGamyJ0nFdbdW/GXkNv1lXXS35YFNEN8rMNvwnXhQSNCMDIyVBY6QTIl99VRiPAldVY8euva5G8VHnHrBsB2/5WsZHTg7QtqlI9E04WZVjwpKZ01aQynTUYRsfEfAKu7zSJ6BoRxeGjtqpwQ9vBrkDSxu+va+gabe0q7rpaNdkTaHfAeG8Fz3yw0cAIA6LxMFWm7daXChwIcRmvBAGdFqLzbbI2uGGWmFNoxfV3mQXCysu6CxLfnrM+0i0PmkTU1HHo9wGu+riyX3R0/vnDOEwUQMCstuknYt15HT5tJuQE+oQtC628DsrdXg2guXwqpW7B2RAOc5Gyi+M1LvNCyYiRCn2rcGom41dlviN54sj3WYocd9ihitv2sZtTYVHiN4cykUuzWNJxut9xSdDDkVv9j5NZf2jswxnU/s7E3HEn6DLM1uXchM7O+Px1Y+NMT9jB3F3FGhtIhdl0jrLSX6h4G7YIOEXrJol+bqdqVsNG/vOkhMttRSQ3or2TT99u4u66ChVqd9LNPRYdUF/r5AIYjOGVhyw4LKsexqB6S38UsXBCepMTRN/+Xtw9t86Po6Ov1vvuc1n9H8jx0VPU913t/aeBwmepb7+cHr839X0L9+eKucCIj5PDqr0zZ4HSn9zcHZx3/t6H6mOT5fs3o/Pn6eUTdWML+8/BblLiBQjV/rIn283wF2zEUxn7V48fj9yenfKAzuFJUL9GyKr45Vh2/z64fzqxueG1mN9/oZvI4YP7y5r9eLviI49tWrytkAr9cBgN7Ip9Un5O23/wty7IkwdC4AAA== -->
