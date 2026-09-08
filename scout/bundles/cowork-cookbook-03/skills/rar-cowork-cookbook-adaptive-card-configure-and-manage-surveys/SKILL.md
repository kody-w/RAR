---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-surveys"
description: "Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_surveys", "rar_sha256": "4f0c46e7b43383e5913bac153c2a24d98f3a9976a25a839ccfbe918f7bbf1865", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
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
    "as_of_date": {
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 4f0c46e7b43383e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_surveys_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_surveys_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_surveys',
    "version": '3.0.2',
    "display_name": 'Configure and manage surveys Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a61968433387527c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical configure and manage surveys status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-configure-and-manage-surveys-2026-05-24-card.json' that visualizes the current state of configure and manage surveys. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current configure and manage surveys KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON for configure and manage surveys status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of configure and manage surveys status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConfigureAndManageSurveys(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageSurveys'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
