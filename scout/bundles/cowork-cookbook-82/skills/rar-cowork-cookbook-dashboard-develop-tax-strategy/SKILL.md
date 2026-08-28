---
name: "rar-cowork-cookbook-dashboard-develop-tax-strategy"
description: "Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_tax_strategy", "rar_sha256": "5502821e9c0ba5add78a1fb267b4a42cdc677056a360607c7c6d49f48cb57cca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_tax_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_tax_strategy_agent.py` and in the RCI capsule.

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

Develop tax strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 5502821e9c0ba5ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_tax_strategy_agent.py` first:

```bash
python3 dashboard_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_tax_strategy_agent.py   # or on stdin
python3 dashboard_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_tax_strategy',
    "version": '2.0.0',
    "display_name": 'Develop tax strategy Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b06e3d358790bd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardDevelopTaxStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopTaxStrategy'
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
    print(DashboardDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZObWNbmX2Hy/WDXKzuF2HFHRwxISIAQkgCxqFxhsy9iX4Sgpv77XCRluqqrut/uiPkwcjhTwLlnP88595K/vthdGxX1y5cX1bdzaGOnaRz5NWTnHrQs+qK+gF/FxQH/IbfI2zp2uraom5dPL57fuHVctnGRg+WHuvA6128gG2r8NPg8Edtx7ntQnLd+bbttfPUhXttJkGc3kVPYtQcFRQ15/tVPixJq7RvUtLXd+uEAfYaK0s8bsBZoMkBOXfSNX3+C8gJaoQQO2S4Q1UC573tAgjNAbeRD19jv/foVqObf7KxM/ebly8+/fHqJwfeXL7++uKndgFsvqzf5q4dozb6pT8FgbWrnISAqB+CXHFyXfg3UzMAtzw+g59XHycZP0H//96W367D56cvXHHp+vr5M/5Quv+vUFnbTAhVdu7SdOI3b4RVi0t4eGqj2267O7w4Dbs3D18fKH5yAU/4+Pfv4EPIa+u3Hry/AMUBX4PSvLz9BwH9fX+pu+v46cSk//vSaFsALH3/6wafpnMR324kZ0Pr12/P6yRYQ/iCNg7vUvwOuj/A6/teX3xk3fR56T3aClS+vSRHnHx+My7q4+rmdu/7Hn/4ZWzfy3UsaN+2/xffnB+PItz1g01Pxnz7dnfwLNHsa9M7zn4stQVj/E0sA+Zu4T9DTUf+M993//8A6BanfvHv8L9n91YLZ36Gf/6lt/2rBJyj4+rLyU1Bkte2k/hfo12/qgVv+/MH7cfPDL78B1v8jG7XoavfO4Vtm53HgN+23bz9/aO63P/zy84euBLnm29m3rk7/iudf+fUu5w8efFJ9/ONaIP+UX/Kiz6H3TId+Lcr/Vf/2Cul2Gns/7jdfoN/Xy/SZQZMRb0IfLvhdzTRA19/58aeX3wA85MCazr0/BlX+X/8F7WK3LpoiaCHVLboWAgFu48yflNeiGKBSc6/tGsBH3cTAsU86kP9ThCeNiwD6/r/dO4ACKHwA6Pwd+L49Qe8bAL1vb6D3/RXSANeijsM4t1NIYQ6Hr7kd+nk7SSxrH0Dg9Q53rf8ZoNDn6csEkd//NeNvdx6v5fD9DuvxA5mUpTChUtOl/utkmRH5+dMOF3QC/+a7HWCfFi7QJYgBmn4CFjdFCmC8nbzQXOI0hby4BiYX9XDnDTz1ZWL2/ft3B+j0NX/AKAo9WkUzBwTv6kCfPwOjgjQOo/Zr7rtRAX349bcP0P+B/tWqO/NJxgGg+TMOQENR3csQqKsuA2RT4wCwa3v3OPz629O1gE0OehuIWhzE/mMxyMuL7735WeWZzwhOQI4P/At8m5VF3QJshuL2FRIC6F1fIHR6NKF3VDQt6GKgX3l+7k6tyAbmvHsyL1qoAcnXBMMnqGv8u9TvTm3fVcxAgdvtd2i3PIBeUaTgx6TmnQgsLvIYuP89Cx73AZP6QwOxbyxeIXnKRKi0a7uMavspI7AfcQE94m05YG6Dptl/zaee6E+uupfFwz2ACHjGfYb08xRz0PMzgAFe8yb7TmNPHU27d7b6a948U96up1C4oAUAoWEXe1Mj+NszpZqo6FLv7j+g6b1bP6LgPaNyz8HVX80Cwj/OD+/9G/raIfACg/7/mT0mI5jNRuE2jMatIE7WFOvh3EmnKQiPeQvMAXcF7oX0YzZ4Q5Y3gP2apzHIlHr424PyHpInzQO0uhrooDAK9GZzfed7T9cp/ep6SnT7a/6G5J+Ak+6wBSIGahvk/pRybwKnp2+aRsBV0/WPrn4PL3AdSAiQklDZOSlIlwA4wrHdC9CqnkruGRSQu/5Ufn0Uu9EfrIIAd5AigD8ElIhBEQG0v7tOLoCZoNqCush+kMfTrFQ+YuxBYDr1XyEDVM2UOQ0oVTDwTDTACx/urKDMBz4GKr57uIns8qHMNNA+FbSnWBQZCPrvI/B8+CPP77pM6gOutme3wJf9hLqef3tE9l3PZ6yAstlUmfdFfwz301bo9y3nb1/zu47vQA8KPp269e+cA4Eszpo7wk541QDMyfxnAoFMuDfm10dvfTTvd12+/GmK//ifDfr3bnn6Y+S+QFHbls2X+fzR4d4a3CtAiznIkbj0mx/N7vOzyj6DKvv8VmV/4Ppw0hfoP9PsDyyeKf0FWrzCr/D0SIpdf8rZ5wc4YvmZtT5j09OvueL/iPAzDSakTYepoN/azhsJ6D1h7YcT8aMNNVP36kHDvOMuiMHX/D0LnjUCYD0Pp57ZFL+r3Xv/BTF9hOy9PYBHeQtke9OkFvrTFiad1G/8ly95l6afXnI78//HrcvUAECWAldM2x1QMWDsaWP/fvU+Ak0Xf9y63WsJgIBXfJlK6hM0jaufoPfJ8xP0the4763yDmyGfp6m3kkkIAW/3mnf94WO/wK2Xu1QTmo/NjjTsPUcgv+sxFRJQOM7tE5t6lmak8Q/MQFfwtCv/8xkf/9ip098aFp7atFx+1bVDdDTAwPPJwi4D1QbKCCAix1Y8GcxQE7tVx3ohd5k7g///TCreNjy290N7WOX+OvLG048Y/CcCAE5KMjPzdQN5yBJgUBw/Ugn8Ow/nBWfqwGugWkFLMdxGKGQhU+7sGPjtueRlL0IHIQgHczGENdzCZKEccJGCZiASZd0CQ+jA4xyHZx0XRvwe6Tkt6nhx5NGiG27lEsuMI8mbcL1UdhBXX+BLDwS9WGcRgOK8jHgnPelFwCKTzMfZk0+fB9bJ3c8rf31xSEwQMljjcA8Pss5rdukKTly5NA1ETBuPhec+ERoWtDWNYiE32C2YdvyRiZbWr7J6k04RmIVZ4wAC6SB4ZeZIs56jZRyrNhftju97OrdiGCDNjBK75rcfExgU2eVdUEEsRKplVXY87NXn1AhSaMaLhI7ws+dKltrOrheh83B14lULX18Npo5Skc10ukynh+T1Q7Mcyf4RJhREx3xC7Vf+07bF0ZlkHTbDOkxVQtkkYiuk7ZOpRct0V/qdZ6TBKIcNjtkSA015ZIIVVfaru4N4tKx+uLAVt6Bp2fB1aHwg9RstZb0zHwWuH23O/V27Ak9WsZ6VZlnZI/KalYZlFXlTcXmM2FxkRUd5sye3maKTaH1GJ077CKchNO4jIbTTTti/HhBd8YqvTmNJ3GkYLCYVBlnUVOy0hsERz33HIMW7VlN7dsR0XRjQ+udQsjseDN3ikSbrVMookqNvVEp23Msp/OLMOIdfGFTp2esciSIiBuO2BlXqzXXt8h+sT1XXUuNrFAn7iWDOdYOVoFzzLSrLmAmmV7iRdV21AWzVbjC6cytT8fWujpeHLWGjLL7ZT334Kh3A6RfN47BOIGs2IuYxkpTU2TT1BN9T6de3Unp1VPK8zIKDyO6z9nNRXa1MY8KurOC07BGZp64uNJXfh/ibJV5CHn2Kmou6BbpUXwzKzplYcHXwa2NGWyypzFGmj5aDVtssVFKMpV9UJCKPeNjFl/o2rkXDWs2LoOs1zNnrZ0tmqhaZRHX8wbjpP6SoPw6kpDmtuVPVBK1p1uUpkVw7Kx5i8ILa2iTbQKT+6Zu+ma4xuN+cbiI3MDVRTHaeZkQQdmAzaAb59eUzfNbTu4klODyERvbMKfsA8ad7NnlnIXUQZlbgqYRehBo89my9zY4cRirgzoXMfa6NUpUbxKJ2HI3ccaL53jQZa26kd761nK7k3WrzpfZgq99nJIQqzJVIMXliqviXzCcq/OtGWOSqEebyz7tPQtvtpHfFzsF3hAnccnhF+zoNWSj8KqkIsdSWbsLSz/sqywtF0m+iu29tFFJzNiwiznh9MPKIEtTXGP6oPSKIrq7wJGuylrss91gobGvLmA9EHccpcyEmw1bmDHW7TyZH30/LJh2BXfoikk2jYwOZROU1Wp9KwoZpJddFoQ0JkulyxPXKVsOY8zqKB3cA+8ZZnGi8XOMLTx+qW9EiyF0rxEXcVRfTp0rz4fZbb+hab5fkVS0E8eoEbqyOhy87dk4BroxLwwJXtSeeN1c8D69hSUpcwrLC5HidwujvoHkW8BCUzj7dqBo1Wly9cCfuGvhB8f05ivKUJs7cytyQVcFlbIi3Wgz8ijcquAmv+LmQpIdJV7Xj2Te7rtAI46d43ChJyG9bLhxW3ul6d0ymbfPGs6lyMpbu+sLniFNGIvjCuR7oc1QdciOSWqaFb7ZxCPvUlcCPu+6hEMPOAfLLHFB+Ag1L7F59JMm8/ITe1pQzPpAxphIcykMq4sa3cmrzgzqGW9STtxROtrsFQ0tMCt29Wh3tRH1FFIleRMFLaojb1hvlljq9ciq3rPlRtiBzYVBnO1OWIl7jU5NdJQbq95hJzKTU9y9StlBunBbvS11qmrKeAfvL4xunY4RGYK0VviA2liFOjiU3mOoEEQEmPF5dUPJctsaWN3td0F4WjKVpMZOrG82CTPoBiIQq1jb9e72shYSZ9dR3KrKVgydR/51c/DcVrAVsXYb+LS5lkf/Wni7LlWQLILjHUHQHCrB5MFMEXd/HspUtDBi5qCqejrHzFmvrsY+WsGRYrmz5fWQ5KN6BL01RzYLkJcJfgDBzIIQns810Rznc4TYwXO65+OUOrUaW+sktpBjlVFJJhG1Jey7liQdQw83hKghrD6br5s1XEhJIjhMTLB6emT4EZ05YJM7BNqNw6ubE/a4THAavVMMlWPLsg+w/CjOyl6dr9pexHHZ3toHXmddt+AQOctL0E797BSY1n7WFGuKFXank3iCFyW3zDU15mxxY+bXcnC723ZpcMVyVtB5NxibW4NkTZFra1tA4qHt9ASANIWTHMMN8mZIa0RXYCHvblHulvI5MUbU2uzPAnlaBwcUzSR2tfP5E4qX1mGPnmQNXfW8aPIIU667BG/ooBF9eMmJW9Rf72faznJPZm+NxtCyqRSVxDLyPKc/tBYqHOhYYTT5TKALOvE3oWcsZVLMmvacZvHK4bGWgosWOyosKy29U+t4S5c7nuKNzMZ4V7hBhon7sI7sQanSrXaMBkZeNrt439/2g070YeKl7VUauH2zLW1fZd0ki4x0qDwQ7pXMk4wQne2tSFIltUYz8hTqbX/eRMiOlZrE8LrN3NRte7mZidetPVfC83I+P2dimZlHE56t7FPkttftuiUN83xqruJpoS+pvVAxupdbJWfNcL64bbixu9lLYu9Hcx9jS7mOLyiy1mCiUN2E0iwtNbhrrwlSqJPD5izkB6KtZbY0LrnMtcgKZBI/JKohSktToPv17TSGQmuOqnD1IhkPZrCoWudiWcLojAwH9MKjAY0hySUE02nP0C5aG36IkWqmH1EdQBEKY/6sI+sLfA3m6RUbZH440oN/bV00ZuJ97eAg6dsW7hEjyLOWalCYbiJiZ3LEwiOQPQlfj7OZtGF4029NjxuXS2sbMpa126COoxphmPfzaoWr9WqXsecDV3RmOfNO5W7EE0MwsOUFFmWtS4sZTq9uq+VFsG+RApvrVOpYzMP8Zbov187ioHZ7SzrpzOiAsCGnmlgdepa9HLD6GsssYwB0xS+gNQHAz4kbU7rd9iK4TX/VRdlh1EAITWN93h4djlBWUgfnlGLhhLl1jBx41AnX+I5alxo9RjWvqa7u1DEqsxbcVWzrcVFzG9Mlxa70/JqM3Dq+3Fx1I3rift1vkaIVsuX+4hL8Gmz5d6qR5jG3iM4O58lMXlhjf11Joqnz+/14ytptcKHzZVNtxh1uxKFT3S614qb1rV93m/baSmJwifLjtd1GArla137mHRJpoO0b694y/5Y4wtZZro+6T5GnmidLMbhtz4Uvn1setHcLq25C4g3n2bbMF3UH3/zZtokw3mtjscLVnZqthZ0WgXztuc1yLy2SKpoVHn0WVKOSzgUitqk+yvmSP24zH9TxFS6DHcE5B0wPNJjeicrtWHUlE25o0oBTZitw7XpDYZrF6wazXbHsJsOP9U5giXx7vrTSOuWq06FSZEI7xTjwGCUumjlJOarUxPTGys9HMrQ4f386boykbM5Vdm0Ub98UCi4iRwIW6AxVNC6cjb40zxYWo1WHKHc0SUP5dkzNXcTyY9lXJSdwTElvU6tMldwLheaW8WJKLg79ZjcXrBHH82JbhZJ19WoBKff1jtSMiAuPY19StVnGlunFZGraYE9AxpIOn2AZXkr7Ud27c5Sthzm/HE+XjHTZ9YLax+dwBpNEeu4VQ9hKklbiRtWCMdcSmpBcMdZudYI5X7ost9FJz6teWq/kDDvtdRVGUrTBLgo9tAWzPgWaXff1MdgnV5yy+/VuOIbmqbj2N9dmI3iWsBtE3K7GcjM4KrLeBAtOFH3OWiNrU6IvJG/2a4+qXQD2rueJ5iml3CIuBEEnudyxF6N+HnoB1ZwQFUxk0fVX18B0dCQjM6DCDZnATldRHhh1jphpb1F3CJweW26bAE7RVoMxniDd7trY0n6QV553XrOKoEiLheZt9idyc5nBbGoqrexlATO4oYYheEkmBcbXbVZ5iH3YkCzXbo7VLV2TmCpIAd4ezXrJXDSnAN2wmWP9iZkt0LM+W5Ku1+1nBTWsLBKuK4qnebibtSzaIF1LJxZK82nbko3sLI9IgOgtjjJeGs6adXRlzVgCI0w413ucz7GanFMJSx2rXqjbYL5YzUF9I8nVc2ddjcwVYZb6ViSX16OzL44wER9urrfMCzAEOPVF7SpnG8BL+gJbSwWdL2NBXzJwT7gUm2irYTVc5N4BM8Nt5uyIvXyzxcjrcGPkb8fVuYxJj9gkvct0pV5IubsNyZT2qRIf12Yq7ZIzM8Sz5LrdsWga6sHqxBJBRGPBnDjYUnIVwkqSNtKBvPGY16a0Oazn8lzoVGRfsKFLK1k3G+dlx/Teal/Wh6izY9sN+PpgKnWnF8HigmD5vOZRf5etPXhrwswAMyfElfdXjNpH5Hmk0DYTutGm28K3bpzUSPYA5kYCyVv8mrUneZhh/a5xaItMzhkR3GbosHNsEeh8QP3yLG/coCHa9U0OPS1TPWVDhVcrwQkWlUwsmHGMhIwSP+A8uiOLSPQBgGPJxSsZAGpWg1HbdeirRJiYqLof2b2V0tn+1FHEGJO9lOXWEokX1BG+bpOEx0s+uWHzpDtYgc0QF66U3ENH1wN8kOQi0dZemBBsQcJD729Xq4ANK/1Kz46FWclgcA6uuO6JkjJaMr2fYfYCJ691G7uoYfpjernevHFnr8gri5gkmqn8zDue+6xzlHlibgIwYbKLFpkpnU0jmLboBfeId2x0oAKN3KzCAMypdd/e9k7vimtPrmjfcdG1czAsGmkZUZXYptl3pY2Z3qq+1J5OXkYN9cBmmOaXpz09GxpJWeh22GIy2Sc9c+KVvQnbIdi4eLHCsakwv2lwZbAEcuzBxtC/ielicbwSG9Db6HUXjVeOgbekP5sBrKQaBCX4A9KZtE5tD07YXbfnPJxH/Yj65ioxDoSASIEnxzW5Qa4zJXZgpLB0VEPPOJjDxK6RiL52EcDmMKe6xqD0ld+iS8c8tUFtMJTiYUoZMza1VkrYQ9iZStukgFSmqxTEuSJv22voU4fZbnWUWXG/XMjBOhlJe2slBdyI7Y3E61E8xGk2g2WspWEwjcy3Mb4cxFPrNis/Gm3qyMEbFk5jpl2o+IDfCM7LjvVCLlfSaTMnkdPV4S1vJrGnVR8JFnqcpeNilzdCsIrQ67rVzCgIJGTXB0xYwcc8JmDWcObni6IH1cFP2+OO2N38zNDCwAA7GF69lrwPBuBF7lurRNpuc1RdZOx8pCsYYYb5jV36uKORu0iuU5h3adQyyFnDGO1cJNq5oK4ELTYWgxGpt+5GcrgeECVbHcj1Ek/Rca434Sqn3Y7BjysXz/IACSMhUc9uyO5H2FNXWNxj5TBoN60+BHkSYQTvZDuGFNENPpCyVLmHY7DU+SrfMCXDMH9/+fQynUI/z5L/zZfG0/ne/7NjxseJ4Nv7pPsxsm97X+6yvvy7Cv3y6aV2Y6DO4xi1Sbvweez4D4eon//1O4hp7fB4Bzu98rq1b4ftrR1Ofzr0EudeB4iHb02RdvdD3E8vTtdMf8nQfHseVr/cDcrK+8n3m7jpePb+GuBbW3x7vCl+mf7QYHqN43sxkP68DJ9nymDtAMISu803lMC/+XU5Wfl8qTEdxk5vNV5++79QWH5CryUAAA== -->
