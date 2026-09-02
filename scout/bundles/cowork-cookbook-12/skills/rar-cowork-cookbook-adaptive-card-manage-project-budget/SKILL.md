---
name: "rar-cowork-cookbook-adaptive-card-manage-project-budget"
description: "Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_project_budget", "rar_sha256": "ab96344307bd47a33593335cb1d49e4c1ca88a9042093f458e990f643ddb0460", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_project_budget_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-project-budget:8eea1b76f0d2736ebc9009dbb3e0ece62765f24a97752b9697c53c6cb9ab5548", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_project_budget`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_project_budget_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Manage project budget Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 ab96344307bd47a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_project_budget_agent.py` first:

```bash
python3 adaptive_card_manage_project_budget_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_project_budget_agent.py   # or on stdin
python3 adaptive_card_manage_project_budget_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project budget Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_project_budget',
    "version": '2.0.0',
    "display_name": 'Manage project budget Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-project-budget',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2fd56f0c92669f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/manage-project-budget'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-manage-project-budget', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardManageProjectBudget(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageProjectBudget'
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
    print(AdaptiveCardManageProjectBudget().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyLLlX+Hl+1DdT1kp9iWvXbNBoAUhhIQESOpqy2IJFrGKVdDT/30CSZlV9br7vttjYzZKq0wBER7ux92PewT125NVV0FWPL0+7YCVInMrjsMAFIiVuoiQtVkRwT9ZZMN/iJOlVRHadZUV5dPzkwtKpwjzKsxSOH1TZG7tgBKxkALUpWXHAOFdCz5uACJYhYssd+oaKVMrL4OsQjIPSazU8gGSF9kZOBVi164PKqSsrKouES8rEJDYwHXD1EfCFHGtMrAzKKh8hg+sMIZ/4Zg9sJLyBaoDrlaSx6B8ev3l1+enEH5/ev3tyYmtEt56eldl0ES5rbu5Lzu5rQrnx1bqw4F5B/FI4XUOCqhDAm+5wEMeVz+VIPaekf/6r6i1Cr/8+fVLijw+X56GH61OkSoASJVZZQVcxLFyyw7jsOpeED5ura6E8FR1kQ5AlRDO1H+5z/wmKcuRfw7Pfrov8gL1++nLUwZVsAawvzz9PBj+5amoh+8vg5T8p59f4qwFxU8/f5NT1vYNWCgMav3y9rh+iIUDvw0Nvduq/4RS7261wZen74wbPne9BzvhzKeXcxamP90FQw82ILVSB/z081+JdQLgRHFYVv+W3F/uggNgudCmh+I/P99A/hUZPQz6kPnXy+bQrX/HEjj8fbln5AHUX8m+4f/fRMdhCnPgHfE/FfdnE0b/RH75S9v+1YRnxPvyJIIYhnYx5Nwr8tvbbjMVfvnkfrv56dffoej/UcwuqwvnJuENpmbogbJ6e/vlU3m7/enXXz7VOYw1mG9vdRH/mcw/w/W2zg8IPkb99ONcuL6eRmnWpshHpCO/Zfl/FL+/IIYVh+63++Ur8n2+DJ8RMhjxvugdgu9ypoS6fofjz0+/Q4pIoTW1c3sMs/w//xNRQqfIysyrkJ2T1RUCHVyFCRiU3wdhiewfSf11J0ur1UvifkXg3SHdIUVYdVwh8wIS0zujDRZAmvv6v5wbkX52HkQ6th5k9OZANnq70+DbY9LbnQa/viD7AK6cFaEfplaMaPxmg8BxaTWseYuOsk4+N8OyUKXwTjuaIA2UU9Yx+Afy9d9Y5+0m8iXvBlO+pNA3FnSYi1QgybPCKsK4Q6yBq+yuAp8hx0I+KbI4ti0nQoZfdf4y4GMGIH2g5sA6Aq7AqSuAxJkDdfdCyMvP0PFlFsNqUA1YllEYx4gbFlCXrOhuBQfi/ToI+/r1qw3Z/kt6J2MCuReacgwHfCiMfP6cF8CLQz+ovqTACTLk02+/f0L+N/KvZt2ED2tsYF24QQYDOr7XJpiddQKHlcgQGpB6bt777fe7LwbtUlgZYU6FXghuk6G0b6EwWHB30Lt3oM2DiqB4rPQjbkgbQFyQsIJowTwvn7+kg4gMDi3asATvIN4n36F/d/d9ncEn5QND6CevyJLb2FsUDs50ssJ9QSQP+UAKmgv9Wg0eDbKygoGbg9QFqdPBmVb1zYUprNElzJ3S656RuoSmDpK/2lD0AE4CCcqqviKKsIG1LovhrwGg2/JwdpaGg+Mf8Xq/DYUUn2CMTd5FvCBrANFEcquw8qCwSnAb51n3iIA17n0+FG4hKWiRoayDwUe3rL5FnvKnXcTu3kX82IF8qXEUI5H/v63KoDM/n2vTOb+fish0vdeO9wAb+qvB3ntLBluGm+RbtnxrI94Z552Lv6RxCJ1SdP+4j/RuMXUfc+e3uoABo/HaTf6Q3cVNbljByBhcXRRDNFtf0nfSf4bAQL+UA3/BBI4GOsg+FhyevmsaQEOH628NAHIPuiEZYDgjeW3HoYN4ALi3yK+CYsirhyNgmIABXZgITvCDVQiUDkMAykegEiGMV1gYbtCtYX4MMN+C/WN4OLRV+d2vLgITCLwg5hDPMCZLxAawNxrGQBQ+3UQhCYAYQxU/EC4DK78rM/S8DwWtwRdZYlXgew88HsLYHKoLXO8j8aBUyLkVxLKFToB5db179kPPh6+gssmQBLdJP7r7YSvyfXX6x5B8UMdv9A/b9FvYfgMHMnaRlDcSgiU3KmF6J+ARQDASbjX85V6G73X+Q5fXPzT6P/29vcCtsOo/eu4VCaoqL1/H43vxe699L06WjGGMhDkoP+rg56E+fb7n2OdHjn2+59gPou9IvSJ/T70fRDzi+hXBXtAXdHi0Ch0wBO7jA9EQPk+On8nh6ZdUA9/c/IiFgdkg29rdR4F5HwKrjF8Afxh8LzjlUKdaWBpvPHcrGB+h8EgUSKOpP1THMvsugQebBsfe/fbBx/BROjC9O3R2Phi2PfGgfgmeXtM6jp+fUisB/9Z2ZyBdGK4QjmGbBEGHrVIVgtvVR9s0XPy4zbslFWQDN3sdcgsWONjiPiMf3eoz8r5/uO3J0hpuoH4ZOuVhSTgU/vkY+7GHtMET3LJVXT6oft8UDQ3ao3H+oxJDSkGNIYWXgy7vOTqs+Ach8Ivvg+KPQtTbFyt+EAXk8qEswmr8SO8S6unCPgpSeDOkHcwkGKE1nPDHZeA6BbjUsBC7g7nf8PtmVna35fcbDNV9Z/nb0zthDN/vXcE9cOCEv9O8Dai+F923QbY1SLi1WDeQb83pGzQwHIrrd4/8oVN4u4fi0yskHPD8NEBZhLDj7m+b6ae7QtCSb20tlACp43M5NAtjmElQEizh+WBFBGnvuwWG26F7Gz98ef3LXvhfcMArC4CF2QztoS7OEDSwHQ5FOde2CYACB9A4Q1MeTlocw1C4zdEc41CEQzs2Z9kURbJQj8GbifXQY4wNfoAWfID9f9OiP91FwMKBU/TgMLgyQZIEytguyVgEQXEE/OXYmEtygHQwx2JZi0NJHOUIj6RYwHGoR5OE69ooSd9AfHSId73e3rvxd8/c2eANUmgSDlrjluWwDoORLsdYtAMI1CYcgOGYy0Bk4PIeywISzv+Y+vDO4Ly76UPowuYQtmbNsM5vD28P4UiTcOSCLCX+/hHGnGFBrG0tsEcFDY6nw1iyQ/2yt53JJWlN10DTBDX3k/SEh6xk1NN1t5xia0fzVUt3i7kaiByfMstN7dYen1yjhDaF1qpXByXZxz0VdyOWwgM/FI6NylNEG5ixmqeRsS2LSl1f1sHsCpOlpFR9RpnsrO70uEsZ5uR6uFXt8oMerlW1nK0OibM7zssxNWI9bJWna0DL+CWZXXoC+Cpe060R6vsaC6OL0xJ79VhSh8yW2/NOaa9tAqYEVbSmJ3tiB/YRbm/6EnfSgh2NTqbTHKjxeL5aHUx2uosNJyyuYXOh0cvJ1gnnUleY0AeTIxdr5bg1yMPStebFtJaS5HhdHWoSRmoM80sl5VOwXWKGG+Y7N6VamzX6JDtr4UkzO+qqT2Naj7botd2uIrPOi4m8BiE2W8Wr2WY5M06HS5WoWoED89rtxtlpXUQHlUX3fJIlAncIwb4R2PNZPZUrfWs53V4e+VPBPU5qJ5uZnpHI1Lpi+laJypLrzNN2O7NJ97QRTwLUxPfORVRjVuedc1nPCtHdV9AdwjramBh9LUsSC1EzsRNfPZ9ZzK8CtV3ZeS7OS6JZCdZlJcu0Yi3HdbGwuCk2ytAymLaLnE4NP93N6yXZheWoPi4MFtux1YkqucVG9U+S5FcdnQMOuKhcVjUt4N7hHLrTNbs9FvMRlybHVMNCuZzWhhrR86tG0DFu2FUglQcwY4zTbumvnWPdK+482umMAawsR3P36oWbhYFKabFO8elK8CI7dPiMapbbaz9bXY7smdU47rBjrOoSSc2MbKarae/U54lWt3q4DU7CiglWRR+Fq5yw7eWFsZeFbau5XEUnq8y4fRE2k6sn7DyNHAkTzqfE+iRIuca1I1NdYmN2tGH7a+ikUmPWDsNFl250Gs8Bbe10zdIPXlRM11S1s+dBd1p0UYvLG105tutQX+yXGe/wiWYvktF0y0+KfU7tILF5WE60DkaJhajNlaywl4RwUPW57Xe8s1QyNogsDbTLmiK20lZ27cnMak/SbLkbybUxS31NWSh9DViK4OmNVtDUheJQ4nwmz+zUiMeaQnqRd1hgStzG4fYqsok5TqOLe1pcPbAnRgt+a4dbycLKdOyxqw4j8zlxiXrWmaUY57FHYk6XZc7Ls/lcbc+FLVs99Ghpxo6FCy2WaMVidtgrRO/MNIOj03QmasnGkDKzkM3T8rCRvXwmB7I4BuRGcmd1BIhgujwXNFnND9EuXNFOnseJONJyg1HjKt1bGyqhsj0+NY2ZarPdmnNToC5TTJDXjF4GR2rqRdjiIBqjFb/frlBuu6sDihWNGdmtEjM84tpWIjhNvTQWZQXq1StybXrRNdzYcIIZTtbdRZ66DQpzdZWXetQvJXRfZUo5Wk0OozLDY2YhehKp7CzST6prdVIsDMaZgBY7ne5yNDS1bqoU9nUla6i6pSDB1FY/K66jnt3JtqmviCgJGJXto06QBS05mCfU0RhpZTLdukzROOGyg+75K/VMc6Mxozv+CPLbQjtTDa+cT/FyjstdFezby5ns9iI06zimJP2YBsfFyscUdp5kWa4tSbvXGuAHPrUxD95YCVsYoRdN1hMnJlnvilqXer+qdmnuUEY66oxQLIRwumn91UhXQ2/ZYHzujUn0eIijshWm+XIyTzfBBNMZy9YTehnOISML3foyqZeRVuj7icG0IVa4+GmyDdbgejDBKZO2YW+kgTdKFh5XSfJOPbssqs/783Z+veLNppBKSm9koV8VFOOlBc7WsqJJS03eYVesIZoIzTq5oUzKzAlpPo2K+rwVenY8nkXiVSXpc42Jk6khjReC6zVxNt6JFF3Pzxo2qhpCmJDBcSaCzopNtphel7y8DjU9SK2Nap5m/k53CtzcndAJubQWl2V+jWeZ50zmKAzUQyajR9zVDXWvh/2+CYXLzs/n0ZovR5N2sRaOUhMFG1e7GLs4x7aep1C6BWuR55onGFWRt84EY+8Rc8s5kNeEVDI66qSIZaajBStOKgrbMy30iklerEbAyOpgiHyPjgQ+8nfO2hxFeTLXiMzNC35jZsTaM8W9OVfxZdcbowSrjiZBq4cqnlQ1LHarEgXZTEhlfX64zHbxuGk39aluwfQk6d5S5fbsUdYvR1wKlnt1t16tlb6MLmyxYEIvEUjevuT89nCiC2Weq7LvJsKakaPK7bX1NKEPvY3nGuNH4cnnrcPIC+cxZu2C7ZyqjNDalcBLSEk9r4JLaF5ia78NugnHs9kumS/aXWM5J7uH/I7vAyw4yFN51k+210q8GGGIsjWWtGG75WfK1QEj2+pOddUl/urs97NJRO8ugJl6XIMrgcVKPnlgr3IlbFI3PaWkya84zu3soNzGJgaEOVGeuEYT0HiHFcG5JEYBdJE2d3pw2gsT1HKP1nxhOI2i0Mm6NS6X/rge77NgSSnXdTWdwVjmLesk7HfG/nrgObktUbM97tyjxhyXsY/ucnOlZFE9EfXDLtJsa+5jonFqsW7BuD2tcWvBjOa4WHBqcC2lDbfE0UBdnk+k7B9I32nsRbrfmvFlTxdZpiSF3+nKeKwSUWWXC0UId1kDFvVyOscXpixIFOD7vuBW5+siqsdNvMq9lO6VGa0UUzouR9hkyvbbibCet6scVIEzPwv8UY7EYzZTiI2tm22ZteNEyHcFrxi7kaNNQNNHdI6e0m4a7GF3pjV9GB9EW+2lRTKvpC0mx4utY+oXchEwCQwdOtKa1FVJKqk13XABbmz72NvmI15RgkZ02aRcKtGxJw/7qatk8lU0luk1mVh9aWyPDJVY+V4a8VPV5otIuqLucYnu5AO1XJPhEsdqveNgw1Az/qaj8kZLsfMkUS8x2TJ60AgiDOsBVOkc73W9Zxe7xCp32XG23M+uq6ziIunAF3KChtmI1sTINdVufq13U9AUxMwot2gke6OzKLKT+spoGXDnmEo7zFLwTbukwVW5GhcdQy2YzLVz4o5hs54dzColaL3LDu3Z85Yiky3R2YEiiXOJ+etqoybC8TorjiE7kbkkjM51BjFdi1dxnVv0QTtR5mbKqJqquepoTaFJz7Xu1BGYQgotXD9P82An0nzXyAdhK83sJpKyBX3ZXvVgZytxHmZJ6hY8UUqGcI05zDxvtrHCFZozDjG6DuB0RZ4ZmBzxWLOLY00IJytN26gKPsGiykx8+hAfBVGyL1M56tC1qe/yiE9jcZdiG9m8VBVtTwDD7neycjXP0r6RxVYJjOk1zphCOGU2bdSHZKc6LSNxm+tSjglXP7Gd2nN+zC61i1hHxWKpLTZEaxLqSLui2VZNjUCabC+zzXV3SZTLunDE6VzHmXW6zQB5jaleOGyqjq8zlSh8uscu9gUFLJ5NJibEaNwVfHEK7NizNIumQxtk2cHQRM4/nhrV2mcWq9KmMlPsOs32Lr+5MFfYsTVkdCJC+ThXV/uAPtBRES0yWWmJCc+wk2MkOX00XwboOsm24kxcD7WnmqF4uS6PZ8NJ3Sl/OTOWAWaWSLVuesgbXu+XwsQN/bF4IjJ5saMVyT6m0kJh7WW10tmcOW4l2FP5h6MRNRtCCklcr32DOk69RCHJ2czeG/hSlFZ8yMwMwNm6ijVLYc+xTI9mwJpTolZW3RIVCAEfoWMvW1M4e+kKj0sueINei5Mypltyw5QqPSNMY+yIhoNDnph3fXnmicN8v9V307NbM0F2vcQZWuG+EpLqKXN6ct5HO/zQ2CZlm0vGyi/pKTlfm+1krUVWFmveXBEEZkSQInZeJNm6nBZsWsBtp1hbTBfz/Ak3KX6sqy5AxZGOra0JjyZj2NIr9mJLHJM1AdspK2EW8zZap25sg2o7Ox3HMEZdf+VcK2Zs8lx69kfjqm6aEb+YCI24q4nReLph3eXKAi5+ZeTS5qYXOuKu08NlxLt4uDj7EjHjUFltxkIl4BPbYpTleLve7Sc+VTnspY2O5Gp7lvs2SqSVdCSWzXTSLShlHNKrkNjLTNXV5iRs57h7Sm3USf3jdlRVmZw6ss/FnMpmVD85zlbKOec7esQ3srIjAh/zxHJCu8CjvHFxOK7OjdoIK3EhN0wgkqcqdo1uRmhjqd7hKoxZF+bCies3Oc63lajGcPc0skJLH4FSOS0CyjqPTQOE41HljdrrNma2a0/XVvxaO/FsP96R5KIq1L4eHUNbKBhG147Xqa2sjl3ipiSexpRrBrrKjphWSWxXos6nsb05Eh4Fg3g6U4XUbfTOXC02uKrTR7WFrpabTRlA3tMubMbEBdF5Aj89O2TLAg10Jr7U9xfaUU1yQTsTsu0s9SD4x8avsiPFEWLW7ZOJa2PBqlFLMnAkUi8WhzYMwsV0fIjycTHxSWfT9gK6oH31upa2hElubCUTBdSa0lupnMb7Kt1GpphqR1HfzOg1t5ZnYzfI+mlvs8o+kGl/LzQdjor4eOEujfqKs/uTCpIoWaKnYma72bwH+aRr0345ARuDChbNpNxnCoam3rIAnOsqtbNbwJqSgf1ChKXeZxZBUNAKv1n2lhgAaNECNWycLOOMWOBVOZEnjhIHOFYc5n22VioOM+q9uwHExqysuZA5KBeTatjNRuc1OQ2PoOXlvk5twdPq+oxepUzsFO966rwumx6W7GYRb7Kgs+hzwlWLiYLXVBsSAW+t3CZLxdbHD1w8LlanOCVEd87R47YAvSWJ44Z11HjLkiJolj6xqo/0BcbIjFgz24wozjVD9mqpA2qD4ast6dnsYjw6ECtWDhp1HKwL1WySZgKkjpXQLjBYfJvrBjMbWSOwn1rGEUioy2OAig/txjFG7Ga7nkwUIV4eZv2Y42Tez+JNX12pM0ZFKb4lPAt3TNvNM2dsLMQTeciOubioxABdHjeZMstgc3m8aE3YT1DVdhK9YAA4bHIaZzGA1/SSYd1Q2fFlWi24eFWy1VZi1EXLyhc6F8Bov2ZJh+frZHsOaXSyO7IOLl3SzicyWxfVs3KZth07O5+48OjGnqZi5yUdpyXZnwuyKoi1Lc3HgNWXcCfqyuxsJJoZdRUsu6jg9tLpKqYAfuSOrvGpatf8fjEWstSdR2Fc4RcyYmNhrY/Bzt5zRQzEs5CaLelMcD+d0I15iCehVEdhIAluE2Sw35wGJ42a9UmajK7agmHqGG7ruO3ZsTf2PHf3PSXis8U5PkXyluefnp9ub3CfXjGU4ujnp+Ho/3GA/zdPf/0+zN8ewggGY56f/t8dS96PCN9f8N2O84Hlvt5Wf/1bev76/FQ4IdTpfmRcxrX/OIz8b8evn/+NU+FBQHd/Ez28jbxW769AKsu/nVuHqVuXVdG9lVlc306tId51Ofx/lPLt8frg6WZakg/SfjDl6eO4+63KhtFeOIwJ0+E1G3BDqwKPS/9x1P/85HbQeaFTvhE09QaKfLD38b5pOKwdXjg9/f5/ADXEdwtyJwAA -->
