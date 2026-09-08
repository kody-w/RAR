---
name: "rar-cowork-cookbook-ppt-exec-track-and-analyze-software-licenses"
description: "Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses", "rar_sha256": "4b49e6ce9bb4bcd28c422ca40a48c1eadef31aee761fe507b1de4b53b5a1283d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_track_and_analyze_software_licenses_agent.py` and in the RCI capsule.

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

Track and analyze software licenses Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses
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
      "description": "Prior period to compare trends against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull license data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 4b49e6ce9bb4bcd2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_track_and_analyze_software_licenses_agent.py` first:

```bash
python3 ppt_exec_track_and_analyze_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_track_and_analyze_software_licenses_agent.py   # or on stdin
python3 ppt_exec_track_and_analyze_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track and analyze software licenses Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses',
    "version": '3.0.3',
    "display_name": 'Track and analyze software licenses Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-track-and-analyze-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd105d5a4f6a4a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/track-and-analyze-software-licenses'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-track-and-analyze-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare trends against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull license data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for track and analyze software licenses reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on track and analyze software licenses for a 15-minute monthly review. Produce 'ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track and analyze software licenses data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Make me an exec PowerPoint on software license status from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull license data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare trends against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready software license status deck for a short monthly review, sourced from Dynamics 365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecTrackAndAnalyzeSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTrackAndAnalyzeSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare trends against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull license data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecTrackAndAnalyzeSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
