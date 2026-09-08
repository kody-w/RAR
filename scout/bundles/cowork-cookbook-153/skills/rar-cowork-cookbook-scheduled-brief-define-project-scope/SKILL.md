---
name: "rar-cowork-cookbook-scheduled-brief-define-project-scope"
description: "Builds a morning brief on define project scope from Dynamics 365 ERP data for legal entity USMF, returning top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email d"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_project_scope", "rar_sha256": "61a01a74a898b9440ae44d196b3fcb76510939d4fee79ae6ebf78f11efc719a5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1Hf98H2IzOZp3xRES00IBCTACGE05FmBjGKQYDc/u99kHTTdlXW66qO/tTKuHklOGfPe619Lvrtze27pGrePr8ZoVsueDfP0yRsFm4ZLFbVUDUZ+FVlHvhZ+FXZNanXd1XTvn14C8LWb9K6S6sSbOf6NA/ahbsoqqZMy3jhNWkYLapyEYRRWoaLuqkuod8tWr+qw0XUVMViPZVukfrtAqfIxUbXFoHbuYuoahZ5GLv5Iiy7tJsWR0Peflg0Ydc/JXdVvSAXaRcW7cKbFmlRu373AZhcFW6ehu3i1i66JFzQHwN3WjQVcAnscm9h48bhh4drTehXRRGWQRgsynDsFkAC8KP9sKjzfvaiBcuDRVi4ab4IgLPh6BZ1HrZvn3/+5cMbUJm/ff7tzc/dtp1j5ydh0OdhwM1Orx8Oa09/jdldICB3yxisrCcQ7hJ8rsMGOFqASyA+i9enH9swjz4s/vM/s8Ft4vanz1/Kxev15W3+p/flw7WuctsOGOi7teulOYjSp8UyH9ypfcXp4QPIVhl/eu78QxKI3t/mez8+lXyKw+7HL2/AysadY/Dl7acFyMCXt6af33+apdQ//vQpr4aw+fGnP+S0vfdIKBAGrP709fX5JRYs/GNpGi2+Gtpm9dIFop/WIRD+J//m19P0l7hXSL4+F/9Y1R8W35c8+/M3YO+zHj0g9/tiQQzAzrdPlyotf3zpaKpbWLqlH/740z8TC1LrZ3nadv+S3J+fgpPQDUC0XiH56cMjfb8soJdv32T+c7U1KJh/xxOw/F3dt0D9M9mPzP6daNAjoHPec/ldcd/bAP1t8fM/9e2/2/BhEX15W4d5Orell4efF789SuTnH4I/Lv7wy+9A9P9RjFH1jf+Q8LVwyzQK2+7r159/aB+Xf/jl5x/6GlRx6BZf+yb/nszvxfWh5y8RfK368a97gf5jmZXVUC6+9dDit6r+H83vnxYWAKTgj+vt58WfO3F+QYvZiXelzxD8qRtbYOuf4vjT2+8AfUrgTf8ELIAf//EfCzn1m6qtom4B4KbvFiDBXVqEs/FmkraL9AmITQji2qYgsK91L0yeLa6ixa//038g/kf/hfhw+45rXx9o/vUJ5V9f274+oPzXTwsTyK6aNE5LANr6UtO+lABpy27WWzdhGzYzmHpTF34ELf1xfrNIy8Wv/4r4rw9Jn+rp1wdwp0/801fCjH0t2Pxp9vKUhOXLJx/QWDiGfg+U5JUPLIpSANwzgbRVfgPYOUekzdIcIHsK0AXQ2fQkhb78PAv79ddfPbdNvpRPsMYXT55rYbDgmzmLjx+Ba1Gexkn3pQz9pFr88NvvPyz+1+K/2/UQPuvQAHG8cgIsFA1VWYAe6wEldSBdIMEAQB45+e33V4CBmBIQM8hgGs0kN28GNZqFwXu0jd3yI0ZSCy8EUQ5nXqyabqa+tPu0EKLFN3uB0vnWzBFJ1XaAoeuZCkt/AlJd4M63SJYVIGxQiG00fVj0bfjQ+qvXuA8TC9DsbvfrQl5pgJGqHPw3m/lYBDZXZQrC/60WnteBkOaHdsG9i/i0UOaqXNRu49ZJ4750RO4zL4CJ3rcD4S4g6+FLOdNvOIfq0SLP8IBFIDL+K6Uf55wvZo4HiW3fdT/WuDNvmg/+bL6U7av83SZ8DAXAlGkR92kwk8J/vUqqTao+Dx7xA5bOkl5ZCF5ZedTg+ntzzrfJYLF5zBKPAWHxpccQlFj8/zwzzRFZ8ry+4ZfmZr3YKKZ+fmZqHiPnjD4nz9nY2fpHV/4xzrxD1jtyfynzFJRdM/3Xc+Ujv681TzTsG6BcX+oP+aC4QKZmuY/an2u5aWY33S/lO0UArxYPPATxBkABGmmu33eF8913SxOABvPnP8aFRzCaYI4LqO9F3Xs5qL0oDAPP9TNgVTP37yvNoBHCuZeHJPWTv3g1ZwvUG5A/Jz0FHQlo5NM32H7efTf9LxufU9G85TEx9iArzUMAsCOcDZwzNqQdQDG3e07twM/PDyHAjaLuZt890EDA0+fFsAmvfdqCGmk/vOIa1gCsP86/n57OV8OxBiUJggU6o+5BdB+9NFdLAWYeYAMoXtBaRVqCGQAE5RWEh0C3mIEBAO9rSH1KfFx+ORQ+GnAmr/eNsyPznnkeeLaAW05/xg/ze2UC5BXziofev6+0b9pm2TOGtgAHgcb3u8/B4dOT+5/DxeJd7ud/OBb9+O+dnB5sfvxrAXxeJF1Xt59h+MnA7wT8CXQc/LS1/YOMPz5g4uMTIz6+MOLjAyP+Ivvp9ufFv2ffX0S8+uPzAv2EfELmW9Krvl4vEI7VR+78kZjvfin18A+MBeoBuHQzB+TTDDrvhPi+BLBi3ADQAoufBNnOvDoAKn8wAsjEl/LPBT83HCCcMp4LtK3+BASPyQAU/zNx34gL3Co7oDuY58k4/DQfw2bz2/Dtc9nn+Yc3gKXhv3Z+m/mpmAu7nQ9+IOhgQuvS8PHpgRNjN7/966FYfbxx80+LdQgwKW//XHwvVplZ9U898vTzwxPyP8zoDlof1CXwc1Y+95fbgoIFtTr700317MDzqDcPhw8W+PpkgX806C/s8RfCANB37cMZX0FduX0OogkuzTTyXTXfBtR/1HECM8G8N6g+z/T44YU3M0244NO38wFw7nVimzWEZQ8Owz/PZ5M52o8t8xuwB/z6tunb3x288O2X79gFhrwacNI8434FWBo2/2ifBsJYPQeCJ9+CKnKDAOxsnxTwgE4wGIXvXNa40WOW9UElgmL9bkDeu/N78QCz6Z8mo4fSD4vwU/xpMYRhNhPuawAAhnQL2i2+o+HhG8BnwHJzmP6I/x9RqB7HtdkYELXu+deF395A0brzjPAq29e8D5YDOJtBo+9g0NxAIfj8bENw7//qJPCS0SYumEKBEAp1EdSlCZdhGY8lCMQNCSJAWcrDI9+jKRJFWJwNCECbNOuGVOhFNBOhaBj5NMq6JJD3bOiv8+CRznaRLB0hLItFBIohATACI4KAoRjKJ2kMcVnPJT2Sdb0/tmZpGbycfTo3R/LboWQOysvn3948igArd0QrLJ+vFcyiHkzQnl5LkI3A+jgsS9eKUlWmC39GCnpberK2VJOcKLfIpiUkX8g7w5lS4+zI4YqQOTbdYasoEOnr7epV1+wqFqNCl54ZrpcypuOBHbGQem3cSyXELe+c+vyYenchykV9f5yO5LH2da61LKLYj+e+Q4WcsIsU3ZQwTLHwhkFAvetbw5PkFA1zV9JyK6+uhMmurpPkpZ4Y7ZszJUNqBd+S8w2vKekkOkYjiSuRr7oNtTOACprxtW1B+ubRTae2liSJC6IVil0bfSeVwdqzN16uyzGCMfVmP8kQv932uZYUfNsHe0nIKquc4qnJTh1P8PI+9aTOcs+TWav1ZW9wnEMVTrqeaoo78AOmJpC4Hs/aukXdHpdQgg3hKDWlO0F3uLdDtHEdd5uTVacXRDyRxrlx9z0ol/3lck4yqfap6hS59NXbm1ZW9TqShXkpnG/RZp3fa13LEn7LbdWVdYput1Y69/Zxi3Pn8uiknZ9znL8trY3aXSRrj9kVuRRLmU1hQ5KqVaNJzZZS8VvNelfTQVRmGA+hNV10oxHiVKwRmZFGV7xUxp6y0/o89e0qEFKlYNzD2QQKxluw0+vyGLb5fhTYPPO2eNpALbJb3kME8I9KwyV6MdpG3QjFfmWgR/3YbmwOoTdb3WovKoo3/kU9OFZZOccjXzQbmd5BXo6bVW0M6KWIo2smsTafrcf70qwRyDLJkN5HuKJTxo4qZFUhDKO9NvJ+uqC24SiGTk25ueu4gfSuxb45Evhu40Bh4medtKLMcVekfKBruLU5Ks3BxMR1ang6zKeQnUYKXoTEQTaXtdIYqNSZ6Kq9uEjMhW3f2eyxyviMZB3/UAxYAzV+cRVy6XDTlza814ZjEaWKdFPT9MbkFtIxHnO2jdRJ8+hcsuSSMYxRJUw/SU7R9nSWCxNCJJMwC1qS7+E9E9W9mDmtLTS6Sm88JY34pXw6MsW2Gor1/COclY3tCQy8qSGs3/v8dshGhjeJ/Q7aKTsSgfsIitNOq5kRKiNmLQ1Wj1pxPBgRtawPm1he5ydc54difzmEp1yFxdXW3jPSkpN5AgF4eDbJdcJzKJoepTVXhZdoa3kgqk7jIydD8ffRJdsHXshsReRyWMuqaJ0KqT5tNJ8vz/JSVtejL+ygQkjK6uotdSQVJLR3zKV5MHb3SG481efFmMjZNcZZ4frGoF1dUBV2V5h0tfb2A5dnRDzdz8JGLsd9YZC7YevYdF4ykUsKpS9FQ7pGGKs76Hke9hlMumZyhyb2NFC0G5FdzUZTY3O03CdmL+/txvGK1ZgcuVEdd5zDhxeRX4tZIsF1cbZE6JpfAi001hZZKPwpD51RXUX5sVF3F/jmo7bCdJtLb0nUekqMZiKCeyf5EhFYXgtgRVEjO4woIqt9cXvVrSbWdLu2Lyl356YtU7WWduXWl+IGG4dSc31d2mhajMEifoROSH8RxmIdJyWR3Pu+3VYNLvXH7lzhw55lLnSy2ukWGQdEQK7EHZWo8jnq+Y1n8FKLxBddD+hWXu6RqTjyOcop8tg6Bi1egrxZ0cj1MIb1TjXPNwH1qaFFM3VN9pRoZDBCqziVnKm+sm4Hdc1EJK9OxFGGhWuWVASHxbhzz1hPHgzvVIQHlmNygmMpmN77RRoQGX9c767K4I+lyZ30kSZCljLXEm5E+pnbTUszG4pddDksTwPG3Qq2O9zO8golpzC9hvCUDimXOhdjaLG2O8fN8lCMG0W5qNhuxUuYh4e3HWGfOrqkxL1RbeuTgmgXQ4ayCVcFbExPyLTBFBOhToqTC8Ox5TQ1uW9CThSaPXKgKmW3a7Rqq9U4n9LLZukJtundpb1t2DGit/FaWKr25TSwNJfQd+vUkE7rDFp8ut989Z53kL8T5bY4iYjOmjeagG7mNhj922q33OcnnxDJdc5QhnHZitB9ue65UaRgcTlNQhbtYDKLd1d8bbLVeahIdO1P0c2sGDMaBbjYjTCMligDBSWdi/ERPd40+TJZ9Ga1VPqrfR4xMpzaQ3XIXfbUF5VRrYQWkc9msSqwC2NjiiVHSx+6XCLv2h7OLbUKFOaQrCkEXYODfDg0QpmI2QlKy620qeQkmYxVudXR1DEtUC3riD+GXr3Dzyu+XlPQ+lACWqGce2/IE8oUSRwObT5oVOOTuu5eIt0a8ayfCJRGg1IYqOW6iifEcUkk61a6V531tah3CTlOI7fcnyJRLDzpAG1V72rs7TvkKKRFh2seLxzEXi/jvuUNpmW89a5X2lM3KmMyJIoKI2R/hPndds+jl7KVEl+4e8KkSdfDlZVohgt8X+ZS8Xgx0NvB8t3jhh6Mbmuw6Nmva04GQBqx9yTY86s6E/cZHwmkb1lLpChGAePN0x3TRbi5hBO3bBvNmVrleOQ4MW82IrW0CQ0B3Jlm1tH1nIHpdxjPiV7D8Xeiuo5pec7MO4Gqh1XMeculeyL2VHbLqWw6yadlcpLUZSa7S10NwCi1aXMDEguDELMg5nCn2MubyLnVOYGKK9rtNT2giJ5Ex0450Io1uXeTZq0+Cy4H+rQcYmXp3OkjWk7Ika+mrcoHALEFUrNr3hy865kyDjuWzEhZipzQltb7C12lyWHlbTKXuLDJNlOMG3dvrTS2MguVpb2lrPlVGsSp62zXlyi4UCbjbjpByDkJQaGtpI2bNSwwRL47huV9jeFnTMS44FApWmQX9uiVNTvEdYip/Fazz1UZFzYgd4G52/fbAVupFaasO7U0023t2zuIuB2mFnACpMtXgb3zNVrsw+uV5S5Sm+3ao8JfzdElqSRrU9uVz/BZ8nYSV6Yr8cg4LuZxvu6MPKb3x6UZ8cFm55G+vKIrrW73yy7ODv6Y04RetcNJOlOhgkpEs8WFm3bHU1bG96tYCHk8JTNneYnjdXg+uVdDT8ITkkhZo0brbbY5KLuaWiludMfz5BQPraXe9wNU8n2BrpFNtkxXmzI5HcpjddchR3anXaqUXnFJx0OUFjsNvt3pfYXV+0s/6Mz5UgqT3VEQjl3vcSOskgzaOEJjOkbILlVM7/LbjTUOFKXBEInokBrt8wnNRGWVBAkYOF0Cc5aiQJB7YcUWuWmrpKSaJ1I/eUyYETiuOntSOZTbLMVAuceb0bpyxSHvaz6bUEFsvFNpcU4KK0vuHp/jNj8kyNXdIwpF2Oi9D/tpfcVt5hqcpMNIOAYHH5plMphnWXOFveqZJAodiNvZCbdErFnOCvGnQXRVe0qqboKkXj4TA9p1O8HzKoVRGPsm6neXMwWhDvb3w/4oapSzSlE5EST8nAarJOwO9qpDdfuEU4MSXy2RWeKkeA2k3eZa2ttOOx336FT06GHLyJGzlcaiYKwG5P9yPkKKySV7VDvW2rKmypV7sQQBjDrC5oTqYofhMTuRg5M7+0MiFdbdcQRLXhFXe0UWh0LECKNRmiGOjlkbTzcPkcpCPO8dapCoUYIvEHXL2KkTjvRxHHb6XoPOS4URq3WwRMt7FHGJdWfOXkcu0c0uGhnMdDGqZUsL9rZIvw/SQzDC5zNV0U1pHU5avyPKoytaRxnhcNG3GXh1hJNRl8dTRZFUdDvQnVDxCdxJ8QZSJSkuLt7ByG8bxnUOLiIIWigNBxQ5O8TeS5P1JoolfDzsLmnSNFWLXmvWIU3PDo5X+GxJV0Q79dVBqPFJPvE8WdRGbF7l09Xx6Dg4JzcC1zbXdBh2S7eQlAN/KqBOtkXlvtmMd9H10CXZCRfmyBBgGu+gMcOhYLk2Is1qUUGAuGtAZxvf19ub627PJ8d1ycDibD29bm/LFTmYB6zY7kQeY2HX9rke7ohNfz7XDX7BtfDaQq5WBQjs6SRT9yeIhhOpWYWOgIDTXnrIpIlyRMpaWdfqAC11XOrOPh71Lizb/RRtUCuMlduW9313GzsuazYtxzXOucR5Vb1V6zztdFaHznh/LrEBXTM84jfj2b+eOel49E1JZeROvSWw1Qz1lEi23Ug9PCgsnIvmZGPjRGYQp5/0Hlq2+5XDXtGBL9iGDjT3Zi0TSrwzANhSWGTRIz8k9BldYbJ3IiyM1e4OJyz3y0Q6nBPdr3fOCeItIbbgPttFSBPlTrfnRyNDOS/N9ocQnAz62xpdhkVziSveQ+Bab2E6Ri7x6n6y2/5oIDlhbK1BM1dTzQuak6t4hvNwHRR3ChvIq5nvklAQuJNoOsNQasa6JYKGr4NtI2/Gnc0VtoPfUqran5DQx1f7tDjdREVPAQ9fjVOI+72p47KU5PwQYrUlBWhgo+ZoBUf2IjW42HRxcvbpQ3ezEGR3OCz1rnEjdHsae0i2IIiEapoxmMoKPbYM94oKjt/NcGsQhWPCPUt2Jzdkbhx/SzLYa+61FTKsNLY3dMJr3OnbpjH5iaEY+nKu8h7L8Ma76pA5HhH8xBaegsb+JV3t98erUbYouprIdbO+oBPNRZJ1wwbZzxzsSov+mnIolGqvqEdt4CPWr1N+gwnQ5NMrxjiu0qUSJddtGyCdO3RmJ14hOkd9mTlBWCPZU9Gx+3u4X7Nw690NO3SxEdGC7uTJFhmiuXdNEDEh+wEuV62yI+jVdnNxJozaQLsmLUgWhtk8YjZ6b5GqcWG7AE5NRjF3ekznV8diw+kktryS7DObyoKtt7oMAqKIpWlmpXJTpWXgaYSYn9pjoFwjnFsuVVmshKllRm2p6wJR3yol3okCy7A8oRyxGy3fnficdaSn3zgS20neGkBDua40x/f6ULnbu6mqcEcZBmywobLw0pH2UTWvb1FWaVklSSM8mEFghVzJmKRXElIDBXXHICCLMVMD0N3XXFUSjRQ6MGYHmhU00wpyp0ZKGozdF5VnG5Vq1VFN2lQQopfLuNuXEnHhNxuAJzZFqDw+eGmj3nuoMpxVT3tWWBvWUerFQD7pp+Dmnuwcum4P9L2+LSe9RS6Fsuta9mLBGZvHYL48wh29zYYtzdg51S1TrvdTAcumjX4ad+PgaBWJh/TWcjegiXx5YlW88uJk6i+ZCybZu7LXd2RaXpyhkSUZjDjZjR8i3vBi6WxaI71Od4NSmHQecaqzQUWoqW2q3l1GAl632gHOlsKt04U1Ox3uMO6ofCFUm+CMWwK9LbjEGeB7c70NcN1yZKQkObsiGSfiWiLtwyilDbwFLLMOaieVCuZSq6frpuAQ564GSk0NcGBm8QU5blgwIsiav51u94N9CLoymBAyxrxOYA4ObCQyw7FBtcUJgpr62GHUFd6a22FbwwCKo2IFKM/zdrAet8i2PBUX2ETXmrsd2WAdgvMaCkE3MJSfnSS52vFh3IE5Y9egMNZL2U5YVR61vjmnUNswy9V+hFeluQ8vpzYhNCkuj0vSYs2rgh4DO1Viy+uXmq/ibI0IBCTzCGj9oMVrlxn6UIUi8nJ3tuMdbhlGBV2O7FjlJJEtBqoKKnur24IjRO9ECg4wIaXj0uw8L6AQaDVqeITQtZYfbBSDUtplu4z2L5d9XRZIH2KHlLhj2GmrQMt6Y216KKkiHAaNb2xTdGd0/gG6Uta1J4caQW4Xo4+Ujsk3IelBBKQdMnosBBPdhxmg/6tFnmnM8bUhUR2bvTodtpOrGtZyOt7yd6kqNEo6JFusi8xk4nx76ZxWxY7ZuN5BDn1Y55IrmaXB0RZwqOecrX3si45eCwSVaXS0HW8440AnMMYYPBKzNxbjnNNWx3JiE2ZwcWPTpsfYfi3jB7PSMNebvN44m0cwa/Res4yo3MTO6piozf6CL/1DviNXLIFD9JZCvJMFWRZH+UqNRXWUl1BCc0eD7FB3CzEui4aS4gUq3tYTedM0o6tg8tT7t6up7CdsG4TSRclsZkvzbnc4YjZ/hultfN6t4dov8PLK2QxnhCR1YYvJUoZjDt8kM9H5tYP4tccodNcWt/aoI13fbNOIYkb9cGS6yylOwz006kezP/FjQdFbUTIh3rmttUzZkyOo/4tVuiMKJma680zNSO46GIBTrilkeDxJA8QGFEQToQraiWR06CpM12ng6g00cZOwcvv1WOFLOAwizqMSS9mUvhke/K6gjveYCEq1vie2AWiti4uomPKNo0nUNYe6UFcwspZQIay4xGbl3X2Tr8ojjMnT3ffXYra2ETLYbzDQKe7Fc8nLJGIadjca/HZk2CryzVFmzJsxcm4f+2I2ZrQN6aB5TdomEUa4QvKZFVabw2lLpptVhqmr86q+4jfcb5bLXcBfBnir3JACV2jF1PaQt+cl7EBBY6PRMkWdA1+i5EDQaW171PxKi9EjjZbJjuorenShVUtjNntrrwxdjFiDY3sWRW02kjRYjA7iocXhZlBxjbMrWxOu3nrYygpeHpsQNaD6LO763kN7oZhgqItVHBI5OaBJ5nLvar9GS0Wt7Bs3RHfYb4KxsVlzre1uW4mZ7ka709m7ro747d7H55C6tuqdDeszdJeKkwppsOGWrJippUsTNbsShFi6WiYkY4PlLLkNi270Q4GZdrC7TMSVv6X2uT3J5cZnUQHKkZ2XSDqnH3zNZOqdwR/uKhzuVcaV1r2JKpjnraTohsPHG9oqqwuEeSHjBl7J3+6qIpIHUtSxnsEbWaazq7NGeAJyEINK90V52Haqafg79gxmwR6Gxzuh7LmBWI0qDJ9P7FVcU6Ux+hvvEiEM0d8iOrZ31dkVQ8rNFEzbxdGwTZUpPrvIZrlc/u1vbx/e5mewryep/9ZXuuanNP/PHhY9n+u8f0Hj8SgxdIPPD12f/z2zfvnw1vgpMOr5YKzN+/j1COnvHot9/Feeyc8Spue3pd6fEz8fPnduPH+f+C0tg77tmulrC0a+x8O5D29e387fP2xnE33w+8/PRP/Omeethx9dNa+P0nlVWs7fwgiD1O3C18f49cjww1vweg78FafIr2FTzy6/nvUDT/FPyCf87ff/DcI3nbQdLgAA -->
