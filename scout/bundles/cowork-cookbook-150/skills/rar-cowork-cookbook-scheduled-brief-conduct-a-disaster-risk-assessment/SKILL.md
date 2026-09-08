---
name: "rar-cowork-cookbook-scheduled-brief-conduct-a-disaster-risk-assessment"
description: "Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment", "rar_sha256": "bbdc6f73921c423613d93727ecf90ec57beb1c98bd4a12270ddd6b4e2ada8038", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a disaster risk assessment Scheduled Email Brief — Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 bbdc6f73921c4236…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` first:

```bash
python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py   # or on stdin
python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a disaster risk assessment Scheduled Email Brief — Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment',
    "version": '3.0.3',
    "display_name": 'Conduct a disaster risk assessment Scheduled Email Brief',
    "description": 'Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-a-disaster-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90ddf5148fc693e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-disaster-risk-assessment'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-conduct-a-disaster-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where conduct a disaster risk assessment stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on conduct a disaster risk assessment for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct a disaster risk assessment, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s', 'example_request': 'Send me the 7am disaster risk assessment brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner needs a recurring daily or weekly disaster-risk-assessment brief from D365 F&SCM, drafted as an email and a Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConductADisasterRiskAssessment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductADisasterRiskAssessment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefConductADisasterRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOj1pblX1Hf+mC7lJnMU1a8iBYCSYDEJBASzhdpZhCjGMTg8n/vg6Sbab/nV92Oqk+tjAwNnLPnvdY+F359c7o2Luu3z2/HwCkWWyfLkjioF07hL9ZlX9YpeCtTF/xfeGXR1onbtWXdvH1484PGq5OqTcoCbGe7JPObhbPIy7pIimjh1kkQLspi4SeN07RAZp006cJpmqBp8qBoF2Fd5gtuLJw88ZoFRhILXlcXvtM6i7AEJiyyIHKyBViatOOHRZ+08aItqwWxSNogbxbuuEjyyvHaD8DcMneyJGgW92bRxsGC+ug746IugTvAFuce1E4UfHi4VQRDuwC7gN3Nh3kxMLF2whYYXyyC3EkyoOUhpOwLYPaPs7PB4ORVFjRvn3/++4c3oDZ7+/zrm5cBd+bYeXHgd1ngs7PT67LwO69dcS/HdeD36pvbQFjmFBHYVY0g9AX4XgU1cDgHP/kgZK9vPzZBFn5Y/Pu/p71TR81Pn78Ui9fry9v8T++Kh5VtOWvxF55TOW6SgVh9Wqyy3hmbRR20XV3MWWlA5oro03Pnd0kgmn+br/34VPIpCtofv7yVwARnjs+Xt58WIBNf3upu/vxpllL9+NOnrOyD+sefvstpOvcaeO0sDFj96evr+0ssWPh9aRIuvh5Vfv3SVQdeUgVA+O/8m19P01/iXiH5+lz8Y1l9WPy55NmfvwF7n7XpArl/LhbEAOx8+3Qtk+LHl466vAeFU3jBjz/9K7EgzV6aJU37/yT356fgOHB8EK1XSH768Ejf3xfLl2/fZP5rtRUomL/iCVj+ru5boP6V7Edm/0E06BnQSe+5/FNxf7Zh+bfFz//St/9qw4dF+OWNC7JkblM3Cz4vfn2UyM8/+N9//OHvvwHR/1cxx7KrvYeEr7lTJGHQtF+//vxD8/j5h7///ENXgSoOnPxrV2d/JvPP4vrQ84cIvlb9+Me9QL9ZpAXAjcW3Hlr8Wlb/q/7t0+IEAMr//nvzefH7Tpxfy8XsxLvSZwh+140NsPV3cfzp7TeARAXwpnuCGcCPf/u3xSHx6rIpw3Zx9MquXYAEt0kezMYbcdIskidA1gGIa5OAwL7WgfqfMzxbXIaLX/6390D/j94L/aHmHeO+PpD9q/dEua/O13eA/zoD/NfvAP/Lp4Uxo2idREkBgFxfqeqXAuAwwH5gRVUHTVDfAXK5Yxt8BA3+cf6wSIrFL39d2deH3E/V+MsD5JMnNuprYcbFBoj6NEfAmtH+6a83o/0QeB1QmZUesC9MAMB/AJFpyuwOcHWOVpMmWQYoDCAPoL3xIRtE9PMs7JdffnGdJv5SPIEcWzz5sIHAgm/mLD5+BI6GWRLF7Zci8OJy8cOvv/2w+M/Ff7XrIXzWoQIPX/kCFopHRV6A/utmj0EqQfIBuDzy9etvr3ADMTNrgewm4UyI82ZQv2ngv8f+uFt9RAly4QYg5sHMoWXdzjSZtJ8WQrj4Zi9QOl+a+SMum3bhB1VQ+EHhjUCqA9z5FsmibBcNKNImBETdNcFD6y9u7TxMzAEQOO0vi8NaBWxVPvi1frEX2FwWCQj/t8p4/g6E1D80C/ZdxKeFPFfsonJqp4pr56UjdJ55meeF13Yg3AEk338pZpoO5lA92ucZHrAIRMZ7pfTjnHMw2OQAK/zmXfdjjTNzqvHg1vpL0bxaw6nnVHiAKoDSqEv8mTD+41VSTVx2mf+IH7B0lvTKgv/KyqMGX+MBMPJfTkbf5okF/5hHHmPF4kuHwgi++P950prjs9pudX67MnhuwcuGfnnmbR4+Z1ee8yow82H5o0e/Dz7v4PaO8V+KLAFFWI//8Vz5yPZrzRM3uxoEWV/pD/mg1IAVs9xHJ8yVXdezq86X4p1MgGeLB3KCeAPYAG01+/CucL76bmkMsGH+/n2weFRO7c+xAdW+qDo3A5UYBoHvOl4KrKrnbn6lGbRFMHd2Hyde/Aev5jyB6gPy56QnIJwgfJ++Afzz6rvpf9j4nJ/mLY/ZsgPNXD8EADuC2cA5a3P2gXntc9YHfn5+CAFu5FU7++6Cdso/vH4M6uDWJQ2ok2eKQVyDCgD5x/n96en8azBUoINAsECfVB2I7qOz5orJwXQEbADgAio3TwowLYCgvILwEOjkM0wAGH6Ns0+Jj59fDgWPdpxp7n3j7Mi8Z54cnuXvFOPv0cT4szIB8vJ5xUPvP1baN22z7BlRG4CKQOP71eeI8ek5JTzHkMW73M//dJj68a+dtx68b/6xAD4v4ratms8Q9OTqd6r+BPAMetrafKftjw+Y+Phi0o/Ox3e0+DijxcfvaPEHTc8gfF78NWv/IOLVLZ8XyCf4Ezxf2r+q7fUCwVl/ZC8f8fnql0IPvuMvUA/gpp35IRtnGHony/clgDGjGoAXWPwkz2bm3B5AzYMtQF6+FL8v/7n9ABkV0VyuTfk7WHhMDaAVnmn8RmrgUtEC3f48h0bBp/n4NpvfBG+fiy7LPrwBVA3++hlw5rF8LvlmPkiC5gJTXpsEj28PBBna+eMfD9nK44OTfVpwAUCrrPl9Wb7YZ2bf33XP02fgqwc0fJgxH4ACqFjg86x87jynAaUMqnj2rR2r2ZnncXEeMB/M8PXJDP9sEDdzye/JYwbDWwe68cMi+BR9WpjHw+ZP5X6bav9ZqAWGhVmOX36eefPDC3rAOziJfFh8O1QAb17HvFlDUHTgBP3zfKCZw/vYMn8Ae8Dbt03f/nDhBm9//zO7Zib6Z5v0oKkAiz3m5SdZ9WCSA8ENQF080/CgNlCzT2J7dNufev7ekX/mePAcQJ6M/kroIwSPYPZBkM5k+yJ+wEvtgnLyP9EC1DxwGbDbHJPvwf7ucvk40M0GgRC1z78//PoGStKZ54JXUb5OBGA5gLGPzTzlQKCNgULw/dlw4Nr/wFnhJbGJHTCZApGu63tkSGEMing4ipEI5jMYhVKBFzJw4BGUG7iIx9CujzsIilKw7/ukiwcosJ6GMRrIezby13m4S2YrCYYKYYZBQxxBwfIgRHHfp0maBNJQ2GFch3AJxnG/b02Twn+5/nR1juu3Y8scolcEfn1zSRys3OGNsHq+1hCDuNCFcof6DJ1hesh683azzbJCc8ei8uW4q1q2d2/DJqL2F6nVBEhIPa2500J81y/WGtLiZakz6b2hbNw1U0lEEZiYXOK+is4ecUBDpRCgcGknA4HlV3oa92S9Oprpccjq6lgd42t4tFIkrevT1joFrNqdNlohxXvVHNICz1P7hmM4wUCQYFOWp4tVzWPToeym+nSdTJH0xfpS0YhGo6g3Xs1Dq94hbrPcE4PV6KN5k4wTuT5JEnqIt5dtFlK5myg3Ai3pVKSFQJSq061hRlFZD5l1GLeTKp7Eeq/jNWwh5nK/D44GVjajEe8SnULMqsXrXD+Kxg7jto1QT8aBKQ9Z1BDOZU0TmRZK/c0e94SvOaiIlbByv5Mkfi/OxJIJQ+KgqlBOeWfsXiR72uBU6XoTaqn1z6UoEvXdGU43vqm4WpE29ybYlvtCP0lVrqRF7I/FHkL5yRuE7FblqzWxWZ55BdqgmmVk03bQtsZ1jL27NKy643QrdpI5JpMvwct0M938YVftUlw/WRHE5MpQtUt5EO+OGiaTCNWTZMfmzZSaaZ8o2tjffbLwjjG6jk61dcJZm1gJ1h6xi3QbWBPPHHHFJ7Ap3VGS6vO57XmaQBv5Fbbv5FnPa2VLNH1PDbiVsMfanvijrzt1Slgsy1tdKjF74rixT1uHqc02OToXDmqlawlvW3sIikOYHbNlvVXky8SR7Hk8HU703YYMDBv45S1abta3RpCOdF2Wjlagbj9N4jETbN6gE7PmLPlAJOGKIhh+OFTtGjdYsediJAtafdmavn7ZRvde5BLd06DJBsAoxu3ZsqlgNZjr0j5eYJG59es2W7t9VqAUGI4T+Mo10oigytmu9eIUZOR2TQknvJ+WUtxVx0IJz8E539whqZZD/JxOnkTccWQptBjPDTrF03GD7liCtIKos7HzBb4PDnlb14i358VgK1dIWCXFmlbKcxdtD4pzYCFVuxwGb4rbS84emmm17PEtkbL7lbmjg/pI8+SQiTRxhcYduksnxiGpHa1NakGTYThhqNz70hZdd3g+GrdePq42bMn6TK8hSjJdy1ba22kZtUxzXAlnccluDw4FXfqJ7q88Iu5G9Yw0xb6vsEObHz2lCLwCJzg/X8IsoYpN3R+3qWwDVLxulSMKS+UuYfGNFqiodlwHidjoO0+4Sg7o9P52z3hzsLGLpex57LBUVpZw1umTvzUheXvSQoSVxqCXyiLlt9ei5Ex+mMwDdUlray2SnadRQSj7ZF/zdarmCQzJTgIzoqbfZazOhgEA6cG9kaERVpMvL5u680+X0MgV4VxdcI7SAm/fKzYp0m5tJevMYWFO53eQIfdKyWxUVVAS47rqrT52buoh2rcF7iScuj7q583UMS4n32QhuY+rtaCeNvnhRDgQrypY4OYFP1W1dSegem2CfltLG7NhA3FvbV0c5odrcSRNLnPRIiIJxxpTs08jS0tVGAs7Cdtuh+xaKtcLQ/rd7T4oDcreAVVqqHbY3XAbMpUwSqH9pTliLLLbn6/jBbInVPCyrBQsiUlFUjFZY89xoO7ZOPMizjPdPG9G23W9Q0uY9/spZSO+d6fJRfnDXlavy/Y2nSiOzYnIH+yVcaIDaqDdkTth7sHZsvkZdAKtkYI/eAgdZbCZMxXmhVcoWRNLqsAZfjV1Es85Qz9gfO7l2+h6H+2SE3rjeo4MDk33uWZVBaNRbn7hKNm8jDsk1orOuNHb9dRAG3hJb+SIR6mtXgmldRA3QsgmabEnbo67VlRU1YP7earzfjqKGSEJeTqlcVXnEyUv49SwzdwhQ/1Yca6utLWlX4WNuD7o0dSOh2xnyeWWPbIKRaHqJRgu2dj1K2Pj4dCRLLqNx2pxs1mypFYOvNxyDNruoQ11t8CMgbPXTbdP8Pt0zcwGSfPlOVsd2/A6jZBaYNRAGDlr3pL9TrnwZAE7J2djjBqOrzxej/t1WXXJ6CxDXN2WMU4yMbtBIaFUKVwSSvSMTegSgoJ4B+H4Mrwd0fbsV7uzcM3v0GY9sNquEzb3NXvmJi2xHT6otzkMe0hUaF6RHmCtMBG5KlYSaeFxmzJxLJI9KHx+7SlLTVru5AOMlHjRqwrRG4WYE9p6VUg7ofRMOiJYoSUyb+le9puRyERYuSIIf8xXNVFi5qWmt4eM4MJjKJCQsImgnhzOdY73ncPv5SWbHIfStxEXjzaYsb4IzS52BlTmjAMlBSuuvF4zmA0HM1tHdWTHCNsWJU6kQjro+wwEcjXqqqoaYb93bd3rrBtxZ3N3J8gnVoY3/IY2862x3SlDt/cpZWDh9NLt4WGpLbdJq231bjpk/dZTbjfkOrppRW2XBbTRNdq0jjvkeD9pwikT7X0rVI2172TjpAqGuG0mvDFtQvfOJiefSh4rzrJ2VCEuvZ5k+eZYQg9l090Wzoc6v60ctjMgfK3d08uNCPnezLHBTI7j1Eh+pQW7UeetZIpZ7k7mt9sB3+BNTiJldNLMdHUTD1tr2jNd6xdXzuo9dIicM2/yUdY728N5bEXSZi48kUwrP5rMAXeigmZcWOeIg+QbWuUE543FjLf8FuY5no1gILT6I1dYlBXBq5bP6umEVGOmFtwoHNobXR90Y1no2zPs3jQy0qwTldkyFxKytd/trsx9PejhxGclfuWi3NzbGGvzmt5zjJbyiCqbBD7wY7He6YXJcOszdDtUaoOsVqYM7cCYtZ628VLf7g6Na8RixcWomXO56aZ3617fRVDaTAAmTO5AwfAAuZvc5VhRk4gqJ6EWLnS24UQvWMsHZCVh9bAMC6oC03VAXvmTJLpDYJNx0t27yI8Ap+Hi5NdZ6mDRxRYERjDXmnVDNJFeHjNos5esZjPsMuGUXC+lYskyfJGLDBo2g3YyEku011VkmO5S2SaFcHCYHdayKpO100DSQYMRJKN1MeuhGICUmN+oq746ePqB1SCDHKThfJcayeUPl44rib2mTyFkEaxSAtwSz7Wza3rUb8slywhKxIrOyVRPe3L0yXWHsZeeJKt0cHsMnpg7g02Q1IslKLFCuxuqMwZ8cMVQ92ZpmaM2h+K8EwyT3KxoMF7p2G5qZOsikQAcaFyAuLw/HEYjrVjB95ppXW5bIZZX29h3zmvp7trJqTKH9sxtiVWMFdZIRnYAeH28bHy3FY8H+XZaC8IRRaeR0Iijwqw97ni9xEURaUN/4BKjSkgb2QQOcRBpr8/asqfaYXIjpD2Z5CStJtwYW4rCqQatN0uXP6nTMY26bE30IIGkfbsk7I0+ClGxOtyHQRI2hKGeVYHx0STzrnSmldP+tsQPFqey6c65OstTd5McLLyoq0NwWrIiIfZnMIbLQiBdBBmty0zhG8J1hDBZGlZcoKXdaXDWChLu7qpJ5HZaty918oYl6YbALyku0VuNAkMdWcSy4e1iRhWJw40XGl2v2OMmXeU6eunq/Z7OKThkrLM0eBtmirWs3GSKgUThFlLxcHJ70TkY6yLYHq7+sjKzyC/62GJoziA7tsSVkjJOQm6mgS9QreKCIwFKncZD19l10GdbnUmozbYgo42jQDoVwFScEL6dy5qO7y5JRcuMVIyb2IN4m8Oy7C5zHeIY3uGmFKRr6kGGNquVR+zAMR7xIq1iDnHfrVKt7S6loFk9cthS+83N4R3ABgVBO71vozkiFdZRPckDMVAeSuuxYWLGVTmtZb1H9lzone+bM7vU+pFPiGskwHVaijdAUCS2RkfNv4GzmLqloZxlyXVECycySuxKpdpofbN2txwg8EqzbTQD451fxfeW0oaMJygqVMiNpF8LscECHnOoKYoq636f1sxyW8OTsF7HSX7Pi8z3b6o3QBciY5ElXLlVxYfjKmnESMZ7KRnOpnMUQ91A7+virAfLY2Ir16tcqIV6BedtVfHTTltZJ9Rsln58GTl7RQ9YfE2rbsvDMk+thitU+zArV9Dx6vvJSj5ZkulyeSKo8GZDsuNtsugR2lIGdz5L9sW93wUcYegdkffnm70pI2lt3MwWKWXHaXp5U1BkyV9Mf+2sD6iz9sljCQ75WU5e7hsJkUX/ZtCeYqykcu3wZnENOKkFTomjJk46nuN6lEBNXkWwwhjmqRv9TmulNoW5WxXCU+uvdV/eEQqD155JuLv8QCv1Lk1rvlWgFJUuwXa/x/Mt2qPyvs1gFFsRDm6mu2ObkPv1aoS5/fnmXvehuM1xfCQSXCWdGNFMxzqP7IUsamY1Sbkgbuob7BhmGHSXEeXrNlul7sZYWSTgNTtPyCVMbc4X1FDqenUvydtwQgJds9qWRMMDnXLqaUmObbBE5OZ69dZ3jZQ4ItyscItI8ZiK3RjHodibevLk1KEPpgiilQbMulq7gPA3+/KcE6Hfn06QHfhSsw+1bdDdcUYSqLuNEBiZ7RyfzANC88AZRp66QDPzTEra6R5olsX7F7o4nM880rpEyVJSzmy7How2/Ip2L/3O2dOnZeWZqnPe94jXXkE3rVCN44yN1BDZETkZV1RHlrcso+L1vq3A+t6RIwv1Lnc53KY70mJgBRWXzFKYcK+WT0cf0grbwlg0aA9neGSMFr+o40jSVyO1kAi6H8KQ9sLmJIMTiF2Gd1RdKkpU4KceJRy6q9zsdG3KI88uq9A2Sx6nFSZw4TOy789IMGHH6/Lom9Vtd3bQ07jUoDJiABXViUrqilaIeyxoKVPEYCtFs8Jy+0Ei/J10te8JPZU3NRhWy4YiFFG7cfmZ8AfQCgfrYNnbLX+jVdQiOm7bjhnRWAx6jHRdODoqRIc15dZDzpsBgRzhpgB56aLBPnB95mjjaS0x6qCcbkf1hkbWjTwxxA0FA5Nxvo/6XiOVyvHux/ioksxy4ja05bP7qE/TFSKkHEEsSRijmqs67Qxeb3cWIifrBswKe3F9R6eNez41XX0ht05wgaX9Hkge+qnBmqCh23tzQXZsQXSnZMlkYdJ28oBr7RTpUp/qx3IUN86Vp9sQhpDgJHoSu3Lzwx7DkdjDsnXsdPWW8C33tl45XmGijXReLddWZBRTuhvSHK/RVeoFJT7QK4I/9BiWtxJ8HCsRW9a7CSOxgKGxyYNMLnYHOlI7NwvkrWcUW5Zc0YaTtYCFIZlSpYmsmj3d9dSJ3TNLMneLM1YVwgmzaa5VYCbD/J1XnTohb3eCstO96UBhp/F6lpjr7mDa1SW+ru9uSWQYmTTXBkEQ8SwaVuijPHZb7/icwhqDUg57cA6n+q6saWUjnlEoHq4NKL0pGwk7u1E7rtLyC43Ve7H0qAhzWA/HNDtMo7yRTzYSSBw4oA46xcHWeQfLd3ZlyPeVEEnsrsI6TFe4VROFkA6NitzAsWQbaYgph9tw2xB5GlbRsSenvsealWMzAT/y0UC3JIUbZ9fdYxuP8UmiLgpUAv8vFO3vl4B/GPWS2Z2LwGe5oa6x7uK6i4TTCGfTWg3cQ+3cMSbfap3KMHWBkXsp4fRuiRt+B+s4U1+Qaj9hweasBLnbV3Uv+x6Kh+spVwPNaUi97NHzWe3krUJe4g6fqp7Ykz7lEohKZDs5wG8qB4ky2wr87Xi5bvv4GFFccKWussgmp6WXy10EyRIYWOlIqC+bA1fY4v14vB7vFhjqut0IX2VzrciqvSoZPyTTWNrJO6ngjoG9NUj7hHoOmEwQYhCK3kYymGpLSDJcXzSE24qg8csmdU57+xz2cE4jkH8O+j3mHCZmpUSBr2Ab1eO1vFxruwuGC0BBdADn01GZ1hOVC7v1FYVCaA3ddb9ViI2XxZpXu1aLBeFWb7NgnbEwIlx7GMNh00UJH6XL/dRZbXa221rKEKiy7eqsHZD6trMvVDOih4mEh9GwLuTOLy+KG2G2fPMqiop9gk3re1DuwUxinDOiOwz8JTAEAnhKLo9LzDtiqriDubLepHccXrnHijimVcDTp2BjmLF0RllLdFXq1JhFrGBxNhbb1tlgRTO1DhYUoQadK3K1tQLYpemydXG+XiIorHZQ0DaoelUlV8mhs762BeeSwlGoaxQei1sWhjoIguY/WxxPXl6e+9pnCVecAoyF3V1QY9ezhvlte+dkxj4d7HBP3NplG4otSlRuqgUlm5wZYSKSY3xPXHdr2Oh1NegChXsW4rt0wnQNip0CduvuiLhhrkgV+HCx7WkDEvE09QTYFKMGDWKSm+jA2ckcEx0xpURYro8uhOju1vxxzZikCDKs3k/NylOuCiGbg+X73RkARW4W7GnSac5Xrw5VwoV69t2Y04zR9N2yi6nThgbADjBQVm/k9S7W1FDESADSdTPuYYwaGEkiwOVluA+p7XmZg9NDP+LLno28g2J0aqr1++NehDBnf1POR4q7VHnauvd9cofrkkroMXFUzodiW2b84YakNX2QUxc7Xzp/icsp3a3JsR52zKFn6vwyXfQljdyvrdAHY3bhXJIHsI8imHTPsWXitMRpkHOL6jWXj/QV5NW7zoT7jc6xJtLwSzNbGq6340bqdt5PdSVYnsLjO3PCXc1txJutSNcYDzKeTlOLgHeJjkkJTZbX0MsVOMGkDUDZydZYm0xyqNuGATlcDrDRBydlTPxa5bfTJJESqi1ZZWP5iFgmRNyxnJHBuxg5yx69V6llsOSMRB7ZcroyJIKVSY/bNryJMs+FcHBoNh16WxU4tw3QzsCnCWAftCbrpe/fT5q2Wr19eJvvvb7uoP43Hvqa79n8j906et7leX9o43FPMXD8zw9dn/87Rv79w1vtJcDE5y20Juui1+2lf7iB9vGv37Wf5Y3PZ63e7x4/b0+3TjQ/tfyWAAlNW49fmzJ7PNYBdrhdMz/Z2MwPv3rg/fc3Tv/BUfCL4z8fzwAutuXX5z3F4G1+BnF+ciPwk+9fo9ftxg9v/uupo68YSXwN6moOwuuJAOA79gn+hL399n8Alm34bYcuAAA= -->
