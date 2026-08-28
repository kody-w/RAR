---
name: "rar-cowork-cookbook-teams-update-project-inventory-levels"
description: "Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_project_inventory_levels", "rar_sha256": "a3e6313e1698d86e3200c7df09d500030c2434e29c350dc6a84bff39f548dfa9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_project_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `teams_update_project_inventory_levels_agent.py` and in the RCI capsule.

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

Project inventory levels Teams Channel Update — Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 a3e6313e1698d86e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_project_inventory_levels_agent.py` first:

```bash
python3 teams_update_project_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_project_inventory_levels_agent.py   # or on stdin
python3 teams_update_project_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project inventory levels Teams Channel Update — Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_project_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Project inventory levels Teams Channel Update',
    "description": 'Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-project-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-project-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68032c2774d33aab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/project-inventory-levels'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-project-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateProjectInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProjectInventoryLevels'
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
    print(TeamsUpdateProjectInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abOjSLLlX2Hu+1BVj8wU+5JtbTYCAUJIaGGVKsuy2EHsqwQ19d8nkJQ3q153v+kaGxvlcgVEuHscdz/uEdzf3py+i8vm7fObFjgFJDlZlsRBAzmFD/HlrWxS8KNMXfAP8sqiaxK378qmffvw5get1yRVl5QFmL5qnLBrIQfSAydvIS92iiLIoKpsO6gsoKopr4HXQUkxBAUQMEJZMARZC7Wd0/UtdEu6GCgFz7ugcbwuGQJo6TvV4wvvND4Ulg1U94mXQsAIJwo+AROCu5NXWdC+ff75lw9vCfj+9vm3Ny9zWnDr7WGJUflOFxye6uVv2rcP5UBC5hQRGFqNAIUCXFdBAxTl4JYfhNDr6sc2yMIP0H/+Z3pzmqj96fOXAnp9vrzNf059AXVxAHWl03aBD3lO5bhJlnTjJ2iZ3ZyxhZqg65tiBqgF9hfRp+fM75LKCvr7/OzHp5JPUdD9+OWtBCY4M8Rf3n6CAAJf3pp+/v5pllL9+NOnrLwFzY8/fZfT9u4DaSAMWP3p6+v6JRYM/D40CR9a/w6kPp3pBl/e/rC4+fO0e14nmPn26VomxY9PwcClAE2n8IIff/pXYr048NIsabt/S+7PT8Fx4PhgTS/Df/rwAPkXCH4t6F3mv1ZbAbf+lZWA4d/UfYBeQP0r2Q/8/4voLCmC9h3xfyrun02A/w79/C/X9t9N+ACFX95WQQaSo3HcLPgM/fZVOwj8zz/432/+8MvvQPT/UYxW9o33kPA1d4okDNru69eff2gft3/45ecf+grEGkilr32T/TOZ/wzXh54/Ifga9eOf5wL9RpEW5a2A3iMd+q2s/kfz+yfIdLLE/36//Qz9MV/mDwzNi/im9AnBH3KmBbb+Acef3n4HJFGA1fTe4zHI8v/4D2iXeE3ZlmEHaV7ZdxBwcJfkwWy8HictBP7Oud0AymjaBAD7GveitNniMoR+/Z/egy4/ei+6XHQz/XztH/zz9TX46zv/fX3y36+fIB0IL5skSgong07Lw+FLAeit6GbFVRO0QTMASnHHLvgIyOjj/AXQJPTrvyX/60PUp2r89UHpyZOnTrw8c1TbZ8GneZ1WHBSvVXmAhIN74PVAS1Z6wKQwAQz7Aay/LTNAxt2MSZsmWQb5SQN0zmQ+ywa4fZ6F/frrr67Txl+KJ6ni0LNMtAsw4N0c6ONHsLYwS6K4+1IEXlxCP/z2+w/Q/4L+u1kP4bOOA2D4l1eAhRttr0Igy/ocDAMOAy4GFPLwym+/vxAGYgpQ14APkzAJnpNBlKaB/w1ubb38iJEU5AYAZgBxXpVNB5gaSrpPkBxC7/YCpfOjmcvjubz5QRUUflB4I5DqgOW8I1mUHdSCUGzD8QPUt8FD669u4zxMzEG6O92v0I4/gMpRZuC/2czHIDC5LBIA/3swPO8DIc0PLcR9E/EJUue4hCqncaq4cV46QufpF1Axvk0Hwh2oCG5firlOBjNUjyR5wgMGAWS8l0s/zj4H9T4HjOC333Q/xjhzfdMfda75UrSvBHCa2RUeKAhAadQn/lwW/vYKqTYu+8x/4AcsnSW9vOC/vPKIwcO/6hCeDQX/aiie9Rz60mMISkD//7uO2dSlJJ0EaakLK0hQ9dP5CeHcHs1QPzsqUPsfkx/p8r0f+MYm30j1S5ElIB6a8W/PkQ/gX2OeRNU3AKfT8vSQD7wOIJzlPoJyDrKmmcPZ+VJ8Y+8PAI4HVQEAQAaDCJ8D65vC+ek3S2OQpvP190r+cCJYNnA7CDyo6t0MBEUYBL7rzBjEzZxYL/BBhAZzkt3ixIv/tCoISAdgA/mzFxLgIcDwD+jUEiwT5FTYlPn34cncHwEr/N4D1oL+M/gEWSA35vhoQUKCJmceA1D44SEKygOAMTDxHeE2dqqnMXPL+jLQmX1R5nO8/MEDr4ffo/lhy2w+kOqA6AJY3maK9YP707Pvdr58BYzN5/x7TPqzu19rhf5YZv72pXjY+M7qIK2zuUL/ARwIBCAI4JlHZ1ZqAbPkwSuAQCQ8ivGnZz19Fux3Wz7/Q5/+419r5R8V0viz5z5DcddV7efF4lnVvhW1T4ATFiBGkiponwXu47MAfXyl2sf3VPv4TLU/CX9i9Rn6awb+ScQrsj9D6CfkEzI/2iZeMIfu6wPw4D9y54/E/PRLcQq+O/oVDTOtZiOoqO815tsQUGiiJojmwc+a086l6gaq44NkgSu+FO/B8EqVmXOiuUC25R9S+FFsgWufnnuvBeBR0QHd/tykPfcw2Wx+G7x9Lvos+/BWOHnwb+5dZs4HIQsAmXc9wAGg7+mS4HH13gPNF3/eqT0SCzCCX36e8+sDNPerH6D31vMD9G0z8NhiFT3YDf08t72zSjAU/Hgf+74NdIM3sAPrxmo2/rnDmbutVxf8j0bMaQUs9oK5jpfveTpr/Ach4EsUBc0/Ctk/vjjZiywAqc9VOem+pXgL7PRBj/MBCmbs5moISLIHE/5RDdDTBIDpAdvOy/2O3/dllc+1/P6AoXtuE397+0YaLx+8WkIwHGTnx3YugAsQqkAhuH4GFXj2f9csvoQArgN9CpDi4AGFo3iAUizjM1SAYwji0X6IsD6JIAiOeBiBEwHGejiJ+B7lMIQbhjgbkgTjhw4L5D3j8+tc6pPZMMxxPMajUcJnaYfyAhxxcS9AMdSn8QAhWTxkmIAAGL1PTQFRvlb7XN0M5XvfOqPyWvRvby5FgJFropWXzw+/YE3HtRbuKd7CTQbf7zh1xI0KyQfdiXAZRteWZ8vLfHWZkKSVTYy3yBREfb8c7U7ZTavDac1yIZaxt6llWttwFZ1dL9eqELk5OfrFBbMvJHlRjgmPOIO2UBRN66+M1lumonuJgXp1CytqmreNnnnjhBr5kLCapRV3mIIXiRZktniyNB4+BXLBY0J9trkTrria2Uhl0xQWKly3axipzV1dINlJLmptImJUvVT5JtYGCUPbPKuFEqR96V0NKjjo7SLA3ZHsx81+PZDkMK2N7f2iXIQztYsaOejqC0h9146rzlduWnwe0ThlbxhjxvuBNxOjXecGtc0tMghugjhV+vUYCVSt1RppKQypTmbCok1aWTXVHQ8KHPX8iN4Gce2QRRO7W5NTKMKobXO/vudp2rdNOtJrF+1o8b7pqW1IaFvi1DsboTaVlUy0DK4JJG55lHFsM6G6ap4fHo2Dores2pSnS7LvTT27uOR9fVzx/krFs1Cetvm+DLd2XHtbFFZOVmEVOre3kqYt2POGFsfKKO0kJq32JBaF2R7rHeulEbw/WBfxrCwibO1a+07rLnuh2wVenmuhsrBMlWK3971LnpWpPUwol3FmuvdPvLtBdIsp6rAuzl3qkMxhVd6928Lot+oQs1ooOLHX9yoCrxuxGzmTyJ19eNE30nnVH3jp6Laxtb/HNFmdjKZFz7B950iD9DabS3lsFsUarfjLfmUyqKhet/mB2dzIQKH0YYeNMaEvrD2nxdHGo+KsU4Jb4uPYYu0kF8s07TPmi6db1OrDSO6mQylLjrC9nJm6rslqsg2cNQzUPXc1VdZ1w/ako53hqRlhrlqIu4VIwjzHRKswpNLTKRvKBbOzK3bThhW6iMgg9vxgjfLOakPf25NLnFQtQw22jk5JcBotp8x4w/M2p9aSxuNk56rOt1KpH8VQAEvTMKNIBGww+pQQRcHeLY/UhCDZVqQz0b3sl5qcycZ56XCdaJj7q6Fp+7uHyat4fb7Idsrn50SRzJOu5p5M3oh8e8V789YMHLqgz/LkOturHCtkIhxhORPc1IvFy35EAxHWyjJMp+BC1jl2Gg3coA+bE6y2teHRXFgeFodRxmOwN5HvLbzte4e9mJ5Vj7C03G2d9rQQ0FxHba1nDG1HsCUf1kh2GUMiI+n4jpsnxFiwnroadiLQ3Ei9vjza7e0MI1mdYe1wpJE2rVQmwrXlbt+sT+W4WEh1Pko7mLWPRZotlkbhjHjV2LSrIRvS2SjKRLB84fskftX4zVFZJLV5NU/w6Qh4mxQaUVoOOsutqHVxUzU7NrSx07N7xok0IgDp7mkfw2qBp/zVVOSmvqDHVV3vWi1LcNxnmYU+5VSqdIFkNpQg393QYlqwWaFBcpVXXtOoxNoXO4pAq0JxzKPVV6IYNhThKyvGoQKboxDyjBcuUzm6W+H6ldZq+2CYKab6sOWAlj2d7vSmb+8ywxEtrbH1gjtcGpHW+ojhsS3i4M3ifiLWBH5FKfggkquJPSu8eu5acrvSVkNgMBQrbIcEyRW1vEXGfbW+6trSlLGYqe6di6RbptcRcz1NJbPMbTXYaHpG29f7Qpg2B7DDRdnFvhrdg7pap2tfEDnrytteiSawHjon9cBYZ6xdc02UbjRrVI1csnC3ZVuYzmL5OKpLE61MTqRyLmGm+9ktr8Oe8VZLbgsYfC8w08XY1fDeaZM9T4iMkGXq8X5iCP5OnoN7Se67EdCQ5OWHWpnWBU4vADmTQTsZUUpdnClfDfy6WynGaHu5Crf+ym7H5Eay6C5ZD2i0xCxkaNX2djwVI+kzwWFdnw+Hqa7HhXYi4PS6xhJYMDmeHhkmw0XlKBlychf33t6pJmVKWk7b3s9Ure+XuHSzLV3l8cSN5SxChXHBWaGY26ZnoHLU0lTaGLLj3MXSKCJFrAidX/XnDeMctHxX72tjhzArqps2ehz6hF5O1Gjeyv6+FE++eE446iIPSlplgj9lbXJSDR/PeseTkVsl6gZ71qfltRAKI0eUbS31mmuj9i6uTw6LrQ73ZSIva34MHY1EM1/VXO+sEHlonXOiPd8Q5h7AK6NzlNQx42RQ7S1+ER0SXXhX3pycJSHIsRa3jl5asYWrU3NYuBJVnGPalKIRtnDsEKOTw+U0uRaxE0E57Uo75aO7PsBitbSphtgFKK57snmSBeFw1w6qkeGbW7Q74V2Igl4kVctdJOSqhdyb61qNTHnU6E1NxqC/ygh9zHVFRT1ERVBzmdqYNNxyQvWjAlbIUdL8zdgPK8yMke1OKc6SNdR0bXLdHRX5WF4I1NI8i8K0kGB3PQW5MWKpkuRbiUOZUxqJ8agSrqRdt2qCWZv0bIy3C3yBxZSHp/yK6Va6zQry2uFUQhUWj2DJJRM28BZG0Usmc/sYU7mKo86Tves31L0jroqhDDyqWkTcUb6wOZxAd1iWlTLsuDLX0l2BMKp3CNrtStJa/mwnEs01S6szeVTgeKU7+rtDsystnuPkm3IUYU/dZwN11IRIIw46MsH0tru2nn87FM5e00A8lodSY3LUWMtUPNUOtpVrlSvGLXKb2AM+XOll6ngdT5joHrlkB1RIAv0sVcdiMFMCz1cVSno5bozDdUqU1N1X7Jb2pctZjHNQI4SrM8Jkcjxxzu12LCVkQg7rzq0ut/219GX9vMmibXUTQbPg2xeFYLlzlnPMyjqjx2kylVjlOCouFKEjSlQW12ZQ8KWIZyNR1iaNodec7XAl3oHmU0H9Gl9rYZQ3y7NxDTN30giJSBNnea3QHbeT3E5AHcJTNrLXxkWVkpfbMavPIhZJ+1yJj5zPIIt6bTUaqrvqQtImL2rLImrrEBa8G7xJicZCJnnBDdPesUhfsPmmUDb5Cl0OoWEoknaMenUrokzMldLa5DJf2mln79qQ2BGrbqR23QnnscUN1yzi/d6W962+70fDDopDchLUq3RaXe5e3tU1c05Ra4vvL/vzQkYzuvNVttgtLK5rujss8f4SZfAVLem7JlGrOxzI+SHbl3KLnAOi9SOqSi7CHdsjvt9URj1sBJ/eFEQjDL16MiUX3kZFZJuuQGS3/JwdlNs5O6KqJqfXnD5iZeBs8Lbir/k9q/h001sMIdDctqGbw76XkWlr2bBV3vfHM4kze23js9odx0ZhWJlonorBoKHoyXC43rwMoFHl8DQCXYimVvsg2lIZdon6vrhcqnJ9rWMt2axAD2eQgNDtfskilSsN9U29GzmcjjXp2DsRGQXszJIec8HMqV/feD3TN2nONtddYtATzuN5BZzMbBkYU4dif9qWtas02uZ+4G0pT1ecseoc+CyVcHcMjoK9LZL+HjH3614pNbjYYEucOIzbQq/6pAhztqqOBiG7AijIk1Idh/2Fzm0npvEQxMgFJNRRWBdnsagvtMaswi12ybWLjyU9uV9cEPHqrhDlZl3lI9Jj8DX1rLQ3fWopRN6Ow268xPeKt7xIzSkZsKOuSOHmfhmUrPIPPVoFpRDUO7tcrs8qaYY5zWH6unZHbKncjPjkjecCQ7zicOWT60qvd9N0l8TqekL0JM5A1xwaaYYvSK4N/HuRugQVqKh+tzBH4VBszYIw5uWNlAZDmtLndQ9szlVlRxM7TDrILNYROW4NyuJ8ZsIaFglW9Iewymtyh4u41LFtgVGMqFoDPNLYlibtkfD6gXK3/I3FKOJ6FbVSu3Zoj65hknQUH2mkiJx2am4ed9xpR1r0YltUt3XTVjWJOUQJH8d0lCdjGvvjBjFpZiDsW2JFy4JTz2RoU8TIL6hw3Eur5dln+cUZtCKNxdkG6/n+VWcRi7pfqIN70GnMxJjKpsBWMiaklg7HLh1kqZfXMSxaZTN4GEJbN1IsKHexYJMBjopLZkkF2+CwMtDYyGZrHD8MoxTvDfoCGlS/2p45Sqrkw3LEFIm3TwGzWur9RtqGjIykx+NqKIisJetoaQi0t6tWCccuSU0S1Vu0PxJV4dk80Rm3Ad81F72MuB4EUU8H15u36waxrHJNiehsCpiKvF93YHsKupB7MvIDtbvgE7ce4mjJDiOWg9Y9vOmr8ORzLXE9BTgFdkZ+1uHYasHbW/tCS/Vd3rGn6LrQ6aG/Id5KzaJD3FMJo+2viOGWKH5AQoJqWHuhXuleUoSWUmh6uaE4ZZDXCctIMXII92Ee5LeE7uo9dkcLgVdj295kXbPGDJLu9r69UfntCBsBQ+jFlj5IlD3RnHpcZjCVuYeoKQhdvLXLROw9Xt4LBRZRpg3Kt9eGrLm7ovztRLgo5XdHnOMbpmjQ+2FHO8tQ2lE7glEK4P/wuLnSw/oUFcRxIRZ82O9bovf2ZGXJQyS6wr6BG6JaNFxEeIfbxCEHdBkmK0vHQzKd9ijHrXsDO252QqF3UyRvucndxVTBs4O3rfusPyJ0QmownxLApeF15V9Di803uBy4yWYQYb0oMzLRVrA7htkeX+/0gamQ8Wh3LXMrWGXXsSrKSpiOURha4vRdNo4kzNXyfrmQdjx9I6QpjtaMJ8mTtY1kvWkPzJAGZxbk/7adovWaO6sZp0484LFyYrfuprB6Cqbv3XYCvrSoQZKJvosVNnTTYjq1S76lq/6GI719wc/5cYlaByJh1+TRGVJmvUKKdHvxfXOCO33lYTl+u+Hj0in88DKKEcy02IJUbsrdRwf4SPkkOnkhe66WIT0UPVKvs6WNIrf74sLwts0Wfg4LlBh3HoqH052c1n0INhLXqXC94wIeMXaIBZXFR7EdNg5ca2J63ZZXXRAwQsnvddPGDLtwsU1n9iBmkauJ300vYiubQNglIgh3xegY+7BAkWoUEzPv+sNw8b2KTFF8cx3Mtr2yG0Y2oqtdH3hx2zLlLojXp8UyUkUQ6csJZbRLcJ+c1MlzfHLTts/xRVBn9JlyA+1uLZmtttvWoZfBhZ4Lh/i2wOu8o2/DANjA20dLuxc2AOMlmi+wi2Dq9NFNzuhyqidz9MhAXLhuNlImu/cbyR6sgI73IP40O1xjR3GxgGWdWCkLkzjQQme2YG/d27twsi+Ji8Msh3aLKTt5hCRvrmGV6n1zvCgYuWMunhbvq3DXqRXLTnuuuuruLQiWuM7f3GkSidvZcUtFtviiuRuxXZzkwghOq3u1UIJDtNA9NMZEHelR605RxCoNwe5Vzo+w5CrH5fLtw9t8PP06ZP5rb5DnI7//ZyePz0PCb6+dHgfMgeN/fuj6/Bft+uXDW+MlwKrnOWub9dHrQPK/nLJ+/LfeWMwixufr2fk92b37djTfOdH8m0ZvSeH3bQcMacusfxz2fnhz+3b+lYf26+tQ++2xvLyaT8j/uJzZAWUTeE7bfe3Kr6/z9Mf7xzzwk+eI+TJ6HT9/ePNH4K7Ea7/iFPk1aKp5va+3IPOB7fwa5O33/w3VVHqUySUAAA== -->
