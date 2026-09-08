---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-store-devices"
description: "Generates a read-only Adaptive Card JSON file summarizing store device configuration and management status from Dynamics 365 F&SCM, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_store_devices", "rar_sha256": "e15b9705f5d4a3c1d81e982fb280f76bffc14095eced34c41c9309e5e7645aeb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
