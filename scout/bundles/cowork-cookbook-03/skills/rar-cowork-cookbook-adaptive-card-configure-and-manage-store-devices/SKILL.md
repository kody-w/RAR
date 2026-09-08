---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-store-devices"
description: "Generates a read-only Adaptive Card JSON file summarizing store device configuration and management status from Dynamics 365 F&SCM, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_store_devices", "rar_sha256": "e15b9705f5d4a3c1d81e982fb280f76bffc14095eced34c41c9309e5e7645aeb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_store_devices`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_store_devices_agent.py` and in the RCI capsule.

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

Configure and manage store devices Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing store device configuration and management status from Dynamics 365 F&SCM, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-store-devices
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
    "action_buttons": {
      "description": "Which 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and file naming.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-store-devices-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_store_devices_agent.py` and embedded as the fenced Python below (sha256 e15b9705f5d4a3c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_store_devices_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_store_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_store_devices_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_store_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage store devices Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing store device configuration and management status from Dynamics 365 F&SCM, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-store-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_store_devices',
    "version": '3.0.2',
    "display_name": 'Configure and manage store devices Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing store device configuration and management status from Dynamics 365 F&SCM, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-configure-and-manage-store-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-store-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a8c0eb7d35c7de5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-store-devices'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-store-devices', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'Which 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-store-devices-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical configure and manage store devices status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-configure-and-manage-store-devices-2026-05-24-card.json' that visualizes the current state of configure and manage store devices. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current configure and manage store devices KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing store device configuration and management status from Dynamics 365 F&SCM, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing store device status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-store-devices-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'Which 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of store device status from D365 ERP data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConfigureAndManageStoreDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageStoreDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'Which 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-store-devices-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConfigureAndManageStoreDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
