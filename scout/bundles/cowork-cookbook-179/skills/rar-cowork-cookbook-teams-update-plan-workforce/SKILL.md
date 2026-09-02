---
name: "rar-cowork-cookbook-teams-update-plan-workforce"
description: "Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_workforce", "rar_sha256": "ec0f2ac2b60ba8bb82977df02941b4b2961773e0a4634d782ca896eccae23299", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_plan_workforce_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-plan-workforce:6a7648cb84745eddf4d0b99a1774534e3365bd27f256db31a1886c39290c18b8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_plan_workforce`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_plan_workforce_agent.py` is
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

Plan workforce Teams Channel Update — Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-workforce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 ec0f2ac2b60ba8bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_workforce_agent.py` first:

```bash
python3 teams_update_plan_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_workforce_agent.py   # or on stdin
python3 teams_update_plan_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce Teams Channel Update — Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_workforce',
    "version": '2.0.0',
    "display_name": 'Plan workforce Teams Channel Update',
    "description": 'Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-plan-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd49f2c068bb0b69f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/plan-workforce'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-plan-workforce', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePlanWorkforce(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanWorkforce'
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
    print(TeamsUpdatePlanWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjSJbtX2FiPlTVEBliX6KtzZ4ESAKENkBIVLZlsi9iX8RSU/99HCkiMnOqul632bOntIwQ4H7v9bucc92J356stgnz6un1SfWsDFpZSRKFXgVZmQtxeZdXV/Arv9rgP+TkWVNFdtvkVf30/OR6tVNFRRPlGZjOV5bf1JAFaZ6V1pATWlnmJVCR1w2UZ1CRAOmTOD+vHA+qG6tpa6iLmhCogqKs8SrLaaKbB81dq7h/4azKhcBwqGwj5woB1VbgvQDFXm+lReLVT6+//uP5KQLfn15/e3ISqwa3nu769cK1Gm8PlBrvOsFEcBmAEcUAlpyB68KrwKMU3HI9H3q7+rn2Ev8Z+q//unZWFdS/vH7OoLfP56fp37HNoCb0oCa36sZzIccqLDtKomZ4geZJZw01VHlNW2WTN2pgdha8PGZ+k5QX0N+nZz8/lLwEXvPz56ccmGBN/vz89AsEFv75qWqn7y+TlOLnX16SvPOqn3/5Jqdu7dhzmkkYsPrly9v1m1gw8NvQyL9r/TuQ+oic7X1++m5x0+dh97ROMPPpJc6j7OeH4KLKb15mZY738y//TKwTes41iermX5L760Nw6FkuWNOb4b883538Dwh+W9CHzH+udkqtf2clYPi7umfozVH/TPbd//9LdBJlXv3h8T8V92cT4L9Dv/7Ttf3VhGfI//zEewmoicqyE+8V+u2Luhe4X39yv9386R+/A9H/VzFq3oJSmCR8Sa0s8r26+fLl15/q++2f/vHrT20Bcg1U0Je2Sv5M5p/59a7nBw++jfr5x7lAv55ds7zLoI9Mh37Li/+ofn+BTlYSud/u16/Q9/UyfWBoWsS70ocLvquZGtj6nR9/efodYEMGVtM698egyv/zPyElcqq8zv0GUp28bSAQ4CZKvcl4LYxqSHsr6q+qLG42L6n7FQJ3p3IHEGG1SQOtKisCuFblU8SnFeQ+9PX/OHes/OS8YeWsmVDoS3uHoXuOfPkAv68vkBYCjXkVBVFmJdBxvt9DANuyZtJ1z4q6TT/dJnXAlOgBN0dOnKCmbhPvb9DXv5D/5S7qpRgm0z9nIBYWCJALNV5a5JVVRckAWRM22UPjfQJgCvCjypPEtgDKTj/a4mXyhxF62ZuXHIDRXu85beNBSe4Am/0IAPAzCHSdJwCrm8l39TVKEsiNKuCYvBruHAL8+zoJ+/r1q23V4efsAb449OCOegYGfBgMffpUVJ6fREHYfM48J8yhn377/Sfov6G/mnUXPunYAwK4uwokcAJJ6m4LgWpsUzCshqZUAFBzj9Zvvz9iMFmXAbIDNRT5kXefDKR9C/20gkdg3qMC1jyZ6FVvmn70G9SFwC9Q1ABvgbqunz9nk4gcDK26qPbenfiY/HD9e5gfeqaY1G8+BHHyqzy9j71n3RRMJ6/cF0j0oQ9PgeWCuN65N5zY1vUKL3O9zBnATKv5FsIsb6Aa1ErtD89QW4OlTpK/2kD05JwUAJLVfIUUbg+4LU/Aj8lBd/Vgdp5FU+Df8vRxGwipfgI5tngX8QJtPeBNqLAqqwgrq/bu43zrkRGA097nA+EWlHkdNPG3N8XoXsX3zNv/2Cw8OgruraN4UDv0ucUQlID+f7Udk1nz1eoorOaawEPCVjteHjk0dUXTkh6NFOgC7pPvBfGtM3gHkXd4/ZwlEfB7NfztMdK/p81jzAOy2grkxHF+vMufCri6y40aEPwpmlU1Jaz1OXvH8WfgBOD6eoIkUKPXqeLzD4XT03dLQ1CI0/U3ToceeTXlO8hYqGjtJHIg3/Pce3I3YTWVzpvLQSZ4UxmBXHfCH1YFAekgykD+5PsIxAVg/d11W1ACoA965PPH8GjqlIAVbusAa0GNeC+QMaUsSLsasj3Q7kxjgBd+uouCUg/4GJj44eE6tIqHMVOn+magNcUiT6cs+S4Cbw9B+k2EAfR91BaQaoGcAr7sQBBA6fSPyH7Y+RYrYGw65fl90o/hflsr9D3h/G2qL2DjN2QHzfXE1d85B4ByBdJ2AgnAotcaVHDqvSUQyIQ7Lb88mPVB3R+2vP6hPf/53+vg71yp/xi5VyhsmqJ+nc0efPZOZy9Ons5AjkSFVz+o7dODej5NBfbpo8B+EPnw0Cv075n1g4i3fH6F0BfkBZkebSLHmxL27QO8wH1aXD4R09PP2dH7Ft63HJhACwCpPXxwx/sQQCBB5QXT4AeX1BMFdYD17hB254KPFHgrkAlfgon46vy7wp3WNAX0Ea8PqAWPsgnE3alJe2xdksn82nt6zdokeX7KrNT76y3LBKQgP4Efpj0OqBXQ7jSRd7/6aH2mix93Y/cqAuXv5q9TMT3fgfAZ+ug4n6H3PcB9Q5W1YBP069TtTirBUPDrY+zHVs/2nsB+qxmKyebHxmZqst6a3z8aMdUQsNjxJlrOP4py0vgHIeBLEHjVH4Xs7l+s5A0ZAIJPVAcY9q2ea2CnC3qiZwhEDdQZKB2AiC2Y8Ec1QE/lAVgH0Dot95v/vi0rf6zl97sbmsfu8Lend4SYvj+Y/pExYMK/0ohN3nwn0C+TTGuaeW+X7s69N5ZfwMKiiSi/exRMrP/lkXtPrwBZvOenyYWAk5JovO+Anx6GgBV8a0mBBIARn+qJ+GegdIAkQMfFZP0V4Nt3CqbbkXsfP315/fM+9s+L/ZWyaIpgHJshaIL0XNcnXMRmWQulwTVOeDhOkbaL0T5GUq6NoxbKMJSDsxiLOChjM0D/FL3UetM/Qye/A8s/nPvvtNVPj6mAEYA6MNdzEB+zHMymENtibJvBWJp2fQRjCdQmbIylgJ24h1gEhRMuzWCOxbCU5ziWh+EYy07y3rq7hz1f3jvp90g8yv0LwMY0mqzFLMthHBolXJa2KMfDERt3PBRD3UkPyeI+w3gEmP8x9S0aU7AeS55SFDR2oK26TXp+e4vulHYUAUauiVqcPz7cjD1Z9IW2t6HN0pQflDHDIGwxpC1iVPbWdPnSNOcKYpnc1ejVIj+Jqm0rcUTkuemJLr/l1tRij6m+7ahwpY2R1lxCN79yHOatEwnP2XGkdGehrK+Gao6OcZYHWi+E4eTJVToSWVcxaJ8QAKMTU1dvM3wo8fAwZKck9A9qZDp5LGPCoOv9aaVUhnsyzruklEcuYJDypJQZshrOOz3JuhDfmkWwiYjMaK5Ic0xORXviIzPjUYrdjxHiZpuo8yOizTbkCAtEezIiBzQGKCEZJ9fW4aIc0V1VOaZncss4c4XRl+vgvPAwuVrvVcuO9cKmQRi6StufIoELtLKkTnJC+DfLQfXWLcnNiYpyPR7qfHNtG2cXS1prUpXRoUG39sqtVK756ziop/REmW58tWzfoBLc3eB5fLydOHJcySc9clZH0yR3zGbYKSQmNiep2OwywsBCEXNVcjD1zsJXKOokmLMgFqNneK603279Pqwy+ULL2QL25a0huSnaZXEhnzk4Td2LxNonqzj4G/iUqHGFi8XF9CzZXPOMrNbqrjvbRbE36vWl4mhH20kWLtUZbF7dBWIrVGx0eiz6WenWAn2sSmknrbWSDFitP9kkkmEzlCQxTtuRsdca5/ycsdy4ttugyZrbIbvxtsDJ9B6vkXHlrPpMuCzzAzFyyDKIb/QxsnBb7ruasbFSkOUu7ec3GFuRV9khtuvZ2UmV+jJjNIkjzp1/OSTb3bhe1U5E7hdqPy42lg6HDN2GFWlGBmoszyphcDqrzDZdp9j1UryK5yEiyqFMyNG9YgWqWg2V6SgcKXWvzmx0y/IaiSXwRmMEklgMe58Sjkd7n89qhSdnu9onCzZ09pLj6jRqN+6VtjGRZcS0UImyxUJBrDIzWRV8F67pPreX62ilXNReDgsYiW+edFhEg36+rOKZNlwJkvezYxtktxFfatwlim71+iBTXCBJnTxHB1VO60ERs6V/Fma5IC63TRAVFy7l9NBeZhtv7MSUT4+3PamTobsvTw6TMswlGw8wWIIk+Hlz2evj7GyQXIoPur2tWc3WluF6NKh9tzhjVCav3F01OzOhbe+YaCgs2PeXJ203u4btBrPgdNgL1roh12h6QDPjQgnsjmjyxckalLl+2cyo4xWm81Le3/St1sB4mxyPpiWpJz8UtFk435GncoOs/W0XENVIux08p2p36e9nrF0oRdTeZFqNuJkC8nhsDBuBacpVEamlJFkeCRrJlmcSj1VOOshoVJ7ikwaHOYVbFXqSxYWZlfMB2e8DuSuHozo0WjJeFyiNiLNVvfDZw2x3qA7ksVyscVSgRBc5MYZ0vuDVMof3MNmz0fx824iuyy3NRWHU9FLUZWbMuP14FcoyGYtx125NU01XWpIVbqgRs93G6DzTuW0Aw7LKeUwwozEb7HIlWIQKOnSQMoCXgzYv98FOlcykvwI8lA8zPd36qmyjx9Zyu6ZeFzg+a3V4LnF7q6XCrnTY04oLY443dnmNEOvimq21vNHIdNary+WcSEIEENKFi9LrJnFYslfH+iDAfka0tb9Y2CEvkMpQrAdyv95cpWSnYxgp1uw2a7FzxK+DSFh1Ad7qu0Fb3bo1qflJurWlwbuwvB4E0aa4zWsMP9lq2xO9sBUOfGgt9aMmXa1RyXVvEOuxobn5QUaSeXzZK5jOqymZ0nvOZncePpoHvfbrTXcTsCyeG0W3n21SUemVGyUPG7un/PPYs44ulIdLpKBaXM1ytjBdTrURtHUDx4rrg7Y+V8dBdGYGwRuaA/cHJAo44TqDcYnd0tkIH93e53x4prQo3x9mshGESeoBJgqugRB1IgVA+bY9mMnlqOwq1IhcdHFd2OtSyqVE6FOC29QyaP3mlRGZS/dsLjWRLUgNxRbJVrmi0aZdiwEtMUc0EOjLujivTmtTbi7c3F9SZnvwh5MOi1StH1Ndl/OCMy8JkevYsYxTRQ13zDmfHe366BS2LK4Iyok3UggA3YAJXivUK2XXhFE37QATmtlqZ1RpRm53c4/mMfeILLK7kE22rc6JAAN9hs12Zy2R0lKMi3xb2hK6XJU7uC1I2azc+rIM4EMGkvd8LTfJEgFbMdbhFa2h4kOzO58xv0EqeZFQ+YajtWYgRTmJzAMCQnVk8PhS5JLp3sxLhErSlT92h/3ykNCWJYG6PTKhj1KVIyCVEvCnrXVpKnaZBr52DYPTaXOCtY4lqoOI7uCDLM2tSwHLG1BlXLDgCQXsdJzoihuevUHgcNMscDVBFm1F5GWhge4hEjVlw6jiYhHoI47xZHhblNYoWYdIkuoLf+7nhpuuxrOomLISYxvzkFFHcx2MSKfIzBqm7a7nrWTTVHTZ3Myovh2FKxWap26D2TO/bK7BlUwvQ6rzxbV1hmtWGLiqWIeWkXXUBtxTIMcrk1IpFkXXnDm4u7Nsq0u+wztWFmtEszqp9US7loeFtdUrXdetExfIfNnLyY0/qPG17i1GGxsTviqRqKdzl93OQkJpqGZ2A6Qq9fPT3rws5s46Ox8vlHUAZG707vIYIYTnxbRPUiwrIcwFSWU6xMu4Urtb4/LOvLewZXpTCRxP99Wp0DOcoeqlNy4HbyhZ+zCzDFHAlrHA5TcDsWbXZa5x2HxlxOeipS9lqyPAR4KcSMocW27IXtiQpJst9xul0BNj2fI6gtKancmmQi7Iw1kVGis/Ces1aqUcwaIot5TLJY2iWrs1quS08s/nRM+xDaVvD9wiUAi7PdmjRiyRjKMucXFaqKLFivCFOFUSkQch3qdUcThlnLB2r4v0EJhyiGqjNNONnZcMKV30WLUdBAZsYZBiRhxGnqi0pYylJkFIvMkebTuPDieFPCiB0y9p0gjngyYs++rS9Ndcu4VLVHNPgsmKC2xXrc2Vle3T9RWLAWU4Gqt6wsX2gzW/pzaLcVvqMwnNK0VE2OyEXUCTN/BGO3jFfjMuE6G53U7azW086kLpcgS4k8cvZ2fnr87eLrZ4zI54wiNubHxSkzKAz8uwXvtwfc3LXY/FVbPdonqvxDdJnC0vCTsM2HXcdw3PcHQlRm6rx0IeqrxCCEPEgLSvQjZED4zO0aa6XCu9rQriwmnMbotzgFVNw3WPxAEbcGJ2jJygGyuSnC0Q1G1JoyN7y4u5wOqpk1fK10AiSzafZ92KvXbDgT8XIoIsN9fdTOFU3lKugc6T6EFqlqt16eoka9JZO2+Q0l7VVrDtTwkscCVpGcpyfSSMy0g6jIGpY7ruVscE0EDKlqMSqfaICXhaLJQVozEMtp0l3oHOa3uzURf93jmvUoHndD6x4AuXw83BnQvaJkvgXmT6eD/kOpwtsDlC7DdVMPbtNfMLtCiO+kU0CW/VjHJxuO04+opbUYX75cYvLipxEJbZRcpKc60zvD9bndID6xZRSqAzC+Eba40k5ni8zi9n+6wNLa+e5ZSdR0dsNR8vu3hxInfzrXbKx/NtbsgrW+rNm7wtXMUjCy8nvFJZ1HMe2SglTjAEHFuX+VKRD3l5UbSZvRvjPjoa4QldmSRhx6iUU1J4GFte25ecSoMMwBWYUEOYJG8pIxLX5GysMZQX5SD1GBmWu8a3qFwgD0jmezmcn5j+bCDbm1uCjfBOY2G09rLr2TyTXsLhKdX2pzapd/xAkV7h32jE4kt6pXTe+SzvpJu97veCKYRHFQlmrewWnSyxOLI6m6XCt3qwbo+iadBVlbX5Oiu90sUsX0Tngx+J/GkTNbWJgy3gcX67KOx6vr141dDeXLrbE0VN0KuaP2Ddmu3OZrvwSV47Ic1uyyNH7MZfL6c2buLLmbQSn1sbRhbX45ZW0oEILCLyM9Hi4bXVb7vRQIgsIzczFg5ucJAek3SVseg4W+IogXkUSxcZSoZnWmIr2eJ2XSLMiQbRs8B0V/2Cz2/tWpfO4n6ZsXNaUlZiZsNHQ8fEuey5u50e9gIcMIXmrDo1E/103PFXV9tuqy2+JYnVZm6heGpnh8GLo3lpYap8HMuxPeF4Uzv5QDajiB/Mxl7g6JKqyOvx1lcLBi5T6rBW/U6LXdddKETae5nBdzu32M6QLWy1qotercNwJqg1gjCKV9O92SkrlUfPUr0JZdpHYWQfl8haxm4MWrH2DI/jcA2Sgco0bG6WnETX+3Dr8CWWmftbekk7C45QkbEiuIYxou5r38PYG58jZbGtzjse1c7V2jE3PEOHp30tDPPDmWjNluWXdiTMluX6EPbxcddf4XiZJ16fVn0MV7v0RKicOMo1yDGBKHIi2XqVSdLbg1Z32S3jowOzNKtovr0tC5qZE5wNp05hEigu7AJ/K3anfD0SYewtz7hPjTd8k9BbQLsssS4P8mBiN5u+cMRejKNoXNhBrC4yGhk6Z6OuUS3UPdDwh6uyxMhI9vbJuTslXNPzDNLUaK3h/u0ogu03SuwGj12ud2pnVCeeqbCFky9o9aqFW+9wnMX4qrzxjoQo9llkU95vhN7lMknBxW45u13gHiFXfR/QjLMSx7QKdmNVn6msr2qjY9EGOVzWe0DhhYT2FC7gucvg/CYzUgoDe8flMV15mXviBe+2yNceHxIS01nzoPWRVbelEHZwV4vlHD7GsL0+wkiUk3sTYyRU2Gm+ccETlOBa1GiFCyNuVHqJzglYWSGEdSNNrW1mxCZHs2zL4UEfBTN8tuZLb+csbhc+XA4sSOEzQx8qP19yVVtu6X1GVURKjXS21JTZkWaWMziKRIea1Ybd7khWrCXR2F/XhiDnwXIfn86ub8azmaMdS74QYslq20PLzivq1kvwqsiXgV7wVHuL+75zloKKWg7D9rRQjZtNq3rwbXupkp5s6xnVdtbSuhDkXGD5Fifmi1KJQ1lI7Ws0NmOMiKSy9Q1MNN3tzUOzzYDiNzhbX2I92syxGB7XuOflOpvxBCtHVBOB/ohlezJYXIh5FVK6ZF9E4gYoJZnP/G2xMgWToEtprvgy227VC1t6kVvtzqVhjPFul8UH3AixbgvPyEAlqhV9Ita00iz6+IrczpSXH8jEwg2SR1lsTBY6vSKk0CfzQwt6TNlC90xxANBc+Iq7zdmGqY/kTdsEnjPPzlxHtcNS0zsEv8wP9VbZ+978tiu1Xc4EdHxmV46/2XlkptVKdnXzM70p3Z00YxZmyVp9cCnm8/nfn56f7m9gn15RhESw56fpfP/tlP5fPOkNxqj48iYEp1H2+en/3ZHk43jw/a3d/cjes9zXu/bXf8m+fzw/VU4EbHkcC9dJG7wdQP6vo9ZPf3HyO00cHm+Mp1eKffP+PqOxgvuZdJS5bd1Uw5c6T9r7iTTwa1tPfydSf3l7JfB0X0paTO8XvjcdXIZR5X1p8unAFXx7mv6OY3pP5rnR4/l0Gbwd3T8/uQMIUOTUX3CK/OJVxbTGtxdH06Hs9Obo6ff/AWRBih3pJgAA -->
