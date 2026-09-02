---
name: "rar-cowork-cookbook-dashboard-control-project-scope"
description: "Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_control_project_scope", "rar_sha256": "29e92a30983b85b24e196baff9b4c2c60a58ad588d9ab3db1eb73fd672ad0ff0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_control_project_scope_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-control-project-scope:0d01698c5eb1bb4937febbfa015cf83c15f31bb0e820e3832b8484c8b25db91f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_control_project_scope`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_control_project_scope_agent.py` is
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

Control project scope Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-control-project-scope
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 29e92a30983b85b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_control_project_scope_agent.py` first:

```bash
python3 dashboard_control_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_control_project_scope_agent.py   # or on stdin
python3 dashboard_control_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Control project scope Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-control-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_control_project_scope',
    "version": '2.0.0',
    "display_name": 'Control project scope Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-control-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-control-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f03f84e22a57e1ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/control-project-scope'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-control-project-scope', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardControlProjectScope(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardControlProjectScope'
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
    print(DashboardControlProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOj1rLtX+HV/dD2obrEPNQJRzwkEAKEZgkht6OaeR7EDL7+73cjqarbx/Y9xxHvw1NHVUli7xxWZq7MDf3rk1FXflY8vT7tHSOFRCOOA98pICO1oVnWZkUE/mSRCX4gK0urIjDrKivKp+cn2ymtIsirIEvB9k2R2bXllJABlU7sfh4XG0Hq2FCQVk5hWFXQONDioC4h2yh9MzMKG3Kz4i41i6G8yELHqqDSynIH+gyB32kJNgNTesgssrZ0imcozSAep0jIsICuEkodxwYqzB6qfAdqAqd1ihdgm9MZSR475dPrz788PwXg/dPrr09WbJTgqyf+3YDZXffmrno/agabYyP1wKq8B8ik4HPuFMDQBHxlOy70+PTD6OUz9I9/RK1ReOWPr19S6PH68jT+29XpzagqM8oK2GgZuWEGcVD1LxAXt0ZfQoVT1UV6gwwAm3ov953fJGU59NN47Ye7khfPqX748gSsLIwR9i9PP0IAwS9PRT2+fxml5D/8+BJnAIYffvwmp6zNG7Y/3WLz8vb4/BALFn5bGrg3rT8BqfcAm86Xp++cG193u0c/wc6nlzAL0h/ugkEQGyc1Usv54ce/Emv5jhXFQVn9R3J/vgv2HcMGPj0M//H5BvIvEPxw6EPmX6vNQVj/jidg+bu6Z+gB1F/JvuH/L6JjkPzlB+J/Ku7PNsA/QT//pW//24ZnyP3yxDsxKLPCMGPnFfr1bb8RZj9/sr99+emX34Dofytmn9WFdZPwlhhp4Dpl9fb286fy9vWnX37+VOcg1xwjeauL+M9k/hmuNz2/Q/Cx6off7wX6j2mUZm0KfWQ69GuW/5/itxfoZMSB/e378hX6vl7GFwyNTrwrvUPwXc2UwNbvcPzx6TfADynwprZul0GV/9d/QWpgFVmZuRUESKGuIBDgKkic0fiDH5TQ4VHUX/eKtFy+JPZXCHw7ljugCKOOK0gsjOCD1EYPMhf6+n+tG6UCcrxT6uSDCt8eNPj22PF2o8GvL9DBB1qzIvCC1IihHbfZQIbnpNWo75YZZZ18bkaVN6q92bCbSSPdlHXs/BP6+m90vN3EveT96MKXFMTkTtuVk+RZYRRB3EPGyFFmXzmfAbECHgFCYtOwImj8VecvIy6a76QPtCzQSZzOserKgeLMAna7ASDjZxDwMotBG6hGDMsoiGPIDgpgSlb0t5YDcH4dhX39+tUEZn9J7ySMQ/dWU07Agg+Doc+f88Jx48Dzqy+pY/kZ9OnX3z5B/w39b7tuwkcdG9AMbnCBRI4heb9eQaAq6wQsG/sOiK9h36L262/3OIzWpaA3gloK3MC5bQbSvqXA6ME9OO+RAT6PJjrFQ9PvcYNaH+ACBRVAC9R3+fwlHUVkYGnRBqXzDuJ98x3691Df9YwxKR8Ygji5RZbc1t6ybwymlRX2CyS50AdSwF0Q12qMqJ+VFUhY0GhtJ7XGHmpU30KYZqAZg5op3f4Zqkvg6ij5qwlEj+AkgJiM6iukzjagx4EGXmUjQDf1YHeWBmPgH7l6/xoIKT6BHJu+i3iBVg5AE8qNwsj9wiid2zrXuGcE6G3v+4FwA3T7Fhp7uTPG6FbNt8yb/ekEIf3r2PHR9aEvNYagBPT/0cgyusGJ4k4QuYPAQ8LqsNPvOTfqGiG4z2lgerhZcCugbxPFO/m80/KXNA5AnIr+n/eV7i3N7mvuVFcXwIYdt4PenS5ucoMKJMsY/aIYE9z4kr7z/zNACYSqHKkM1HQ0MkT2oXC8+m6pD7AaP3+bBaB7Ho71ATIcymszDizIBUDciqHyi7HUHlEBmeOMZQdqw/J/5xUEpIOsAPIhYEQAUhj0iBt0K1AyYH665//H8mCcsPJ7kG0I1JTzAmljioM0LSHTAWPSuAag8OkmCkocgDEw8QPh0jfyuzHjIPww0BhjkSVG5XwfgcdFkK5jowH6PmoRSDVsowJYtiAIoNS6e2Q/7HzEChibjHVx2/T7cD98hb5vVP8c6xHY+K0bgNl97PHfgQNIvEjKGy+B7huVoOIT55FAIBNu7fzl3pHvLf/Dltc/TP8//L0Dwq3HHn8fuVfIr6q8fJ1M7n3wvQ2+WFkyATkS5E75rSV+fpTZ50eZfb6V2e/E3lF6hf6eab8T8cjpVwh9QV6Q8dIysJwxaR8vgMTs81T/TIxXv6Q751uIH3kwEh0gX1DR7/3mfQloOl7heOPie/8px7bVgk55o71b//hIg0eRAFZNvbFZltl3xTv6NAb1HrMPegaX0pH47XHA85zx6BOP5pfO02tax/HzU2okzr8/8owEDPIUYDGekwDgYFyqAuf26WN0Gj/8/tB3qyZAA3b2OhYVaHZgzH2GPibWZ+j9DHE7lKU1OET9PE7Lo0qwFPz5WPtxojSdJ3Bmq/p8tPt+MBqHtMfw/EcjxloCFt/IdWwTj+IcNf5BCHjjeU7xRyHr2xsjfjBEWRljiwSd+VHXJbDTBvPUMwQiB+oNlBBgxhps+KMaoKdwrjVoyvbo7jf8vrmV3X357QZDdT9d/vr0zhTj+/uEcM+a8eT5Hw5xI6LvzfdtlGuMu2+j1g3g23D6BpwLxib73SVvnBje7jn49ApYxnl+GmEsAjBxD7eT9NPdGODFt7EWSAB8MZZmXU1ACQFJoJXnowcR4LrvFIxfB/Zt/fjm9a9n4T8v/FfERlCKZSzSMVHTJFicdh3TdA0EJS2XwS2UdHFwAXEYDHFwBsdMhmAIizEx0jZZ1AU2jFFMjIcNE3TEH1j/AfLfHc+f7ttBl8BICuzHWIfFDBxhGdxkSBMjHJSlTMN1WZOwMItCDJIxbJJhbNYwcdtEHZPGXZuiMcNGXPcG3mNCvNv09j6Nv0fkXv7AmiQJRosxw7AYi0YJm6UNynJwxMQtB8VQm8YdhGRxl2EcAuz/2PqIyhi0u9tjuoLhEIwqzajn10eUxxSkCLByQZQSd3/NJuzJoDDa3PkmXFCOfjlPJDM4Xvd2Y/umfEEXmrUSZodpesECRjrVwqqXBXRl7by1cbQLce3zLJfS8qa2a5dLuiShNJEz11KqJod4IOMeZkjM94KZnipXRonPYhAvWVlWFOq4PXkFLinoos/l5dlL8YGsNZyepWcMDTs10SaTpl0C76+VQAmXvMsjA09n+q5N9PrYO4tZNU+IU3Ba7lLHVCe9afRdslnBQz3f4lq+HcA5GWM36sRlYsIrEKQnTlJ51JgLe9JKsczNaHs5BHo6kLCbDsjEOW+wWAZhTzfwlgkdXfYxIU3nzhytTvukaOxkgkXFSojpVhNNhF/Cu2JZbE/7lDDzpVyvD/GkEO1aNi7MXG2zI3Wts+2M7IF4GSZWohzPTek83+7P+X5fHBY6E2O1f+2i0p6hyvJ0Xqv5ydLPWpzUaIaua9K/4JmNholWb5lDuy12huytSCoVhr4hkDYxOcTs+J70ImqrL7HdFW3bStNxjYxLB7b9aD7U+4PBc8Vy5g4WedhcFOI8kP4VXVZamRLUPlaUrjjS+infhhcWBUcQUxEtTNldd7XhwatNuJ9hAj2t1kmkXmmHKeVrxpTXrCtT2AC0i5hHKtRaIZTc9HrSZpWkE2mjKAeM9NhDe6KpNhUnmGVRfMRfDdysExolke0VJJ++MFlHlBGiq/uymcNxI+hhglStPxvWCCZ2Pk3G2sWsdmp9rqfk6eIAAI56PXCuiGgaPd9fMpK42rtzuBxqSuC7dKDFub/B1G4tHKNW6v04Vtxtf5nAIW2UCXY6nTNSU3aJpMlaZyWAEbid6s8oQTucFuvz8f5zOM6xHI2mSzYVFXuvEfAc631Y5BluLja5JmcbH3Gx2RyZpOcN00/aNR+dl/u1bVDny0ZgcwNd7+P46NRiulv0g2Jpohy54mbIStbzQ15cHdSGiiyTXPrJYckQ+FbFgziiVshio8T27mSla0shJMVv1KWmgHaPq7M5t502QnSE19Ra2mgiLgy5kMlq1Qa5Xl75aHcQcCroWiKZJh2+hoUusN3kbKuNDRtnZLc+scLgOzvGOh+Ls63JU3HTSzTs7IG77pwl16fJckrgVrZHi6oJJ23gN7qOCVFChkQ1b2g6EAn8FKMrb0tgGSbYxuVwtB0+DxE61NYyrV0W+N6/0D5BURk13xhJWTKrhsrnAurshw2fiMf0mMUZu2QbQdmt3eV14WH7QCJbTEiO3fmQVEI5uNeFvCHha2mYO1jDN7NGCfZt3tqG2RfWMHQCUnRVbsSIvJAKOCaujOGXi0DZCat55rjTU7fXA9IvEtsvZ/ZwPFCeU1PSDqQuGfhKLGTxfrItL17W5kG3NFijtnsqXYBi3m4QWucLBdQVomjLSx7u8MTqd0vLO+/O4kW7xMNyOTtJh2NNFpFyPva6nZnDSt2V84NVhPCl7ufFChtUanMRsxVq1QPliMwqOVHtQe3LnhiS1NuUqX523EpYX0u8WhO8xdcUW67MSaS3C/LsbC/rxeKw7aJBmV0wpCKIOXmRu6hfHi0GWStbb1hE9TpxQ507HVufqboMtzmtU81ccRtqSlxWh5GCw+OOmSznCcu18gmuDkfNvQ6DuezmBTFXle2W4ZSzLUULhl8BjlhhMnFxVdendtvdYqC41W6FasS1do5+GgVcye8DM9iJRsgNJ6eXmXlgqm2pRnMpsDYqIgzXSN7Yqe/AycJmK0nZr0NgcSQ2oSdWHdZscqkkj40yG5YFyVrnAqNqRd1J8lbZox3a4E2EZL3SkGtSy3FJFKK8DrezgZlMhIhv1gQV1ijPIWcJLhcpRbOwtCNYIp7Au0N7xDlN0botchQrrblW6p6bXXTBVnQtHELRNgSBV9hTltjbi6d1VGBYl515xrmdPb32J2paaXJ0Qt0IlTyEBh0kWlz3eXiW1q3bD15MLnXp0EVOfMw15xjhrXJa57W1QU6a5cQ63Rnnqc6H0+oYECfxIs4nmsTMUVfMdzs+2rowdZa356ojqj2rtsVuflVTx4ttczUctmS20rlZZKCVfFbLJtsv3cOUI/c1leQLsVU85pDkCuxuCjVhJINpZLRviQDwprY5Tv39ScaVWHHY+ExtcIdN6Cmxi4odleCo1Hk58EPfCrGaSS0+QdlCXTYJxTQLKnAWcCboJ02N1yF9ROdbJ+cwOxqwfX7Fk5m0VKNJgqz4TuoFYdFd9liNXMrdxFiUKCbns66DTc/r1FpUJOJ6yKVgIXE41nrSwAumfC5mKoonve1KW8LL0JzkLtf1ZX4y7H2pH1PVq7BoO8W9PC76uD045uokavg0uoR6K0R9d+l1k62OXSafuxUanK/SVNIcWu1qZdrgKC7XYjc7mSdcMJ0uCdj5cn9aarW4AExBVadoG6q4tu09exZrWrNF6EXLl7FnxU5WJrKLUOrBCaUd3cm707qNRVFPECGDjwy/LWlZSAALakcHmZH6ilNOwWDIkteQArJbdMfQk3bnQeM2l25NujAi77eXbJYiOLzwWny/wVKzY1JhGsGxx+etY1ck7+eKgcr2HDmJ5qEiqU3VHCqKoCuY2xHX9QKWRSymz4teIpwEb4oVEJ6W5cTJldxtyMGSCdWUqNiisCmFNFu4XorcQnaqkyMM09n56nG6voHxxWGvgeNrOwn4fF9MVX9PW1PZbniCzneXtI/KdpWxUhNo6Zk/CUOyDEVHcKhCyqil18/PM6Y5ytN9qgUVQ+bnzRrtFQ9UbH9NtkuKX26n02hDmE2CTjdOkJxnlHFolY4/yWmXTI2hPG11mkyM/CDBnLA2uSKSOkTXZWSvnEl5RfgyhtbH1t6svZr2Nj2ZN7sUDafJ+hoTLX32K5jfiK4WiL3kx4fjcUAWSrIv15k+lw/zbqlXVSSduOs1CbD5ivd7MUtlXsddVcWrKlBmnNmjMrPzKxa0ycVMd1wxXlNWMZ96c7yk1qjaOVe7kJB0ebCIwegWDjWrK3pTIfLVa/w1g/YLfDtkUjN0zeISzkzqRKpWF5pwfG6jmi1pe4oeVG0eJu4Wja6p0meuhOmp3V8NNsdzdZEmZqZzeHKah2onSqERi3LbsWtGWsz2EnqoIyJbzAypPXbGJYlzP6vDXcHhpTRf53E1UQPXSlS72VruFaGcuPADQZ6j3TxqyWoPhrhZP1/u/I2qajIacaK33c6zNZBZzq9Zi9lyuwP0mpx4B/B0c7zmwLBGqhsweRw4LesFut8yMw7GurAdEKsKVXVFKzjvyou1YUdOut2sHHodqMZlc4F7gxEkdIr3YNTMihQleDN1OYpCpPlBISIus2ep7p8OiS2gyjTgFdNNVp62YfQWZNEyVS6egm0KShIr9hrQ1TlUr9sDF06WaazttH6Grwck6BD0iDHZUM7AoZ3zNYTK4ThrlzUNUKooVV4hSyzNt2JCGDu33yWOVIV6lm8WuZnta93yiIGzEL5s5/XB5+edLi62mBLzaiQhQ6wxSOrqbYJ6qxNmIZ5y3dDxngi9VbrDNo7WTg9qqcyx2ZSpCtcjbCnbhlagRm7pZxFSmW26ivkgRYVpVWl9bbEdO8DN0sFoaXXBUfmyP3UwL2243lQTZ2Wd13EqzHiWTXk4t40ZPd1dqy6f5JgCT5BNrSXRxD0RbOVUrn42JNzTzixhcROtMfY0zcG1H1T0CoV5/4J1xOHKe62SXxclPlcRIj7WFI8exNpalBZnWqHQ5zR3XpnbRjqyZbw61YehRS3JJ/eVcSDSnYh2JgOGUVifYtEBlEpjd8yCoikKg+WGWzpztl2hdHamt0hcTQ/Bll2URVv6ot2rmF3Z4dWMZkbfMrZ4SckTYka8liw6bNHsAry0rQ1ar2UdVsCZThrcaFap1+FIV9akE5g0I/HzwoThOhLPOV9fDuYBnUXBYld7mbXY7HKKPy0R0D6qAOvTbtaRnMAhJDyY4BjKzddrejnbIu3EK/3QSpjtQnKjAV5m9dJWixpXSF1ccuYKTexm1ztTn6eumHe12yuPnRG6D1Nh7h7Lfh3xy4IQmaw1HXGKMmt9kaMkCYaJxvbqNUMxUqlerpNa2PjgEIGepbOVMyEYAyhPmOHYbEgHFU51foaolDbDFuRVzg8k1YIZYRFfN+zlRC0nFDqh+fnsXE1ZdiqUHDqP+GHDLkPPwUp6TZOBXCpNU+3mobBl2ipULpgbGs45Ro35lh7ohusvFRImq5Qt2dCeRCrWbo+EYmPsQdZLa6KTh9yjp3qqRlRwIqfrTiz6tNYaV7ckbr8aQr4j57RsErG8LvKWPHlu3i5CXiJIC9RoMsPA2WQoF12Uqn3fFYBwbLLjiF1baOvUX53Vtew0cjhx+GmG2L64yjYnzg6MvV9XkxIldWEuMTLCuYQUNaYz5crF+grYWFsCuI1jgZH8ul4m51ZPZzbCJis3rNJzBQ40+8L2K6LuLXu+VAev064YuV1dWZW/+ptkP2PgcJg1VqwvdLPIRfiAsRRlXBxCWEvWecsktVQx4RTZhPwJAbFMV9l6TsEzxHVPNR1ctdByDacVsnnbawvztLLMtYf0Ln7SyBXC0hfWQDNd8YctdvaopXSmVNzbyz7NccWaskuJ5SlqcxACbyN1EyGVJ4q3s9KWgY+zYCEX16mJxRZ/MOh0tnSEaVZRsGVtZvzFxc6wWiWaa6PIEi8mYkWtMm8DT7qWOvGDN6fQZG6VZKAUkx45WxgLBNRrs3FVuFvR/uSsr3ibbVp3QrpW1V5FhoY5rCQNWGPmRLhsw4MgIISS7rMCmVssjIgSdt0yu4ySr2wXNB5MFKyuecZsps+vRr1McZI6Tvld3qR0WIjLQd6Ufg2jKlGRg8Y0EyOgmV4+WpbHr/3BYDwBEWdIPONX6JbsyZYSqsRdomi+Wp4xmMaOjblxF6w2a0VfPQ61zw4xZWs65yxCxJ2vDmd/O1mKyXbltaettOscgwvXsHgST+DAioODFL8G/B+1LXMqDHZ/tOLm4qChTMeLjBr4nMJY0quYhdWsWqG+4mWMKQy71F39slqhdXgVavvMzsNDv6YvvUBQIiH7Lqlv64O17zX0zFy3ex8O3M1llcEoU07J9LD0HJWjnZ2H2tlyH7URrkvbcrU5ew7XrK8HNWM8cjh3HVGHDkymISLaQ8mUhwR1F9GE4Qp72XPaNuc47qen56fbU9ynVxQhWer5abzf/7hr/zfu+npDkL89BOE0yj4//b+7LXm/Rfj+NO92C98x7Neb9tf/2MZfnp8KKwD23G8Tl3HtPW5E/stt18//5k7wuLm/P4EeHzl21fuzjsrwbvepg9Suy6ro38osrm93qQHGdTn+/5Py7fGo4OnmUpLfnju863v6uLX9VmXjSjcYr98eBycO4KvKeXz0Hrf0weYeBCuwyjecIt+cIh/9fDxUGrEfnyo9/fY/eqYYUGgnAAA= -->
