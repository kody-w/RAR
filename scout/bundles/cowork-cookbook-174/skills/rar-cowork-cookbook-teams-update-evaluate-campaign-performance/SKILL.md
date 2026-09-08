---
name: "rar-cowork-cookbook-teams-update-evaluate-campaign-performance"
description: "Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_evaluate_campaign_performance", "rar_sha256": "365ac4254ca0907bf611156456e1ac2692bda2e0adec6b595018296b778736ef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_evaluate_campaign_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_evaluate_campaign_performance_agent.py` and in the RCI capsule.

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

Evaluate campaign performance Teams Channel Update — Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.",
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
    "topic": {
      "description": "The process or area to summarize, here 'evaluate campaign performance'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 365ac4254ca0907b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_evaluate_campaign_performance_agent.py` first:

```bash
python3 teams_update_evaluate_campaign_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_evaluate_campaign_performance_agent.py   # or on stdin
python3 teams_update_evaluate_campaign_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate campaign performance Teams Channel Update — Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_evaluate_campaign_performance',
    "version": '3.0.3',
    "display_name": 'Evaluate campaign performance Teams Channel Update',
    "description": 'Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-evaluate-campaign-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab5a20f8007b6787',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-evaluate-campaign-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'topic': "The process or area to summarize, here 'evaluate campaign performance'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of evaluate campaign performance. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-evaluate-campaign-performance-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads evaluate campaign performance, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti', 'example_request': "Draft a Teams update on evaluate campaign performance for USMF with an Adaptive Card - save it, don't post.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': "The process or area to summarize, here 'evaluate campaign performance'.", 'name': 'topic'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want a review-ready Teams channel update on campaign performance status from D365 F&SCM, with an Adaptive Card for triage, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEvaluateCampaignPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEvaluateCampaignPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': "The process or area to summarize, here 'evaluate campaign performance'.", 'type': 'string'}},
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
    print(TeamsUpdateEvaluateCampaignPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WZebWLbmX1HHfcjMKzuYxOS7aq1mFgghCYSQSNdyMoOYJwnIzv/eBynCdla5qqtu91MrwpYE5+x5f3vvOPz+4vRdXDYvn16MwCkWkpNlSRw0C6fwF1x5L5sUvJWpC/4tvLLomsTtu7JpXz68+EHrNUnVJWUxb+/z3GmSKWgXnpNXThIViypowrLJncILFmFT5gt+LJw88doFRuALQd8vwO2Fs4iSW1AssiByskVQdEk3Pvi3zg1Q6+7lwmm6JHS8rv0EVgM2qV/ei8UxcHLALXaKIsgWVdl2i5/Rjy2gEMwc24dE46LKesBw4fZZFnTtLw/SQFXGd4Dst2DBOY2/UIydtrgnXbzY7OX2sabuEy/9CLgmQNlgAEplQfvy6de/fnhJwOeXT7+/eJnTgksvD0nMyne6QLg5WQ/euTcj7L/ZAJDJnCIC66sRGL0A398sBC75Qfhur5/bIAs/LP7zP9O700TtL58+F4u31+eX+Ufvi0UXB4uudNou8IHBK8dNMmC31wWT3Z2xXTRB1zcFUGTRAp8V0etz5zdKZbX4y3zv5yeT1yjofv78UgIRnNmjn19+WQDffH5p+vnz60yl+vmX16y8B83Pv3yj0/buNfC6mRiQ+vXL2/c3smDht6VJuPhi7AXujVcTeEkVAOLf6Te/nqK/kXszyZfn4p/L6sPix5Rnff4C5H1GpQvo/pgssAHY+fJ6LZPi5zceTQnib/bQz7/8I7JeHHhplrTdv0T31yfhOHB8YK03k/zy4eG+vy6Wb7p9pfmP2VYgYP4dTcDyd3ZfDfWPaD88+zeks6QAKffuyx+S+9GG5V8Wv/5D3f7Zhg+L8PMLH2QgDxvHzYJPi98fIfLrT/63iz/99Q9A+v9Ixij7xntQ+ALSLQmDtvvy5def2sfln/766099BaIYZOqXvsl+RPNHdn3w+ZMF31b9/Oe9gL9ZpMUMS19zaPF7Wf2P5o/XxcnJEv/bdYBi32fi/FouZiXemT5N8F02tkDW7+z4y8sfAIMKoE3vPW4D/PiP/1hsE68p2zLsFoZX9t0COLhL8mAW/hgn7QL8zqjRBMCubQIM+7YOxP/s4VniMlz89j+9B+5/9N5wH+pmdPvSP+DtS/CGb1/eUf7Ldyj/2+viCDiUTRIlBQBzndnvPxdOBCB55l41QRs0N4BY7tgFH8Guj/OHRVIsfvvXmXx50Hutxt8eMJ08sVDn5BkH2z4LXmeNrRiUlKd+HkD7YAi8HrDKSg/IFSYAyj8AS7RlBipAN1unTZMsW/gJQBpQ4J4VCFjw00zst99+c502/lw8gRtbPCtfC4EFX8VZfPwIFAyzJIq7z0XgxeXip9//+Gnxvxb/bNeD+MxjD0rJm3+AhI96BPKtz8Ey4DrgbAAmD//8/sebmQGZApRq4M0kTILnZhCvaeC/29xYMx9RnFi4ATAesHNelaCSFtEi6V4Xcrj4Ki9gOt+a60U811E/qILCB2V0BFQdoM5XSxZlBwpzl7Th+GHRt8GD629u4zxEzEHiO91viy23B9WpzMB/s5iPRWBzWSTA/F8j4nkdEGl+ahfsO4nXhTZH6KJyGqeKG+eNx1z/Z7/MHcPbdkDcWRTB/XMxF+RgNtUjXZ7mAYuAZbw3l36cfQ5aGNATFH77zvuxxplr6PFRS5vPRfuWCk4zu8IDpQEwjfrEn2Pvv95Cqo3LPvMf9gOSzpTevOC/eeURg++9wI87omf7wr21L8/uYfG5R2Fktfj/uZuaLcNIki5IzFHgF4J21C9Pj80N5uzZZ086Cz5r9MjOby3OO4y9o/nnIktA+DXjfz1XPvz8tuaJkH0D3KIz+oM+CDLgsZnuIwfmmG6aOXucz8V72fgA7PLASBAGADBAQs1x/M5wvvsuaQxQYf7+rYV4xEwz22TOwkXVuxmIwTAIfNfxUiBVM+fxm5tBQgRzTt/jxIv/pNXsOWBtQH8BhEhAZgIfvX6F8ufdd9H/tPHZKc1bHl1kD9K4eRAAcjw8OXtj9g0Qr3v280DPTw8iQI286mbdXZBIQNPnxaAJgPvapJtB82nXoALQ/XF+f2o6Xw2GCuQOMBbIkKoH1n3k1Aw3OeiDgAwAVkCK5UkB+gJglDcjPAg6+ZwlAIDfGtcnxcflN4WCRyLOBe1946zIvGfuEZ4Z4RTj9zhy/FGYAHr5vOLB928j7Su3mfaMpS3AQ8Dx/e6zmXh99gPPhmPxTvfT3w1MP/97M9Wjwpt/DoBPi7jrqvYTBD2r8ntRfgVIBj1lbZ8F+uOzdn58r50f34Hj43fA8ScOT+U/Lf49Kf9E4i1LPi2QV/gVnm+pb1H29gJG4T6yl4+r+e7nQg++IS5gX+YgzGYXjqAj+Foe35eAGhk1AMbA4me5bOcqeweF/VEfgD8+F9+H/Zx2M35Fc5i25Xdw8OgTQAo83fe1jIFbRQd4+3OnGQWv84A2i98GL58KAHAfXgDABv/OfDfXrHwO8nYeD0E6Adt3SfD4BrLV/zKL8yT6+98M0LtH0izmm1/D7e9R9cMieI1eF/+6xz+iMEp8hPGP6OrjLMHrtQUFEojajdWs2nM8nBvKB6YN3Q8ke3xwstcFHwD8zNrvE+WtEs6dwHf5/PQG8IIHLPBhMYvZzpUbqD8bZ8YCpwXJBaT8oSyP6vXlWb3+XiB+Lnh/KnBzm/HoYABavpnINLbiD2l/7ar/nrAFmpeZll9+muv4hzdABO9gEvqw+DrUAI3exsyZQ1D0YIL/dR6o5hB4bJk/gD3g7eumr38ycYOXv/5Arq6sEu/vZTo+cdkL2ocFQVvizCK27x3ChwXI2mDxU/DPmo2ffmAJwPKB66A6ztJ/M8s34crH6DcLB5Tpnn+p+P0FBLgDPOq8hfjb7ACWAxj82M79EQTgADAE35+JC+79X0wVb5Ta2AG9LCAFvO94KxRfeQ5Mw6QbEgiC4MQKJwLE8VCCRl3fQQMYFB2PcHEahxEKpQmXJCkSI4IQ0HsCwZe5HUxm6WbRgFE+AiwJvt0Gl/w3tZ5qzDb7OsTM6r9p9/uLS6zAyvWqlZnni4NoxIUw1R2a87KAl4OIo7gstsZJgXPC588+qqh+62JISUpmpyo1O6w4Y1B0jmMuzFpthMsUXqLlxV6m2JSTDCMcKs4oiAu9wllBIZUVHWD4El9OG8+e2PFOjWpuxTrHYPllsEBHYd7Sabqad04xiBMmxUNf2UqZq4Oru8aoQjTuQEnZDa3NkrQVFEvQTFLYJZlcQ8ZMhxdthKbUjFjuBn+lOvpF12lTzjdI2ogHQxdO1igdTemKM76xyZGjfJMTa5tcYX6zG6a1dcESw8oofkxrixC220K4w5skc81JEy17LSmsZyVXSTsRrHTMymy1buv2vlWT086Jl+pSdWlikxPxJYEoCHgZn2Q6E8Vh30olLPETtOw7TCXpZXgrxqM6UAFU9AFMg+yR4ky51DE3qr5dHlHSCC8xqvP8Bk8khYhzSmSrwFYL5b6Xk6t+IJZFVbPjGFuIzmw38i6ZRLPErgg0LPUs2yTeaDqigqzOsjIVgndIWJxtOtEgJGGbrxGjL4fDeJS1ZuJII7hmhAVJeFZUGkZuqdhjbdVNN3A1pcKBvN/ESTANzjJKU5VOI68gjGy5iJInia62Z20XNVYToochYTOYtSOZa+7E6A5sqaloheAnaO3lpXMq4UlnWfM2EMr2UJ0nX+WZZbL1U+Eitcl1dETBQnfc1rnw0PHkHqo4GBOVFSmEz7hrczSdNYxuq6Nt70U/3UDB5Qaba2x7ElnGkDLb5iwhqLLN2TwqXHk5CVcqOcnnjYYIxuq8ZnrUB139dil4YbTmqw29YZcAoJK7xloRt74CO0FXO1BRpYaOqpsAO5+iWtK2jtSfLrwVR+49zVCyzrwELiTzLPXDsREd+uQUtr4qR5GQOWhVbupy8myA8PsUCevzmYPu5/u9FRUociDh1HDKqvTL4IC6fAQj4/6w37tdaxeXDDZzG9equ7jnd3dKhSPMpHZlEbtpie+MFaULqM+MtaEKFSvEedRfrh4krLC4NRtmt9V3EG0SlEBOeESa9fJOcTsbpZZrctyRd+8mbhv2GBxt9nTZdRhTp/FkkesLF2OpeXJL53gWMqI7XTNOvIeRbFrRDaXkG8XWahqvpKPeFiQhHzpjc0WkgieslLR3tORM3EkRUrUMhXrjsnCiJWZDsBoLi/hq3596qF8GnN2z5EHR736Ty+0kwKu+RUH0CeNwQf0WS/bOphmQ2yQ7eXaot3kzXE8NZSTIstIdqNTdc9rInGLV4cExwpMH8YYUDNi+OZklvV9PZmabeneC0kzB9Xqk3F3gBvv2ptdhIp6lZnfDuEgx6KuHdH41yWtjfegw06pSnkDoYdsyt2VuczYG11bK0SwGM7h5Cqs1obC8GBEb4VALG3nq5VsNRezZEWG5CWMopjMr7DFeti77ez25Adx5jpffhNCAcxw2qGTwu/UIbMLZuMlMiYnDDbm5ZcwOn856JVe2XKYHnohxCj/bezAy+bp+0Sa9NTVI8chG2wUKPV3Wy1wQjuMU3O/nOC1yKyJv9MAYRQiKGH8IkIF3osHKs9TdT2d/Yrhqq9x4acXmqT1c3LwspyTVlCQXQvUOqI7QaoeX8FGCd+XlXgfnpZNJPRTkobgEgMN2+mRjOn3eWeo6LCopK7Its6IFKnBS40osr217ms7dytlRmQdB9ZWi4tuhReTYK0AliIa4ccbNbcNO2C0xHfi6r2GGZBkisZG+O5XDep3JSQJt6ZyIsuU917QjFShkZJ4Fc0NnbrVhqi0bX1KTJ6pkJdSHOKdrF8GDgLmYljGmylq6pLhUq8nW9oF1mIEyAr6vq9bfB+3VVjYWK4OKskl2uiknVKeUonwhb71Jx5jQuptG5qPG5UnfLKvG5l20FigWlxIhQmHy6sC3Vq3xywZpdIE9TRfmmNIucmX9YZclRhOXyzI8VyMUnpsxXSnbRt9F8urMk87pgHPbeu/YSk+DGmNxu/YIEw3lr/ZSvL43ubAmw5hjE/NcUG2hULewwAeqD6/JSNOQE2CbY6HW6Rae9oPdHg7xLeUwkTnzk9HajmkbWta25UbShIHOloZMxFVXLsMzgwgoxSI3MTeHy6XEsOQmCDvCak+wyxChQB1uiQdqLcqV4hTjY2oSJ6VvL1ls1odjPlzz61kyo1u9PlpmslqiYRaim4DvlC1qHu+hsVpTtH1D9TSsThtMIGXv7PNJjkhQZ8tuc55sUrn0016/08i1jErZiWLjDPvDUe1p/7Av1Q5dFUoucEjaWUxSKCUlntzL0Y3ak8PtCCMSz91IxJF/KBkEGNY+cdjIWC1xuy6b0k3GbSrnKj5A0VIqtIN3gVkJdE69ROtOTPgjetLRML/1ksyiSSdvm/rGJfdU5tpDe45OuFtfWJ7fcbc+0mpl48iD0bZ1lQybmOeYVQn6fsQb0hM0eY1kxpw42am624yixhgaxayPBSUVsX1jnUFVtMgNClY7yemNGzeMA8x73WzNq9RFmm6emYMcRrFUlQ6ihaG2K2G8bqW4vXDZIEh7b4/2bEaV3JlILZG/2Gl/D0ZXli4stHcy4bA0uM7EsM69X2pQmRwpIVQ2GU7N3RGjlMYOsMQMnE+dhqOmlE65Eu+6elTg5n5Ql1fdw8rRZCHgYMvVuOFKHy/dubbkiYOmtWCa5rTZoAJ6QS5CcxJu8XKMUfMUbY9GtuMkudXSuLVF7oqdroQObympFOp4TXY34p5fUh4R7HYcsm2WnRDS5ga004O6cZY9jDFkb+djtAbxy4cu3erTxddkbq2c4DNyiwlx53t7WmTbrNzpYaFS1O2sbj0pXGZCyY1QlB5P3KbzfUYsHHwEjRuSZ+WILi+KqBBVyh2WyfFQrULidBRViXZUTtsyjSg1kWObjX5AAwtizgDIcKr0Dupm4xxdUYCZwpeyhDyn18mDHN3nGohcrUJDSw/bta2sw16RjvetzPqbdhhB36Y7w244F4olnuT8kvMNrh7iawhJMuOZw5IVpmWjoRa+xS4HBt6wB6btN/XFyJbmlo5uLjBm5wsr1/K0pQCFEG3ptSlNc2NtFGztbzF677qDggBDWMNSOKpNvq2ZQ7Q88Lp5cT01OI3b8LzHV+N4UDDfEnLmuEM3HC5EtW7aMqEPnHc6kdQmvQlTbghlfjdYf7k9bHZ61o1lHZ4dyIHPpLLT3Y2FFcnKyzqqP6ajHhxTiiqO2Aorj6aNnhNU5nTvnnfTycCvR/xu91rX6tF6zJx4TLl1c67SqjwwGUPFqSpHaiAMu7I0SQetR+OMdo6+pEQxrLUe0oN8FJtQ9iMbu69rOTicjsGK9M4uQg4ko+gax1GhlcFTbe/DAyswdl3WMMlZDCNueqm+TPAGwfa9k1/Z+sqe+kysaxgvCv900mIJaUELx8aaBdMAukFzgNyb+xhe7G104AhCMRpJcXKkFyvG4u9cLpt2xce9B/D9NBw2aMxZBz2LBFHom+Mx52qBZPexxMHyMcImi1XCS9utltQGgm5ScFuK50zNDqgaO7ydYmhubscJOq4GhIYNbOnh+9Klb5qZW8YORUBJo/pAzt2uE0adXO9Q7cqkko3jxsCdxAGCxpI4F2ZbsolwIdbCzQqd7V7h7OLQNb56cq27Xpk07RqdIZ5OCFy3JWjwhhvN7YczPwQxA1ENnZzXQhWw9wO9SZUuvkgSo6T3uDpCXAVakYGtO9FJiLt1FFJl5Qe38mZej+xJy4P4qpYj59yM+GQF1eFQXvX4smoP1CiN6EEaGsmAYtU/YlvC1rsQu6DXcBMr5t6SJT/edpl21YJBr7WNtwNBw7fXOBUZr4K7S3lqYEp1te3Ijq6By0i7XHqCjVQ7/X69gWqXgMjG2FbZpBa/Z005nbBmvd5v4CKE7F1HwjyGM5q14dRArpW6O8SGbYvdgdkgrABihVJsf3JIfg9ZPbpalvjKKsMDz25Rv79vBdXy7F2WRTu34fG+qccQW46uZHdNAa1oBNbjjNcifwtCw0hQnrXqUVT2+yJskEHHzuKWRgYkpYcQ9JvO5Zph4lh7h/qUqFNcnByUlylpTWX1NNQMjo+DQbt7vtzmsr/h6sNoiPYKndqtKHASbeRpD8sQJlQ3RsZVg2cQC3VJnmqHY2hpey62SRHa90ZtSTV/m7rRVg6HTY8jTF8dTdoLGHkKClrWlTDohTMpXJ3j5Oi3NIj38pTGhOvtJHe3bXxf9tcTc8pixSDh2hasQqmW+yoW7lLgsavOuyTb5lLm57XlyoHReN1E70uRzXVfLVaMcNOuvcsTGs+RHqU3d8jg7hOz4YJSzblN0Fn+bqrrqct2Tb/f+VjpkFZHWZRMXiOFrZTV1By6MTBWN58xjaIK9gNlabeK4HXJilHWH9deEO34wtTcrKXjoAQdI55ga9LfXdh2XekBaOJ3/aS57IrwkwuCYefMq3zBZ3yYGDZFaC6znU3KlUOXNrmiomjTjPdqiEnfJyCoYk5rMwS9Blec7TPfExM97c7xhHkA6qUCj5dB7JQJlC6JYpm6ESXHfb49pi5ofbdnUdCvph6uUKXtSCy1M9twjyis0Sp7QVwYsnG1VYvb+UJhaMO7KUXHjpuhmOONFEpmyyRY86kfbDaUq6KoGGsq56MuRNMGtLof3OQqTGK4R/dLKRNMuxVcFUKAFPmGRuWqPyYIWqm2Rx5aaxfzchiLBXx3z+5S593IX9cwJmeMLJ+NuHRW8VLkU3bU98frbuQ02m413UFqWOO1IhhLVMPJLQqvi4vR0g0j3EuRm1Sqw6Mp2wWtcQm87ZKEhn1aVi682nf2NsTXeiaLtWYuT8uiX5JGbdhDUU3hXRdXaIYeZb1H+DR1GkxOCSlMnG5VhH5razmM2xPZJGUv7c9t7sRYZ6xI64orBuROxNa/3W3BOcsr58ALib5fX1fFcV+PLbF1V4myAn21M2FcUhd73VWSiRgQ1zUpbAhq6RRUd012NdW+6o2LAUfgvG0P45bdT8Fob+EQD9QTHKtX8QoCP8n01Nje1yzhhOYQbUdkZA9b6lLFoR8EG6vcgDkHz3mPcHbJFlu5eaxFulAdqhuo0nseZbIQO26MnWr4kMfbzB21pmvO7oVbjdrQJsW3xXGa9tuBKpNkmSg8qONZjmiUcECCND5dw4m/5hdkKcbY1TzhDVSZoiURqcLsIHIT6OTB0g9nfunKZS2Rm0kAU5R08mj2vj3ujdxbunpWhBid8zmWMhRaXrWi7+wGvzXlDj1KuEvR91zfGPIWmg6SxYPGmPdrMGM0kRzyiUAKeLgjAmK5VahksmqNNAn+rkzH/Oh664trCkNTyChq+YRqF4GEVl4c12sxGYN1WefnkvbaYEtQnMCajs92K6SLBlXmKThsYzBWxUcLNJ7ddN3s+ySoUIGot93Zu286klnne7eH4i16uwZdeO6QU0o35zQidvWSyLiSoHMpIGGo83ryQNuonPs+mVGg2YBJfy0RCUUiBzD2rjJWnKwlhGAgBiECiYNRdE1luXcr/2hTZAP3+zrvXaOy5Fhcputrkt/Z66B1FnrSnNWFRppT2Brl6tRcW95JWmoXeHQ1rCYcw+8uetCH01kX8VDZgBEpOVVcJYDylAatRmhLzYpQ1sSz7URMK9MMJ3J1kJuLuCvXinI7ZlIaXpzlenWcNhQYVPQYYrgMRvb5kRF22nqXWdExvSTSDnTGWelFy91O4Zeq3GvG3Qgzpd8lwZAXgdqp2TVXkgZEe1Qrt92NThpUu62DdVMqsDiohZyRQiKeCJz31TCJ8TzeXzVkr6OOeXNOLOEFU7hK7/0UOt11A23MXddtML/y06trUOtNeLOSNYudJS4N1rdzt4HhyzjcGlfvLghAbzAVbupT1moXWl1r6flOuJbVHWBUl0qSECNP8vedlhfrBszAhXLe0bqF1zIKDbVPjZt7HcXpan/vViKNUgy2v7NEQJ0S47x0GDD5BGa0maJWXMcm1t12hpqDsmGZ4krPKY+KqzXHYPKK9tGwsnDMoCwYwnQlnZZFWxKNuqc2SLAu1Nu6OfJDQe/yk0mX0TbZUgfnsC5vHsUUV+buDPcrRmJQBSniTtpdb9PuGmAJWp5VcyffHBQ7gQqOsUio5hmFDKE1JvxAh4jXYdeG0NS82tXseEU1HxOuuVaDmcG/BJKUGmKji0Hvu6YdogWK9c5JJNd45GU1dtlZCLmiqSvPunBqSHgkcdXWlhCs4NuSdx1yX/QsqHz7AzPIUh+cliynsrvSF2B+QPbJitmt9YZaj6Graf3Uovp05a+HYbUcd8Vds0t7aqoeGW4HfiXt7LKPyUyg1PoatJSyr4lkLyAUYZMduW/6usXyKxmTdAfiH9uFKsCQhp3OhHZ3vVvtHvolz/b7/BBJacGTPXI+b3xzLZoagYmu3dCnO+mHRnjdaHc6xpdIaxJT3pgcdkdQvOlP/QppPNyD7+TAQVsPbjg4aGG+RUgoiNA16qnAIYGinii/x0X7HE5RU/H8mjuPqKVIEaMZXcjWBedcuPLGmiIsBoVGHghP4hOyym/SjT1Ezq5ESNmetFLCGbTcXaOVWeCMDGbR3g+80r/DOkFDrd3uKLVbFiGdQFYECxqIp+UKHrG+OqerWh9jX+UlgsbUlXjdhEIi5MMyM1lvIA9DOSYidsug856bIKi4CdV95uYPy65LCLlFJcNauvhZCscDQFOOjnDxzF46ArTpkmsG/O2+jSfoVp7h+RjlL395+fDy7cD05b/xiNh8lvP/7Njoefrz/qDH48QvcPxPD16f/jvC/fXDS+MlQLTncVmb9dHbcdPfHJZ9/NfPe2c64/NJrPfz3OdRdudE89PLL0nh923XjF/aMns8+gF2uH07P+fYfnk7aPz+GPN7xV4ep8ReUHVfuvLL/OhQMC9JivmxjsBPnkvmr9HbWeKHF//tKaUvwP5fgqaatX57bGB2yiv8ir388b8BvgxB14guAAA= -->
