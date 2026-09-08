---
name: "rar-cowork-cookbook-scheduled-brief-define-project-scope"
description: "Builds a morning brief on define project scope from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email d"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_project_scope", "rar_sha256": "61a01a74a898b9440ae44d196b3fcb76510939d4fee79ae6ebf78f11efc719a5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_project_scope`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_project_scope_agent.py` and in the RCI capsule.

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

Define project scope Scheduled Email Brief — Builds a morning brief on define project scope from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email d

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-project-scope
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
    "responsible_owner": {
      "description": "Person the brief is addressed to and whose email draft is created.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 61a01a74a898b944…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_project_scope_agent.py` first:

```bash
python3 scheduled_brief_define_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_project_scope_agent.py   # or on stdin
python3 scheduled_brief_define_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project scope Scheduled Email Brief — Builds a morning brief on define project scope from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email d

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_project_scope',
    "version": '3.0.3',
    "display_name": 'Define project scope Scheduled Email Brief',
    "description": 'Builds a morning brief on define project scope from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email d',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ad0027d0a429812',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/define-project-scope'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-define-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'responsible_owner': 'Person the brief is addressed to and whose email draft is created.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define project scope stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define project scope for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define project scope, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define project scope from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email d', 'example_request': 'Give me the 7am weekday project scope brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose email draft is created.', 'name': 'responsible_owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an owner wants a recurring (daily or weekday-morning) project scope brief from D365 F&SCM, with an unsent email draft and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineProjectScope(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineProjectScope'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose email draft is created.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1Hf98H2IzOZp3xRES00IBCTACGE05FmBjGKQYDc/u99kHTTdlXW66qO/tTKuHklOGfPe619Lvrtze27pGrePr8ZoVsueDfP0yRsFm4ZLFbVUDUZ+FVlHvhZ+FXZNanXd1XTvn14C8LWb9K6S6sSbOf6NA/ahbsoqqZMy3jhNWkYLapyEYRRWoaLuqkuod8tWr+qw0XUVMViPZVukfrtAqfIxUbXFoHbuYuoahZ5GLv5Iiy7tJsWR0Peflg0Ydc/JXdVvSAXaRcW7cKbFmlRu373AZhcFW6ehu3i1i66JFzQHwN3WjQVcAnscm9h48bhh4drTehXRRGWQRgsynDsFkAC8KP9sKjzfvaiBcuDRVi4ab4IgLPh6BZ1HrZvn3/+5cMbUJm/ff7tzc/dtp1j5ydh0OdhwM1Orx8Oa09/jdldICB3yxisrCcQ7hJ8rsMGOFqASyA+i9enH9swjz4s/vM/s8Ft4vanz1/Kxev15W3+p/flw7WuctsOGOi7teulOYjSp8UyH9ypfcXp4QPIVhl/eu78QxKI3t/mez8+lXyKw+7HL2/AysadY/Dl7acFyMCXt6af33+apdQ//vQpr4aw+fGnP+S0vfdIKBAGrP709fX5JRYs/GNpGi2+Gtpm9dIFop/WIRD+J//m19P0l7hXSL4+F/9Y1R8W35c8+/M3YO+zHj0g9/tiQQzAzrdPlyotf3zpaKpbWLqlH/740z8TC1LrZ3nadv+S3J+fgpPQDUC0XiH56cMjfb8soJdv32T+c7U1KJh/xxOw/F3dt0D9M9mPzP6daNAjoHPec/ldcd/bAP1t8fM/9e2/2/BhEX15W4d5Orell4efF789SuTnH4I/Lv7wy+9A9P9RjFH1jf+Q8LVwyzQK2+7r159/aB+Xf/jl5x/6GlRx6BZf+yb/nszvxfWh5y8RfK368a97gf5jmZXVUC6+9dDit6r+H83vnxYWAKTgj+vt58WfO3F+QYvZiXelzxD8qRtbYOuf4vjT2+8AfUrgTf8ELIAf//EfCzn1m6qtom4B4KbvFiDBXVqEs/FmkraL9AmITQji2qYgsK91L0yeLa6ixa//038g/kf/hfhw+45rXx9o/vUJ5V9f274+oPzXTwsTyK6aNE5LANr6UtO+lABpy27WWzdhGzYzmHpTF34ELf1xfrNIy8Wv/4r4rw9Jn+rp1wdwp0/801fCjH0t2Pxp9vKUhOXLJx/QWDiGfg+U5JUPLIpSANwzgbRVfgPYOUekzdIcIHsK0AXQ2fQkhb78PAv79ddfPbdNvpRPsMYXT55rYbDgmzmLjx+Ba1Gexkn3pQz9pFr88NvvPyz+1+K/2/UQPuvQAHG8cgIsFA1VWYAe6wEldSBdIMEAQB45+e33V4CBmBIQM8hgGs0kN28GNZqFwXu0jd3yI0ZSCy8EUQ5nXqyabqa+tPu0EKLFN3uB0vnWzBFJ1XaAoeuZCkt/AlJd4M63SJYVIGxQiG00fVj0bfjQ+qvXuA8TC9DsbvfrQl5pgJGqHPw3m/lYBDZXZQrC/60WnteBkOaHdsG9i/i0UOaqXNRu49ZJ4750RO4zL4CJ3rcD4S4g6+FLOdNvOIfq0SLP8IBFIDL+K6Uf55wvZo4HiW3fdT/WuDNvmg/+bL6U7av83SZ8DAXAlGkR92kwk8J/vUqqTao+Dx7xA5bOkl5ZCF5ZedTg+ntzzrfJYLF5zBKPAWHxpccQlFj8/zwzzRFZ8ry+4ZfmZr3YKKZ+fmZqHiPnjD4nz9nY2fpHV/4xzrxD1jtyfynzFJRdM/3Xc+Ujv681TzTsG6BcX+oP+aC4QKZmuY/an2u5aWY33S/lO0UArxYPPATxBkABGmmu33eF8913SxOABvPnP8aFRzCaYI4LqO9F3Xs5qL0oDAPP9TNgVTP37yvNoBHCuZeHJPWTv3g1ZwvUG5A/Jz0FHQlo5NM32H7efTf9LxufU9G85TEx9iArzUMAsCOcDZwzNqQdQDG3e07twM/PDyHAjaLuZt890EDA0+fFsAmvfdqCGmk/vOIa1gCsP86/n57OV8OxBiUJggU6o+5BdB+9NFdLAWYeYAMoXtBaRVqCGQAE5RWEh0C3mIEBAO9rSH1KfFx+ORQ+GnAmr/eNsyPznnkeeLaAW05/xg/ze2UC5BXziofev6+0b9pm2TOGtgAHgcb3u8/B4dOT+5/DxeJd7ud/OBb9+O+dnB5sfvxrAXxeJF1Xt59h+MnA7wT8CXQc/LS1/YOMPz5g4uMTIz6+MOLjAyP+Ivvp9ufFv2ffX0S8+uPzAv2EfELmW9Krvl4vEI7VR+78kZjvfin18A+MBeoBuHQzB+TTDDrvhPi+BLBi3ADQAoufBNnOvDoAKn8wAsjEl/LPBT83HCCcMp4LtK3+BASPyQAU/zNx34gL3Co7oDuY58k4/DQfw2bz2/Dtc9nn+Yc3gKXhv3Z+m/mpmAu7nQ9+IOhgQuvS8PHpgRNjN7/966FYfbxx80+LdQgwKW//XHwvVplZ9U898vTzwxPyP8zoDlof1CXwc1Y+95fbgoIFtTr700317MDzqDcPhw8W+PpkgX806C/s8RfCANB37cMZX0FduX0OogkuzTTyXTXfBtR/1HECM8G8N6g+z/T44YU3M0244NO38wFw7nVimzWEZQ8Owz/PZ5M52o8t8xuwB/z6tunb3x288O2X79gFhrwacNI8434FWBo2/2ifBsJYPQeCJ9+CKnKDAOxsnxTwgE4wGIXvXNa40WOW9UElgmL9bkDeu/N78QCz6Z8mo4fSD4vwU/xpMYRhNhPuawAAhnQL2i2+o+HhG8BnwHJzmP6I/x9RqB7HtdkYELXu+deF395A0brzjPAq29e8D5YDOJtBo+9g0NxAIfj8bENw7//qJPCS0SYumEKBEAp1EdSlCZdhGY8lCMQNCSJAWcrDI9+jKRJFWJwNCECbNOuGVOhFNBOhaBj5NMq6JJD3bOiv8+CRznbNRoFwfASYEP5xG1wKXg49HZij9e3gMTv+8uu3N48iwMod0QrL52sFs6gHE7Sn1xJkI7A+DsvStaJUlenCn9GA3paerC3VJCfKLbJpCckX8s5wptQ4O3K4ImSOTXfYKgpE+nq7etU1u4rFqNClZ4brpYzpeGBHLKReG/dSCXHLO6c+P6beXYhyUd8fpyN5rH2day2LKPbjue9QISfsIkU3JQxTLLxhEFDT+tbwJDlFw9yVtNzKqythsqvrJHmpJ0b75kzJkFrBt+R8w2tKOomO0UjiSuSrbkPtDKCCZnxtW5C+eXTTqa0lSeKCaIVi10bfSWWw9uyNl+tyjGBMvdlPMsRvt32uJQXf9sFeErLKKqd4arJTxxO8vE89qbPc82TWan3ZGxznUIWTrqea4g78gKkJJK7Hs7ZuUbfHJZRgQzhKTelO0B3u7RBtXMfd5mTV6QURT6Rxbtx9D0pif7mck0yqfao6RS599famlVW9jmRhXgrnW7RZ5/da17KE33JbdWWdotutlc69fdzi3Lk8Omnn5xznb0tro3YXydpjdkUuxVJmU9iQpGrVaFKzpVT8VrPe1XQQlRnGQ2hNF91ohDgVa0RmpNEVL5Wxp+y0Pk99uwqEVCkY93A2gYLxFuz0ujyGbb4fBTbPvC2eNlCL7Jb3EAEco9JwiV6MtlE3QrFfGehRP7Ybm0PozVa32ouK4o1/UQ+OVVbO8cgXzUamd5CX42ZVGwN6KeLomkmszWfr8b40awSyTDKk9xGu6JSxowpZVQjDaK+NvJ8uqG04iqFTU27uOm4gvWuxb44Evts4UJj4WSetKHPcFSkf6BpubY5KczAxcZ0ang7zKWSnkYIXIXGQzWWtNAYqdSa6ai8uEnNh23c2e6wyPiNZxz8UA9ZAjV9chVw63PSlDe+14VhEqSLd1DS9MbmFdIzHnG0jddI8OpcsuWQMY1QJ00+SU7Q9neXChBDJJMyCluR7eM9EdS9mTmsLja7SG09JI34pn45Msa2GYj3/CGdlY3sCA29qCOv3Pr8dspHhTWK/g3bKjkTgPoLitNNqZoTKiFlLg9WjVhwPRkQt68Mmltf5Cdf5odhfDuEpV2FxtbX3jLTkZJ5AAOadTXKd8ByKpkdpzVXhJdpaHoiq0/jIyVD8fXTJ9oEXMlsRuRzWsipap0KqTxvN58uzvJTV9egLO6gQkrK6eksdSQUJ7R1zaR6M3T2SG0/1eTEmcnaNcVa4vjFoVxdUhd0VJl2tvf3A5RkRT/ezsJHLcV8Y5G7YOjadl0zkkkLpS9GQrhHG6g56nod9BpOumdyhiT0NFO1GZFez0dTYHC33idnLe7txvGI1JkduVMcd5/DhReTXYpZIcF2cLRG65pdAC421RRYKf8pDZ1RXUX5s1N0FvvmorTDd5tJbErWeEqOZiODeSb5EBJbXAlhR1MgOI4rIal/cXnWriTXdru1Lyt25actUraVdufWluMHGodRcX5c2mhZjsIgfoRPSX4SxWMdJSST3vm+3VYNL/bE7V/iwZ5kLnax2ukXGARGQK3FHJap8jnp+4xm81CLxRdcDupWXe2QqjnyOcoo8to5Bi5cgb1Y0cj2MYb1TzfNNQH1qaNFMXZM9JRoZjNAqTiVnqq+s20FdMxHJqxNxlGHhmiUVwWEx7twz1pMHwzsV4YHlmJzgWAqm936RBkTGH9e7qzL4Y2lyJ32kiZClzLWEG5F+5nbT0syGYhddDsvTgHG3gu0Ot7O8QskpTK8hPKVDyqXOxRharO3OcbM8FONGUS4qtlvxEubh4W1H2KeOLilxb1Tb+qQg2sWQoWzCVQEb0xMybTDFRKiT4uTCcGw5TU3um5AThWaPHKhK2e0ardpqNc6n9LJZeoJtendpbxt2jOhtvBaWqn05DSzNJfTdOjWk0zqDFp/uN1+95x3k70S5LU4iorPmjSagm7kNRv+22i33+cknRHKdM5RhXLYidF+ue24UKVhcTpOQRTuYzOLdFV+bbHUeKhJd+1N0MyvGjEYBLnYjDKMlykBBSedifESPN02+TBa9WS2V/mqfR4wMp/ZQHXKXPfVFZVQroUXks1msCuzC2JhiydHShy6XyLu2h3NLrQKFOSRrCkHX4LAeDo1QJmJ2gtJyK20qOUkmY1VudTR1TAtUyzrij6FX7/Dziq/XFLQ+lIBWKOfeG/KEMkUSh0ObDxrV+KSuu5dIt0Y86ycCpdGgFAZqua7iCXFcEsm6le5VZ30t6l1CjtPILfenSBQLTzpAW9W7Gnv7DjkKadHhmscLB7HXy7hveYNpGW+965X21I3KmAyJosII2R9hfrfd8+ilbKXEF+6eMGnS9XBlJZrhAt+XuVQ8Xgz0drB897ihB6PbGix69uuakwGQRuw9Cfb8qs7EfcZHAulb1hIpilHAePN0x3QRbi7hxC3bRnOmVjkeOU7Mm41ILW1CQwB3ppl1dD1nYPodxnOi13D8naiuY1qeM/NOoOphFXPecumeiD2V3XIqm07yaZmcJHWZye5SVwMwSm3a3IDEwiDELIg53Cn28iZybnVOoOKKdntNDyiiJ9GxUw60Yk3u3aRZq8+Cy4E+LYdYWTp3+oiWE3Lkq2mr8gFAbIHU7Jo3B+96pozDjiUzUpYiJ7Sl9f5CV2lyWHmbzCUubLLNFOPG3Vsrja3MQmVpbylrfpUGceo62/UlCi6UybibThByTkJQaCtp42YNCwyR745heV9j+BkTMS44VIoW2YU9emXNDnEdYiq/1exzVcaFDchdYO72/XbAVmqFKetOLc10W/v2DiJuh6kFnADp8lVg73yNFvvwemW5i9Rmu/ao8FdzdEkqydrUduUzfJa8ncSV6Uo8Mo6LeZyvOyOP6f1xaUZ8sNl5pC+v6Eqr2/2yi7ODP+Y0oVftcJLOVKigEtFsceGm3fGUlfH9KhZCHk/JzFle4ngdnk/u1dCT8IQkUtao0XqbbQ7KrqZWihvd8Tw5xUNrqff9AJV8X6BrZJMt09WmTE6H8ljddciR3WmXKqVXXNLxEKXFToNvd3pfYfX+0g86c76UwmR3FIRj13vcCKskgzaO0JiOEbJLFdO7/HZjjQNFaTBEIjqkRvt8QjNRWSVBAgZOl8CcpSgQ5F5YsUVu2iopqeaJ1E8eE2YEjqvOnlQO5TZLMVDu8Wa0rlxxyPuazyZUEBvvVFqck8LKkrvH57jNDwlydfeIQhE2eu/DflpfcZu5BifpMBKOwcGHZpkM5lnWXGGveiaJQgfidnbCLRFrlrNC/GkQXdWekqqbIKmXz8SAdt1O8LxKYRTGvon63eVMQaiD/f2wP4oa5axSVE4ECT+nwSoJu4O96lDdPuHUoMRXS2SWOCleA2m3uZb2ttNOxz06FT162DJy5GylsSgYqwH5v5yPkGJyyR7VjrW2rKly5V4sQQCjjrA5obrYYXjMTuTg5M7+kEiFdXccwZJXxNVekcWhEDHCaJRmiKNj1sbTzUOkshDPe4caJGqU4AtE3TJ26oQjfRyHnb7XoPNSYcRqHSzR8h5FXGLdmbPXkUt0s4tGBjNdjGrZ0oK9LdLvg/QQjPD5TFV0U1qHk9bviPLoitZRRjhc9G0GXh3hZNTl8VRRJBXdDnQnVHwCd1K8gVRJiouLdzDy24ZxnYOLCIIWSsMBRc4OsffSZL2JYgkfD7tLmjRN1aLXmnVI07OD4xU+W9IV0U59dRBqfJJPPE8WtRGbV/l0dTw6Ds7JjcC1zTUdht3SLSTlwJ8KqJNtUblvNuNddD10SXbChTkyBJjGO2jMcChYro1Is1pUECDuGtDZxvf19ua62/PJcV0ysDhbT6/b23JFDuYBK7Y7kcdY2LV9roc7YtOfz3WDX3AtvLaQq1UBAns6ydT9CaLhRGpWoSMg4LSXHjJpohyRslbWtTpASx2XurOPR70Ly3Y/RRvUCmPltuV9393GjsuaTctxjXMucV5Vb9U6Tzud1aEz3p9LbEDXDI/4zXj2r2dOOh59U1IZuVNvCWw1Qz0lkm03Ug8PCgvnojnZ2DiRGcTpJ72Hlu1+5bBXdOALtqEDzb1Zy4QS7wwAthQWWfTIDwl9RleY7J0IC2O1u8MJy/0ykQ7nRPfrnXOCeEuILbjPdhHSRLnT7fnRyFDOS7P9IQQng/62Rpdh0VziivcQuNZbmI6RS7y6n+y2PxpIThhba9DM1VTzgubkKp7hPFwHxZ3CBvJq5rskFATuJJrOMJSasW6JoOHrYNvIm3Fnc4Xt4LeUqvYnJPTx1T4tTjdR0VPAw1fjFOJ+b+q4LCU5P4RYbUkBGtioOVrBkb1IDS42XZycffrQ3SwE2R0OS71r3AjdnsYeki0IIqGaZgymskKPLcO9ooLjdzPcGkThmHDPkt3JDZkbx9+SDPaae22FDCuN7Q2d8Bp3+rZpTH5iKIa+nKu8xzK88a46ZI5HBD+xhaegsX9JV/v98WqULYquJnLdrC/oRHORZN2wQfYzB7vSor+mHAql2ivqURv4iPXrlN9gAjT59Ioxjqt0qUTJddsGSOcOndmJV4jOUV9mThDWSPZUdOz+Hu7XLNx6d8MOXWxEtKA7ebJFhmjuXRNETMh+gMtVq+wIerXdXJwJozbQrkkLkoVhNo+Yjd5bpGpc2C6AU5NRzJ0e0/nVsdhwOoktryT7zKayYOutLoOAKGJpmlmp3FRpGXgaIean9hgo1wjnlktVFithaplRW+q6QNS3Sol3osAyLE8oR+xGy3cnPmcd6ek3jsR2krcG0FCuK83xvT5U7vZuqircUYYBG2yoLLx0pH1UzetblFVaVknSCA9mEFghVzIm6ZWE1EBB3TEIyGLM1AB09zVXlUQjhQ6M2YFmBc20gtypkZIGY/dF5dlGpVp1VJM2FYTo5TLu9qVEXPjNBuCJTREqjw9e2qj3HqoMZ9XTnhXWhnWUejGQT/opuLknO4eu2wN9r2/LSW+RS6Hsupa9WHDG5jGYL49wR2+zYUszdk51y5Tr/VTAsmmjn8bdODhaReIhvbXcDWgiX55YFa+8OJn6S+aCSfau7PUdmZYXZ2hkSQYjTnbjh4g3vFg6m9ZIr9PdoBQmnUec6mxQEWpqm6p3l5GA1612gLOlcOt0Yc1OhzuMOypfCNUmOOOWQG8LLnEG+N5cbwNctxwZKUnOrkjGibiWSPswSmkDbwHLrIPaSaWCudTq6bopOMS5q4FSUwMcmFl8QY4bFowIsuZvp9v9YB+CrgwmhIwxrxOYgwMbicxwbFBtcYKgpj52GHWFt+Z22NYwgOKoWAHK87wdrMctsi1PxQU20bXmbkc2WIfgvIZC0A0M5WcnSa52fBh3YM7YNSiM9VK2E1aVR61vzinUNsxytR/hVWnuw8upTQhNisvjkrRY86qgx8BOldjy+qXmqzhbIwIByTwCWj9o8dplhj5UoYi83J3teIdbhlFBlyM7VjlJZIuBqoLK3uq24AjRO5GCA0xI6bg0O88LKARajRoeIXSt5QcbxaCUdtkuo/3LZV+XBdKH2CEl7hh22irQst5Ymx5KqgiHQeMb2xTdGZ1/gK6Ude3JoUaQ28XoI6Vj8k1IehABaYeMHgvBRPdhBuj/apFnGnN8bUhUx2avToft5KqGtZyOt/xdqgqNkg7JFusiM5k43146p1WxYzaud5BDH9a55EpmaXC0BRzqOWdrH/uio9cCQWUaHW3HG8440AmMMQaPxOyNxTjntNWxnNiEGVzc2LTpMbZfy/jBrDTM9SavN87mEcwavdcsIyo3sbM6Jmqzv+BL/5DvyBVL4BC9pRDvZEGWxVG+UmNRHeUllNDc0SA71N1CjMuioaR4gYq39UTeNM3oKpg89f7tair7CdsGoXRRMpvZ0rzbHY6YzZ9hehufd2u49gu8vHI2wxkhSV3YYrKU4ZjDN8lMdH7tIH7tMQrdtcWtPepI1zfbNKKYUT8cme5yitNwD4360exP/FhQ9FaUTIh3bmstU/bkCOr/YpXuiIKJme48UzOSuw4G4JRrChkeT9IAsQEF0USognYiGR26CtN1Grh6A03cJKzcfj1W+BIOg4jzqMRSNqVvhge/K6jjPSaCUq3viW0AWuviIiqmfONoEnXNoS7UFYysJVQIKy6xWXl33+Sr8ghj8nT3/bWYrW2EDPYbDHSKe/Fc8jKJmIbdjQa/HRm2inxzlBnzZoyc28e+mI0ZbUM6aF6TtkmEEa6QfGaF1eZw2pLpZpVh6uq8qq/4Dfeb5XIX8JcB3io3pMAVWjG1PeTteQk7UNDYaLRMUefAlyg5EHRa2x41v9Ji9EijZbKj+ooeXWjV0pjN3torQxcj1uDYnkVRm40kDRajg3hocbgZVFzj7MrWhKu3HraygpfHJkQNqD6Lu7730F4oJhjqYhWHRE4OaJK53Lvar9FSUSv7xg3RHfabYGxs1lxru9tWYqa70e509q6rI3679/E5pK6temfD+gzdpeKkQhpsuCUrZmrp0kTNrgQhlq6WCcnYYDlLbsOiG/1QYKYd7C4TceVvqX1uT3K58VlUgHJk5yWSzukHXzOZemfwh7sKh3uVcaV1b6IK5nkrKbrh8PGGtsrqAmFeyLiBV/K3u6qI5IEUdaxn8EaW6ezqrBGegBzEoNJ9UR62nWoa/o49g1mwh+HxTih7biBWowrD5xN7FddUaYz+xrtECEP0t4iO7V11dsWQcjMF03ZxNGxTZYrPLrJZLpd/+9vbh7f5Oevraem/9bWt+SnN/7MHQs/nOu9fwng8Lgzd4PND1+d/z6xfPrw1fgqMej78avM+fj1C+rtHXx//lefus4Tp+Y2o92fBzwfMnRvP3xl+S8ugb7tm+tqCke/xAO7Dm9e383cM29lEH/z+83PPv3PmeevhR1fN66N0XpWW8zctwiB1u/D1MX49FvzwFrye9X7FKfJr2NSzy6/n+cBT/BPyCX/7/X8DdWwKWAEuAAA= -->
