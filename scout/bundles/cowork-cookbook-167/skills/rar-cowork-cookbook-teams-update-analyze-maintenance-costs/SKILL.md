---
name: "rar-cowork-cookbook-teams-update-analyze-maintenance-costs"
description: "Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_maintenance_costs", "rar_sha256": "4562e5ec6e548cdb551ae16c1a942e67f7d4dac86d57b18bb461d5b2e651a6bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_maintenance_costs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_maintenance_costs_agent.py` and in the RCI capsule.

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

Analyze maintenance costs Teams Channel Update — Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
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
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to analyze, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 4562e5ec6e548cdb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_maintenance_costs_agent.py` first:

```bash
python3 teams_update_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_maintenance_costs_agent.py   # or on stdin
python3 teams_update_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Teams Channel Update — Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_maintenance_costs',
    "version": '3.0.3',
    "display_name": 'Analyze maintenance costs Teams Channel Update',
    "description": 'Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc9f362c3f48c6a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze maintenance costs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-maintenance-costs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads analyze maintenance costs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.', 'example_request': 'Draft a Teams update on maintenance costs for USMF and save the Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on maintenance costs from D365 ERP data, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeMaintenanceCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeMaintenanceCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpvMbEU8BAJJRFubDWIVCJBArBllkez7Ilah7Prv40iKJauyeqrG5tMoIlMC3K/f9Zzr4fz+5vRdXDVvn97UwCkXrJPnSRw0C6f0F2Q1Vk0GvqrMBf8tvKrsmsTtu6pp3z68+UHrNUndJVU5T++LwmmSe9AuCicpu6B0Si8Ac9pu0XZO17eLsKmKBTWVTpF47WK9wRbM/1RJcRFWYL1FlAxBuciDyMkXQdkl3fRQonUGILIbq4XTdEnoeF37CYwGa2V+NZaLS+AU7cKLnbIM8kU9LzdPA7YQvgOUG4IF6TT+gldlaTEmXbwQTof2MebaJ162ABKBBe1/LPwKLFRW3UPIOzAwuDlFnQft26df//LhLQG/3z79/ublTgtuvT0W1mrf6QKidPLpHojf7SaBiNlHuVNGYGw9ASeX4LoOGmBtAW75Qbh4Xf3cBnn4YfHv/56NThO1v3z6XC5en89v8x+lLxddHCy6ymm7wF94Tu24SQ5c9L4g8tGZ2kUTdH1TAruAs5ukjN6fM79LqurFf87Pfn4u8h4F3c+f3yqggjPb//ntlwUIw+e3pp9/v89S6p9/ec+rMWh+/uW7nLZ308DrZmFA6/cvr+uXWDDw+9AkXHxRTzT5WqsJvKQOgPAf7Js/T9Vf4l4u+fIc/HNVf1j8ueTZnv8E+j6z0AVy/1ws8AGY+faeVkn582uNphqeYfr5l38k1osDL8uTtvun5P76FBwHjg+89XLJLx8e4fvLYvmy7ZvMf7xsDRLmX7EEDP+63DdH/SPZj8j+jeg8KUHSf43ln4r7swnL/1z8+g9t++8mfFiEn9+oIAdl2ThuHnxa/P5IkV9/8r/f/OkvfwWi/49i1KpvvIeEL4VTJmHQdl++/PpT+7j9019+/amvQRaDKv3SN/mfyfwzvz7W+YMHX6N+/uNcsL5WZuWMQN9qaPF7Vf+P5q/vC93JE//7fQBYP1bi/FkuZiO+Lvp0wQ/V2AJdf/DjL29/BfhTAmv6J1gB/Pi3f1uIiddUbRV2C9Wr+m4BAtwlRTArf4mTdgH+zqjRBMCvbQIc+xoH8n+O8KxxFS5++1/eA+c/ei+ch7oZ2b70D2j74jyx7csPoP5lBvX2t/fFBUivmiRKwJiFQpxOn0snAtg9r1w3QRs0A0Ard+qCj6CoP84/Fkm5+O2fW+DLQ9Z7Pf32QOvkiYEKeZjxr+3z4H221IgBazzt8gDoB7fA68EyeeUBncIEwPcH4IG2ygERdLNX2izJ84WfAIQBRPYkGeC5T7Ow3377zXXa+HP5BOz14slwLQQGfFNn8fEjMC7MkyjuPpeBF1eLn37/60+L/1r8d7Mewuc1ToA+XnEBGj5oCdRZX4BhIGQgyABEHnH5/a8vFwMxJaBkEMUkTILnZJCnWeB/9bfKER8RbLNwA+Bn4OOirgBZltEi6d4Xh3DxTV+w6Pxo5ol4pko/qIPSD0pvAlIdYM43T85E2IJkbMPpw6Jvg8eqv7mN81CxAAXvdL8tRPIEWKnKwf9mNR+DwOSqTID7v2XD8z4Q0vzULvZfRbwvpDkzF7XTOHXcOK81Zoqf4zI3Ba/pQLizKIPxczmTcDC76lEmT/eAQcAz3iukH+eYg7YDdCOl335d+zHGmbnz8uDQ5nPZvkrAaeZQeIASwKJRn/hzBv7HK6XauOpz/+E/oOks6RUF/xWVRw6++P/vGp/21Z2Qr+7k2S0sPvfICkYX/791TA9PsKxCs8SFpha0dFGsZ4TmxnGO5LPXnPWcDXhU4/dW5itcfUXtz2WegHRrpv94jnzE9TXmiYR9A8KgEMpDPvAgiNAs95Hzcw43zVwtzufyKz18AG54YCEIOwAIUEBz3n5dcH76VdMYoMB8/b1VeORIM7tprrpF3bs5yLkwCHzXAT7p4mau21doQQEEcw2PceLFf7BqDhTIMyB/AZRIQIqAkLx/g+zn06+q/2HisyOapzy6xR6UbfMQAPQIZgXnAM3hAup1zz4d2PnpIQSYUdTdbLsLCgdY+rwZNAGIaJt0M0g+/RrUAKY/zt9PS+e7wa0GtQKcBSqi7oF3HzU0w0sB+h2gA4ARUFJFUgL+B055OeEh0ClmQACA+2pQnxIft18GBY/Cm4nr68TZkHnO3As8S8Appx9x4/JnaQLkzWX09NrfZtq31WbZM3a2AP/Ail+fPpuG9yfvPxuLxVe5n/5uI/Tzv7ZXejC59scE+LSIu65uP0HQk32/ku87QC7oqWv7JOKPT578+OLJjz9gxccHyPxB+tPwT4t/TcM/iHhVyKcF/L56X82Pjq8Me32AQ8iPe+sjOj/9XCrBd3QFy1cFSLE5fBNg/m9U+HUI4MOoAYgFBj+psZ0ZdQQk/uACEIvP5Y8pP5fcDFXRnKJt9QMUPHoCkP7P0H2jLPCo7MDa/txNRsG8j3sUSBu8fSr7PP/wBtA0+Gf3bzM3FXNyt/PWD5QR6NC6JHhcgSr1v8yqPAX+/jcbYvlRLIv54bc0+3uA/bAI3qP3xT8X6Y/ICtl8XGEfEfTjvPp72gISBGp2Uz2b9Nz6zc3iA8du3Z9o9fjh5O8LKgCYmbc/FseL7Wa2/6GGn1EA3veA9R8Ws4rtzM7A9Nkxc/07LSgoYOSf6vIgqC9Pgvp7haiZ1f7AYTPbPz3wco6misyfSv7WL/+9WAO0J7Mkv/o0M/WHFwSCb7DH+bD4tl0B9rw2kI8df9mDvfmv81ZpDv5jyvwDzAFf3yZ9+8cPN3j7y9/pBRR74Cpgp1nWdyW/D60eW6zZBCC6e/6LwO9vINEc4F3nlWqvHh0MBzD0sZ37EQiUJFgcXD+LBzz7v+zeX1La2AF9IxCDYhskwAJvE2DozvNdDIOdAN54sIOjSLDZhlsf9R1vt/GxrQvvXBfdwD7mgkdg4Mb1gLxnIX6ZW69k1gzDt+EKx5EQhZGV7wchgvr+brPbeNgWWTm462Auhjvu96lZUvovc5/mzb78tpGY3fKy+vc3d4OCkRzaHojnh4Rw2IWMras0LmSudrdpbNtaR/hLLSM9E9pHubFUm9lKGziu4ZVmVrSdqTIvacbESYIMp+RIbZlTT+NTuAzFTBZMl/QZfCPvidWQ3fnsjkHS+l6N/u2W+fz9GEC6wTfWpJ4TbSLt80HL4WqnbflGsUoWyzIhdkPbodv8lHJrCO2PbdPpvauYmNnfFWGT0UZ9U+tTt+RX+S7uGDa9bcV2uMlDaNbTjnHaFQMLbYX0esIkna3eNC27MJc2yhimDiJEuWXj1WZwRthXRmDdL0YfNZdid54YJmHF/CrXbU5zB28SVnutFKMdc8K3u2C1RhPrKvVH6N5hFTdIF/asm0SsppLEnRQ7Tir13BWHaM3GMASFJnbdLE/r7WrDOMtlYIbLaAoD14ipjvJaLXZcifT6JIQTGqX5wstzRhLvIdmOvXhbZdZprylj52HlUNb9/jrFBqwQonCQkzujVfcKOhWXO12vDwV7M4KAkQmPxziL3shdKvB6VpkamkZGrznloUUpBx37VdpgQdzdAp/dRDB+h44rpK8yfcU6GZqStL0xp3sk3Ohr7ZFZnBYHikzYRqKzC+8Lei/l9Og4MAfz5yE5OUR0o1uir4iE3yrb9r6droGBy6NXn+viSiWwrmqqE09lhBrMkWGdhM5TQ1EwiZ14yRSLs4uuEYtxzapOxtiVCFxvrnuWU3Thslnt9Ivtbgt3VWz9A4Ub3IXQmJhXDUW3yauMq1errQxPls89z8VCfV5ebOGQjnJw8sULu4k9peTQ/bhRB7UKi+u6aqnzpSJidDTpE4qYKpJYW31VyBA9xatmv5IcS5O86/nQebc2uTpwCKvZeZPWh+Z4sWr9OgSb5iISo2mTa27PrXTGVzF5VberYScMOHvlIYTfVQFhmqgMOcRpT+/MnqYOLlNOzmbMq7ALjSUDpCfHy24jpxHpsX6NmrXUpuMmWgptlNuTycV1tqqMi0ES1Z1KdAkt3IsHMTeI0mqDDaxkt9zxOHoZQBZ0arqldgcwZL2zQgszq60M683+pir2nrflbktUq66Wj5xP7teFxoTXiu2PR/xSc7rIR+HhbHV82KF7CU01nd9v5CK0pVK7KE624q6dzI3dHpl8R7wVdE6OmpvqOh9tFDIWcpzKRpTcielagMN1GDLk+oBVNIrKUkro9rTxTNa1UynDxmrjX83itBKaER7WgsP6xtULqhvlXXcOLEAHWwgZh3d2uWUpQm7fqLJd1hgrZ22e9pDRu+kqUyRFyRTkpi9dq0iRq3Nz/G2swDksucuzg67tHNloMWm2zjJsJNkhNvSG6acRbquLcer5JJKg1f2gHJadoklrxCT0VM71ZXbqsxEOJy3m4UFXUlsLFZyy5bWKKgZKofT22u68W2C0I5XCSLGstisY61QPghVBrfglrZbBaTfWRqZdGwm7T+JGx3N9ulw6Dz44imCoNE9TQSWHso5ccmXV19WORMtC5qDaQ6+4bPP41jUPAT4GvYCviXXPLAPMIPsSpaJKhOwwABDVRUZHxbjE8feh2ikGSyPR0mP0iegqPD2bvK1wzHFDbuktSphpJd9dS0LRhmJpudxGS7ff6dIJl++nIF0mOrJmnO6+7L1mkqHzJB5PsrXv0Etj9xdhKFE52ZqSjN8O5nS+iWITwlPAMlNGOyDKlMeJtntWMky/73F0C/sF4nvCSJB14V8q/XqK17uaQanVGnETUt+SWnY73XZRsFc8xXIRpScaJGPZI6lEJ+FC3AiVFpHW9Yd1mbE4U7Q1qYx5zcrXaZ0Upr2nItqlUWtzFVxWaeDcVXl1PCTEyb6sJj6nzbwRCZtj/W5dtnKbpbxuExbjWAB+c4k3DmYAH9aZTGTnnC1SD2DyLvXNI290zgESOjcgtnKR22NHT5fa5wAdpqftCgtCU7qpvSC7OekdqvO+DEKlNqgSms58XyAKwhF0wWC7a+RsIaSiw7RnS/ecJl2mCUMUwu5pKEfnxHQ41EH7HDocHdhHslzmnHqLVQZxPOcJ5YolNHpwwxodM1500FALUXrofXmJc2gcX6/9+rKHPWsHXfjVhJcXiLqz1trKs0QiBXYVja5NnVB3FxLXoN2dB8PTBg0hK+YeY1OmbXK+b6081q/qXUjplo3Een9bWT58xhpJcQgV9fFux2wwQ5w2uynGW14MsKV65I6TuHMm54Yss9Fg1xU8irf0PBaVo8WSudJvF6rf+mexOkrIpjw4NLmj28ATy41pu3xGMlIj7reUokR+rh+D9dHAg4iwrZ0uH9K9ZSzPqlSokNdgCHrdJrRCey10O0OKcSCFi+uwLg5F/Dawo+XyStFXnZT2HqGQMKyddFOl9wrKILegreCd1kYMY+wID6ZgDdVWBzzvpkkhImqkV5VbZLCEZ9rpDsJ/Bk2LblSGFmYHlcxclGQ5DpWO5D0APYShuuQNF8gNQ2R9ghyIK9onlCBpHGMSAGm8PRFvSFoopMaAcXFVpJfCGW32FgkmPVrouNxuEDOp+PCqWFoTF9Z2v+Wzsx1xO/y6UijsIEiXYAkP+8QaLLhyjtWV5XljAA0Kqd79VLNSml/fTUYUi+EaR0ZMd+JaHfbEsPHp20kpagplyG2ZuHFhtENWHOEpS3YArxSUo/PDmODxqfA9QoC1Bj1VtcUQcKohB8BqiXBUDg7iK9kJc5crhTwpVwrkCoTnuE5TQrS08hMbCHXWFvj2IhrLJjvkuK/rbI8V0sprLWkn3ncIcjLp1j1VBwDC1zqGWk461253OzU6TarDlkGc/qLuPNG/uScyZNxb4ddRKjTD2Zma3SCRtyusapKrt2IGtvf3vXXUIJRYnny1SPLSaXNwEcmjkqzoIhdgVUqzQWHuZ8NwhbVI3KYrwJ6zfES0laMdG0OV8TsaXLl9fj5SNl9eWpq9jCLKWxv3nolln8CJHg2yqjnNbnuKicxBqApztTQd7saBsLRBlrh7UMrIBBCDGYlR4BuiLQ7XC1IuDXoZncxUNLuALi6mJyEcFK6Xzr43DEpaFdgkUxd0G6zwbqDXhhNhLkcr5763qsOulnaRfK7E5cb0mhxd9v5dqbJIg3X9vKpIna1N4xDRqrM+sCQrCZPTu7yHxLvKkz0AjOxZLOEo5jeSZITsfQNr200e+NqG3QFKCnK8K/YxvhPNYbO07gbocyljy1ixFObXfGDLNILpY2hbxFEUYE450JwBqfjlGNHLfU1x+p7gdrzj3YjahLszmkG1sLphqKBuSde/prgfkQamYVHT+FG39v2bP5jrXoOmZjgcWBsBnfCQa3iLXBpk8J3bVWMwn+AG8XId4eogXY6wci3JztOXAEfhNLkwMkhfz5FljDVH0dIcNbMPN/3uEIZFw/xknxUlZm1yq2Ge5kRxiVBnJSoKBpWmlZWwES9FN/m6PfcG3m4ZvJpg4MLY7e963qIWnERLE0oUro5AAiFce8FPgc+3mXr17Wtqgl2futa6lFW2HoFeR0ulx1Q4CcFO7Uiux0FjwJ+EarLI/HAlZNup7vTZ3e3Wh5CzKdfhb7AmO/rRXfmCpdNnvx5RuD5fVpRQVfvQOxdGgScQCa28OxNcInRV+FOIBlnfBztJtdmNLslXb7QOatjvj6v1unR6m7DrqEmSUbvQhYKel0MFaemFhI/L4JByVUY6wzm+GEFdGpdplTgsEdjbM4Y6ySll3Ikuii3LC9eAhQcs7wjSlCNH2O7v3p47Yq3RGKx4u13oiSgoM/RswiNxv0FOzAYXyR5Ue6RHq0DlXGhf7FPbudMhtnG3GIpAJE7YscpL8T1SKbbdbewz2BHj98417f4KtYGK1AeNijlMZApGSNU65XStElVs30SZvpbLAE87A+pzDB7aWzQkHTHhboBI2+Aqn4/0iaEDX7FrwMFc25L6JUWJzvDx4eZMmzUUdOkGRidKvY6Hm7rnOsvLRg4ib5Sk9XetXS49eTCZQ+1py62x1ddrHS+D2if6Di7a8HDVpiSFJT48V83lyMZ+gS0T+FbkJnNMr+b5lkHY9lScrPbOkK7TiClGh6Vhk7VIR42+PuGIym0uo1Yzut9dOYVLI5NoAn4/bcT+OBgrQi8r6Jz5MMeU+k0QCPVqkraPKVVCESEcXFzG1xuWU6uoFqYxg++hze6ZZER9oiXbiRorFqMOGyMTWSZtp6Yuh9Y5wTyKOsOOJ67ikKcrYhkmk6kXOzbiLFliYdTk+B2xnQqnK7TuOsYeYmcXLA22pX4/Xyt7uwGbEPywSSMxqVsygK9GfbJofXmzd/WujHcG51ry2rvyhuu7x63IhT0gPyn0+2srDGlfN7vuhGw8/G6c9sLOPeKezwZI2kUb+jYM/SCj9pW9eNJqM17TUJuYY43uagdPbDzzzjSjYJaGjcvaPA1396BzBir4d9Bvh4xmL2FzG1tsTxbaHcIbKoLOR7R3Kr+CsGLDJYRZl+KGtdP+fsPPXnZjzCBO7K0rSm42Cm4QGgm/NtzRFcl4a+zTKTJIHHRkuVS4wdZFhtuJut0AeXUmu+oKX1YaW18elhA0riDrekpSSimGAeMgSiWLAwJ1EYP66uneGSgtQsIkbLXUpnBky8SEV4Xx3lyNoQ4t49Nh9KhaOk+bDe31UXek423BoSx5Lm0ZkUWIOZR4jq7qymi8uxhoEIMVVym4DNcTe2OwcT1JN+WKFxrm3iluaVmWiEAWbo8QLxSopK33l4J31jy7tynuvFSW/rapmhpraMGob3s0jB3Tl+LiPsqkUg/iVWHh5WHaGWecRZrVoPKlaOyECXXwXmCunKnlt6njJiNfFiZsbd248mJTvSSsTZMCJnLUFrvx+touQloSGSJ1jLg969nYcfZBDxCnczZDrujLys6nnMi6AZYSmfXLIIXLHIdT9nAWIdE9lfeIz1eBKdDBwZCRQy7ognJwaYuz46XS+pllZw29j6wRUhN5BXl0e737pHSP2kGjL5VtVEgHNgeWwkaX8q4hKb8eTyqdJtrJ3ZxDOQqmndeiBxPO1SOEqaeynHChLIPAovYhnucHtUhtWA+WonbAxr1VmuGmJqlAWQVMDl+scONSuZEnCUq2S3EoA5mgMk9UZS8IMmmdI4BJIrHBNlRsFU7WwtEqdYXlWeKpYJ0RO+RK8WU/WDi9hmHG5ZugCwz0Uusczer4et8lR4qL1ptz0lx3FFdtUxl49t42S2tqPWcH1+lyKfKi7IP0WK/XYb45X6V4jdjYEWvwyuDdJJ5YNvMr7oD2BmoHw20cd1NF0N6mdDbh/VZhMRGop3WF1/nh1hzqE78hGG5jDdeLIlyprT2J5OCNMRYhQ3uUpRh14WZb9Oqu7JwdA8pxkCu2llMrXpdBiTf5WmC2/J6+N+t+nbl5ftmvjts4vPOacl+fDA/sRN0tpOUsxI24rmx3sA/av74XdVBk8qCiO8HAumOnq6y5uZgcw0RUeXWddS11a1bzO6Fe3oQ0NvrTShSOVHNgqREpU7QEw3p8D3ps3whTlGd2cUbWvG7F7YHOpHjQ+9t1xY5OKtaIa4TqlCxPIbXXXaIuDigvLb0qS7fa0Qvjk3S8wWTMcjtCMC/a0hWJM7ryNnbq4uIxNWQdPtYVHpGiXFPQ0eolbYmBpmK9Snq8yIJje8qbgp8Gl2ishoeEHk+atYx0HSWNrLNcM/edRiS1cLDbpmVOuLLlDskNMpVM6fKGwJTliRvyMMSijoXzsNYvQUOpXemYdozXwT0/IK7PxqcW6XkuAVx16TpBbN0JXjWOpLumbN6EJufdvTEE451ncNm4FY3GSBmWizGAS9BDsRe+u20iMxRU5R5q+85R+X63G/BEPQgVaotUewz3g90ROLQj5MhnDm0OGRl5FThQHhl6vOmoLin7OkQ5L29NI7fOZUtvY+zOGkZ233WJ3hg4TFXCFg8VIqeK/LSdYmWwvPWyyQ9h2BcXvoX4QDN8o5VVYjpvxn3NgT7mjsW2RFUwtdxBmHm3kSZZ3XarlWZMBkxi7sncBHjXHzsNK4851Nv6vRF2bS5y6XV9xbYxdxq03gH2csLJksxzIVvLimprOEYtRzkYHZ1vMLi75JATuhVTa2YbFvvJAP0p5ppDkt5kkRvUPe8WhCVk98w1g2BzU6XObZMAZRzOwomUjhzMvuzIzCD988RX5fUSHEcC9dlhrLIl4lz8EkuVvDxxGFkvY/+UOHcCLk3Xcyk54c50cL/p1Fqg0P5KbcaxXTZXeVcOJS/jsO/guV7u0MYkoLopHUBp4hAi+Alhh5VLIKCIiV0fUPv+lNgR0papWyCmSeoaJ+mSs2Zdu4H4yh0GW5mY5TIc27trOLpz13tqO3pYMqyFtWeseglxLB1NoeLgwDdDNJLTGuwwVpbdQkgCYlqvleMmc3v/pJlFdhA87E4o61YnzzUBmL/0QN8pJIRwWWsKJpo1Za+C0/FaOTtnyyS3DKUiO+ZGJNpae+csgwrehDmxJCbQ+nOJsib3IbwhVmu7axW3W0IsjLXEQQvQutvearjfqaB0VmXOZRXnbO/7wbr3KlacEpM8BlOpKdq4JbB6mpj1aoM1HObjUApFq0MZRkcagyaixpfhbV1vsSH3bKi++Msbz0E3oSUVd22QS3nKcA4i8ENwPiKrM0EQbx/evh8+vv2Lr1TNZy7/z45+nqc0X1+UeJyfBY7/6bHWp39Vsb98eGu8BKj1POpq8z56HQn9zUHXx3/uzHSWMT3fWPp6Jvo8Bu6caH6z9y0p/b7tmulLW+WPVybADLdv5/cA2/lVUQ98/3gY+KNB4NLxHkd9X7rqi5+0ddXON2cdmiLwk+eY+TJ6HQJ+ePNf7/N8WW+wL0FTzya/ztyBpev31fv67a//Gykhi8uZLQAA -->
