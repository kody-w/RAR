---
name: "rar-cowork-cookbook-ppt-exec-define-case-types-and-policies"
description: "Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_case_types_and_policies", "rar_sha256": "5619336784d46c6600dccf70da7d39d4921b916dd8f0693577dfa325418fbe88", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_case_types_and_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_case_types_and_policies_agent.py` and in the RCI capsule.

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

Define case types and policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
    "output_filename": {
      "description": "Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Intended briefing length, e.g. 15-minute monthly review, to size the deck.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare against for the trend chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 5619336784d46c66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_case_types_and_policies_agent.py` first:

```bash
python3 ppt_exec_define_case_types_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_case_types_and_policies_agent.py   # or on stdin
python3 ppt_exec_define_case_types_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define case types and policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_case_types_and_policies',
    "version": '3.0.3',
    "display_name": 'Define case types and policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-case-types-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10f5e2afec633f1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-case-types-and-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-define-case-types-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.', 'review_length': 'Intended briefing length, e.g. 15-minute monthly review, to size the deck.', 'review_period': 'Reporting period and prior period to compare against for the trend chart.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define case types and policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define case types and policies for a 15-minute monthly review. Produce 'ppt-exec-define-case-types-and-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define case types and policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on case types and policies from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period to compare against for the trend chart.', 'name': 'review_period'}, {'description': 'Intended briefing length, e.g. 15-minute monthly review, to size the deck.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing define-case-types-and-policies status from D365 ERP for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineCaseTypesAndPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineCaseTypesAndPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Intended briefing length, e.g. 15-minute monthly review, to size the deck.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare against for the trend chart.', 'type': 'string'}},
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
    print(PptExecDefineCaseTypesAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H3UvO0j1oiMGCQkEYhESCHB1lNlB7JsA+fm7z0G6t8rudvd0T8xfoypbAs7JPX+ZWYdfX5y+i8vm5fPLKXCKBedkWRIHzcIp/MWmHMomBV9l6oL/Fl5ZdE3i9l3ZtC+fXvyg9Zqk6pKyANvXfZL57cJZNIHjv5ZFNi2CMfD6LrkFC7UcgkYtk6Jb+IGXLspi4TltsOimKmgfvKoyS7wEXIRNmS/YqXDyxGsXOEUudv/ztJEWvtM5i7AEki0iQLJYZEHkZIug6JJu+rQYki5eiOr+06JrgsL/BMTwX8PMiT4tHG8W8cHFqSrwMBkXbZYA8RdV1reLtgqcFKhclF3QvgHFgtHJqyxoXz7//NdPLwn4/fL51xcvc1pw60Wtui1QjA3CpAg2QIvzrART+Oq7CoBC5hQRWFpNwLYFuK6CBoieg1t+EC7er35sgyz8tPjP/0wHp4nanz5/KRbvny8v8x+tLxZdDKxUOm0X+MBkleMmGdD3bcFkgzO1QMuub4rZ7C1wTRG9PXd+p1RWi7/Mz358MnmLgu7HLy8lEMGZrfLl5acFsOmXl6aff7/NVKoff3rLZof9+NN3Om3vXgOvm4kBqd++vl+/kwULvy9NwsXXk7rdvPNqAi+pAkD8d/rNn6fo7+TeTfL1ufjHsvq0+HPKsz5/AfI+g88FdP+cLLAB2PnydgVB9+M7j6YEceMUXvDjT/+IrBeD8MyStvuX6P78JByDiAfWejfJT58e7vvrAnrX7RvNf8y2AgHz72gCln+w+2aof0T74dm/IZ2B0G2/+fJPyf3ZBugvi5//oW7/bMOnRfjlhQ0ykLiN42bB58WvjxD5+Qf/+80f/vobIP1/JHMq+8Z7UPiaO0USBm339evPP7SP2z/89ecf+gpEceDkX/sm+zOaf2bXB58/WPB91Y9/3Av460ValEOx+JZDi1/L6n80v70tDAegyvf77efF7zNx/kCLWYkPpk8T/C4bWyDr7+z408tvAH4KoE3/gLAZff7jPxZS4jVlW4bd4uSVfbcADu6SPJiFP8dJuwB/Z9RoAmDXNgGGfV8H4n/28CxxGS5++V/eA95fvXd4h6uq+zpD9lf/AW1fZ4T++kDorwA7v34g9C9vizMgXzZJlBQAgTVGVb8UTgSQeGZdNUEbNDcAV+7UBa8gq1/nH4ukWPzyL3L4+iD2Vk2/PEA7eaKgttnPCNj2WfA263qJQRF4auaByvUsNsEiKz0gVJgA/J6LQFtmoP50s13aNMmyhZ8AjAEVbHrQBrb7PBP75ZdfXKeNvxRPyMYXz9LWwmDBN3EWr69AuzBLorj7UgReXC5++PW3Hxb/vfhnux7EZx4qqB/vngESCidFXoBM63OwDDgNuBnAyMMzv/72bmNApgCFCfgxCefaOG8GkZoG/ofBTzzzipHUwg2AoYGR86psOlAHFkn3ttiHi2/yAqbzo7lSxGU7l+G5EgaFNwGqDlDnmyVBGVy0IBzbEJTVfi7SgOsvbuM8RMxByjvdLwtpo4K6VGbgf7OYj0Vgc1kkwPzfwuF5HxBpfmgX6w8Sbwt5js1F5TROFTfOO4/QefplrvHv2wFxZ1EEw5dirsLBbKpHojzNAxYBy3jvLn2dfQ56lByggt9+8H6scebqeX5U0eZL0b4ngdPMrvBAUQBMoz7x59LwX+8h1cZln/kP+wFJZ0rvXvDfvfKIwWcT8A97me2fNUDs3AB96TEEJRb/vzRNsy0YjtO2HHPesoutfNasp4/mnnH25bPNBFwf4jzy8Xs78wFZH8j9pcgSEHDN9F/PlQ/Pvq95omEPJAXIoz3og7ACksx0H1E/R3HTzGZxvhQfJQJotHjgIVAKQARIoTlyPxjOTz8kjQEOzNff24VHlDT+bAwQ2Yuqd4HZF2EQ+K4D/NLFs/c+XApSIJizeIgTL/6DVrPZQaQB+rMrE5CLoIy8fYPt59MP0f+w8dkVzVseHWMPErd5EAByBLOAs5tmZwLxumeLDvT8/CAC1MirbtbdBakDNH3eDJqg7pM26WaYfNo1qABSv87fT03nu8FYgWwBxgI5UfXAuo8smgEmBz0PkAGEJkiqPClADwCM8m6EB0EnnzMDQO57k/qk+Lj9rlDwSL25eH1snBWZ98z9wDOqnWL6PXKc/yxMAL18XvHg+7eR9o3bTHtGzxYgIOD48fTZOLw9a/+zuVh80P38dzPQj//emPSo5vofA+DzIu66qv0Mw88K/FGA3wB2wU9Z27kYv85Q8Posla9z5r8+Mv8V8Hz9yPw/kH9q/nnx74n4BxLvKfJ5gb4hb8j86PAeYu8fYJHN69p6JeanXwot+A6wgH2Zgxib/TeB6v+tGn4sASUxagAAgcXP6tjORXUAdfxRDoAzvhS/j/k550C1KaI5Rtvyd1jwaAtA/D99961qgUdFB3j7c0sZBfMs98iQNnj5XPRZ9ukFIGTwL85wc3XK5+Bu5+kPpBHo0rr50TwLzlgxdvPPP07ByuOHk70BmAe4lLW/D8D3mjLX1N/lyVNRoKAHOHyaIRukP4hNoOjMfM4xpwVBC+J1VmiOAcDoOe7NDeID0r8+If3vBWLnYvB71J9hrwK2eGTXp0XwFr0t9JO0+1Pa3zrTvyd8AW3ATMsvP88V8dM70IBvME18WnwbDIBG76PaY7QuejAF/zwPJbOJH1vmH2AP+Pq26du/LrjBy1//TK4HGn2dY+Hp0b+V7gw6q6BbvIE0Ghcfy961/RdT6xVDMOoVIV8x4kHmTw0EmuwkGL4C+lEX/70Y+7mk+HMvDEA9nGHzufJdEpR8Bcg5d605CKg4m4FspvdpNmyb3J990Vz8/xlz4KOk9P+euRZ8NIPPFc+WAfxqPm4ALgBzqrkRcqIHxH5DxUdDMGdf0/0J7wdzUD9AFZ69+T1MvjurfIyTs5jAud3zXz9+fQEJ5cxNyXtKvc8jYDmA29d27rxggDyAIbh+YgR49n87qbyTaWMHtMiADkmhKxyn6CXhE5RHUQjie15II75D+/jKJ1YY6q5QyveXIUKtcJKm/dDBMZJAl6EbLJeA3hNwvs5dZjKLRq7oEFmtsJBAMcQH4mAE2E4tKY+kMcRZuQ7pkivH/b41TQr/Xd+nfrMxvw1Ns13e1f71xaUIsJIn2j3z/GzgFerCF9qdDiZsIssxG/S6ti9lyE2bY5OTmKRhu9RxTU/FuiKMN9G4uyanXrQPh32AlXG5hTQBGs6rQ6iclTSOtUzx85ynb/uhEXKynewlnNL20lEI+KSQJ0GsmHgp6Jdxco6nMBbFwx677qX9TRhXmb52taumFZSDS/fVvhS908iK9A6HYUqGOeyq7I8icuxhc+MJtx03icRuf0L3KY3RB1VADhaBJy6kMMkluOFDjN9wiuiT1UbFNzuiRcaBPKTbcXsQfOjAaSdNMnKBo65WYkAhblHbVO9TnNnK7WHc3xxzD215zTrKjubB052xQu1YX1OhzdpLtk3qM9yYkmbvL3qTr/Cqu92uKQwFrkx6+aioBba8DbyBTv1e0BHR3dhLqQPY4VopmVZGxW/0swDzrYnwJtFIh0LaydcBpREi733oVuSZMFHJZWefJXErJbHQJjcJJ5F7EMPaXYhbo7lG3ZG9qqeTDbkQUiC6WDO1p8l3wfRFhmAdauzTa0NfEoQo1KwezVXR61Wl6EVkafvoelRPGrMKd7CyN7kxZUUPQtdCezrs2lN93u2c46E9d2JUXa6hcuxVSUZOlqFFBoRvrCN2uvjncmWobHCxQN1JaY0Zy14TBflINoN32MbJ1dZYsb+Tmr3jl+QekXPdIXjI35nnsjdWW0U8QHrvTtVdOG2NIybdRB0zE4jzZVVNhJV4XuVSEkXV4di2sbC56ePKAIbT6/sqVZO1olmTifhCLC5Z9Yqcl6swXeNb6V5zV001a3eJasL66mxYJg00fjzD6ko5nyWhHwoO3mIx0qyRXe3qclsfuU7e4tdDl+GGMvKVsq37zEgyTEQc45Lb61GcdpC4UYlapLKjV7l+FZZISIW6BxO3dRwez8sjTiSodVR3u/Y8cXfL44peqzfkzZevOryrk2iSbVRiMsLKeaNPRQJ4eotOrpCcWQJmr/nxKhW7EbonFjaQTXb3qppUVe0SjvVaHswra7AjWtCxKql73kIPuYpcr456x2J4Z3LK5E/UZXuFs3TbRZTpKemJQ1zJX+53gaYZdSzInnnPlq13PDrnpbabdI7CIkOOOKE/bYsai2y5WZ9a+GILu7o7TwFbKpzbXbhgSI9OpG1SWYgclI0P8nJj6FQibVd3qlviobp1cN4sEYkQs+vaqKbK4w/bluXu0pITCnsbaHSicwoKN75+b24aq9x2e4EEEap71NKICr67TmKFI6yGXM+nA8qrwtIskFBL6gNsoSYdKmTtiLlAX5C7QcGZomm8DrmyjbfIMNGXDCZOhGkYMFJu9N7CJPvseOO6PS9PsJlXe37KVOnMMSxcKSOSQ7aqKTx+wVJqZcpNs9eLrbrOOEnB69Wkt3g08VpBBKQSCqpyU9mdtyYT+BxuVVDgXN1UVzpUHbe3k3gKeXcbFxebELqaaf12qRwEcu8oMtV30el4aAhdocxb4dCHafJHU3fW/v2+O4eTqVDFPU+iZY6ZWbwWl43asj7Bk2RWKjR+HLZrHN/RUVfI0vlSSiY5II0CnW3O2ocjJxCmuVcQfnlxyGqSMmcY7qK8I7SSt/0lt1xVcaeZ+vKohibkZDyH8yt+uG2aS8SltIuTqAkZ+CFgqzwrMmk7Lvco7CSnKxUkbZs1ZpeyCpR65rU5Lwe9cDtrb1Xs7YoJhHU+pXWdhK1HIFZ00W0/iBh/jzjnfXi9uOGhVxG+77e4uGs5ptGQMKGPy01OJOvLLSfZmwFRjDJ422lEpPFoEUfE3sh0iDeV040FIRwQxr0ggdqIkUBqHOQdu26rNYPRgmEcaSlU0KzkEvNDSdtbOnEHpGWk5OphUIOx9klL3HzfEAeepwy9FmqYwbtTT7K5sBW0urxxUBXuC3+6580l4YeDjgP0HtAzt52uK5WMRVYlGajQpjA0qxEAVJZlveglGyjUSKPcqTQvbwtTGY/UWdidhvrk0DBVbtVbfzh3pRZbGOjzDztYtG8ku56gUN0hS9ZC/Tw1ZN7JaLK9MIdjvmHdTbqJhA4P6yEdfb9srWQjpbZXKARHjHFd9/iZQX0QyfigbN2LbW3JKVGVgynsj8t+X3WXdUDcGdVxmSaUNtUxup0pfq/Wuk5fbhUmlYKEtUllE6vl5BgdJEaRuCchqvJsnKNSU2xtnmDrMSnys0Za5oHpsaD1z/tVg5RdeGq3KzdkOyHhqWQ0Y0KVDqiFoBLfl5QkTZt0b2Qo7+kTf4NuzR62SI1IIZv1i/wyxZsNQkHadX9h+hvS8oZpLK/rzuJ3ihGTK/Z83EohgXEGbsFbZjomxE0soPVG5pwr0h2RXcOUKp9NepKHBVyL5VlFTVPwGEzTGQ27GUbQGmrDVKW4InbQpeaYYDiPSBQmlcYY3EqaDoO1vMon5HgvZWx7rJKTTqLOMlhhpOYzpq4bvm1pyrHdi3qsK+wgWZtR0YLJPLnMtNqw1U5O+wTbR2TZJ6wo6+dNuZe1rckE+5CouN7YolnodqI1kGD05dzS08brwC67TgxO9DJC2LyYJFyUMS+v1gkT3i+9tlXTqDKFlXtZcqK4umIx6IYjywWiObElKB2OB1fkWISCY2pNbbXiRp4Ex8ayIDmECKrdqCrxY3MbXemVMlyVC+6E214zGWgyZf2EjIKIibS1a/hDltBLdtJBUY/WTRMJt2jY5rdUvoolYVo9rPtnU6jXXilDNENeNncuhsqYdQKlWrY1tjnvT9i0P9i+aaJYTnD+SrlIm6Co6Maib8n1vLEF5kTWzRHCtkHZrtBIXnbc5hSTO8wrNDRQip6WzJQXdoGS9/m1jfSzR6IWdzfqrDzlk2Uf9lSVbo9BzR2FZb/JTOEgovZhEiSGXnPs0XD0qyFhytnnC3ktG/fwToCObFrn7fW+9gjxonR1cLEzCMvMDcRwO5vEw96AjoOnMP5ml6eeGiUGdU5U7mRRwugVRO5LZwbxsgo0L3BxtNR6f1gndnOJ79IqoxuDEcd1eTxddoYCIKTlnejaDRcF6xOLaYINtAlvcAxJiCj7KbWx1fNd03NzipBgeQrsic3aW7ydKDJhrnCKDwwFmjq3CWtvLNAGCiSmgPwJjYXjFusuUYs4iMltuMxT8V2nkB4lwQl5u4OcOkqs0pK4qRZUa/VJL0aHDab6w27INtGUVocyrJzWtA4pw++xspAMcs9IHitRaS3wWY11Oy/noN4d0IsVYtbYDw5K11xuZfH2uHZOpxRAzW41hjccys7tPVqmcbNjJmGYjIzpt0nFIzpqydZKajGluKPkqjgsSckkMMOXxs4k4ZNz6ka6PIAqp06mtTMOacT5J+UUIrlcNJR1G5UUYHo8DKJhjSt/sx/KSKlEEXY2fSyXOxlIKumlEMGmLHi2u6f6FQINm3DZl6AobJf39VU60NnKQFtXHoJyBAIcErOeKlnowYyMYu6pVgt709ci7DnqaXRL3Sr0AUKkvaRJ8rgnFZ0l9U1CIIqfFlYzEKZzUBMruzhVvNXJA5sWWw8VexIb4sS0LNytousq0EqfzY46G+db7WJoTtCVAlzCsuHYthWwrNCmnRNroPCcZZbac5Hi95Q6NBsa1TOytXu0acR4XUMaQWBSjmwvUs0WDsHmnbdqTDQgDBEXNgMLBQl167E0tN2LwYBWLAd97WVonc2RuxN2IoTIIPQkmF8ckSrOQ8gldHKINdaDN6AnHvYeduRQXcCTULdjVbdrdXcgLI/07YYOCYfpVGaCOGx5dy/F+e5T3SZB1il99dVsjC/FSduYpTNRXq72U7W1enfM0RKn4DBxyoEROIjFlI1+PKHp6pJPhI8sXc8pDto5cFE+jMoWlK0q5rFoj4VSxGwEJZ8wve0v8pYCbVLgMbWmI1J3k+7H9CivKYlYbnmYqGmWHcsdNIlah609yl9j97jJbaMLpRXC4JZJbM8X6R7HezaL2r0R+O7Q1eVaL/ucYiIpX0HFZTUc0L7rijogDjnfrNP8IBTWRYKNfQhcdEmtqXX3Et9mkBpymmH5NS3W8sYU8rPQXSVre3fWWWEdbueskJB1KK7znV0X3AFuUGl7MW41RVGQPcFjaJiiW9KiGmQxsVOoDF3JjrKHbZKNqd013YyJkBb1anA1/GRyopP5e9xNb5tiAICu3zVm0wWrgyuEm0LT2YM2nmNPhe9g8ORwL94YPgaTd8tYNyahYHSS6nvQX/ayUtU7WfGHkCmPo0Wxjt5DHnQ0JF25Eyh2wUzeVljXO9tYYMIDBZvOHVLhVGxVakhKsz1nKXqC5DMotYm3u9+403q31vRbZA/qgbNsuaNZL2Z6xXdhZiniImTBjLOj2zuB9z5nav01xY4mrtjlXYy1UuvzbshiAzlS3m1pUVGW3k5T1aYqACDucqc3tW0TbKQ4yvUyOlEPtajcra6Bfzg72kSHjmljgjMAEMDW1HqVNh3souREOPSxr9Oblt/qUgFTDkIfb2YNORGtYsCNnX0BW3w7GJd6pJ7j4xVgY1BNXgSRhL5ybtKq9o/W2iDLCyTQ8mGqkP2yNg53sXZLvw1pUGnrm1xUZa6wYONtf6MKKg4ZQoiV2myuPo9tows6IlddODeKHVVIYey0vYn2ng/viJTu4M3q4Iy410m35kCOxaqQjwa0DuWWwzj3evM2u/tGwyfNlDv9goad4QYuJMtJkLOl3++te43InKq1XEDdCxjGUHhkSeNUCNszZcCwCJO27t9SbiUfbg21g09lE1TS1PQXjroFawtyEo/fW5K850PLZAp0Q6wRqoGXw2qrazeRw6LE7S01YkHTqEfjmFOVtGolbmiT0aZIEwzJYSNnMd11LtlWG6m2xN0xPNFs7+mgTvsJaAcHmT9DMlLsioC4deNhpAVCEvaddoSxEFmROGGcDsrGVOl+K96Ue2C31+0Sx05jxigHde2YEkZVHEThTZNR0pS7Jq91cnDTHOxqgjYBvq1x6GKiJQHHVCUUjJQzOylnq9WSHmi3XfHj4bw+2TkA0u3aRoUsvtACuCqxi013GzSU6p0WU2rQEkHu3lW+NnFs78bDfXkSoUC5quMF51BvfyIGIrNOtqBX20IKiv5SrLaZu7vm2+hIkdfNipIJwye0mvXR/W0AQ3UbZ+xG58f4aMEbEUmc8BKZ21NYQLng8jfl0K/bQVEPwnAfKoVDlRbOEChQ+Vve1zR0FHY0n+yYJYHujQqVpXWFKeXV4D1jxfYOFggJerZMshuxeurQbuKKHEzsN6apCgIORujacEiHGfk+pwcpItvdKN1xLQduLCnCFxSYwVhsHZztuMSjm+y3GIqSZ8G8yD6+dLIdv+VkChHIIpXG0uosVzcgHkxMWU14ewo7kDQZ56PjYCONDGZeyM40hE5SoWSEhwhy8SnRLloYt49JPPGNXLksYpgsotzW7FW5MTFjyN0xLXZlEUeXo0qXcJVtp3qfSjGNsNdm39SZytQElBvynsalbWDJjRujCAFJ1ETebq7j4lKY31Hi0NS2g5aYFUJh4Vc5rvBm4u/uh7sTBK5yN8da47dFMUI4daVbkbCzs4ubZzrcEmaokmlO7gWNpyGlWkMTRpnb+Izdqot7HkiYoZMk3dbp7pBbrU6RO6RCzU4rB6fJUhPReD/BXe9oQe0OyjsZ0mjPOKNob55TfNodxTI1Ttx0Tc4G57su5wbOWlRPBTS1EBpvlzbEb4iJ8Y85fqYJUrP5HCJYfy+MIQBLcQyj1Unksnu13HFck542yxxiaeWKKTZKZ2XIrHl6m8FxajaRpxWk4/Aa79CnK0extkNe2yZXm5M4hdO1tzpyT6P3uLA2qLjsK0hg9vURWucavsapsvRLzcLDc2qTmVmvj1DByzgqSCziulrvmIqjg1YRvfpYgSWuY0bk0UZPBw/PwTjl0z5GOwbA9+xq65jrTLUfUh4n6ggrO0SMcQotdbGEdVKbormi3B1uffXAQNyNdWrCO9G4qxcG64QtrhgmRnfBbutczqq7MYcbDXq92y0KEb9sdqlKLBn/fPSqpV4cvJO6bWpuJ7ObJu/YE9JsJDgqdEXxra7TRurewlyHxsaqJ2kwkB341dr30cMUEo1PBctkFfqtysHQSap7ysa7bVVm9pEvC2/JFB0ztRhRsCS6JEJKPGzg6qCY9TlgvNogcPpqo1cM7VG6GwI8p+PbjjfXbRNRUEf1sCvjluxSTY9p0xXL1pQz3jnU7gqlPewyW4ockBNhL9d6SHO0S6tisrouB+6E0ih9cGjyGtj3SJ5OgqwPbOzl+tWhUa53NLnzszO+aeAzX26POYvze5ypdlFhIkkrwiw/Wgx/KMfAtQ9o47gSjtKydCXUsrhdd9USDGtOS7uuf3SR0GFZ98rrqlWpG6rk/RuYw0KTHdehsgydEbi/7nbLA9+tQwLC2b0BQyWennVHhl2PlVej4gOYlnNiKeScCzoy3BV8T9jpPoqgjVf5BUzKrM/DCLFpwnBYQs5FCnq7xJmOVHzMdAu/l50bqWbG/ZDcKDt2w43FXEQY8hCFZRUz181iiRnUDXcbFz2jFb1CWA83N+ZkXmwuYuRTH4p3d71D1rqZ1MnE4FXt2UZa0oZ8tpcOsd6MKcFe27hY5tFZX9dHnw8IUp34eF3ZkK94t24ADcmKbu1WWgodhId+jl8ihEeX3hIi0BPeV4cUrs8j41wgGcXzC55K1fK+1dybFcVuvXcuNmMeaRTUF/QeqBONr7hQqTUFZy7VHTrGDV2mOz4JdLuC5SCMlrLK7+1+dwrrxiCb64hjcMQzB9xM2VRiGOYvf3n59PL93PHl332lbT4I+n92HvU8Ovp4TeVxrho4/ucHr8//tmR//fTSeAmQ63kC12Z99H5Q9Tfnb6//4gnqTGR6vjP2cV7+PIXvnGh+ufolAYHWds30tS2zxysrYIfbt/O7mO38uq4Hvv9wTPyu0nxU/NCm/Pp4w+9jb1LM76IEfuJ0wftl9H4w+enFf3896itOkV+Dppr1fX/dAaiJvyFv+Mtv/xsc+//1EC8AAA== -->
