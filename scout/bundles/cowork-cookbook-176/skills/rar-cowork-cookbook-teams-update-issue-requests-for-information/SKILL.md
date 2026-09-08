---
name: "rar-cowork-cookbook-teams-update-issue-requests-for-information"
description: "Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_requests_for_information", "rar_sha256": "e8740e59b3081f7cc7e183ee9c7f367287b11956501ffa6b8b668dbf33ac893f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_issue_requests_for_information`. The original RAPP
agent is preserved byte-for-byte in `teams_update_issue_requests_for_information_agent.py` and in the RCI capsule.

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

Issue requests for information Teams Channel Update — Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the summary, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 e8740e59b3081f7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_requests_for_information_agent.py` first:

```bash
python3 teams_update_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_issue_requests_for_information_agent.py   # or on stdin
python3 teams_update_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Teams Channel Update — Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_issue_requests_for_information',
    "version": '3.0.3',
    "display_name": 'Issue requests for information Teams Channel Update',
    "description": 'Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-issue-requests-for-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad422a5956ee3307',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-information'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-issue-requests-for-information', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the summary, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of issue requests for information. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-issue-requests-for-information-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue requests for information, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.', 'example_request': 'Summarize issue requests for information in USMF and draft a Teams post plus an Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update and Adaptive Card on issue request for information status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateIssueRequestsForInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIssueRequestsForInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateIssueRequestsForInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2H5mXSUKQFRXRDEIgBEiAkITTkWaeBzEjt/97H6R7M9NVrur26/7UcjglwTl73muvc9FvL3bXRmX98ulF9+1isbWzLI78emEX3oIth7JOwVuZOuD/hVsWbR07XVvWzcuHF89v3Dqu2rgs5u1dntt1fPebRRv5C7era79oF01rt/6iDBZx03T+ovZvnd+0zSIo60VcgH9zexawCOoyX3BTYeex2yxwYrXg/7vOyo919iKMe79YZH5oZwsgNW6nh4GN3QN19sKr7aBdGL6dNws3sovCzxZV2bSLKuvA/WJBezaws/cXrF17i52uKosgzvyH9NrvY3/426Io2yguQmDoY6/vvQIf/dHOq8xvXj79/MuHlxh8fvn024ub2Q249PLQeKo84KI4u6e9eceXtfjNNyAms4sQrK8mEOv5e+XX821wyfODxdu3Hxs/Cz4s/vM/08Guw+anT5+Lxdvr88v8n9YVj9i2pT3bt3DtynbiDETjdUFngz01wJm2q4s5Jg1IVRG+Pnd+k1RWi7/P9358KnkN/fbHzy8lMOFh6+eXnxYgJp9f6m7+/DpLqX786TUrB7/+8advcprOSXy3nYUBq1+/vH1/EwsWflsaB4sv+mHDvumqfTeufCD8O//m19P0N3FvIfnyXPxjWX1Y/Lnk2Z+/A3ufxegAuX8uFsQA7Hx5Tcq4+PFNR12CqrIL1//xp38l1o18N83ipv0/kvvzU3Dk2x6I1ltIfvrwSN8vC+jNt68y/7XaChTMX/EELH9X9zVQ/0r2I7P/IDqLC9BI77n8U3F/tgH6++Lnf+nbv9vwYRF8fuH8DLRkbTuZ/2nx26NEfv7B+3bxh19+B6L/t2L0sqvdh4QvuV3EAWjAL19+/qF5XP7hl59/6CpQxaBTv3R19mcy/yyuDz1/iODbqh//uBfoPxVpUQ7F4msPLX4rq/9W//66MO0s9r5dbz4tvu/E+QUtZifelT5D8F03NsDW7+L408vvAIMK4E3nPm4D/PiP/1jIsVuXTQkQUHfLrl2ABLdx7s/GGxFAs/iJyADn/LqJQWDf1oH6nzM8Wwzw+df/4T7g/qP7BvdwO6Pbl+4Bb18e8P3lHb6/gOb88h18//q6MICKso7DuAAYrdGHw+fCDucJMONp7Td+3QPIcqbW/wi2fZw/gAGw+PUvaPnyEPhaTb8+0D9+oqHGijMSNl3mv84+nyMwKp4eugD6/dF3O6ArK11g2Iz6zQcQi6bMwDho5/g0aZxlCy8GWAMm23OygBh+moX9+uuvjt1En4sndOOL58hrYLDgqzmLjx+Bh0EWh1H7ufDdqFz88NvvPyz+5+Lf7XoIn3UcwDB5yxCw8DGcQMd1OVgGkgfSDeDkkaHffn+LMxBTgBkN8hkH8dvABRWb+t570HWB/oitiIXjg+iBQOdVWbeP6da+LsRg8dVeoHS+NU+MaJ6Ynl/5hecX7gSk2sCdr5EE8xEM3DZugunDomv8h9Zfndp+mJiD1rfbXxcyewDzqczAP7OZTy5gF2URg/B/LYnndSCk/qFZMO8iXhfKXKOLyq7tKqrtNx2B/czLzATetgPh9qLwh8/FPJL9OVSPCnmGBywCkXHfUvrxMendEtCTwmvedT/W2PMUNR7TtP5cNG/NYNdzKlwwHIDSsIu9eUT87a2kmqjsMu8RP2DpLOktC95bVh41KP57svNkKuwbU3kSiMXnDkPQ5eL/Qx41R4TebrXNljY23GKjGNr1mamZUc7ePUnobM4s6dGV38jNO4C94/jnIotB2dXT354rHxa8rXliY1eDdGi09pAPigtk6hGnufbnWq7ruWvsz8X7wPgAnH+gI4ggAArQSHP9viuc775bGgE0mL9/Iw+PWgHRAIEE9b2oOicDtRf4vufYbgqsquf+fcsuaIRHFocodqM/eDXnA9QbkL8ARsQgtWCovH4F8efdd9P/sPHJkeYtD/7YgfatHwKAHf5s4JziIW4Bitntk8ADPz89hAA38qqdfXdA/QBPnxf9ub7iJm5nsHzG1a8AZn+c35+ezlf9sQI9A4IFOqPqQHQfvTQnPwcMCNgA4AS0Vh4XgBGAoLwF4SHQzmdgAMD7RlmfEh+X3xzyHw04j7L3jbMj856ZHTwr3S6m7/HD+LMyAfLyecVD7z9W2ldts+wZQxuAg7n/9e6TRrw+mcCTaize5X76pxPSj3/tEPWY7ac/FsCnRdS2VfMJhp/z+H0cvwIEg5+2Ns/R/PE5ND8+EOHjOyI8put3iPAHFU/vPy3+mpl/EPHWJp8W6Cvyisy39m9l9vYCUWE/MtePy/nu50Lzv0EtUF/OVs05nAAX+DoX35eA4RjWAJ3A4uecbObxOoCJ/hgMICGfi+/rfu67GajCuU6b8js8eBAE0APP/H2dX+BW0QLd3kwyQ38+4j26pPFfPhVdln14Acjp/5Wj3Tys8rnKm/lkCPoJkLc29h/fQLt6X2ZznkJ/+4cjs/romsX7gq81988o+2Hhv4avi7+Q9o8YghEfkdVHbPlxNuM1acB4BPa2UzX79zwezoTygWxj+yfmPT7Y2euC8wGKZs337fI2B2ce8F1XP1MCUuGCMHxYzHY289wGLs4RmhHBbtLH1PpTWx6T6ctzMv2zQdw8zv4wvABIP1Q9W/UxOae3WJ10mf9THV/Z9T8rOAMKM8v0yk/zNP/wBo/gHZyIPiy+Hm6AZ2/HzcffCIoOnOR/ng9Wcz08tswfwB7w9nXT17+YOP7LL/9kFzDsgblgcs2yvhn5bWn5OJDNLgDR7fPvB7+9gNqzQZztt+p7Y/RgOYCoj83MWWDQqUA5+P7sKXDv/4brv4lqIhsQTCDLJ9dLxF9RDo6QaLB23bWPkrjvU+46wIk1Rq4dFKVWxApBg8AmHNIhCNJzAhy3XZLCAyDv2aRfZo4Wz+atqHWAUBQWLFEM8Tw/wJaeRxIk4a7WGGJTjr1yVpTtfNuaxoX35vPTxzmgX48dc2zeXP/txSGWYKWwbET6+WJhCnXg1d4ZKwEqEHKM0KM3XY8b3s0mqTUAid9JbpxeJrvyML24ROFJCfXN6hKxtHxlznfFOq90YYqEXIfWVUHTYtjtWzCbINW0pDOztQi/rwv0jt2LzlUuUWtI1bYWkDZjY+Vs6ysk7CG8aZlKbJd1Z1xii1UNTb7E2DTpkbaH4UMDj3y+wt3KhRHEOp2nEys3pImkkbHZcEh1OSqU4q387NwrYebeWk4cVxRkxiTUQPf07pJGeUPhG7Dc7tCEPpdELhYWI+7EOxWreh5fpKU0onV5llv9tAybfb+BNi4Z59o5FE+rVACFUlzwu3kbkXoXEXWyunlBttlt8xFxUzs57Fw+yLnBUfv+DnQH5zs1UUG883ocfF0ve7zdu4h0jvomHjD7tJY3DC6PXTmlSOMhd6VlTD6vmoTBdO48ofe8mzxMZOE+yhl6q1lZHe9GqJtO06nzbsog3QKOJwZpQ6J3wwo9J/dD0+ISZkygG77jkGWik4M6xLXlJ+14DrZYilEcvj8tI20XC5V4GiL2GI2hGmRya0dnNjX3Z3NJWytaPEvtLi9YrO5dQuAMLIQr0SM157jZKrxuX+LrEbv0dnFBL6Q32VFlolUes3HmGifd1qYiJc48t9nGBXaKfCfUJ+nCUnu5JFfIwMEYMYWGTkWKEseBnYi3vaFFhmjsEMg0LH8tBXi693YcpWeG6BxvSL0X9TBBA71Sjsc6mMpkubE2N3O/NmPXSVIhOIzq8bytvJGTiagkjzJx8zppKOX18XhtyhUNK8qy04+cuFZBBS3JO8Hr8l5Hd62Osi1nIyHjN3l7oU7VRm2dXaRtHU/qb+10bUmUYahUcsmTp50sbJ/Cx+muw4O4Rq/LirwWerEcqCA0MDL0pf1VOO3yYbk7uHd5ez/DzraC9obJp1ZCOJExjN7hQMoKru4lJTcrujfSRuVQBYPPRQZl6nA4Y8ugkPkOVlcQN+T5qLsaeefXMCLAoUpCjnyXYFfYJLl16CkICk2fS9fmuREOu13KZymxE829Z8QjPpT66h6W99vyunFrXN1cN8OWISMWUgr1Hm4vuaKdGj20fSO9RPoezXVzl6NLYIPAKcSNc2xdPBzFEPV2oX1KRikjuYtJxLLNiVJCHo7J5oRv0HKDLnftnb7U04oUJMsyldxaXj1/PKyFnD8tfXyQiC62gYzbKqCJ2Az7o25ewl252yal5Uelek317uQfCftw821N4ZvWO0kompCalqK7M7YlrAu2ud0u1o2zBhwy0/zSIP1KqUKqz447dLO7Ug2/K9H9bVqOl91167vqld5tpnFDEVYp58G5vhX1yoGGTlLkJE2idRnRUhjXR+eowJfOnkoNIVL6dLRvoKP30WiIrt0j+ChgWC3frAJqLP20uSqsRC0JujljxoFNtw3NHHg3P8mZgLVY3JatLBpkKjqieAh8SCzUYG9ftDIwmfuAU8kluuzuXhAIrLVfhgguwUuaxhkOlhsG9wXiGPtQaVBbfl3FW5SJV8pORA8FhLEMb1tGt2WWtLfTx5WTN602anI6TP35Ru6woqk4pj+Yrj1oqCgLdwrPq13f4kacEk25u/k+PLj8PQsY3CG0zFolG6VneUyZPJMMM/kirSo8dzcUvyTaiYITytA6VEwuxUa16VWcbLfNKJUIclB9W43NdSsfjrRYFcyRqDcOh3unYxMkJ6tLJa/hcyNdb0iI5PlokzSr7SoJMF0MI05QtrS6lfeCIomJjysE7EPMVVaPU7qDtyavcEeVPWHEUnTpBNsQgqMZV8LmLBPtTg2rIgXt7/au7vv5wG6Odoefg0GWDIm3MOakNZGH9qemSiPvbu47cx0zZ9OWOOx6OrQ2Mfr7rPCYnu/X7j5YS1rG1UpWsKsiEr08AMBN9vsWOzXSYZ2xe+UkRnW/Pvmno8RBme6UVKkwSZLQsGr3W+hOXs9Kiw7D2t5cr7KeWsFBGEoBhkfS8qTDpUaWYGndDmk9rK+Hg2IMmr2h6cA6xUdaIajUYQz+7KCAK7DyRoOLCNmsoqq6QcOdRs2JZE6JkGPojvXEzSjknMDsL+dWHdSSOWxctuBlpvVvjLzxjxXP5el9u09GRxOr1fHMl8iYCYMakXdXGRM+49UzJ/aVmiLJsITkKYHZrXxv+AyQNbHe3UvxVgBn3LO/FNB9IxfSSivsGjYgY7xafmsVZC2FrB3arMK4RJIXgknKxy7t8CO5Uq5hZO3N9Li720ZknqENKZ8PHHMOdif2foO2qYiqtSGF1ZFZSceyYWveAeeQAB2VkR4yZX8grzhiJbReAXBmz+slS5vnbKlI22BqVvCwOkkyv2LKhKdQk4xC88hE8qkurDbeNuLSuei0dZA980QbdKqq+H63kegDZugRtDXOOKSZ8P7uTzR7rG8Ve0e7YyVuj114RcggxK57ntifd9auEwRkyZTVKSPyK8QVDSHJHlvl/HWyY0c+DkeYmRS7q1sbwqXjqN1PS4WxhoxLyo11DwAD3O+ODRttGgnDhp3TkBtqsx8cwjZtMXI7YbPrV9fLsD7ieWnn4U7fHKfW31+7TUEshXDYivci7/aaBfiuQKtgeXM/9qMAKkacfE7RixO7FfpNnsiZ1SPQzoybhJQbSlPvm+y2TKhISL2OldBNyId9eqVkR8zU7VaMvTBuLJ5JAi8hjqRCntNNHMKEG8RTXoYMevKaKaoOmWlgjrXdYTvPlfYS1KVxggfaNIaiuj5wrtM2l/tS24ujIJruBastjFfbs8JlamOkdKUKPU52htuQKgWAquzOOzKP7XJQqlqkm0PnZEx5t6qVXHU5q+n+zaLTQ5kgkn9ostOoo/05BoRmI42aeGKMW3SV8vUAX1miLKNeEnh2YvOwG12F35qw7R+6LvWdIrCBDWxGY5ChCtejLIT2Uh9Mgyvlws+R+J62/kbELhUEbRItuapJ1mqqCjduyMja1s2FnFI9n79ZzYFmypOeM5ZsnjtFoNKxpf3D1u5tZK8xHeE0Bwr2d9vtyrrKuH6pcvdUNQOMUFW76d2ImaBgYC3PtfWS1bkVgO5jRCGN0lkGAUO+3KRsfkslIaMNEZUIfEPn+rnajMeovJzM+21fXRSO2wlmLe4YkACRd8TpHBlGfzdLvLpE8KXQ2AheX/vDBDhbNJB+kGQUKSQEKTbV3r0PUR+kA53eAcFYJgI+Dvnet2JX6iRq01xl5GwEksOe+AOTsTKjMA7AE7ctmUCpjhGC2ey0vvh62g0mPpXw5crzLara4nqzPtgryaHvOY5haxmv8bsUrS5cSo+te8ZQRL/1Zy9C3WDUxtuFI1BaE2S/mphUoYy1ot2ymFBKemvcr5B1PRGrSDLUdZv6x8aTnPIIpzswd+sDpU+iY05VxEimeD3RdjxORShik8c2+6tYKH23P+lmxDXbe2QOHHG34GOvdEiVjrKk2NdJ6bOt0Bzu/dbWOvbU7furwgQUaafxpNk3/JyzwQUXzDYfL9a9MawUJpwuhQ6T7WH0Xd8fuZt+U8bNdojU6WphgYmlG88m4x0jj5XJHI4aW2ViXG8wN/FlDeFFWWePmF9jO9ImB4PUStVY62FUQ6ZKBmnaBmlyh1cUWu/j026D7Q+bMyJdEnPsNoQhGOCocPX40MOkjZOmykH1zCpg+SZ2j9zudtP15s4KDZmaEqh2KTybKi4C4Av9obWEke1XrGNEtSDkkYkmQlys9icZkCpAvztllx0hxSyU4spGdUVXSbOr5XC/izt0LcTUOWeEa8kPTMbBTXKGl8RRl/uW3Y2AZcGkExhMmZLVpptWxy2XnO1AFk+w4xN0PZzxCgbDmNUCs5L5lDd53JWFtjvpcUkPEe1m0IEYR7XwXcyS6tWg72iMXUqggQdSFM+1e907pz22TZT70dmzfe2V9nYcgqt1ZM7i6XqjkckU3Ik7ytneUNheoQ7bIUixyMLCGl/XmQpPaFsMFSBILd+6FNVaqkM1xnp3jLMTYt6lXSPd4qA7KkVzQV1sB43MORLWvSd2MXO9WtqZ7YK43Rygy6DEUu/YuXqzC/ouXuQzRYF0XNUbT1P7IzTKBOmrecPqJxoOQeqWAmaq5Q2j+TWvxerZ8trA28Y5mH4nTtm3jM0S65hXTjF66+RLqHLq1didtj6krRJ1ZUQkTJdJGeeXw0DLjMO76s20PKVc8YU5uk02bljWtfPKofdKt+Y3RoEQnpopRObbPTWV17XfpiY8EkXosW2kB+jm3KhkY0KwRVUjHpPLzHNWF+8m3Rw+uAxONKgM6d7Wt/Z8MAkPokwQ2FuvIh52dw48CTt77eLlxFLv5LUw1kl3kMaBMO9+K6444mCdKU+crOZmUxNA1qEMb3to2CHbrUfRzU41Lyuna0EeRkq6XMQlSbnn3hwQIsfgktSPLsV65sVtySq4bRF2yDZENanbKViG9HCRNEU35d4B53fd0Spl8kHfdmQfe1dI6QDbimXySgwokjjpSOJ1n7LnbUJa0ER17Xp99jxjHHrXguHu0ENsg0nNSvRgp+7JS6Dl4730MnTDkp3lLLFEiwSj8COv1CKtWjoslXSyJkXc2hrvO+poiJZfQb24M2p2uzpiTaNRHAMxq13S4P1he+gA/VqiDgIb0r0agpsCGK7D98wKE2qbpY6Xm3DsMEhQXWWVhObmfMA4o4solNpJt1VjrrdGMzoXi2UsjjZgHF3huGVeDH/ftE68HWAWISaL25eDm941f3WKHYO8rEoAWHXrVVsE96/t0uQHdA1lxklNbidBwvoU3VP94TZiMJNpYQCJSLitNqF/ONztLe5lFuni40ZnSglDhVzgUZqOzw5foHWFAfrlsu1ZvaFGSNCIja03CQZ34w0e1AmP0iXrYSC3TimFxAXP2MuWF2pW46VaTPlSThAK1pZme1qF5cZvrsPhgrfx1LChSHRtGjAGg0UpKlymXcouER0cSoT1WNrjZk1wFmuODtcJoSMXVxsivUGnBCkvggkBmU+WyMGjoOWWhVGxSH2Ms6iLz9CKUC+9K+6DkZIzULT0eBTVrzBhcaadxyzgwpBw6M+nuJDw8QAKJ9quyzU/tCNvlKtoQC7NBDiLvauyw9nLaPmYi+5Q323VzTyeL4NczZP9SipRhwo3TgTOYRG5pqlJYQHF85aGCU7mXmiixbIp15hHkauLqvk2NsJBus0PMoEgzpoqllTpCaOzVkmeBMfavdhqxxWXGPKSS4Nif1L7C2xffe1Ms4e10XvW6kr6A33YCfDSO+0I1Z6EkOxkU+PSC6qWxWmHekeMOXdXGjabyy0bl0q1vnRXEq9scrlWkkC9YatzfB1hDPKF075z/csp0e77YdWpa5k7WzevYPBcJ5dYr067YQgx/NY7UCdiEAR3t54P2yrwNpANZSaUjetLz+mXugF84jTAbjoxis9UNgglLlsZZhK1Wg5XxRxrgaNuaojX6iV3le0y96ClLpCmhl4x4Y7AE3+UqjTT+Um46eaWuq4xx7UjVp6K1c1qsbVYVoEQrwa6vprDXVitIo3HbgELzkvLA+w2/LUetRXDaisEZg3uNO0EdTpj8EFcmZfOjwkdWS7ThHCnAUuaS59Zbbdpi2zXXJzA4WTH1LARV0xDvQZrgEdrL+YOl6NR7tFSGX18twFno2m7lmCGu7u5vxW6a9INpQdBNFLC/bo1DgBCsNqdejctD0ZbAzYDzlAY0jNTgaNlNeCIjp/qiXDa6pwn27OHOnZbb29on9XLytDlLCmEcrlqYgh05oDetum0xIVgaLjwUlGVjCypJdntLMAVbyyqjLwJ9QlosK1wSuVMg5Se7nM8zEeS6R00dm2j3y1p+xwRRth7bnjy+Lt5uQUTi3s2nzH+xuqFg2hbU6PE6uFMFSuzC64d3x4oRLd4WHcOnhEWneL0xj3FE4yJShwuOKnOE1PQtvZOuXLI0bdpAw0thauXLUTBqwDj875HtqiCbCBEMuWVYw20gGHLDjWKS3fJV1kQyBcuLEPSvVCXvYcQGydb64IqeMf1tiPO411AGT5VyQPL6QqHtlxxhLybC6/1tbJppZiKyUE1UKcS9jZF1f6uC1tI2+2vA6cdc/duE/fuLKtU5RZ3nKmva6HkmpQT9vthiDZhf1Zjm1mBPN5plTvW7nZ/XO+UDs8KDq22Ww2iyAMvRQQ84sL+7Dm9HwpL2eM0hxPOh2WvskSM1PBel6DciSUI5uFwL/dd1eAAUbQL1KZw4ASHdO1Nu6DEqXpQcQOilnxCOko3aLKCF6fax/R4qUvluqr2NvCNoyZCXa63flvC4wihzZW4n+szexlgjO/BIF9idYe3E32/sz3fI2sG8+WBaTwYokJ22+kqXPaBLrVY1VXH9QlGpNuOY4U4GGKT4sNwd2zhXVWwzpUtE/aEghRdeEK3XcGb1re833bMsbFUcbUWLXhfblEaK9k4XDfFSpfDpso9n0y9ATkJ1KF0GggRWwgOKB0+h4h0IF2EWiIE3u2CnLS1iSbOiWKu+0t4xSt3Wmv7hE804ybebI8+IyuFH1w0AYeLNQQnhxARhSDcbwh4R7dzCYLzq6bawbQPCHmNh9crhJ6Hm+Kt7RbFDoco0OzVWtJ5hqbpv798ePn2APLlv/Jjq/khy/+zZz3PxzLvP514PDXzbe/TQ9en/5J1v3x4qd0Y2PZ8ytVkXfj2IOgfnnF9/AtPT2dB0/NXTe9PR59Ph1s7nH8L/BIXXte09fSlKbPubYfTNfOvBpv5h6UueP/+YeD3rn17atWWXyp7DnBczD+T8L34eXv+Gtbvlnhvv+b5ghOrL35dzS6/PYUHnuKvyCv+8vv/AgOFjZ/JLQAA -->
