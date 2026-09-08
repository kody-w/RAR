---
name: "rar-cowork-cookbook-ppt-exec-manage-file-storage"
description: "Builds a read-only executive PowerPoint deck on manage file storage from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_file_storage", "rar_sha256": "9266489f344cb21e2d7d4d434e41a8b84bd8da353515c79f5e9306cc5ebbecae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_file_storage_agent.py` and in the RCI capsule.

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

Manage file storage Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on manage file storage from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-file-storage
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
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-manage-file-storage-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and cadence for the review, e.g. monthly with prior-period comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 9266489f344cb21e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_file_storage_agent.py` first:

```bash
python3 ppt_exec_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_file_storage_agent.py   # or on stdin
python3 ppt_exec_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage file storage Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on manage file storage from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_file_storage',
    "version": '3.0.3',
    "display_name": 'Manage file storage Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on manage file storage from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63998d8a11492f76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-file-storage'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-manage-file-storage-2026-05-24.pptx.', 'review_period': 'Reporting period and cadence for the review, e.g. monthly with prior-period comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage file storage reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage file storage for a 15-minute monthly review. Produce 'ppt-exec-manage-file-storage-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage file storage data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on manage file storage from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build me the executive PowerPoint deck on manage file storage for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-manage-file-storage-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and cadence for the review, e.g. monthly with prior-period comparison.', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready manage file storage deck for a short monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageFileStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageFileStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-manage-file-storage-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and cadence for the review, e.g. monthly with prior-period comparison.', 'type': 'string'}},
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
    print(PptExecManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
