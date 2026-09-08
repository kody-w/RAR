---
name: "rar-cowork-cookbook-demo-data-monitor-background-jobs"
description: "Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_background_jobs", "rar_sha256": "59433331b729c0f632e95abe736b8f7dc10ff0ce42d774973bd989d1a3bbade0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_background_jobs_agent.py` and in the RCI capsule.

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

Monitor background jobs Demo Data Generator — Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 59433331b729c0f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_background_jobs_agent.py` first:

```bash
python3 demo_data_monitor_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_background_jobs_agent.py   # or on stdin
python3 demo_data_monitor_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor background jobs Demo Data Generator — Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_background_jobs',
    "version": '3.0.3',
    "display_name": 'Monitor background jobs Demo Data Generator',
    "description": "Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-monitor-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '756377500cfc55f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/monitor-background-jobs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor background jobs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor background jobs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-background-jobs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor background jobs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo monitor background job records in the USMF sandbox and create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for monitor background jobs in a D365 F&SCM sandbox — never against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMonitorBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOiWLbuX/G+50NVHTJfZoQ80RFXRBEZBBkUKjuymOdBBgXr9n+/GzWH6q4+fTrifrpmZIqw95rXs9bKze9v7tAndfv26U0P3WrBu0WRJmG7cKtgsa5vdZuDrzr3wN+FX1d9m3pDX7fd24e3IOz8Nm36tK7Adj6swtbtw26BkYs2dIu061N/EYRlvfBcP4/beqiCj1ntgad+3QbdIqoBn0UHWHn1uOBwilwUYewWi7Dq035a/ByEkTsU/cLU5e0vHxZd78aAfp+E5SKtgIiLzeiHxWKWchbww8IHjPsflsw0Pzx0acN+aKtuEbp+sqjC20uIn7pF06al206LPJzegVbh6JZNEXZvn37964e3FFy/ffr9zS/cDtx644A6nNu7cl2lwAzsN8X2tTfbpHCrGCxrJmDUCvxuwhZoWYJbQJfF69fPXVhEHxb/+Z/5zW3j7pdPn6vF6/P5bf5zHKpZhUVfu10fBgvfbVwvLYBN3her4uZO3Td9gP2AT6r4/bnzO6W6Wfxlfvbzk8l7HPY/f36rm9lJwGOf335ZAPN/fmuH+fp9ptL8/Mt7Ud/C9udfvtPpBi8L/X4mBqR+//L6/SILFn5fmkaLL7q6Wb94AQunTQiI/6Df/HmK/iL3MsmX5+Kf6+bD4s8pz/r8Bcj7jDoP0P1zssAGYOfbe1an1c8vHm19DSu38sOff/lnZP0k9PM5Zv9HdH99Ek5CNwDWepkEROjsgr8uoJdu32j+c7YNCJh/RxOw/Cu7b4b6Z7Qfnv070kVagfT46ss/JfdnG6C/LH79p7r9dxs+LKLPIGmK9ArizivCT4vfHyHy60/B95s//fVvgPS/JKPXQ+s/KHwp3SqNwq7/8uXXn7rH7Z/++utPQwOiOHTLL0Nb/BnNP7Prg88fLPha9fMf9wL+ZpVX9a1afMuhxe9187/av70vLIB2wff73afFj5k4f6DFrMRXpk8T/JCNHZD1Bzv+8vY3AD0V0GbwH48BfvzHfyzk1G/rro76he7XQ78ADu7TMpyFN5K0W6QP4AMKALt2KTDsax2I/9nDs8R1tPjtf/sPXP/ov3AdnjH6SwBQ7Uv5hLUv3wH7CwDs7rf3hQEI120apxXA5+NKVT9XAIyrfmbatGEXtlcAVN7Uhx9BPn+cL2YA/u1f0v7yIPPeTL89cDp9It9xLcyo1w1F+D7rd0rC6qWND3A/HEN/AByK2gfiRCnA6w9A764urgA1Z1t0eVoUiyAFuAKYTs8aMFSfZmK//fab53bJ5+oJ0/jiWcc6GCz4Js7i40egV1SkcdJ/rkI/qRc//f63nxb/Z/Hf7XoQn3mooF68vAEk3OsHZQGyayjBMuAo4FoAHQ9v/P63l3UBGVBBF8B3aZQ+a9icBXkYfDW1vlt9xEhq4YXAxMC8ZVO3PcD+Rdq/L4Ro8U1ewHR+NFeHpO56UISbsArCyp8AVReo882SVd2DAtynXTR9WAxd+OD6m9e6DxFLkOZu/9tCXqugFtUF+GcW87EIbAYOBeb/FgjP+4BIC6oq+5XE+0KZ43HRuK3bJK374hG5T7/MLcBrOyDuzqX5czVX3XA21SM5nuaJ5/5ibigeLv04+xw0JCVAgqD7yjt+9SDBwnhUzvZz1b0C323DR8kHokyLeEiDuRz81yukuqQeiuBhPyDpTOnlheDllUcMvmr+D93MYg7gxdwTLOamYPHqgea6OmAISiz+v2iKZt1XPH/c8Ctjwy02inG0nz6ZG8LZd88ecpZulv6Rf99blq+w9BWdP1dFCgKsnf7rufLhydeaJ+INLTD8cXV80AdhBHwy031E+Ry1bTvnh/u5+loGgDaLB+YBRwNIACkzR+pXhvPTr5ImIO/n399bgpfOsz1AJC+awSuAh6IwDGYHAanaOVNf/gQhH85Ze0tSYLEftZrdA+wF6C+AECnIPVAq3r9B8/PpV9H/sPHZ+cxbHl0hiIewfRAAcoSzgLOnbmkP8Mrtn/030PPTgwhQo2z6WXcPpArQ9HkzbMPLkHZpP8Pi065hAzD54/z91HS+G44NyA5gLJADzQCs+8iaGVBK0NcAGUCggiQq0+oZti8jPAi65QwBAGJfMfSk+Lj9Uih8pNpcoL5unBWZ98w1fxEB0cGd6UekMP4sTAC9cl7x4Pv3kfaN20x7RssOIB7g+PXpszl4f9b3ZwOx+Er30z8MOD//ezPQo2KbfwyAT4uk75vuEww/q+zXIvsOsAp+yto9Cu7HuSh+fBXFj38Eg+4PhJ86f1r8e8L9gcQrOT4t0HfkHZkfSa/gen2ALdYfWfsjMT/9XB3D71AK2NcliK7ZcxOo8N/q3tcloPjFLYAosPhZB7u5fN5AxX4AP3DD5+rHaJ+zDdSVKp6js6t/QIFHAwAi/+m1b/UJPKp6wDuYG8Y4nKe0R2504dunaiiKD28ViLv/wXQ216ByDulunulA8oD+q0/Dx68HQoz9fPnHwfbwuHCLdwD0AI2K7sewe1WOuXL+kB1PJYFyPuDwYRE84BdEJFByZj5nltvlD6yflemnZpb+OcjNrd8D8L88Af8fBdL/aW0AoNeDLiPs/65K/NeiHEAbMBvTe4BG8Owr/5T5t6b0HzmfQDcwMwnqT3Nh/PDCH/ANBglQaL7OBEDl15T2mKirAQzAv87zyOyDx5b5AuwBX982ffsfBS98++ufyPU06hdQsKs/8ZIylB4INoDNj+L6tZoCYb+G6XebYOQvf6r515L55RlOf8/iWVfnejtD5CNg54UfFuF7/L74lzn9EUMw6iNCfsSI97Hoxj8R4aElQG5Q/2aDfffEd3vUj2FtlhbYr3/+38LvbyCo3Zn3K6xf3T5YDoDuYzf3ODDIfMAQ/H7mKHj2788BLwJd4oI2FFAgGQIHH9RbYoyPRBSOhQzpeuESpzw6WgY+ikQR4ocEFiyXBLPEvYChmQB1cc8DFWYW6JnqX+ZOLu0fJJcRwjBYRKAYEgCPYUQQ0BRN+eQSQ1zGc0mPZFzv+9Y8rYKXpk/NZjN+G0lmi7wU/v3Nowiwckd0wur5WcMQ6oUY7E3SGT6TTCrFva9fik0TFNQWZQcpc8dKZ7c0sQ6WAbUVp9g8OIJtTvpZY+ojt1KZjYptYN3AA3op0+uzGPRSgLcuoWmsVzb53aGXWTAS9yAZK3rtKHUqKWMgqFIfkKfUTaC9NhRGesRQ3YcE83ruig2ZLRUo6CO4rGFdP4U7ofChis/TNNYEE7u65rhaUQpb1oHYSpy5pRv1Vp6pkzPSNIQd08PZzQhLTi+ZnZ42tYUTzhYSd/Tdvx6xQ7KuaAXqLN7LT+aao48NSXO8fW0VifGboSpOK8Me+EQWnCYzVtPooLsyPUo6d7fTPAj5tRXuJQHCopYwClyqOM1Tz0uEOoBogGW1SY2EgaBdt0cYGtvEx2aTs019jLZNh+wZSmAwwRCPO6L0INm+1gNRo9vSzdcRf9v5niFrUdlUbSraZVnZG8GJ1xsnbdXKQe5hNq3gfdJZVZUE8W4dHu+ppDIZpXu6funY/bg/y5ajlUJOcTp1G5CyXvKtRXvVhNY+41TFcj9u6LXrk1KXZDGEC452z1vRVHXuHK8Th0NLUd9vD4V45ulUFxtyVwgSuTLcVTxu2DPp70fOYe+XYNfKdE86CTmlRr/h+MuSX2391C8Ieau70zG6UJmdqbd0EtWiPLErmrLZaxY5sRmEQ37e2FR9JXUSlkrZWh2tjEBox3CcZeohOcEIZ7pVS+0mrtd5n1LTxuSgXC1v08ke+t0owLJMrsm+qxHXERssSOHEdhlItfkOi6He9o+2mFQay+WJf4TvRnRGJE5crmUP99KjRlnxhe+VCz9YNncCfdGtKLDlpbJTpOLN8/oy6h7v7SyrKTVf75IorXa0VQyNvBOjnIPTY1ccBMIrN83yto6YDR+noYjrRa6kd0LZ+hmiTkkb8Q7GHrdN6Rmuv5JWS/WwZqTe4g6XZjDqfFwTslJcyH2KXC0CpcL2fu/0cxe4ua2O8b5aVmpkhzakq2OTySqdJaEqpQ1dXWUjJnJs4Ix021cnMjFE/VZZ2ZCs2klcX010QzrQoUe5JFs7KrCjHl8xehPIwqjo0cQ1ZWmYN9NT0dKQ3AtChD2y4/b3Vh9tfS/mibWy9bjpdqYd94St71yutyX+dm5JO+Wj1MnXO3+rrQT1EJRndlLprrzLhLnHPR4EKmueJBO2iNYpBfTGNHbO2adjMkinpJOQ2mlFNiY3zfYqyMV1qQZJI0k2PuEdV9Aal9a6WfenHI8gSRM3W++G2awkF2R5KzTEtqyEIUxnf5JFO4gHa4xHelmkxIQKCZ+m6EolttCmilw9zfGpDZDYh1E1LmjkdJR6UT6aN840JXvfHWr6XCqap2wHQSlrZNULwnp75xTcy2JJ3kEBmXXUCVOUMarUxoRZr9hu8o5WOSU9dQIWVD5nV5sBzeXc2p23YWnK5SpC9/GKZfH7NcoRVC2WlLga0DprKoqHeSgthhDi0zWWinKt3FOBvEn3xuFEnFOuZswVBlo4xLnlT3sPAWGGaNk6tBEB4zdT7NDbYuL645IvB33KDqIGlPWOl+taPiyFKsarvuprXWyNFTPCk1kvW9lA4Y1tueYaOQdRVJ0suOW3nHrnRNUNhaBTRt85nO7mjieb6ozb1flKXTs8Oq86SjxH8VrgmdDOjeRkFvVyyzjkWCd8X2dkICiuAdoYsm0QRd3bQ30oZBYdPNXfQFkNb1OS3ijJlusjYNbQgai17NTmuFU40crtJez6KaDtoSwCV8HatuzsfozLTSfodBjgsj0VnYlAeS5Z50u3DPu1Yeuivp54EJvkRkglBBU1LWmZChFdZLk+HepgJdd6w0D5dl+LERqSHM0qliiyXY/xXR/ZV2ua8sRceRh+86rWl2upkXPqbCJN21QMHZ3vFHMFplu755PbCuvKiY6kVW/VZaVsSjwcj1S25zqvbKuQpE36QGG2FvTKmuegYVljGAQ+y5oOlXh7vAWtR6BBaZ4OR2tNA1xjrU67raZp79I7ZYKZ06Zao3yKprG0qUlkid2imOcvl+VOZtvSS6Xzvs/4uxTXoj5Wx2xYsfSB7zfddOmqeN3uCcM6JKPmbLNcjIzaTPVGoPlcX/vYprt5/lTVuz0hXvXTrXap1oghkt6Plg67aMftOO8kSieCPg/EnW7ZHSdeIhXm95wGI52qsYK26dlgqKe0lCncRjxtizfocNYE9C44dLkji+NqohWRGSSe0Q6HVNYIx+woFU2AJrtrEMKnG4TT2+SAGLF8yG89YW03l6rBlxdadPESItic5S19XWHuBRou7S3XkBQ7atcavVn5jcPqBMfIUbLY3jzZ47FSLnGvU6ykr3M5EdvcEHwcluAQWp2mRhbTG1enxM1MAhunx8M2aUQp7e2MkeMcSxKqU8zzZnIF+xA2pGk7R/FiY4VTivSNJdjdXbNcvrEvNO76oN8YYY6tbZ0Y18UdFIWBOGr+0c1Dk9XRRiPlySJWUQIIdq6QBJ0hTT0pnxqkGYTm4rZasUrdXWVJW4nys87mNiwylj3Ku57BIK4ouPu+GNxtuNlGqhtc2WSPrawEzgmnkBSoHM1uanuZPuL4upC0lIpP93U+aJHdblelK1U7rE7RTiROh/Ho3hJ/bC0fyiMj2taAFg21G9hlgzS+IgA5Jd7GecjLUvlo4ad6z5FwJigBqbai1hO1G1UQGA1DUJq62gdwc7VD7IqJ11pmKCUsBE4nrneGivhtTflLmgq0rrToPHVrv2+WAremcM6NT06HKCuzN9j9UWnkWN8jO0pROIDJTqPj7dE+NivFrUPRL/qsYvcDrZSr4VIWN/g4ORXhO5uzF9cN7rsQ6LaFgZErNj07jUJBDlyNGLTZjaxNVZnUn3OeQw7Y2uCl3cpRGaXZZPvgFp33FFOQ9Shzx+lUcOWVObC4alYhu7m7LVdGJG8FICiSg3mT9uklJhvYWis1hxKGiLZ6KVg4FyQwzBB57BVFfA9GGWuMBCt3WIWc9b3q99zEq1WcXwbBr9Y6Rwpdm7qX1roNDrwcK3YryhB7r8ytqCWe0Vblit2UhS7WfqBvN2zo6aBLgZmlX64OycrwA3KETtUO72pL6C6DEZ2y41Qf96IKbXdoVGnbOLhdVpsg25zFcc1Wsb1blUcTyc4oOjl+Q/v38nK7WbsrfOB6vY0tXaEbrGHE1hUswujiTa6HaDLp6l6GV9py4u5iIsD3vr8NsRvcNinleQ4iY4W9UyKzOk6H0rb7SEohIRWp/cVyyoASRV0+nBjFDQcuyo2GoKOr1JPq7kjK1fXqQyM0TGSPnnIH3rVYEbddYQYdSV2wqydmyPVwzeFsLe2iYjivDUtieSExaL3ab1BsJAWqWjar08H3rb1MrWg01VNvB/RN2FqLBHZ3WsWb7Oyw9Sa3Srew4yY4UNTqtl1tsMvZ5mGq53CN4tcnW3LiXtPban33nB2WLKMWRnZM16y107KejOX2pGD1AWX2Zh2u4OF+6tSkcWBzfUSF/uy23u5wxlVuu97lsFp5+Rhd4SEanJwpgNJ9w3swJawgNeI5otZkMk/609Lhr6AbChDEi3EttSduvfVOq3SHYKxyDGNBsL38fOtU1xCVFTZOWH0bsZpljPAcMdNoX40Cgg8GqMXrXMqjap+eQHuJbkWs1k7tKeb7+0q4bE1knI7+5jJlkVvSSX7KFZzBkU1GQyp+XUID0uaY5jKS3it7b5esGhXraYyaMsIlqrovyx5n2/R0bYoEEqhyg09n2874WDUYw7xHF581LQBifTiSsq1czuK5yPJJpMyulqiqEbOi3mtV1GvRlccJU4/WajxkK8W4XzKF3AbbShJ7BvUvJn87RGvQuLvrFWRLG9nxE2l3RynB5/e+u2rpmKd2UnYgzuN6OzKZLunpDnKXazufwGhMZiM17sazyem95oIhlToYuVdYhL8f3OQ0wM04wrGrIYZSwrjX3t14jM+GAMBXE/dLk9v5Auxihy7j7TOjt1NveS7WsomtnXIuCaSsJoXG77W6rVs0NITWtvdEMQaW5Qc2HEUNpsi+L1YHyYyN/dY1KNqlZHNHNcESWVr7ST5igTe6Wx0fVAUfQEW4nMMDNkaNRE4x1p7SQus5Bm/JKF+ONnFBNxcBJiRyaSqcc3XQNU4KUK2Xhg8cZoaUc1KlvchnUBkixnC8HSSeTe1SLytZ1i43yA9iu1XMoRePmNtGHtVF+hrrUujiCqgMANHODvz90G2wrGtiGqbraLXeWl5FJ8Lxuol6qcbRwD0fB09DMJO57lVTLjQC2ePmKcbuIiVxB9zV6YsV0WyZLE+q5hmH3cpnIVC/MMVXNE7mvEPtjQTV6rrqjcflYdSVLNfvPLQLJydeHhQ9H/gSlQ8j6mwsEmeXA77OsfZ+u2K1el927ck67Sv7dOgGgpK0ts0tCpVK7OIfYgtRyHI6Nzhw7l0MSyukuAHMFSWZIGs4uBTNMF4ozhdC3M2hCMPyJcTHl/667K/Qkc96c3TNux7DOyZEdmIybqziKhHwusyHoN8rot5CCBjLOPvibuHc48wOwfC7Su2OYjzslj6zLW8S75H3NjKswDnzU391cbOXdwRFb+tjfcdI7nZK4rJlYAjqI3rLdM5+OnLhoMKjBPME29gKhQRr6Ero6WXl3DZMl3Uit1J3hnw+OUtOPEZMnWFShKjjzkgDJVufy5hVRR7U9vNgqyDiNlEJE8SNRkof20mn01EfGL91K7vBBKrfsiTdn/ZKIqjEcc14uUze8PIg3o42ftnc/IxsJ81Slq2CEQVMo92Ur0eejaTIqKKoOMlnX9d9nBayUCn6fNpwDeHnmbvx42hyhn2G6wGNVPi5upOVOgxi6vpQmJrNDiLFDHYPeSFBQ3TVRvWghXJc7vLVKOTGSEAX5E51zeGOgfpxXl9bzwxt/2xaqeJ0p+A0ZI5bDbQEmpa7mHEIW+MZta96GkqCqO77HSfd7CVKkd1969Hn7ZTsUjaNdO941HPdBpgw2nBDDvtOnsBspMlE1By9MBxE3kSVtcLsTNJEwtwWtJAv1PjOnjUwW58PHHu4xdC1X2uH3cmPDrurHjvne9ULhAa1TkVfdxlJ07QxqjAijPaYJxvIxPSTp+6z1ArOF8GycFa7LcvgnNoBgm2hE00VAibjp7t6l5hbFQcI7luqdj31+kbBt5gweLGQkRSX2NWllEkaz7w9VS8P51Nos3dxCBoH5DesMP6IIc5ZMk6DjyHIfl0dtpZD7EnFFkfTDOyzZkIqj3fS9kaOsJmdl1RdFqZ7mSD/tr8bJ8PtluhwYW2kLTlP6k/ZxYVEbMuWPN+EKbfxz5J5uLLVVcZXgoYeDSTZRacDt+li9X6EyCM/eatUTmplWfFmZPGMkUskZmlNWPsetlLkAV9mIOKu0qmDDw5qTeTlmkGk75CQmdYkQx1gvMBtMoCyo9EZ8mWJnfFg0nrUV9KCQan4KjfkXexhK7yeYp25w6jiQjUbnK+DSaFFEBYjahKtezrf5H10GxgkrNsubOQLDbkErVMESrXYxlVEdGzx23EbGLDjszbtZcvV8k7ZKlnssMBPzyxeenEQx45xmKqUs0A6BinfVTc3QzwaqyFmLRMNfZXuqzUan3UhqspkLfUu3DAbmbjuNthWVslV07NHkoEseas7AoOLuVcdfWxyrOW29nM69HWO5o+2txx1SMy8YO9JrWG3Rz4d75nflkivpPKVqZeYGHIHKKiP3Yo5qRsgXbXZCt7KE5crAzY5CGcxFb01fOgk08qMsvudvB3uIcNj26gojGHH6srVBk0xU4d4IfAW32tZO91W/ehcvabECj6MpjFvPaV02sqgq2Oa9/EdAIoTZxAu2fftxShT+85frT5j7z5lKP29UFVI21Rl2DFu3hm+o0SoGqKicHPlrLThzJlw3EvLkRHC6rq18wSutPUFVUVty94Nm7J4haH5bY+byMW7VdLtTnLHoW6ugo3b2LU/kc4An5A7UvvIHh43x4AZc8gKem7ZI17IZEQ75QBWO0rg9kq73wpLxDxAgn7SQsUlouW9JW8R5bssDOaYKvbCWG62FLZPl0ymtMYFt87BtcfF8IIMxjRw7YRdlssGgJd1vWBUvRNVGz1b2U4+WzzmUzffV4UNd0rXTEiATgxW9v3Nh/qttyNjZCCXiCq5GWqG+2sc6CdBQhA2kctDRt1HMnQ5hQlyAz/UNzZDYnvPekswBK8Dm9wLUulEUrCqWa6fPJWhc2wZusz1WjtOdXNG1od2HsnLNOqgEEqtIlRD+m0nWxqTpjSHnnsMUrsL1Q77lpwMqNtq57OJ7SA8qJfwaSJ2y0gtVDK32CJC2xVGweqQBfSaHdRYu93DfdIvHUlK5Et2uZS9l+w7GBZqr4Oh88ZEe5i7MxfSaA+uoonX/f16D4dgINAatmjs1iYcLMdomxOQczzcj/USQe7KLdu22DU95ApoamCTsZZsAdfUTYeOrZavhTVVmHCm5Nuztjqq1nGXj2GO4keCHsSkJQqklUJjAwYgj25yActJgaeqmjhsWchc6Zh9P1xD7UCa1pJRgaQYtrnAPQ47V9QR+R10cEPfDTx8c7372zUZM2B2uMC4JByW2uBwG56E9sTpkvLFTtsihyFSmWFwEjoKoxVJ8+SK8IE815jaXA+lbkqsw7vRtMvlw/I8urIqdEfU8NReCg/slZYUZ8BPIcquVqu/vH14mw/AXueu//OXvOZjm/9np0fPg56vL3I8jhhDN/j04PXp35Dprx/eWj8FEj3PyLpiiF8HSn93QvbxXx7yzdun55tTX8+TnyfUvRvPrxS/pVUwdH07fenq4vEiB9jhDd38FmI3v6jqg+8fT0m/qQGu3eD5KkbYfunrL8/TwfBtflNwfksjDNLvP+PXwSEgMAEnpX73BafIL2HbzNq+XgcASuLvyDv+9rf/C7cCovIHLgAA -->
