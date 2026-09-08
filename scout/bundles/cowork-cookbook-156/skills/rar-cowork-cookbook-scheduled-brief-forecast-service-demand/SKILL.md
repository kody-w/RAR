---
name: "rar-cowork-cookbook-scheduled-brief-forecast-service-demand"
description: "Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_service_demand", "rar_sha256": "1d7534ba2ef9e0ee8924fac119fd87975df1cd7285b55b437b4443c168c68876", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_service_demand`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_service_demand_agent.py` and in the RCI capsule.

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

Forecast service demand Scheduled Email Brief — Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand
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
      "description": "D365 legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 1d7534ba2ef9e0ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_service_demand_agent.py` first:

```bash
python3 scheduled_brief_forecast_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_service_demand_agent.py   # or on stdin
python3 scheduled_brief_forecast_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service demand Scheduled Email Brief — Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_service_demand',
    "version": '3.0.3',
    "display_name": 'Forecast service demand Scheduled Email Brief',
    "description": 'Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b8d02300d471a8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/forecast-service-demand'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-forecast-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where forecast service demand stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on forecast service demand for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast service demand, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to', 'example_request': 'Give me the forecast service demand morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly forecast service demand brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefForecastServiceDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastServiceDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefForecastServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOj1pblX1HfimjbRWYyCykrKqJBYhICSYCQhPNFmnmeQQwu//c+SLqZ9nt29Xsd/amvwyEJztnzXmufhF/frK4Ni/rt85vmWfmCt9I0Cr16YeXuYlP0RZ2AjyKxwf8Lp8jbOrK7tqibtw9vrtc4dVS2UZGD7UwXpW6zsBZZUedRHizsOvL8RZEv/KL2HKtpF41X3yPHW7heNov36yJbbMfcyiKnWeBLcsH9T20jL35MvcBKF17eRu24OGsy99Oij9pw0RblglxErZc1C3tcRFlpOe0HYGqRWWnkNYt7s2hDb0F9dK1xURfAFWCHdfdqK/A+PFwClhRZ5uWu5y5yb2gXQAKwv/kwb8wXDVg8++DWlt8ugJlRCrQCX73BysrUa94+//y3D29Ac/r2+dc3J7WaZg6dE3pul3ouM/vMvfzVnu5uH94CGamVB2BxOYKA5+B36dUgNBm45IJAvX792Hip/2Hx7/+e9FYdND99/pIvXn9f3ub/1C5/ONkWQAXwwrFKy45SEKpPCzrtrbEBTrZdnc9+NCBfefDpufO7JBDH/5zv/fhU8inw2h+/vBXABGuOxpe3nxZFDfTV3fz90yyl/PGnT2nRe/WPP32X03R27DntLAxY/enr6/dLLFj4fWnkL75qR3bz0gUiFJUeEP47/+a/p+kvca+QfH0u/rEoPyz+XPLsz38Ce58VaQO5fy4WxADsfPsUF1H+40tHXdy93Mod78ef/kosyK6TpFHT/lNyf34KDj3LBdF6heSnD4/0/W0BvXz7JvOv1ZagYP4VT8Dyd3XfAvVXsh+Z/TvRoFtA8b/n8k/F/dkG6D8XP/+lb//dhg8L/8vb1kujuUHt1Pu8+PVRIj//4H6/+MPffgOi/49itKKrnYeEr6DbIt9r2q9ff/6heVz+4W8//9CVoIo9K/va1emfyfyzuD70/CGCr1U//nEv0H/Ok7zo88W3Hlr8WpT/o/7t08IA0OR+v958Xvy+E+c/aDE78a70GYLfdWMDbP1dHH96+w0AUA686Z7QBfDj3/5tIUdOXTQFQC3NKbp2ARLcRpk3G6+HUbOIntBYeyCuTQQC+1oH6n/O8Gxx4S9++V/OA/M/Oi/Mh5t3aPv6wPOv72D+9QXmX59g/sunhQ7EF3UURDkAb5U+Hr/kAHbzdlZd1t68HsCVPbbeRyDk4/xlEeWLX/5JDV8fwj6V4y8PII+eKKhuxBkBG7D/0+zrZUbxp2cOoDNv8JwO6EkLBxjlRwDBP4AYNEV6Bwg6x6VJojRduBHQCWhtfJJEl3+ehf3yyy+21YRf8idk44sn3zUwWPDNnMXHj8A7P42CsP2Se05YLH749bcfFv+1+O92PYTPOo6AQV6ZARbutIOyAJ3WAYpqQdJAmgGMPDLz62+vGAMxOSBokMfIn0lv3gwqNfHc94BrAv0RI5cL25tjOfNkUbczFUbtp4XoL77ZC5TOt2amCAtA0K5XztSYOyOQagF3vkUyLwB9g3Js/PHDomu8h9Zf7Np6mJiBlrfaXxby5gh4qZg5czbzsQhsLvIIhP9bOTyvAyH1D82CeRfxaaHMtbkordoqw9p66fCtZ14AH71vB8ItQN79l3zmYW8O1aNRnuEBi0BknFdKP845X8ycDxLbvOt+rLFm9tQfLFp/yZtXE1i19xgSgCnjIugid6aG/3iVVBMWXeo+4gcsnSW9suC+svKoQe4v5p1vU8KCfQwWj2Fh8aXDEJRY/H88Ps0xoXleZXlaZ7cLVtHV2zNX80A55/Q5g87mAmefffl9rHmHrncE/5KnESi8evyP58pHhl9rnqjY1cA8lVYf8kF5gVzNch/VP1dzXc/eWl/yd6oAzi0euAjCDaACtNJcwe8K57vvloYAD+bf38eGR0xqdw4PqPBF2dkpqD7f81zbchJgVT138CvLoBW8uZv7MHLCP3g15wtUHJA/5zwCPQno5NM3+H7efTf9Dxuf09G85TE5diA59UMAsMObDZwTNxcAMK99zu/Az88PIcCNrGxn323QQtmH10Wv9qouakCpPDML4uqVALE/zp9PT+er3lCCrgHBAr1RdiC6j26aiyYDsw+wAZQqaK4sysEsAILyCsJDoJXN0ACg9zWsPiU+Lr8c8h4tOJPY+8bZkXnPPBc8y9/Kx98jiP5nZQLkZfOKh96/r7Rv2mbZM4o2AAmBxve7zwHi03MGeA4Zi3e5n//hgPTjv3aGerD6+Y8F8HkRtm3ZfIbhJxO/E/En0Hjw09bmOyl/fKDEx3eI+PiCiI9PiPiD+Kfnnxf/mol/EPFqkc8L9BPyCZlv7V8l9voDEdl8ZG4fifnul1z1vgMtUA9gpp2JIB1n+HlnxfclgBqDGiAXWPxkyWYm1x7AyoMWQDK+5L+v+bnnAOvkwVyjTfE7LHiMB6D+n7n7xl7gVt4C3e48Wgbep/lENpvfeG+f8y5NP7wBKPX+6dPczFPZXN7NfBIEjQTmtTbyHr8eaDG089c/HpIPjy9W+mmx9QAypc3vS/DFLjO7/q5Tnq4CFx2g4cPCBQFqZjYErs7K5y6zGlC2oAZml9qxnH14HvzmUfHBBl+fbPCPBm1n3vgDYQDgqzpvRldwKrW6FAQSXJpp5E/FfxtT/1H2BcwE8163+DzT44cX2oBPcLT4sPh2SgBOvc5tswYv78CR+Of5hDJH+bFl/gL2gI9vm779+4Ptvf3tz+zqQVn9o02q15SArx4D8GMJqLBijrEX3V/A+iAvULFP+no02J96/t6Ef51lUHruoz3e0eQh7MPC+xR8WvSel8w8++J7wEftgrKyP1EFdD3wGLDaHJjvEf/ud/E4ps1WgTi1z39V+PUNlKcF6sV6FehrzgfLAXx9bOaJBgadDBSC38+eA/f+b08ALzFNaIHRE8hBXYrECdvCPH/tIZ63WmMEGOZQdO27K2pNka6POi6FrUibJG0Cp2yCIHAHXa6c5WpFLYG8ZwN/nUeOaDZttgtE5CPAAO/7bXDJffn09GEO2LcDx+z7y7Vf3+wlAVYKRCPSz78NvEZtGKPscX+FrshqSPtLV3JW1FB3164E58oP0Q7haTP2xGZELnW1kccdi1gEgOYkoIKMD7ZrNqd2R+SAuZm0kyJ745d423aETGuH6zGbjjmZ68dYpAN+T+02qiud+yqOtMSVBr6oETRy1KExDCKTBv/QomJKGFmEsneYwNYw1yCgYlVOs/dyhHqptT+mRlrUBmtUtdh2UoMiVTsVI1E1sL9BPfjok8tLM2itau0SKS01kIjCn9AR5om0uvIol3V+aC25XRsbcRcqVCaDwjhVtmlEpsVfuVTdpypRtuVe8KJxJ7HQjrlWJVOrnhLR5+VIgWOtfLVOVQClNH1xy4u5YVEllHcxxjLuaJxq7jKOU+9ty5F07zm1XkEdRWbXGMLtDj8SdiS41q6pT2yK7C6kdqsjLm24m4awpiCThpiv2cEuq9pJxYuGIXyUEufGLeC23xmHlIE2tGGcjcAgPPiO7M3D9ZCeuWRtpBK3NESuP7fcmQzoCdXCRAtk+rK1b2ESjcvh0I8V6cUtSR1j/WRDJXHFTEMyT6WRbEcpY09Tf1SqzAvFeqdJ6SQtGRYK2L2CIeNgiGm3WxLYQanwdbJbSoLLZlev0e5LSne2DKFS3URN07G+pLeL50m7KkwUlTUMbt+7+00QbQ2NW6ZrUe5GRO6k9VaN+Y6BM9JDlta5WV9BbKpyAxtDScNdvyxOK0MnXaqykYxyxe36IlzZcxruVMM0SKY6rEZsczPH1OYHGpYbVOeMyrHi8egd1YN+wUJnFyRESJCavIz8rkIKeX/Sb2w87A6SPzRNqsgjtm9lV6BvFXNWbAvZuVW/afcnPNjZLWZYa7bkBTtFzEaupgwnq0aKRA47tcMUQlw5FXq5TlEjnSIDt8hBWA2H1Bk5DWbyNUmvWG04ELocBhefu9zkLIYQRSf0jNrLkzclwI5dYjbXvlEOe+mYDceQkD2jl4+X4XYoo97V+SAy0Q7qTGgb8NmgOcpqYjmIj1eM4MFyZqbHRrDM4ZDDCAHrqLdtl1V7k46aLu72InqiKzRGVYzjGdk4RLASqdCYgHYLvIjt/UA8mEGPr9hyxVT7JBR5/STnKFFgcorpqlk1hM8jgr7Dqml/08wy2+wYIjXN26G9BS1xq+iVHvWXfehfsYFlYXa60RhrMkU7SbfI2pw8nUzdZNkTGBPh46GT6t71s7shw9cl5rVJr5emt0OanCUuRuRu1ZW7S5BwzVxTiDRhAeu0Hb7BV4cQMuSsiMaivu19utajHTSsrZVly74JMZAf5Vemlu9hXCkSGVt2xo+heIydjcSPqyK4DdF0Ekd5tes87Mrs8qmySMQ9kNiZbzU3ce/quRxOG8MawqVPUTyAOaPI3DvjndaIaEDXbZeJTe+XiHFYl94NoRRYhoxyNxLS3ohYk3aqQT3CNH0gbudxQxoeolF5a+IgzyskKOzC8+mW9/HdOSzcy3kl48rWj7Yu6gV3ziN9iqt5niXtO3HF+yES772ChqdCgo+ZeQ9zhLil99OtOWNOfhm2Q3q76RVnSMo+Ea1o7yBppnOmbUyFoSZLHzOuDHy8+EtkQA8sO61XRmrWDb7Oh82A2ifbWHlCQEx1Gw6EuVRTkzsFx3ukUIpmENCGVM4WWeP9butp0BEq9dXo+FqHFOENHGytYAhdftOUea8u8VBW7u5u7QXsSmQvuli4kCJKOB+J2p26kthJ7jC5LqtrjBUrOrplJ6ypN+p1ddMg8bo9n45OvEGTkRcxcKa548X5wsQ1Um60Uzpcj8g2kJVDvhEKcRl2KeKwSyUNlhfXTHfi2WTu5YkbTZQ968mZLtnMbnGhOfSIXqoubXL2zffs+Li7RZdtyak0HzGcp3BbspGEUTGse1oNVQBHuNsJd3KvppvI3++4zmMZcQm5hxqBfD/XobzhDsVRliHWWEGxVqvS4SJsJQGApHSUHGtMNy7kHyP95I2U7YbMgZJOJx8NIccnENP1j9fiDMNLew+d/PuVX2pn1m2EPAtJsd2IvLJl2pGZnLvJi+fB8NaXLiu0kL6ahM8cJM6hPHSiLTIj4jvtUBPgrSuf0caAR5trj8vo1mq260FjPKRisOVNGENtLxZyFJKqeRc7A3P1PBTSWOQvgQgph1u3CXZyW+9XBiRp10YvKJIiAXc0FrqS09hjwiS8tyqpEbmBtUnr1ncHTTvvKIbXfnXYjUwustxUmQfWzZMpljaIvb0n5kbjWUXSlNU6CBvLx0IwYJx73O7rFZGZRXNi9wJamuIRZjdEK1Gc3aEN3KrKwJzCQ34cfRwxo+3Y0lZ8MEb66rTS6hBvLJXoYEJBR5V2tWvSTMbaNYgyODeMtzrvr2dmxd4mVS0OvoSeYOPQyufNtKT2WSPySICbepQa7JQh/uBQmFqew/PyfJQvpZIHuw3JhDcJ2hp0cw1SNs1AodlqMLaJxmOkXmwu06qp0DIhVva2ZDha708UM6BWWVcVhGennTqxhMyYfbqNRfYa+8Y63e/O9419biQE62m7WZ+vyDXAkXFtiaHTCvzubt6uPbW/ZoWZnQSCVWPsnibXjWZ72/7EsOY0XdPigiV8GPBnKb0YvGTCeiHpiFnRkHpqSCI3WcMnPWM/7Viic7ngXO0kI+WojS8vE9qgEfrORWF+1jHZ3nPKhWejNgkTk9vGsBEvVUTZ8AWnBTjh3u8nXXYYeJCsZuUHSZNBtC5rUE/vA/h+GyPc15eDfFnJ4mEPjdgJ5s7d/qQGZH+vILgVXa20r9rtnJ8lrbhPoAaO+16kjrsALoP9VtYp5dyqNqVfTu7Nd4aKUbNxwBjdlNkoWRkjI+bqtpARTa3KKN17LTdwCYtWYVBsMujiiJnQL2+bZe2H9Y4+HCVmkgyk28SxxrQWPukaVI33e8mqw2V3RdLNXRQ9gXbNzcRpiLxHMNZzUhPRY8ht8D65yfYOc9Lo6K+HW1nQIr/DzIu9otALVGA0QXOhug+D6K4IZDK0tHfEvM5C9hIDLe0GhuBjU8VWUvFUKQyR4+Q7D68p36oPm5aWDtdpszM8q99SO6aPDnK3gyqNv+p3GM85oZ/I891iw13Axi0UVKooIUambRLHFtidR2qY0wcbKkU95xLRSn1Yoz09jqezOZiOUjZrmguMKsiS0i6u5rkx6L0jCizK6mzqn2j7xu+m3ZlR9lnSbp2MhzrVxC43/3Ib2oJzArEaJlpAD0TC0l4IgAK79LgPOgVxRnzs9Nu9sjwuhpIVW68kAU/vO3naVGqzQdeHFuMniB86fkMJXkWgoyznp+Jan7m+ds8J2h0aTtxqVyLsAg2pJDxrxWRvRW1Ulqh7alZ2Ed3L3a70eq+QfDBihgF7uouccC5r0bfyixVzTO+eC+GO5ZFGhe22jlhmkEcq7I8SqUjZzlPP9H5wRlEXKVkFXYvqO5ZeX6wohk+dZxohLdTsvT7i6+O6IicsZvsSJ2MJg8+3Tb+NieHSInoOmZTeK9fjEGh7k6tq17rt1r5jMWfBtzY7abVKPdXSKFmx9etZbzt5W1wjQLWJIa6iA7mP4J7Q8uZw2fEbXMBpF7L265ITseO6bE77GrhCH1HQGpmpopMqIIXXnA6RW/RTcML5My/qJ4PfigLP+VdLVe+cXiG7DKuo0reG6qqW2Do4Bap+T4RGUSZTT0/x2VRUDseZeDjayGhfTsykNMyG7tAQtDM35qRaHWl0Y2kT3wrrGJT+BCaz4QTQB1vnWHdO4KPRkCK/YjIXTbibs2vulsXVls3twbg7yuppIOirxx7E8mCgoJQ8bIRDJSfvuIFuONeXj856WS0JxHc85H46LJG2u8DbtWFy4rlReUc2UibXbT91tVZKBfhK80ySn48WNR1AJWLmEXKKI7u5bKgDpmC9zO8vstm5p01oN/KWmcqKiqjtReJrvbnhSoxaTrw6F5oVlaOccBqjdbKMj2MywkJr3UEpybZjgDFgFO6wddn3Bto5iN5aYNC3+st13Mt0mo9J42MYc+Ot2xbrl9NNuerm6m6f3CwLrey4nwrADlMds7AEqg8vesUoQniXi7QEh8n56jsneDuCwauKmWFESEHZLLW8bFOzglG6EbBqj5e47g09GiYYYuQ3DkwGuiP2zrUi9+75fO04N7IPkYU6B93jLzi9pME5iif5emQ1BmFJoqEwVtFJsfGMK8YXinIdd8QmUTXpqhfyRb26B41D6KstMXRl6MgFqcljgUQFNJtqdMbV4r22aSUoul4Sh6H5AmN363PpEVQyXKndncgv5m6UXPyuG0QBmR3a3rcMReMC09dDtrYAtsC0NJX6urofIBefzkc+gu29d3Wz5XrTyZQw1HF3jIbV8rr12jO5XR6NK+vulmZzW25HjxVPBVZJByQ87w/sISxIv8q0MfXvbTvkd2g4X0zANvj9Um3up3twhU4RItH5ZMZKjScwEtKXgj7RnJ9edlQN4uWeXcvWITTv0BhxLxK8KmXEVuSCnFbo0lOovMKPtl3EURkfi2WzdkUUamwZo/DYCAOIL8Dhg2fW7QE/EwRXGzAVUzi8jddRsdu4dcvBsIgTFu3SnL322Pt+vAxugdARWy6NfVsxhctcyEaWuCkhR6orhPboyzk4iKsInzpOwR9lOkpjbRpYWRHEbZLp/XLjnOPlxPoxGmvrJlZyZqww0MANhgj5TetGm9gyhbGh9iuXDKb0YDQaYEkl3PmRrzAy3saCOV7q6TJJJ0EOEBiwRgcR1WonE/cVer/5xIqy7V1Cd/IwaorRn7XloAyyB+n3rLtiKWnIuzU6nK/bPO7V9kYcdme/XlIqOMsPELU1N5l7dAOGTWhUTLYDCfHESDX1MeYxKYIU+3IpoJ7NCj+xppuMte5hxI9bwqgGPDEOQrUdcrsZjyZEbSq4n0SG96My15E92e1wIhONjcBvBZvXOCkXkzI4xskAnxAXdYxzwR4Cs4d1xNbCbrMRl11beUKsoCat86am5JuiT1i3ZjkCUW6j7+jURjvsLbdfbc1kDcZSQE0mQZ0Tan2JB3INXc638H7bkraWMvE+MfK6W4+32yW4rYdDDWFbVthMzWrad1l/73HBAUeaDbl0IPkeVI4quNu+PNf2gMEFlezl4YwnJNOjV3k8bA/2VKbCBQXdm/Ci2tuT5cl3VyoTP+u6YG8ebLQeQhZi1IFJXfdkEdqgEgpEiNXyTgMOo6dGNZx9Be+aVpAoxbrBTczG9NWVLGUdOez6pvPFmbdJGy3WgWcDN0aeLxwCB6NeFpjeHRuH1bCmJdEKNIqZwoIKg8vpSNxgUy9c9KzzxIpdx7lYVKlb1tslUTWHzqEVKuDzew2vA6L3dax0MBO+IGR5cQ6QTy7JKLoNMAZ5wnnfOQx+EdRp35Mdc1d0za9inPGzbM1i0QEf+umK5dV9D0ciNML7Lr+LQVzmrpRbbdJQ631QlXWKpKgtgsmKKm0aNAcmd9TV7rjcttCLwFoH3iIQXWcRwYoxISWPvOLZh8E7xAe59lM4JsA5Wo3YtSaUArqTcq8BZ9VOIE6xXEJWBk5coyT509ohaFAESy5eRUgR1adjGkBbR2DVy6YAvb4KwhuxPPZNj8qRypdoYueacVENdF/WXjAeDuUWFm6dksCmMiIogFK07jVNuXHxrepW8logj6SBN4a7FLAbDbsMH9/JBmeP4GDLB9IJP+FEcSMTnejXOuti6b5bng5J7jJ+b8Iuj6F2ZvSXlBnd1sRdEy55zCA2Zw9rue4AwZcx9/CtCc48jTlOTW273a3Gr1AWV2lLT5fu5sZx19e3rVJvL5U1CbHTTnTvKUyOFYM+wQkkknl9vNT7c87p18Nw3KfsTbmoI3cksIZf2RBjCiceul8Au+qDQm817KhpHFFWEaUf0KvVNUGLX8Ly5vdbhSDJrX4wd506LPHGl9qJUMa2xLtoYjK83zpV7nH2XZ8SPMaosMDhJN5PRyuIxfrI8sl2KQpHercE1B7gYGT24M2d3Ji9gJCogWQewhsb0lL7m4BhRIfqidTlHWn4W4BSRRGsvOv6unfp5ZlKqVN+CtYnatMt47JP0IOSHFbHzVZTtmhLX0+QW8kwpVH7WLmr3gDduN0dItURa/0xj26E4CSRhso0cd3FItY51DUOdPtqIuu+guRhSbO7YD2NMi2pN1GJxSzyiDXR0tsQseDtKuEn3W6pW0GG6lQ4k09vdeLSrBpyQHGLwAtmtRUc5HJaYzG0jwKvWUk56qo4gq44c2rrFdVUKypTbIVaK86y3cPHFIab7V2p1/wK1DPe49Q9QOyYTMRtuSugZWugkksqQWOT5f6yBB22kpYH6ii3wgDH+aoWUTRrLw0Lh5Cz3fr1emivSrNP4zxLPREuM6Fd7YLtDTQ7dWJlB/I2pgetDaqMnBHFhzu0rvaoVbgyKvTtkg01uiuNIzHpjJHQ57wrIokdR2sq1p7AqCgx4HsjFntBcDZw6jAZskWC21nQ+5WkrpjEwUE33MG5gFgWiu9nPCoAv+A6hwYhVJcxD3f81VsONoLEo2ccxsCtfW65niRCws7QTt4r1FI9cZPQbvl4X3jCqpFI8nKk1msiPNK4KEzdHjGo64nDUK0kOu481HDsbQvRd7ih4o/c0Yj05XSMAx9mtsU5YUjldKLptw9v8/PS11PPf/U1rPkBzP+zZz3PRzbvr1Q8Hv95lvv5oevzv2zZ3z681U402/V4utWkXfB6QPR3z7Y+/pMP0mch4/M9p/cnu88nxq0VzK8Ev0W52zVtPX5tivTxegXYYXfN/P5gM79i6oDP3z/N/DuX5isvX9ri6+vtx7f5Nb/59QnPjazWe/0MXs/+Pry5r1d/vuJL8qtXl7Pbryf0wFv8E/IJf/vtfwPopUqX4C0AAA== -->
