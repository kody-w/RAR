---
name: "rar-cowork-cookbook-teams-update-forecast-marketing-campaign-targets"
description: "Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_marketing_campaign_targets", "rar_sha256": "867f2a8e2d8ce15e77cac3e65aeda1122d53aa228b68dee6b8a223d09ccf8aaf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_marketing_campaign_targets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_marketing_campaign_targets_agent.py` and in the RCI capsule.

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

Forecast marketing campaign targets Teams Channel Update — Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets
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
      "description": "Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 867f2a8e2d8ce15e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_marketing_campaign_targets_agent.py` first:

```bash
python3 teams_update_forecast_marketing_campaign_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_marketing_campaign_targets_agent.py   # or on stdin
python3 teams_update_forecast_marketing_campaign_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast marketing campaign targets Teams Channel Update — Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_marketing_campaign_targets',
    "version": '3.0.3',
    "display_name": 'Forecast marketing campaign targets Teams Channel Update',
    "description": 'Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.',
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
        "upstream_slug": 'teams-update-forecast-marketing-campaign-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '89bac41943a7da32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/forecast-marketing-campaign-targets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-forecast-marketing-campaign-targets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of forecast marketing campaign targets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast marketing campaign targets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.', 'example_request': "Draft a Teams update on forecast marketing campaign targets for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update plus Adaptive Card on forecast marketing campaign targets status from D365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateForecastMarketingCampaignTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastMarketingCampaignTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateForecastMarketingCampaignTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adfiRpbmX2He/mC7yUyENqTsU+cM2kEbCCSBnHXS2iW070ge//cJAW+mXeXqaffMpyEXQIp44q7PvUHo1ze7a6Oifvv8dvLtfMHbaRpHfr2wc29BF0NRJ+CtSBzwb+EWeVvHTtcWdfP24c3zG7eOyzYu8nl6l2V2HU9+swiK2nftpl2AC4nfxnm4cO2stOMwX7R2HfotGFMX2YIZczuL3WaB4NiC1Q7zzIW9COPezxepH9rpws/buB0f4jR2D8DboVjYdRsHtts+llrUfh/7w2cwcV7PK4Z8cfbtrFm4kZ3nfrooCyDLjAAU3Ho2kLj3F7Rde4v9SVX+YxG3C68A0HnRvo8d2wiI/Qlo6d+B6KnfvH3++e8f3mLw+e3zr29uajfg0ttjIb307NbnXlrL70rTL53PT5UBVmrnIZhUAnRgsw9vpV8DBTJwyfODxevbj42fBh8W//7vyQAmNj99/pIvXq8vb/MfrQNmjPxFW4DVfA/YtrSdOAVm+rTYpoM9NsAkbVfnDTBJAzwGFHnO/I5UlIu/zfd+fC7yCQj445e3Aohgz/788vbTAlj2y1vdzZ8/zSjljz99SovBr3/86TtO0zk3321nMCD1p6+v7y9YMPD70DhYfD0dWPq1FjBWXPoA/Hf6za+n6C+4l0m+Pgf/WJQfFn+OPOvzNyDvMyYdgPvnsMAGYObbp1sR5z++1qgLEG527vo//vSvYN3Id5M0btr/Eu7PT+DItz1grZdJfvrwcN/fF8uXbt8w//WyJQiYv6IJGP6+3DdD/Svsh2f/ATqNc5AG7778U7g/m7D82+Lnf6nbfzbhwyL48sb4KcjH2nZS//Pi10eI/PyD9/3iD3//DUD/H2FORVe7D4SvmZ3Hgd+0X7/+/EPzuPzD33/+oStBFIN0/drV6Z9h/pldH+v8wYKvUT/+cS5YX8+TfKaebzm0+LUo/0f926eFYaex9/1683nx+0ycX8vFrMT7ok8T/C4bGyDr7+z409tvgIhyoE3nPm4D/vi3f1vIsVsXTRG0i5NbdO0COLiNM38W/hzFzQL8nVkDsKVfNzEw7GsciP/Zw7PERbD45X+6D9b/6L5Yf9XOFPe1e3Dc13dq//qN2r++U/vXF7X/8mlxBusUdRzGOWBwbXs4fMntEDD5LENZ+41f94C3nLH1PwLAj/OHRZwvfvmrS319oH4qx18e9B4/eVGjdzMnNl3qf5q1NyNQTZ66uqAC+Hff7cCCaeEC6YIYcPsHYJWmSEFVaGdLNUmcpgsvBuuDUvcsPsCan2ewX375xbGb6Ev+JHFk8ayBzQoM+CbO4uNHoGaQxmHUfsl9NyoWP/z62w+L/7X4z2Y9wOc1DqC2vHwFJJxrFKh4YZeBYcCNwPGAWB6++vW3l7EBTA6KNvBsHMT+czKI3cT33i1/ErYfYQxfOP5s1wWoY0X9qMxx+2mxCxbf5AWLzrfm2hHNtdDzSz/3/NwdAaoN1PlmyblcNiBAm2D8sOga/7HqL05tP0TMAAnY7S8LmT6ASlWk4L9ZzMcgMLnIY2D+b3HxvA5A6h+aBfUO8WmhzNG6KO3aLqPafq0xl/7ZL3Oz8JoOwO1F7g9f8rlC+7OpHqnzNA8YBCzjvlz6cfY5aGZAv5J7zfvajzH2XE/Pj7paf8mbV1rY9ewKF5QJsGjYxd5cLP7jFVJNVHSp97AfkHRGennBe3nlEYPcf6ElejYt9KtpeTYViy8dDK3Rxf+X3dVsmC3Payy/PbPMglXO2vXpsLnTnB37bE5nEWdRHsn5vdt5Z7R3Yv+SpzGIvnr8j+fIh5tfY55k2dXAK9pWe+CDGAMOm3EfKTCHdF3PyWN/yd8ryAeg9oMuQRQAvgD5NIfx+4Lz3XdJI0AK8/fv3cQjZOrZLHMSLsrOSUEIBr7vObabAKnqOY1f/gX54M8pPUSxG/1Bq9lHIOwA/gIIEQOvABd8+sbqz7vvov9h4rNpmqc8GsoOZHH9AABy+LOAs9OGuAVkZrfPxh7o+fkBAtTIynbW3QF5BDR9XvRrv+riJm5nznza1S8Bf3+c35+azlf9ewlSBxgLJEjZAes+UmqO1Ay0RI+I8EGGZXEOWgRglJcRHoB2NvMD4N9XD/tEfFx+KeQ/8nCube8TZ0XmOXO78Ix9EGO/p5Hzn4UJwMvmEY91/zHSvq02Y89U2gA6BCu+3332FZ+ercGz91i8437+p53Tj39tc/Uo9vofA+DzImrbsvm8Wj0L9Ht9/gSIbPWUtXnW6o/PAvrxnSg+fiOKj+9E8fFFFH9Y52mCz4u/JusfIF658nmx/gR9guZb0ivWXi9gGvojdf2Izne/5Jr/nXbB8kUGgm125Aiag2818n0IKJRhDWgLDH7WzGYutQOo7o8iAbzyJf998M/JN5NUOAdrU/yOFB7NAkiEpxO/1TJwK2/B2t7ceob+vPt7pErjv33OuzT98AYI1f/Lu765emVzvDfzzhFkFujr2th/fAOJ632dZXoi//oPm2r1kT9/QquL9zkfFv6n8NPirzr+IwzB+EcI+wijH2cZPt0aUCyBsO1Yzho+t41zo/kguHv7J7I9PtjppwXjAzJNm99nzasqzl3B75L76RTgDBfY4MNiFraZqzhQZjbPTAx2kzzqzp/K8ihaX59F658FYuY694e6Bri6eS+cL0PpJ5n7U+xv3fY/A5ugkZmxvOLzXNM/vNgRvIMd0ofFt80O0Oi1/Xz8cJB3YGf/87zRmoPgMWX+AOaAt2+Tvv2Q4vhvf/8nuYBgD8oFhWvG+i7k96HFY4M2qwCg2+fvCb++gYCzgX3tV8i9OnwwHDDUx2buXFYgR8Hi4Pszm8C9/+ve/4XXRDboNQEggW8C2CZ82CNcf435m41ru4iPY7bv2es1DHsYYtswTDg44fk+7hDgC+JBpOsGhG0HAO+Zo1/ndi2eZZwFnCMapLn//Ta45L2UeyozW+7bVmM2wkvHX98cHAUjBbTZbZ8vekWuHRyTnHstLCfcv4brE2exIt1k5/wYwV5TH+vO0tgmKWp1ebEbcRvJ9Fmgh90gpcXdXHdGRIRnLMlHzyVkeseEl+48xubBqMora+UlvuzL9YRPuX+VL7aN0aalxeJKlgy/TCRdxCZb8/e4qC+NyogucY5J1+P+3ll7ujAR+KRJ+wu6nlZL0cUryXbKHm/pWsW2FmbmJsLjp6VmRqiBklLT3w8q4sBxlvBie8Aj9s4X7RXnT3rpbnaWsuMOOybe+5fKorDKcEdJSMrEbg5miqiyJZgxKUl3YWeZMT5x0nCkrGxXYoJ8areX/SQe7vuV2ucb0lSjk0anuz2cl/duIzLeDaZQNb8gyJrs08uZJMjD/XK4bMjNEoN6JIN1WlETivdoo9Oz6ZpS11CbGvEmY5wkkNspOIVj11SSPHjbcN20Llb3gtVR4p0olOG6rSSxdTVfaqGNJ1+6ksX0u5luMNS87oc8awfx6DmZHxtiU+zb/k5hV0Pd2RDUy0wjV/Cl2PjqhEKN0h/Jca3ujNiOwvZMK7SvaVuZqDH7zjSGWJlhOQz9QG0LDZ+MPTteTqlzc3GBOcPhqty3hOYcWV6RjhSkK8kGjhCsRG7dWVfEZStDx6NRj3Z8ikWDQE5DsQvXemum0s1lTMvGLuk1VW5RznfUKsNMCLf1RnGsQqhKd2Uw5bH0q4yLsCobcYRFSgVeakJVHbJjKdF01o7VSOvKMpU5cZwqWOY4YKTUXK6vOY9iFDIR54SLqot7nNTCVhNe0Q4b46rzSrGXec0NgzgnLrs946jRgDNscx8qSlecK7T3qoFupSMS7p0WNmySLXnVu1BanMC7NbmxdtV01xMJOlqru6aK5eRae7/sEy6o9MtpNVyKSeYOq1BcqYlCsYTeQYedw90G28DlY6A6bePk11Q1zTMfTLro80qJBWXUWaijXVP7RENozUTUmbvzmaefrl0RDq3GR911slbp5N5IOaP8xnRXvLUiqFXIeKvGsdIVxDZ7UskRCFrdiZ4yN4bpMta+LfgUGtdNvDohLNF5orx3LVi/u5BMd8Ymp1noetsRx5PK5SoSCpdM0aDGDm0/T673k7DOTrbmlUPgFarpIJpwHLIiiM4oZwDhkt3xWNHE0fV3vRzS++lMoRy6q1C+3WY9zbgDnxFdz90z2DpbmSkISHMiNEQzfKYnoC4q8UhLU0q+YkdNVXW+zeVtud8wIm9UtFHdWeLOsksiJG/ISbtfdpduq68U66CT+6PWrZGaw1IH4XClCWR4A186J0fL9WBk+UCu2VQfem59LBlBmFSOZfaeEeraidtytIXeAlK+s3pQ6+32gDN9FY1NFZ5F6A6xqqdzmp44NoMfGrvOqEssjuF2CHFdSOALd+OPxT0oV5natvZVnw7L46iX56OdGvWd1HZkm/r0nico7WB4XLHfHVpZ4RwNto7tfnesjqbfYeTJv65MoqQj4pofzj1kLPdKHnAE4eHZMDInVw7GQzAcgzLNVSfcTJwwIHLQrEk62jtXTnLR4RacvA0qC0YZqaglRZQeSYLW2SNUC6x52YmKX0OgXIwQesAKKOchtdgOnd8TTa142UpeyoygpVTr3DGfualL4KMgL3kjT+UtTOxweb0/3zCKNbw6y4NAVEhpI1z9w80sSXpzoXnRFayK4Xc7Xcuv3TE4Eft7iZdBA1HHO1XFgcG060KVCHuXVCtFz93ivL9ORLb3D7Y30PvY4O+JU4t0ydxomg0hVmGu6K6ArrWyIQPRczZ0HBmRuC1RSz1CEo0ds4t5Z30xCtUIGgxWrULYaNepuE3L7drSo1HecxeuKrelxHnkxDWHaxpbhrWluOC6OtmpwAXixV+7feEXqH5kkCPhdCl5I816r8bEkfFcmJcx1bxd7ybhlG5iDXZgX9IxOFwwgiwhWhcH7XrzaHQ5nSqBYtL7pO3bwdX9bDgpcZQ79bQKrlzhK/AQInazux7w4b6k6vNqtdktgwMmrm7L0y0i7W5Dn3qmJQgCPuy5Qjtq0FXtrqrDTbuOYw23N+qy2RWa6PsCes4yQ9008kBd3BVr8xTWt6m5l3VjmzPBzgqo9OweKp3BOHFPnkQm2If9nk9E74jtmfHGQidoEtd5AdL2Tgq4Ha1geqCPRX2uVb6HaSKNPaSRapy4UvC5OOpdexw2OzNGhbXUyb2IabVYb6FtNhLrQcoLtBdIYusl9C6GOo+azn215HfO6eoUvlsTx6OedqPKYrIXth4TnRkuHQYYbw0XlHZq62iVwUokpYcGZFLH0z1zJq/e5EXsxHQU+3qAtm0hsVRqs9OeoJBt4nYVqvDYZX9R0XzF7Y9QeN1mkXPtlnLLiRPl9t4Wt6IbdWZHb1lxW0K3E2hnUcl4gmqKuYQoeoxNW8j2XRBjyO52ImgECs2gPdnB1hZitrztUdLfQp2YxrxpRFQrMRB+AuUsU8Orqo5dfRK9GOsY47wfOXon7064s2v1C4adbEV1NiCv+G3pnqPbyKz6JArEMF2WXHTa8p7UCE1GURm9gqVKYw/JUEDc1jEJXsJJ6HaELpYpmxTcR8mFNhSfAd0Ii03Txdib2Yq/hULFI6ZVXdAoIf2kPFBdcYOdCE11y6g5PMeujS4HJZZX6vKalDwbNHtiqljNLNIwZAyZr9TEzg3a8OQ7dS1v4b3qKVJawfHuPCrHQqH7AfO6XWijNzLWZQ2/XHqHTFBQwmC9uEs4cRIPHilI/DbcyIRyb+C7d4h0qGDdGKv6yeSSk0eytjAa17ygTm5/SZduh1uot4llT6fSniuzihJtfEkFzJRIYazA1UmrXTJKkluXHfeUXWnbfMJEk9Abx0j6iuLohnUMhl3fe+0K+5fV9sIxhoIdMVQ0JYdxLBYe8onP4k3Z8kO5RGJ8e+kndOOfjOTEC3YppJ1ingeZpUK8O6SyEMfr0QIbzbPOGbvsmjE1Jh21W7Cyr9ubPvl0kim+0yxhu0saamT5iNpfDR0xJAIKOF6pmPvyvj67MR4emmxzWPVnUh3gUoxg5EjKaJSS5cYPSriA7iMUbPHAlTOjBA01tlUabZOOPXk6nnDAGQRa0PBZ5M7LZL+jcy+C+dOe0eNi0KA6HtB4j1b6PUuY9JRAyXCiXKrR96pWdiN6I5oDqjuKJoiXVR/3Xdoue4YaSFIRkOEeBDcs5aw0VQ/OsWQHulqpllPJAWDLgl9Ol+GCGriAH694A8NZ1m7FhqF5Iz5RPsrIGHGsBKmKwJZX51JySXBKUCn9QfOzUaiPO79w1oNwFDcQvFIvNQJ60gSXRoHK9NqpRMqwNyqLQzUWokNNk37EIbG0vnZrTq1kLmo4mFecrZay1n0txrkhtycLWSVRTN3S8yjySSRMcnSiRbik8AMn73Z4Sbt5W3UQFpni0dyFx3NM0Bjur2mNzdArOTWu0IaOCq1sRe78Oyspy2vX9hrPu9K4Is47j20asxtJuq83Zczs2SpjrJL29mTgJjDssGSuWjypnWm6IcppFJds4BRBUBxXqb6SKTzRd4Ke6g6+U7a2l5ykbum10o60an6qCv8cthymnwqJW2b2St+pdMLz1M7pvQ275AjzRhiF6mO91sIrs1utVyMLmgOjXcpkf8n3ysnaHrFI0KaOCtihrxUO8NiaHkzLuTZRrLnQXkDgci3qYzodklsxYhLo0rwh2R8gBF7dRONgDrS1OWJXezzcuPMoqLnDn7lC6UYoor0OvqJBlJSeckv9O5Vpom0epaMkOszuFF6l0r+j9aUcDNi2dGbSzknmD4IzxLuWGo+Nkm4I4hJoHaEs98d4sDApYmyftK4Yxqeby+a07sDWJ9gR+BBq+zuryEbJi+d9UVc2ZxThDd+q1H5z85vruUBKL8uQi0Lft2woCHqEe6lDpyQiG2Ql1KCo3XxHyvqyRd3sjjuONeidVMnu1gH83JXbwjCTMktNzpP7CBTOONEYfQgujC9E0saNzirr9bIL4j0uzV3ui5phmzLRXLHpwncHQBiBwMlYI6jpqNEJFiaga9uUyY1k9zdpO4DdprDpg11/YhKCTeoQUSI4FjbCsB1utQtnUpGRwy4xEL7XjR2SCfUtZA7QqjirlJQy0jaPtlIgRduW8kKyEu9RjRvxzjix8VkRLCKC13asdo1f4MG9QsQb6KQiK5P7k7WB+Yw8J+quXm07LtLHJUHdiv1VqiCa0etWECXblvLE3obJuTDX1XVvnQH7j+U67C/7SpU42+d9XVbKyyRdZfI2HNbsXTtUuWReekJcOcpKx253NZh6D8NBZgYK3NfoGbkKW1zlfOpSB5IraBcThya7nhohkJHbeDjAI2QgVtcU9aTeCRvd3IbGVwuiNys3IS9dFXZ5IsOm52MHhr0efcPA7SMuMU2X5+zOcEWTrALECQPTWI8qdbjw+dpV5LLPseTYRVYh4vISv61So8h3VJy6Uzlk6nhQDLo/s5onmQrog67w6Xwq25K0LcSzehW9S0LT8YFgXTcwVYc6YqWbvncYmlCEqwN2oK4TwxGKCm27QmtktdxOZFwsRdnj7eUqDQhFFO2bO8IxEt1phyj4llfQXuXglN3LB6kx6a12w9hdcKbV+548mqjll6vDjju3MV8eYbnRSIZaUtj+1iDBgT90ycSjawdancVpPwACjVyS4XoKg4X6QpNH2xaODbyUVFfBbuGZNQ8Zc+4CckPuxQqTrQ1/biLnYtGUxVC3VbDGEMQCTJELo5lOzPVysz1LjvgJV09a1bvZWdkv9wQESjG8JKDpZPWyvxRjwI7+aV8J2lq8tc7lZBtLs4evThCOBdpsd1DIl2zoHw6TzSNeahFX5M6eqEKE10ImcOstEZsOl6/rCjZT1KVbU3bHaiC3trKxYm0TwFfjgkvWeRgJSp78Jdrq3MmrpyGq6+3NKHcxpyWnmOA13FwVPI1XbqjTB1O95vUGvmuX6AC1lwxVorLYHEebqkFhp66nPZ2tYkDaQhOpRMXriQsTWISq0x6K+545sf1pWe8RvBCYO7okBQRsXJiwJ7W9JdRR5nXOVZkKUqPrbL0RBHnqCYkpsrCeEORYpGOFJ/KoHla+H+Vneijd6nxSl4XTTo1GXQrLmGBhe5fJvSPtS970SEO9Uiv/eJvsQs591EhcM+7CjSXXaT1FCQxpEZeTIjsNCn4YpPaurSOP8lBvuuhZXY/n1dmwDlFnre+1kyP8VrWJyXG0nvDcM58iK6VpN5B/P+zb9oQxjK7ugpsrnH25P+PWdWl1A8UOe6IbXNRR0SuXMCscwV2c9wz23h0o6YqNolgBHx+XcCrRtbDlfJQqN8sVflVlASKri9IF61a119m9zzujuxaZHGB9Hq3pTS6k6wPk3gn3skWyvlfWah1aNyWIGC23CsLqamd9aVce63hBWl+QZHtZD2p0UgKzXtEoKeVpKbVwyl1EK+ho0Kr3W2hzGlrk6ihwu6n9Yri22lBfWLbyU7ZWA8j1RPTejpgvDLq2yWtm5R2IEKc6+pyyXHpIukLBSVjGB4eq5DG3WpsUcQld+ixoEKizrI1nB8K0UoDGgIpZAjkcdJG9gi01qHRnrBgo5qZNZa0M0OQrV+yid1mL0zsUTw5EG6PwjUgQ6Xw+iRtE1NBuWJrdNRfJ+qzezfNybWw4pBxImJWRrVXWHqLcT6OYNFE2dsNutRbPTezwAu7GcpO7B/GAoGQoLVeKVcBETYhVAF1Fo92cNsomSzeqfrNayGaXo40nvmR4ngpDxXjvpcupLWDM7Lw+NgxxhOnWX9+yUUIJpT6Yhejsb7JH0oPK+AicTefb+iYSVVLnflFfIdYIsGWAomxhaMfRElCTYJYbm3IQlCUPtni3pKWyFXToIF456Z7HbSmtuS5dhd5o3j1bDW8HdL8GFKSGrZZiG7k226nKR2WNd3Eg5ooYbA2+91GsB/v1o7/ytvzNWepELStmp8bycLQHpgyJgcqn7Wgz58khV6uxb2oyyMsJ7wulLYxqPyK3UFbbdu1WuVq5KwX0WmTpmnzEUFiwltv1hFrdRdm5aHunmtOqLHPW1Uf/uDkOkoIOsqmrAYPD9RSkUgP5iMttWCx0M8QpBckmyXG578J2qe2l68Box8ydbHxKYUUFy+QTQtXXjVAwTcIIkjQMERv2phrbFLbLu2mrMsfa5aXjZq90SHqb0pTnrSVBqKkY4as7IjCm5/R+KKCyx2gOI5gHNMco0AcZQXrngvPhnl58vB+WUz1VDkloHWSs6uUBgi+rDWCz/oIrxNU9NLseCagCESYpFM7nCFvbmz7ZVUJc8Zgd4w20xAi361vzfqvtA+oHrcOpDVatty1xICNnkzqdYiMKIzcqoffTRRGHVqiV7YbxV4CrIrKm+40Eo6fUb6TO7FyB6MXqONyHlFh33k7fMpVxwxVo0M5bg0OrogkPENrjwTmcErBhJPH1lWaZO8L2mCRb7Xa949cU5B78JNhqrFIrk7RJb8D720tO3toIicge3qwaA9fV8N7XaY6oiUmSOyJPta4QTtC9671xSWepkF1oyUcTfe/dpeNU0JkQFT3TdVa3DIKctQge2+Lu3c8Ots32cKWpYbOtbgERusIpGAfqhkCm7Ldsfs8DIUQIJjtUGGSU1Ha7/dvbh7fvx45v/+0Hr+YTmP9nhz3PM5v35yceZ2e+7X1+rPX5vy/i3z+81W4MBHweeDVpF76Oiv7huOvjXz1FndHG57NO76ekz3Pi1g7nB4bf4tzrmrYevzZF+ni6AsxwumZ+qrCZHzx1wfvvDwd/r+Tb4+zV9cv2a1u8FH2bH/ybn5zwvfg5ZP4avs4EP7x5r0d+viI49tWvy1n315k8UBn5BH1C3n7731u2i830LQAA -->
