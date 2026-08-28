---
name: "rar-cowork-cookbook-adaptive-card-manage-project-budget"
description: "Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_project_budget", "rar_sha256": "ab96344307bd47a33593335cb1d49e4c1ca88a9042093f458e990f643ddb0460", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_project_budget`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_project_budget_agent.py` and in the RCI capsule.

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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyLLlX2Hyfajqp6oU+1LXrtkg0AIIIYEASV1t1ewgVrFDT//3CSRlVtfrvm9uj43ZqCpTQkR4uB93P+4R5G8vVlOHefny5UXzrAxaW0kShV4JWZkLcXmXlzF4y2Mb/EBOntVlZDd1XlYvn15cr3LKqKijPAPT92XuNo5XQRZUek1l2YkHsa4FbrcexFmlC4masoOqzCqqMK+h3IdSK7MCDyrK/Oo5NWQ3buDVUFVbdVNBfl5CXmp7rhtlARRlkGtVoZ0DQdUncMOKEvAOxhw9K61egTpeb6VF4lUvX37+5dNLBD6/fPntxUmsCnz18qbKpIl8X3f/WHZxXxXMT6wsAAOLAeCRgevCK4EOKfjK9XzoefWx8hL/E/Sf/xl3VhlUP335mkHP19eX6Z/aZFAdelCdW1XtuZBjFZYdJVE9vEJs0llDBeCpmzKbgKoAnFnw+pj5XVJeQP+c7n18LPIK9Pv49SUHKlgT2F9ffpoM//pSNtPn10lK8fGn1yTvvPLjT9/lVI19BxYIA1q/fnteP8WCgd+HRv591X8CqQ+32t7Xlz8YN70eek92gpkvr9c8yj4+BAMPtl5mZY738ad/JdYJPSdOoqr+t+T+/BAcepYLbHoq/tOnO8i/QLOnQe8y//WyBXDr37EEDH9b7hP0BOpfyb7j/19EJ1EGcuAN8b8U91cTZv+Efv6Xtv13Ez5B/tcX3ktAaJdTzn2Bfvum7Zfczx/c719++OV3IPr/KEbLm9K5S/gGUjPyvar+9u3nD9X96w+//PyhKUCsgXz71pTJX8n8K1zv6/yA4HPUxx/ngvX1LM7yLoPeIx36LS/+R/n7K2RYSeR+/776Av0xX6bXDJqMeFv0AcEfcqYCuv4Bx59efgcUkQFrGud+G2T5f/wHJEdOmVe5X0Oakzc1BBxcR6k3KX8MowoC/6fcLj2AaxVNDPcY92SwSWNAa7/+T+dOnJ+dJ3HOrSf5fHMA+3x70N6356RvD9r79RU6AtF5GQVRZiWQyu73X6dxWT0tW5Re5ZUtIBR7qL3PgIo+Tx8mXvz135D+7S7otRh+vRN79OAolRMmfqqaxHudbDRDL3ta5IBa4PWe04A1ktwBCvkR4NZPwPYqTwCj1xMeVRwlCeRGJVgpL4e7bIDZl0nYr7/+agPG/po9CBWDHsWimoMB7+pAnz8Dy/wkCsL6a+Y5YQ59+O33D9D/gv67WXfh0xp7wO1PjwAN7/UFZFiTgmHAWcC9gD7uHvnt9ye+QEwGqhvwX+RH3mMyiNDYc9/A1jbsZ5QgIdsDIAOA0yIv63sJql8hwYfe9QWLTrcmHg/zqoZcr/Ay18ucAUi1gDnvSGag3FUgDCt/+AQ1lXdf9Ve7tO4qpiDVrfpXSOb2oGrkCfg1qXkfBCbnWQTgfw+Fx/dASPmhghZvIl6h3RSTUGGVVhGW1nMN33r4BVSLt+lAuAVlXvc1myqkN0F1T5AHPGAQQMZ5uvTz5HNQ9VMQU271tvZ9jDXVtuO9xpVfs+oZ/FY5ucIBxQAsGjSRO5WEfzxDClT9JnHv+AFNJ0lPL7hPr9xjUP7LnkB79AQ/9hNfGxRGcOj/b+Mx6cyu1+pyzR6XPLTcHdXzA8upW5owfzRYoAG4S77nzfem4I1S3pj1a5ZEIDDK4R+PkXcPPMc82KopAWAqq97lA/cDLCe59+icoq0sp7i2vmZvFP4JAHPnK+AgkMog1KcIe1twuvumaQgMna6/l/O7NwGCwP8gAqGisRMQHb7nubblxECrcsqwpyNAqHoTul0YOeEPVkFAOogIIB8CSkQgZwDN36Hb5cBMALNf5un34dHUJBUPv7oQaEe9V8gESTIFSgUyE3Q60xiAwoe7KCj1AMZAxXeEq9AqHspMHexTQWvyRZ6C2P2jB543v4f1XZdJfSAVcGsNsOwmpnW9/uHZdz2fvgLKplMi3if96O6nrdAfa80/vmZ3Hd/JHeR3cg/b7+BAIK/S6k6oEz1VgGJS7xlAIBLuFfn1UVQfVftdly9/ats//r3O/l4m9R899wUK67qovsznj9L2VtleATnMQYxEhVe9V7nPUx36/Mixz88c+/zIsR9EP5D6Av099X4Q8YzrLxDyCr/C061t5HhT4D5fAA3u8+L8GZ/ufs1U77ubn7EwsWsygLL6XmrehoB6E5ReMA1+lJ5qqlgdKJJ3rgWO+Jq9h8IzUQCVZ8FUJ6v8Dwl8r7nAsQ+/vZcEcCurwdru1KcF3rSJSSb1K+/lS9YkyaeXzEq9f2vzMhE/CFcAx7TpAaCDxqeOvPvVexM0Xfy4absnFWADN/8y5dYnaGpYP0Hvvecn6G03cN9hZQ3YDv089b3TkmAoeHsf+74jtL0XsAGrh2JS/bHFmdqtZxv8ZyWmlAIaAwqvJl3ecnRa8U9CwIcg8Mo/C1HuH6zkSRSAy6fSHNVv6V0BPV3Q6AAKb6e0A5kEIrQBE/68DFin9G4NqIHuZO53/L6blT9s+f0OQ/3YJ/728kYYTx88e0IwHGTm52qqgnMQqGBBcP0IKXDv/6ZbfIoALAdaFSDDshkSw3EMpmwXpywMIxgM/HJsxMUZD3cQx6Jpi4FxFGYwHydoj2Fgn8Qx17VhnJxUesTmt6naR5NaqGU5tEMhuMtQFul4GGxjjoegiEthHgzk+zTt4QCh96kxoMinrQ/bJiDfG9cJk6fJv73YJA5GbvBKYB8vbs4YFolSthras5L0zpfTXLAj/Xa0ncUt7UzXgLMUNo+L7IJGtGA0y90gLpGdowaKpbvlWgl5hs0ocd+4jc+mfZySJtdZzfYkp8dkJJJhRhNoGETcuVVYAutCM1GKLDYOVVkru9suXPXAdRWh6CvCpFfNoCdDRlEX10etWitOerRTlGq1PaWOdl5Xc2JG+8i2yHYeKaG3dHUbMS9Q0IbsjEg/NkgU35wOOyrnijjlttRdNbnru9RbYkTZmb7k84N3jFF7P1aok5X0bHYxnfZEzOfr7fZk0kstMZyo7KP2RsK3i61jzq2pEW4MF2cmUat5Z+An0bXW5bIR0vTcb08N7qN4UkaWgkuX8CAihhsVmpsRnU0bY5pf1eiimgPR68uE1OMD3HeHbWw2RbmQdl6ErLbJdrUXV8bldKtTRS1Rz+wHbZ5fdmV8Umj4yKZ5yjGnyDu2HH29Kpdqqx8sZzhKs2DJuedF4+Qr0zdSidjV1NjJcVUxg3k5HFY27l72/IUDmgT+tYwbxBr8ayHpecm7xxq4g9vFexMh+6rCkQg2UzsNlOuVRoI6VLqtXRT8usLaLWfdtpJEypY4b8qNxSyRWQ5X4bLbFGRmBJm2bkR8iKpZc94YNKLR9YWomM1eCS6CENQDWXiM58JSVTckh/qna+Qud/ThXK5nTJaeMxWJpGrZGEpMrnsVIxPUsOtQqE7eijIumhjsnHMzyu461nTK8Ky8gAu396P9xoCFrNxl6HLL+bEdOWxOtOKhH1fb25m+0irDnDTKqm+x0K7wdrldjk5zXahNp0eH8MJtqXBbjnG0LTDbFm+ULZa2rRRSHV+sKmeOZdQuep/TfBWfcQsmIPjmwgmFynQzUxGROT3b02MfOZnQmo1DMfFtmF3ma4+0NF219JMfl8sdUWv2OhwumyHuUGmvy+duF+mbo5izDpuq9iadLQ/sojwWhAZI00cKrHMQgi95dS3npS1i3EnR13YwsI4o53QYW6rXiQ2BHYSD5NqLldVdhJWozaTGWGWBKm/ksfFoAmPJvVqSxI1gYOx6xa/00kjmqoz7sX/aIHLSJdGh5+nUnGfxzb1set87YrMNe7Cjg2AhVTb36e2A4MUau8Uj7awyhPHpM7Ymq6pgpdV6rXTX0pasEXi0MhPHQrkOSdVyszodZWx0VqrBkFm24tV0bwi5WUrmRTztJb9YSaHEzz18L7irJvawcCleSxKv16dYi7akUxRJys/UwqCUpM6O1p5IifyILk1jpdj0sGPczFPEDOGkHaVX4ZlY+jGyOfHGbMseD1uYOWhNSNC8scKHbWpGZ1Q9CBijKrfWIqxQ6f2yUJc3XUWNPcOZ0WI33KSl28IgV7dFpcejKMDHOper2XZxmlU5mlAb3hdwWbPwIK37+iJbCIgzDi41nRwKODLVYSmXdr+VVFg5EIBgGmtclf1spDXJNvUtFqchpdBjPHASp6Yn8wI7KiVsTWrYVRmcpEx+0v1gq1xJZjandCeYAX7bqFeiZeXrJRHXqAQ26cfudsWHIw/MOs8JQT9n4XmzDRCZXqd5Xqgibo9q6wVhQOzNkz+Xow5E6E2V9NRJcNrvYevWHLe1lhUOYWSzwYj4kouW+y7YznQl8sUWYQt/jsPnUxJXHbcsxMU624cLRKcsW09JMVoDRuaG3W3RiLFa6seFQXURUrroZXEId15/Mr1LLhyi0chCf5ZufKYWJE25ujSsr8frYd33aLsvhYrQW4kbtyVB+VmJ0o0kq4KoShrSIy3WxnA+SC1hEmaBCetlXDbXAzfS8/kq5nsFJ68Nwi+WhjDfcK7fJvlc4wmyWV9VZFa3GLfAw/OK9wYrMely2YustItUPcysvWJeVoGmOyVqahd4gYvW5iYWfbLKfWexhkGgnnIJPqOubihHPRqPbcTdtKBYxzu2mi26zY47C20c7l31ZmhJgRx8XyZ0C9Qi3zUvIKpif5dzxtHH1pZzwvsUl3MyHoSYppazDc0vagI5Uh3wionfrJZD8Ppk8OwIzzg2DjRnZ87iIl2rWO4WJbs3c2znm/zRXCuoOIzGLEXqs4mRyqlOFnUDit22gr18xWWSvj7dVloyb7t9c2k6b3kRdF9UmCN9lvTbGRVC8ahou+1OHqv4RpcbKvJTDmftW8EeTheylNeFIgVuyu0oKa7dUd0tU/I02mihUkEcXQLWOs38aJ0glhYe1kRtRJZWeX6KC8p1G94i85ZYx0M4LBiWzrV0vem01nIu9gj4HT2GSHiSltJqXBz6mr8ZUQTTDZJ2UXdgV3LveDPbGi5NPaTB9hqMq0VMajePWvpMi8qhRQsBfqJ7qeb2mZtdMtxktwzjDnZYHRIT8bg1Vl2YVuXgREPK8FphsxC4SF07o3c5cgvYcs/WemM4rSyT6a4zbrfxvJsf81Ak5H5XL1cgllnLunBHzTj2J5aRugo2u7PmnlXqLCYBrBXmVs7jZsHrJy1WbWsdILxx6ZBhQ7kjqTI7zozXKF8ySthXwp4RUThUxOsFl4ITHjitvcmOBzO5Hckyz+W0DAZdns8VLK7taiNzkZa33qYRl2t0Y0qcQHjsOJbM9tpv4mbeJtvCz8hRXpFyuSSTaoYslvR4WHC7dbctwL7cWV859izF/Dlfydje1s2uyrt5yhVaycqGNnPUhdeOMVnAl2xYhkfQnantGCUn3lZGYZOua+GASMnm4Jj6Dd+EVApCh4zVNnMVnEgbVTdcDzUOY+Ifihkry2HLu3RaiXJ8HvHTcenKudTzhpj16cIaK+NwpojUKo7CjF0qNlvGQg+7ZxHWpBMh7vBIRJFGHxjQMDRUsB+IolUz5LpIlVuCd5QethwPwnoCVbgmR10f6Y2WWpWWn1ficdVv85qJhRNbSikc5TNS5WPXVIZ132hLry2xlVEd4FjyZ1eepxdNT6m5564RhXQokQtMuyK9Xu6Nm47AFkjmxrkw56jdrU5mnWGkPuSn7ur7Ik/lIrw6ETh2rZBgV++VlDv3q/Ic0QuJSaP42uQA0x3f87vCIk/qhTD3S0pRFdVVZjsCTkemc5cOR5VCZKH6dVmEGk+yQyuduIOwsttYyDfk7dDroWbLSRHlaeaWLFYJBtcnDGJe94dEZkrVmUcI2YRguiytDESKWaTVkkTlosVWVfeKjC6QuDbTgDwlZ44X7NtSigd4Z+paEbNZwmsZspfMW12T9sKj6KMmyb15FY6txHdyaCz7JKdK7pLbpNGcUk1xOkpg9r0oJZirX+hBGZkgoUX1xjdxuRHVzR7rTEyZqT2cH5TMCIXF4bba99otlW+70uGXax2ldtkh9/A+IUbutK8HtskVrAzIEbnZN9ij0XyxMAFG86Fky0toJ76lWiQJtrd5fjJUngnOl1axjrlFK6Qpr2S7yfKjy+5vVA86thaPL1gkndfK9hiSJzIu400uyR22YCl6cY4FZ4zXYgjv0vzAr/jdVHvqFYxWu+p8NZzMXbK3K2UZ3sriic7NTkXL6qPILdwomPMXLJc2GikL9jkTNjJti/VWpwvqfBBATxWczkbc7jEhwlG9CQzivPRTGcdXK/tooCIvbNmIWhkeY+sK0orckaGpEc49a03walUPIsxhHDqD536+I1D6NpQ+k97QFu7LizwnO3xPVQq5wkxj7vCGgwKeWA9jdWWx0/p40LXl1W2oMO9vSQ7XaCBHuHLJnRFfj7GGnlrbJGxTpKzill3Sa98eFjs1tvJE9dcyx1EzDOeR6ybNd9WypLMSbDv5xqKGhGUvqEmwc11xPZif6cjOWrBwOgctvWxvDtg53WGgnbJSarPu4l3mJrZXH1aX8xzEqBtsnb6m5ibLZNdgNq+btp2xmwXX8lqDzebLPe2KW8tz0Z6SKptZ3siY6Zen24x10WhzDQRsxcCS0s65mkMXtkXJ4vyw046LgKgd+tbFZ3x7uEpjF6fCVjhjYrtcDBtCnkfkNsKOElUPjbmIujXqXjIbdrLgfJjVdS5ljhQwCaPQOTEuzqutfC3YgZyxrSRrWBggPl8tSNfzCX9ens7ba6u03JbfSC0V8vilTlxjWGHqXGg0VAEx64JcuDDjvkDZruaVBOyeZlZk6TOvki+bkLCuc9Pwovms9mddf0iow87X1S27Uy8sPc41HN/UpTI2s3NkcyVF6eq5X9ry9jykboajWUK4Zqgr9Izq5NR2BeJ6mdv7M+YTIIiXK4XL3FYfzO1mjyo6eVY64Gqp3Vch4D31RudUUmKDz7HLq4N3tKd6g4mK+vFGOoqJb0hngXeDpZy44NwGdX4mGIzPh2O6cG0k3LZKhYeOgOvl5tRFYbRZzk9xMS8XAe7su5GDN2Sg9DvhgJn43pZznoOtJXkQqmVyrLNDbPKZeub1/YrcMTtpNXfDfFyONi0fQ4kMjlw7oDCPzjeuaDQ9Sh8vipfGqQhfypXt5uvRKxZDl43iwtsbRLhpF9UxlxE488XSY1xXbhxtA2pK7h03PCj1AbUJw5KU2b04WnzoAYs2sGGjeJXk2Aatq4W0cOQkRJHytB7znVwziNEc3b2H7c3aWnO5AzMJrkTDanbd4cvo7HWsNDaZzflq01zhXsj5Qfb7y+AP+fIk0vtNss/DwSKvKVNvFjLaEF2Ehay1dds847sAPTHJvNxekgzj3TVDzrvSGy2Bn7e0oyQHGue9VgywbXMmbyBGVtiOOuRYeW0ofFQq3SP2CLo94L5Nb+azE7alpbBV5uGuVMw2bReeMNACPIQGjR4K3aBWM2vmHZeWcfYE2GURj0hO3d4xZvT+sFssZC4RT6txzjASG+TJfqx74ooQcYYeMN9CHdN2i9yZGxv+gp/yc8Fvaj6ExfM+l1c5aC7PN7WNxgWs2E6ql5TnnfYFidKIhzakSNFuJGtsldUbJtlWdH0QKGXT0dKNLDhvdtzRuMOyTXq4RiS80M60gwq3bAiw3NZ55Srflt1Ar64XJjq7ia8qyFUkk6zCx2uJ1yW2s4X13KN1EexEXYlezXgzJ3rOsssabC+doaZKL4jdWZ9c6m7HHjdzLs/cdRwlNXrDYzrhdvrc0+wjUyYef+Uys8OdBRpkC7I1T8kiEpo4CgXObcMc9JvL8KISqzHN0lmvbiiqScC2jjlcHXtvrwv3OBI8utpck0ssHVj25dPLdPT8PED+O4+IpwO9/2fnio8jwLfHSffDY89yv9zX+vK3tPrl00vpRECnxwlqlTTB87Dxv5yffv43nkNMAobHs9fp2Vdfvx2411Yw/QHRS5S5TVWXw7cqT5r7Ie6nF7uppr9lqL49D6tf7qalxSTtB1MeN+5W1Pk02o+mMVE2PdTx3Miqvedl8DxY/vTiDsBVkVN9w0jim1cWk73PpxvTYez0eOPl9/8Ndll2u64lAAA= -->
