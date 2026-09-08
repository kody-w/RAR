---
name: "rar-cowork-cookbook-adaptive-card-manage-service-truck-inventory"
description: "Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_service_truck_inventory", "rar_sha256": "471a33b59b31fc0f632b63965f3069633fc3e7a29a9f5395d63498961a7b6291", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_service_truck_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_service_truck_inventory_agent.py` and in the RCI capsule.

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

Manage service truck inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
      "type": "string"
    },
    "as_of_timestamp": {
      "description": "Timestamp shown in the card header.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 471a33b59b31fc0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_service_truck_inventory_agent.py` first:

```bash
python3 adaptive_card_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_service_truck_inventory_agent.py   # or on stdin
python3 adaptive_card_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_service_truck_inventory',
    "version": '3.0.2',
    "display_name": 'Manage service truck inventory Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51fc379efbca01de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'as_of_timestamp': 'Timestamp shown in the card header.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage service truck inventory status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-service-truck-inventory-2026-05-24-card.json' that visualizes the current state of manage service truck inventory. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage service truck inventory KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable', 'example_request': 'Make an Adaptive Card JSON showing service truck inventory status from D365 USMF, with 4 KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}, {'description': 'Timestamp shown in the card header.', 'name': 'as_of_timestamp'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want a Teams/Outlook-renderable Adaptive Card snapshot of service truck inventory status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageServiceTruckInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageServiceTruckInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'as_of_timestamp': {'description': 'Timestamp shown in the card header.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOb1rbnV1GfV9VxHvYRM8KvblWDBEgIkAAxKb7lMIPEJGaUznfvjXSOE9/r+16nu/9q2YkE7L3m9VtrefPbi9u1SVm/fH7RQ7dYCG6WpUlYL9wiWKzLoayv4Ku8euC/hV8WbZ16XVvWzcvHlyBs/Dqt2rQswHYhLMLabcNm4S7q0A0+lUU2LZjABQv6cLF262Ah6gdlEaVZuGi6PHfr9J4W8aIJ6z71w0Vbd/51kRZ9WAAO06Jp3bZrFlFd5ovNVLh56jcLjCQW/H/X1/LiQxbGbrYAi9N2Whi6zP/8cTGkbbJIAPuw/rjYH3eLFnBrPi40RljU5fDxoZfrzzIvgCJtWTSvQLYsWwxJWCymslsUYQiWFIsw98IgcL0sBLqGo5tXgNLL51/+/vElBb9fPv/24mduA269vGs5Kym7hRuH+lOn06zS7l0jQCdzixhsqCZg9AJcV2EdlXUObgVhtHi7+tCEWfRx8e//fh3cOm5+/vylWLx9vrzMf7SuWLQJsFjpNi2Q1ncr10szYIfXBZMN7tQAF7RdXczOaIDPivj1ufMPSmW1+Nv87MOTyWscth++vJTV7ERgnS8vPy/KGvCru/n360yl+vDza1YOYf3h5z/oNJ13Cf12Jgakfv36dv1GFiz8Y2kaLb7qR279xqsO/bQKAfE/6Td/nqK/kXszydfn4g9l9XHxY8qzPn8D8j6j0gN0f0wW2ADsfHm9lGnx4Y1HXQIPuYUffvj5X5H1k9C/ZmnT/m/R/eVJ+BmIH95MAsJzdsHfF9Cbbt9o/mu2FQiYv6IJWP7O7puh/hXth2f/gXSWFiCD3335Q3I/2gD9bfHLv9TtP9vwcRF9edmEGUieek61z4vfHiHyy0/BHzd/+vvvgPR/SUYvu9p/UPiau0UahU379esvPzWP2z/9/ZefugpEcejmX7s6+xHNH9n1wec7C76t+vD9XsDfKK5FORSLbzm0+K2s/lv9++vCdLM0+ON+83nx50ycP9BiVuKd6dMEf8rGBsj6Jzv+/PI7AKGimRHz8Rjgx7/920JO/bpsyqhd6H7ZtQvg4DbNw1n4U5I2C/B3Ro06BHZtUmDYt3Ug/mcPzxKX0eLX/+E/cP+T/4b7S/cN3r76AN9m2wKA+/qG2l8fqP31G2r/+ro4AR5lncZpAeBZY47HL/OGop35V3U4bwSY5U1t+Amk9qf5B0D9xa9/hc3XB8XXavr1gejpEw+19W7GwqbLwtdZa2vG9KeO/ozoY+h3gFlW+kCy6FkZgEBlBgpUO1uouaagFAQpQJtHCZppAyt+non9+uuvntskX4oneGOLZ/VrlmDBN3EWnz4BFaMsjZP2SxH6Sbn46bfff1r8z8V/tutBfOZxBPXkzUdAwke5BDnX5WAZcB9wOACUh49++/3N0IAMqLsL4NE0SsPnZhCz1zB4t7q+ZT6hBLnwQmBtYOm8Kut2rrtp+7rYRYtv8gKm86O5ZiRl0y6CsAqLICz8CVB1gTrfLFmU7aIBgdlE08dF14QPrr96tfsQMQfJ77a/LuT1EVSoMgP/m8V8LAKbyyIF5v8WE8/7gEj9U7Ng30m8LpQ5SheVW7tVUrtvPCL36RdQmd63A+IuqNnDl2KuyuFsqkfKPM0Tz11J6r+59NOj9/BL0HsUQfPOO37rXILF6VFP6y9F85YObj27wgflATCNuzSYi8R/vIVUk5RdFjzsBySdKb15IXjzyiMGn/3Av2xy9GeT832f9KVDYQRf/H/cUs2WYQRB4wTmxG0WnHLSnKfH5iZz9uyzL53lAGH7zM4/2px3KHtH9C9FloLwq6f/eK58GORtzRMluxqIoDHagz4IMuCxme4jB+aYrus5e9wvxXvpAHotHjgJ1AKAARJqjuN3hvPTd0kTgArz9R9txCNm6lnlOQsXVedlIAYjYAXPBf5ok9mb714GCRHOOT0kqZ98p9XsCOA0QH8BhEhBZoLy8voNzp9P30X/buOzW5q3PDrJDqRx/SAA5AhnAWefzY4F4rXPnh7o+flBBKiRV+2suwcSCWj6vBnW4a1Lm7Sdff+0a1gB8P40fz81ne+GYwVyBxgLZEjVAes+cmqOyRxEEJABwApIsTwtQG8AjPJmhAdBN58BAgTOW/P6pPi4/aZQ+EjEuai9b5wVmffMQfWMa7eY/owjpx+FCaCXzysefP8x0r5xm2nPWNoAPAQc358+G4rXZ0/wbDoW73Q//9PQ9OGvzVWPKm98HwCfF0nbVs3n5fJZmd8L8ytAsuVT1uZbkf40V89Pz+r56Q0HPj1w4NM3HPiOx1P9z4u/Jud3JN7y5PMCeYVf4fmR9BZnbx9glvUn1vmEz0+/FFr4B+YC9mUOAm124gS6gm8F8n0JqJJxDXAJLH4WzGauszO2PCoE8MiX4s+BPyceKEBFPAdqU/4JEB6dAkiCpwO/FTLwqGgB72DuN+PwdR7TZvGb8OVz0WXZxxcAlOFfGvPmspXPcd7MYyLIKNDItWn4uHpC5dcnVH4FlaRo59vfT9PbcgAJAyL5e2CdISgt/KwDqfQB/YT9PAvbTtUs3XPOmztDt/laRl/nLAF4n1f/TP30/miuYaBjTd+LMzDdE+l/SPcBeOMPpD08frjZ62ITAnDNmj9n0VuZnNuEPyX701HAQT6wzcdF8ChzIMGAo2azzUDhNiDzQNL9UJZrlf6XtvtWrL4zG/aJAFUtdAHYPkqb39X1DOO9m3XPGAGhNJe0GlS3H/J+VMmvzyr5z+w3cz39rpAC7rcOABfg+hq/PurqD+l+a/f/magFOqqZTlB+npuLj28oDb7BiPZx8W3aApZ8m39nDmHR5S+ff5knvTkoH1vmH2AP+Pq26du/5Xjhy99/JNcDyr/OOfTMhH+UTpkhGpSw2bH/qj0BwgMBgs4P38zwVwDrEwqj5CeY+ITij+WvlwZ0eP9sQyDso0yBYj/r/YdB/1CrfEyzs1rADO3zH19+ewHJCuRp3bd0fRuHwHKA6p+aud1bAmwDDMH1E4XAs/+rQemNVpO4oDkHxHAKcTHMI2gPQyIfjkgM9UiMJokIg0maxLDIx0LKRWmXjgiMJgISw+kVTSIu5ZEojQB6T1z7Ove36SzfLBwwCzBmGP7xGNwK3hR7KjJb7dtc9kCop36/vXgkPucT3uyY52e9pBEgleRNog3dyajU3Jt13rnc8ejgFtz17cq1JKhVonUmXmndGEqRLbkCXTPq4HLMVCKiuU3FY76OxAAmsHhgdnotFuf74bw3IJGVqmNxJ20KmUjSLkJcQB2A31W7HjpT13jLPGmJuakq4y7VSrqH77tmP6HhaPHh7dpUl0ZO+WK5JOkl5xLFfpdOGX/jyjObHJv76Rw0Hk1BBRWg+4qr1r1SdYOxpTUSIL/RgqlHn6aLnY4n/6CktYbTUr/FW2tZjOSSdxWubkTOkZhbC+0pmAr7MVHGyr8hlqAQlnHnqDu04nTTgkdlXHUTspf2dapeTtZO026eaEj723TnpTam/CtnBnXuVK1ZZoYej2ISDM2ZnbYprB7Yhg77O0FAUX1G/cbGO4tqiGMf2QKapdIeTiQppZgbgmSsvZ7uaqXVlWEYRMevxUiVMbiU60IM1JT0VHdnaWbSFETKSgxMaaLMTbeagdLoeKqS1W3NmuKt3dvUUKleXPJMRjRMdmrPOjmKFFfpA+zphVjGvQyMTh7suob4aRtesWg17TcXWTbklL5mrAVjdsoQtJEaZ95R47XE7csSIbUdkpNuZYpXHU5ELeyt6BqzBnsu1/d1rPcTofcYi+9G9EzjRJH1p0aS9qKBqpO9S2+JesOhLFY1sa7WmU5MTDPBImsFl/gi5MwSRkL45tiOmw9apKh8L231PDOvzV45CgZkW1NBiyGmM8usQkZBdHTDtMxQdZPCchOpaWSlZhw/5VML9KSleeDHUWoLp+MEIQ2kva7B2aFil4HWac4+kdThcEJjfWUsL5OzlzknqszL0Jf8bmg3XI5Ixh5WapXhyclFIkS/qqQR5jzfNfKNyrHDrdvrnISq1X3SIKG8N9oYVIbJL9OTrd+HfkwDvb3g7nJdIAmzMsLhsPOUZLBCflse8wBFlftKJ6WtTB/ut30oiFdimWnt5TpdDrcLfKyX/MZRT/dQlsxjveIVFBKKdiXD2V05F3h/wD1+P0gX7mQvm+OSCfDVENTm0lmmBw2H+jtFngL8cEq1/dBGso4GnsXaldS1FrPellcpq07EpOLi0Oo35qil8gViA2iZWytHbuKNOrp8SUBmCG9a2cxd+yDkxBGdBEnBbpvG1SozvikmmouVddzVZsIWIxGHGsPdO2GjbgYTGY5usg8vinoX8iHv10dlNXWD7/hROErD1r3eVlubqIONhui30uQINmVuB2dYl7kjG1xr7YWsis19wFPsnoMCmb5UkXzFmHPX6Kvd7mRUrqu12fJqsqOFOeixapXi2GAG1g+jLdTHYzLdlD1yCZSWPQ85QxS7S1K2+92OL7eDPOwiKD/HxpJENrt1mDGeynqcnG6pkvRvorE2GmeXY0ffRATJBkjlMHg8XjkDKvje2pVjpIYp3Pmun/dGdCOY9Mwzt0ndMb4w3Xhu6TOMB6tdxVRVCI9Y1opexvVcfNFYk6QKREIKCF5L1v7CtWTQJf2480n0WKQljnKqe48vobnNGcxvmljyJT8qujV+wgfBtHLRM9ZSDDcXP/EpSmb28HRdyXXJkCaTJZ2bGtdMHk5ch0gSXIeH6Y4rBL66CLxQ+UN0uJfV/oSdmvsxW4+ceZJyJ6JwYqiDdCrPqGaKm9PAp2N/KqRpbWt6bV1CYmBXEilQyBLSLWVPmcxheVjHMIttrdLBZJu/l6GxghFeQlw1qRgy9wHUwyW+Lfw4GY4XfkQnM23E+uIst6sQ5/mRS/thteMYmkzicyvAFxm9GarVUDkd2cc8X57Uc2ZMGnfOz5uToVxAe6vIiV5yMAwV1yNmWK0XNhvTZQzupq4latcYmoaGA7e7Yk13pWMczX1dktccP6Y01Mlq1py9vCtWFzRONFmhN0RDblEecRueRJoNi/gWW0IHa3keWi6dRo3PdC5YhtvjatViAE73sdo5ZzrOkWjMAPwLQkHtYBQaNZDU28P6vtndo3AJcxvWWrlBuxGEzb4ckVVfwtFydaanzrmsWWS53fR1K+5XgldRxM1SJabR2LZUefxwNnMhEfV9Z+mjaa41dmrjpbQONANFfabOvXQbiGivZIao2lq8Sfqr3CcDfhMQjYFYRzuufVHJ9+sdp6lnfpNf1/yRsi5nBLa2ocClGimv8d2ytzu3gbpGoQlytJobxmhnPuFRVOju20xJ/aWL6yjaFfeGv59uI5kfY1pVeQVwrNaiCnAJKx3Vws7nJmV1dUhA2vY9YYXuWk5FCHQDJC/y/OVmcCHDsepWbFcDSiWBfPJPvtqImnqHcmXkHSC8isoVwOPrsNf4o1TuMtK4kwo9XB3pWl91pQl4OjFX59014NfpGN6MvQ0PieUKm3gc6owTDJJDdLCV6fY5A+oBacRcLeVqnkHbENlcO21SxGSCb5qOr9X+upuII1+L8iW9GJf1vsSsLCFARCrwhFjr+zGHa2FvpvrBVkZUhIe4ZGl1PLtN25BLy/KlgfWXPFM5ejk22arupnDabq4X6ciG3J2ksS5Xb936eK9vINauTm8ptWevuv2K2qNpGeQTsTmdVlblVPypOl8YJz6kMkGUJKyp5sXWhBuHhrxr4qcSCuHzgV2ymsjuOswyh2yVIVbflMygQxKTGSfjvt+jHOogamxOpLG7KnBtsruLgSGn7sJoAqwO8u0yeumd1mBlJZTCFC+ppsfUk+yz9Lh35ZV3KZuw251kvUM5kaBDhOdzqDBhv8FlRpZWExpFvIxuYy0mprqB6GbfqqPnqZGOGHu92VYJEW0JAj9TDQq6mfzgm0raKgHTschk44pQe0fHbIdB90+dvdvFreHGp3HF31AALbfB5ixfs/aHdbJ3cSrOvX5Dx9IttQTc4Zurs3UurjXABpGddAe6cdodDegMIDanpt5ephQQDGHSDJZzdbXrZU0rybYWdWg3Nt1ps9rFbH0+nJq+hFryut6nwuDkIXLu7ptzSlL4Wo5vLGcJ6wzSZTrpvVg+tYGx2je4h1fQcrnlkczw/IvqnVRIjgsRNgISNNSmNNTqKrlC+FmUtOgKTWpYCbi9xgCi1hUGLe/Xy12Gshua7XQ/VdDYsK7rdcufrwxcJyGeVNjOQK7rXTs4q72oRjZjAm+ztxtc7TH6hDn8xj15p9IUTyfS1K453243sH+syjsz8YcmtZjIikEMecXBjTp9NZgXMaF2PKfetyDSAUBPTqQcZBqh6QQvG1u8BS1dEUzF7YgYSZx2dZZrR1vJzm4lplIeJ7Ab85dkqirSvQkQvFdNuytT8455t6GvkQYPTxp0YTrfz2CYupW3NXPkptP6dlLk431vG8Iqg8fApWLP0DM2SCELNWhyqwxMhiwJ+2B61El0Y2onxJfCPe6o+ALjCordDaVhif1m7Ha3qxjFROjbMO4ctj3RQOFmpCEGPhLYXa/um97fsUpMNNwIZjJP3aOlV+/OJKeiJDR23Rna0frtNsAsx7DsRSaZaxpvcSUW4TYX5fVVNveenQ53qaQddSed9x2LmlWg8hzRe9A9Ryt/JyTnPXvNTuKhFc1GHS5OqhPrOnQpa2nrMFrfVckaziKmGVlsHtkjLcR2h+e8NckYhOWXMZeCaM11GL7lViOal6K3uvSnTcXfaiV0+T2EjymFhEijnve1lW6q4r5ahx5Fb7jx2mU3f3vnx+5ahKHeeewRswirL5KLLLC54d/2hmihPnLbYJzKiGw9wI58su+mFpcEc9taIAkK3R4TC/PVzaXDkVWD+xZfX3ewFLMVs2VJA5L0UxjcuoMrcHkG1y4fuYwmH/TWrFmfETDBtffZpiuJsxdk950uVR0RC74XEksJkc0OHhPG51QhrFreOLheHW5MbOenNl3lprrVXPS2aw78spSmmrAFIy1w2F6OylLZXtEbvxPPgxPK5P1UJPVRwIpIcu/OpnSPA5ucBNBkHhjothsVcw1VkhmmoIRyxRWDlNtUcx3ZNKNAEYjKsHLi4PgY1MH1fMzve8nocGZlxkfy3LnnXAiytSzErSyd0nQnWYJtkPdekQAMHUlF3cqwcuoCTaEgoe2dREGHwZ/ZG/rtMLTQlt85aSLMFTwQrI2AjzS9ggtxIgL/TlVpo5T0IR87osSPeBXveqrW9bUL4YfJpi2n3cTNuetoaUtEBBF0vokdgqmdaLw4Y8YVWkrRsZOwk5DUTYUa0M4d2JGprwgRiXPvMqyu3fEEHSYE2xSMCYNOSY2ay3p5PnHDEs+koF1vSsWHbutrVfgoPbBo47mlidw9OSXyoeEvnGNIjcRlyeSLMoGKTsjvr55jo1sVVuyUxU/BjrnaZinkXnf1r0GrqjFK4Gp+k/PblO/IHTwK1cSOBnBVUIj8DbtclMvWDTi6OaxOwzHjxvs522NKeGf7Ng0wW3XPGzLCeg+1tYrOcvd4tpMjX4YbFUYdEnGlMYHXCNqCRnBFjVSkxJB3p5uWCFCvbiXn3kRCd8Ahya6rrDSbrXM0KbI8qbntCV3v5NAklwlx5l2fWm4q+3AcUMve9AItLJ1V5NbktOKrkUq7QVxdoMvRPm8wXzk0IAihmyJt1H0oL4fr2DsBjnlRVS6HYp8RjCQTeaCUCHpGq/JMcFM4kgftmBwueZ6AMQQizaDc4BZNlFpPqn4l98PJgY5oe6Ryblm6eIYNLjOuUGfrspZwWZ2h9YQrQW2z3mUaqKhbLiG0hxjf1rH95B+PiA2J0e5+cXDB9VZJYDveVr/oLLsLibXfcMSqGx1k54RnioKH851f7f3GJLa2G6reEmv39DBukzo94vpB3bIyGSqUI2JYXmJ8nWc3N/dkmj93nn/w2vJ4GPjIkFdtRls+7t23HLCQJ4Oae6OopX7iJ08r4IJs6H7iNhMr2ClwZBCcwzBfncYIwzcjxFcKjIJBMQ6vFy3kjXhVlPU9PC9hKhJYMkDIFZLZ9ubUkKaikWgS+bUO6WlPrKB668ny0afKTsbFq7qrr4Ov9P2Wt4P8vFLhibMFtKXVuC5DB8zuJd3QLoJE4somk7zgD2x1CkpPDmXvsNzWx52Z9dvdsFsqlHjFeAQSV6RRjBsTHbmbDrrXjXPBcfkIbwqz2Jo6z5aCL8OIjPV1mvNKrZuh47KmvEWKY3io9/kgXtGSQ1ZYEA9Bs7OhcrhucqTY3hOKq8iMxgXdhPsbeYZqdliFx16jMWyIM35VUile9bGY0qmD09GZTBUzQDj5QBQBnm8DJYmy/lDpkhdgMlLiS5og+EDYiC1OKZ153gRQkEo3/LKHwhK3xLzahJGCo1PfCkgGGzbnT3XhRG6KePfIloNWMCfsXGIeQJ1kk16mFc6ERLOjVk7g2IYZHpdct1FGUsN6qtrejfDQIO2lm9iNHJ6RqqRR0Tqhie9crHNxLfIWYSOk22+4g+KA+aBcHqwy8PtwdfcZbWOeME2KFM+R9YkBWL7cmcfqtnambbzsfFGjDQ9hhYgSzVzLE6t3GHikgkk+CDTkITVlHvddoehQiZ3qo20a1jZqhvsyLIJLgZGbve10HoKVqy3ErDdo3q7CRsASH9Zo9niA2oqsUYhMvba/0p0ElSJZH/WaWdl0H+M0ldSqLVWN1Oz45Q4f2MBlKiJHEbr0zBVN1VYZyWEF17aQ1lDKdCEYk+k9TtAQkdur4YLtsOSOLyepkUfGqDJii7D7LLQOtGBv/J2WG5DiHrvodNjbCBE6jNno1bhZpfBOC0pbis5st7lgG9ZeQ8zhrF7D4DhlyW2jbLuiSve9fL0aRpCSZ4xgue0AoLGxtydi16YwCqcdUhWh1Gym1T5uLrAbVBc5om81yvZ5iPUle2Xvum3kVJxyiKAz1J5iN5hZANhFj+N0NiLntsGNCFsS67PtFGjtpP00lEc+qSyql1YNBPfq/krxzWVosfFy3qa0gZ3aeu/7WFZXFuz5lH0okEOdiR5r9eFwF3k6tMa8NnjlOuZHaDwLm45C8pNX3Nxg1ZwjmVZJ5OzmuNQQGEE35YUtp8P5AimFFAWd6G25hAxXYLyyoTNzAM1pxRj9wdePXNXBmm/aQdRXldMlYXQtdKHwgSU1lgQDi9Xea4vzLiAT77ue3AZTwOPDQAVk6Kd0uJJZpSfuUzMi2UDu7ixbi4pIXVUZcqyTCloIIlzSEgXTsHndL4/kSSqCMPZbnDSCwguKQ3W/FinlN21vReRwc6ZwO2oS7dMXakR0WylDZsn3N56CjGwdmQdUnu6+vBG5jW1A7R5H8Wmp2C3mh5rgbYkEJkcS7o+uWfSNGF07HZUZ2BAvMnqISR4/dq6t0HSsY4dyZOkhdgjRo9acvgY2FMttkUZUw+DKuh0ihW6uKAVZ68Pt6oBIpEbGBL3dciv7yhnpEII5EmC64xs5cJbpCt4gl8SErKtJH5ZCBtIaG6zKDk5ubwdk0tMecqnbFeQsURTE5VJrNl620kgTG3YCFbL3TUvwAtZem95Ibwfy5iKdTE3R1MXdHRJSp8LuEF9Q5lRYPuLG4UoIl0fQzWBC62VDISjhPiIyoXXQLXUQUYFedkQooKcjGMH88KBgZxzrWDqOzOBoqZfxiE+Kru2Yzc28kAo8aCdG41aIYakFqtnBthooct+ldti2InMaMb6fcv/ibprEc/U0XjZbQlXE80YmaWJHZWzUwmHb3yVH89pwSSJQIw4NPW4i7LLpAzwj3QQ/7qWzekAKEDtj4fMXqY+xzd2aCkMzBoqpqsndXKIa7Tseo5dCFMO7bRTvOXJ52IWQK8o30DjUypE6U4cUoqdC6K8HCWBUMebLbYytGLuEoqpIOIZh/vby8eWP47iX/6M35+YTof9nh0/PM6T3918eZ46hG3x+8Pr8fybe3z++1H4KhHsevDVZF78dW/3Dsdunv3KSOFOani+pvZ9mP8/4Wzee3+5+SYuga1ogSFNmj7diwA6va+bXQJv5TWEffP/5MPU75Wbq73qVX99eYX2Z39Wc33kJg9Rtw7fL+O1k8uNL8PYi1leMJL6GdTVr/vZGBVAYe4Vf0Zff/xchEI/MqS8AAA== -->
