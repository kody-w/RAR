---
name: "rar-cowork-cookbook-teams-update-define-queues-and-teams"
description: "Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_queues_and_teams", "rar_sha256": "d4c7d73d50d3c176afcbf116894222f870e75ebb8a6b31998a17eb3ddc09f9f0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_queues_and_teams_agent.py` and in the RCI capsule.

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

Define queues and teams Teams Channel Update — Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 d4c7d73d50d3c176…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_queues_and_teams_agent.py` first:

```bash
python3 teams_update_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_queues_and_teams_agent.py   # or on stdin
python3 teams_update_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Teams Channel Update — Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_queues_and_teams',
    "version": '3.0.3',
    "display_name": 'Define queues and teams Teams Channel Update',
    "description": 'Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '662875b2de9feb84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define queues and teams. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-queues-and-teams-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define queues and teams, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons', 'example_request': "Draft a Teams update on define queues and teams for USMF with an Adaptive Card — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to report against (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on define queues and teams status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineQueuesAndTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineQueuesAndTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWJbnV9G8jpjMbGwjseOOjhgkQAghhACBpHSFk33fd7Lru89FenZmVmX1VE3MXyOHnyS49+znd87R5dc3q2vDon77/KZ5Vr7aW2kahV69snJ3tSuGok7AW5HY4P/KKfK2juyuLerm7cOb6zVOHZVtVOTL9i7LrDqavWbVht7K6eray9tV01qttyr8lev5Ue6tqs7rwJKFfOtZWbPy6yJbsVNuZZHTrFACX/H/U9udVn4BhFgFUe/lq9QLrHQFyEXt9NzaWP3CZyhWVt1GvuW0zWewGgiQuMWQr/QnaSe08txLV2XRtM9tQEHGtYDEvbfaWbW7ErWzvBqiNlwdlcNLqqqLnOQjoAjUWgFd2yJflPVGKytTr3n7/PNfPrxF4PPb51/fnNRqwKW3J79r6QJd2aeel6eaTO4+74D9qZUHYGE5AWvn4Hvp1UDDDFwChlm9f/ux8VL/w+rf/z0ZrDpofvr8JV+9v768Lf/ULn9aty2spvXclWOVlh2lwCyfVkw6WFOzqr22q3OgCzB9HeXBp9fO3ygV5eo/l3s/vph8Crz2xy9vBRDBWnT+8vbTCpj+y1vdLZ8/LVTKH3/6lBaDV//40290ms6OPaddiAGpP319//5OFiz8bWnkr75qCrd751V7TlR6gPjv9FteL9Hfyb2b5Otr8Y9F+WH155QXff4TyPsKRxvQ/XOywAZg59unuIjyH9951AUILyt3vB9/+kdkndBzkjRq2n+K7s8vwqFnucBa7yb56cPTfX9ZQe+6faf5j9mWIGD+FU3A8m/svhvqH9F+evZvSKcgaJvvvvxTcn+2AfrP1c//ULf/bsOHlf/ljfVSkIq1Zafe59WvzxD5+Qf3t4s//OWvgPT/kYxWdLXzpPA1s/LI95r269eff2iel3/4y88/dCWIYpCIX7s6/TOaf2bXJ58/WPB91Y9/3Av4X/MkX1Dnew6tfi3K/1H/9dPKsNLI/e06AKnfZ+LyglaLEt+Yvkzwu2xsgKy/s+NPb38F4JMDbbonQC3Y82//tjpFTl00hd+uNKfo2hVwcBtl3iK8HkbNKnphcu0BuzYRMOz7OhD/i4cXiQFC//K/nCfgf3TeAR9+IvTX7olrX18A/vUF4F8BVH593v7l00oHtIs6CqIcoLTKKMqX3AoW8Ad8y9prvLoHWGVPrfcRpPTH5cMqyle//DPkvz4pfSqnX57oHL3wT90dFuxrutT7tGhphqBKvHRyAMh7o+d0gElaOEAiPwK4/QFo3xQpAP52sUiTRGm6ciOALqCavYoKsNrnhdgvv/xiW034JX+BNbp6lbkGBgu+i7P6+BGo5qdRELZfcs8Ji9UPv/71h9V/rf67XU/iCw8F1I13nwAJn2UI5FiXgWXAXcDBAECePvn1r+8GBmRyUJeBByM/ei+yIEYTz/1mbU1gPiI4sbI9YGVg4awsQHHMg1XUflod/NV3eQHT5dZSI8KlNLpe6eWulzsToGoBdb5bMi9ABQeB2PjTh1XXeE+uv9i19RQxA8lutb+sTjsFVKQiBX8WMV/138qLPALm/x4Lr+uASP1Ds9p+I/FpJS9RuSqt2irD2nrnsZT0xS9LE/C+HRC3Vrk3fMmX6ustpnqmyMs8YBGwjPPu0o+Lz0G/AlqS3G2+8X6usZa6qT/rZ/0lb97D36oXVzigHACmQRe5S1H4j/eQasKiS92n/YCkC6V3L7jvXnnGIPsPGpxXL7J770VeTcLqS4esN9jq/+emabEJs9+r3J7ROXbFybp6f/lq6SMXNV+t5yLeIvczL39raL6B1jfs/pKnEQi8evqP18qnh9/XvPCwq4FDVEZ90gfhBXy10H1G/xLNdb3kjfUl/1YkPgDtn4gIhAZQAVJpieBvDJe73yQNAR4s339rGJ7RUi/WWfJvVXZ2CqLP9zzXtpwESFUvGfzuZpAKT3cOYeSEf9Bq8Q+IOEB/BYSIQE4CT3z6Dtyvu99E/8PGV1+0bHn2jB1I4PpJAMjhLQIuflm8BMRrX2070PPzkwhQIyvbRXcbpBDQ9HXRqz3gyCZqF7h82dUrAVx/XN5fmi5XvbEEWQOMBXKj7IB1n9m0AE0Guh4gAwhbkFxZlIMuABjl3QhPgla2QAOA3vc29UXxefldIe+Zgkv5+rZxUWTZs3QEr8i38un3CKL/WZgAetmy4sn3byPtO7eF9oKiDUBCwPHb3Vfr8OlV/V/txeob3c9/Nxf9+K+NTs96fv1jAHxehW1bNp9h+FWDv5XgTwDD4Jeszascf3zVy48vaPj4goaPgOfH5+0/0H6p/Xn1r8n3BxLv+fF5tfm0/rRebknv8fX+AubYfdzeP2LL3S+56v2GsoB9kYEAW5w3gfr/vSR+WwLqYlADmAKLXyWyWSrrAIr5syYAT3zJfx/wS8It+BQsAdoUvwOCZ28Agv/luO+lC9zKW8DbXTrKwPu0DGKL+I339jnv0vTDG4BQ758a4JYClS1x3SyDH8gg0KK1kff8BhLU/brI8aL269+Mxudnnqy+LfgeZX8Pqx9W3qfg0+qfcfRHZI0QH9f4RwT7uPD/FDegFgJB26lcNHpNf0u/+ASxsf0TuZ4frPTTivUAYKbN7zPjvegtRf93CfxyAjC+A/T/sFoEbJYiDXRbTLMkv9WAbAIq/qksz6L09VWU/l4gdqlkf6hbS0fxbFZAG/DM99WPi4U+rK7aif/pT1l8753/nr4J2pWFpFt8Xir3h3cgBO9g3vmw+j66AMXeh8mFg5d3YE7/eRmbljh4blk+gD3g7fum77+I2N7bX/5OLiDYE11BjVpo/Sbkb0uL57i1qABIt69fB359AzFnATNb71H33q+D5QCMPjZLfwKD1ATMwfdXEoF7/1ed/DuNJrRAF7n8MIE5pEuiLr52UWdDEpbv2P5mQ1A0hiCIT5Frj8Q926YswkY3NE1ZG9KzUdd11rRP+4tMr3T8ujRi0SIXTpP+mqYRH9sgaxfIgWCuSxEU4eAksrZo28JtnLbs37YmUe6+K/tSbrHk96FiMcq7zr++2QQGVgpYc2Berx1Mb2z4JtmTKMD5mhrDzcWd7hdO8GAB92LMym4i2osuqRgPNNm0R23EdswsmneOcYPt4ZFq1ZQoyc4/JdDtpjCMylzFo2uzpPkwmuQkK/oah2AyTPE8drDr1LlHhY+ra2Xs8JQr0u2UYS0KK3CpRpYYNSZqahdJ9MmpnCGJQo9kerVhzjpLsSqG1n087kruJu+2buQFh+FhiC0kNikVtWyujMjD9aOtD3s3ktCqUTsQ6p2YOiPio/ahjYweOmRe1tJxU+fn8KbxQpEO09G/z5d7d5g1glLHvV50zXzpPbE8jVySNIPIjVayTvzYpxDai5DWtU863N/SsvOrcXMWUn6rbrIiTE1VLZOA2osbGoZ9G99Mfp+XkIgTsN/7qMdDdJEgqbbePVLTHLULNagbytjfEeQxWeaZeGQIF2Vzz7KBNbJ1+eAzmrqcb+f0blxPQ8FM0roKDz27wSfokoZ7617vcIqyD8zdPK21225I76lX2dP9fnZvU6dzjjjtUzx0S8WYaMmOnEmZ2Ruq6Ew1TpF6HapgkDXtYR3YHNclszCCktc2qcdk3mXHR7T2KIesotAuHNZ0oRDOrYmkO8OQNRNDPScMswcCvemwOt/EWlOzMs9tNCorgil66CFhbrec2SWsK8mXrcWvDYaX4zDfd1s4G801YV0bWXoUwlTFhbRx+Knyz0JW2VLt6F6S2zjnVQH02AXN4aghUn1QLyhxnSRUm8I+5UaGPrXGNqvGszxOQg96SVHSLx02Rs5l7Q1RX5UIVuwuc7MNq1HgFGp9i4jwrj/mzJu503A2gmrfyta+M+6smQb2kKQIWaVOtK75s5SfR83mLVp/KNp4qiaeODgwVhyrcnYepVdCd02hJRCzhLi2s90ZHWS4v+yDyDuiGp/I0Yxtzmq8Viak9vc4slX5tKHzBmfyMCM8gbDtzLyuc3Kv6+vuzG1ONkPckW0yjbio+vI6tyUH5kdUuJXnrXPXcIjU4UmABJnEB7rTqcvo5WvE9/UZ5ieKt1peHU9JvAmI20XypqNLOuokwtKFOM6HB21eLkfytq24QwBz6qWJaZvxlGHfNFpY3OUjYsOHcrcW69PpStlkQtqHa4dCxVEVuex4PaQ37b5PD9Qlb7C7p1z06KJur3GIcViVYXuXyXp2dgZ+R3X+7jRLh7KZFTauEdG/01jVbxFIvBmzrWpxahzu26tmHq6cEXFbhKkx2mVUxzok55LeZiJtzNPZfZCCs3WvkYCfGiusj1Hrq/Cc5TFSS5v6gbcjnaLujbpU+DxL2J2ILtXd9MgDR8ds0bORGnTTOGhTf2LWusDpaJkxk0FbVeX2hTMZ6726Te4by4u4Qwkd223Lo7Qz+L5DOPnhfDgDpcwJA7nE7yX6PN9JZFOGugPj8VFLjG1hmL1Ac9EeeWBcsgl2J9Rj0quTGPZNVs0kSpIwUjmoYnM0dROyPqezYBS+u50vKBWirfqYVb+/OYV0CFD0SJMsCe0EMVYCMmaUwTj7zRZmjyMySmY48lmWWNJJ4dMwPBdXKSydQLoZjaXhknD1rlvtHBvYrVdE0xVOoz2TpnllHE0R6FyLb4+eVGJm3Dwutkm5aIDVvbSNA2ET70ZZZ5R+J9ey9jCoIB66zaz3h8eeSimWJlDggC50i3BfnM8Fup33znRETlXD+hSOF4R469ZDPDDH7G6wUaNGclBN+4jcdHay67it1uCKelP60L2rh3mK9QuCJN1xPz+ussyekP2Rk/fS7PW3KTfpMcdkSQvEynSTkzO4hJgizoWO92GJnZtjHq6d/SSFTTlwl0CgSgrn4l3K4MgFFCoTdkSbrcR76E6czRluTYvHm2M4qUMmHhWeUy0KbEJgb0jf3Cr8waL5TmhrHjayclqT2Q6NXTaJCVYhUafXAYYr+UZhTpd6a0ynPRkT8jFxIEjj5XW33oYqRoYyKpr6zYMnXthIbYtwHFmW263v5ylGw9Rm9KURFwgSNyy4e8yPjdslqS9YDxIvTEa6JBFrn3J0cNbS3vOOhwo0jTf1PhbRgaJOg8DJcntb77F90d2Cs4JRCFIy2mNLqXiwGfY5fV3XDPm4YnpzvBtNNl6Ly+WShdoRFCmm2K8nyZXrw7bo9xeuoFTKlnOx2yO7CEAgLxhu0+i5e9RvclpnjLGeVV2KlFMMoD1oDVkO3Sti6vdIr1n4sY1SXCBlVXSESzOZ5lwYF6hnsaYvRIMtlSyNM8WiG/RiZ+TBuyang31NNUi5Pur9MOVGhBwOgptAm2OEd2F4Nxu+CuqBrVVsz4u3B+sifedGUnc47kVchWMICZrL3ih0J58EleWO+cmzPa2qdjPEbyaPOd+NgJfs/ggnx0m9HJPd4B15+ZaMbLZP+CBlDlc3mS/u5v5w1TSymD0qthfx1Bvo+WHCEupNzOEORufdvKn0GdtefGBYXOHry14fr4026aejXAxOrj2E7hSu2TNO3R6Wqp+sdthwkxMOEbvjOuQuXHm6v2axnkGDbY7BUeGwOxTAEhncokL0K/V+Dba5hm5JMR0eQU9TZpHtp8PVTqGx9nT+7BFGaUlFtRdDs+cLc6f3LhvcWU5E5xvfhAiAwsCEODSzyqNzmb1c3emDXV0AAOoGkV7VrN4g+XhIzJOfYScisrLH1hzzeddfxrC5BZftMe2vXCTb7ihD2SFor+Hw2AgBnPbkhRPpfaHsAgFz+gpL7lcB5cpqHo1zmqJD94gEBA8vUl1RzRpJkP4xzcHAYKjbdtB5y3XF9RIYm9udJu86UV3QczIh52CfYsosU/RJmgcS5RPqQM/9vkSyHVF19LaXxoRtLHlf6WpFmmGSRJ3pHLfHpGRylDjyidGQatrfg4J1OItWjUJrr+j9oaBbauCNm8xaFyauUDZLYjR0qKMpdxFkaTrlGVB7WJ+P69iWHboJAszZEqlUPvbsoB5peRRyce/yGNxbcrPlWHPy8tiMKXl8sMUW24twRqHlWPfuxd2umfMuModajCqjLOCp8S9CPGY10u7WbO7IiAD7KGSGnWmyMpISeMpLkoLSimWr4vqxVg64fzqkBl4cGfGgNFs0nfqNdiGIFO73zlW1iutY1DtvV95uTMhF2uaQnTl5RwTdOXSPZfMojzw1DMme0A6B0cSixctnWDZjL/UE2nO5owC3EeYlbZfHKgbBOUsS977GqClrJyYSZEgZdhZ8Eu3s5N/47G5CMznohUFIu8uNaBDkiPjMMWF3e9CesxtMg/bmwZlxWlUSOE31uA9KO7i7m0zZZCfb5m/F7txx0MjOuFiSD1PkTHw62BTt92pMpoxTq5PwQKzasireMMgzULfGtMZKL9B4YdV5Xzn3x26+EhS20UZ3a8BjQm3g7Mqfu/uUlB0uCoEkRFnFyfhOyx7WTF7rab+xiUegTCVL5XNV1BLVgDZ1u+ukQUrbzVXUNDuMCX7c0tTOQmZYrY8Np0azk9kkaLY6Y3fqYQ5TdMXji+bmNMQZtvOdKpV8Vcvew3i05+kYHzxznxuPviqkUlb6i1nwIj+L/H4d6faU4dJIKhWhVueq1LVOOifjieUNzuKnXo7Om73HqDM3JHJc0Jq970FXdkhsiXrsvTW809Hb5qDko8xVmrm5qneaceZoH6DUURHX+sPE72CyIjWCr+8Fnmrq1Tsld/8q3+9pfrQ46DjszFPNyae2ce+ysR+jFtsJt6Bm0yurRwh1RCY0h3jeDcZOKtM1JBr5UbhXYSYyXlxLySnYiF63IYWINrPtzSgsRvQcRWRb+LIJ49KKuctI2iSMIVBEj2AAFOVwDq7xvqGxKZzHlkTPHSnZKRxQxd4cT6oSswBzymlvrYO8vG7vlXNEtienlsPYifCamhBzXufUtmHq67X0xsBUy4B4VPZ1jzDz7FHIFUxc9YDL0RpZ67BszEfDKBBWdNQmaLCpaKJ+JlSfhWKDzyyudaAeIvttjtJQutvhKn2sGKYSI/iW5gaHh6bdWbRhnPmTh0TRRk2FY1g0zUl0h8OQa15578SGe5idKgm+crdyh7k4m3Z2e32gvMSkd+V13dTu7YAjlQKx92vPG2MDoY/jjblrdSe758qhpdyEmL1QwlrkEqjSGeG+Yzb72658QPKlRkbUS7SrZvf2eX2m7fJgDQixS1VQosY7ZuYiTsVlKmkStB9pqXVrgPzCSc3nWQGjzZwkKm76d4s9TdBVuXDGVhLdc6paqRvg7M0PHScPuF0FRtbUZmpWJYlMVSqF8N3bUVOVMWuP0OXm5rWnYgWyEylg/Z7sQpMUeyS/WocZcte9b2wKHO82rcR6m8BmC8xAdK/l6oHAq7bU6ao/D+5mthQugm1JvbkZgUbdiRTGOu6UaCwIhaJtcSQ3HlGuCfcyPdwNkVAndctAxtGbtjPCl/QJOp8Ns7SzlnRbkaZv+gHlaEf3jWE9ZQMcY49i77ldwHYmpKObHbdFgWHXZL57CDQRPMrk0FXRnm/Xos71BS5OEJGnrujzCAhZp/FOnEqlm7Av9jkf4x3qcdfmJGAoneatnSMNSdziAClKGPLPPsW7jSFOKtHNNx/r4Nhks6De1nyKexqpnPfrvZyfNxp5iaF4HlA+iLn7oO4EZFIyFgr9YKL14qxWKOhptbB9HMCEx2K7Sd8/es+TfVfM5bBCyy4zcj2Br9KezhDFZ+NCMTc8EZADQPmSPjuYPQuCdnDsZg+aLpJ0xWOGNwyYF3PVQh+77YNlYljZ4Cj6MG66d6BaO+IHeLdGpgcrFYWTzKq313Qw2ojRWnPpDW2tFc3oTx50jLA77WtlJaibY9zaN81KIbNH7zZQoEAVmtMu7DW6KEJO1rHdTQ10su+VyKzlhxWT24jos0stB7O1WZOSRp1DsxYMrRxoxpJJN1JJH70bN4J/6AOYTU+kB2HtlR/dmh1Cu2ZiozxEvJFoEbVXCRMumt26ii/HbR7zJ52GCaywgrw616Sf9Ne1XzyEYeNUNgPAPdT9iWhMoQmPlGVeEweh8BA7j+Jm1/fsnWtUqC7BXADKMgbTOer7FQvarAvnVzkAAoPkhkHtVTxyTaXODgouqJh5M+QQLpuzYZlHKRRnbIKoBGfO1z7wyjOCyqiKHlQ7EnN1YsOmeyQuEa1v+vHc1eLgFTN2Ger5ATmxu+MLPztnsYQf7xubDjh7q45q6rmMh1lbmZDPlFQdezYMjtjseKZLZhBChcKhl+07HAXsLGSuZcm0SELeeh937SYHyfyAGTkzD4UXjjlnh8RZSivhJqH9qWdKJlT8Eu1AR2bKd0bJYnh9rpINLz/YwUPPpyIkRCK76lVANAHJFGjDeHe6Jys2fkCn44aeUdHTkd6rpHS+5aZ4zfVmmDE4l+sUPcr2Uawe8wB1J1RWslvhojybediMWOdBPNARgnZNfe4kCCLQjqiZYMvVaAGaTPzml87NkBwoJyqclehDGe+qYavTinOz1fZ2sNvWqtmIF9jWeYgFYbE1jrNjksd4LuR1v1UF3nBtP8ZEngqTXSka96gR1zlIaaMbq/V+sOKmRGzT16IIkn12eyWZNjtgYkqzV0ulGWG4hyeEfxDpJWahHc/WFSw2zAVbO8Q1duRmjk0xIfg12g8qL6xLOm5u3A5OMpzQCPVm0lovrwUNOcdN3KkVcphgJOqxjNwJ3RRmA9uSdoV3O0e99tcT4iKMAJVHutHvA6omKpnU21KFfMHN/Rzv2/0m9bNroehheSZbqcGgtXKRNbJaGxhoaOzKwBy6W9e6GktnqAHrY8NC55C6lKVpDnO8dhxE9YWyfVgbVn+c7LgvzO1gr6E1Yjleg6FcAwbeDW9nRWA7JAc7iRpuRFa8+rE9SHiL7btzIONeo8daPoGBKC28BJNQ/cALKuhCiJwKWtQMH5dbuLfHedonThnf43jTPyDDzksptHXY5TJdIWZ1UzkneKwNzHM6yjs3yt5fVw/DQazDdJzHbclA0XYedl7DbgsXVnq0h0VIpzY0VKyLLlcRZiputX5mAmSNplDhEPREo6eCnDTKTU9CPKEVTnbCJb/21oA3wlG5pzctOt+R4tCUmxC7W+rB7IuI4OdWT2HLtwu+vN4aP9tOZu0WuH3rk3w8nYRe24LOl7kfkzmxb54DjYHc1g3kYbwtgOaL5QILx02OOzQ8Ma71i3JAaHPYDoRsB6MmPMoWoZqrUxXYoJh+EJSOcvP2GE6QpWuvGXgbV5Z0twgV5seLb3q8T4BoKTss6ntbgPOHQW/kCmJR6wxvWoH0bZLK9U6r6T0seyxC3dA+SPwYT067smwoon0gk2nsRkNw2+0dtfy7v61rUm/uBBJDAKLNUa/PlnuRfBYG3TxukrHZkpwusT0nUcisNYKKz5fzdOvnibl7xKkGfVy+rm/VkUylioZGQz7c75QOHaL+kHDbiu9xmcN0mzE4zEq6oB+w3rL1YHBurrPBNtiRZ7ez0D9Y5eEyyGG/YdaOwCbwQeXk/DTXaBJ3+4hBazp2UySUe5SEixux3ocjHGd5vl9+6pEoNNS6u6Kt1ap3J4jtNlJ2mSQHS7Cjqwr6XOwQYVt0bNdZIXTzfQzF5N0WxXbjuR8ayQch6KoHTs9yCkKBNSiSHlHMEL2Kz9MSFi4wtGsfJ9yIqQvDMG8f3n47kXz7lx61Wk5f/p8dAr3Oa749NvE8R/Ms9/OT1+d/Tay/fHirnQgI9TrwatIueD8a+pvjro//zAHqQmF6PcX07YD0dSTcWsHymO9blLtd09bT16ZInw9PgB121yzPBTbLo6MAfprfHwj+XpnlYNBqvK9t8fX53Nm3/VG+PBnhudFrzfI1eD8I/PDmvj/Q8xUl8K9eXS4Kv5+/Az3RT+tP6Ntf/zdm+Mussi0AAA== -->
