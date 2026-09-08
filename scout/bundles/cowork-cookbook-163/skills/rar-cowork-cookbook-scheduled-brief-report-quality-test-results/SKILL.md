---
name: "rar-cowork-cookbook-scheduled-brief-report-quality-test-results"
description: "Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_quality_test_results", "rar_sha256": "bb7d33064cd6208a938fcb4874aa5dc409336b4afa1fbfd51ff32005aaaed920", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_report_quality_test_results`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_report_quality_test_results_agent.py` and in the RCI capsule.

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

Report quality test results Scheduled Email Brief — Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am (daily or weekly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 bb7d33064cd6208a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_quality_test_results_agent.py` first:

```bash
python3 scheduled_brief_report_quality_test_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_report_quality_test_results_agent.py   # or on stdin
python3 scheduled_brief_report_quality_test_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality test results Scheduled Email Brief — Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_report_quality_test_results',
    "version": '3.0.3',
    "display_name": 'Report quality test results Scheduled Email Brief',
    "description": 'Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-report-quality-test-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3da882574219c9c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-quality-test-results'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-report-quality-test-results', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am (daily or weekly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where report quality test results stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on report quality test results for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report quality test results, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf', 'example_request': 'Give me the morning brief on report quality test results from USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am (daily or weekly).', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a recurring (e.g. weekday 7am) report-quality-test-results brief for the responsible owner, with an unsent email draft and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReportQualityTestResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReportQualityTestResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am (daily or weekly).', 'type': 'string'}},
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
    print(ScheduledBriefReportQualityTestResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916efea2LrmV7F/d62u1DUJgwySu85ajSIoyiAgIJWzUsyDzIMM1fXde6MmqTon53bX7f6rzUpU2Pud3+d5d/C3N7tro6J++/Sm+na+4Ow0jSO/Xti5t9gWfVHfwFtxc8DfhVvkbR07XVvUzdv7N89v3Dou27jIwfZNF6des7AXWVHncR4unDr2g0WRL2q/LOp2UXV2GrfjovWbFlxrurRtFkFdZAtmzO0sdpvFisAXO0VevEv90E4Xft7OGy6qwP78adEW5QJfxK2fNQtnXMRZabstuOrZ43tgbpEB8X6zuDeLNvIX5AdwfVEXwB1gi333azv03z/cqn23yDI/93xvkftDuwBygA/N+3ljvmjAYuBHvvAzO04XXm0HwFl/sLMy9Zu3T7/8/f0bUJ6+ffrtzU3tpplj50a+16W+t5mdVh4On5/+asBd5ektEJPaeQjWlyMIeg6+l34dFHUGLnkgWK9v7xo/Dd4v/v3fb71dh83Pnz7ni9fr89v8R+nyh5NtYTct8MK1S9uJZ20fF3Ta22MDnGy7Op/z0YCc5eHH587vkkA0/zbfe/dU8jH023ef3wpggj1H4/Pbz4uiBvrqbv78cZZSvvv5Y1r0fv3u5+9yms5JfJAIIAxY/fHL6/tLLFj4fWkcLL6o8m770gXyEJc+EP4H/+bX0/SXuFdIvjwXvyvK94sfS579+Ruw91mVDpD7Y7EgBmDn28ekiPN3Lx11cfdzO3f9dz//K7Egwe4tjZv2/0juL0/BkW97IFqvkPz8/pG+vy+WL9++yfzXaktQMH/FE7D8q7pvgfpXsh+Z/QfRoFtA8X/N5Q/F/WjD8m+LX/6lb//ZhveL4PMb46fx3KBO6n9a/PYokV9+8r5f/OnvvwPR/1sxatHV7kPCl8zO4wA03pcvv/zUPC7/9PdffupKUMW+nX3p6vRHMn8U14eeP0Xwterdn/cC/Zf8lhd9vvjWQ4vfivK/1b9/XOgACbzv15tPiz924vxaLmYnvip9huAP3dgAW/8Qx5/ffgcYlANvuid0Afz4t39bCLFbF00RtAvVLToAsh0A0MyfjdeiuFnET2isfRDXJgaBfa0D9T9neLa4CBa//g/3gfsf3BfuQ81XdPvywPQvT0D/8gL0LzOgf3kB+q8fFxpQUdRxGOcAwhValj/nAHrzdlZfgmV+fQeQ5Yyt/wF09of5wyLOF7/+BS1fHgI/luOvD0CPn2iobA8zEoIV/sfZZ2NG86eH7gzng+92QFdauMCwIAZg/n7moSK9AySd49Pc4hQAfgywBlDc+CSLLv80C/v1118du4k+50/oXi2e3NdAYME3cxYfPgAPgzQOo/Zz7rtRsfjpt99/WvzPxX+26yF81iEDMnllCFjIq5K4AB3XAaoCTDmnG8DJI0O//f6KMxCTA7IG+YyDmfzmzaBib773Nejqnv6A4sTC8UGw/Zk1QVBnSozbj4tDsPhm74umZ8aICsDQnl/OFJm7gLEjG7jzLZJ50QKSbOMmAMTbNf5D669ObT9MzEDr2+2vC2ErA34qUvDPbOZjEdhc5DEI/7eSeF4HQuqfmsXmq4iPC3Gu0UVp13YZ1fZLR2A/8wJ46et2INwGJN5/zmdK9udQPRrmGR6wCETGfaX0w5zzxcz9ILHNV92PNfbMotqDTevPefNqBrv2H8MCMGVchF3szRTxH6+SaqKiS71H/ICls6RXFrxXVh41qPwns8+3oWGxe0waj9lh8blDYQRb/P88Ts2BoTlO2XG0tmMWO1FTrs+EzRPmnNjnUDpbC6r22ZzfZ5yvOPYVzj/naQyqrx7/47nykebXmidEdjWwTaGVh3xQYyBhs9xHC8wlXdezq/bn/CtvAM8WD5AE8QZ4AfppLuOvCue7Xy2NACjM37/PEI+A1N4cG1Dmi7JzUlCCge97ju3egFX13MavNIN+8OeW7qPYjf7k1ZwuUHZA/pz0GCQXcMvHb1j+vPvV9D9tfI5K85bHGNmBzNQPAcAOfzZwzloftwDM7PY50AM/Pz2EADeysp19d0AfZe9fF/3ar7q4AdXyTCuIq18C6P4wvz89na/6QwlaBwQLNEjZgeg+WmqumAwMQsAGgCqgw7I4B4MBCMorCA+BdjbjA8Df1+T6lPi4/HLIf/ThzGhfN86OzHvmIeFZ+3Y+/hFGtB+VCZCXzSseev+x0r5pm2XPUNoAOAQav959ThMfnwPBc+JYfJX76Z9OTO/+2qHqQfGXPxfAp0XUtmXzCYKetPyVlT+CroOetjbfGfrDAyY+PDHiwwsjPswY8eGFEX9S8fT+0+KvmfknEa82+bRAPsIf4fnW6VVmrxeIyvbD5voBm+/OiPgdcYF6gDPtzAjpOKPQV3r8ugRwZFgD8AKLn3TZzCzbA1x58ANIyOf8j3U/9x2gnzyc67Qp/oAHjzkB9MAzf99oDNzKW6Dbm2fN0P84H9Fm8xv/7VPepen7N4Cl/l854c2clc1V3swHRNBPYIZrY//x7QEaQzt//PPhWXp8sNOPC8YHAJU2f6zEF9PMTPuHhnl6C7x0gYb3Cw/EqJmZEXg7K5+bzW5A9YLCnb1qx3J243kYnMfHByd8eXLCPxv0Jw5h/7u6FRZ/IhGAhlXnz5ALzq32g3vApZlafqjs2yD7z5oMMC3Me73i00yc718QBN7B4eP94ts5Arj4OtnNGvy8A4fmX+YzzBzzx5b5A9gD3r5t+va/FI7/9vcf2dWDOvtnm0A2S8BgjxH5sQSUXDFH3I/vL7SdeWwu4SerPbruh55/7cwfOQ7Y8Q/D0UPG+4X/Mfy46H3/NhPui/wBN7ULEpT4Ow9oewxA84p0/PkHOoHSB1oDzpsj9D303wNQPE50s3kgYO3zPyB+ewNVa4Mysl91+zoSgOUA3D4089ADgR4HCsH3ZzeCe/83h4WXqCaywYQKZDkO6a1WMIG5HoHCa5tarQPXwdYkZtu452IwtVoRDmYHNhI4gYcjQbBCYRi3bdv3KHQ27dneX+aJJJ7NwykygCkKDTAEhT1QqyjmeWtiTbg4icI25di4g1O2833rLc69l89PH+eAfju3zLF5uf7bm0NgYOUeaw7087WFKMSBDNIZTyZkwush7S9VZRkF5EzOMXHNbAqDrcg0eFtbbNia151zU6WjfQC4LhR4yEkRQ9E5ycuoJ0zCRdW5MfdWraN5/fWQuZIpZ4FMSpmzz/2rOKWGxx5NorE2R1NCdpV5LbeEWpStEx7Esap2kcHjSGPxS77c2Z2+FIIAiglfz3eqre5ZMb6rEoueeAc6Xpqe0jJKt9j74PDB0VGGah2kUDCC4Y5cKwWstpbKX4z2uCNH3L8PiaxYeYrdGiVFq3owDzmWwV0/8PKBzJwtn2YGvjGNejKLti/W3uUywYbCn/Ph0C7rc4XpybXrvRIQ3FiJzaG9BGrIEoJiVbELC8rFDklO1reJf9W1A2IwPS6Zp/XSvefkQEG3fg0tnXYZ+Ev/0LJ93Le9rZ51J+e3HY+kihHuskYZ0767UnjvMHHlprChZthedfrGOrGkRdsddlPxgxKdI0PXw9N+4peeYDZ2eSyjxpTrWD/nW+WyJ9OD1GqSoEeH1Nv6g3zt1/HoHuppS0x+khIElLjqCY3IVabcdb/UdjKwKYxvTUNPRJvuCi8udRVOpZ3u00c2Fg3Hqm4qeildZ8n3MFXIlZ1fdwaieuGYWmC0kod4XXqo5WFkjiRqs5f8I19FN1HZ6RS7773TNowZU0VM3XVCezwdWsywOBW/9QzEQdMtsamUM9a5F++rlIb0muNiJfLOJVblI766QLVoEOqeuEldH/HbsSrGemQuLZ5feD3n9ZuzS7DoUl3LNhcsbC+fusxK3HMnjKpL4x6vVedgdXFuxubgRatk68LgDJSvzQPPOFI0rs77BGOPvccYGcuYx9umVnsRG0E/I2qj2EqCportMMcOb6eqjtPNhrrx7noXRJVAsoZpe6weYKkOt2tQvadIaaCticWTe5bZfcPE3HR12TxSCAbPvTZxIbaMh0m2IBH4eEXz23LFtRknXibyfOJSSd4gtMpUZ5i79AV3GRohi7trDvb1eNRcatoXFD9YlhCWLxkxJwYLNZfnUcxhIgi0E0SrB2PZYpyvTjR/OuAWvUYiRMFZLoINN13VWRQq413FzgVDX/fj7kT6LinRln9FWHU4bkpcUnzsYmc2yR9zDeSmtphNBl02acvDRH/hKkjd3dq94MZtccHks3k7bwQyCGF6zSYugxbKHmuRozMS63Pn4KmYWVc38IfTsL+yOiZBk11xSeWdNFNdb4jtdfDpqjND+awaJ1g4qXB9UU8rydCIzmz8QStlfIv39gRjAaXu0g2HmL5m5uzeTQvUg1EssLq0A2k1uVq4R6udrTtb3LS3U7SVU3d75Ea4SAIj9A7cllvuVrImjTdtgDWM93ntIIwFxCqsWhLs0b0w7OXSU6RHTabbbzHFuNz2t70axvmINfzIcidIiqNVW2tcjtcj2rLJAN2yrX4tciek9y4aIhcpJdHuGLfl0eV5lINpAPIkQB983ZZXnMGwpb8PCmdtW5J3wjGLFMOdoPdDcPCCDb00/DPbMa2gBYytLCetoamTQ7d2LfIcEpNoeBZq7eiebTNk4XY7Fc7tdhhtJ7mWmB7Uhk3lUe9MwzUTeE9nNmvSY0sV0BdqrXc7j7tsEXkfEZKLkVfB3vo33VBggdZcp8dH95bDuwwp85u8lQjKk3AfimVVlahj4iXs0qbxWOY4MeKno73PZY876CsuCEL6qkrcDT7unETfdlGRnPDRSqQ+5LLpRu7gJcQi0Q6gMsfGV3nchVtYYdzdGcWE6RoeivsVZQnI7xrnyiVDyp/o680CtxEFts+niE7W9tHRzhqGBEl5RbprGenhwd6d8Zs3HFneZHllU15bj9rQrQz4wGKVLcSaNjSqcZ2eY1MLuWWEJJFCSwgztJWJyojd5BUSxlt7aBgLdVsXD9sb2uMHtIeXlFQ3yyAwwby53olouIfjKe9d3eaVMVxb4R3eRAo+Jdy5tFBiDWEix5yGFt3tyD7fxol0DqA7Y6UIRa29LA/6CeL2eES6pbTuqmLSBCjlhs12vz2fLpetK4uAlkolPyBmNcU7QB3cei2F+W4jtibMYVzR3UM2HPC21Y2jwBTJtAHcvI9AjTAVrQ17uhw0WrsSobfZXTjljJeyso0N1rZSyeQ2tnixVGYZOqLEsWkcIFLUXVwvd47B4Df6dOz6raFgBtdzPr5Pnc41j6iCZhU0oQaO6a6HRNhFgzfyGdOI4w1T0S4XhYNmNB16bvDD9XwrT2y4SbiohKySt2xW9os4H0a8i8Kz2wR2mJ63xyMdiuLE4tJxGaGHG3GOD7m2xyXS3g60ZYTNkNNWz0In9S4WNK+pXGDdu924gXblhdPvng5V+i6hdcBU65i+H07XM5LlTH/FjG0sVMHWL/cpbJusepYwvgWwzldOdKiCCls1kcofU1Qw3ODGxdtbjXEHeY+JyXbw44ti2E48UBJ94kze3ccuPQ1eyrqGlTF5L9JyrJwUhmI4thpRuJ48q892wr7o2dPWkNxCSynMXF2aTD1IsYolZycU4SnV+2gpeho/FDGL4k1UQengM413GZgGMXlf1AY7DW/9/kxy9EB7Aj5ptl4QRcFVWxZTK2Z11BDifFtzgA+LG6P4FqrxK1RL436MlvtUKfabWL1dlWWfT1LKs73IbkK6MAcXzCfiesfFVhzDA7dJTD8hdEgU1Hxnh2tCDCJ1chWaGvaOUFyTdRMvcfKgSFN9Upl7TSxHm/GpvOZoepLWgnhHB0WM1vB151akeq+l9iL5KGywUqKL521M+jKzJClh6B2IOxDhdFoyyuliEggCM/be5PMQttqmSYwVs+FxeeOGKo0oxEbeT0Z9LW203riKpbLXAq82ZZ0st1a3llG6q/jeGcNDNF4uY0bJURH2hWZGFLxO6vXK5tfL44pF/fvF1M8y41i5CMYSrReWGysu64olHIM3thSON8VtN3G9Z57sWLAgm6C324zviy5A8Kw/lR22ptn0fDywKa+rKHwflf1NJNd8TNXhDbXJ6D7eSYhMb4aeNqPHd7rV29dJJBUUpTTK7umTBTE8MoysIlc8dKP7lD2utmsEp0+VuV5bm4ByO7fiUloVkCMxHmX5Et/6M1xHFXYrV3YgFSdJM/DowtBoSK5WB++0EQOZkYumzSHaPVYX9hqePLM96tJEnzIW48L40NQEnZzoodsI2b20LylV3sL7NJ2NYdIq2CzWVGuU2Ya9STi2Lvxd2LUBdzhmtyTK2oPbJPp9jUUJH9vmfTyHMTKUy9MKSV38DjNZGU3ZRupXW+QQrwe3ujs0jXN5ddwUyM4tg+WStyu1qwYDCWiZw1kW2lAXVyEkpICnc4xeEWosTSm7xMuy7dEsK/TVcTx06bA84eIxcxE6ULmNgbKFg16OMb1NisYuVnHIQpiHYeIhm44aSZVsq/cbvhmSMJ2OuNDejpXi0KfBHQ/agXQtPUOGc3jh1gaRKasQ9aq0tJg1thumgNqzK4ZP0hDL/PoqKDW79e/RoZetvc3WjekBPDY8/r5Tq6ss3Xg4B1Yb7NmjwEGyxdQLvve0seGsy8pxWulwuZuVHl1uxqFXBVxuUZ6LV/sVky0d2KvYAyF71fmsuQlONWgBg6FwSMU9csxiZTlG1QZNtP3mtCu0q8kxAntjmX2GnqXJyOrjvU2jWuqK8gRDMbc9KlhMqU13Rm0woodWJS2X2NU5StdLyPaCrZ0YpWCGokziFEdqUUcYrwOFoxoZdZY0HWqTsLjVOs1NtYk6B6K8+pU9Kul14zFtyp3PVgMZNlvYqG0jnh4Z59i2JTqG+ijcnEZIOPQkPJnQ0FICgd2v56ouUzLPjW7VBPDek1Eti04uJahL0ERRmBexiF7r40a69fiJyCq9OkA+TWzV6EzVkkB5tmZlFD6ewdBVsKjZuGl4bfzusrpgYbZdXTFhk4Pe4kxUuLZBdqU6n0n9AEB9YRAJPkIhe420VmjISYXH5Z4yuuN5J2qsF4iYz93vSSrAOtKt4TPLbkf94uunge1CDWvaPVnWaORM/VjeDoWr9IzrmVXkZ3CFHCAj2G6Ohbelx5M/bXBjyHNrTR/AaW5TMvAuWFrFTk9qBRALz9/pu1+Xon+rLEogTTMUSwmcVLzQQsyN6B6L4Wwb+6LR7ueshgixtNITcwsLlj3Uh7u1tzhR0DIdFkSEqLBJP1e0sdofp9xfbWrTihi4WvdjV1bLs9DrJXMoPaPofd/DkNDxca/pXAbSBcJBweRCdvx0yoWeyikuQZfRkEvJ4HFL5eQh7dLDD5xK0LxEBLWVjxwP6SJTDnK0vrSRgzHucZldB5nsg2gtbxrjBJXt5ehKvkgpR43q7tLF2E+aLI2QeVJy70Zwy0FwTlM9dXIcg0R4foeVJi6zGhgxULuxDWqUDsewHMFgTNWXk7iT6Ka5m84RJ4tNyZOblVdVWD61IUUMV4RsqRFCWS4+7vakgEdeAGC031pn/RzZ3abRU4e2WpWvUHSPNGDGBhVLcYFArOCTKABQgTZ7UfSWJ2evSIhiu9q+cIxtV5PnbJ+R1NI99rCX3IdLk0gdGpjwumFXagBNlAOFCoebN+uoZcQK2mmjAKNN1Pk4ZSIkfyVg+1DK0bI0rQtxxdYSZTvwPhWnBrlNpLpeKuJxJTI1tevw8MoU26MhMvtd0MNuKKkO5bfklV+tsmLF1kbdj8LS3R8Ty0yayTn7XnRcWvdQQqPLSbiPq4yRXPw28BHeU3tuia/h3eRne6rk/WvrCCXtqkxAmMSSJJtyuk0JfjLIaDNNbdtk58QK9jyYKTfOqbuuOJzgpSXpHW22zFbZPmAVV/DlwUaSEEuV5X1v2/rSCNCrE4RjSTb8AQ65chf6sjwZ3MpLrfV1NezUTV2hyD7bpQiPxYbD5gi4YKSYu20NwR2rnqJtkbRihQSydJOQLa0f14ww+UusHSSIxcGwhIVX8hpfyku5ixoldLOA4LQwS6qUDmFG4gjXWN3rMIK4pBw655JVt0TUNgWHpNqVj3l4e106Rn+VlrtlZO13jQ+7m4bwgxM0rqLN2BBnHyJNAudlWb6L1Go1htmJEGgF5AVfkvdzzuU6JjdOvfKaaQPRmBwTRCnIlBitjmVzuNekHJ1IOD3gML++e4K7nxTYG28GFtsgm5hzyizOL1oWHpOamIQ9dzocrjrecpx1B5OnNJnmOW1S0aaIPg6aAism3+ud6zi0mLjEDhVxp5dLeTs1qu6RNtQITS7dRfsKdRqnMbln2yIVuhp11TjjYji4gxQA/0pHTUeOq9x9fsC6rLf8OzoO68Gjj6cqtMlkihoyCo2zDBUQCA1RFZkwYAK5l/SzfoRUdY/21DWysLOD0qLsmxO0HcJl1tpLeeracvJbml/6uEpw8XWAMnBqvZw6119ZKJ+ZKeXuOodD8ovbcQAUoJO49ahkSOg20H1z7FUPgZxW8+ONad7ipkKu2h3uODXrTLXW11Fq3au+oa/ryVEpmRoxjGpr/eoqBWbVyVXWMoEEpxJc4DH4hFhwDe+8IT11+Tqgb+SwPajIQboFl1vlEf2qQTEn2gpjPlRWuyIPRQnJyBBujB64LY8nNT62wnJiMLF3fdDWkZYk45ZNkhLaZdvipkqIts5dYndEjl3piieYUYaBD3CHHYr9Ulka2WU8JsV9MxyQ0ODj2ulhwbxBqekPOplBXshQ8M6WsN3UXLzYYogNz3hMEEdyZskJgwgKal/uGrshQAiDvujvk2y3yRE6xiFlcOC0tb6PG6r0af2E1so+ulfevQSHO5RU2xPnNg6Bwo4hdcg9re3SVIU0qfflFQfTujzZPVJxtxFb7YO+YUKzpEoBJihs312sI76qtshpuCBDp611xdhfbgJodRHQVbYKjaHf3B0kbuwzpIU00jJ9tvGXJV0sj34tuyg4y59qBd4BgJYw3x3y9C5Ap2tqI3fvTEwdpMMaruBKvjwr9AqRHFIfYblbmeKAyuH9qMlmwhSxcJMa2j7LQuit+yYGFV32FISbedYMuqnuydC6nNJ7vu0Dx4lJXdJh4u5NR5843k+8tsGIluh8zELcWzrZuSorGhlX+IbvM0Ruc6nZM8zI0wjWdJHnXPAAzdBV5Egxlaz7o+JQRJK2KkWtdlAv4acdW9mbPtMkpfVxKeflbNlNPJnoayWCE0zZOPntGl7ifpXsFFFY7jVQrUwL23cGHABI1RGXtmuV2jSe0WDKNYxr1qKFoCtQjcUAb/bNWj9TY+izqXY3JAAznprH9nJtQW0tBV3VrDKSPJNUq2LMSjJPAWmbG66GnX7EApsDUeISNxCWtCdK+1yvO1zr5IaNTU+0V5yGB4N5XllUursFJA5tJ7G1Sr0WDUy+b1bZEXJrbwBDAYKXkRnfl9eoNtnrYIPJC19tJkbIo9i4e15L+OAA5w0lhfs1XpdcfiTxXtwqBc1carO3yz7L6OrU6xtvE5S8By/zzf3aEVY91P3lwCWd6I+cO9mb7ixWTIHJOL8EJ3qHc3IzP+1dcbe5ByTnMPctGbQr6HpHCnGTBHtZ7kShJSsdl8HUX+xVeOju3rjcXMYaTCJs55YsbQo+LNhCFWH+sa/rNIDuq1W8WzNuGEjYXV3dPdp0NF4K13SVBBTnmpo89kqy6o2TX6/2Q7bah6v19jgmiSpSG5qm//b2/m1+8vp6fvpf+XXX/FDm/9mzoedjnK8/0ng8O/Rt79ND16f/knV/f/9WuzGw7flUrEm78PXg6B+eiX34C4/nZ0Hj82dUXx8WP59Dt3Y4//j4Lc69rmnr8UtTpI8fboAdTtfMP1Ns5l+yuuD9j49E/8G110PSL20xL/YA17zNPyWcf5Xhe7Hdfv0avh4avn/zXo+Cv6wI/AsYvWe/Xw/9gburj/DH1dvv/wv7BTKQSC4AAA== -->
