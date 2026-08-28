---
name: "rar-cowork-cookbook-dashboard-manage-environmental-social-and-governance-esg-plan"
description: "Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "e0a5304660566fe22fd19ac417ff9fe1c13c545dcf479e3be8fe9d918adf62e0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` and in the RCI capsule.

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

Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 e0a5304660566fe2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` first:

```bash
python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py   # or on stdin
python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan',
    "version": '2.0.1',
    "display_name": 'Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-environmental-social-and-governance-esg-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '696fd3b7d6031bc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/manage-environmental-social-and-governance-esg-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-manage-environmental-social-and-governance-esg-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardManageEnvironmentalSocialAndGovernanceEsgPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageEnvironmentalSocialAndGovernanceEsgPlan'
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
    print(DashboardManageEnvironmentalSocialAndGovernanceEsgPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZebSJr1X2FyPpRrZCe7EO5T54wAgTaEJBYB5TouVoHY96Xe+u9vICnTrq7umenp/jLK40wBEU/cuM8e+LcXq6mDrHz5/CJ7VgoJVhyHgVdCVupCbNZlZQT+ZJEN/kFOltZlaDd1VlYvH19cr3LKMK/DLAXTj2XmNo5XQRZUebH/aRpshannQmFae6Xl1GHrQWtF3EOuVQV2ZpUu5GcllFipdfUgL23DMksTD0yLP0JV5oTT3wnHNWu9MrVSx4M+rGThRyiPAdRPUJZ7aQXEg0EDZJdZV3nlRyjNIA6fk5DlADQVlHqeC0DYA1QHHtSGXueVrwC911tJHnvVy+eff/n4EoLvL59/e3FiqwK3Xrg3iOId3ep7cPId2jJ1hXdcq+p6BJiAWPD7CubnA2B1us69EmwyAbdcz4eeVx8mhj5C//EfUWeV1+rHz19S6Pn58jL9nJv0DrfOrKoG6B0rt+wwDuvhFVrGnTVUUOnVTZne6QZKSa+vj5nfJGU59NP07MNjkderV3/48gI4K61JZV9efoQA+19eymb6/jpJyT/8+BpngKAPP36TUzX2zXPqSRhA/fr1ef0UCwZ+Gxr691V/AlIfxmF7X16+29z0eeCe9glmvrzesjD98BCcl4DPO50ffvx7Yp3Ac6I4rOr/kdyfH4IDz3LBnp7Af/x4J/kXaPbc0LvMv7/sZHD/yE7A8LflPkJPov6e7Dv/fyU6Bo5TvTP+N8X9rQmzn6Cf/+7e/qsJHyH/ywvnxcBFS8uOvc/Qb1/l44r9+Qf3280ffvkdiP5vxchZUzp3CV+Ba4e+V9Vfv/78Q3W//cMvP//Q5MDWPCv52pTx35L5t3i9r/MHBp+jPvxxLlhfTaM061Lo3dKh37L838rfXyHNikP32/3qM/S9v0yfGTRt4m3RBwXf+UwFsH7H448vv4PIkYLdNM79MfDyf/93SAydMqsyv4ZkJ2tqCCi4DhNvAq8EIQhY1d23Sw/wWoWA2Oc4YP+ThifEmQ/9+p/OPfyCQPoIv/B72Pz6CJlf/xAyvz4i5lcQML9+C5hfvep6t59fXyEFLJqV4TVMrRg6L4/HL5OUtJ4A5aUHgmd7D5S19wkEqU/Tlym4/vpPrfv1vsRrPvx6D+XhI66d2c0U06om9l4nXi6Blz5ZcEBo93rPacDqceYAqH4IwvRHwFeVxSCF1BOHVRTGMeSGJSAsK4e7bMDz50nYr7/+agPIX9JHEMahR5qqYDDgHQ706RPYsx+H16D+knpOkEE//Pb7D9D/g/6rWXfh0xpHkCaeWgQIt7J0gIBXNhMlU0YCQdty71r87fcn80BMCvIqICj0Q+8xGVh15LlvapDXy08YOYdsD9APqE/yrKxBZIfC+hXa+NA7XrDo9GiK/UFW1ZDrgUToeqkz5TgLbOedyTSroQqYbuUPH6Gm8u6r/mqX1h1iAsKDVf8KiewRZJosBr8mmPdBYHKWhoD+dyN53AdCyh8qiHkT8QodJjuGcqu08qC0nmv41kMvIMO8TQfCLZCNuy/plGy9u/VMxv6gBwwCzDhPlX6adA7qjQRYnFu9rX0fY035ULnnxfJLWj0dxionVTiT/Q3QtQndyQj/8jSpKsia2L3zB5Dey4CHFtynVu42KP4v65DNX5c377UD9KXBEJSA/k+VRhMVS0E4r4SlsuKg1UE5Gw8VTbAnVT4qRlCL3DHe3fFbffIW3d6C/Jc0DoG9lcNfHiPvin2OeQTOpgQYzssz9EZLeZd7N/rJiMtychfrS/qWTcDOoXvoBHoHEQJ40GS4bwtOT9+QBoDN6fpbZXE3EsAu4A4YNpQ3dgyMzgdE2JYTAVTl5LhPvQEP8CYn7oLQCf6wK6CSGhgakA8BECFwRZBx7tQdMrBN4LN+mSXfhodTvZY/zMCFQH3tvUIX4HuT/VXA4UHRNY0BLPxwFwUlHuAYQHxnuAqs/AFmKsmfAK1JF1kCXOJ7DTwffvOWO5YJPpBquVYNuOym0O56/UOz7zifugJgk8m/75P+qO7nXqHv095fvqR3jO/ZBISNeKoYviMHAoaeVHebnaJeBSJX4j0NCFjCvTh4feT3RwHxjuXzn/qQD/9Yq3LP2OofNfcZCuo6rz7D8CPLviXZVxBzYGAjYe5V3xLup4cjfvqDI356+OEnsPynb274CSS+T/dy8ftFHxx+hv4x4H8Q8bT4zxD6irwi06N96HiTST8/gCf2E2N8IqanX9Kz980AnlYyhfN4mPz9Lbe9DQEJ7lp612nwI9dVU4rsQFa+B3egoi/pu5E8XQjkjvQ6JeYq+86170keqPyh0fccBB6lNVjbnYrJqzc1YPEEv/JePqdNHH98Sa3E+2carykBAfsGLE19HPA1ULTVoXe/ei/gpos/tq13LwThw80+T8748R5AP0LvdfNH6K2TuTeNaQNauZ+nmn1a8rHy+9j3ntj2XkBPWQ/5tKNHezaVis8S/s8gJh8EiO9BeUqTT6eeVvyTEPDlevXKPwuR7l+s+BlZqtqaSoSwfosHFcDpgoLrIwR0Cvz0kV8aMOHPy4B1Sq9oQC52p+1+4+/btrLHXn6/01A/etzfXt4izFMHz3oWDAeu/KmasjEM7BcsCK4flgae/Wsr3adwEDBBMQWke4hF4ggxnyPkfO57GOa7KG05BEr5Pu17qIPiDkmQruMTFO3htrfwPdql0YXl+nPMm8A+jPnrVI+E9V2k7+E0ijkuPsdIkqBRCrNo1yIoy3KRxYJCKN8FOeXb1AhE2ycLj11PFL8X3RNbTzJ+e7HnBBi5JqrN8vFhYVqz5hhh970+G+eeYafzkwxcKrXPkoy6PM/HGCfK0saODstMNyhB2yil4lwcuJITg1/qyeYoCF5+mJkDTW4GIlHg7BqcaEUat/F4pBfkMCw35xAONzE59lldZhe5J1VVI1EpMWWQudA+slmsbeQy3DRa5aR2T21CzdOGjkR0XjP7C5EXY4nO4dk2o0NfTSJ7vcPYBYixvbczU23nOpWZl2mBRsVJu6pH4RB6HFNyxTwy6upICr5gitGe8/dGLUjb6OZZxRCV23U7YJYEV8qVP5CZlgrudVMnvVUdzdpb4vrmckOcZDRnbjoipJeOaAA26qf4Qq9q19gWNrPctKBklbRibQkdlt0Oq/YmRuRKqeCOp4VCRpF8ndDrRg3Ucm0dKcfShn3qX68oeqnVHbcd/JST2hWmb8Iwj8ahOmlgG3hknwI+6HWVL5gsQaOlvjf1gkdIrSqLgzbOHCEpZFjuVO1yQvI0yjM+zWxCT1yS3ca72fUaumK5WJ52aDzn91yo7HBrXHlJsu1oUbUiF7mY1xOvEK52WJryIibZ9mLv9KiuEVE+q23pr8a6EXbBbLQVres1RyRYB445D2NmwoELBYR0t81BqPRC0XpLKeS5WIx8vp6RN7n1UKWoSy5Rg5lnmsaOYMqICOc14S6lmu9j2BpwcyF54nKwcHWPoDI9WyjRDpRuFrAI/RZ5q8PtGtXCrE09c1xWO1QQ9v28IDCOLHYEknS3mh5Jduhai9QGa4P1LCz1xkVhlEI905qyKzoFxjyZ7ciZT5wyBj4nu25AI4dV5WKl5xuaW7g0fWEpKy/iTUu2R3W9Gt1GYTVsjBan/OyMZNMldHJKYI21E+NmZ7ZtYvhytANvHG5Ok7oWLeOGjUmUvOBJmgBSmdmKo7ihVq+kZ8EU02PuWFILuzX1/YaSvEuNkX3IUnvhlh2sfJVcYhIn9/wO1sOCzh1MrvLFYWAGfy2GRIwQnYXibBAlVGhUCEqavcRsRcIU4lLmgqXqhDtL7jTeoqRIxFXhakgRv12r3vl2IEpDtCs3OrOMcnO7JuGYZXDRSWfoRMJfda7c8LBwMXB9ESi6NfJNXWvnaH/W0T2jmTKiX0Uhq3mHl1daXFC7K7V2RT5F9nsOxkdFCCoM0Wf0bTZb3064c6ncfnHxi2hLCNbQruAGHt2Wnsm5Z5HDbM2KOOqz1NoadHQuywtTPkRozi21fC3vuBU74lyPoSZieZUmX+1Tv1rcPP4a6+fETKRbPeBH5jC6MIUKPHcrsBOB8UUibYRxpSmxJxWmTPH0vpalXkpABVvDqmjpTsHsnXBDVFWB7I/Hlc2vaYVdqKgkm9sa6yoOhIBQOKmHdeb5K8E7InS41zb2LVvbs2DFMLE3nlqL22HBeRuwW/S02JwMOdoFF2LeuzZPyUdFvd5ODNbvL9fgmlb8Za+Ry9EXzewm0MsiMkjeTqKoXmTd4BX2qrjmLrLNCQYWsXCHKAcu4kd0ViYRbB/sCl7lsaaxs1MPt5R/OB18yV+OcRnXR8HrDwRNHlVlbvceQqV+7CFHNSXgE05vciUm3MEzE3N/xs2zQrnMpaDIYs1fUyHZxFwddUvCWqokd+5xAq9uiH+dyWRkxYx+ZEsEPWKk7ogxeY0isRS9Q7Mn5zS3hDcLhGOuJmvt/b23TLvNbpOxZ3unWJvyNgsJ5RYZVbBCHcxVmY2THIkadAT4iZWY7Gywktqv9szlNMsFY6cKxVaJbyVr1adwlE6aym+H2bDeNSckO+mxabj10FNMvppXZ0Njj3mp4VJCwtieI49Onoqya5Pogj6OKIjPDL81VkLOXBTXPwdaFq95G1ODGq9ULr06rILjs4XoH857X3e8DrbP7LrdZ2uCvmAXf0vSyY0hF7Ry2MES4vYBsUlkslHsob2tqqCI19UZbrjEMvtSqWKt5I2w1MWod7TZtiJyFW/W4YLTriWyIkR7VxfUpmD4Hg95fZN0vH1pBvramx5imhhtrHbX2Tkq97IxZGkbjOIuSW5mnZrnSE+JHUkygawO+D5hFwuxizc9JiLwlt/pfcNFhrlqd96Rz4Q5SV9yPUmZokArBcM0x74EeUoDe0DMLjCskDb1jYPu15QS8ranYfYyuwiIpIfuWi4G91j6xYKTyban1vly3iHaeQjWiZq5+SUPQdqAZYtKqC0lL2/hPMJnxyDfq0xsr5H84BsEou/8i1l6O43UcNqgxb6Tgt086IpuAaogVayWWTVuiR1zwtLFCrabcsgbNz+rIW+QuzpXC/G21QIhVI8jqK7K2T4JzO1h1MjDedWpPNsFucEal0S6qBW73hNUvjkQhJdFUohu1ZAh5Fkh5aLM2fhCSKV9vItKgSsu8VqXaroyV6Teb4LcbLNjlpw6hl3P61yTPL4751EfBra1v0lotG1C45ou6MU8C0BQF3g/F/TO8tozi2gWUZyr22mB5QBajxz64nBan4MxL1dzqthzpRkYcb3T7FU7d1fb4znt6yFqd7DBDpyfWjvWlwvFF+f66RjEOzTg6qt6UZpxNzPiVXTdF6G1AvHyZLBufsUaf57hagtbq3oj0QyM7GC6t8zNeu8eFlgQpRZIatxgtBKGMxgG8CXNMO5S46SZ80PTKvGcSgx3e+STWhKvrnU0Xa0b0zmnUwhCwOms7+hNVSYemhzww613bkO+7Ru6z2dBZvjH67aiqY17uzE7LFky/dJUWEWEkW1vC5Xh7bdifit4KSiOGVHr5s7WGgK9MrtjjpAn58zvKuFIFwsvs7qAMwo93xGbRuxaBnE21mmOx5Ve76gb79D5Ml6bKieh9BCdmP4k0DS+Qrvd6Ybb7HxnBLtmrZ8PKHYYGopX5xJsJ5WIHK8MJ3T7syAeWJOVBIX1pW27MkWsTuLmpPSjR3BVY+07EzV689b0HnMol/OKwfBjUbneSh+KstgHy/2CcYxTfEgqRYhlFkzN5ytuinaJdiJJ5YyMYeSSUrhmgm6Tt5i+MrPzYVXkjlzEs7aQBa7hpJvCOvluuFwHYx6Z45YZcbPeCUm/T8c1PzoOi7TUsSByzPSdwxhHpzWTIvNFza/Mg3Q+p1hoK3VoOyiIk71W20dddmHxpoTVaZy5ppzTgkP32zEipV2dojevXhBuL/a5QGsrcxjbLNgPpyblONUsE9HW/aWrtvESV867MNgqoATFkoY6zavl7grcer43Fz07yxFr7nUU8ECE3q/XRFaoSLJ2iUzVVqfNaupDGMWUKuRMZIJXKLcTi23sgdyvhsWhW8n9io1BGl6jx500r8vNod5KMGtonB6AKhvbH0WXvXgLerki0j3HD8247Q88z7UxL6/zEvfQWxzs1kcctAk7ESnLfTDYF04Z00MgpAbNkmPWWVc9M0CtPMQaG6i23gkLsagHQzqvPKKPzXGjH1fd0jwdcU2vx7nB40YzN9VgxwjYWlRIVN/sq1EsuDSbBzUsU+I2SYNlN1rXajZcO6oxLZbSD8ItOkgz9CQySNOeUsGROEaq7e06CUlGbX1mMzCZtMSz5XbbtenysHdAf8Et20icK6Hea4VSH9tzLxSGVDg8usaQ3h3QHcm4xZFgiu32rEeBeKto/JBihLgpT0PLOSdnG2w2SL2IYnHXro/FUrG9OhaTZqzmRbdnh4W4u3V5lTiH7W1U5qizoVexbcZ4zW32S5XyY/+Qqae4BYUgTqApfWIRcZxxtVEojTb99D0s0OkNAb39DJu3vZ+Phs6l9b6DE7/GzuRFgx0lWmBme+NOJIZmdqpIVMTysCvMHWSOniNLyYqbKq4QGHGdJbrSsEsq2269CmC7LgYyacdVzt8IlTV08nhQxE5yqtBCFTI+UqIN+jq+9VFQ2m5vy9PVUvJDI1eiL7WyFqbo1gYJJfMvV03SuTN+WrkNGntmY6I3w1r3zeC0QuVWlY0N2tpY4FTp4Wh6PGckfKT24wgHDLGseiSt4bZX4PU5xLXUzfxdKcDnSxMcR2ZttRGDn48Rwta97yoyu0PKE3m94MLI+ohwibrTca87Gqm0GXfe5iYRSogScV246GxGVW/YnnXX7eUQmuqioaNBRPmh7Iq5xFxpSr6MHNF1Qq1vyPHWionRH26HSDMSQ4OZQzyjrSu5qBkrhr2ZTgQz1OnaNSggVmIyDnBLHG8JxoNmUPF4z/SSypKXugGfxx6W2xJf5uHK3TMu57oCRmDHCyYEvoPL8E4oZzB1OfKyJMp94SnzpRmxWzqRULxz+ZOLm/AZwdQGzi/SfFl1V1LQBmMQ0IraDTAeX4AjnkXCKyRJWpup3pPUMHjENlyuj9Ql5ReC7DugQ+/4W01yG2ETe+iYyQO9om4lPPiyulkfgtt8k1DRAZHhdAvs/hScNGZ9u/mGMds6ncXccs7GKlbstpzQ0kWX4KEu+c1moYKasJNbdktQ6sL30Wvn+X5QCJmPLl15eWYCE/cwU1nHQXfdXpurEjHUgTANSVgGM/2knUYYN7gBvSAb7TDOhtkyyo0EcKglAj0HjRllRjWWKBWdbxdKNSYsSXF5vMDJlOvlnJco4B/rpnZAd4Gia9/EHboCmXTB8mJFRV7JMa2SLrGaX15UkYPT/CqOIcFGlF0OicE6XlhpV0o5MWPncUYuYHHSSS5VlkenaCy33oNeZ7sFbkXGUbyOR3Rt98ax2cfHk7gifV3i8GqOryqR2zEUt56r2faKnbP58ex121hH9ePcvmyW9A0L4pZYogPlKwuh8z2JtuGuEkLJdWkJ11vJxxKG80fuWC9gqTktsrVDkTkmCTqMtj0f5SGuksHOqAe6oiSlrC7JZpYaR79xcXWxCdoLfT2k0qXNfJa4nvvzGPF4xqZqe8DcxprF+v5UwMZ4vh516si2gYSUdOEx1okF9Zzc7FNqsdBI5rw8puYgr/t8kc5UbAHqjpqMqr0bnze+uUg3Tk2vDxyDMMYxE/lsowrG0LfsyCCi7QhqSTmefsznGIF6TUMZNCZu193yArqM2R4dnEu2c4/rHon4XlnR5JoameHEZx3v7JnAspfr/VzMxKIlD80yuYJIroYKvx4ye91o60JBlPo8qFuTEkWi8A576Vi3K7zHNpsyqqi5dm2HHSZIRiLMqRupz60LPW9PqgRnQ4MbyhbEcE07uUm80AJst2jg3ZIt4IVMDocy9W7rjeSiAwFa7WaMjbrN2NVwYBY9v6OOSrw7hPuAOYM0mNySC00qHNmBdkad3YKWus2wle4gs2DRHE+lTYXZcrn86aeXjy/TWfjzRPtf8/p8Okr8l51oPg4f396J3Q+0Pcv9fF/r878I7y8fX0onBGgf571V3FyfB6B/ddr76Z96zTKJHh7vsqeXfn399j6hBvXCtLMwdZuqLgcAPG7uh9EfX+ymmv4/SfX1eej+cqcjye8n+G9oJi1mpedYVf21zt6Olu9vbBPPDa3ae15en2fjYO4AdB461Vd8Tn71ynwi4fneBuwde0Ve0Zff/z9d4ZBIcycAAA== -->
