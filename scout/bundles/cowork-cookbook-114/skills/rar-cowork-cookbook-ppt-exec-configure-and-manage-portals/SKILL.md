---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-portals"
description: "Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_portals", "rar_sha256": "c769e2a829f0c376baeeb44b4dc75029413cecda69988e69e44020d0a096f4c0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_portals`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_portals_agent.py` and in the RCI capsule.

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

Configure and manage portals Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals
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
    "comparison_period": {
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject area for the deck, e.g. configure and manage portals.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 c769e2a829f0c376…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_portals_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_portals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_portals_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_portals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage portals Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_portals',
    "version": '3.0.3',
    "display_name": 'Configure and manage portals Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-portals',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec3c5215d53ce730',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-portals'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-portals', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': 'Subject area for the deck, e.g. configure and manage portals.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for configure and manage portals reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on configure and manage portals for a 15-minute monthly review. Produce 'ppt-exec-configure-and-manage-portals-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage portals data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on configure and manage portals from D365 USMF, with charts and speaker notes.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject area for the deck, e.g. configure and manage portals.', 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready .pptx summarizing configure and manage portals status from D365 ERP data for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfigureAndManagePortals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManagePortals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject area for the deck, e.g. configure and manage portals.', 'type': 'string'}},
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
    print(PptExecConfigureAndManagePortals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
