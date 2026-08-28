---
name: "rar-cowork-cookbook-dashboard-update-work-order-details"
description: "Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_update_work_order_details", "rar_sha256": "1093b4867b993353326c13f721081ab3a314d620fc4ee70eafe5d511df719c74", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_update_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_update_work_order_details_agent.py` and in the RCI capsule.

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

Update work order details Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 1093b4867b993353…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_update_work_order_details_agent.py` first:

```bash
python3 dashboard_update_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_update_work_order_details_agent.py   # or on stdin
python3 dashboard_update_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update work order details Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_update_work_order_details',
    "version": '2.0.1',
    "display_name": 'Update work order details Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-update-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-update-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f47e979c0164e41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-work-order-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-update-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardUpdateWorkOrderDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardUpdateWorkOrderDetails'
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
    print(DashboardUpdateWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5ei2JL2X2FyPlT1UJXcQeuss9agIoIoKIJCV69q7nK/g9Bv//d3o2ZW9+nTM6dnzYexVlaK7B2XJyKeiI35y4vVNte8evnyonpWBvFWkoRXr4KszIWWeZ9XMfiVxzb4gZw8a6rQbpu8ql8+vbhe7VRh0YR5BrYrVe62jldDFlR7if95WmyFmedCYdZ4leU0YedBm9NOglyrvtq5VbmQn1dQW7hW40F3VXnlAt2uB3YmNfQZygsvq4EAYM4A2VXe1171CcpyaEXQFGQ5QF8NZZ7nAjX2ADVXD+pCr/eqV2Cfd7PSIvHqly8//vTpJQTvX7788uIkVg0+elm9GaHd9Z+BennSvnooB/sTKwvAwmIAAGXguvAqYG8KPnI9H3pefZyc/QT9x3/EvVUF9Q9fvmbQ8/X1Zfp3bLO7XU1u1Q0w07EKyw6TsBleITbpraGGKq9pq+yOHMA3C14fO79Lygvo79O9jw8lr4HXfPz6AsCprAn9ry8/AOSAvqqd3r9OUoqPP7wmOUDi4w/f5dStHXlOMwkDVr9+e14/xYKF35eG/l3r34HUR5xt7+vLb5ybXg+7Jz/BzpfXKA+zjw/BRZV3XmZljvfxhz8T61w9J07CuvmX5P74EHz1LBCjj0/Df/h0B/knCH469C7zz9UWIKx/xROw/E3dJ+gJ1J/JvuP/D6ITUAP1O+L/VNw/2wD/HfrxT337rzZ8gvyvLysvAdVWWXbifYF++aYq3PLHD+73Dz/89CsQ/d+KUfO2cu4SvqVWFvpe3Xz79uOH+v7xh59+/NAWINc8K/3WVsk/k/nPcL3r+R2Cz1Uff78X6NeyOMv7DHrPdOiXvPi36tdXSLeS0P3+ef0F+m29TC8Ympx4U/qA4Dc1UwNbf4PjDy+/AorIgDetc78Nqvzf/x3ahU6V17nfQKqTtw0EAtyEqTcZf7qGgJnqe21XHsC1DgGwz3Ug/6cITxbnPvTzfzp3JgWc+GBS5J0Bvz3Y79t0+9ud/b492e/nV+gEROdVGISZlUBHVlG+ZlbgZc2ktqg8wIXdnfca7zOgos/Tm4krf/4XpH+7C3othp/vTB8+OOq4FCZ+qtvEe518PF+97OmRA5qDd/OcFuhIcgcY5IeAWz8B3+s8AczeTHjUcZgkkBtWwPm8Gu6yAWZfJmE///yzDQz7mj0IlYAe3aNGwIJ3c6DPn4FnfhIG1+Zr5jnXHPrwy68foP8H/Ve77sInHQrg9mdEgIWiKu8hUGFtCpZNbQQQsOXeI/LLr098gZgMtBwQv9APvcdmkKGx576BrW7YzzhFQ7YHQAYAp0VeNYClobB5hQQfercXKJ1uTTx+zesGtDHQvVwvc6bGZAF33pHM8gaqQRrW/vAJamvvrvVnu7LuJqag1K3mZ2i3VEDXyBPw32TmfRHYnGchgP89FR6fAyHVhxpavIl4hfZTTkKFVVnFtbKeOnzrERfQLd62A+EWaKH912zqkN4E1b1AHvCARQAZ5xnSz1PMwRiQAjZw6zfd9zXW1NtO9x5Xfc3qZ/Jb1RQKBzQDoDRoQ3dqCX97plR9zdvEveMHLL337kcU3GdU7jmo/el4IPzjXPHe0qGvLY5iJPR/bCaZ3GF5/sjx7IlbQdz+dDQeME+GTeF4DGNgNrhbcS+p7/PCG9u8ke7XLAlBzlTD3x4r78F5rnkQWVsBG47sEXpzvLrLvSfulIhVNaW89TV7Y/dPAKk7lYHYgSoHVTAl35vC6e6bpVeA13T9vdPfAw3wA6kBkhMqWjsBieMDIGzLiYFV1VR8z8iALPamQuyvoXP9nVcQkA6SBciHgBEhKCfQAe7Q7XPgJqg7v8rT78vDaX4qHoF2ITC6eq/QGdTPlEM1KFowBE1rAAof7qKg1AMYAxPfEa6vVvEwZgr300BrikWeTlnwmwg8b37P+Lstk/lAqgVyBmDZTyTserdHZN/tfMYKGJtONXrf9PtwP32FftuG/vY1u9v4zvug9JOpg/8GHAikclrfuXZirhqwT+o9Ewhkwr1Zvz767aOhv9vy5Q8j/se/dgq4d1Dt95H7Al2bpqi/IMij6701vVfAGwjIkbDw6u8N8POj1D7f++O91D4/S+13oh9IfYH+mnm/E/HM6y8Q9oq+otMtKXS8KXGfL4DG8vPC+ExOd79mR+97mJ+5MBFvMkxV/daF3paAVhRUXjAtfnSlempmPeifdxoGgfiavafCs1AAy2fB1ELr/DcFfG/HILCPuL13C3Ara4BudxrhAm863yST+bX38iVrk+TTS2al3r90rpl6AkhXAMd0HgKlA2aiJvTuV+/z0XTx+wPevagAG7j5l6m2PkHTLPsJeh9LP0FvB4X74StrwUnpx2kknlSCpeDX+9r306PtvYCzWTMUk+mP0880iT0n5D8aMZUUsPjOsVPnetbopPEPQsCbIPCqPwqR72+s5EkUdWNNXTts3sq7Bna6YAb6BIHggbIDlQQIsgUb/qgG6Km8sgXt0Z3c/Y7fd7fyhy+/3mFoHkfIX17eCOMZg+e4CJaDyvxcTw0SAYkKFILrR0qBe/+TQfIpArAcmGKADAydEzY5oxl7PicIiiBw2sEIn8ExdIZZNmERGOnSOOo7pOcxqGf5HuVSGOb6DDZ3GBLIe+Tmt2kQCCezPNT3iDmGOy5B4xRFzjEGt+auRTKW5aKzGYMyvgsawfetMaDIp68P3yYg32faCZOny7+82DQJVm7IWmAfryUy1y0aZ+zj1YYr2jPMCyLYoVbSZ9PW13FHR+VlkUZqz6XEdr1dyMNxgzYH7UrFV+Yc7FkCF5SU901pNq6pbWgu/cLI1w25NwYTtnfpRaHGzOPDUsznnKzPsLLf0lqX7rcUuuwve9NbGw6yPaehh/miWvNzX0FgWfHENFPL1kFspmLgW4JVyUk1duRsEIwo2+tCghVOaG6WzA4ndanQk5EmqVMRFkc+uAbdfhj0bV0JiMolRj6H2/ri47tZT9B8okkxvrTdGrABvtU0HZU2+XxToLSfRRTsdRkzC1cYPPOrWUGF81u0LESntGaW6W0Hoqrc8/USd6tdwtz0hY2uNvCx2hpDczRnu6GIyyrzlOxwShjhYBzydL/OXGt57f2skvsyxdZqV6UrvBL0a6WahmlfgiKZSRqHRYWWBpHuxNtExwLXIiyAMUpLKV95UaeWjaT5wsChg7TaWEvVF45Z5BbCScavLKZmCcaK6LXfhIm+NUHXL1ts3BsMhfOHSnLiFOUWZ0+56If01OkseWGSUKVRnDirji502/bkZha9Xo8byplRVbGoKfFo8a3F0rLCWEucs9mmS/O9dTNns6I4RGSKnSLzghMCM+IVOrtu+82VzKI6UflWIPvgqFTlEnMap9vInq1cxjHnVZ6KvPZ8uXQ+zZ1lwlnYsn0d5IrH4GNiEURIbjOHv2WcYZHEMRj2ipFL/c0uSaKfHSSlRM2MTcyIES9zfJkPJu5vN52+K41aQxg+0snthVmmeCwt/eQUOoeAuexy3WxWKT8u5rh/0jOaKdtx0+MDPC7HLSztmLMpqGIsOkN9soZCpfNiNEerECu6kAvJjS2rJuenKkQWN2TpEAbS3XynnxXEbrE750jvShmHI/A5o1lBjpw5R2FM48fNmUikPEWZbTmqt53qX8vCOW/F0D8fB8C5wTVZ8fuTUy/z1WHpc/vUSsDxTOwWOwlFClk+KtRAk61608fDwA/XwqZQNukMwRbIlb/lkuU1NEQZ31yEseBMScAOYWvVaDSWRWG5Z4N0TscbOVz8pTDIHWG16cH2XYUSstVM5WO6Vm5SFzH8hVQx0YjojeTBG4qJUd3hCdWNoghejFu0JrdIM0fq2UHGoyIvBA2RQnIlN1UXiQZyNnYVHxwEt+PK7fZ6IGeZLfb4InZQMeCDWGXQ1WJG6Bruz2oqttlxL902smoRQSVI4VWkLBy/cSDVlzPF2XJel1BYQ6qpkfYXDpyGultftrrhU1taRd1K8lLdb5q+j7kYy7ceEcVzyyhm6nGHymIjMFofqkFHXwYJK+veM+j6QKZXar65rLfnMVm0ZuuqIrI/KiUXMdvrdvSRWI3hg3rWFWQJp8v5ntevmcWAashwTrb9OEglvF+dnRDPzG3e3sbNqtkVu9BjgIv2Rj2M9lk9cjM7PYdMhS89Y9TQnLlJ8lXjbYSI4HPkhmiOU7CR7TJrjccpPVMGJB7DBb2qb7XLcSeGXFlIKQbZ7KCNRnX2Dyt4k4wIkqII23IK0yxX677TES1eG7Z5WwdF7p+XjrkLE0U+KN24o5zFLWXxy5pfSkrlGU2G8rtMxG82QYX4Tk3drTnwY6ZkDC5LhrY13eEMl3EZwqizO3iARVezw2I7P1jSjEfYoydweo/Xm8UqiK/qKdyzagjOfNQZFtzDId6x6JCuL1qyc7dsXSalio4CbqLUVWC16MC2M3RrpKIwzxYXmEf8WUNuD2Klwzty2Sea1+NuKl9wt8hdwcwugFFsebwNc09RraOxrraqeAOE7MVxPlgdJid4exPlxeLiylczXSCIESzC/UhsmHjLSRojLTB4WzHMbFs1BELWGzLmc42gjhi/bS9+2jYht7gKAoDhfB2Pe4/n1iwAQUpP2prlaTii8/Wxj2XWdNlyTBj2VEqxhp1ibHdCqz6rYmGrFtVZ6FhtueqTxcYQTvjSt7Z6uaPtkNyt5+eyKVjFXduDoMd6l47+2JXH2VDPm5Nz5uZqyGsLpffH3k1uOXLBZ1WqYt4Ob9XGk/A012TaZwPvIKqLmzOsJTanMV8jA0rRzHSolotutd3Gc2bXbE5UrwfRxr8IMFU4jUxTebZdCNQ2WTTq7Vz4kt/Yg12vrrzabAq74xCeTSReugbDeTycgts1j0S8gW1B3vmtaB9GNsGrQyKgFKYo2obvFRPEL3YrDe2HBXWNYBy1c8niVrWpH8hG4KNjdxM0gRVgq8XlTRYmy4iTqEOeLMQwy4VdyQ6SJK1ysaqBFaSGm5XUz69VskC2ScoGDA26Y1/ug7Y2a9MznaVnyQKzb+bXS4npB73pxaWDz0SxNlR3S2zOTumxWGynmkUcMoq/IWYr1rx/IFCctbjCa3xfb5izbqLEXtTm58GMT0ZQUvJRFcY9rRyXnJS5JbbWOETxSHU1aHji7nA417xszh9iAlRy2SSjtqOW+W4+y/NlFDE6j+BcImsuuoSNZinr4WCKXBDkyXDkjvopEBYXArCPedtTPoyaqmHmKxalkXl/tJsTA04t0XHo9V0lsHOHqM5JgDOn1D2guq4fTujMg7uNjc592KpX4XFO5eyF23ip5CtLgXSzKlQtpDnZrgF35/VQ+aeSyjCjFVG0oXGPQG8HDN7x7ObqNRtXOC2WFzpgDUNJCds2j0GQ9Ui5otRqtbuqM08EP11GRpvS37luYPf8+VDN5fZciJmhbG7oVTpvd+f1EbtQwVZ2EadSt4k3XxlJdGzhNathdKVLe73hsn4ZG6slx1CFr3ZsnwZphqN0fEiG01yI9XZzPHGeagB7UhBNOT7I9rJOhGZIhCs2WifAJ04jJfvqQhTSvl/OQl9FC4QKblFByVt9fjOqoG4v+vLUhkKoRc1qdhS4zM9obt0aoMMmomzu18G2ycsqdcRYPmIGI9p8Qh2HKznTz8fV9lDA/G6n3MqjjqlH7bw+yZkyqPn6WvFJPco61xW2qlmtmpAkaPnnC5zEBK2NhwuaHJr5gsn3+Cq7UfipxIN9Uou4DIZBlQxrFiOYyDLMCl1TG91dDVITkzShw2te4hhYV46NPG+GWSz5OMrN9gZWn4RL6Iaaka2W6D6IHJENTi1shIFX5qOuxk21LE+b4zo6ZizhCJhcUF1fR76T7uzu4PglxnhRdQ05cT2/HeN+AMcwNF+Y2yTviXhZ7cgtuzoKwhLdwNoCX2IXc4JDiMv1uLx2IJaZrJ8xUC4l4mf2cRVo+cgxku8sWQYbQnZEXTfa1Q1jXWJb5FrLjeXsoJ48uwjZ0lRceAxnnICtiMG9pnmFyqTKZGDuolFhfbLImM3dZWYUupqeuL21CFdb18fT4KzMjH5GFUrGecGWV5pBwptVWTPu5borDyc2QqQsPR7xUUfsbaETeUk15PHm8O6eY5dMg46dvGK9WbcKWixvavJgemEU2AaQCYu8w4XtIgxR2rMy7ToEiwWWcqSxWQTbOlot/LCv5WutW0tDONaXMulNucXgfcXxVQhqbq35mVX1l4MvR6E5N/v1bjgEFy3v+ptrLa4oHC0WuLhdjTd+sFVc4T2ME0WPM9b4+iLNc2lzAYUUctWgnHjkSDLk5nLRMdEXtkK55NceJuL43KHOzmwpo4Qhq+t5LdX5bt3qHgvPdAJZMPNbqdhlJ2GnGpXneNswu6ydyctttYE3c9wknNXaaS+76z6JDP7WtjUe5LG4SKkZHW4sL1RdD3BETqbtqASSfJSYM1NXWWtsshouddxCtrOFhnFHi0nXO+0kVBHp992Zu1kBHljdVuz2N3LNlAovs0AHoy3gE4Uyh8vc1xJnMw9Pc9QuemMrg7HOxte4RXXHYyWdbqiZIsnp6B1WluFvHIcxPCq0R9eIUM+LEATGaYRkHa6s9xKpIDNNYfB4njCEpHThssJVWtWI2HUkckFYuaUII3omgtJC6hSTKDGv4D6ZH27GPlXiRLrly0UUNQObKjsfFYQcETt9jW7EHVLSSpSd9YHWbXmO9buax1BaMzcB6TCWpJ03UhSNsIYxQ5LtzEBzBjkeVxIt99WtOV9Wdm8GnR2IyApBjuPJcW/p+ni0qPXoCL7U1UUJH7obTY2uYKDtMhThSFlhmW97i2DgVAl2F85eJuKrpMF4BYBQEQm0yw7xZJnz5a1dhoqxSAUh6wz65B9n7gK3M0Y5CUe3xUjGWN5Cdm6e99HevhB1JyHWnm6N9Zq4UvmcuhG70Z0xV1epdzh3uJCpXs+jm13vEDPlT2s8Ou5Ncb621XAe7uwigZ3uIKISIJrknFWDiJ+02zacX07RQATg0NXx2uk4kpq0n60bacN0ByUSFdNNGIWzHd9czMjV4lybnXriSe3sIvvRaRGfogjOafu5tsDEIjzTIH3tJNC0zVWMt9JC1BjX4MLeoSXBuhrdpRMxNbfjPU+2HhJq5NjmfG/PFy4770bi2OLG3jMbQjmrI0fssLyG443ZxSfTGGf0gYiaWRAhdirfNjQdXczGYWiwnYwlwWGO1Hm57ObSBlc27JnbbfwovPHqzTmmvosTCWOM605xbXcVLylLWtUl3+7x/jy3s+RCOSRKOIRbXbVmpVzaUu2dzo3F+cbuD2KwYYVKpg+1NJdKWh65MFCEGxJfxFkZ6E7Wg0kVDhmxK3kb72bcaDGX5d7jFrk7wFdHWc5Nu+tgz2/qjpHyU3e52j5pL1if6TIYLTcpZ2Norc5tZnM5g7BeGRkV9xZpt6082pjknFxzhcNSDUcELTGwyh2QxD/ABG5f0PkBRA8+uMahDFkN1jkXc1NlNtxqPsdjb5eUNDUw/bYrETMjLUDDCzVWShqW08zrtWOml+Cke0WzS2JdFL6Zna2bjSAudpxhHsdzZWdSB2G+kkeaXZRytNjw1yoPxvkYoqA5XYkAnC28olGIpmgp5RDRenhYB8scacHxKysXitnDShi0kpGCOdQzPIM9S6zeN/K6qVmHyId8CPzS1rJ9sCOdhIt5JVHxAI0VtSr15tgDZ1DHvMVzOiVHGV51F4JbXhYmoWYrPxJzpXbShCbC24qQpXbAcsp3a0p1nJXD37plIF7cUjBdr4RzAIqfZxJ+8pSTP7KejQ7kJmP3RGztN+YSLXfiGuc4aXVqyEsgjWUsiQonzzA48aTctx30RqwFemNFHOVaN1pB2E09gx1a3R5Y9uXTy/Qo+vlA+a98mzw94Ptfe874eCT49vXS/WGyZ7lf7rq+/CWrfvr0UjnhZNP9iWqdtMHz4eM/PE/9/C98LzEJGB5f007fhd2atwfwjRVMf2v0EmZuWzfV8K3Ok/b+UPfTi93W05891N+eD69f7q6lxf1J+JvOSbJXdaHjfWvyb88/13iZ/i5h+obHc0Ng0PMyeD5lBrsHEKfQqb8RNPXNq4rJ2edXHcBH/BV9xV5+/f8HCw0f5yUAAA== -->
