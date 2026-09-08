---
name: "rar-cowork-cookbook-teams-update-conduct-post-sale-follow-up"
description: "Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_post_sale_follow_up", "rar_sha256": "abb709b04aff55579fbf712f72ae0b63bb9543040b6b648f4b0900a4b07991d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_post_sale_follow_up`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_post_sale_follow_up_agent.py` and in the RCI capsule.

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

Conduct post-sale follow-up Teams Channel Update — Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 abb709b04aff5557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 teams_update_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 teams_update_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Teams Channel Update — Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_post_sale_follow_up',
    "version": '3.0.3',
    "display_name": 'Conduct post-sale follow-up Teams Channel Update',
    "description": 'Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '454bf84372283b4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of conduct post-sale follow-up. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-conduct-post-sale-follow-up-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct post-sale follow-up, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes post-sale follow-up status from the Dynamics 365 ERP plugin for a given legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file; it does not post anything.', 'example_request': "Draft a Teams update on post-sale follow-up in USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update on post-sale follow-up status from D365 F&SCM, saved as artifacts for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConductPostSaleFollowUp(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductPostSaleFollowUp'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-post-sale-follow-up-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G894Ptq6piEWvd6IhBAoHYhFgkgaujzA5iFavA0/99Eumtst3tvtM9MZ9GVbYEZD551uecrOTXN7fvkqp5+/xmhG654t08T5OwWbllsNpVY9Vk4KvKPPDfyq/Krkm9vqua9u3DWxC2fpPWXVqVy/S+KNwmncN2VVdt97F183AVVXlejR/7etV2bte3q6ipilWXhCt2Kt0i9dvVhsBXnK6t6ryP0xLMAGuv4nQIy1Uexm6+Cssu7aanQK07AHh3ZYZu0X5sQjeYVmDRLKjGcuUnblmG+XP1BQ0MLFdM4AIBh3C1c5tgJRpHdRWlefhfq7RbBRUAK6vuNcMtpy5Jy/gT0Cx8uEWdh+3b55//+uEtBb/fPv/65uduC269PVe36sDtwl1VBr3faQDAAPrun+paNYDI3TIGY2sACszz4a0OG6BaAW4FYbR6v/qxDfPow+o//zMb3SZuf/r8pVy9f768LX/0vnxaq6vctguDle/WrpfmwB6fVkw+ulO7asKub8rFKi1wDpD/NfM3pKpe/WV59uNrkU9x2P345a0CIriL6768/bQCNv/y1vTL708LSv3jT5+AImHz40+/4bS9dwv9bgEDUn/6+n79DgsG/jY0jVZfDY3bva/VhH5ahwD8d/otn5fo73DvJvn6GvxjVX9Y/Tnyos9fgLyv8PMA7p/DAhuAmW+fblVa/vi+RlOBuHJLP/zxp38G6yehn+Vp2/1LuD+/gBMQisBa7yb56cPTfX9drd91+475z5etQcD8O5qA4d+W+26of4b99OzfQedpCaL/my//FO7PJqz/svr5n+r23034sIq+vLFhDnKxcb08/Lz69RkiP/8Q/Hbzh7/+DUD/H2GMqm/8J8LXwi3TKGy7r19//qF93v7hrz//0NcgikGWfu2b/M8w/8yuz3X+YMH3UT/+cS5Y3yqzcmGc7zm0+rWq/0fzt0+rs5unwW/328+r32fi8lmvFiW+Lfoywe+ysQWy/s6OP739DfBPCbQBLLM8BvzxH/+xUlK/qdoq6laGX/XdCji4S4twEd5M0nYF/i6s0YTArm0KDPs+DsT/4uFF4ipa/fI//SfBf/TfCR7qFmb72j+p7av/4ravCzt+Xdj864vNwfNfPq1MgF81KaBsQNE6o2lfSjcGVL2sXTdhGzYD4Ctv6sKPIK0/Lj9WgN5/+VeX+PpE+1RPvzyZP33xoL47LBzY9nn4adH2koAy8dLNB2wfPkK/BwvllQ+kWoi+/QCs0FY5qADdYpk2S/N8FaSAZUAVe1UVYL3PC9gvv/ziuW3ypXyR9mb1Km8tBAZ8F2f18SNQL8rTOOm+lKGfVKsffv3bD6v/tfrvZj3BlzU0UELefQMkfNYjkGt9AYYBtwFHAyJ5+ubXv70bGcCUoB4DT6ZRGr4mg1jNwuCbxQ2B+YjixMoLgaWBlYu6ajpQCUCN+7Q6RKvv8oJFl0dLrUiWkheEdVgGYelPANUF6ny35FIVWxCQbTR9WPVt+Fz1F69xnyIWIOnd7peVstNAZapy8L9FzOcgMLkqU2D+7/Hwug9Amh/a1fYbxKeVukTnqnYbt04a932NyH35ZekC3qcDcHdVhuOXcinE4WKqZ6q8zAMGAcv47y79uPgc9CmgFSmD9tvazzHuUj/NZx1tvpTtexq4zeIKH5QFsGjcp8FSHP7rPaTapOrz4Gk/IOmC9O6F4N0rzxh87wH+tOt5tgqr3Xtn8uoZVl96FEaw1f83DdNiBIbndY5nTI5dcaqp2y/nLA3j4sRXj7kItUj7TMTfOplvbPWNtL+UeQoirZn+6zXy6dL3MS8i7BvgAZ3Rn/ggnoBzFtxnuC/h2zRLorhfym/V4QMwwZMKgccBN4DcWUL224LL02+SJoAAluvfOoVneABTAHOCkF7VvZeDcIvCMPBcPwNSLVb95lMQ++GSvmOS+skftFq8AkIM4K+AEClIQuCCT98Z+/X0m+h/mPhqiJYpz2axBxnbPAGAHOEi4OLoMe0Acbndqz8Hen5+ggA1irpbdPdAzgBNXzfDJrz3aZt2Cz++7BrWgKM/Lt8vTZe74aMGaQKMBZKh7oF1n+mzMEsB2p1nRIQgm4q0BOUfGOXdCE9At1i4AHDte3/6QnzeflcofObcUre+TVwUWeYsrcAr8EGM/Z4yzD8LE4BXLCOe6/59pH1fbcFeaLMF1FeE35++eoZPr7L/6itW33A//8MG6Md/b4/0LOTWHwPg8yrpurr9DEGv4vut9n4CpAW9ZG1fdfjjq0h+fC+SH7+TxMfvJPEH/Jfqn1f/nox/gHjPkc8r5BP8CV4eye8x9v4BJtl93NofseXpl1IPf6NWsHxVgCBbHDiBwv+9Dn4bAoph3ACCAoNfdbFdyukIKvizEABvfCl/H/RL0i0UFS9B2la/I4NnQwAS4OW87/UKPCo7sHawtJNxuGzkninShm+fyz7PP7wBBg3/1Q3cUpiKJbzbZe8HEgm0aF0aPq9AngZfF1FegL/+3VZ4//7ke5T9ZqV/pNcPq/BT/Gn1r7r8IwqjxEcY/4hiHxcxPt1aUAqBvN1UL7q9NoFL2/iktEf3j+Idnz/c/NOKDQF95u3v8+S95i01/3fp/HIHcIMPzPBhtQjZLjUa2GCx0EIFbgtyCyj8p7I8C9PXV2H6R4HYpaT9oXYBdm6/lcd3A1mGsv9T7O+98z8CX0CbsmAF1eelYn9450PwDfY7H1bfty5Ao/fN5HP3X/Zgn/7zsm1a4uA5ZfkB5oCv75O+/wuIF7799R/kAoI9SRaUqgXrNyF/G1o9t1uLCgC6e/3rwK9vIOZcYF/3Pere+3UwHHDSx3bpSyCQnWBxcP3KI/Ds/7qTf8dpExd0kADI9TwSpj0Yc6MIx3GSjryIRNCIRN0Q9oiN59E4toEx8NsjMCrCPJiGYRd8kTSNBCjAe2Xl16UJSxfZFsGAST6CxA5/ewxuBe9KvZRYLPZ947Ao/67br29gITBSwNoD8/rsIBrxIJT0Jvm6vsLUw7G55u5cKlUp0OQqmh5/KFN69pwDjKEXOdnFj/3trjvWZLKHEK2Silvr4no0aXkot+V6v7PIy2UiN/5uK17lYhbLmZq78lGRN5YjjONu2l0lQ5zvkXsjdFs889aVW8tneTKh3JUzDI4e88Egae00E1cMpyHo4BMyGXgaoq4zskZLf6aGbp/k09nL+Ck/BiQPnW3uctuQUH69Pehsyixvf1EuTjYmQRMY5xvnF4gwZg4+NdHOpI5J5A4nFduY3DgTtk/GljWM6xOxr4Q8Pdulm8R2ioZJubZjMSMpeWtCAUR2PLk3suuYnnfkbquY6eM4mvEmwvX23ATzFqNbeOMhNEWt5yBFtAfWomRHr0ksgTG2PmDbCdrJkKhmyV5+7IbC3QrY3aMtztywKl2HWVj5EA8L2bkuosYh7dgz0N46sYfdKYUnHuvRuYPn8EwKSiHN0jXi7ts111qkmY+BqyFWc48OcnelcuU+mpNhi/KsEKZ7y4kLJOFUdOGHe+AwhUD4xnYvVgpnV0y13SShvFPOqXixsOCgyS1n7hwd4Y3wsVdy6crTVsuDzoM0dBJYhmGU+4OAGn4nkjrZziR8Dy/0cWyzKjcdVndTSTqKJ8ccfTnL4xt9JpqI1UZqfpjTJAvbPlAY6DHA+IgOkT4nBuoms2QKY5+fDRJ5KLVZd1ruZXcotAfYEnDJcbaswRV6PV64dUo+ghOGjCi+m8527ON5d3bn8XhkA2XeQztsQ1on81i5qs0S9zJIW4M9whzPyoUJzWYo0KKT0Re2Uox5PlZ75tHdTjnSnCS4uxlMvp7ds2cZmY1bkVTuxa6UiDtyTNPplMnwCYceer43Syw1cLMRZYgDZA/Fg977xjww6nqveDsRq0Cjf0I9Ns7gSTtFKn1Zq3Prl/NZocsWY0DKuCE/mV5x2VvzRkYnTGLH22m0Lrqr22q9P6EurqAovpbnI/8w2iM27kl6FshYo44gJ+5eq2G3m6M11Hqd34btROWXVhQhTRSbLdxWZzULcNRuMvPYJlbRd87RN2dk3SqnU8pSOr+DeYKIkShWdTuXT5O7z4i1ft5XpuHWGebJIKIPaLU52iD5Hzqqnjf8sbZU7s6P6tW8H4ZY0yR8E1CUbvrmMTbNmECVrV3K+ajcaLWm5iPLdqjY2/R4Lzl0LVz1G2Ra2Z6XHFwHfesZq/eGtpfApbGjYVWeDnfTZdHdabs+z/Axh6kb2CicdyXe5tKtMVK16Cl7EPn1dX3jhBm5kXKtDHjvQZdCgB9nkRlu/FAShpmGbOqnR36Cudi4lO0hHfdreFbMQ5ibFh2hN9dmiONFpMn9YeaUs0UZZhXJDYn2do/ASbeV0QO/15w+H209kxWBCBx2cC+FenxEN2G8+xZxPEvUYOu85+xvuyhnDqRdBEZ4k+gqwQbpkEtismUEYzvAG61wTWFCadmSbiqFB306PM7FeT7Pj9G1CRnRxz4a2TNjRhN9UDbHTSlsbiUHOQGhMgaKHS4ORvNuS96ZA3eu8yN2vTIi3BASqyB55UqnNl/b9/O1v/R09hi9+ZH36uFsbhkKihz74iNHSAm59V7Pme722PQ3oqObwoI04yjLkrTVMRHxkUMtwBCborcwMlRMxnkSgUhfV3nS3KmM7+sDWxywykbb6c5GFI5Xd/F6h8d5ZKTCPbNZq1NRdrRTyoORnZxwl+Z4zXR2hq4FoyvBwdPmo765R/F4SXhVZRWU33Eif5pDaHMvL91YYmcZjiNLGQ6OG3eEmKP+iU54BYePrVTGcEBMaqKKI3eKBaom8D2TStPcxlx869eYiQq2r3dSG+/iro069VRmDb0JzwqZHavsVPN9QqEqi/P39mrQLqIPuoeumc0RLZ2xGB3Rb52TAzklsg4GIZmh6rAzJydhTvfE14Ic6Mis6zXoPsveCtOHHqShNg1CP9OVLkNekqCwPbYOcjwOQkpfo81MEQylCRD5gCPxUQRsK0q+hMzzbFHYJVEZHj0fFIb1B8hK5LTZ3ruzuOUMbpqHiPVPJ+QceXXs9njIKNTtFnlMm50wR8E8nJl5Z3vI3T2ZdgxdB9vOitl8Z9BypcQJDqq2ZM2zw9+N8X543DpRg0jGwaUdisvcyELHw+Z81W5lOca3s4z3l/PuYto702TDLF0bVGnyadH5wwBQIvRsh8Ma9s1MVU6VjFuWZZDDNuPhfTEJ1wPKZdrBVQrgYx6XpngutynKHTj0kLb7aMPNNKMdS+LEuUrAinFFxzCrlBXZEFc7vdXb00OTBWKHuTuEcfhWeURCy2uaUAF6z+vrBiqqVo/lzL/zRbMe79SG8cNtMJ5lxOKPJ3s0EuWsJXYVErdDoTNc2xuXrXWwOR5XfGuQe7+o1nIZrtkyvuwJgGKl7Mgl0QnhcG3bxLzwMDJ9zZ18zxipPjNYsTaq3XRrtBRhcjt3dzWeYeyDhbmDroSXRibCTuVKDo4n9cZYvRg/0C3d3KlrVkHivMNqgVXzgt2ATJwYjSYu1Z2fGMsr1ocmNDksJJDKBRnI2+ll2FaXnSkEbGyznLiZr3tFK2IpjS93Dr07Yl4NJX2MHU0vDya258gyDRLOyjaTiU/jSV9bl0tliSkoYjpt6/je2+56XQqTubqcfe1wVguOT500xXR+e7v0D/oA8b1s7MSTTfMD5JiZzlB3DRVPj/ImOYiIaqkbyxKuG1eEKrALTmgXZRuiDuY0XpcW0a6uqBOu1MS6JYuTc031oa/P/iXGRTQazBT3lcfoQBxnpJhTTvaDuM8o36br0xqPYClRua6R+NQVzyIucdLpstPMurql51mVLrR9kA7MtkG4SyxdLteE24SCyVzPsq9Cpzlu7UelNldW13O9SBISyW4DtXE6ChKhOaPD3byOK34yjjdftMrYZnY4sjEPtqbuG47cg+3Bvb5hOwfzTsktgi4HxuH8cpfi9LXwpGNOpFQ87Q9VfDnvzyJkQCIXnjbDWOybayK2yIYNCgiixyI293k8B2IfOqMRzixkoiiShs6dzf0h5QwCs8YrYbA44zu+Q9wN7mpp9HpOY7mWD61nJWLMNZ0U9/pBwize4DM/KDkn3BhirkAnuJp2J68eU/UyKXllTVCHoxWp+hF5DgPOECKwMe6K/liy25GGtM1mRCIzwaasm+UdT6P6FsTVKAdRGPWGZGEqUlBwgcnwDj9tDEe1ZIW0TJ8/MaM1ctRpt5msdE3xuSp6/CDP1y7Bo5Tq2gI0IJrp7c/ZdCQIUm67uaMiiCRqq8Nb4WRlNVzXNny5tBa8I7N74kLUXWYxQbpvR+R2vvDHJMzpoVYmoUvX+lgeO7ARSIUz95guMJnV6XZKdETaUYl4PeYJUSEV56l7RWJIpZzvl0g6MTdPzKSxTXZ+Qdmtvj0Jx9GTxDO7ucklvaVQwuRZbuxAY+B74Z3tbCin7PKIHXRscFsXbIPwKguJWcWINQ6aNlQkpcC4ILq5Y6q2ehgyx8VkYQkJ3Z3l0jpTW1n318bN3Kodzfue3jropUNTK8g5vo4utLC7i4Glxp5JFYxnHeBdtmOTg6fqBCi7UFOvD/BVpCrVgqG9sNbSUzmkjgiBtJMmzO1twGFcRoLOWZVF0XQUTjm2+7Asjo0NWrmdiFCg7CCKZI01Nlloaj/uG+6Qzg+ViG3bwDt7i5cdO2zvGOw3IVMhG/vhOHLu2jp65JQUwTXCGZSDBHYyPkxKImU0F5ubuhtj6EIIkVxUy0jfHagBlHRAXUrM2KZDHoKS5lFJy33GFLQ6HsibR9narpBRuT1afoUh+VD46jGWvX2XllMEs7V9OKRYQhUTsuPFRssRSZCskPaZS2/0I9w4CuipZC+hbsXWZtbVLbhLYDuxHKbc8KwOGNO5RsHDupg9tDH9h9pZa9KJHnvcEtD9Y6IYL5a5A24G4s4kKfd8p2osfqjxuUN8LAQbFaxPLjhUwJ5RwXF1uQhHKTjreNDsjrvYuXZ00Z7WksnacCAXMalUfVXK2Zm7ab7C9NVFtAvT3TtWxJT4Xjm5oOuUUGtWzkWyfkDb2rBI2XrAKYpz4g69CZWa7e8YolC8LgkbcaMfHigSlAgjY3Ic+ZuNIBoQ5lFRh011g/ZBnYdx0UjpaZDHYIJHi8NZM6nWbMQdz2O8xbPcacbdKB+S8jzz7ckNUAWjrEFhzLs9ZKxgPjiok+/wiT3NPV+w9kNmy5lBzye0eNyvyMU53vqHCD9yLhxxerjoyGDRQqDnrYsMgm+x3Fm9m/fMRWqST8k22PQJ3AvkgOw7Xq2a3AGbtgEvMOy415UNqUtkJMdNeoBcD+oFuUXY0R/QlLpunKKLSe/4UFySvI39tU+sqxwdFaLZnFXBOF7MHV/axXpSDtu2alXKx9fT9TRPJpGLF1wKr469bu+uDQklWd8JoI8F3+hpP59aeHsmNEeHxg45ZcxoHh34ctvV86SfQvjBnaNH6pEerFrZLDdOdLk5m4s3d62BkOn2Np0uPBK7mK6iXohUuG1rSUXKNrXREh+FS4Gh2zV09CGowqLW2evGrZqvENVESfOYD06KPgxq0Ny5u5CcGkm4QWa3nhUncp8y3CHY7gR4HC7sOmGrh8/eVV0i1lwAuleRS8hCxnaAfJ3j+qhsHLFc59VGvBfnwisiDtrjrauG5lBp/LgnYjQWHvqdLizcm1nhbvu2gkL22pmhm64+QMbvS31C+p3FGobK0CyFb67nq3krxJa+pvuYZGGU8Fi1HH3rZoSilZgmdt5j7ZoIBrQOs+Bod/gZGWHyCPZCYV5dNxI8VJW8DrT7A51Z3bMGbMNwk81Yk30UNnNza/pZWR9cW9ru4C6wb80hIY7TqaHbh4Qgnpxu0KQo+XyXTvTpopBOoZMa6p436MFJxpl6KFN4HFvLTPxGx2KPPKRnkcv3SaunPs8SvIMmiWUVJ3dbsqpqdgSBHfwt2MvV870dLM6scBLsOSST6XU+Nge0a3l2SCZY5bkqRNsHhYUPGZlu2e3On0UtQhoqBKUQC3sCr7S9Nl2lGFfdue3oybYltqIfUsUjKSf4c0vJ8r0Yh3EjuLWyP8Oj0wYgcKnd8cYmKIYWDU2eNvbZTsWBmW55Bbo8hzDGi+keW7n2Wsaj2lgoEMo50iQp2CodbC+TvWmuJSsWu1vKgloZT2P+GEavG/VzHm7pMYBLO2twwlg3VC0IkSrZ0EXfOsl87FQ+8MN10W0rrAmcJjubwmygtZ8kd4FvH71QVcW1Qvw2VCaK5bj9uq9gwluP9j5j14RGnO5CYnF6oW03PjY1RHVtLwnEG/JO1nZsOG7rHIlmReBpwkU8GDre0VLtZ1HA8ev1kF0FrZ1nyM2DOUGJCyHZoYeARiEnH7TpYor92MAjrKNbjZfvKH3Gg2G732yQO7LHDnvai6rgpiG1Ovaaiz9cAw/c5LpWmjItGLEZVZWbyIp2pDVG5805ao0K2zc3fS/ozDnS7FDKfGeN+aOGHQ7Y3Zv3VFQfBs5KnZqrOaQ+ZmGrEur6eInRrYXnykzQ2NWKZsoH++NWymy2zTbVdDO0/hawlOwkl2NlHUYo3p4IYnjosbTf3UoT9vQmtQxjlpJAJSlG39JS5Hj7BwwosA8Le5KwzS4gL6N5mK2gCAfRehTXNXImhetVi1CYQxm8Jf2rOuk7KW+T/tGPDISImy4lBYxQ7lp7PomSRhD0zlxDCn1HlQZSJBax3XNPgq2a1smwUh8f3oGSCOtCZKGgeZ0EZ47xGBpP72zQaVB0ZEv3c96qNi0LanYdCe9y6U4wavIYSexjnw+0Ti1KoTnS4wxaJ5CKD0kGhJtqec3ZgXGaLAFDqd3aC3eecNqBeiA9aplWmO0F1nanPU5m3A2X3HtgQieebE5ta4w3FcNBXTqyeqcnBNkOl26u8rHDyT41pZLWfAzsdUMM6RHtaIbaeeJv0dpS0t5TTwHnVDESa3qIVyBWthlcDMmG3EA5dLgSa0jfmKWBgy2pJeeNwAiD56Xk+ehb+NDNUujag+yYW4zq7n2IO7DK5XNUqppukukdE/XHHmG68tgKLDuJDIIo11Pf3f1h1sngMBgpfaNGHuBnguzSa7sXoTiYDFG2RjbxC//m4jO5lkK1C0pzs2vGWaiEGGzWhAPE1Pu4BFq4IoEKic8IcoWE8l7rimzjrJ3YcczJOrVRvTExvqVUB0E3xLipEngrtNT5RBvxWiZuYetL2p1INQ6h8Bq6BnnT3L09SfaZCjWuhvSbGT9uhux630M2xXYYVIbbE8TPUcuZbIcj0qbD2t5O78e7ayB9NuhX/mpuSn1dtwJ21NDuVl5sxB3PIbuxL7TfBI/mglNikl5Tcu2Ciz1ItYPmepv1vFWEQcmhKDwR18bqorVZB1C/A82xjZlr0RhEjtve9wOucphpMmcOc7N73I1V73pmvGmvgY9gCCbt2e0sDA6rOR2DHniEgX2BzqDDllNLZW42GdvzqXZt6FuQo4k0kAGEyrTLnk6bxzyTN1MOiTw001qQ9nCreM3GH+KLcqdMTPcE6Xzam0LH8jepCvfpQBD4FSLp0DdKxstYZyMQBOJV6ezWdruejf4IbZIhwCAdIkV3Wy1GvgoOFW4jhylOJuUsZx9/efvw9tvJ49u//TrVcgLz/+yw53Vm8+1NieeZWegGn59rff73Rfvrh7fGT4FgrwOuNu/j9yOivzve+vivnpYuKNPrjaVvp6Gvk+DOjZe3e99SMLXtmulrW+XP9ybADK9vl3cB2+V1UR98//4Q8PdKve63yzsSX7vq672vnvfScnknIgxS9/tl/H729+EteH+L5+uGwL+GTb3o/H7qDlTdfII/bd7+9r8BgL5gI5UtAAA= -->
