---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-file-storage"
description: "Builds a read-only executive PowerPoint deck on configure-and-manage-file-storage status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_file_storage", "rar_sha256": "b35dd17322ecc9720724cf4433c94801a332287d2625a5c332662d0aae860970", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
