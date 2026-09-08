---
name: "rar-cowork-cookbook-adaptive-card-purge-and-archive-business-data"
description: "Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_purge_and_archive_business_data", "rar_sha256": "ee31c9ae3d083f6bd241eda447e5d5c63631cff4c08d22c189b3e2d38752a822", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_purge_and_archive_business_data`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_purge_and_archive_business_data_agent.py` and in the RCI capsule.

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

Purge and archive business data Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data
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
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date/timestamp shown in the card header and used in the filename.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 ee31c9ae3d083f6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_purge_and_archive_business_data_agent.py` first:

```bash
python3 adaptive_card_purge_and_archive_business_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_purge_and_archive_business_data_agent.py   # or on stdin
python3 adaptive_card_purge_and_archive_business_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purge and archive business data Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_purge_and_archive_business_data',
    "version": '3.0.2',
    "display_name": 'Purge and archive business data Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-purge-and-archive-business-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53ab1d529c84ee7f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/purge-and-archive-business-data'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-purge-and-archive-business-data', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date/timestamp shown in the card header and used in the filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical purge and archive business data status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-purge-and-archive-business-data-2026-05-24-card.json' that visualizes the current state of purge and archive business data. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current purge and archive business data KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing purge and archive business data status in Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing purge and archive business data status for USMF as of today.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp shown in the card header and used in the filename.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of D365 purge/archive business data status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPurgeAndArchiveBusinessData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPurgeAndArchiveBusinessData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp shown in the card header and used in the filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-purge-and-archive-business-data-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardPurgeAndArchiveBusinessData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZOj1prmX9FkR7TtVlUCEiCojhsxbEJiE0JICLkcafZ9B7G473/vg5RVZV/X7R73zJdJhyslOOfd3+d5T8JvL1bXhkX98unl5Fn5grfSNAq9emHl7oIp+qJOwK8iscH/C6fI2zqyu7aom5cPL67XOHVUtlGRg+28l3u11XrNwlrUnuV+LPJ0XFCuBRbcvQVj1e5COB2UhR+l3qLpssyqoynKg0XZ1YH3UGjVTjgvtrsmyr2mWbhWay2a1mq7ZhHlC3bMrSxymsUaxxbbfz0x8sIvgK2LAOzKF6kXWOnCy9uoHT8s+qgNF6K6X7RAYfMBrNIoflEX/YenLmc2HKhq2yJvXoE/3mBlJVj68unnXz68RODzy6ffXpzUasClly+ezI6os8VU7lJPe+l3c1lgLZCTWnkANpQjCGwOvpdeDazMwCXX8xfv335svNT/sPi3f0t6qw6anz59zhfvP59f5v+0Ll+0obdoC6tpPXfhWKVlRylw7XVBpb01NiDMbVfnc8AbkJc8eH3u/CapKBd/m+/9+FTyGnjtj59finJOFHD+88tPCxC+zy91N39+naWUP/70mha9V//40zc5TWfHntPOwoDVr2/v39/FgoXflkb+4u2kcsy7rtpzotIDwn/n3/zzNP1d3HtI3p6LfyzKD4vvS579+Ruw91l5NpD7fbEgBmDny2tcRPmP7zrqApSIlTvejz/9M7FO6DlJGjXt/5Hcn5+CQ1DrIFrvIfnpwyN9vyyW7759lfnP1ZagYP6KJ2D5F3VfA/XPZD8y+w+i07lYv+byu+K+t2H5t8XP/9S3/2rDh4X/+YX1UtAptWWn3qfFb48S+fkH99vFH375OxD934o5FV3tPCS8ZVYe+V7Tvr39/EPzuPzDLz//0JWgij0re+vq9HsyvxfXh54/RPB91Y9/3Av0n/MkL/p88bWHFr8V5f+q//66uFhp5H673nxa/L4T55/lYnbii9JnCH7XjQ2w9Xdx/Onl7wCEcuBN90CqGYP+5V8WcuTURVP47eLkFF27AAluo8ybjdfDCKBk80CN2gNxbSIQ2Pd1oP7nDM8WF/7i1//tPLD9o/OO7ZD1Dm9vDsC3twckvwGYfHuH5LcvkPw2Q/KvrwsdKCnqKIhyALkapaqfcysA0DsbUNZe49V3AFr22HofQW9/nD/MCP7rX9Lz9hD5Wo6/PiA7eiKixuxnNGy61Hud/TZCgP1PLx1AYd7gOR3QlhYOMM1/gj+wqEgBs7RzjJokStOFGwG8AVQ2PmSDOH6ahf3666+21YSf8yd8rxdPjmsgsOCrOYuPH4GPfhoFYfs595ywWPzw299/WPzH4r/a9RA+61ABo7xnCVj4IEXQdV0Gls00B+Dech9Z+u3v75EGYgC7LkBOIz/ynptB1Sae+yXspx31cYXhC9sD4Qahzsqibmd2jdrXxd5ffLUXKJ1vzawRFk27cL3Sy10vd0Yg1QLufI1kXrSLBpRm4wM27RrvofVXu7YeJmag/a3214XMqICjihT8M5v5WAQ2F3kEwv+1KJ7XgZD6h2ZBfxHxulDmOl2UVm2VYW296/CtZ15man/fDoRbi9zrP+czL3tzqB5N8wxPMM8ekfOe0o+PCcMpwISRu80X3cH7fOIu9Aej1p/z5r0hrHpOhQMIAigNusidaeLf30uqCYsudR/xA5bOkt6z4L5n5VGD6n8zw5yeM8wfx6HP3QpG0MX/55PT7D7F8xrHUzrHLjhF18xnWuZ5cU7fc8QEoh86Hy34bZr5glhfgPtznkagxurx358rH06/r3mCYVeD2GuU9pAPKgmkZZb7KPS5cOt6bhHrc/6FIWYPHnAIrAaoALpmLtYvCue7XywNQevP379NC4/CAAkAjoNiBhG3U1Bovue5tuUkwKo5Y18yCaremxu3DyMn/INXc2xBcQH5C2BEBNoPsMjrV9R+3v1i+h82PoeiectjYOxAr9YPAcAObzZwTsmcMWBe+xzPgZ+fHkKAG1nZzr7boFuAp8+LXu1VXdRE7ZzcZ1y9EkD0x/n309P5qjeUoEFAsEAblB2I7qNx5rrLwMgDbADYAfooi3IwAoCgvAfhIdDKZhQAKPs+oz4lPi6/O+Q9um3mri8bZ0fmPfM4sPCB6eDK+Huw0L9XJkBeNq946P3HSvuqbZY9A2YDQA9o/HL3OTe8Pqn/OVssvsj99Kfzz49/7Yj0IPPzHwvg0yJs27L5BEFPAv7Cv68ArqCnrc1XLv44c+THR5N/BMo+vjf5xy9N/nFu8j8oefr/afHXDP2DiPdG+bRAXuFXeL4lvRfa+w+IC/ORNj+i893PueZ9Q1agvshApc1ZHAH5f6XBL0sAFwY1wBqw+EmLzcymPSDwBw+AlHzOf1/5c+cBmsmDuVKb4neI8JgHQBc8M/iVrsCtvAW63XmuDLz5WPfok8Z7+ZR3afrhBeCg95eOczM5ZXOhN/NxELQUGNjayHt8e0Lh2zsUzlf+eCieK3b1cf0PkDmjDxi7gdnFF76s3dnUdixn256nuXn+s5q3wp9HIe/PsoF5HjT3D0D5rJx5Csyl0TeBi+fJ5BEpQLxfx6c5fHMQvqvwAYRD+2dth8cHK31dsB4A3bT5fXe9c+Q8I/wOBJ75A3lzQMg+zIwEsA00HjBgjuYMIFYDOhI043dtScroDVBw/h1rdkUPQAigw1eWmmMa5U7aAWT6cf0R++m7Ih889/bkue9EdCbH31PhY6Z5jEsgUx8W3mvwujif5O13ZX8d5P8s2ACT0izLLT7NQ8OHd2D+MFcB+Pb1HAWC9H6yffw9Iu+yl08/z2e4uQwfW+YPYA/49XXT17/E2N7LL9+z64Heb1/S/mfrlBmVAWvNOftnU8dcsXXhdo73Hoa/hFEfV/AK/whjH1foY/1r3IDR7c9BBNY+qAkQ/Oz4t4h+86t4HFRnv0Ac2uffVX57Af1pzYreO/T9pAOWAyT/2MxzHATgDCgE35/AA+79352B3oU1oQXGbiDN89aIQ1re2oWJtY/b7gpFPNdC0Y2HuZiDr3Fw3/dRBybc1cpBCNJeeyt3TWywlUWsVkDeE8ve5sk1mg3EyI0Pk+TKR5EV7Lqev0Jdl8AJ3ME2K9gibQuzMdKyv21Notx99/rp5RzSr8exB2I9nf/txcbRuZHQZk89fxiIRGzoKtmjsINymBhCvMGTNDmRSl2vaYS8p+UNikPfTNvUu6nWOQ16hpoEw+SobaCYt/RUjYmaML6cLK9XFRUOgbhL79KmHcbTWcwOeYk7pE/2vTsMmbN1U4uJiUN4I7Y8dBGizAgvpxHZVry/XO4JElKYCFOP+lrBvWWZF35sXyG0ujapecvRrvXprXBH+qzRtTpWO5+A/Lt2rrfnLIyWa2MiT/7F7g38xqXtJT0NnoRJd2sttmwEG4QfYT7k5htcq8YTS3WdfGqM5DJtkhs91HfJ1bZj6TPK0oVuFrYNj/rEVpCT1MnpcuU2ipGITTKkApY3urU7DodrjeDQUrqMpnOdCENqB8gDjojs0JRBpB+Olx2q2Zggh2y29Q8KHEn9eb0s93nF39d7WUpF11xC9tE6GdkNavMyou+8vKGpg7hniJE3RZeEJ29A0Emo2vGymQ5HPZa2VDo26iVub3tcWKLQeO71AeFOV15Y5akuwW53mtDVXYG0dRadj5FG7Li22HNB4GfDJvBsXr4wtHEubpK6CTgdPzZIxjjDdp+Iax45O3zWasuTZZvxKtjLFT1CdSbuN5TaTnVfewam9ERRpbpGa1UniAfheIt7V+LCKNY02gtr1LuhJU7t7ZyVFUIiFYesYbghLm0WeGMyLQ0map1WLBLLlUvi7qa7zbTtshASJnG/945JJKhMHyPHpVTn/NDiqM/FfZhK9aGNwrNHb4aN0N3uxZWDoobCXFqvj/71bCcGU2hwwyRkwd23KgrBqSL1zLiORo4gxoo+yrYJC64FM61kwoHgN6vUQLiSP1x2YzmcbNrqLnauabc9s93snQ1WjFE5NZfSKS9JCkWXK7MZruh0KDWQ/CWt2icaLdrAPWY2GyTEqB5tZUMWVo62Sl65uFo2W5Xle4Lsg5WDysW6zoxh6feBzYjX+7TlW6XWXfW0WnpJ7KyRid7k6H3TuFli7pBIqrHVbhOoxMFeIzXbqEScuGrdLJfJ2mNTVCKdlVYYsCuJW/O2G91MxLip3l+Eujb0nCNIv2ZVjgsgToNbuusKpUbZsyFcznKW3Q5seGugXai4VaaHLaS7TZzEnhBIV97BOCm+3IYY16hT0LBOYKrBAWIIuJNJfeovSK9aoXhg2dPEZ8cmJ0gFHrtJbnglN1s0FrmK2F2xOmWPbXvRyiFSFU/sbyw0oJdY8SotUxX2ACPiIEceFZ/US7jUh/OhWBP5xevIyLgV1T6N7ak91NC43u66sQ0m2wuX23R9mKAVMnSjVJg1S9UWQqyPJ+fcO3pz6s/hjTFR1iflgTv59flcXzBTFu1J6gniJp7pc3+/cGOoo1ZF+I4lLeGxuBk6PaWYnHQ7hmjdQN3VgnLXoLCcxA6DpN0khhe8E+SGcivNOKUmjhGRe/LWAiiF1kl3t2NUafxhT+HmwTuQy1PqLI17atGOvt6xd+TqXG6pcnGJlslVZjAI6U7sUZTd3IyEx+72xNETzNjNPVe40wrdGzdsy0fNpuL33KVMFfSaUwJc4yIrI2lhiccmY/Zrz+jcC7uydfq+U0zzOJwhQh3YSxMKkIPL5HAi+dxy3DqA6vsJjYM1EjPjGFG2x9UnO4FrzGOLCon1+7XkiZQUBrpGCws6dcgxPO9U3A6GMLCYAyIHKnxXXXFPrq+cRjHibXU+RMNuv5akvSP1HnaITkS/7aaE3DrL5RYJuVjV+Wk17ItoZRmKRCmrA8uX4pH1NgreL7ujuTeOXOKjcrO3rKBlhRJOjstw5yDwIWVyKhk2I1nBAsWBGjwX9E2oI2vsj9Qxir0R11ds6mih0PR7ACx6p/RJ2riTfzE26SEIrqURBUt+yxJG11yj4YZq1eDwCIt6I3zTmOl2Oza3/sTfahLy/Tra+IkUJcxNp9WGw3fZiAen2J2gXNYFtyCZGOZPvrMWCQ9V+WzXlxm325xClr5f0cSGiEM+EQS7ZCEo5Mec9A27GxOsrzxVlacptbn93rlxd41SRoJk5FZ0TxVyLrbaTb+Hd5Xs6IHWbxfS6yjRHNClp8Y2flQJn4PjNrkcTq6SbLCyYTLSUKVRxi4qR0T51inlUdy1qHEUt2yU24iQRlnk63IKWjKTS1mDvUPbZLKV1lXucN79fKYuWHqy+xSRj0ug8xQofX9Y2hmDmNDKoq9l2YbKiCr4tMOk6ALZok6LcZT4NQqqrEHvmd9TF1g5eK20PZ+T6NCGFH3OVyMPwsVzouA0+XBL4LPFl7rZ1YXDKxs6Oyou2wcFSU25fMmw67pBuDUnMJwpQ1rjFhLHbsvOooiNm+8Vsc/s7X3MBwk7ttS1x5NWuZCCseuOa50aOjEd8+OSNRhYyGrCEOljUQtFUFfjJMUSFXGdwB752EgwZZNcVcSx1d7hRqI9tls7OZ6YpEYZf7dDFYwZvIgI7mhGx7izTblKZy+cQSEHF+Oskpu4qlA0NafMfRSUx9LiYdqvL8K+wFbO7tiYTDrIzIm7Dn5yWuY5zUXXrYzdyKut0nTDEuIyB/W4v0rMYIrMaQsfMAWteKHqHMfwhWrFa4VyVUyWomA9VxXNSCrdtJacV9i3MumuIR/Dm2I800s20sYRaxKJkTClSX2hiE1ps5cxTdPloioEYqwD2hZTnyKWlCbGAl+OfQoK4mgwJtlY6aiWVwIexLNWcX6BQBvJifZ8Si8H0ZCJmy2W3njWzxc3rKRueT9PzNoHzRNIq0llZVtpLgIhZunAJmNQE5bUhaeCjyH3VJspO04N6eVbFL3V0eRR+zRFR3usDiRdS1PCNp7CV3oomUYIJxFiOSdaTEsqX+EVf0ybjZbeTTBzOpSFnBIYGFI3crahlhYT1X2oaQhgJtFednwas4iyZpG6VEnsOuYxPZwK3ZXyNtmLbC+fwzLU2kSTa3jNeU06FfddBN2S/nhUbAH30716B4hdnUeP5ib8rqzcm4zcOIoStwXVdGIlROnyJJPh3Q5k2+gYY1t3PCRDd2jwtP05Z+iGKNEbxEqbEw/5gy9gdFp0GsKgGFdqwZkdKVeMp21yVzxtBIOjL/f1JudWKB3tU+pcIdYkcEEdnm7703G4ny/pBpOyFUtOytKK+T3Trdz61BaXpQOxuKUc2nOmqAN1EOhz2HKtaDrjod4giWYw1M0XHSLskSpk/XZM5fQ4mAjACLowVtIZ19aONO7OGQsJg2AEIUsq2NB62K7Owy7Z8ZNxvFaao8FViluVnVGH4LC3ztLlsD/Kg0kt1e2gc8TmmmLVeTi3bhlU+8oMscYnhTqj14SFd72R22KAR1RNYyQf45486h1frcUb6FjXdqTDpeS7raBxS6ZXBLdbihticu6xj5nNBcfMUerTYO+uhXTliDF0pOo9emDolgIYebIyupHJPN4QYeNMaH4su5vXTaRN1UctvuBIRpWtghxrEH9nS0CwiK/CTk2EtGvD08RxMifKKrPvC/7AStyRvWt0HFD5tZh0iSaqkKcBlexXmEI5wTZRwFQ9lo1WBRUjO1HL0Bp+Euxe1+nTVU83k2ZfXeQWm/eWq8p8dXORaOWdCQqC0Vjwub5b37L7anM2b0NTY30aEoJadHgcMc5d3pxDRreqtZEdvHvnqY4C0JOA07Jq2exoyh6UH9ldWXFLLi3xQCJXhp0VciQbFwbMnRgySLRDuBW6BFygJ9ZerD0FYSpPP2rRkZFxQgrHg2+KxO1MiR1z0ZXlwVhH1IhqG/NSXuQVAQ1Kpe82t44joz0nhbS2P6jntjHkjNxcEg+VBU2d648s9oIbdYjRKDB3hnWqiTheAZgwbOSkYq2saom2FtaVCZCXX+E0HAm9sFqvjnq4No7KsLytttdcBwQ7HtmbctXkFaQrjDGu/H3P4rA/hXZzUOlst9mXt95EtTq/G15L2Lp196bN0dfJe0AfHZPzGw3VBStkObib8HST4gd02WuwrqHrXNGQcOUrmYDdG61ZR8I+ciXvct7Y0hUvRFVmTZnf+vbO0liyxUeEOQx6bqZ4mhmVFY+rSEGDVpamfKJ2LGun22Cb17i3jcgypGCFWlEVmIMh3i+8rcyFA8nD1YES9+vT+h5dewklG9Mee3ZlCpNZeuUOObPC4ZhDeZaiSMyNtlkXMex3KRRLfttT3JYM3OZO9EeFDpqi1Zf3mFDR7QYz94qgZGskXWvGOevC/EYiB1RyxiZboSwWNnupqCLZa1eacSdhbi+SMNTqh05P0Z7xh/2WQwnX2VzVdVqQ02EwneWYI0c5MVaKZlabQ3xrp+11OVJbvxgTUzsFGnTbF/sBlfpun40m6sWYjgVHV9oR1Cm/RNCYIre+POj1DtVvyllw2yWNIdv6ouj7ZXyhlTIyiURfSv3Ax2l2OYu+LPuIDR9XS7rfUd5Zl9r0HJ+rDcMvqz15P0TwPe3JypuaMnYwoVk14505gImdD9umRKplesrvrmHBk1VPza514Akz76sRvqxvXWu28WEgLHQTE63ZpXxorNwAud4r22UH1xFxN7I3+z4Ix7FfayhFDj6txmGZesQVNsm4Ne7XcRqUo4dY7WlZkcIV6ri622Ur+wI5l+FeuF05sVDkZvgN5SuSFHaQSZ4jlA4yeSoDvj3t8EOoJkflqt5ioZKaIQy5oJeQ09Rg/mnqWs1dnr0oGqGtEiN3S4a647Q818nVJ+/TbioLLKRNSx0ytD6WZY+Y2B1Fd23vQ229hmgW6qtTk+LTbQlFJcmrNYtNO9uQcIiwRdj2TH5cVddkme+SlcQVpNbz7V2nd2Lcl6N2CVy1HMr7iYxSdz/0NzTCwTxBj7qwuR/4w5UUssNQIaWVXbLp7p5tBscz22OnRjGKWA2nDswILRbEd3ktG7bn0OEIRe1hkK5lmzsnyBN5ljkpZ/VKtqTiukvjnExxKq02wUGf2rLJjqx12gl75MrbLH9e8wMuHJbqUe7ZS5jL3lKMUJP0T0W18xApbm9X57SFrveVadvh8lS6iVZS8kngCE+NFHm5EadiuAMaZS5IW6uOKIo8c6yVYBIRxJZO0Co0aj49VT1JWcrmFmkbf2Ve7A0jB+htKWY39eoYaNQOzVXkOtk6GFx2uvDaXqLMXVlCGnrVzBu9B7OD2avXaxxlLTg0WJ2cOnnGVox6Vi+Jft7SrbO3PakeCmvgNnh3G7XBYu+bwJZ3KD46MiHWaavr6nBWd/FA4FLVLc906FcZalg6uir8W7Zi4I1/PFZkFYXDJG98pseFQiRIEq5YEXMdvtldoTCnNBhvomvUrMMLp6y3q31YB3KN4WxoZlbSIAEc2yI+bM67XJIprDX4/H7DEUPyr5TbZpdxjQUr2xCcaOpC/YYy5NHU1iiK911QEYfB7vRtj5XQGXF09A5OF+CgDJG9MOkZYKt4s6oYc6U3rC21RlzBULXasomsOHh20Aa3pUbSa9MYy85UUYqCVOxUfup4+kZBXUwkYohdNNmOe227W2n+BZ8icGiAtVtqoWG8ptpDu3GUGF3X+qr0LphiIZi4XBued9neFH5gIYXwQaE7qNM5TJpdO5JUUFoVxFAfGkfzad/MGRky3fiK5C3SwbBzH4dus+Qkq8xPaV+cWxzdkFKoHXdqKdV5n0LUJoqyno4HpZVWyLoOb+usvSwBgAVZp5jrdFsSR1KARH2Ir8upuW6CKaru4AAEjZq/L6nxdDP2NeMKpGkjdmO2NMEXk+hmSA3XxT1O0eO+NrdqvBOEu5byiX9pI7UPwZiMh8d4t6S2AMpVGZwvTPHgSiR3ORw0bCdXaQ+r5j5mqyM0rqS4a4IrZtm2tgPjsc+s2NK6RU69aiQwafljfTcr0rDxdbhCGYV2dWwp7PfVkacybc0CAtyTjW5Cvp5oabpZKkeAF+0WYTMNV1oRUqVYEdnUtpBuPJHlEkn3/NXnw51RjggPDtlghmvFc2OPSFLbSmobh3wpgmOQRWd3t5+EHdkZ4Mx25pUzkqkHzObp2MF1pR2qPPeF7Dqpxn5VCuaVd66kyYFx5cDr1IZZ9/bKPqr+hmKLjWZIgo+kVBUF2IkrDzKReIJ+TizrwF4Fe4tUBids6APqOUO6JWRIMlMLubseenMP9zKP4imXUF6DHdaBhot0XGIuTjS9fIP0MrtsrDO7j1WOT2hcWquUgPYynzn+AHmQc8f2wyjB5FnEi2uiiKHXwtiBtHXvioe9uK43zhjnWjrYIqpu0/YyrS11B9ppdUNp+LzE6g5NHI0867eppvueiMCRV9/CUm3lKlkoXWOUmjcszZ3gtCs2bb1luZPXvUfuubQz6aDSD1rrYngNpK66CdsEl8IFUA2f6DpP/eAY9Xq10xSKKGzSBTNKgXTsVm2zbH0bbzCeamPnXnzGvqBGQ4ARH1lb6LqgCWbnwMaRNOJuSx5VW2J0vCvs0Vs65eaq4HZV1QrmQuIeSqu1Ym4wIoQayURFcDBn7RZC8e26N5WROBEMnMC+u4rwZSwmaFXWBhqXAjQa7AbAnjZWTU6o6iqNcsNBrMD12PxskE7tDraBKiUG8AshlZ6sI/l45/z7wVa1MIvhfFo3d8elMlWC6tsGvuuUXvgCRJXWOWOolFkTWeYIZSBGsqBfjifsfBW2Ze+upa6ywAywZYYEjfMmzIlVYJ9ZKxBFthv9lBqZMbshm1FbM9r1Di/DDsyU4ZVcQvh22dKF6aNYiQ0lcgdkpvTnOtvCDWfVa+cekO0JS+FofRAMJj1rMIFTZdhb0t2us/qerhGS9+nqeFhTRrlc6kdkCZ+0yyZPzxYo45WrOPWWP6xj2r4EyVIBYLvze8fEJ+SuckeKov72t5cPL98e3r38z16gmx8R/T97UvV8qPTlDZnHI0rPcj89dH36H9r3y4eX2omAdc/ndE3aBe8Psv7hKd3Hv/TkcRY1Pt9W+/Jk+/kaQGsF84veL1Hudk1bj29NkT7enAE7vpoInHTA798/ff2De4/vz/dfvPqtLd6eTyy9l/nNzfnVGM+Nvn0N3h9mfnhx39/Gelvj2JtXl7P37+9dAKfXr/ArCPJ/AjIt4dObLwAA -->
