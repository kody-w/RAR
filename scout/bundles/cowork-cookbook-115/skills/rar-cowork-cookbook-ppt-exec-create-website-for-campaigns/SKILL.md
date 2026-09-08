---
name: "rar-cowork-cookbook-ppt-exec-create-website-for-campaigns"
description: "Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_website_for_campaigns", "rar_sha256": "1112e8739102fd6f2d44d22ea608b9fc1c0ce591a33d6d7d19f49ca18e13cd9f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_website_for_campaigns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_website_for_campaigns_agent.py` and in the RCI capsule.

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

Create website for campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 1112e8739102fd6f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_website_for_campaigns_agent.py` first:

```bash
python3 ppt_exec_create_website_for_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_website_for_campaigns_agent.py   # or on stdin
python3 ppt_exec_create_website_for_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create website for campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_website_for_campaigns',
    "version": '3.0.3',
    "display_name": 'Create website for campaigns Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-create-website-for-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-website-for-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bed3c9ec9d52d1c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-website-for-campaigns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-create-website-for-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.', 'review_period': 'Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for create website for campaigns reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on create website for campaigns for a 15-minute monthly review. Produce 'ppt-exec-create-website-for-campaigns-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create website for campaigns data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on campaign-website status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on create website for campaigns from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on create-website-for-campaigns status sourced from Dynamics 365 F&SCM, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCreateWebsiteForCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateWebsiteForCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-website-for-campaigns-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior-period comparison basis for the trend chart (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecCreateWebsiteForCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
