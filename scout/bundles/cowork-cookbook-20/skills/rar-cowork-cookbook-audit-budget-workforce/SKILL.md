---
name: "rar-cowork-cookbook-audit-budget-workforce"
description: "Audits budget workforce records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_budget_workforce", "rar_sha256": "06a38d701e50a941d4de4d086d97642d0f0d16b290565f70831e37435c09b9e4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_budget_workforce`. The original RAPP
agent is preserved byte-for-byte in `audit_budget_workforce_agent.py` and in the RCI capsule.

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

Budget workforce Completeness Audit — Audits budget workforce records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-budget-workforce
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 06a38d701e50a941…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_budget_workforce_agent.py` first:

```bash
python3 audit_budget_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_budget_workforce_agent.py   # or on stdin
python3 audit_budget_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget workforce Completeness Audit — Audits budget workforce records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-budget-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_budget_workforce',
    "version": '2.0.0',
    "display_name": 'Budget workforce Completeness Audit',
    "description": 'Audits budget workforce records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-budget-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-budget-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e3cd745b27bce66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/budget-workforce'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-budget-workforce', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditBudgetWorkforce(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditBudgetWorkforce'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditBudgetWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6adOiyLbuX/G+50N3H6pKQECpHTviCgKigoogYNeOaoZknmSGvv3fb6LWW917d599TsS91iCQmWtez1qZ+Oub1dRBXr59frsAK5sJVpKEAShnVubO2LzLyxh+5bEN/82cPKvL0G7qvKzePry5oHLKsKjDPIPL140b1tXMblwf1LNpoZeXDpiVwMlLt5rBO0ggLRJQgwxU1YNDkSehMzyfh1YGp1u+FWZVPSubBHy0rQq4MycATlx9ghxBb00EqrfPP//jw1sIr98+//rmJFZVfZOAefDXv7GHixIr8+FoMUA9M3hfgBIOpfCRC7zZ6+7HCiTeh9l//mfcWaVf/fT5SzZ7fb68TX+UJpvVAZjVuVXVk1BWYdlhEtbDp9k66ayhgprWTZlBxWYVNFPmf3qu/E4pL2Z/n8Z+fDL5BAX98ctbDkWwJiN+eftpBo305a1sputPE5Xix58+JXkHyh9/+k6nauwIOPVEDEr96evr/kUWTvw+NfQeXP8OqT7dZYMvb79Tbvo85Z70hCvfPkV5mP34JFyUeQuyyS8//vRXZB/eScKq/m/R/flJOACWC3V6Cf7Th4eR/zFDXgq90/xrtgV06/9EEzj9G7sPs5eh/or2w/7/RDoJYdC+W/xPyf3ZAuTvs5//Urf/asGHmfflbQOSsIXRYSfg8+zXr5cTx/78g/v94Q//+A2S/rdkLnkDU2Gi8DW1stADVf31688/VI/HP/zj5x+aAsYasNKvTZn8Gc0/s+uDzx8s+Jr14x/XQv5aFmd5l83eI332a178r/K3T7OrlYTu9+fV59nv82X6ILNJiW9Mnyb4Xc5UUNbf2fGnt98gLkD8KBvnMQyz/D/+YyaFTplXuVfPLk7eTOCS1WEKJuHVIKxm8O+U2yWAdq1CaNjXPBj/k4cniXNv9sv/dh6A+NF5AeLcmhDn6xPyvr5D3i+fZiqklpehH2ZWMlPWp9OXzPJBVk+cihJUoGwhhthDDT7CJR+ni1mYzX75c4JfH2s/FcMvD9AMn0iksOKEQhUEyk+TJnoAspfcDkRy0AOngWST3IEyeCGEzQ9QwypPWohik9ZVHCbJzA0hQkNEHx60oWU+T8R++eUXCL7Bl+wJm4vZE+qrOZzwLs7s40eojJeEflB/yYAT5LMffv3th9n/mf1Xqx7EJx4nCNsvu0MJd5ejPIN51KRwGnQJdCIEiYfdf/3tZVJIJoO1CXop9ELwXAzjMAbuN/tetuuPOEnNbAAtB22aFnlZQyyehfWnmejN3uWFTKehCa2DHNYbFxQgc0EGq1EdWFCdd0tmeT2rYLBV3vBh1lTgwfUXu3zUKZDChLbqX2YSe4K1IU/gf5OYj0lwcZ6F0Pzv3n8+h0TKH6oZ843Ep5k8Rd6ssEqrCErrxcOznn6BNeHbckjcmmWg+5JNxQ9MpnqkwdM8cBK0jPNy6cfJ51NphTnvVt94P+ZYUwVTH5Ws/JJVrxC3yme1hqIMM78J3Qn4//YKqSrIm8R92A9KOlF6ecF9eeURg8w/V3/29xX/UaBnXxocxYjZ//d+YZJnLQgKJ6xVbjPjZFUxn3aa+pjJns/WB5bwB7NHTnwv699A4Rs2fsmSEDq9HP72nPmw7mvOE2+aEjJX1sqDPpQK2mmi+4i8KZLKcopZ60v2DYQ/QGc+EAcaH6YpDOMper4xnEa/SRrAXJzuvxfkl50mq8DomhWNDS0z8wBwbcuJoVTllD0vW8MwBFMmdUHoBH/QagapQ29D+jMoxOQQCNQP08k5VBMmjlfm6ffp4dTmQCncxoHSwkYRfJrpMAGmIIDOBLBXmeZAK/zwIDVLAbQxFPHdwlVgFU9hpt7yJaA1YW8Iut/b/zX0PWAfkkzCQ5qWa9XQkt0Emy7on359l/LlKUg0naLjseiPzn5pOvt9rfjbl+wh4TtSw8xNpjL7O9PMYMakz1icgKeC4JGCV/jAOHhU1E/Povisuu+yfP6XdvrH/1nH/Shz2h/99nkW1HVRfZ7Pn6XpW2X6BDNkDiMkLED1rFIfn4n28T3R/kDtaZzPs/+ZRH8g8QrkzzPsE/oJnYYOoQOmSH19oAHYj4z5kZhGv2QK+O5ZyD5PIZBNBh9gWXyvG9+mwOLhl8CfJj/rSDWVnw5WvAdwQtt/yd69/8oMiMuZPxW9Kv9dxj4KKPTl01Xv+A6HshrydqfWygfTZiOZxK/A2+esSZIPb5mVgr/eZEzQDcMS2mDakcAEgQ1KHYLHHdQFDoTWdP3HPdPxcWElz/CtaiicVT5A4JUOL3T7MHWnGQSQaScw1acnlsP9i9Uk9SRsPRSTdM+Nx9QEvXdI/8r1ka+Qh5t/ntL2w2zqZj/M3hvTD7NvW4XHnitr4F7p56kpnvSEU+HX+9z3baAN3v7xJ2K8euS/ECKcIGMCmae6wP2OBw9nFVYNYU9TDlCk3Hl0BlM1rIZH1fxXtSHDEtwbWP7cSeTvNvguWv6U57eHKvVzI/jr2zdEeTnv1fTB6TB1P1ZTAZzDsIYM4f0zAOHYf7MdfK2CuAcbE7gMpazFyl2iGCBRiyYwl3AB4aIryqWXFIG7qIe6GGXjNEpSpLdEVwsMLJbEgnRQ2qYBAek9g/frVNvDSRLcspyVs8QISMKiHLBA7YUDMBxzlwuAkvTCW60AAY3yvjSGsPlS76nOZLv3znQyw0vLX99sioAzt0Qlrp8fdk5fLYo82ApjI0vKy3l1tVovTWftJ9exIvQY34qFX7BWsNdz3zLqUMeWzlKMa7HuPf6oKtqpU07D7tS4bROkO5NPEI27c3zrel6JNsaYHQd0e1YZ0tg7tmbzdK4v9UDLuWYI8NvFvMfnpsaN1B3ykkZaqaULOV0ZLMXFaaBViy66GG6h9if9msRSlJkkechSiVgYR4sy7+Wx34ypfj9XuFnGSg7UwUvVHQYMdUV6RrbkDwVCt6e8v7HIYp3X42XfmSVV17muYBJfX3UquXVxBQZiAMS14QdDL/aDQdjFYadveQwI56xMtXTOKNJ9d7xf64ik2nEfiu7+HKR95Zc3tLuzyU1kb2RUAXZpnBNn7GsYS/a5cgrzOpwx/Yrq49bEqJPtOjaSLO9mvhAjsK0jMwzRsWtFMuAPpi7mGOn4R1dkOUyuqINxYMLRu9mp3i9JXDiXayJOUY5x4ks/4sJw64xjgs9NPdCXbgQF9FVcRSoOpBTPhVvozXZHRYmzP+xCdSF3832s9FuTrWM0i/QtlhSuzs2j210yg5WJagi1lCkvFsbEWnXRTWBc8dZl0X4/Lm8dciP3NWmdRts6uu6aEMmws8biSAM3woQ4Psi+e8JyM1IjYbnvVwaur5SgscGC2d95XG7XQ+rSeR1ieBdrhzm/1ELeM6MDZ5DpMRoYsbc7ktKU80LyyGg3rLiRjlWb5YPTRe6PouGUuuJcCeNSkBvSc2n1srTqeyK2PNFyB250moAlK269GvhDzljASetGSyOnwJRrurR3cYsiXumfjZprccvw21YEio2fwz0budt+RMx2SfTzLBN2vQM7Zw8/lOZKu1/y86o6Ray75xMdNEKmbIdR03ebeDhFfIDrzOrcBCVX4MZ4QeQ+OR8OMBfsXLiNykXrqE2ZnYEfgtE7hmZQbICp11qX9MLCb9Z8L+dVmN2YSy8tzGWuSZwQsgOxEi6MeTdImB3Vit35ZOyO8+RoblWq8AxhcWg3DZx3gMnJo6Mrpc5Kz1JvPAKvwPaGoNKc0fTtWubTu83grnCYu3yEIXQh5iE2N4aRpBXDs/YDkoX7xFpEGHeMwzsSm2if2n2p6wVPcBiXdYdxsekx7IZe3GbjsCnMG+7K6AoXaAiqHG8avd9f2b00PzlQl3annlddpfUoLWcbhuTPpKEmGBd3HnbM1z2eV9RNoReGzFrH8OIXoyUH9yviEkTo5Cv7Lmyi/IIoFYVRZa8O8VrPYna+97Lu5mjauTWvrImPa2lBX054K26J+LSwCQPRLrFC0DrCyfHOTc6lReuNukLQKB5y0WPdisEyMeIpWktRxMw9cnHytbzMpFIaiCRJ9tzOvzcWySZdl0YUu1LPy3Ie3oyVNyT3Sq+29mkUycQ6z7XLbZuvxs6jRaEQbrV5z4msPTuHRkwR7yJ4WFBbcoec8tift/R2KW0Vwxo88nSkk3aX6lxel1YHTtmwiXaxUJG3VtNuyq7ZbVx5ro9+VsBg3l2V+s5poXg5sHObUIibrEpiquhlSNBNdkBPGzPratm74kaj3kwzE9e1U3DHg8/r96178k8wnIzbcBSuoy07mr8/cZdoM3ouJl/SMbkfCalaDdw5ssJVr+USxgOdGUQfk+0TuRnivXm7Z+ll3ZkVdiPsXdHjms3uk4gYctmXc8LjC4fmBzI8SKFRMzeeXq1aO1jRzf6iiIeK58uwFL25eil391NkiyGNK/1OOOfxsfU2Y4c5lrY1DEfvPJYN2DZgvR2IjWxExOVipeyQQ3DundxOtmdxX9wQ2xzEM+f4AVqY1lbGxlH1G+Zc1s5wV09r/CSax/F4zBt/c8h3+mVuShEjRs0yDwvUioHmOqF2UeX9gsHVpHNjgrDmgp1v+oty3RZ7jZt3HljtG/PYJsC9XM9AaW5n/B5brOl2ZywSmKtXtMedhivu9mj7Q3lXzVAdVioJXKrZCvdYLuL7pT6gCyEpR0toPCwxAmNMj0mQGGjkdAPaknharZVeJ++UL9hEw/ZHV01wVInpcgQ3GSw0HJY5lfOWTM6seFmLV3dt6x76uWIh6XK7CHdsjCFtdR53erzZY4eYltZmh554rJSwtneBFq2G06bTeGtf9HSxAlZI3Dc3c8tVFpKgtbY6q8GtaQWKb4q1sFlv4jYYeNfLY2ljO1UxHm4W7hy3bVauGVcyGt8So71tBpcjzcidOG7EcpuVewlbpIPriedxfb1fLvHoHFYGr/Z6JV6znd/ior9lmc3JEMpEt8tVLdV3Vuz03r/JcRgpCmpbWNjp21Mx8saeU8QtWEp9TTHeAlvsGqFnr/YVjW3QZ+mKwuO7o1Nmycxzqr7GZrRb6OfBd9lE1+sOrbfhJkt8J3H0e7o/US5Hnm6xyPDurdLnCqzp7MZdGIy7GbQw67zwBIvnzq2Ewd8F15KPtUvNWnu1VEUsW5/D9lj5wFbdcEnnlzgYz0xfZMiR6WsJIpDdSBnHxPR1zSOivjFdYs/21WBf3XOi7+/D1mujDNFaw++b+CLzizPdiysko+S1si3nqeOqpYSIbGLQhEbpAmL0fqskZkbCuo+J4lDvWZG7sdkNx8fRD6L8vOc2dhGjNH8XrU4iOkTn/VTPrYGPkYhfraoDFaWpIQo7oAxDpPLJ/W44fCSck7UX+mxy7TnlcgG6kJXHzKCzMB1PPd8mJ6yLU9eKKSZwff98z0RFVvaJFClhawyxyOOmjsZjau4wbRWTEtojKQMCLlRXm4FVzLtVnoxU88/z2N9u3N1hdOeSxWxU5WwVDILnNmZrXFAZZRcz6kFDlHmgtN3a8m1xEwHezta3OgXmNkH65VKgjoeqc5mxvwkEGTb9SRTBhlum9a7dFZUbQrA5rgNMPSqaIW9xbq+fTo4gzR3jspMTmhwSbSu32uYQd0F1LFwcuLag27hn4rvsjK8GkKREdxB5YZGer/LKKS8NZzPzvXXPjodm07dz2IxKFi5abh9e5xZBRLUhlevRvQPq2C6O9FZbVUTMzBGtYIOlyx8ym6NBNt4CR+yOCrFo1b1zWpO8GksEuEa6BVuyOWNf1KshY2JThv1SulP4dXFIeYuhakryjDk2mmNYu6QihaxLr7dgIV41K1hPRSw/6/19X2cnWUgs+862JxW7IwexqOMQcY+ZZtvzhVK3CEr7HCC1BtluB2Fr241fLW6daV9Bd1vDP3t+e9bsoNLTCG3nFrdYMyJed4cjs0TuB5wTq9uOvarZIXbWS+EcnNbinRyoWxHT9Er2l7vE2MkXMbztHFLlLmaXKzttaK8VP945N9mFHnuTbmhgCmBdw35Y25FpHa6aKjlSbexToV1sGKuQ+Y0sLoy7sS4tPq9tecfskbVkFY0cyJ7UAtndSrRpIr3IXavO9KINvhc2B4+QlBbwN7s7wFbZoghCl+5cX7M8diZI5l5QJeefWkXx9+vNuLT5bV4U1mDHnERoVQVR7crIyL5mCQXZnSpRVOrVoQsXVaE7bBxfeZzZKWh5jAfsYt83p/JelQ6se06ZFtqib7lCqU8rxSxuRbPZk0hoBFQaL7WKswWf4EV+D8Ymtsfjan/j04OaMbVyai5SW8p3NKw3KiudRu+q+Gl/LvWI3Q76wQ7JOLvKfb1Tb4bc2gLZeaedNrdWTX+3gzV3HZcZc9ZPBxLRBYm1Vc1B7ns2aIBjlQBxQU3VpCv1iWWpLmbgOLZ06YUbRQ5z8xZBh9E67S3bZkNRwn5RG4Z55DN7Gxz9Y8Oy9wQsHBNW1KtRlvc90ZU+nfUbXsEYgU/KBUNxW3S5BOPKI26V2vmVMbI5Tl+MykLlEvbxNR9dRm+QqE2GLLCz6x/S8qhZq7VQ0m2YY3nC2NfKviIXObml6rbpt1mzaxaYPDTy2bSUmM/IK2oPqp5m5CC01qU7u81pVR93VndD5uCazdf6clgyl4ai56G9ctktc3R6dX7LaUE1gO/vojFSg/NhYV6aQ+r74la60NLI2NYokfR5W8g+ytzM04aKZFzKrlkoUhfnDLSy2ZgHNT71t6wY8STkvFEqk9isFU6/X3F6uyME7oQvLXa9UN3mNqZboEkQa0I3v2j62Z2PXY3DDCfo80a+LgCCaNGcO48L4+wi8XmLYwo6dOywpIYyttMNuOmxtL9tXGlh0UJ5RBbOJkw6Uh8ogbTk8ibo9coVOhJP5mntBeNcP544c5f5buN0G/GseLDgIwiLUtt6eRqO6TmgkISwpetNsDtVvIbmKGCr5YFCjpFeZkBxCHA7HR0wSnCrUx0K2k+HdTe/ybf23OtLRsbbM2E2K30Ht5S5ZYjhtZAXh+28SbEzrChJRErpMpbRC25ch505rG3UonakmcFOTdp1FlppqyVD3dhziBAlawD31kcEMxTusfWPV+6yQ8qqmJeg9dpFN7LolgqJnmVCv7OcbSbp0ToohVO65MLOoQ5rK8hLpSXrcxv5MmI2ttfjzm6h0qZLhrhHkcSyLut0vwhteUTjuD+OslnaBYPbg3wEu/0+5qE/UhGg6XD0l8bFXaX1EsPQYRmJzpkE6tEkDvk12qHHaHNFCYHOFPHIUwgbeue6LeNGjxzPundxzneDntmKCw5HHyWjxVUnZRQjbPoO9777YLzotk8dcoOSFv5lFyzX63tDCc6OFinqpHKhfxJ7TzSOFHVWnCynEI0Nt7v2vrfRi2OP9jJjD4Bj8hpHRufERjBpF4hTp7oHruiiNZCrt7CZtUe3WY/et+naXhgSoMeRx6w54jRFpKcQxrgOjAcha2S6Cju0XHr+OCdQou72x9WykfCquNE3iSGiZReo1BrFb3Bba1QXcovhklJrvRkpcFdJxOmdsuf6NRd8P2WsFFYreu7x5/P9olcl2ArL5HCqRsy9X9MR3eFeswCxW7OHvVRE23oToDvzlG/ofK8Jpuac4F7aAuopoahVmkCx3OXeqMesi3iiYkxPkJZ3zyGt+IpL2wDF+F7VFkR86HvSZ0yJMVjU1NNO7GF/pCYyUtQXCV+P+bjfrY+nRMdaNOF3S/xc57hLblbujcEQDKPMegW7MM3nmvvc3VcHZK37VD9YduluNcmh2oVOb8QlHe1V1b/5qYzAKKJkZnuw83awuztHJatVjGdLg11tU1mqGYLY1Lvj5qpX7X4jKK6AsR1HzDlzP6d26yEaDpl8OtrR7qRY5KiigtuL84VE1qeCPNBMDwP5EMbr9frvf3/78DYdlb5Op//N++Pp/O//2THk88Tw2/uoxxExsNzPD16f/50g//jwVjohFON5rFoljf86jvynQ9WPf/72YlozPF+/Tq/I+vrbMX1t+dPPg97CzG2quhy+VnnSPA5zP7zZTTX9aKGaftfiwO+3hwJpMZ1iP9jA7yAswdc6/1qCGl69Tb8mmF75ADe06m+3/utU+cObO0DDh071dUGRX0FZTHq9XoRMx7LTm5C33/4v6TqIh2QlAAA= -->
