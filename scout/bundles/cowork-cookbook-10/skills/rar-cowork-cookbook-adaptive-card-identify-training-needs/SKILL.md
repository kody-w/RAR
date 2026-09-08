---
name: "rar-cowork-cookbook-adaptive-card-identify-training-needs"
description: "Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_training_needs", "rar_sha256": "7e182e5695f7b7c370b53ee518ddf2a16844fef6b0badd4854b63b4727b7eb2f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
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
      "description": "Date the snapshot represents; used in the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 7e182e5695f7b7c3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_training_needs_agent.py` first:

```bash
python3 adaptive_card_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_training_needs_agent.py   # or on stdin
python3 adaptive_card_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_training_needs',
    "version": '3.0.2',
    "display_name": 'Identify training needs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4a6286d600d2999c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the snapshot represents; used in the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical identify training needs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-identify-training-needs-2026-05-24-card.json' that visualizes the current state of identify training needs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current identify training needs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing identify-training-needs status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing identify training needs status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents; used in the card timestamp and file name.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.', 'name': 'output_file_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of identify training needs status pulled from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardIdentifyTrainingNeeds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyTrainingNeeds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the snapshot represents; used in the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-training-needs-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abOjRrrmX9GcGzG2r6qOxA7V0RGDWCSEQBJICHA5yuz7vsvX/30S6Zwqu7t8p3tivoyqbAnIfPNdn+fNSn57sbo2LOqXTy+qZ+WLrZWmUejVCyt3F0wxFHUCvorEBv8tnCJv68ju2qJuXj68uF7j1FHZRkUOpm+93Kut1msW1qL2LPdjkafTgnYtMKD3FoxVu4u9epQXfpR6i6bLMquO7lEeLCLXy9vInz62tRXl4M7H3PPcZtG0Vts1C78usgU75VYWOc0CwbEF/z9VRlr4BdByEQDh+SL1AitdzGLa6cNiiNpwIZ6ERQuWaj6AUQq9XdTF8OFhluXMKi+AHW2RN6/AEm+0shIMffn08y8fXiLw++XTby9OajXg1su7DbMJwpuulzdV5VlTICG18gAMLSfgzBxcl14N9MvALdfzF29XPzZe6n9Y/Od/JoNVB81Pnz7ni7fP55f5j9Llizb0Fm1hNa3nLhyrtOwoBUa9Luh0sKYGuLbt6nx2cgNikQevz5nfJBXl4u/zsx+fi7wGXvvj55einIMDzP788tMCOO7zS93Nv19nKeWPP72mxeDVP/70TU7T2bHntLMwoPXrl7frN7Fg4Lehkb/4op445m2t2nOi0gPC/2Df/Hmq/ibuzSVfnoN/LMoPi+9Lnu35O9D3mW02kPt9scAHYObLa1xE+Y9va9QFSA4rd7wff/orsU7oOUkaNe2/JPfnp+AQ5Dfw1ptLfvrwCN8vi+WbbV9l/vWyJUiYf8cSMPx9ua+O+ivZj8j+g+g0ykFlvsfyu+K+N2H598XPf2nbfzfhw8L//MJ6KSib2rJT79Pit0eK/PyD++3mD7/8DkT/H8WoRVc7DwlfMiuPfK9pv3z5+YfmcfuHX37+oStBFntW9qWr0+/J/J5fH+v8yYNvo37881yw/jVP8mLIF19raPFbUf6P+vfXhWalkfvtfvNp8cdKnD/LxWzE+6JPF/yhGhug6x/8+NPL7wB+cmBN98CoGX3+4z8WUuTURVP47UJ1iq5dgAC3UebNyl/CqFmAvzNq1B7waxMBx76NA/k/R3jWuPAXv/4v54HnH503PF9Zb8D2xQHI9uUdhr+8w/CXBwz/+rq4AOFFHQVRDkBWoU+nz7kVgMHzwmXtNV7dA7Cyp9b7CGr64/xjEeWLX/8l+V8eol7L6dcHOEdPBFQYYUa/pku919nOWwhQ/mmVA2jKGz2nA6ukhQNU8p8wDzQpUkA17eyTJonSdOFGAF8AXU0P2cBvn2Zhv/76q2014ef8CdfI4sljzQoM+KrO4uNHYJufRkHYfs49JywWP/z2+w+L/1r8d7Mewuc1ToA73qICNHwQH6iyLgPDQMBAiAGEPKLy2+9vHgZiAIMuQAwjP/Kek0GWJp777m51R3+EMXxhe8DNwMVZWdTtg0Hb14XgL77qCxadH80sERZNu3C90suB+50JSLWAOV89mRftogGp2PiAN7vGe6z6qz1HCKiYgXK32l8XEnMCnFSk4H+zmo9BYHKRR8D9X5PheR8IqX9oFpt3Ea8Lec7LRWnVVhnW1tsavvWMy0zib9OBcGuRe8PnfGZgb3bVo0ie7gnm/iJy3kL68dFFOAXoInK3eV87eOtB3MXlwaD157x5KwCrnkPhAEIAiwZd5M608Le3lGrCokvdh/+AprOktyi4b1F55OA79y/eE3jx7FPUZ5/y51bncwevIXTx/21XNBtMb7cKt6UvHLvg5ItiPAMxd4FzwJ6NIxD9WPNRdN/6lXdMeofmz3kagayqp789Rz7MfRvzhLuuBt5WaOUhH1gMAjHLfaT2nKp1PReF9Tl/54DZggfgAa0BDoA6mdPzfcH56bumISj2+fpbP/BIBeB6YDhI30XZ2SlILR842LacBGg1x+o9hiDPvblUhzBywj9ZNfsWpBOQvwBKRKDgAE+8fsXl59N31f808dn2zFMeLWEHqrN+CAB6eLOCc0jmiAH12mfTDez89BACzMjKdrbdBvUBLH3e9Gqv6qImaufgPv3qlQCMP87fT0vnu95YgpIAzgKJX3bAu49SmTMuA00N0AGgBaicDOQcuO28O+Eh0Mrmuge4+taFPiU+br8Z5D3qa2an94mzIfOcmfCfWWvl0x/h4fK9NAHysnnEY91/zLSvq82yZ4hsAMyBFd+fPjuD1ye5P7uHxbvcT/+0q/nx39v4POj6+ucE+LQI27ZsPq1WT4p9Z9hXAFCrp67NV7b9OLPhx78o7z8Jf9r9afHvKfgnEW8F8mkBva5f1/Ojw1uCvX2AP5iPG+MjOj/9nCveNwwFyxcZyLA5ehOg96+E9z4EsF5QA4wBg58E2My8OQCqfiA+CMXn/I8ZP1ccIJQ8mDO0Kf6ABA/mB9n/jNxXYgKP8has7c4dY+DNW7VHfTTey6e8S9MPLwD/vH9xizYTUDandjNv7kARgSasjbzHldV8KfwvLrBkvvrzxpYFd59plYOGJCwe7Dp3PcDev81097VpmQP7yH2A0dmj5J7WzUrOurdTOSv73LjNrd4DoMb2n9c8Pn5Y6euC9QAYps0fs/6NrWa2/kNxPv0L/OoAwz4s3AfpgIIAGsw2z4VtNaBSQJF8V5cHWXx5ksV3nDAzzB/55NEKPLoMAH0fFt5r8Lq4qhL/Xdlf+91/FnwDDcYsyy0+zVz74Q3dwDfYo3xYfN1uAIveNoCPDXvegb31z/NWZ47sY8r8A8wBX18nff1HCtt7+eV7ej0g8MscpC/PTPpH9eQZ2wD2zx7+K9YG2gMN3M7x3vzwL1X6R3gN4x/X2EcYfYx7jRvQ6vyz94CaD2AH9Dhb/M2V3wwqHhu52SDggPb57w6/vYBcB4q01lu2v+0EwHCAgx+bue9ZAVAAC4LrZ/mCZ/93e4Q3IU1ogfYUSCE8iIQ9DKcwn7AJByHWNoZ4HgaRruvDFoSTKOp7Pm6vbct1URJDbRyxUQIGoz0b9oG8JxJ8mTu8aFZs1mr2HQAT79tjcMt9s+hpweyur1uSR2U/DfvtxcZRMHKHNgL9/DArCgLLHmyltJd33C9GzWirc7I/JkQEt2xdu/FU2gPhptNNgqSSPbcdnaxV7hwElkRPCn6rPCPEhjxTVw5R2u0gqLV4z67IbW+6QnHq17h+wu6VZuedJ+uJUR28E6SXKh/LEooY4bW6RocGEm+pYp0ELNPJs5NesqsS6SuS8FZReC014dqloaLyScs1KiZTNjWuch1Z3ap7rNCpS+jWFJ0oMdweCUgaWvkiHyz7dO2aEEa7ZJnaDQodxXpDLQVsRcFuX4r1QWJUGKJPm9sebkKO26fTabzpjp1oqxWSlWo0pnssguR+d1iriu7t422QmGm+vUWppqVpVq3cXUEajW5jS8o73TtYO43E6Ua09xWOttAtumwOKkRfm6hCbucd029FLLavgqliunM9nEgR4VCm1ve6RW0nfaxKll9VnDntOuh8ZwKm6arrZmd4Tp80GqRJcoZSkn7gCvUgRIYS58YUu66YkhdqA2kFGsf7IeilQy3jR72ul/Io9pbeeya/2bOCzPvnsxnShBwjDAlX2ijyxpkw6q2G03tIuOATIV+j29TasTN2W7gZl6plczkcCNLIaEvdMs7wpbdyHWwJjpg0kOUI+iRGbc3L1bopYh7gN57ltlHGUKyqmlrOrekr3G1pC90t9ZS4lKk6xrbMkZqg451RQvp+v40vo3ZK+9ZcqXa7Dk6Q4zqheuNSXkv1ZFsQd7FUCXEC5gq7cVtewysBbxIvJEZiH5nI+hBKXE4fd5aGa+wSukF8wMjoGR1SWeixsufHzQBPkdTChz182RjbML+IYc9bDFQMW9KUlx1e3gR3I+Y8VDYSfs+QrmrERODhczuO4ZIviOJcUmmqpfdAQ6xxyMnxqEkTr65onZh4VEgjf4hM9twsxdV5b52IM+SHjC01E4T22Omo7gsTyUMq7eww1hw4o7zBsKOtuVsdQhlejhiIgNxfDB4fmgNpaas7sdzJyHK9yfTVWbHyZnJW95rYThRvt/a24OWdCp/RrXKt7YjSPPzACCR0OCHmhrZjg3dolSUV3l7r+DJc94GsGClv3C0sgY/8DUu7iCcgPj8gcEKYx3Jr2IwqS5BY+Fx1sPn1RuC07RSrNDkdg2aDeSEjKMt9pez7wT1EfKkHB1S5TnfYl+7hQFCVnZ2czRn1EPSIH53MlY+1uaXljYDGZ+UoDDy4nMobn6iFRQZ3v+885VKf9jtiEJFJtLdBWW0ln0EoBIbWzqkZ06S1l5eL7fryoXO3hn/Bj2s8YnhvzebqTfI6oLhIVrHGBO6ZHZjV1s7DxCk50i3NYrdpNlfOVMzkeG1ueaGUg9KJRWkjdxe1TG9f7wdmYtKzcsG8W4cxsUwlo0nAEFZenBV136u5tbndmhttDfkucCuotmMJ5tcFL54oukuJq4bR9TlHDYE7XZwlSjSejavHAJcTJIXxw1KUEd0hG43YUiojCuYq9aiQz5m1EK1oZLtNArVZmpzHw1AaHSk2OsqcOCQ3dpOGoVwcT6HiBAA3uTU/ao6yV3KhGzpKROom9NijJVtjGVd7jrlTpJaaBUyQI9ptiH3leR5KyuO9cXE5Pg+gEVa3ecAeDk5+9BPuWCWwfKSONxYSUN/iT1PisSKhBJGwpXojuITZOjEPLFXskOByEs/YOsDKo6oaaSyPlVFLBg0fnAw/FA2Tm5MXVd6KiYZoHxe1OkjF6XRjd9ZaKo1LMrgJp/RGhfm9vz/ZsKkIqqVclDiMbeVoW5elXvgjL2GQR6Zifqb9A1wwcUIXUYfvAqVCk6ipMj7clEbrUozYHou1avIGu2fq3jejK4sfMFigSPbExsr5uIvTRkBuB8hqLAFqtlRc3KglHG+5pVrvtVwW7aW58nc5Tpx0U1qLzrm7mlSQFsvLVCni8bojpDU8Qucty3Lq3pyIxiZOcE4juX5g66o4BzbU6uOwokhfoVcdYvSdv+rbFt9C4r3fV+TWMhG0gQ2Btkq69S5L1FPRS30OLXR1xdmqSxCB1MN75Jw5GPLPdsBkpw4h+pWxM04naKVGPKRd80CyaKdt4oyUl3bI1m0+HFHTsJ09p5zbIBIB7DhX3awFienumdFIE2UaTHLZhSRharCnhfHqaLDb+1HQ96oIZVJToFmzPHX+TYWua5gnwkHqiPheB+Z1id3JmrplYr8R9n4KgeChPXMUaBnf9ocrj2zVtWD1Y8RfMw/Z7vYEt2X2dqMMuGrEphIhEIl343R2DRrayAFHXzeqpUl8h96uuX5FODYyA2PFZljsGKq2vQvsJek2k41tbScm7duhgBRU2K3r5LxrKZ4etXWV5GTYjf4RXYNaDnec5Z4i7Fyk7MZZX3lreyjFRrwKFidHOrnOytCIyuWh9iZlW2rHJjbH47kUxHOfKC622lRYjQQll2Yp6tpqALcJs5OxnKHLU9TVokRwiKidHYS70f1AK5VxbS39jl3Mw1bWgzUf09fscC7GiRItTVdL62pUqNCmOeQ2yytb2IFOLh1LCJ3uoG360tBLOOqNsLLqa3/cj3AfJpqYWdiuGLfCIY+6yoek3mVFa62SE3GMeG5VrG8yLqWCf0avBhlVhypRqXtT51uTxW7aNhC2e1EJd3LIXWV9z1vRxNCeJQvZPhKzXtxWbhA2e17OQaXhCimTt4QTgxp3/Vi9OGeaGreAouw4SOoLZkZiWWAM5l9cRbFbE3PvfL4JwtDNYAJDD9vBAGV2hBwckYO6urIOxh74kUnqDWy2ebn0vK2Htrv1YR/n/EVFLvp5c/YcfMkoGXyfeFuRuIyj+GkjHK5EwZF+a4VRmlsNP/KpoEXxVByzTkCFjBhWRoQXl01/oLssHu60jXbbNOcly98hF6Y/Hgplz4fBRdjX4f08Mbtw2vGhGSpxpEj1uue8Jr0U/a4hlDY807K9x93UOSGeSaOFK233eqvazRrWutKjFeF03uwt7cqmIjn5+Eau2PGu4mUzmgMCXah+hVyI4wCX2xCeaEpGcnHFwtTqgmmXoT+TYbpBzX0ddNYZE45SHO2ThlKNCQ9Xp8zhluPIdwcj3Kt8iremdRbEtZadGfV4xCOjN9MznDQlTXDQNmFrAQpvd2+tyeruCCRf8hSwQWfSlbXcFQUnwIY2lnRitLbqsOPu4vWXPc/0TenAucpWO+J01Zysz8OqaUO4GqJaY0LzfOg7c5/izCaNIhE6Ko7Cy6h62HgMqIIyuKZUwcVBPzq3Mb5FJHMXO7fRpNXVFNFhk6W7pPKXx8OOxLzTxQfNTrIbWViXkkson7kTInToUbPDYDKTXXoLm/DS87KW7zMfN3N7ZY3Ebmtip7NrYcK241XkFiNrfLx3Va0u1yepygxkdA0tPxFsdtAhAyN3BFrsO5K+cvEZ1aQ910ylRAMqESukGu4HYdXowsHcd1J2KV3FrvpGW92sPaF5A15uqSuBCtDaAvV6G9OIHxP+Lvaq5eqxQU32xaotGubB9okdhJjyKfaAHEawdUYlrZpsQhd3mi2a8CE8eBFinwbDdNenchNkkJa18pXqOt63W/06EWJyv7gxdz1Lnk8QmzhZB8twU+NVTUJXm2uYSjpqtHs+YvdxvyHJiyAnU8kc5aBSbxAkECraishum3oZWvWmvIbzCR3vE8FC0UTROs9DNyxe8oTPJHtMzYP0UoGNKdjN+JTSxlgxcbWb0dyGY+Q17S8ZATpGu7gOfCikc3a5oeuOFDa3bWzUBYpI/DXQ18ZevGpFEriY2GhUnWaYl1n1Msb0yujOZVTuGE70XEySrzvctD2WRk5GSFBprhncVdUkJEgQir1dkZ2yjMPjklp6h77onazA9DPbDre1VN2R/nDz+Dq2a6uRlzCXD3S2qdTNiI8Wb+bGDWwGau6sUOededjlhifXydLgoBtSLQfQzUhSVk3ySru0QStOyYHFaFgJc0Kvm5NHTTCgwomVqEDDzQrfR5KbRZIQ+FIdR4lw2PK9JdLV6tJkyI7Kqk1m03XVpQ65yhEkCrIY1RMhDBRsquIytQd0E9046oZs4+EsGyVzjtSBn2SGjrKlBdCosq1ay6NgdTAjgpaxPWNHDGGeKIRs18i+arVtWYw6hV9aPiJUdtepRr9RotKUGbxSZNnXcyFwcR9QWuTiThqdTfSgSd0V9K3YaNgmfCl9tetHvSF3bHCZrI67SpPRcRImpdRgk3h5FKFxLaWe2tMVhzWCs8LX1mYf4qQoqSfydNZMvcLIc1nsuboarItTu0d0gtZc5xY9b0N0eV2WDY4AlueP1+MkYyZkD9n9Ollqi98wjMgDwyz55F5LbePtij67iju9Oe2wYscMLMVUS6qBVqvwhjVWbCxhulrj92G/XkOtmiOuRxXkAbY8E6OWt+lEyPezHNnwrtZz0k95DAG64ublBHtWLuBHCTJ6ilg7tJKmVVHcTf5aozEhW7uje24lD+WoRszvbGgvW69b0jcMB7Ddx4zBMtSFp0YWOkGyygp7pa2YS7xN73ohMBvnpotklA+lHu87Jjr3tXPNcWF0jgwVO0p8qho9II02hvnYj5LWNCEElS0JJ21eDAZ/d4hciuWPu0EXrti27Xs8JlYr9rIszqbo3KWWXGkg8gf2qgQ7G+xM0VTStu2d0Yxmy6NJmaFtNopsQd7ruAjgLAX8cu2tnY6TR0voGkX3YWt7FJZhQtFkoTjrlXz05X1+ivPyIvS62dnRWdIzp9xjx2VBEfR5fx1ry9fy440cR4g5be+bfst45GqdjE52werDfehqMqXJ4AKNCIWvdF3Py54L9D3GGqvQct02jO7qDnS+engT1sKKW+p7YVnbhAWVPZIfFH50ZG+lCBBb4Olmane4py1zAMuEHU7Y1J2uQ7A16cjz2cFaLpPDvbn30TUbqqmDAotLNZqN4Aufp3kNZyXmqeFVArk7yALYv5qxktuIAdkY3bSoeQQ7iN5mbmjRj6fc4paCeISFVNRERbA5Z2fmy7BA/QIvzwJLD2EHtuoEjhbp/bIuEBm9hJcNWd6D2BvLhi5FayP7cm5JO5vRcFjaC1iLjTS6IUSu9b1tE48HvOX9Ku8Rol0hvkuRwi70R3eCo1MaIMtRdgSiYhWm3iKH3U6696TNNtlQ3xHEKHhKxyOLdv0lSrFdRkbqksmy4z7tiOOo7Z1Qs4+G0/N3Luy722Cb+vqOTWx54ERDu7tYM7pZWvjZEbSamFjcbep+5IN03IcUTi8Hl7MHAj9ndU0CaMGOVHTr+/aQW9Pk8hFUxncjOWUnGV9PthxcHarQr9t1dsO4K3S/tJ0mNPIZh1QV9SLSWMbQNHB3d9hw2Nl0ER5eu8FwEHartU/WkcsLl+MlMRFPKEJ8j2dXuyomKLjTpd7QnuHmxzujNKtMtijrUBUlofdbao3eoXXEXxBCkshTuTJAnUfipblLOHoiEHk4lAN6lMkDtqsc7KzfBVzDdGKlU3t9R2w0inCh8kyiaBc0vqMcEQVdiRbWHih94nWS7RmeD9g8sy0kVjrkbHitWLKjGF9a19rY3D0PBjlv3NMN8nrP9LLYM1WCWu3Ks4ulAoMJnTE2AhfIQ16s0LrcSEx9rxQIIrBSWZ3siY7a4EoNTgJTG1EWqP2d5FDv4EjQWUBRKmFiCFpVIlc4qIN7Fl2Zx4uy0aDDvnaTxHEYfXkbXZMPnKV4uXh7Yifa6G3NpoW2MfWOxFnG9BFNb3SPZ1f2mUXZDO94BtkIQuWIO0IkaJbQtps7C0ubybz6RrYprj6yIpThuL+1R4jzU+3sHVi1zS0dM6nCGzQBtt1tyCErZB2PeF22Nyg/djbA9gqXO63OD3iqqY0b1HprYE20PLHW/V4x8GRODsvA0k4ebClDjldyhXaRZeITVE3QftRAp6vg1yLmi+lo1ss2P/h2t7d3XIpvSC1S9aVHH+srCVrFnnHEE1NXKCTWm3rb5lCF83v84qKWA0X8sEXyZmotxIt8Z6WXOL29eeuS7K66SwW3FUSWG2JF0I7cY/XU3KHUwIX7ZlPvXWGXnKWlcbucjzGO+j5VEyS1bpLNigMpSuIYjdnjnd5tB8I31d45Vhnm2h66gsIrlJKnKALEt8J2epx01oAHuOhfM6Q2j1xWmo0JRah5U4Vtv8PgQ20F9XKdIcoBW2uNn7FqrfdXsq71c4dmSxbaG4F/OW+3kyGeal3FsYJcy7BycvA42CIqHyR84wkhvYfiJgt60ySdNRNwMrKJyNNk2y1WrLE1liegG2H394TqE/QW1sclPKyZZb1NCgqKql1zzQeragF9TlNdZWjW95Yv6yac4dndz2oAVBhE0ISPkeWq8Q0BX94dAEsQIR3i4OpOJAOz1mTKS9t0vZI/O9AVqh1TT1fQnnaRpaoqA3Rf8jmiTbnuQFZw8dj+drs7NTXaHn7AylCPWkoeqDoz7oayJCWfbYXBIxWDTYm49Frfl3QJ7EhrXVvF6HBeGvo5YQQWT6+rWgYN5ZlWTq6yS/ZUkuYK4XRWWKPQOj94F468nQfMlpR2353b9KCsXZglSy5pQtjdkIk7oc0Rp9eIWTcCtLr0YejYEyeegD8pFMIRb89mpLWZaPwWyy4R6ImBhM5ECPJ9UoIS4lzQSYuGswV+x7GKGN2Vv4lxedqs0ag9+XQi+62UoOxZrOUTcR/JvOUH6ugLzoXSxFMseV58QncuCbFBO25omv77y4eX+Xzr7Yj133uZaz6i+X92GvQ81Hl/d+Nx7udZ7qfHWp/+Tb1++fBSOxHQ6nn21aRd8HaA9A8nXx//pVO8WcT0fFPq/Sz3eTDdWsH8OvFLlLtd09bTl6ZIH+9wgBl218xvHzbzC6oO+P7jEeafzHlcP9/E8OovbfHlefo3H4BF+fyShudG3y6Dt4PBDy/u23tBXxAc++LV5Wz125sAwFjkdf0Kv/z+vwGW0rUN+y0AAA== -->
