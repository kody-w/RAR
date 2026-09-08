---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-offline-mode-for-apps"
description: "Builds a read-only executive PowerPoint deck on offline mode configuration status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_offline_mode_for_apps", "rar_sha256": "92d63a019de31b34e1a03f703bc5efc47a3e943b830953d942ff38ce13def816", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
