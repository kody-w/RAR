---
name: "rar-cowork-cookbook-scheduled-brief-make-payments-on-asset-leases"
description: "Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases", "rar_sha256": "89cc5bd78118b4a368553fef9f937077d4333560f4518c0fd3013e59d94b5213", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_make_payments_on_asset_leases_agent.py` and in the RCI capsule.

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

Make payments on asset leases Scheduled Email Brief — Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 89cc5bd78118b4a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_make_payments_on_asset_leases_agent.py` first:

```bash
python3 scheduled_brief_make_payments_on_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_make_payments_on_asset_leases_agent.py   # or on stdin
python3 scheduled_brief_make_payments_on_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Make payments on asset leases Scheduled Email Brief — Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases',
    "version": '3.0.3',
    "display_name": 'Make payments on asset leases Scheduled Email Brief',
    "description": 'Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-make-payments-on-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82721e850e1ae81d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/make-payments-on-asset-leases'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-make-payments-on-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where make payments on asset leases stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on make payments on asset leases for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads make payments on asset leases, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a', 'example_request': 'Draft my 7am asset lease payment brief for USMF and email it to the lease owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly asset-lease-payment brief for the responsible owner, drafted as email and a Teams channel post, not sent.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMakePaymentsOnAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMakePaymentsOnAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMakePaymentsOnAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjxpbmX9G8/cF2U1WAWATVcSMGCSEhsYhFIHA5yuwg9lUC9/3vk0h6q+x7fXvGPfNpVFEhAZlny3Oe5+Sb/Pbm9F1cNm+f37TAKRY7J8uSOGgWTuEvNuWtbFLwVaYu+L/wyqJrErfvyqZ9+/DmB63XJFWXlAWYvu6TzG8XziIvmyIpooXbJEG4KIuF07ZBt8gCpw0WlTPmQdG1i7Ap8wU7Fk6eeO0CI4nFVj0twhJoBkMjJ1uAYUk3fljcki5edGW1IBZJF+Ttwh0XSV45XvcBWFnmTpYE7WJoF10cLFYffWdcNCXwApjgDEHjRMGHhzdFcO8WYBYwt/0wDy4WLRgwm+w3TtgtgtxJMqDpIai8FSAKVdaD58DX4O7kVRa0b59//uXDG1CfvX3+7c3LgG9z6Lw48Pss8Nezz6KTBqeXn3LBzN4Ls/NzzDKniMCEagRBL8B1FTTA5xzc8kGwXlc/tkEWflj8+7+nN6eJ2p8+fykWr8+Xt/mf2hcPI7vSabvAX3hO5bhJBsL1acFkN2dsF03Q9U0xO9eCNSuiT8+Z3yWBgP5tfvbjU8mnKOh+/PJWAhOcOURf3n5agMX48tb08+9Ps5Tqx58+ZeUtaH786buctnevgdfNwoDVn76+rl9iwcDvQ5Nw8VU7bTcvXU3gJVUAhP/Ov/nzNP0l7hWSr8/BP5bVh8WfS579+Ruw95mVLpD752JBDMDMt0/XMil+fOloyiEonMILfvzpX4kFK+ylWdJ2/0dyf34KjgPHB9F6heSnD4/l+2UBvXz7JvNfq61AwvwVT8Dwd3XfAvWvZD9W9h9Eg7IBFfG+ln8q7s8mQH9b/PwvffuvJnxYhF/e2CBL5kp1s+Dz4rdHivz8g//95g+//B2I/t+K0cq+8R4SvuZOkYRB2339+vMP7eP2D7/8/ENfgSwOnPxr32R/JvPP4vrQ84cIvkb9+Me5QP+5SAsAG4tvNbT4raz+R/P3TwsDYJT//X77efH7Spw/0GJ24l3pMwS/q8YW2Pq7OP709ncAQgXwpn/iGcCPf/u3hZh4TdmWAMo0r+y7BVjgLsmD2Xg9TtpF8sTIJgBxbRMQ2Nc4kP/zCs8Wl+Hi1//pPXD/o/fCfbh9h7evD0wH0U2Dr+9I/rUsvj4Q/usD4dtfPy30GT+bJEoKAOMqczp9KQAKF91sQNUEbdAMALTcsQs+gtr+OP9YJMXi17+k5+tD5Kdq/PWB7skTEdUNP6NhC6R8mv02Z5h/eukBegvugdcDbVnpAdPCBCD6BxCPtswGgKZzjNo0ybKFnwC8ATQ3PmSDOH6ehf3666+u08Zfiid8Y4sn/7UwGPDNnMXHj8DHMEuiuPtSBF5cLn747e8/LP5z8V/NegifdZyAj69VAhYeNFlagKrrn6Q5LzmAlMcq/fb3V6SBmJmqwJom4cyE82SQtWngv4dd2zMflwS5cAMQ7mAmz7LpZn5Muk8LPlx8sxconR/NrBGXbbfwgyoo/KDwRiDVAe58i2RRdoA9u6QNAUP3bfDQ+qvbOA8Tc1D+TvfrQtycAEeVD1JtXpwFJpdFAsL/LSme94GQ5od2sX4X8WkhzXkKOobGqeLGeekInee6zI3CazoQ7gB2v30pZl4O5lA9iuYZHjAIRMZ7LenHec1BI5MDhPDbd92PMc7MpPqDUZsvRfsqCKeZl8IDBAGURn3izzTxH6+UauOyz/xH/ICls6TXKvivVXnk4NwPfG98/tgQtYtvvcNi++g/Hi3E4ku/RFB88f9xUzVHhtnt1O2O0bfsYivpqvVcsbnNnFf22ZkCcx8ePKrze6PzDmbvmP6lyBKQfs34H8+Rj3V+jXniZN+AGKuM+pAPkgxYMst91MCc000zuwzseicP4OHigZQg3AAwQEHNfrwrnJ++WxoDVJivvzcSj5xp/DlGIM8XVe9mIAfDIPBdx0uBVc1cx69VBgURzDV9ixMv/oNX83qBvAPy5zVP5vS5FZ++Afrz6bvpf5j47JfmKY9esgdl3DwEADuC2cB59eYsAOZ1z64e+Pn5IQS4kVfd7LsLCin/8LoZNEHdJy3Il+dSg7gGFUDvj/P309P5bnCvQO2AYIEKqXoQ3UdNzZmTg24I2ABgBZRYnhSgOwBBeQXhIdDJZ4AAAPxqX58SH7dfDgWPQpxp7X3i7Mg8Z+4UnhXgFOPvcUT/szQB8vJ5xEPvP2baN22z7BlLW4CHQOP702dL8enZFTzbjsW73M//tG368a/trB48f/5jAnxexF1XtZ9h+MnN79T8CSAZ/LS1/U7THx8o8XGmz4/v2PCxLD4+MOPjE3f+oOTp/+fFXzP0DyJehfJ5gX5CPiHzI+GVaK8PiMvm49r6iM9PvxRq8B10gXqAON1MCtk4I9E7Q74PATQZNQC/wOAnY7Yz0d4A2jwoAizJl+L3mT9XHmCgIpoztS1/hwiPVgFUwXMFvzEZeFR0QLc/t5xR8Gneqc3mt8Hb56LPsg9vAFODv7TTm3krnxO9nXeKoKRAL9clwePqgRv3bv75x020/PjhZJ8WbAAwKmt/n4wvtpnZ9nc183QXuOkBDR8WPghSO7MjcHdWPteb04IEBrk7u9WN1ezHc1M4t5EPXvj65IV/NugPZPJ7CpmhsO5BLX5YBJ+iT4uzJnJ/Kv9bD/vPwk3QJMxy/PLzzJcfXsADvsG+48Pi2xYCePXa1M0agqIH++Wf5+3LHObHlPkHmAO+vk369gcKN3j75c/smrnon21Sg7YCXPbojp90dQMdHAhykAwvjH0QG0jbJ7U9au1PPX+vx3+9zCD//EeNvAPLQ9grorcgSGfefVE/oKZusXLyP1EFdD2gGRDcHJjvEf/ud/nYw81WgTh1zz85/PYG8tMBCeO8MvS1CQDDAZJ9bOcWBwblDBSC62fhgWf/d9uDl7A2dkBHCqRRtOcRrr+iUJRycQcjKYLAwiCkQxpbIauVj2MYRpBIiBMo5SGhjyEoFhC0T+MusUQxIO9Zy1/npi6ZDZytA3H5COAg+P4Y3PJfnj09mcP2bTcyR+Dl4G9vLomDkXu85ZnnZwPTqAubK1dtXPiCUPfsHuBpYWVymmNL5Ej05jWRtyZTRbnmrwPOWK53xDZOJoceNbbfWCYTWhV9KyAdmqrUTmqlXCKFG2CeKwvr7VTdCG8iIGJ52hV9IF3aVDgoNaGhhunYXKHkdXestmVtn80VdeySvtqqAd9ml21SVObdLDsYHkCQstQ/EFvzXKtE7l1stZ5www6ZYtiQE3e6h4fwIDEkCsnC6YLXU7eEt3JCr3lj6+ZKJCbk4OvcxKGGfQ60HcTtd9k5QU35vitiZWxye20XbZmuc/liZqp7cElHxfhivN4PCWMQ9bkmzrrSb6uCNJlCTAZJnJbx7XBVdluxU49+YJyF8XrM/Q1kmLmWbVPJJ09qCsFw6HZL1z9hBEVzyzAcMHhVjnBgIaNl302cE459V6QHuypgJ+6arVdtmv64LVpz164aBWyyUzltEkMrBMwUJ2+NFGOErSO2bslY0IBERLDli+hya1s+HbmRarYbQljWlFfpRwFFap1j9GXtboc00OO1aV/ZJU4E/YBj25quAprLDajWd068rc9HauITyJpuA4dnnnY1tfTc7AySOaAb3hQ6u0hBQ4/t0KsndfYEpRV22Hfb4iL6hWgEzknt6cqHHB9fpROrDfvY4Q/HrDipB5Sre72ytlvVIZUJGVDeyM52s6w0jD9U0QlC6t1VP6IFR3o3yDheyN7C0auolxx8ON8vI5rT0oAlPG2sKYEzLOWcERdVWcZDC2UNqL1znKqn8aBlWqPL/HCXZd0Xp52t9OKoeQzhH/TqHJ7ObmquSxthFLwstiGFXGoysnQbywMsEjmm2m1raROaHdOo2q5dC3S/rE0r428UM3TSNTfFJY1eMj+O6pGDeD+8azKZHj0i84nA4kLIOx9h6pIW9tGG1i51N1q+SK7LmGDtVmanc0qvKTzo77GfmKjJXarRi9nbvTudKHFLn9jjiVTZnspZ0Zs4ORrpcX1jpxMR3WQPF/uVfhGxOEwQOm7PKwZqVeYEKyHErCZiimsTVgK7EMkQ1q/wFiVlrK6lqPYPYnRrWUNbr5p9fe3Wu3hpeMap2bJKkdqZuCknxtov0yJsdqwDMSiXGMZVqnI9wk03N5e8O5wDbxgcvUup1L63B6sdxz6mtLpp98o5om+7zWAyIylG3hoP1/Lx0K9X6uF607xNTcfh+miq6mT33laG7Zy4IozR7zto3V8rodCRDJ8Ys815EdnqV2ldRODCA0uVj5Vpp9pNoyJUgz1qvJqqdsAiY+hE/MArSGl7fpeFrR/fA8zK2aqjO1nEvOVAbO0rPaT4VPOO3XiCf8BvF54orGasJfPIoxGniJQ6BLnFZOwKbXgmGFWmNOs6GiNJc0jcOFnIxKRn4+6uSRpDWHu1aVTOTZmzEtQCbwkjOvGePVDFYb9cDpJjX+Hets4HS6yN5LZJWDu4j9W4uhe6Rp7ZzMC0QxVIuaoceU0USs0gVwXK0gU0ptdSvhoS6fcxnFx9aTiduPW9FVs9xC34vL5G173At+NhOFXqmOCrXFq6UsIfbGfDJT3JuRMAwSqKw9RTImRQ1vVRmtSLLRppt+aWBlyYvl80N/d+t01RYF0hgsJ+NJoTLU8ilMiF0cuhjFPSfYr9FcC4W5vg+q6IhELwCjlMt3KdYpIM6eKeVJAOEUPOonbG2KzNrbeTalY+XRQ1L3spGimWGNV9X/K9IlaFrZB+La9JsxSjPdFETSjccwaryDBZWtQmwZMD1jbamlFsTVMwdgt1086vqTKlrFJa0eGRdrHDNkfLKnF1cbPLW9fiERLytxnjV1UnCVFVncl8be9WzJliOnsbGXsvQVX0anPROdJ7iLia+9Q8eHXLrNeX5QlZVvDaZPTRZ4rbyZO5LUOZJxNvQutkkHeluUTiUVK9o47gxLo4jlq4NzaOLxz8kT5NKwL2EYs3NhVjKHcP2yOB4RzU0aKI8gQxt3K9VpujdliSFEyIO1YikdVxI4hg8S8TTJIdx9KheWFpla1dAiIZVtYH3lnJjr0f+yXPM5697UpmRwTjVmmirsIHa8XKdbbEqXMsJL5yXsrhRhYRotuxKgYFJ4o9KfdaRePLjizXS2RzFHJBOwTulaWu+S3cEpab8Lu1BUXTca+IytndjW5u6ARmmYK9S+M16UV4vSHZnYdUDofX+GpPEnv7dGmOu9G7bTh0v4tpZsJKqPajM3HRhrOkADbdVUJzs3AIUXHG2FPsoHLFRkOWUHffbC45aUdspsasuWlNpvcI6YQjOi2SyrKqon4zCuF1Ilf7AyjMA7IlmeVa4Q759r5bVb4+eZOn9IecvdKymwv3+HB218rywtg3jKzzVbBkKRwRGkNn+ZPcpLtdFtRR32yU0dzoPJ4aHpmXwe2KS8rp7pVonSzzZId3PIeiZ6nVxGKKrpuOqy2R78OaXKaXIz3WgnwYjYzROCo+wwIu+YeCMvi0bQEQOOf9iopUyCpxxVjRTV1f5bVXCHVKKhp/hBkRdNSNafTcZTndY0uSz/bOMbe9GFRhsaqLMbO3RoWVtZIvMWZVFdqkshS5SnXW3grd5PYSLCSVjBr6VpoOfH1u9Cpgrf6s+ktRTUTlEq69M+I4aS0bZMYmeRUYwdY5Fd1RT8PSOpaaaky5TcE+QWv8Xj5AxsEs6ypXzq0N3RyBaZSi9NebGD6bvqjvObn2VLHi487mTjpsXEkVkahduUviPe4PhaKL3pq+Hx2RchO8zUHHIGoQt5VkuEW5fY/lxui1uMiIArUEXQ93Xm4jLbJvzQ2CW1nXVbfgLTsQxYw/YC5FyNOETBjXQtUgsGKEK8ruYl4UeR2I94691+ikSW4qiunWPwtrSzjL1hYKbW1KsuxoalQypvJNvZ45/bKXON0mQkoFLHzGssS4jdrOuYbC7QxogPVqyDlfSNX1mGDgwhVChOWZj0HaGyzwflNEVpuRfB6UTtV5mdVgaa/1CbuLIxLSkK2Fwq7N71GxidQN5Ew+6H4l2VSOxNphBEGrk6QKU/1kXZY4y60uhjg2wQ7ahQMcQz5hsqd2eY1pKzsa6Q1G6MLMiyqICF3e3JIL6KPOm8OaSn1VSWmkl3qXJQcoECmBVpruFh80riEzO1T4Y3s2lY0mS1oSDVGmLIu20ipWQ3LRYbtBdkHOO1CwW43TxZ42bHa5mjybOkV1sbPjusm8DU/kfC3gwsiwLjPJ1bGoDqHJHZr0hqG3akmtWRK7tLWB7s5oISgsro8djOOljzUoaRWG7GvoKTymuqmL4XnNnjgB3hg7TrhXF+MkVGIM+orSg1h0uTKqgApvsmEjJcIHYCcKn3uAMIXuHiNmaUB8Yx9u5x1Ih3SjSjcTRZAkJ8wA/L7cqhSt7dN5rZZaUd003kwBEhuga6TPIWokGS63ypqYTCbt0ZUm2GGkjY5/o06ZmHPJuedr5Epukq3ON6LOoRmkGhsmiMX1wV2isXeYJGs4EOFxLXonWMUkLLJQq2fNtlVlRItP5n0XbNAYuXX+bbUXrqRiy0ziq+srdZXT+9BPmNMV4p20yw7XFHJn7gflCjDLClvZbakwPG3HDSGSTH+Qib2G87hZtHJv58cxx7Ya5GJ0vU1XNk3L5yC5+JfYvEV0p4uSs2Y7cxtkVyQ5IHpnyucNREhRzLgsc3MsAGJOpwluZq0kyGnJScuwRu5xqkFuQirQd3Jt7kVY4uSDItmSEEadhO7FSNkQO+uQXEskKvEuUZJ2hUI1OfpH9RKUgmhSQb6JSZY58+c62th5t7o4VxHRZUMyeX7bXFyXF7X7fpxKy4wvWdVktJfZx2NVUowwHPdIJUurTOBokYMp6VRFF47ecEYonjyarEfiCpVEFUwBUrlZtQnHbd8KjETdjun9cnasQ6jay26TXdSDf1DbYX93D1C5ph2PvORHLIzjtAvUYnLlpYZIRwuR05PPyWGbQsyRwsyVJSJRv7Yh8dpak7BR3BGUyIipwgnNV2xzV+/oRk9bUfWyEB/Blse5YrDXjdRhWO2q/N6b7fWKYa2Qh+uwSs2EKQ+6bajdiR381EdOrn84Rid7i+xsR2nuu4uQZROjsGfHjTcj2pxJd7k+TRWpgIZB16YU7Bkhv7zCygCa8GCnnc1dcoLG6nhE1YMMtlLrPd/4l9HZ+OcksKG+4afgSh9tJPcK3ybIPNnSVpMbl5UkypudTqLLaDUpd0S+V4bN3yMmrraSQqUMI1Jex4W7JQaaZkNtp7YuB+laNJJl7C4dFGObmqSNk3YMNuqRbLcp5mB6v+m0zcqKO85MaaMHTJJTYnfqzCRaMRiXZYGN0IerT93ddLWs3KCrJuzEjIaOeZDTd1Gw5wf6dt4MN0iY8GAd4T5eo1LHQUMSCDyxv5MNTiKktKJwK5+MHPMD+kbtl3JgEzRkjqeVNHFd4i73zaWgfGNLYAlJrSptkAMtT0mxRW2UXrUeo2e5U7eTzGk9bIHaPsKGhuVjsdIPSxZeHYxiuPEBO04aeiTYIzwaedyf94ElyFFvrc6Ud2at6HBhUeFkFzWa6XWuohCILrXeCF17pSTntLuxx04e9As77mnaxHdXaRdEZ5uauqKsTBht7BQLKKgTL7eR1nvcOowISV/0FOAXPIhhSAWn5bFO+b2IXGCqC7OydLi91yXU0OQagWgIctgYfr1GjHZ9Ol0HI/eZWPdY2BJRtIFL/SiFKimc4Z5lmH3pagc+ALXDKGkF6cfiGqKaDXO2VNtcDUuTaK6Tdmnwg7RE94MVhV4nFnyJypPgdURyrUVTNN1APBI4TGAZ3tWItB9i95Kx64yPdAuD7lA/9LDrHRgCGe+9dUKglaNLaRrurOq0q1VepfmWvCj0Ebsarg5w00xWJO5IiX4gBRVx9qlzQvCaNob6Dk2sQZm+nEVMmzOcmLMxTePIatVOp8TMmWvYZ6W75exNqAUad+nyctk3RGDGZxHBq9tBcGnducaFjVm0TVi0dU9E9jSZE0cTGsztvGZC4qbZXo2KTzg11UZ6p5ImXA4bqNZAMjJL2boU0zVZDkdOw/zl+s6JmLFdb1fKobPO8vG87fh83yjo9UCM8S5NvSWFxx5DbOnmgsUNj2hQc8Cgcs/ecZoqsDA8bqyuBKEoeH0o1qstcb8G0WmbV64jKuEUTLcWIt0NLHj+mF6YMKqKO0GvdEQkl/2+AS3TtjyaK2+1PaPkzvDoeBT1k2aOK1ftCi+ZMp6jWoXoDKmX72gG4tFbJCk2RT+te0yc7ptCzDIX39CpxWEIQd6gqAYM61r56rrUB+/iDZlid1zp7iGc6R0Ka/QDnI8xSDDS7ZNxWIcSnCbIETF3pW+tefGkBl6o5ITH2j3OAMDjyFZpzWu/W9sMDF3hzNPtKtmORTm1HmGsz8JK4kNXy2K0iHeDxSD0KjxSwo4lbbTBvT7Pi86cSGwqpMspvZxO7TTdyIyerktyuxYnCm4i7mphBRmfLMAcvjxoe8miiULrajjMu2qDQ2jdD+G2rUV0h658yV0Z+yvVXVd1s90pTWqYpFOvmN1JXKKDCnt9K64cztwn0i51yOU0EYmMR458MoNuQ8v0kSL21BhjRCDoAD4FhRsVD+SXcmCc+GRA973JWpyen6ehxq7BFZJCYUOOjK5xiC7gWXm+YtqpVGKxmyaUia8spB1D/QxZrRYn9lQd8SJXOz9D7WyLD7kPKapKHUPb5dDDQNttkC5TY9tBR4XLamNtgxaLZDd2iBmXVvVRFnZBq8XmZUdvsPWWrzURNEhLdg9VMpuzraVHYwmN2fpWwkOD1cMq0l29Vy/E+byvR6Txseyuhc4lyjS6BhsxFz+5pIqHvrxs3Cm6SITj+OHucsSmjrrVlSnf0CvSeks13FedbaOsax9dHfC6GmEdW7UoQV57aL8tQFscOlR69zIoXN0Q/KwmS3u/RWFzlQ0SvO2uo0ZHy+O9YukTs0Xr4HwDICFy+/iCWk7eRfTV1EfU37TwQUYkmbwn2FW/L+2gcwf9VIdXhI5Y4dSrS8jw0w1GNBkfhpCn+y0sBOc86NZ7dWfzvn2sGCpZY9NmPLIGLNAreDmAcCi9sod51Q+jJt1nw16iPIHt6OxI8+TezdBupcMmp5uXG3Q82E0B3Xy514jiWu7LitYugZvimlPs7oUpxJnNRw4VFlbf1ZthpazcdChU8w5Z0rELaH3sG49YJSG+P6dJbOaRyOU3JLz0sTTpROm2G5NA9/yp34ItqaBQasLozV6V1hCqY360Z0q9ZzPcT5eYO92r6aAzJVQFOz1fEyGCX+JGppcRvoYEOSu7e+LsW7OIgtIHfDYmQ7XE82GAQpDk7qp2OVrpEQku1BPUYxMhwMBaqoCuCoe5t1QUiugsQRSb792x4sA25qJVG9Vt8s5N5ASGSlzv4eSoy1IJxwSNegS6lMyWG2K4FUKvoe/DhQAtQXTJDUjwK1PqqGljJyF8ZRW1ytlb0NzUfvLXcKH1JAJR3dmjzsl0tSmpj/ktwwIqhk3HOlYRkwR5IvA6zDfydYn76P5ybzrZbJMDjik3whXV7tArXQb4JAT7+mqbtvHSn7dGI97KJINgdtPyHQSHrEYtU/4c4ES3ujdoT2mshCP7jEurvbOa1oN17zdEgSnuNWtUzeFry2XOCCFxeIBeL1iyguHdECF8EUbHLQEDrTSiuVeBSVpkSE7sGGKDHt1oFXUkpoXEC77ah8iATJKnt9yaYZi/vX14m49iXweq/713vuZjnf9nJ0jPg6D3NzceR4uB439+6Pr837Tvlw9vjZcA657nZ23WR6/Dp384Pfv4l07tZ1Hj8wWr9yPk5/F050Tzu8lvSeH3bdeMX9sye7zRAWa4fTu/xNjO77l64Pv3p6b/4B6443iPk8SvXfnVT9qqbOcztKSY39gI/MTp3i+j1xnjhzf/dUb8FSOJr0FTzc6/XgcAPmOfkE8gxv8LRns1cmkuAAA= -->
