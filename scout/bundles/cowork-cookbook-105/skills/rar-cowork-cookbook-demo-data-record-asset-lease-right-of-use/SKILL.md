---
name: "rar-cowork-cookbook-demo-data-record-asset-lease-right-of-use"
description: "Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_asset_lease_right_of_use", "rar_sha256": "2c8349f2735307623a0d6e667b884e129780e646cf65c69764e57f5d2f68cfdf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_asset_lease_right_of_use`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_asset_lease_right_of_use_agent.py` and in the RCI capsule.

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

Record asset lease right-of-use Demo Data Generator — Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
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
      "description": "Sandbox D365 legal entity to write to (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 2c8349f273530762…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_asset_lease_right_of_use_agent.py` first:

```bash
python3 demo_data_record_asset_lease_right_of_use_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_asset_lease_right_of_use_agent.py   # or on stdin
python3 demo_data_record_asset_lease_right_of_use_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record asset lease right-of-use Demo Data Generator — Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_asset_lease_right_of_use',
    "version": '3.0.3',
    "display_name": 'Record asset lease right-of-use Demo Data Generator',
    "description": "Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-record-asset-lease-right-of-use',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d5c2d8a7c5f4121',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-asset-lease-right-of-use'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-record-asset-lease-right-of-use', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic record asset lease right-of-use data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for record asset lease right-of-use. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic record asset lease right-of-use records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo asset lease right-of-use records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for asset lease right-of-use in a D365 sandbox tenant. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRecordAssetLeaseRightOfUse(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordAssetLeaseRightOfUse'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRecordAssetLeaseRightOfUse().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V66dLbRpblq3DUEWO7IQkEsZHq6IghsZBYCGIhQJCWQ8a+7zs8fvdJkJ9kucrVU9Uxf4YKiQSQebe895ybSvz2zurasKjffXqneVa+OlppGoVevbJyd0UVQ1En4KtIbPB35RR5W0d21xZ18+79O9drnDoq26jIwfSjl3u11XrNaoOvas9Ko6aNnJXrZcXKahqvXaWe1XirOgrC9kPhf+iWC88pardZRfnKWtEoga/Y/6lR51UD1NvFCKYEVrry8jZqp/erprUCIL8Nvew5I18xo+Olq8XKxcD3Kwcobt+GvH/6UHttV+fNyrOccJV7w5vKH5pVWUeZVU+rxJs+Am+80crK1Gveffr5l/fvIvD73aff3jkpsB14RwM3aKu11Ofs/eKPuLijLt5cfL3xgIjUygMwtpxARHNwXXq1X9QZuOV6/urt6sfGS/33q3//92Sw6qD56dPnfPX2+fxu+aN2+WL/qi2spvXclWOVlh2lIAIfV/t0sKbmm1MWCEkd5cHH18w/JBXl6j+XZz++lHwMvPbHz++KclkhsFyf3/20Kmqgr+6W3x8XKeWPP31Mi8Grf/zpDzlNZ8ee0y7CgNUfv7xdv4kFA/8YGvmrL5rMUG+6QJij0gPCv/Nv+bxMfxP3FpIvr8E/FuX71V9LXvz5T2DvK+VsIPevxYIYgJnvPsZFlP/4pqMuei+3csf78ad/JNYJPSdZEvafkvvzS3DoWS6I1ltIfnr/XL5fVtCbb99k/mO1JUiYf8UTMPyrum+B+keynyv7N6LTKAe18XUt/1LcX02A/nP18z/07b+a8H7lfwaVk0Y9yDs79T6tfnumyM8/uH/c/OGX34Ho/6sYrehq5ynhS2blke817ZcvP//QPG//8MvPP3QlyGLPyr50dfpXMv8qrk89f4rg26gf/zwX6NfzJC+GfPWthla/FeX/qH//uDIA1Ll/3G8+rb6vxOUDrRYnvip9heC7amyArd/F8ad3vwP8yYE3nfN8DPDj3/5tdY6cumgKv11pTtG1K7DAbZR5i/HXMAIQ+kQ94ACIaxOBwL6NA/m/rPBiceGvfv1fzhPUPzhvoA4vAP3FBdD25YWMX55g/eUJ1l+eYP2l8L8AsP714+oKFBTgXpQDVFb3svw5B4ict4vysvYar+4BYNlT630Adf1h+bEA9a//tI4vT3Efy+nXJ3hHLyRUKW5BwaZLvY+Lv7fQy9+8cwAJeKPndEBTWjjALD8CIP4exKEp0h6g6BKbJonSdOVGQDvgrulFDF3+aRH266+/2lYTfs5fsI2uXqTWwGDAN3NWHz4A//x0MfVz7jlhsfrht99/WP3v1X816yl80SEDf99WB1jIaxdpBaqty8CwhfsAzFvuc3V++/0tykAMoNMVWMvIj16EtlRF4rlfQ66d9h82OLGyPRBqEOasLOoWcMEqaj+uOH/1zV6gdHm0sEVYNC1g5NLLXS93JiDVAu58i2RetIB526jxAdku9Lxo/dWuraeJGSh7q/11daZkwE1FCv5ZzHwOApOLPALh/5YQr/tASA2o9vBVxMeVtOTnqrRqqwxr602Hb73WBXDS1+lAuLXw9ed8oWJvCdWzWF7hCZZmY+kunkv6YVlz0J1kABlezUT7dYy1MOj1yaT157x5KwSrfrUewJRpFXSRu9DDf7ylVBMWXeo+4wcsXSS9rYL7tirPHHw1Av+4s1kahtXSMazeGqOFb7vNGsFW/193Sovv++NRZY77K0OvGOmq3l9rsnSHy9q9Gkpgxgok5qv+/mhhvsLUV7T+nKcRSLB6+o/XyOdKvo15IWBXg8Cre/UpH6QRWJNF7jPLl6yt66U+rM/5V1oA3qyeGAgWGkACKJklU78qXJ5+tTQEdb9c/9EivPm8xANk8qrs7BSsjO95rm05CbCqXir1bR1ByntL1Q5hBCL2vVfLOoB4AfkrYEQEag9Qx8dvUP16+tX0P018dULLlGeX2IFCrZ8CgB3eYuCyUkPUAryy2lczDvz89BQC3MjKdvHdBqUCPH3d9Gqv6qImahdYfMXVKwE2f1i+X54ud72xBNUBggVqoOxAdJ9VswBKBvocYANIUFBEWZS/0vUtCE+BVrZAAIDYtxx6SXzefnPIe5baQlhfJy6OLHOWHmDlA9PBnel7pLj+VZoAedky4qn3bzPtm7ZF9oKWDUA8oPHr01ez8PHF96+GYvVV7qe/2+38+K9tiJ4Mrv85AT6twrYtm08w/GLdr6T7EWAV/LK1eRLwh4UcP7yS78MTAz48MeDD9xjwJwUv3z+t/jUj/yTirUg+rZCP64/r5ZH4lmRvHxAT6sPh/gFbni6Q9wekAvVFBrJsWcEJMP43/vs6BJBgUANMAoNffNgsNDoA5n4SAFiOz/n3Wb9UHeCXPFiytCm+Q4NnIwAq4LV633gKPMpboNtdGsnAW7ZwzxoBO7FPeZem79/lIP/+2a3bQkjZkt/NsusDlQSaszbynldPuBjb5eeft7yX5w8r/QjQHkBT2nyfg280smD3d6Xy8hR46AAN71fuE4NBegJPF+VLmVkNyFuQsotH7VQuLrx2eUtf+IT5Ly+Y/3uDtDcyePLD94ywIOAAKmXZVa5+BLtRq0vbla6d2Z/+Us233vTvddxAE7BIcYtPCx++f4Md8A32E4BXvm4NgHNvm7Xn7jrvwD7452VbskT7OWX5AeaAr2+Tvv2vgu29++Uv7HprHwFP53+xHqdiAGAFUORJpV8ZE9j6NSn/cH2D/7XjXwnyyyt5/lbDi0UXdl2A8Zmey8D3K+9j8HH1T1fyh816Q3xY4x822Mcxbca/MOXpLMBtwH5L3P5YkD/CUjy3bovVIIzt638afnsHsthabHjL47feHwwHMPehWTocGNQ7UAiuX5UJnv33dwVvgprQAs0okLRxtii28zckiqNrktig1tolPIIg7e0W85DNjtyuPQIjHJ/AHWJHEpiHkz7ubnxi6/iuD+S9Cv3L0s9Fi3GLZSAmHwBWeH88BrfcN69eXiwh+7YJWbx/c+63dzaBLdmBNdz+9aFgCLG9DWxPogmb+C4Sg1bXo1LdeFO2W/Ol2Fpjfr3u8YAhN+RaNDb7wonU8fpgHbkbuLBgoehEUn4pkpeNm00Uy2500rLtdh8MlDbxyfzYkrE7YrMbjrlDWbS0h1hz1CZWPK2pKZ8scV2WUFrdutMpcqcMa5Te91mBj0V0mhXTh3vR3K772z3Ir2u9g69BNUWBwilrWKPmfFQKlXc4k0dgGK5SDHL7GZu9aMtLQ2aSVCrqPoVnum5ndiSIa4Q4+Han3R7TNdqx5+COHl289EVJ3DjRfi+maM0d9hJVs4ebZ3AcoTh24oQgmtrAsIln+8iWn8h0DtfnOCV2l7jduf413DGa0/fIsKvOtZxNCSUJyXipqXpbSllx5huH30xrRI/OtAwfdX1NXjh2VA2jVO/+3HHFRr9MDawPrK5r85nZE8WePqdKfti4ZzOBg3a626xGYLnOD2AHdFdg6H5p8rVe3HjzHtWZ6qnHJMJiDRsvw1Q/vLjFbDk2dg1x8m4l4kzbh7yP+DA5O/RshSktaE05ELpvclyu78OHv84sjT92o6xnQXVt4Ae95TRfYbN9IPTsmOuH5LQJUaJEw+6qS8Lae5T7ZDIThEnvyoRDaaCofF3ycF1JwxkWxXOxMYx7Ic1lcIJaJOUzhCQed6WtCmdK552pq+xhVM/tFU+llGxK3+duhHXapucsCHlaq5qhomSDJprzLSHNO0i4cU+cm4dNSEx2i9pTk+EZFDpX6BK7zJmoXEIYuTOpKPcknnhI8Ec45CyzYFNZynh2TnWqsDZToRFGwFq3sd5rqN1WKcFrZ1d10oy73mtjlpqo9vm90j+oXJbMuxVfRpMV/IKSUx45xGcslS+KAXHNhqFHldxjYbM5HUo0GQ8N2m/Gyo/WyOPRGFspaLF7ReedfiRyLT1GY4JDtMKckskodfSxsfyGZGV7c0MJq93NWzNpNqG2lrcza0B4vJtPni94ktZDtMwRuYgC4Cgu5iBqiFp5SpoQ6JkqNZTBGpfguG0U1BGePLA+r12FdIbbYRtqiiDt+oPo760I5yzQYvIJemaP8+6RrNe3yjPn9rCeXEJf35hKKwW92FJF2ZjKPXAHa8q1fRfI8nlHdp4n4N0hV/hyiPY8jc/pgHWPXapvHnkYrkkG1qHAPEWkf7BLiyrX6qEetUvrcSUbk2bUGPctUlRmHY/FwwpKy0y0xtqGawuWtvO+atrY925WKg6BLGlZqQqbm2OSxt45F8ohmSjPnq9SDup0uGWn9RjzwhCkp7anBOmoRCdmZh0juEUKwmLD+bzPYfWsaNKuQo2zDA/7iQ/FeqvEFTWks1IqvEVd73dVytpdTbHolUZdxRoV/RRcy+k62GKs2nvH6tfoeDqScoYcZ9iUEx2yhympR3x/FjZaTzP0kQrmzAwnTxN2tVfYGnWN9hIfHMPDjCP9ZB9yjYS4fWe0cUgSR/gI0ZnQQUIQn+j7KX7cfex2GrrDUAUm3IUqWhBjSoryKDO7jmIDRxImMae1MQi9RJ/DhxPUij/e66wBW4CE472M8ep1q0OTh53x8iYL8aXgFFmWIc3I6WuPnIKeKm/BLccI9LDLTwISy9d1XM1TFphu0NIoP52dGstKaTtiZ1REdDKFt80gMeRc3MT4pG2wMxZPkd7u5/uOHPJjy1REe5aYgNWkKJ0t5k6XF12BTlrG1Sxf3/b9uPWj8b6lIixUG5+dQ/8AEZR0La7q8XbMzzdKP1lOdNx1NnJAnNSnS/meH9R9xgfcA2w9D2dHywqhbGXeulRb67h7nO5Msk0uiXy4tpNgMGaXboPN4VbDzRkpN0xjKPWeT1K33vGCQRhwhW/4iXIrRqdLZduWFjR6tZE8VHffk/qx36XjNIbZNIfuHMV5ZqIo1Mdr0k9KRd92gcGoxYlGH4bGq10Ka6W07tZeOIIMhLNH1svtde9PZOtNAYBh53C+5MNDHnx4humS6Po+rybDt+peSUrsUed9Vj72DdUxx024FwO80n0W5wYprdqiogRATrOvU5fCsi05RgZJdfvkHsezfa+EK1cGknekYO20Xd/XVWN3gn0gNdDo3oMLS2k7uXCcMFR1l63uqclSp/CuI8lZlAOTmbdY7LaP2MXJQTSi8pFmXjTuDsfsdpr7dkzxI3sThN6VfVmkbbTCPGd29gpDYVHXcXOUyQ/0PExBbSokzgRJGNJyUvsScae06HBqRmV9w4cDj7LnY2lyTIyfhcsFHuzYdMQMGxUhWWNCXA7WSag6Wu3sbRV75i7sGhq0F+m6b9u14c7pFZtUSguw7KazkL4OxKTw4Q2uRAblOg4TPjrecRoBO/BaGcg8mwtdEaKQudltp+oh7Aexjo6DGXJljVPFpV8/CCElxI0AaXdBLgcjvB6EfROVRzQvXeMoGNGjFazsGsh7xtsfEH0kghr1SvkY04DUtCkQrsxZV2vXEEeROhgkozeU3lo6GsvGJThhIvE4SozSbS7xcNt24pq4o4yCSAZxC0yJHqo0SuzLY3M+RHuCn/Mq5KXSV29jdIzsh52VZniIMbKYdJoSC7qyd8IQdabdnqbHPmrl7TggFCJpURZk87EpKM8QvAMuaNB15BAT0xPNjyiEoh/5tTukIryJOG26KDtJPsFJMzOKfDY2o3C8QwfIuj/OKitVdznC216UpFGqN05zZ7bSvLttTJNJJJE6cUdXQE99DV1rLJYt2iy1fZL7ENxfsSE90bmjz4KUDHKyvho02Urq3gx3o1awR1uSrqyYDJpyta4cE7qUF19VOwFbZ70lANtYCn2rRCoXrMc4aHZPl4FYVdrRL0hmzqgLXZeD7pAbVq527SD2Jj8W6fiQPI85HXinQk+imzcnOjmN1EwJp0G97KTw1PLGFOU8sWOHYmxOxrQp6WOPXMaTqBcXKs923gM05+cOUk8EpZfB7coaMa3CBjeFshmC3qUXLKXD7K0IwTCT0FbRHu3iks0X4+IM0Lpt0eg684rTpjgngUTjhUlPoEk8Yk0VmcecL7dbOI/ZPZEQdsNRehjdclNeU1TJ3hPjDlWCwEUOkdM5D5O3cb03+Ckj7TlmWk02Va1+PNDagtojlSohTrgW6HpZQwwPVnjbF1jCdTeKocX9eGGlA63d4I4aObEZUITYV+Zpz8mShwhuR5nWQWOhLRGSuZKOR2VYexYnYrAPSxN5KQfN0sk7/QjHHrqbjeQk5aZK9HUZi+lxs9+o/HprUIZcOml6kFjlcOX0ERoQQwkq0P63m/EuxaR85bHJg/MZhy45OsV+U4oxgQ+gBe3ry9a4HRtJcqrYSEb3xpK44xiPXZc7tiYx6UWMNkeNCgClcDgKOl2UZdrOJ8qN9UhnjjlGtDxdeDfRb1i3R5IeCbLxoirqfX6UTXDdjxp5FpT7dYOSihscqWhDGfcMJdMdquAZbd4FJOoGmssn7cHvcPUADw3YmqjcvTtd9ue8e0i6UwvrPhR35P4Iqx1FrGETOawjV6vdW+P5hNUREXfy3JO93nm93MFt5617S+e9eLPjL+eclxFyd6kEcugv05HyEElKCUSZDa8129ngpJk78qDxl7FoMyjWYRO0d+Ysu9QBvvkhx06BhdPoDaN9/dGasUlidjR6uehuvLwqGbYwxevFZXei0kHd0ThOxdGolYPtBYIRi1WBsxfGeKh9CrYDFG8eSYhgIhW6zC0B+X0rPPDGUhPEjz19KhVBR2LXvQAISY+qfiUNFZRwUu9FFojr3Zjqwl3KoBvzXsR3zLg5M4Y6Fnu55YRZuNqGLBKmRK2HHo9aVfTbA7TFianAbVpvREz3kaGF2FOqnkiRG7TsDM1zpxqquB1rn3U5ROoYeWKwRGJpJPD4plXCeEbW1tlkyrEIySLKpwNmzOzB0JirJmrZCbJI4Z5M+hZ2VAy+1+u6Skq96AgscE8icTc2B2cP2eGt83RS7LlrI+mwjd7dyxFRrKEOI0Vl+Tbd7aWkgo+FR9LqTarrg1a3WtVx6a4sibXBzI+bIovKDRUw9Yi7ockJCUVkV8xHLEyACquaiNmetpLvq5WFYYa83QahXUriVRh66VQPKhNB4d3e8L6nqjaYkuaqcRnD462KonZCb+J6Z10FUZ0KIcDttdFHlH22VTsyGJ80ts1EHu+W4N5aSOMqpk3QY08j3JSh8YTwROhqlndGhf2RopnozJ7nOcu4h/OQ9lVGZ9nujEChPShUxe/bFHGZLpiGwwgj+2nAH+qxT8a5bh8J5UubDN2lj2Pe7/bbgOXEqk6v2+DYu6EPIE/Z6X6esw4tXW9xmIG+FuguzEJ0Ofw4buKqv2y4+rInzwU3NwWLCpBSFoS9K06NEHcXp3mIo8WK6KG/HtpjfBHo0uVLR+ZOnc0i1jxkuE5f4NyOAww5a5hl69h8YLOrSWp+u8Z9UpM1DbbE0XczC43HBmcIBEFPoSe5zDGweHRELlCZrOk8ndJ6w+dNTNDJ7WKll06YtO12l8tVqiGn6844tExvt9fcJOJBhvLarKga7wsVKkZdTs1rkdt8sR6nfeGpB+1q3GTbq6y89NSJ6aD2ACvDRsjHHj+pQuYZdplC9Ba5n0wcQMF4M+T7lk+b2rZAJxvM9tjDdXzYSqeHPQis03koiWGn7tDDbY3CB588qo7+OFYoCQk9bp+FRDV7F/QQ8M5nkbvDJFg8TPLQX7n17aKS18xxWsZE3Dq3p1jYE/6VhWyN2QR8eV/rjurT6rTH+cJFc5EVoWY8YjtrbQlGNveuXoM+aWfaigeKG8bQtTKFOqm3sx2fTsx9fdc327v/GGBeyDDdRP1rF9ooLxweNFMl/g7pwOdEX/gAoiO2JA/rDd6GsQqdSm5tdjcOc2B2tHgZqgu7NqrDnIkeqzqSB+MOQtcW6LBBG3Mz4KOJFKQdct1G0a4R9WAoAT+faBtHRgN9VD2lZ0ENbZC8YlhDtmNAznma17esxRttp0sOUSjS2b5JrcrtQPdu9Vu6abDHhT5Zve3c7rEf3TuD2yqSW10toVIi9caNF5reySpyC1O9A/Cb09JFtFNkVHZZUYZdiaGXLC7og0ajWtkceIE4SP7RaI90H26QVGAKb9MMkCP7LIzbU04zxNXryZzoTzG/3jkIYvjC6d5wkxaiFMnPEsY8SPZCk0fihsbc4A4XGuu66krDbXJ57KVc2vpXjIKcopDPfR9DVZwkDWpsuNAO+JYf6Glr6trRGxtuM/XNZU7XcLZ3pjp/2GU130TfPLvt0ZjWeIG2srRXylk1bt6+T26UC10ujVgI/inyNnyGOaAwj1t268S3XnItR+EYvJylFjnMe+Rwac54spkwpMhyOW5D5RFW41UvrDjCrRCZduQsDXuG1TVX2qF2t76zCQ0RMqGrTVbwMefRED6mJ0TtdZyC9Nzks4o97gL6Knb4HrtJ5Bqp0TXkIju5ua1TdI5l9JqYJ7B1mmErdedwQ4yH87jdmp5kHjqE7+KIE3q/Kq7zzXM60kfMdjcwve9Tu4dZBzeDrJNqE3Sohm1Fhy9FBLPYHrv61VUxNP+eib7CPrxGc6ydQWrSMbfwx2GrqLnhb/I9IteH3s6v/e0Anwtn4ydb7LKd9MM5obnHTYcUojARu1EQsLfUibJxXRWydH8mccWwBqG8XKKrn7NU4t8ImN6KeGhdCuZ896eDQhD9RDLFnXAI9XqZObSrz+0W7KOvHsxzA8HI203kmqcw2ohXUxNItFKxDXZI6/TwOGGFdb1Y8i6qCbk/eae6OOgscsm5ltxHJ4TWKPIIH2jb5bxYWsvqptL7MKUwxweeNUM/uu0NZ308VLxW1BDUMh+PXenRqUjUKh86YxSUp3C2du0ty5muJjZr+3bJkD6di9LUzmncnsoCbyLoNFsDMtHWY2uH/d27BtdyVzo4TsyhQ0zG3OtGZ0V8vy3i/KTe2GTy1ADK+rTvUEaaIWUnW4L6kKFzcNIrTw+Fa0T0ermzZ8wQxa4s9Ty8mGk+ieylOqLJWgPwCBVOj/o1oRL6xTrCnsBl8GGCiU4PdxDOy9m8TXHtYRmMy/BJ9IhMzcMZWq7Y5M6vJ1SE4dQ/0yedVkxcVE2HsXUxLXJDbmy39apcqlzfnQTIKzpJK+kD7iNNi8wk2Zms4Boxsm8suMTo6lKppuAWgMU0CXBw0IVtbeD9TNvNvY0P3gjdWb6B8MO0af1Hnt2xk5NEGnLeYyafc5vOmcwsuNrmY70bqu35vuOovXIj8Hi9BzzlKdRlpHG7Yfec29EG2SSk2eL1mtipaervSeYxr92+ecyjkZukWRxgg9butnMHDT2LY6dK1vqtr5oI6qjmnKRzYkXlpUNsX/aLGr3RGI37cHmBbsYhh7fVfkM6ihc624hv5L0+7DxXa8mHKIZcFXdZ0tqt2PSoWJDJDjpxpuTA4eOy88YKSdrt0RqaTXgjY6tDfNSgZUnYWm15u7TbK+VG8UiCixOxE+mmNx5nd3fpYANR0U0/hNfygp0lWsG4fcX2+E1w+CrgIk+oRI52LzWUr7Ezy+Z3BK1tTWG27mhvKxDCgORsQ1s7JzqAhQMvCZe5RhO6M1gPvhJHUmrDY0+48Ebc3bQwhOMsz4/5bTeKW/SgdHdZG9SqdyeI7tZipoyHztE8tivCUl0fDDpYmxBqSgMk9v3gQLQTuBeuvubDjjbJKy/IzLa+XiFlm6v7CTNidk2zsmHNuCnGgQ/Tu9Sn68FXgv3+3ft3y6HY28nrv/7a13K88//sJOl1IPT11Y7n6aNnuZ+euj79N2z75f272omAZa/zsybtgrcDqL85PfvwTx8ELmKm17tVXw+ZX2fXrRUsbyK/i3K3a9p6+tIU6fNVDzDD7prlvcVmebXVAd/fH6h+cwv8tpzn+eGXFtyJmrJ4qovy5SUOz42s9utl8HayCGZPYOUip/mCEvgXry4Xl9/eEgCeoh/XH9F3v/8fxJrobjMuAAA= -->
