---
name: "rar-cowork-cookbook-teams-update-manage-funds"
description: "Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_funds", "rar_sha256": "b23791246a02810036702d0fe7bfd353509cf691347dc59d822d7cceed99282c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_funds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-funds:bff8846279486416ffd186a332c77e98004b84738912dfac4ab876c08a996d3d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_funds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_funds_agent.py` is
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

Manage funds Teams Channel Update — Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-funds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_funds_agent.py` and embedded as the fenced Python below (sha256 b23791246a028100…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_funds_agent.py` first:

```bash
python3 teams_update_manage_funds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_funds_agent.py   # or on stdin
python3 teams_update_manage_funds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage funds Teams Channel Update — Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-funds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_funds',
    "version": '2.0.0',
    "display_name": 'Manage funds Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-funds',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-funds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f50c9c1a091e1bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/manage-funds'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-manage-funds', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateManageFunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageFunds'
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
    print(TeamsUpdateManageFunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7166XLjVpLuq2A0P2wPVcK+qaMjLgiCC4iNJBaSrg4ZO0CsxA76+t3vASmpymO7pzti4rKiJBA4uWd+medAvz7ZbRMV1dPr08G3c2hlp2kc+RVk5x7EF31RJeBXkTjgP+QWeVPFTtsUVf30/OT5tVvFZRMXOSBfVHbQ1JAN6b6d1ZAb2Xnup1BZ1A1U5FBm53boQ0GbezVUN3bT1lAfNxEQBMV541e228SdD3GeXd4veLvyoKCooGsbuwkEBAP6FyDWH+ysTP366fXnfzw/xeD66fXXJze1a3Dr6S7dKD278eW7yOUkEZCldh6C5+UIzM3B99KvAPcM3PL8AHr/9mPtp8Ez9F//lfR2FdY/vX7NoffP16fp377NoSbyoaaw68b3INcubSdO42Z8gbi0t8caqvymrfLJEzVQOg9fHpTfOBUl9Pfp2Y8PIS+h3/z49akAKtiTL78+/QQBs78+Ve10/TJxKX/86SUter/68advfOrWufhuMzEDWr+8vX9/ZwsWflsaB3epfwdcH1Fz/K9P3xk3fR56T3YCyqeXSxHnPz4Yl1XR+bmdu/6PP/0VWzfy3SSN6+Zf4vvzg3Hk2x6w6V3xn57vTv4HNHs36JPnX4stQVj/HUvA8g9xz9C7o/6K993//411Gud+/enxP2X3ZwSzv0M//6Vt/4zgGQq+Pi38FFREZTup/wr9+nbQBP7nH7xvN3/4x2+A9f/I5lC0lXvn8AaqMQ78unl7+/mH+n77h3/8/ENbglwD9fPWVumf8fwzv97l/M6D76t+/D0tkG/kSV70OfSZ6dCvRfkf1W8vkGmnsfftfv0KfV8v02cGTUZ8CH244LuaqYGu3/nxp6ffADLkwJrWvT8GVf6f/wnJsVsVdRE00MEt2gYCAW7izJ+U16O4hvT3ov7lsN1I0kvm/QKBu1O5A4iw27SBVpUdA0yriinikwVFAP3yf9w7Tn5x33ESbiYMemvvIPT2AL63O/D98gLpEZBXVHEY53YK7TlNg8DjvJkk3XOibrMv3SQMKBI/wGbPbyagqdvU/xv0y19yf7szeinHSe2vOYiDDYLjQY2flUVlV3E6QvaES87Y+F8AjALsqIo0dWyAr9OPtnyZfGFFfv7uIRegsz/4btv4UFq4QOMgBtD7DIJcFylA6WbyW53EaQp5cQWcUlTjvXcA375OzH755RfHrqOv+QN4cejRM2oYLPhUGPrypaz8II3DqPma+25UQD/8+tsP0P+F/hnVnfkkQwPQf3cUSN4UEg+qAoFKbDOwrIamNAAwc4/Ur789IjBpl4MmB+onDmL/Tgy4fQv7ZMEjLB8xATZPKvrVu6Tf+w3qI+AXKG6At0BN189f84lFAZZWfVz7H058ED9c/xHkh5wpJvW7D0GcgqrI7mvvGTcF0y0q7wXaBNCnp4C5IK73nhtNXdbzSz/3/NwdAaXdfAthXjRQDeqkDsZnqK2BqRPnXxzAenJOBsDIbn6BZF4Dfa1IwY/JQXfxgLrI4ynw71n6uA2YVD+AHJt/sHiBFB94Eyrtyi6jyq79+7rAfmQE6Gcf9IC5DeV+D02d259idK/ge+bJ3w8JjzmCf58jHi0d+tpiCEpA/3+GjUklbrXaCytOFxaQoOj70yN/pkloMucxPIHufye+F8O3ieADPD5g9WuexsDn1fi3x8rgnjKPNQ+oaiuQD3tuf+c/FW915xs3IPBTJKtqSlb7a/6B38/ABcDt9QRFoD6TqdqLT4HT0w9NI1CE0/dvvRx65NSU6yBbobJ10tiFAt/37ondRNVUNu8OB1ngTyUE8tyNfmcVBLiDCAP+k+djEBWA8XfXKSD9wfzzyOXP5fE0IQEtvNYF2oL68F8ga0pXkHI15PhgzJnWAC/8cGcFZT7wMVDx08N1ZJcPZabp9F1Be4pFkU058l0E3h+C1JsaBZD3WVeAqw0yCviyB0EAZTM8Ivup53usgLLZlON3ot+H+91W6PtG87eptoCO3zAdDNRTj/7OOQCQK5C0E0CA7pnUoHoz/z2BQCbc2/HLo6M+WvanLq9/GMl//Pem9nuPNH4fuVcoapqyfoXhRx/7aGMvbpHBIEfi0q8fLe3Lo+l8eZTXl3t5/Y7hwz+v0L+n1O9YvGfzK4S+IC/I9EiKXX9K1/cP8AH/ZX76QkxPv+Z7/1tw3zNggisAoc742TU+loDWEVZ+OC1+dJF6aj496Hd38Lp3gc8EeC+PCVvCqeXVxXdlO9k0hfMRrU+QBY/yCb69aTR7bFfSSf3af3rN2zR9fsrtzP9n25QJQEFuAi9MuxpQJ2DEaWL//u1z3Jm+/H73da8gUPpe8ToVEmhWYDR9hj6nzGfoY+6/b6HyFmx8fp4m3EkkWAp+fa793No5/hPYYTVjOWn82MxMg9X7wPtHJab6ARq7/tSOi8+CnCT+gQm4CEO/+iMT9X5hp++oANB7anGgs77Xcg309MAk9AyBmIEaA2UD8rEFBH8UA+RUPoB0AKuTud/8982s4mHLb3c3NI8d4a9PH+gwXT86/CNfAMH/PH5Nvvxom28TR3uiuw9Jd9feR8k3YFY8tcfvHoVTr3975N3TK8AU//lpciDoRml8u+94nx5qAP2/DaGAA0CHL/XU7mFQNoATaMLlpHsCkO07AdPt2Luvny5e/3xy/bMyf3WCgGEICqNZgqEIlAoCD2UoG8cxl6Z9lkEQwmEIGmdYFPOAXYTtMDTlIozNspSHe0D6FLnMfpcOo5PPgd6fjv3Xx+inByHoAxhJAUoHw2kglqBsBGNQBMEpGsE8JPBpJ/BwEicR1g0oFsUJ2nNJ1mMwzKNdF3Q6lsUYzJ34vc9zD23ePmbnjyg8yvwNIGIWT7pitu0yLo0SHkvblOvjiIO7PoqhHo37CMniwFk+4d+tfpC+R2IK1MPgKTnBKAcGqW6S8+t7ZKeEowiwck3UG+7x4WHWtOkT7SiRw9JUENo5S5TVMRWV2rhKytlbXM9nTkZsfS42Y5xFSSk2MqZK/DVW5lp32nCzvTjrdVrKj+kmSC+Y3hSNVwhrG+NFcgwalK4yIxy5U3fekkc+GypNM4DOW+faE0e3ZkwyJ5okSkv30GkwE+elOVpmEsGnm3AbY7k66eJgn7phaY/XK0agjWmPy1vRLbepzpds6e7FbdjNXL6STH5Qth59VKvEMO1s0KJR0VOKURcs7QZSS4sJ4cN4C2vNrlvWVbK/bEa+jiisbA4p2vhWhqKXWJRWh1rGrytnMDKUsJpDOYypmhGpesTic0ugYnotszmfm3v0aopDkEsqcT2qpgv2m3trmw6GkFKmZawTgQz2B8wqeNZmDVs3jFsyjLFnmbbjXxDfdm0sP7ISUtzOx+35TBSGXQm7lXUuR5mpZoosYtvSnJeSkTMKf0gc9eKTQnYqq8alLB8ugAEkLop1XcUrhRnQRamySsN1RwIMCLrjnVeRvW3HAA1ztQUbYr42cRvNAAHVxEszq7JEReez20Za7usVQtkhWqG02Iu3dSruWSXpcCVKtvEZN2zrkJwWDKt7fUgpwO/7DeMeXe3q28VMFWYYCWtqfxBwWUJvI0XS3el8or1+WbN1vrkRzik0rXPL5tnpFmEyEXPNasVvrKg2vJntHm1HPGhL/OKjK5MPD45gwfRpne1aPcTAuFTJ59MNHpSlEwVzNjwgCC27hwjVNoRtqaezc1gnWtbQ7SwrGtTcm5hW1mm3WAwUIwnOyt7wS6RQqbooqBNKspUheltDoJLuRqaZlNNBEhSHQNXVwdX6XRByGxSu9stlMrvAOxjXKTQI9NuNI9TU9w40riteSm1n26YWsjJmKjWLs/1xi24bWxKFY7cChlncaYgcoczWtNmyWMrNpOXBC0WYlbY6ygudGgfz9pi220wY0mVwUkOzTze7A2fNq6VgKsfE3vt82e6ve+EkyigXX08xxRt7fZ0SzBi6+nwg6Nzdbka1w3dqpp9816Q2+dyNScLadPoC29I4a2vCpc4WN02xsFHdYXa8h5cC7ERucUbCjoXHeV3TmSSyFc4iplHT1GFLdOYS0xIvxAMnVqq6LJGVAQvqlmgIRbd5jjeIJUtFxcwprqIWmJruDa5uWEa8EU+lv6OqZrkq2VwrZn01Jy/eprnxuJ7dkIZhgj1V1EPYwFWo30zKcZPMZhUfI3HWPxh8e21WUkOYFovyZTMk9dIlj9t9fIU3HWJVjryd73VJIHeCH5HMIRDQmDqa8a6jegFmr/hFL3KiCLpdujEKlKhwSjit1J6fSUIROJLpzpQz2YMsVDqJU878UvOS8oRZRu6VkSoEmigaeynXszMo0lu63WTR8WxSS3VR99e1R+Vxf10ox8UAm+z5ihQYOTuvsiIQwqPr0AxZEWtE18JzimbeWvApfuioeNCxw81PjhVd61JI1bOuSdduEIf4nHA19TbnDHjLL7OmRuzFdResitEh2AwLirziM/9Qu7rsWNvLSljnKolh5LyVIna5Z1gH58RynMVGQh5Sig3m7thZ6VYSg+jqZjd6fxvme27g17vdJd8uci3EE4kqscOwMmO6LA6H5RrbjrxeOWlzxeBFNSLLPVxvBmu5WhlXY5UDb6cgU2tp39s74SqeZFzXlWzHVKBMTAI0kRELS446Z+y5V47bgj3Wnuw79S28MacByY84y3R6zXr1LRopzuBQr8FZeRurFryajzWb6S7P2wc1Pcs3mBl3287JWxU/GYu4XGhpwQTikkkWM2shDdQ1gteHOVEGS0knxriGzXl/2PHaKfE2VoknrUzVGwE2x+tZpq60c5npFHeOtss6zAh+68dq54SIH+hzYpZfBlq/CKiXHOULcuXyJlnY9pn2Q5UwikWdImur0EMuSN2z4SX9snfXp2Yh6peZLeGX3XXVe/nteONFa6HWJJ5YdLgNbV5c5VywQOchLoAmExr5wfQarOibs2RlhYM1NJIykuT2sYODsjmtuyHJmY1zvkgJEi9WyCXNAoPWzugiIZIrg52qQY9FxK4OSefU9oE/YM4ysFVjfj6g4ri1B610JTh1xiBeRyv70vWzGRnLc1snuPairvXUl336OHhtdo2W9JxdlTs+wdh0fjGSbCfjHMyY47EpiyxeROuehY/Xpj/oQs8pCerFWIOY1JxWjdXcPCpHIljgWctdDJqgiktZ8kD7uglCsRe0cMi26bjVvTNVd/pNaJH1fnvcrcYuxq6p0gzbMZIv2qCEwma+B/DRJRizLhu5KflN0g7hGRT1uT85imsNSTEqpyaN9zYf1utK1/prH+RNsxCU2Oisrj1gbLa9skKlm5Jaz5e3Xd6AUO0uMm2FSNhwZIUZBWuN1HDbCni6kAGUFMguYVd2osWH4srsrs3x6uwWCwKPFexWJwe6F7fuhi6WzGArRmUYhr2/LXYle15aWLRRdsPBbfyIxd1Zoum7tJx3IQY7MozJ0gyhiPl6g7rMcrcSuMMRTHGXgjcRsTJRw9INX1TXXdflo94F3U0VSvVy3vgkR8wKWuP0tQ4ymAqsjNmfpY7uEep4pjRL7vYtKZdO0Bw7+YpIfbyv+fGY+0oXT91GCB1lHrkjW6fHzYjNmVjZZVYRbJfF7NJkNADu9Liqw31qU/zVtovyeM5F9bRjdn3Fr0rjelhi3vZy8Y+nTVgeq701cxGnNQ9nb6+YI2hkYjGbEz7X7/mZjWfpziELgD1qJpDL0Akzai9b7XqvC/7hlJMJdd4J+bhZKiEYILb9LAFtgUxgUGTrA6nrCJGbGTn3dU20LdjdOBF11AUby87ERuTO7F6vinhvyuRODt1ySZNCtBmNTLoAdA7EXTs/mgpp7Dsk2BqepY6rQT2rWpmsl+aVuNi5JRCmF2KDcvDqa8aur3G1k0xMlNq+3lup6dajX5rSRckFL/PNW3dmSex8SFZRllILHh09FR5N3+9Oi5VzoQuD7tCYLOK5lM5nreTYaoCK4t4vBuxSlZ6cGwN36UjJim2P7WdjeAtodwHzRFVkbitUQjn4c6Hg2DXBz+e4lC6u0awIsTHZqmfKyjYxOqI5R7kCAHCmpkiALg3ZDe5l4ca90xEkGJJQvaWwHdrbbRaGV5Q6ttdtslOoq1Jz+U5lEg47LNasOIYssZcu8hJsVqSNKTCesD3vOY/MzG1pYSQZOt4mG67r4nIyRDj1r+ohu+wtxGNjmT+ulx4SUhEj5GdhPIuald2K0GM8qiO3xmGuyTPN61xSq2XK2fajUQT6en4r98KYcoPRZZurJp1Wu0HuyXPVHQLudGPitVZifugduBsP40wViXiVOzYiLnnLFiLWHUFSD2nLylhhzfBrotmrTQPGzRPGm0QWkTJ3hIOUTMyjvSnbukO8njZCVjy6ibNYoSOS+OfBPpAmXnAHte+3SkjJy2NCcKhpXRSPmW+Kc50vM6Y0UrABvR3Yfe8ZpwXBLQtLNLvDlqP9zvLmOp9utofNKlBv1UnWczTcZ5Fl+seC0LfYsEHkIUS620W4jleSZbYzuXWVXrnhShwLnmcFFiqHMX+ujAonVYyRsoOeLA6Kgi2wKBgHz5mPzVgNGnLVFiRTaeuiupZMjaq3bNb2ZrtPPDzqGxbURdWd1mYvmzPSBV3LYmt7RQ2hsvQkjQYbjkZVDEVNsRs9X4RMPltIoYWZK9Inr86idNZVvrw24wmWsTCep5tbScaeIK+XMNr2eRGurpfUME2yC6IZodyOvrHjV/iOTliCvEmzS3eYVddepBINLY6LbEB8ZrGCy1NNntsercXFGT5beH6aW5ZGIccVIbAImPTtBXu8JLMg7jp4lLtxflqZZxuGTY1x/OPI0lWemcHxqhzrCnPFTqT4436h4jtjJuWF2SzYJQsgbEuRRAIXK1IMe3nszsuTvq7n5R4hiVhN18I6lekQ4wlywVgglPR40w+0N3atF+9WDUh2ElHWMYi/WImmTKBqnuosQa95uV27o4KsVlbvsXsvm50WJiMX63QAAxDMzuG5q7Apwg9xvqTdTTcnMQuHdxrlkzwpnahQWOLYFu6wHeshqwVIq1oMtZtx1PMLYVYnGJOMgKbowYLRDlYXJm95PMrOhZpDl8mCJGerodccP8hYZhAw6Vg1O21VNJXWtJLsrPGmc24nUNYOSl+4cehQdC3cPNgcWnzcOrvNllmquB8R9bAN4lOUbNydqmBCjmzB8Gxtbi0Ix4THESFzbnr1uh2+XMByLqF7TSN5zlvJsEu48ZqrFGcnNgS2lE9Zx1dbyxdbVj/PGWIxt+pzxy9nhGGwsL2cgQ31vrhxMr7zrxy9zKym60InYWKV5+Rly8nE9oSf0xC0CDnGVgWj5TTvmUYzCnsmkLuwVAUnXhCK41WndTtrB05yzwqhjj67XMu3kLHiNak3GSmzSCpn/Jb11i2Ycvgb1uMWYpOqkx+PFy0XomGRUavk1ntwfVIH4mTPLhyOkPU8bI+9leN8iXaSajcDXTncvm9XfE9TaXXxklVnsQTrZr5Nt+cWJQp5R6P0trAvMYlyTu9q0TpZ7GSBhO0rh8ckvgKQuJ3Di5y4qRe0iAbGv1xGfdtdUx8pakmnFt7i4m/mxB5jZycxbpkGw5Gzhs2OrMcouNO2vp+0824d5S3Trc8EU0huByv2sqIVLKBwvhkDo8zo4lKwwdWJnYoPXES9UVoQdsHN3S9ak+XoYLC6qxKJ3MAURD/3VlzJ2Fc6psHgIcWnpd5skLOEskN6DNeBORO1HatwMoCzwMQZUlTZENR85eRgIDx4/ln0RgpHz9XaVTTNXMMmetlFOq2p3LrwsIDjlH3iin09uAIWtK4VrcuypDByIZUNjdWkj/lshZxowRZEe4UE2G52G1Aur4lgPeyOy1rXYqeT1zInrfklsz5Eks6vlVG9MlGn3ex9tlu56hjvFuuxcsAgqh2qq97sbwa5p9S6H33P8c9rMGtWt3AuFQ0tOnEgMdgaU/WDB2okovMlvD8nMx11Zrt0vcMXsoQrfHo7x8MJKeF0yxsaKp0vVZM3HcmtNYp057dwRY61eqkjQ5UVBYUFaaFf8C6UUPFAouskd204v8UUgdCZurqNrXiE0dXRYPwQbsWlIgWbguO4vz89P93ftT69ogjBYM9P03n++6n8v3S2G97i8u2dBU6j+PPT/95B5ONQ8OMN3f2I3re917v0139Bu388P1VuDDR5HAPXaRu+Hzr+t8PVL3950juRjY+3wtOrw6H5eHPR2OH9BDrOvbZuqvGtLtL2fv4MPNrW09+B1G/vx/9PdzOycnqX8L3a00nr/Xj7rSneHq+vn6a/1JjeiPle/FgxfQ3fD+qfn7wRBCd26zecIt/8qpxsfH9JNB3ETm+Jnn77f8PM1xXHJgAA -->
