---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-file-storage"
description: "Builds a read-only executive PowerPoint deck on configure-and-manage-file-storage status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_file_storage", "rar_sha256": "b35dd17322ecc9720724cf4433c94801a332287d2625a5c332662d0aae860970", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_file_storage_agent.py` and in the RCI capsule.

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

Configure and manage file storage Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-file-storage status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-file-storage
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-file-storage-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart, e.g. monthly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 b35dd17322ecc972…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_file_storage_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_file_storage_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage file storage Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-file-storage status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_file_storage',
    "version": '3.0.3',
    "display_name": 'Configure and manage file storage Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on configure-and-manage-file-storage status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b39ec2eedbd4025b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/configure-and-manage-file-storage'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-file-storage-2026-05-24.pptx.', 'review_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'review_period': 'Reporting period and comparison prior period for the trend chart, e.g. monthly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for configure and manage file storage reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on configure and manage file storage for a 15-minute monthly review. Produce 'ppt-exec-configure-and-manage-file-storage-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage file storage data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on configure-and-manage-file-storage status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on file storage config status for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-file-storage-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart, e.g. monthly.', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on file storage configuration status from D365 F&SCM for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfigureAndManageFileStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageFileStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-file-storage-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart, e.g. monthly.', 'type': 'string'}},
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
    print(PptExecConfigureAndManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
