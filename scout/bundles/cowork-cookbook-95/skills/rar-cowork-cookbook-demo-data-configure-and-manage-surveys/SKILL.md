---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-surveys"
description: "Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_surveys", "rar_sha256": "0885b851cf8f0a4b16753393b41cbc213db5bb1ab1b3fe0f67cb79bd5f0459ea", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Demo Data Generator — Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
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
      "description": "Sandbox D365 legal entity to write to (default USMF); production is not allowed.",
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
    "record_count": {
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 0885b851cf8f0a4b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_surveys_agent.py` first:

```bash
python3 demo_data_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_surveys_agent.py   # or on stdin
python3 demo_data_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Demo Data Generator — Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_surveys',
    "version": '3.0.3',
    "display_name": 'Configure and manage surveys Demo Data Generator',
    "description": "Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3a3db1fa7af449f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); production is not allowed.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic configure and manage surveys data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for configure and manage surveys. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-configure-and-manage-surveys-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic configure and manage surveys records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo survey config records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); production is not allowed.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for configure-and-manage-surveys in a D365 sandbox tenant; never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConfigureAndManageSurveys(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageSurveys'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); production is not allowed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWLLnV9HcFzFV9bAvAsTmjo4YgVgkEEhsEipXuNhB7JsE1KvvPgfpXttVXf2me2L+GjlsITgn9/xlpg+/vTh9F5fNy6cXPXCKheBkWRIHzcIp/AVb3ssmBV9l6oK/C68suiZx+65s2pcPL37Qek1SdUlZgO1CUASN0wXtAsUXTeBkSdsl3sIP8nLR9s0tGD+C/WES9WAV2ALWeGXjt4ukWDiLFvBzy2GxwQh8wf9Pnd0vsiByskVQdEk3Ln70g9Dps25h6nv+pw+LtnMiwKqLg/xBoFhwgxdki1ngh6xh0rTdh4UHJOneFn6Y/535dn1TtIvA8eJFEdzfBPmhXVRNkjvNuEiD8RXoFwxOXmVB+/Lp518+vCTg+uXTby9e5rTg1ssGKLZxOod9UypYF/7eKYBY+kPb2UKZU0RgaTUCExfgdxU0Ydnk4BZQZ/H268c2yMIPi//8z/TuNFH706fPxeLt8/ll/qP1xSz5oiudtgv8hedUjptkwCyvi3V2d8b2q07AkMBDRfT63PmNUlkt/j4/+/HJ5DUKuh8/v5RV8HTG55efFmUD+DX9fP06U6l+/Ok1K+9B8+NP3+i0vXsNvG4mBqR+/fL2+40sWPhtaRIuvugHjn3jBaycVAEg/p1+8+cp+hu5N5N8eS7+saw+LP6a8qzP34G8zxh0Ad2/JgtsAHa+vF7LpPjxjUdT3oLCKbzgx5/+GVkvDrx0juB/ie7PT8Jx4PjAWm8mAUE6u+CXBfSm21ea/5xtBQLm39EELH9n99VQ/4z2w7N/Ip0lBciNd1/+Jbm/2gD9ffHzP9Xtv9vwYRF+BomTJTcQd24WfFr89giRn3/wv9384ZffAen/Ixm97BvvQeFL7hRJGLTdly8//9A+bv/wy88/9BWI4sDJv/RN9lc0/8quDz5/sODbqh//uBfwN4u0KO/F4msOLX4rq//R/P66sAD2+d/ut58W32fi/IEWsxLvTJ8m+C4bWyDrd3b86eV3AD8F0Kb3Ho8BfvzHfyz2ideUbRl2C90r+24BHNwleTALb8QJwNUH6gEFgF3bBBj2bR2I/9nDs8RluPj1f3kPlAfg/ER5eEbsLz5Ati/veB18Aeg8WxmA25cnlre/vi4MQL1skigpAE5r68Ph87yg6GbOVRO0AVjoL9yxCz6CpP44X8xY/eu/xuDLg9ZrNf76qEXJEwM1djvjX9tnweus6WlG9KdeHigCwRB4PWCTlR6QKUwAen8AFmjL7Abwc7ZKmyZZtvATgDCgjI0P2sByn2Ziv/76q+u08efiCdjY4lnfWhgs+CrO4uNHoFyYJVHcfS4CLy4XP/z2+w+L/1r8d7sexGceB1A93vwCJNzpqrIAedbnYNlcCgHAO/7DL7/9/mZiQAZU1gXwYhImz1I250Ma+O/21sX1RxQnFm4A7AxsnFdl04EqsEi618U2XHyVFzCdH811Ii7bDhTnKij8oPBGQNUB6ny1ZFF2oCZ3SRuOHxZ9Gzy4/uo2zkPEHCS80/262LMHUJXKDPwzi/lYBDaXRQLM/zUanvcBkQbUWOadxOtCmSNzUTmNU8WN88YjdJ5+AdXofTsg7syF+nMx1+BgNtUjTZ7miea+Y240Hi79OPscNCo5CKZnb9G9r3Hm2mk8amjzuWjfUsBpgkcDAEQZF1Gf+HNh+NtbSLVx2Wf+w35A0pnSmxf8N688YvBrB/AIpmcUv7U87WJuExZzn7B4a5DmMtujS2S1+P+sY5pNsRYEjRPWBrdZcIqh2U8XzX3j7MpnqzkLB+L0mY7fepl3vHqH7c9FloB4a8a/PVc+HPu25gmFwOI+wB3tQR9EFXDRTPcR9HMQN82cLs7n4r0+fABme4AhsCVACJBBc+C+M5yfvksaAxiYf3/rFd50nl0MAntR9W4GfBUGge86XgqkaubEffMsyIBgTuJ7nACLfa/V7B1gL0B/AYRIQCqCGvL6FbOfT99F/8PGZ0s0b3m0iz3I2+ZBAMgRzALOwXdPOgBfTvds04Genx5EgBp51c26uyCSnm6do7oJ6j5pk25Gyaddgwrg9Mf5+6npfDcYKpAswFggJaoeWPeRRDO+5KDhATKAkAU5lSfFM4DfjPAg6OQzIgDEfYuhJ8XH7TeFgkfmzZXrfeOsyLxnbgYWIRAd3Bm/Bw7jr8IE0MvnFQ++f460r9xm2jN4tgAAAcf3p8+u4fVZ+J+dxeKd7qd/mIN+/PdGpUcpN/8YAJ8WcddV7ScYfpbf9+r7CqALfsraPirxx7lQfsWB4CNg9vEJMR/fIOYP1J+Kf1r8exL+gcRbhnxaIK/L1+X8SH6LsLcPMAj7kbE/ruannwst+AavgH2ZgxCb3TeC0v+1Fr4vAQUxagBMgcXP2tjOJfUOUOZRDIAvPhffh/yccqDWFNEcom35HRQ8mgIQ/k/Xfa1Z4FHRAd7+3E5GwTzHPRKkDV4+FX2WfXgpQPD9i/PbXJvyObbbefIDWQQ6tC4JHr8eUDF08+UfB2H1ceFkrwD7ASxl7ffx91ZR5or6XZo8FQUKeoDDh4X/AGAQmkDRmfmcYk4LYhaE66xQN1azBs9Rb24OH8D/5Qn8/yiQ/n2l+EONAOh3B1kyj5Z/qhd/mzHDf/abM+rOtgU+BeOg/5cSfO1d/5H9CbQKMwO//DRXzQ9vaAS+wbwB6s376AD0fhvmHsN30YM5+ed5bJkd8dgyX4A94Ovrpq//DeEGL7/8hVxPy4JGEzTH/yiaWN7nej0+a+57eQWyvofrN6ug+E9/qfh7+fzyDKs/c3jW2Ln2znj5CNx54YdF8Bq9Lv61BP+ILlHi4xL/iK5eh6wd/kKOh6YAy0FFnI32zRvfbFI+5rpZZGDD7vnfEL+9gOh2ZgHe4vttMADLAfR9bOcmCAYwABiC38+EBc/+L0eGNypt7IBmFZBZUhTuUjjihVS4dFYuQpA4htGYu0I810MRzHdx10UcF3GxMFiGBOm5JO36eLhc4XTgAHrP5P8y93vJLNksFjDIR4AfwbfH4Jb/ptJThdleXyeUWfU3zX57cYnVHBerdrt+flgYQlwCJV1950INEZT4kZEl/aARznGKEA5NsEu7G7rIKwW/6AhBQ9Zlm+iDceHbc3/fxiWPJ2LBBheZnuq0btNYa6vDhayWF1fYcFyWIUSn46Hq6xfPH5jEr9pyOFk6wRcrLVmNIaSXdTLWcNbFbOFVqmSS8HI49ZdRud+WyESROg0rPp1uLyuKI4vliojKcslyCj8pxVF3mowWHHs7HC+1GNuRvrJbVhoxfYLkJRFAQWKFcFiIo9VqI+757C63TLc17xnXw0l6G2Dv7FqEOkhcc7e28Sgb/n7L8EVx318SvF3ekDolLpatFZl2Tc21kZa0x03wkqyyTA/4VCTufJlTS3tcxd51dNRDccK4rKPxyDtMBB0WFwJSDxciTEgFE6mBoqkz1zHh5RglYWxBJjHZObI7asemVlhGJHOZkOwiPVGzacrouMmXnCefd8ewXglyrdh5wtnm2or0rZvAh8Qbw1bb7TMg2dZwl+Vxuu23ObwWl9xpmcnH4YxM8o1d40Oe3WM/y04JLbp3NHRI2l7CXmsQdLZKAgY5tBl2JO83vuFMRdHHYhMzSBixmsYieaLvMinVMWG6JusqmKCU96JdtzbthGuoPk2jtoSWKnxWKWV04up0NZQtJ+iwWKYVm4fKsmXZneJKWE7E3gYex0lSeM22x4vWRCGuWp2a8hMXVlxEZ3IB9WUisdcWjC1XyZVl24BaxK224eiNzoZLd1I9Sc1W0Q/1EW4M3r6T1WYVXfLTvqO5xNg56HVpUFN47BlYHPJIoC2V5o+50EXbvX7BOVhRVuGdU2SKG4t84sfhXjPm3r2YO7++s93miEU7t0Mth+YqdV/2esOprVXjOapZRRptz20s35LrnteLVXLMfIq9WYeCoziZNS1ic0Mj5a4deDJej8JwoXIQIMvDCDWhUJ12fmal4+EaSYGgxvi5YvprrF8HTcBh9sgdu6Mqj77tENL6IknMwDq9cl1aZ8oJDZMj74hGrSYMFfuDIpIWT5yp49AWKW5Dhgvzo8fiZ6Ee2NO18e/Sbusg/YBuy2SU1FbekvtUzuFTf1pvo0nQVklMydsuXEu3Vr9WtrBxFSw7tQfH4LUsTa1SNeg2PiGeE+Fpqlu1tK4hnUt7kfOSruRSkd2M9rRCmwkKk9iN/CXreNuI3UMebqpyHl40JcfvEem3bh0eZXngb5hKnPzE4g41qqlSVZylKt8UZKaP1tgMipV2G3a3zNQtRWS4mF54/nZze6vIdUjhDNOrt06LFCI0jIJglvbo4Actu+RoymxW8iTjy3LU21mX4CIK1+21P8mJXKesLW1LPNqIaxer8/1uCyFhncsYUUYcllOT5FcDsA6Cc6wtBBv20EDLZpdvs7YMolJSnSPJT3lu3IwCxP5t2UxygCl5pkxwccjMQfdmaeHj3lOyE7tD7XWE2X1CZvsmz+WWLu/7MrfTtb4VD4YH2WQLC9eYR4So2MPaEaOuh+7ITJoa+rLuxgO/PGEEu+mFteoeWZ9e7o7W5uJhl6iX9nkXcd0mYU7+fuVm+7WU3jNKJiPWMSCJ9xCe98yY8db3K+5kFYKaN+22l3DfyrL1ld3h8MS2uNsRFRXuS2u7q3sHJVUCH24Xm6HtsaWqSBBbpglwSZvIcVsPZyUYki2NS6sQMm/JoNMJEtnDhbltoF1bZsy4r68hheOltu9LY+y2zPKqVJx7vq4vjj74d98hk9bM7zabFjtIzq53SU4EYaCvpgfVwiHcnnThxGX7UbW29THO6aurANzMQrdyt7mmmblo2mcq8AfFGxNEusTqjoCqllD9y9ks0zbS0zA+oqxScEWetXecPbtY79ExwrUXvTmyUdZdabU+r62wcdGKW3vE9rQxjP4UV6EdWvX9UvYAQZvreRB3IyKrABOJQNruK+h6IFe4eu4wz3SilGrbwSAYOaNFAKwm3HtL3fBIXizb1J5u43bCwqReh2JwEl1tiI+TFEIlvNHCUD5gIUR1txuMbcwORHZvmKf9cjrgfnu018i4cymRHimqV1iuqYQRNc3thumwIO35vX80UTT0sDXCB9DxCnCgSspKTjLQetsysQ1d7arXWr/cmWLH1tKSXVOnbXDB2etI8hlr58a+Wtq5zE5MJa9OIbwEse64QoaJzqjJI7cefJHBEHy4lvkR7929KjueukdJquu0CC9i9+xAE0B8RW3CbhWwSRudOFYfLNMcSON8moI11UnKOPK7frc5Rel5LdgSQBhxwh2sYYZ7lZxvarOJ41w8OGuLRjfoLXMLR1ybzWZthwc1HJtmXQZFeJOX8TVxybg8qjtr24chL6L8SU2v3lJLpAzXyOt2Z28wKTxDvbnDj3tjJyingMWcLYuUuglz7BhfxrrdBmFOWuG2SOuN7rTb6y7j2KpPZW8FM1VVY9HVbmgpak45Q3cKZ+ejxNlQgPAn+6JLW/yQiNtcXqsg+Xgmq1icdOlLNcnrzZXas3ksXbn6fDa0nIp4duBJLjoLlkIYiLHW9DWM7hKNO6SAvnonT5S6tQiBFo8+n0pjvFWaVcXr+a1nyj2TcDje1I1rSdWtAkCN5lp1LuszrSZ2Ed1TEiA4PNlKjSSQTnVnydlM8p7WxmmdVXac3xtN4BM9s6+ESOoSLBJVnXMyeRLuRzC3eVqL2FDqbw5MzdglA5HuaslN4jrc63l24GxEoAheAMDKASc0BKm3hw5XnS1jDOc7piKuSXnsCpu2XnLpb2GwbSBV8w6+wERZudFhSGRQr8/LlUe26kVrhR2Usnqd0HG5TUcSE05XU40QhDmOhraflN061uu7TNA8I+j5pbpjpWZr9VpxGtSxm+rSbHbB/ZBHSdkiFKSttGK/NDhbbquqWMrsBrG9oqwM0pcSyZioSGIMzaJ6/KqA5ml3TPgi3YtJgoxOcrN1OSMP02a5jZnmohrxTYcOXg1CVmD0kO8UwnPLqxkemXQdHbNWGm0pzZ3DOAhLZkVVHYfsXI/HNn4Mw/Qyj1wrjgZfo7lrZkZe6EgYOSh4XqqngbqKJlfjqpeKkuafhdDS5crDbxPII0XaQ9kAg5bmuCS1ZqszjJn0upN21pbndn23jicKpq/H1VrKJ8Pv8CkKGlFMm0ubkkR3Nq9bAnRBrAIh+2ViWWm0vDfrpZVw5w3CMl1kF1IeyZUSnhkz5SHHrZGjJV8j7twlvCv1HONOAb5Zn6Fu3V9wyGj3qrQeeEbCTDNlgkwh4ovPHnljGQt1aWA0D1cb/1ydEMvLp9K5bJeBcKsORYnasZTLfXiMhLryqqvknO26BkXLX2YdvsqFwYfllLocQkNbwfk04cit9XicommCUCHiLlrGvbm6rnRBLvY5HAIIE3k9zC4iyxn79Yn0doq5Z+LEIQcLzMpnWY7PdVE3F2/FMLd06W3Q00Xo6/7ONJJiym1qWpK+yXg/3dqn0+kSn1gWRSHHsteoCeYZd42Gx1ZVTMeWh2iAJGwtj6G+q4RQGm/wAT7m3BTsYlvRUgzb12lnWxa0S8IgWknTcCGuBLTacQahOTVSTDBzxk4Df5RLMixcHHgOEtWlhJABhBarUfTk3XCU8gAChVpco4LuIGGXtghAzK3vBRueVa7R/oj4dldu0DuIDgIAi0BdGeaK675WSuMhR0wxyM49QuauhBDB7VzBYe04Z2ZdKIRtYKE6LrcD6UrHE6p4ugRGCpMTKn2Jh6N+DiXVi1d65osooScapE40RAeh7+xwyrFM7HC1zbEMJRO5ev4hLaWMj02CtLT2fmK72r10buxceoUqUEFGO83kPWIvTsdMz0ID0esTpkZxeCINKQ0Fy9pgkYHl69GSZSvI4INgQP2uu6dUfQwvF4G12PUedHm0p4VesBzyXjFAQaUYpeY0a89tvPvJth2EoeggKZjk7GQOvAUN09HaZpq2Ly+cA1fxrUKP0uaATOJtmWzQulLxS6I3rZBuCx8Lm6jUXEwfPAofRnjKdcRgMgML3KJGQvVuh0FiWJdI9LeM35zVNBKZamOvEPtg+YMYZpJyQq0c4Dkj1iJ1P4lGb1wsPdZg5Mzju8y9jS7nISZzvgYedob5GEwG3A5K0N1w15IaubmXaPJrBykdeofKpivcvLs28TXqDO72wA2Z4tt03JZmk3Q1A6cXQ6hYoaPXad66h5UFHYm4sBs3qK+wd0uPjC2SztRcb3cLscd9QKB+0BUmmnqo3tMHYs/qEH1bS5Gt4n2y3Q9kkkECwvs7AuUPwlSVgDl1XGGpGMYdIvleW8an8VKh+z2BH8CY40HjcrM8UFdqwFO5bkD+RyJOCvCSqc6WWRQ6f70q7qnERMU8+AZnMktRLforCH0iUlcr1odGP4FMr/QVY7nFhBgUlyNm0fH1vDkqdMyiDrcaVIIqrkuqCa6la91dluQhgp7kfBPaqIIirnsfBgzpDJH0A3+1bEj9cBrhs3wq/JQo1WHfKTiCY1wMeq9d0tmMeUCDPuqWqyofwwobyOgqXU9WUN/2t36Y/Mhhwv56RwptY6mg+QBjR3u7Nx5NMhoPD/ThMKxFXaihblvhNnzF4zU/aCzbCCl7XEsE421kXT12Z7qFCNC7mlgIu5SeF9mJqML8xhMOMSkTksvbKgijqKMvFwQN2vwcKBji2Yd4wGVj0OSOFGKFX/srEqa7AF5xQXu5jNre6W/wcIT5ArQjSkivJBABCGXxZalDySEsqTXlHzQbF1fqDt0sj9pyQ7GhSZSiQej8ZB5LM/YlIWkScWWqR5Hhjuqe3G4xJL8jfHNqNHNPeKSUuVV9LkliM7SxfUJoDswBKiJ76ApYXFAFXrkJu5MHL2Pdczpi2KFrVW6vaypLMraAibMBGp0q58pQQDXMi+rQR49DdVaWheNOEudnYbLvLgWsIThSI5sLdunYthdubhI7MQKu8dOVlqRbIROp392X+3FbKXd2n6/5fb6JaQovCbJFxFg2thrtOhjCsn1uxdMuuaIT0pxPVD6ca6H2TFvIFZJFy6WD0oRygnT05HnXtUEbbW3sjdtwOuvLYHuChq1iDVvNbjhXZgoo8gh8fWcCdnMEY1SlnYOgl0zP8lUF2aekuQyW9i4KnOwQWYx73DXEoJSjT62Xt52d0Sid8lNFULaaUaU8qCnWDDjUDKvRPxz2tCGO8V1mpbTqBnn0poBRA9SIoKEv89VECdQmgqamTu8wednkwdU2QmwJcbdCldhp3xDrusRNWUH8pMpXG1f31tSNR7i4UBpVaRty1eJgto7EfY2jPRG2qxYBEOhqmdf1Dk43+FYXVUoupyNPr+9up2lI7DPGigqhYX/elMV0sZJDf3KQuGqM+gYKiHpR8rvqQOUOuWVKDlmCsl9ePKSXNtzhBDB1szyd5aXanw+nSw9aUGkjl/eDbKGbdRuFsAbptZKemP3lenQxdV/3tbJKy3Bs9cFB7gnWrh3XP+8mdiiCvNOhldF3FZ2jeQQf9ph11tojjISiX2eYKpI3GrSk4+CtIA+CwzyQ5IggDjV92OM4rHU3PziXlEHzqxtSnBCGP49928MsQcvXtpryZYNcVzoc+WMlarZDGyAb73ROxP7QWG6/NR2/QXJ+1ITAPQTh1oZukg8FOt2tqLG736BwG7nT9sgR2l7rbKMSQa3RumHS13YWVqlGo+IlNuBAzBm+Wdfpzd0pI5gOL/BArnb3sAcFtDSGYJIAWjZwU+rxFE/VbgvvrwFOj+SoaheFpMqIXpnQ5PDICEmN7XNxqkCt6Q79fWLMmlgpekQVVE2i0q0MqHbl92vewIQ6TIqU2cJHY0vGLmUKwZJBFeyOc051gjTzcB1ohmoMleYBlqbZlPPMiHTu2a/o8oRmK9UM645DmftJYosA63I0OzneiLaN6/c2GGWgQkiybj2c+pWfX/tJtg2l2QA1L1ejPg0R3itKgVZjcb4xvrmRzwGtn3b9Fr2ho+ojnH0y5EsO405/okjKw7CdjNJ2J6S35Wrtn2rcuNeq21R6h/eHzR4Ebp7pAUcGwllqI7R1g9CQ0MYjKlj2g6YULyZZGYRT0gbJd1iFjzJC3teUC49WdrlVRrDU84TPdzRHphFHlYIVFywc3kKooI57T6Ulv/Ql+M5nx/5EeMA0PZpBtWdrSOD2qccjHpF54rXGapxMC/uuny0UaMYfesFoztecr1NX8G10sx21LVYuu1Ov9ObNT/z+0oCp/0jv8wL0gRlJRu1tw8hUpgNDCUm8r/JhWZzacUPq+KHo2RNocMu1x21EWT4fj8ndaEhNYEOVoU5rZiSUc4LqtIPmd7iWhcSmgvRY3BkEYiqFP/l+B7U8LSK7mEaSWmzN892paWK608jZjFfprfAPeZjxhu+XGNyTGmjyifsZhWDWp0lno8KVyXQEVdIsseInL1xXMUE1jIuO1pnVLNH3FQeT3MsNOh+xC0yp69rFYRa0MvjVIhVntUeiC+20mIB4Ndn3QuBYqwrKbQeb9hd0ezjXyxTg6pE6jfS9HM9WTlJhKiRyk63WHVLsmSIpbW5tsRjV8CqHHHntwJj8kgtEjcysNCEbIpkoh7D4Qk5UtVKAKJyrB6mVlEQgxkesUji0E/CMHqGbkIjngr52JXI3QqgPSSGQxWOI0feJLHQ5QIt+M5aipKIddW6w/TUy9zHEerK64dUyqeIlYxlFOhVuk5chj2HUPmTqo4qtzWqimbjByxThxgLtM8qiz5segp3rZtxwpKmTyFG8tg68hovqcDq66Xzc8ve/v3x4mY/I3k5o/833xObznv9nR0vPE6L3lz8eB5GB43968Pr07wr2y4eXxkuAWM+jtDbro7fjqD8dpH381w4EZxrj8zWs90Po59F250Tz28ovSeH3bdeMX9oye7wGAna4fTu/3NjO77964Pv7U9WvCoFrx3++yBE0X7ryy/MkcT5LS4r5HY/AT779jN4OGQGBEfgs8dovGIF/CZpqVvntPQKgKfa6fMVefv/fa42mjmwuAAA= -->
