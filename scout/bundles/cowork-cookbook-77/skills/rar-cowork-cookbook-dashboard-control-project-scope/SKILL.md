---
name: "rar-cowork-cookbook-dashboard-control-project-scope"
description: "Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_control_project_scope", "rar_sha256": "29e92a30983b85b24e196baff9b4c2c60a58ad588d9ab3db1eb73fd672ad0ff0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_control_project_scope`. The original RAPP
agent is preserved byte-for-byte in `dashboard_control_project_scope_agent.py` and in the RCI capsule.

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

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjVrbtX+Hl/VDlpirFDKoORzwkEAKEBjQAcjnKzPMgZvD1f78HSZllt923uyPeh6eKrJTEOXtYe++194H89cVs6iAvX768HF0zgwQzScLALSEzc6Bl3uVlDH7lsQV+IDvP6jK0mjovq5dPL45b2WVY1GGege37Mnca260gE6rcxPs8LTbDzHWgMKvd0rTrsHWh9UnZQI5ZBVZulg7k5eVDap5ARZlHrl1DlZ0XLvQZAv9nFdgMTBkgq8y7yi0/QVkOcThFQqYNdFVQ5roOUGENUB24UBu6nVu+Atvc3kyLxK1evvz086eXELx/+fLri52YFfjqhXszYPnQvX+oPk6awebEzHywqhgAMhn4XLglMDQFXzmuBz0/fZy8/AT97W9xZ5Z+9cOXrxn0fH19mf6pTXY3qs7NqgY22mZhWmES1sMrxCadOVRQ6dZNmd0hA8Bm/utj53dJeQH9OF37+FDy6rv1x68vwMrSnGD/+vIDBBD8+lI20/vXSUrx8YfXJAcwfPzhu5yqse7Y/niPzeu35+enWLDw+9LQu2v9EUh9BNhyv778zrnp9bB78hPsfHmN8jD7+BAMgti6mZnZ7scf/plYO3DtOAmr+t+S+9NDcOCaDvDpafgPn+4g/wzBT4feZf5ztQUI63/iCVj+pu4T9ATqn8m+4/8PohOQ/NU74n8p7q82wD9CP/1T3/63DZ8g7+sL5yagzErTStwv0K/fjnt++dMH5/uXH37+DYj+l2KOeVPadwnfUjMLPbeqv3376UN1//rDzz99aAqQa66ZfmvK5K9k/hWudz1/QPC56uMf9wL95yzO8i6D3jMd+jUv/k/52yt0MZPQ+f599QX6fb1MLxianHhT+oDgdzVTAVt/h+MPL78BfsiAN419vwyq/L/+C1JCu8yr3KshQApNDYEA12HqTsafghDQUnWv7dIFuFYhAPa57klik8W5B/3yf+07hQIyfFDo7J36vj1p79tzx7c77f3yCp2A2LwM/TAzE0hl9/uvmem7WT2pLEoXkGB7J7za/Qxo6PP0ZiLJX/6F5G93Ia/F8Mud2sMHN6lLceKlqknc18k3LXCzpyc26AZu79oNkJ/kNjDGCwGhfgI+V3kCqLyecKjiMEkgJyyBorwc7rIBVl8mYb/88osFjPqaPYgUhx7topqBBe/mQJ8/A6+8JPSD+mvm2kEOffj1tw/Qf0P/26678EnHHhD6MxLAQum420KgspoULJt6ByBe07lH4tffntgCMRnobyBuoRe6j80gM2PXeQP6uGY/YyQFWS4AGICbFnlZA3aGwvoVEj3o3V6gdLo08XeQVzXkuKBlOW5mT93IBO68I5nloK+B9Ku84RPUVO5d6y9Wad5NTEGJm/UvkLLcg24BWmGdT2beF4HNeRYC+N/T4PE9EFJ+qKDFm4hXaDvlIlSYpVkEpfnU4ZmPuIAu8bYdCDdB3+y+ZlNbdCeo7oXxgAcsAsjYz5B+nmIOOnQKWMCp3nTf15hTTzvde1v5NaueSW+WUyhs0ASAUr8JnakV/P2ZUlWQN4lzxw9Yem/Yjyg4z6jcc3D5l/OA+I9DxHsPh742GIIS0P9HA8jkBisIKi+wJ56D+O1JNR7wTrqmMDymLjAL3C24l9L3+eCNXd5I9muWhCBXyuHvj5X3oDzXPIirKYENKqtCb06Xd7n3hJ0SsCynVDe/Zm9s/gmgdKcuEDNQ3SD7p6R7UzhdfbM0AFhNn7939nuAAXYgJUBSQkVjJSBhPACEZdoxsKqciu4ZFZC97lSAXRDawR+8goB0kCRAPgSMCEEZAca/Q7fNgZug3rwyT78vD6d5qXgE2YHAjOq+Qhqomyl3KlCsYOiZ1gAUPtxFQakLMAYmviNcBWbxMGYaa58GmlMs8hSk8+8j8Lz4PdPvtkzmA6mmY9YAy24iXsftH5F9t/MZK2BsOtXmfdMfw/30Ffp92/n71+xu4zvXg5JPpo79O3AgkMZpdefYibEqwDqp+0wgkAn35vz66K+PBv5uy5c/zfIf/7Nx/94xz3+M3BcoqOui+jKbPbrcW5N7BXwxAzkSFm71veF9fpbZ52eZfb6X2R/EPlD6Av1npv1BxDOnv0DoK/KKTJc2oe1OSft8ASSWnxfGZ2K6+jVT3e8hfubBRLbJMFX0W+d5WwLaj1+6/rT40YmqqYF1oGfeqRcE4Wv2ngbPIgHMnvlT26zy3xXvvQWDoD5i9t4hwKWsBrqdaVzz3ekgk0zmV+7Ll6xJkk8vmZm6//oAMzUBkKcAi+nUAwAHw08duvdP74PQ9OGPR7h7NQEacPIvU1F9gqah9RP0Pn9+gt5OBPcjVtaAI9FP0+w7qQRLwa/3te/nQ8t9ASeweigmux/HnGnkeo7CfzZiqiVg8Z1cp1b1LM5J45+EgDe+75Z/FrK7vzGTJ0NUtTm16bB+q+sK2OmAoecTBCIH6g2UEGDGBmz4sxqgp3RvDeiHzuTud/y+u5U/fPntDkP9OCv++vLGFM8YPOdCsByU5JT9TT0DWQoUgs+PfALX/tOJ8bkdUBsYWcB+bO7OMRNH5gxuMaSFES46pyzT8+YWYWM2hZgkYzokwzhz08IdC3UtGvccisZMB/G8yZxHUn6bun44mYSZps3YNEo4c9qkbBdHLNx2UQx1aNxFyDnuMYxLAHTet8aAF59+PvyaQHwfXic8nu7++mJRBFi5JiqRfbyWs/nFpDDaUgMLLinXuOoz0QrPt6PTOoElXdG1Zm/55WmRXbGQES8Nvx0kHt3aqr8zz04p7AJuzma0tG+cxmPTPk0pTWCtnZgp6SkZyWSAGRIL/HBpZPKNkRNdCJPNXJJkmTofLn6JizK6Hgppo/sZPpKNhtPLTMfQqFdSbTZruw3w/lbzFH8t+iI28WxpqF1qNOfBXS/rVUpcwstGzVxLmQ2WOfTpfguPzeqAa8VhBGcxbL5XZh6TEH6JIANxEauzxlznF60SqsKKD9dTaGQjCXvZiMxcfY8lEohrtocPTOQaUoDxWbZyV2h9OaZl66QzLC63fEJ3mmAh3AZWy015uBwzwio2UrM7JbNScBrJvDIrpcvP1K3JD0tyAOIlmNgKUrKyRH11OOrF8Vie1gaTYE1w6+PKWaLy5qLvlOJiG7qWpA2ao7uGDK547qBRqjUH5tQdStWU/C1JZfw4tATSpRaLWD03kH5MHYwNpt7Qrqs1A9fIpHJhJ4hXY3M8mRxbbpbeaJOn/VUm9JEMbuim1qqMoI6JLPflmTYuxSG6ztHarSxZsDFZvamN6cPbfXRcYjy9qHdprNxol6mkW85Ut7yvMtgEZIBYZyrSOj4Svex20Za1aBBZK8snjPTnp+5CU10mzDDbpriYu5m41aQ0SiKHG0g+Y23NXUFCiL4ZqnYFJy1vRClSd8Fy3CGY0Ac0mWhXq1aVRm8W5OXqAgDORjOynoBoGr06XnOSuDmqHm3GhuK5PhtpYRXsMaXf8ee4E4cgSWTvMFxncESbVYpdLnpOarKaipqk9XYKSp5VlWBJ8drpst7p58fP6bzCCjRebOaZIDtHjYBX2BDAAsewK6EtNCnfB4iHLVfILNP3zDDrdlysb447x6T0656fFya6OybJ2W2ETF0Po2xrghR7wn7Mq7kfRJywPSktFdsWuQnS04Yh8IOCh0lMbZH1Xk4c9WJnO1smRDlolY0mgyaEK8sVe1i0fHyGd9RO3GsCzo8Fn0tK3YWFUd24WD3xOBX2HZEu0h7fwXwfOl6qO0rrwKaOqLvLnB8DV2Vs/VzqjiYthP0g0rB7BO56qzm5u8w2CwK38yNa1m0068KgNQyMj1MyIupVS9OhQOCXBN36BwLLMd4xr6ez43JFhNCRtpNo7brGj8GVDgiKyqnV3kyritm2VLHiUfc47rlUOGfnPMnnm3nLy+rO29zWPnYMRbLD+PTc66e05qvRu62lPQnfKtNSYQ3fL1s5PHZF55jWUNrj2PNI2deFmSDSWizhhLgxZlCtQ1nlt6vc9RaX/miEZFCmTlAtnfF8ony3oUQVpC4ZBnLC58lxdqiuft4VYb8x52bjDFS2BsV82CO0wZUyqCtE1jbXIlLx1B7Uje3rqi5ctWsybjbLi3g6N2QZy/p5MJzcGreKWq1OdhnB12ZYlVtsVKj9Vci3qN2MlCsw2/RCdSdlqAZiTDN/X2WG7no1v7tVeL0jOJtrqHm1tWax0a1J3T1cd+v16dDHo7y8YkhNECvyKvXxsDnbDLKTD/64jptd6kUGezl3AVP3Oe6wWq9Yhey11IK4bk8TBUdnlZltVumc7aQLXJ/OmncbR2vTr0pipciHA8PKuiPGa4bbAo7YYhJx9RQvoNSDuh4pdqtuUY24Ne45yOKQrbhjaIWqYEbseHEHiVmFltJVSrwSQ3uvIPx4i6W9kwUunK6deS3Kx10ELI6FNvKFusfafSFW5LmVl+OmJOe2XmJUIyuqKB3kI9qjLd7GSD7ILbkjtQIXBT4umuiwHJnZjI+5dkdQUYNyLKKLcLXOKHoOiyoxJ5IZrJ66M85qstYfkLNQa+2tVo7s8mrwjmxo0RgJjsnznDy/5KlzuPpaT4WmfVUtHWdVZ3EbLtSi1qT4gnoxKvoIDTpIvL4di0gXd503jH5Cbgzx1Mduci409xzjnXzZFY29Ry6a7SYG3Zv6wuCiRX0OiYtwFVYzTWRWqCcUqsrFBw+mdOmg1z1RH+dKV6qrm5K5fuJY2/F0IPOtwS5jE60lXana/LjxTguWPDZUWqyFTvaZU1rIsLcvlZQRTaaV0KEjQsCb2v68CI4XCZcT2Z0nOrXH3XlKLwg1LlUqxVGx9wvgh3HgEyUXO3yGzktl06YU066p0F3DOW9cNCXZRfQZXR3cgsWceMSOxQ1Pl+JGiWcpsuV6ceD5dX89Yg1yrdSZua5QTCqWfQ9bvt8rjSCLxO1UiOFaZHGs88WR4y1JL5cKiqeD44kHws/RgmSvt911dTGdY2WcM8WvsfiwwP0iKYekO7nW9iJo+CK+RkbHx0N/HQxrXp/7XNL7LRrqN3Ehai6t9I28aHEUlxqhX16sC85bbp+G89XmeNlojbAGTEHVl/gQKbh2GHxnmWhae0DodcdViW8nbl6lkodQysmNRJXuJfWy6xJBMFKEz+Ezwx0qWuJTwILa2UWWpLFl5Us4mpLotySPqOv+HPmiqo8au7/2O9KDEel4uObLDMHhtd/hxz2WWT2T8YsYTnyu6FynJrmgkE1UclbIRbBONUnt6/ZUUwRdw6xK3HZrWBKwhNbXg0i4Kd6WWyA8q6qZW8iF15KjLRGKJVKJTWELCmkPcLMR2LXk1heXHxdL/eazhrGH8fXpqIFDVTcLueJYLpTgSNsLyWk5gi7UazbEVbfN52IbapnOXfgx3USCy7tUKebUxh9W+pJpz9LimGlhzZCFvt+hg+yDih1u6WFDcZvDYhHvCatN0cXeDVN9SZmnTu65i5T16cIcq8vBoMnULE4izPI7iy1jsUcMQ0KOsk5KWyKQMLQ5d85+5ze0vx/IolUzNFqku1tCdLQe1DC3FzwtFAYxSE7n84is5fRY7XJjJZ1W/cao61i8sLdbGmKrLRcMQp5JnIF7ioLXdSgvWWtAJUYN6jlok+ul4XpCsqPscrXwV3hF7VCld29OKSLZ5mQTo9mvXWrZ1PS+RqSb3wY7Bh3W+GHMxXbs2/U1WlrUhVTsPrLgRO/iZl7RzgI9KdoqSr0DGt8yecg9ETMyZ7iZ8wIvlHWWWrnB4ullFSm9IEZmIkhdP98x4np5FNFTExP5emmK3bk3r2lSBHkTqSWLV+JqVyT1TAk9O1Wc9mB7N4RykzIIeWmF9qu4I+sjGOKWw2qjBntF0SQ0ZgX/cFjlOyCzWt3yDnOkTgX0ml44F/B0e74VwLBWbFoweZxYLR94ejgwSxbG+qgbEbuOFGVLyzjnSeud6cRudthvXXoXKuZ1f4UHk+FFdIEPYNTMywwlOCvzWIpCxNVJJmI2d5aZEVxOqcOj8iLkZMtLt762Z4wOZNEmk6++jO1LShTq+S2kaz1SbocTG802WaKp2rDEdyMS9gh6xph8rJbgKMkGGkIVcJJ3m4YGKNWUIm2RDZYVByElTNUb1NQV68jIi/26sPJjY9g+MbI2wlXdqjkF3Ko3hPUBkxNOiUVkTDQGyTyjS1F/e8FsxJdvezo5EpG/zVRs72rd4qRU8gpbLpi69HzCEfNDZIdK7FVBHiO11WXbhAszlF/UtTY09ryfj3C7cTFa3F5xVLoeLz3MiXt2sJTU3dr6Lsn4JTefZxxcOOaSXqi3ui9mBSbDM2TfaGk88y7EvHZrz9BNEfc1fU7Y7ExrzSNNs3AThDW9RWEuuGI9cbpxficXt3WFrxSESM4NxaEnobHXlc1adsQPBc3qW+vQiud5lWwvzWnsUFsMyGNtnohMFdDeYsAwChsLLD6BUmmdnllTNEVhsNSyG3c177Yonev0AUnqxSk8zNdV2VWB4AwK5tROdLPipTl0jCNcM/KCWDGnpeseW7dqiFeOvUebnWTAMjjTiaMXL2vlNp7p2p71PJPlJK6vLRhuYkEvuOZ6sk7oMg7XauPn9nqvFhR32SCgfdQhNmT9sidZnkVIeLTAMZRd7Xb0ZnlAuplfBZGdMoe16MUjvMmbjaOUDS6ThrBhrS2aOq06uIuAo26Yf3O6G4fpCD1EGb/yztWwi7lNSQhM3lmusECZnbEuUJIEw0Tr+M2OoRixUq63WcPvA3CIQHVRtwsmAmMA5fNLHFuO2ajAmcEtEYXSltiavEnFiaQ6MCOsk9t+fr1QmxmFzmhutdTrxXy+4CsWXcXcuJ9vIt/FKnpHk6FUyW1bq6uIPzBdHclXzItMV09Qc3WgR7plh2uNROk2m1fzyJnFCtYdzoTsYPOTZFT2zCBPhU8vjEyJqfBCLna9UA5Zo7WeYYvscTtGXE+uaMkiEmlXFh158b2iW0ecSJA2qNF0iYGzyVit+zhThqEvAeE4ZM8SaldquyzY6spOclspmrncIkecQNjm+wvrhOYxaOpZhZIGvxIZCWE9Qoxby12w1Xp3A2ysbQDc5rnESG7XbFK9M7Klg8zTrRfVmV6DA82xdIKaaAbbWW2U0e+1G0Yetre5wt2CfXpcMnA0Lls7MdaGVRYCfMLmFGVeXYLfibZ+YNJGrJlogewj7oKAWGbbfLei4CXieZeGDm9aZHum2/H5qhu0tXXZ2tbORwYPv2jkFpnT17mJ5oYcjAdM96mNqFMK7h+lgGbZckc5lTjnKGp/4kN/L/YzPpNmsq/aWcfA52W4lsrbwsISmzuZdLbcuPwirynYtvdL7uphOqzUqeY5KLLBy5lQU9vc38OzvqMu3OivKDRd2RUZyuVsQHQbmwMBzc5qPQXut3Qw040t58zbzpuRnl13N4GhYRarSBPWmBURbbroxPMIIWfHvERW9hxGBBG7HRg1p6TbvA9bHybKuaH55nJprG5ms8lwkjovOLVoMzoqhc0o7auggVGFqMlRY9qZGdLMIJ1t2+d2wWgyPo8ISyRZclv0QA5kR/F16m1QtNhudAymsXNr7b31XFt2QqCcxyaYjwnlaAbrriPEW21PenCYbYT0sPW7y0FUe9dkox0sXIQLOLDi4CDF7QD/x13HXEpzfjzbSXt10Uiik3VOjVxBYXPSr5m13W47vrnhVYLJzHxjeMZ1u0Wb6MY3jj5fRadhR18HnqAEQgo80jg0J/s4aKjO3A7HAA69/XWbwyhTLcjstPFdhaVd1UedfHOMuxg3xEO13eu+y7a720nJGZ8c9b4nmsiFySxCBGesmOqUot46njFs6WwGVjsULMv++PLpZbrv/Lx7/O8+Kp5u6P0/u6/4uAX49gzpfuPYNZ0vd11f/m2Lfv70UtohsOdx57RKGv95o/Ef7pt+/hcPHqbNw+PZ6/Sgq6/f7rDXpj/91dBLmDlNVZfDtypPmvuN208vVlNNf8NQfXveoH65u5QW97vdb/oeX96Nr/NppRdO1+8PIVMX8FHtPj/6zxvJYPMAQhPa1TecIr+5ZTH5+XyUMWE/Pct4+e1/AHv0fJmsJQAA -->
