---
name: "rar-cowork-cookbook-teams-update-issue-requests-for-information"
description: "Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_requests_for_information", "rar_sha256": "4013420969b4b11c2fef9177e66263d1ee9ca415df53794e4c29e18edcf7af11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

Issue requests for information Teams Channel Update — Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 4013420969b4b11c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_requests_for_information_agent.py` first:

```bash
python3 teams_update_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_issue_requests_for_information_agent.py   # or on stdin
python3 teams_update_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Teams Channel Update — Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Issue requests for information Teams Channel Update',
    "description": 'Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba529d59cde5bc78',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateIssueRequestsForInformation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIssueRequestsForInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6a5OjxpL2X9H2fhh7mWnuAs0JRywIIZAQIIEEyOMYc7/fQRJ4/d+3kNQ94/U5Z9f7vhGriekWUJWV+WTmk1lF//Zi911UNi+fXzTfLmZrO8viyG9mduHNluW1bFLwq0wd8H/mlkXXxE7flU378vHF81u3iasuLgswnWvsoGtn9kz37byduZFdFH42q8q2m5XFLG7b3p81ft37LRgWlM0sLsDP3J7mz9rO7vp2do27CCwNHnV+Y7tdfPFnjGdX9y9Lu/HuE+s+dtMZUMUO/VegiH+z8yrz25fPP//y8SUG318+//biZnYLbr3c9TlWnt354qTE4akDXzbiNw2AmMwuQjC+GgAg03XlN9NjcMvzg9nz6ofWz4KPs3/7t/RqN2H74+cvxez5+fIy/Tv0xayL/FlX2m3nezPXrmwnzuJueJ0x2dUeWoBC1zfFhFULjCjC18fMb5LKavbT9OyHxyKvod/98OWlBCrcdf3y8uMMwPDlpemn76+TlOqHH1+z8uo3P/z4TU7bO4nvdpMwoPXr1+f1UywY+G1oHNxX/QlIffjV8b+8fGfc9HnoPdkJZr68JmVc/PAQXDXlxS/swvV/+PEfiXUj302zuO3+R3J/fgiOfNsDNj0V//HjHeRfZtDToHeZ/3jZCrj1r1gChr8t93H2BOofyb7j/19EZ3Hht++I/11xf28C9NPs539o2z+b8HEWfHnh/AxkSGM7mf959ttXTV0tf/7gfbv54Zffgej/VoxW9o17l/A1t4s4AGny9evPH9r77Q+//Pyhr0CsgXz62jfZ35P593C9r/MHBJ+jfvjjXLD+sUiL8lrM3iN99ltZ/Uvz++vsZGex9+1++3n2fb5MH2g2GfG26AOC73KmBbp+h+OPL78DpiiANb17fwyy/F//dbaL3aZsy6CbaW7ZdzPg4C7O/Ul5PYpbwGL33G58gGsbA2Cf40D8Tx6eNC6D2a//7t6Z85P7ZE64mzjoa38noa93Kvz6RoVfAat8/Y4Kf32d6WCJsonDuLCz2YFR1S8FYLqim5avGr/1mwsgFmfo/E9g2qfpC2DM2a9/YZWvd4Gv1fDrnenjB2cdluLEV22f+a+TzUbkF08LXcDK/s13e7BWVrpAsSAGlPsRYNGWGWDnbsKnTeMsm3lxA8Aom+EuG2D4eRL266+/OnYbfSkeBIvPHtWjhcGAd3Vmnz4BC4MsDqPuS+G7UTn78NvvH2b/Mftns+7CpzVUQPlPDwENN5oiz0DG9TkYBpwH3A3o5O6h335/4gzEFKDcAX/GQew/JoOITX3vDXRNYD5h5Hzm+AA9AHRelU0HWHsWd68zMZi96wsWnR5NvB5NVc/zK7/w/MIdgFQbmPOOZFF2sxb4oQ2Gj7O+9e+r/uo09l3FHKS+3f062y1VUEXKDPyY1LwPApPLIgbwv4fE4z4Q0nxoZ+ybiNeZPMXorLIbu4oa+7lGYD/8AqrH23Qg3J4V/vVLMRVOf4LqHiEPeMAggIz7dOmnyeegDcgBO3jt29r3MfZU6/R7zWu+FO0zGexmcoULigNYNOxjbyoRf3uGVBuVfebd8QOaTpKeXvCeXrnHoPjPG4dHt7F8dhuPMj/70mMISsz+r1qSSW1mvT6s1oy+4mYrWT9YDzinDmqC/dF0gZ7gPvmeOt/6hDeWeSPbL0UWg9hohr89Rt6d8BzzILC+AZgdmMNdPogAAOfdmilAp4Brmim07S/FG6t/BKDcKQzYCbIZRPsUZG8LTk/fNI1Ayk7X3yr83aHAbBACIAhnVe9kIEAC3/cce8IgaqYke7oARKs/Jdw1it3oD1bNgHQQFED+3RfAAYD579DJJTAT5FfQlPm34fHUNwEtvN4F2oIW1X+dGSBPplhpQXKC5mcaA1D4cBc1y32AMVDxHeE2squHMlNX+1TQnnxR5lPUfOeB58NvkX3XZVIfSLVBjAEsrxPpev7t4dl3PZ++AsrmUy7eJ/3R3U9bZ9+Xn799Ke46vvM8SPFsqtzfgTMDAQjCeOLUiaFawDK5/wwgEAn3Iv36qLOPQv6uy+c/tfI//LVu/145j3/03OdZ1HVV+xmGH9Xurdi9An6AQYzEld8+Ct+nR0n6dE+4T28Jd69d3yXcH5Z4IPZ59tfU/IOIZ3x/nqGvyCsyPZJi158C+PkBqCw/sdYnYnr6pTj439z9jImJaLMBVNr3qvM2BJSesPHDafCjCrVT8bqCenmnXeCQL8V7SDwTZuKfcCqZbfldIt/LL3Dww3/v1QE8Kjqwtje1cI9tTjap3/ovn4s+yz6+FHbu/5XtzVQKQPQCVKbdEcgk0Bp1sX+/em+Tpos/7uvuOQbIwSs/T6n2cTa1tB9n793px9nbfuG+FSt6sGH6eeqMpyXBUPDrfez7ptHxX8BOrRuqyYLHJmhqyJ6N8p+VmDIMaOz6U3kv31N2WvFPQsCXMPSbPwtR7l/s7MkbgN+nYh13b9neAj090Pp8nAEfgiwEiQX4sgcT/rwMWGeKY1AVvcncb/h9M6t82PL7HYbusZP87eWNP54+eHaNYDhI1E/tVBdhEK9gQXD9iCzw7P+ln3yKAuQHmhggi0BQnMCQxXzhEA6KuljgBwuUovz5HJvjHur7C9cmUNILSJxaED7hYgsfpX3PDSg7QFEg7xGqX6c+IJ7Uw2zbpV0KJbwFZc9dH0cc3PVRDPUo3EfIBR7QtE8ApN6npoA5nzY/bJwAfW9tJ2yepv/24swJMFIgWpF5fJbw4mQ7FuzcIgFqMuh21uFSqtblZo3bhzqXzB1xkU8MdfWybiWFy344mEhvlVK7y6j51ef6WJ0v4VaC0rGl2vTgFoWyOh1kgWsVfIN5xdkviiyvtHi7aaHOORslakFdWyInG91Jpi9dCmNAtu6p2ZieYa7JzLCrJSwV27Otri4wddPhNZHlF1EboINvFVtsdQ4Lk7QaA00RtLrVZN+lG6Zfo6bUyCtcy8a07cVAyg2PpsXAIFEvnjuGW6vx4Osx5ijNhqZ7M1mQ0mZOBwKOBtrNd0hT5ATtmJzZrh0N1LnYdCdnNba0mtyvl0W/xtl2053Pre2l9Lbw7AEv4IqV/flxtVoxOW50krm9eSbP273ZZxqqIKUeQ67Myz56KrjleelJF/e8OeOcmNhlVzirK6afDHnuOElHrBUq0Jy+wOvEwuvqkB06asuJRDvgw5LEUHu+GtrMrXTNDYJ9qipNvJBr63COF303NpZA3oS9qSw2Mu0ySeLjm9OIIT1Lk0e7tSm1iUxBM3IBvuzQkESd0zZyAsc4JvPGRsTM4HvteBYEeBu3B+XqBGQlKC3uNlvDkGp7PMvpBZaTapMSwmneovxVqKhiDONh3ZcpnWaK0wvoLvMupranIPx2tZS90hRepOyHizrwRo9zLBU40tLr16a4NpWg4sXTbtVdfHEvWdEZ4kuK532DWqEKZI7seYU7Z/RQhsUtLuCW4/OtRsvCRddzpTVhoh9O+0sJXW+WDeeKbN1WW3+L6v3WwMgFR5K0bEmugdlaTZnL62BWCQnck3thl0bb+dHUD0cLVowag5VKP6qVbghYILP2HsXdHWnHIT26dcKS8EYL2ApeFdBSxmEttzfuIoBZkQzGhoIC+FZeNqhfc9RGZRDcx4kOkbCbMZ/Xt3hYasMOy09Rq+lJZMg1hWnrnL7V1jFe5eZSIq7L9Q4bWmJfHtcLpFiBBodsl4J3ztOzdVmWjrNBOC1vlsk+CmUk147bbCNG801/TT2xkc58nBrS8XQc5rXdjqlUcLHdB36GL3O6MKlsn+zVnbm5aaebuypJadVvNXEpbcQlqTd0R2XyYXFICHnE5a5GpD6lOHOkuUyvTsN4cRx4C+2VKknaimkhh6E5pXV6h7dgw9om6/iwCi6rvN6gamTqnWQwZ6PVGT5fB1B6DrrbiQsQhGO5BVWJqX28aYOOLAhVbU/b+YJRMag2zH3R0weOxM8k78OQfjt4+snz7d0wrBe7i+0lnHdGDhfY0sotVMnrbUKQNd4csyLcs6A09dkRPfpHpTBwk61v2rXdjXtDicgFa2bkcns65X5/XIoXKL3cHM+lrMsKx9FYM7fyOm+gSOGZ1juZXN8qOUlfKm0gsEwkza7c9ah8ZsX5SMWtpdBjUW+kfm3XqVSNcuedeZ3vDdRM/Js0eNiuvOGkbwA1O0wVFl6HNQZIGxZxshFdrTe6BWf70ti5vb868625UUPmyhAmG9Bpl4d4pxDcUfXT4uJd4FG9wv5BYVCO9Bimlvj93souRWtxp81irnMNblTQVi8ROiFYfW+fmfWtLqsTT92WemWE5EBe2EMQDNB1efCIcyEpFRuoJu3tqpU4koQFy5hxMwdRYPTd+rZn6xDbGVAPl6K48lq2OSt8wohaxqeOG+0AuKjUrSks2hJsEe5IpN4ngh428dlOF/SgZoEiDUwWlRvTt/k2WZ2CMWyIJPRuworbGPiWdnZMJ+JCS5vZ3ryatiFo7BlFaTsoMmThX4pquW3XeCIfiTlMFbZx2qXYQrbNs7BOqZS/ofOVryfCMGokTuyxlSqWzG1D+n4QnHkYTg2jpmGdknyYJoqYR44ec1G33RUrWJaRglrXouSkno3ViZmORHHT4MMlTerClo9EWVkeXKbuDSI+iZJHtVhpL/OKyxj8eNKyrW6IgegO3FCw3JnQUTZARQdZhFW3LwVGVdcjUxSn6+48jx1BDC/wGt90Y4KIkjGHdpqNw7u4hkJnY7HBpXaRU0RGwzZMZSspl2meXpD+2jT1GjLNI2+6Wa7NaSUJrmEuMtgSCWwbBQYpW8q2HCv3sGNOYNYVFAUFkrTOtlqZY26qkbRok15YhZPx035A/HMorkBZTzFF6s7Xfr5L1MNwgciM2IvHPMXpFq+9hNVQPUM4hWr1G7+x8kukDvDGpY8le5b9ve1jlW3HOiH6YGe8rRqMvo6bre9wPnf2U0jchbs+0u1zFyXklYukfYg1WU1GREt34hGLAknm24V83J7Y1EF4TCwI2Y1rP0a22NlxUChjbDbBWiQ8WfN5n4/O8RDTS4nvNye2GbbngjJoSq0ozzp24mm1N3ZcQxQb5iyUQXaWM0PPM7q03SuahQk9ps5xt+g60mWwaqBsKMQDyOoodF8ppaG7S7hftJ5maaJTB/ryvO97DU2k2keYhRgvltTQaTK0KX3TW+qxWTu1XR6kkYX5sNTn2Y6jBFRDycgyNjvpIC1CbM+bTWfFjFMYlsoXp+jUsEycWrLFwmZ60WDooK2uWqmOyAgLUpPu6HkdaIO7z3RMYU5hRKqLpUJmenHsOuN0XOPMQYsomCRorwq2CXcl11hXKtRKVnBBj3Xhqu8X6+u4mx9I6UKVGGSSUA8x5aad59jlgtlb0ci38UEc2E6CLw6LrEXuoIQOp2M0wfaZKc4VlojlW26Ux2KdQvqpQ+jePtX2EJW73Y41clWrTlVqKdltETbblXyrTojJo03EEt6ocGlUAX/2SUSxQ7MvbfrQmXZ3IwoClKg1L+JzjEYslklTfZ96CllvOLMS8PWy8xR+lSqQu0UUrSf2DN5uo32i60wZoeOoQ3VXRWthg1h2xB48RGWWce/bQ0YTN4ohcjNspEDOaHW9vHWlDKrNWjnWhqgWS5m0LeuwXdoI3hb6dbVNbe/IHpGwk6Jh3ZqVdE6LaJOf12N2qy99InA024M6WPpeO1wWir5Gw7PZzv1xWcmaYWzUU46KxhgrQ4u6FL6Hz7qAhcecx8qAY5XQh9r+ujRotlMZ/GZt0hq98WkCmpkE9CDzPV3bUEQk0llRFigdHcaoCIZKA51WkYJE1CCXkUl0j4zKWROx6jC4S/PExdZu6ZqOgHLjXvWyjebWi86yQhl0nwzuirKaZRSKCnniSIRxEzYDJyiXtDlI5dlQ5tgeJey+b8NmQRl9vY73MlZLLV/sFahl1hqndZvhyCbHfhRPKAILcreivZV9OogWPc4LtQl8+ir06ZZAdePQSzEslqdjo5P7Oj8Y4xqXiigeUO/ar0Cv5OzawjH5VCt9hTbprNyERQaIHe3oyth6/NGqO7FY0ZJrb/c7fq+gDbm3EwxlyfAASqLRrJNxvSPqSJoHgsglIez3iRJSfI8fqNEOq6uFiTRvGTro2WnnJHcLDlfgo7GjVtk+FNX+Kqk0ucuIJR0tKSXKR5Tn5yPICHltXGqQYrwY0i2mFJmdY92Jzbg4VNaMaC2rMgxNSza29LmSy801Em5+jvPhnDL5RXywI6kPeZ/hchM6FTx59UoYZpkm0lb8Nk3Ugsfb9UaaX1cugdQqf3SzBSAge328ake6JJ0Wir0AahJKdEitv2xXtJ1XBewhtH27tBSJH7LVsZMyTO1buzQuN3Z5i6oIRq9VcsFSEpunfCEUTjY/gr50rMjTwocUKKkI1+4xbINBQoVguk3z5m2EBBE1i+zajWdbEULcbL2yPi39Rc/6ldCp+vnYiwwiqJvS0wYOqTfU2txfvIXDLDxdtrrRzBhrV7vxHtfoplof+BA0Cyx0BLmkeMdTblDQyF2528gc99qadIiNsClGi98RaKfjsSbLKuVdCjkp4VJTYfvkjhG4tgLhehjai0LrbWkSmJnRqYL0i+tcX5hjDAU1DF9SFWZW7JbiNCiDYQkmdnbXCbijXufoZXcsznsCOfQNwUPrTaCIMSTZmqOd3VOi+9oajN+4yNFIzgmVaDf7GrorygUoDjzEVmbBy0SplHRVdOYZclfDxbSaDHEj9qJhnl/4emqpHMI2NaYpIejyfLcVbskqTjGh5w75mBRztStGwVELeSlV5gJbQYNK75PA8w7Y6kDASS2UhTpAc4EFuZjhHrmuF7Urn4S1Qqq+twC7PU481JcM45F00ceH+XqDUFxhm6Tfgf5rfbshSRaZXljB7A5leTjnbhAU0RTXFirO6JbnReiKIGIqZCGibFqiRxNYqrFtpkilzszJdpf0u5Sj4cS7pBaGaEdi4/ULfWPHFszn+DG9sahyW63jcYQWcWemgtvDnLlL+c2wt0x8rkZn/LaFaDPBR52B7TAQdpJL0qAOUayjbfSrK9zSgkBGtYhN1yNvIaGPWusF+47eQ5d5xwcYQkOQP4yKSHncYi8cWwzxxjBx8XaP7LOsC7cFK/DUmRB48dYZBHqIIMLleadx8k1EQHpwALs0nFfH84XtrizFUyLqxNJFhsbQyshYS1CjtjIZEeSjm9a7+d4sXfpaLKA2qRSUziMdIhQUOO8mHvckdMs3CgNv2iVFk+vxFgr03D3kncB4ZmAHEKzIt2YrGcKCYhQlRpztGBR6z4dDPj8qur8IEBnvBTPfW+vuluwOw0I5JgjVGxuZoRmexw+nQSgZmINuu5Cp24Bg56rUItQGCopUtU4DtW2KBZuLm8Whj8ZLuqdimwOsaBQOwVmbrMNG4uop3JyWcKbdl+piHIn5KRkGdS6KLnxVhKZplQumct2yxG4KVXLkalHgK9zMxvEq7KwFFEIwxa7VhYlxrcrbUL4V0mVRJwnDY9ayuNUN1LQ3ePTl9BQhySENTHx9CiIvxIkLtK5KPjxW0vxySQ4HxJVXe9npmR3peSh59MbtJTj1oE080otjCKiCjexc8d0lsx9bKGTWSXU93CxjvtldaaJbynrp0Ws3KuaUw85tpxMs0K+gVnxlVw6OLiSzPu0IYNeYQvW8uDBQYPtn0PGyCqEVSxTjFAc5H89GYHO+nkdrT7FzXRCG2tn7ZtHpiN6dBzq+qu7mBsTFMOUPbICH/LJgz6qdsIHv1Ypr5ac5paO6sGsOFCYqbQDtSqkQcbZ1rv3yhM0T9oRXl4rnjhLKo0V5ERZ9Nqi7tWNx45WfE0Zygq7dWud0L7otrwjsq6slPa+Wc/3G+PJlTt4WkXpxdlRylAMvKBdudEZVOESJATVabEgZhvnpp5ePL9Op9fPs+X/zwnk6BPz/dhb5ODZ8ezN1P3j2be/zfa3P/yvtfvn40rgx0O1xCttmffg8qPwvZ7Cf/sKrjUnQ8HizO71Wu3VvZ/idHU5/tfQSF17fds3wtS2z/jnD6dvpLyfar8+D75e7qXk1naJ/b9q3U9Wu/FrZE8D3d5W578WPx9Nl2Lxp4g3Ae7HbfsXn5Fe/qSaTn+9KprPc6WXJy+//CckXnMoYJgAA -->
