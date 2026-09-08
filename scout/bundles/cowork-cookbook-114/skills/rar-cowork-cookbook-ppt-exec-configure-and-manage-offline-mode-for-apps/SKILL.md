---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-offline-mode-for-apps"
description: "Builds a read-only executive PowerPoint deck on offline mode configuration status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps", "rar_sha256": "92d63a019de31b34e1a03f703bc5efc47a3e943b830953d942ff38ce13def816", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` and in the RCI capsule.

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

Configure and manage offline mode for apps Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on offline mode configuration status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-offline-mode-for-apps
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-configure-and-manage-offline-mode-for-apps-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is sized for, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Deck subject, e.g. configure and manage offline mode for apps.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` and embedded as the fenced Python below (sha256 92d63a019de31b34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_offline_mode_for_apps_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage offline mode for apps Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on offline mode configuration status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-offline-mode-for-apps
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps',
    "version": '3.0.3',
    "display_name": 'Configure and manage offline mode for apps Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on offline mode configuration status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-offline-mode-for-apps',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-offline-mode-for-apps',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d187b1efbcdacfa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-offline-mode-for-apps'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-offline-mode-for-apps', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-configure-and-manage-offline-mode-for-apps-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is sized for, e.g. 15-minute monthly review.', 'topic': 'Deck subject, e.g. configure and manage offline mode for apps.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for configure and manage offline mode for apps reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on configure and manage offline mode for apps for a 15-minute monthly review. Produce 'ppt-exec-configure-and-manage-offline-mode-for-apps-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage offline mode for apps data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on offline mode configuration status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on offline mode for apps from D365 USMF, with KPIs, trend vs prior period, and speaker notes.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Deck subject, e.g. configure and manage offline mode for apps.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-configure-and-manage-offline-mode-for-apps-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx summarizing offline mode for apps status from D365 ERP data for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfigureAndManageOfflineModeForApps(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageOfflineModeForApps'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-configure-and-manage-offline-mode-for-apps-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Deck subject, e.g. configure and manage offline mode for apps.', 'type': 'string'}},
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
    print(PptExecConfigureAndManageOfflineModeForApps().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
