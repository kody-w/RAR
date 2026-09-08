---
name: "rar-cowork-cookbook-adaptive-card-delete-users"
description: "Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_delete_users", "rar_sha256": "f165c84a477beb36ef8f3fa16d7d59fdab88b6e93af48ca77c79a54294fd1920", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_delete_users`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_delete_users_agent.py` and in the RCI capsule.

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

Delete users Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-delete-users
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
      "description": "Date stamp used in the card header/timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against (recipe default: USMF).",
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
    "output_file_name": {
      "description": "File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_delete_users_agent.py` and embedded as the fenced Python below (sha256 f165c84a477beb36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_delete_users_agent.py` first:

```bash
python3 adaptive_card_delete_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_delete_users_agent.py   # or on stdin
python3 adaptive_card_delete_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Delete users Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-delete-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_delete_users',
    "version": '3.0.2',
    "display_name": 'Delete users Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.',
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
        "upstream_slug": 'adaptive-card-delete-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-delete-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40dad3c2053ec79a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/delete-users'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-delete-users', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date stamp used in the card header/timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (recipe default: USMF).', 'output_file_name': 'File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical delete users status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-delete-users-2026-05-24-card.json' that visualizes the current state of delete users. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current delete users KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing delete users status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call for a dashboard/Teams-ready card.', 'example_request': 'Make an Adaptive Card JSON of delete users status for USMF as of 2026-05-24, read-only.', 'inputs': [{'description': 'D365 legal entity to report against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date stamp used in the card header/timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a shareable Adaptive Card snapshot of delete users status from D365 ERP for Teams, Outlook, or dashboards, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDeleteUsers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeleteUsers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date stamp used in the card header/timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'File name for the generated card JSON, e.g. adaptive-card-delete-users-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDeleteUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
