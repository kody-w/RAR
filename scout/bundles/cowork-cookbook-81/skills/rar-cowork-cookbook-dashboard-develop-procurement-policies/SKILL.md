---
name: "rar-cowork-cookbook-dashboard-develop-procurement-policies"
description: "Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_procurement_policies", "rar_sha256": "a26b6c065e9fb1668996193dcfa4fb4acb191e4a10af9db1b258a117ed90a0ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_procurement_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_procurement_policies_agent.py` and in the RCI capsule.

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

Develop procurement policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 a26b6c065e9fb166…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_procurement_policies_agent.py` first:

```bash
python3 dashboard_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_procurement_policies_agent.py   # or on stdin
python3 dashboard_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_procurement_policies',
    "version": '2.0.0',
    "display_name": 'Develop procurement policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop procurement policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a685a2333c559952',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopProcurementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopProcurementPolicies'
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
    print(DashboardDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOjVpbtX+Hd/pB2K/MyT1nhiAZJIAQCCRBIcjrSzCBGMUt+/u/vIOneTJer6pU7+kPL4UwhDnvea+1zyN9enK6Ny/rl84sROAUkOlmWxEENOYUPzcuhrFPwV5m64H/IK4u2TtyuLevm5eOLHzRenVRtUhbg8W1d+p0XNJADNUEWfpoWO0kR+FBStEHteG3SB9DK3CiQ7zSxWzq1D4VlDflBH2RlBVV16XV1kAdFC1VllngJEPYJKqugaIAMYNEVcutyaIL6I1SU0AKnSMjxgMoGKoLAB5rcK9TGAdQnwRDUr8DEYHTyKgual88///LxJQHfXz7/9uJlTgN+elm82bF4mLD9ZsH2aQCQkTlFBBZXVxCnAlxXQQ3MzsFPfhBCz6sfJp8/Qv/5n+ng1FHz4+cvBfT8fHmZ/tO74m5bWzpNC0z1nMpxkyxpr68Qlw3OtYHqoO3q4h5AEOYien08+U0SCNJP070fHkpeo6D94csLCFDtTEn48vIjBOL55aXupu+vk5Tqhx9fsxJE44cfv8lpOvcceO0kDFj9+vV5/RQLFn5bmoR3rT8BqY90u8GXl++cmz4Puyc/wZMvr+cyKX54CAYp7YPCKbzghx//mVgvDrw0S5r235L780NwHDg+8Olp+I8f70H+BZo9HXqX+c/VViCtf8UTsPxN3UfoGah/Jvse/78TnYFWaN4j/g/F/aMHZj9BP/9T3/7VAx+h8MvLIshA09WOmwWfod++Gtvl/OcP/rcfP/zyOxD9/xVjlF3t3SV8zZ0iCYOm/fr15w/N/ecPv/z8oatArQVO/rWrs38k8x/F9a7nDxF8rvrhj88C/fsiLcqhgN4rHfqtrP5P/fsrZDlZ4n/7vfkMfd8v02cGTU68KX2E4LueaYCt38Xxx5ffAUwUwJvOu98GXf4f/wFtEq8umzJsIcMruxYCCW6TPJiMN+MEoFNz7+0awEjdJCCwz3Wg/qcMTxaXIfTrf3l3QAXQ+ABU+B0Ivz5B8Ot3IPj1DQR/fYVMIL2skygpnAzSue32S+FEE1ACzVUdAEjs7/DXBp8AGn2avkyQ+eu/p+DrXdZrdf31DvvJA6n0uTShVNNlwevkqR0HxdMvDzBFMAZeB9RkpQdsChOAsh9BBJoyAzDfTlFp0iTLID+pQQjK+nqXDSL3eRL266+/usC2L8UDVnHoQSUNDBa8mwN9+gScC7MkitsvReDFJfTht98/QP8X+ldP3YVPOrYA5Z95ARauDU2FQJ91k+sToQAYdvx7Xn77/RliIKYA3AeymIQT+0wPgzpNA/8t3saK+4SRFOQGIM4gxnlV1i3AaihpXyEphN7tBUqnWxOax2XTApYDPOYHhTdRlAPceY9kUbZQA4qxCa8foa4J7lp/dWvnbmIOGt5pf4U28y3gjjIDf0xm3heBh8siAeF/r4bH70BI/aGB+DcRr5A6VSZUObVTxbXz1BE6j7wAznh7HAh3AJkOX4qJK+9Vcm+TR3jAIhAZ75nST1POwUyQA0zwmzfd9zXOxHDmnenqL0XzbAGnnlLhAUoASqMu8Sdi+NuzpJq47DL/Hj9g6Z3FH1nwn1m51+DiX80K0t/PGe/8Dn3pMAQloP99M8rkFCeK+lLkzOUCWqqmfnwEe7JtUvOYz8CccDfk3ljfZoc35HkD4C9FloDKqa9/e6y8p+i55gFqwHofIIgOvfle3+Xey3cqx7qeXHK+FG9I/xEE6w5rIIOg10EvTCX4pnC6+2ZpDEI2XX9j/Xu6QQhBgYASharOBSGDQhAI1/FSYFU9teAzOaCWg6kdhzjx4j94BQHpoGSAfAgYkYCmAmxwD51aAjdB94V1mX9bnkyzVPXItQ+BaTZ4hWzQRVMlNaB1wUA0rQFR+HAXBeUBiDEw8T3CTexUD2OmAfhpoDPlosxBcX+fgefNb3V/t2UyH0h1fKcFsRwmNPaD8ZHZdzufuQLG5lOn3h/6Y7qfvkLfU9LfvhR3G98JAABANrH5d8GBQDXnzR1xJ/xqAAblwbOAQCXcifv1wb0Pcn+35fOfpv4f/trG4M6m+z9m7jMUt23VfIbhBwO+EeArQA8Y1EhSBc03Mvz07LZP33Xbp7du+4P0R7A+Q3/Nwj+IeJb2Zwh9RV6R6ZaSeMFUu88PCMj8E3/8REx3vxR68C3Tz3KYEDi7To39RkdvSwAnRXUQTYsf9NRMrDYAIr3jMcjFl+K9Gp69AuC+iCYubcrvevjOyyC3j9S90wa4VbRAtz9NdFEwbXmyyfwmePlcdFn28aVw8uDf3upMBAGqFoRk2iaB8IMxqZ1ugav3kWm6+OPW795bABT88vPUYh+habz9CL1Pqh+ht73DfU9WdGDz9PM0JU8qwVLw1/va932lG7yALVt7rSbzHxuiaTh7Ds1/NmLqrKlgJqidaOzZqpPGPwkBX6IoqP8sRLt/cbInXjStM1F40r51eQPs9MFA9BECYQTdBxoK4GQHHvizGqCnDi4d4Ep/cvdb/L65VT58+f0ehvaxq/zt5Q03njl4TpBgOWjQT83EljAoVqAQXD/KCtz7b86WTykA78BUA8Q4GOVSHkKRARu6KEUxLEuhLO57oUOELuF4LsqiAeGgiBOyvou6GMk4KEoHPos4SBACeY8S/ToNBslkGeY4HuPRKOGztEN5AY64uBegGOrTeICQLB4yTECAIL0/mgKwfLr7cG+K5fuYO4Xl6fVvLy5FgJUropG4x2cOs5ZD27Srxy5bU8HxdIAlN7EvpukKVps21LnSxAu/5q4BrQdLmV5znmGp5kp0xFbeoIvtLp6VOpueUXybJvK+uqbJYGOR1SvFOqX9Gb3qAk8T9gedUkRiWdoXW7YsNE/GpX1Q5ewgmVy9KCobRRbXmjxZEU6TMzhG6dsGoSzrVtBbPwyxTd96F3ex3RAban00z6qFZldbyv1rt+B74UpZpz7zc4Q6XVK9kqTt6DWtUTuUivCqLfcuAVfeVtzMhsoWs+UiwwwQo0PUYmsP6N4Kpb9VECosTgi5PZwI+IQd+wN5g0V6YYuGuXXiRYjaeXZyKcRhrdLJelGuaDk6wYlyWtjWxT1EObqM9wyOshfR7daGMBc2Q+lll8uaujGkehMiqqut+DTOxtPCExwELwhnoyqdbuRFw+8sRHIv+8q+aINxwXrLTYPzzmPQ29KCB4Q/lJ2eravIzo8KGazzLaOM66OBYTGHGkWGztdIPJhJZsknwP9dh97UI01i4q5WvDRHlrwdbA/+Ljd7iyMOdJYYFILhtuFZUi8HZlw4lCDcVuSRIeuKb8g1AcoiL7fnM4VEbSwOrkleFnZv9yvZkVdoZQVqGtKHuA1it9ifbK5xFww7VDurWqw2LHnbh4dmdTkldKilFDrDz9nOi7amRocN2A+FS7nzO4zHGJxP/WBTN7WChtlqECS6VTbSrovbRdwcA9KxYofe69uMjgL/UJob/nJWsOsKbQWyG/eYowVyYZ+IM4uxy3pIz7ggxArWjPJqz5xj+3Ickpu7SrfF9mDBKuZeOvmmhTdTpjfbbU2kY3sqI8nepTcHV2uqVy9Y04EhN6n7gi8qUIbaFqeWxXC8semBCcKRHM+kmTvzoTXh6CZoFQsz2hap+TQsyl7rzwO/jlvWYKtqc6VKrLlxGeF0lpB0TiFEeO6eHakqx/MSX/PUBuOLUTuJgE9K4zQsctaSD+d02fnjbFE12Q7djNHFwa4+R/bIvKI2kSSf11y2zhOzWbrNCTGWSUoh+sEXPf1UHVDfuGwYbV0SqavAmXhcmUwbbjVVSQoPKZLDSUEOa2mZEVdWFNlNWhjbG58HJLve8z6TH08NnKh2q2lCQ7shBSPbvpQjxWSVkRgkpJZh8pov0FFPCMTg922Z6fp+W6xS+KiJyMbM842/y2bITWVwYYeGXklfaHGck1hqpYXQwiYHCvkMpo1hsZr1S8UKfIUSLpieL6sBWQJAVuhRFAOnz1TayA9VbZd4qK6vw0bOs0bzxSCfOcsUnvNzPFAFSUmJ8zUpKcxZIbIzC6WtmgRF6od7ytT2OZmSrVQw2QYuD0qbIMUm7B1r3aTZ5hLORCNfCKpsgS6gLZ8rsL3mRmlUKtiwsL2EKLxL2d1uq0W7qZokoGMx6uZX7+bahr5kzdxO6BqbByfVlPc+UhTSZSFwixGu9WakPIfZY2a3UGwz0LZsYAgkXwq3o+ic52RF8DMFE4YDvZZPpVWb3YAtiFI64zQ8jvaKHdKRlkNVWIhmV0nbHXZLCb4dZpt0uJKZFDDpRfUGBk/HQjwu3ME6EhHTMhec5BzdK2q573P9qGsuQhayGw5MCB+pthgu6Ep3WSq4KMrppvPkMUMkmVvWCN8VV3fGryQusxcy4y+7+U5YJxIaz7Xqgreui+Lu/LBb+HPHag10XEYL+OJcFH+ZnPA6l7i1oW5k4sa18TGtSQB1hKeON2JXzfPWoG7RYmHF9Px08ei6wrJ4XxW+6p58htVuKMVoiaaXAi4b6xGdMUGallenR+0M68a1xvOOr8WnnIfhY8Rn7Q1f0ZEk6LszzOTMdqbgNDtji8VIMqxvL4IbuYNlueQtjGZytN0NEsGbrbFLNXdND0PU8YZSeVdnqDl8NYT20GnHeJgrpWB78HGO88dzTh3z6uqkwZ714r2xV2VcIIxsCJYlQc/nAbKgdaO1clM98FWIIVamzlnE6hexvYON/La75qth3Tv2LrHkI6nuVixxqjpvPmvP80uZotJhDAWehFcJW9uD6Id2ZQaBjGKNI17ORBRG3G53tNV1cJW1pFRnm42ZaW7jIK3LDefKP86VkYE957gea4wQD1ulOuGaumd3WqHsK7+0N4JCuBnsmW3kS4lesc6JKIhBqKTR90QDy+ZHceMvjxra3046msz4raseeRF1uE7EtVJySjKY8+W6aJLWyQtxp2yRkMHPPu/uoi5RqBUAfozSurUUc7F4E5D1uGHQch/F4TZbzk7yntf5dBDR40ny+V2b3qx+nt/UU7Bq1kFpVFYTcXRo7fHO0hshP2tnBZej5UEfFf/W9xhzuHTztuMlK79Faz+7mphBOohvDjboyHlxcARcwkJ6M2oAcsVZPpi7VMl6Om9vzpWVS5KU80t+UJPNUjicMFlfCZ1ObfR4Q7d22ZVFfcYdLjFzpK7yAl2cEbq87hPmttetZhZE5dHilnC15Kxw2y5PxTHZkzq+U8gEKUlbWaepMZfmh/XyJBw0Ls7CVp7PVks8g2lA3HEeqbVZwzgv9EjoH/HC0Yx5hZ44qU4YCk1XtRPdLnZ+uSScbPI0RfidicJ0MEhr+Rwby47bqM2MaZb6QC8ApaKjVtjXGzvLlAybFehtVY6eWVUu2wHayWNn7wCecFhqThxFeTla0nzY2X4f4Nw5Xqsx7AnXzF6e9nMkWDtsUFSoYd3MXKyGLhLWJZlkB8W3bvkqF1tphzrZSvfsfUesYnx2lPdUavV7ViaIfasD0gg71Ljp4X594XabuAcscm3WkaydPKVuzaReqvs8tCVBUUeLP/e54BRSTXA7spHz3XllWlFhSlWIpHgiFQebNGmEoeZ0wMFKnrJiqG1WR+pyOKtn+8Ad1UhoHaaWEgdw467f+d1JGS9jvM82h2WdENguRubXi3eRI6vaaDp6pCVXzEhjHgvMydYXl101Ezeb7XjRbcRcnDu06s3Cl3A7a2jNkmqNaip5U6wtplmfYiWkjCSklQpZU0mjd7FwXdH6jdj0ClovhZvo0iLb8lWztniZJsd2ryGUASfyNSfQHPF9gDJJv0xUfF0QFxAI2N0LNKFdba6lqHXlZtIoH/fRqIli6XK7o0T09uayuiQqmsZrMNDlY6q7yHpQ8bmwG7SQxcsbsjY1CjlsiTagK+q4O8/jg39cc2pN2428s3eVI6nkkA9a0nDIfC60/Jjyatpaon2rAluVedvAJI5las27tLXRusUMFpFkJdV6vsb2ASHy5Dlb8nXJuuLp5Ilof8l3awahJV9M2hxBzeXCvgY3uMgISb9s2xQM6vqh0ocM38Q8jpeDnKO6xO8oQRuNS7HJOQc5b8S9gzd8xPiEHtO3a7g5nrj9JqzzQ2sIFolR/fy0j3J+NTtsteTcpnUwFqbSm5bpXjNxMKhQmgsHsy5mnsixdCDHVq1bJywSUXXFYaNiFDNjM6wFTxGENTJDu1jPovmi3vDDoC04i9SWc1iIj75yvOw3191511p1dPX988y1OfUg3AzuUsIzKwQsIforiqZunHxKY66r9DBOKGaxqFBxvkj3+6I/qkusaIIleymNHVMOSnPJLZoKtn2SkRitzbI1zq4O+wN6MgEhJQvZCsi1Daueanib+Q4nS+0msH3dHIVVJwTCjNNJOJLoM+J2F4ZBNXpH4J6MM2A7NhAc2AUzLd6YHSHKtNcZg6toV3Xh+yeL1yVTUW8lK2p7WEzngJEOOqqyechRXuJiGV7iK3PYrk6spTSofuQEE9FXdXfc3/RN0vUxPGdLU0gWLl8vy5zBV9HhWrJHQra353ZYkdvC7PkQZQ1rgLH1FtdnBR+VbLNQe/fguDm7yZt2u9Jzd2aBIZ1Tq5jxx1sX0/m6V9Fkq5PUAYZpt4YjHjEuA9JHMDzu4N4zsUPvNzNYcranbbU2Ex1b9tGqvSQlc97qvmdcXflK7/s0T270PEQXQoQcZ/G+FyNppWm4ND8yI7yLkjOTs/vDzktvs7qcaf7poACSofEDd9u5B7PS02AR3zqp1Y9MjGz9zr3l22DfCJWauKWxt/cnWEfEWePciGO0cBK23/EzE04kl1bAJu06VwgidniXDH02PlzRq9s3Z0NUF+dKgs0qpm69WnDDSVaEEMyLee+WS7tlW5EhsWxmn8NzOGs8X5odLdxiwsGUdnroDAg2OxPUqsW31yDfJbRfo9ggnJfzy7V1RQfr+1Nw6AYX9RBF6RdXvcbP3TqnSVykQ+nUSlE97GmfWiX48TQbE9EUsGhUT2tWrM05m2wO9YqpgvhAGByHa812lbrN2CZWRnXFKtH4WcEFm+ZyLobSVgnFEdWQ5ahNygKBHmHQt1rbgiWycFao+X5cXOELsodVkoTDbgxXTdhyvjG3sn6BBZjgrrIY2a2TapifeMynTsetwMXMfrDk2ww+7mTUxiWjvzHJLEpLspFmZA3GQYnFgdu826/7NXY7lBcy94UEAdMciLWyiraG6K3rDAkJdZwp8IHzQaDSUx763ZL15itRq6OjCQt7eCyJ1RiXFLPR1jd7EW/OdXvoVm5OtCRFr7osWsj6Uc10FFPwOV36HkbLRZBTNj34F7Q8OjF+wA4xJUoFovY8hy0Dbh5RFcagCNe3dGNI3KZezXgvu1Kqfd2uRmqBrZt8djnBu2Cg1aplNiqRACgaPJhOcBc2Fa4XcDvEWISk66GoGJVoNsBnMAosrkl2W2Hr45VF25ptyyurO0sxKxM6YLaJW+8CLDsV6AzWQzhnz4eopPGOuDlURmPRUCRKPxc2u8UhuYApqhu3A65GpIiaZNKuwJQaVBazwlX4vEMWO8OMWvMw7hkYNzqJUt057QWxw2AmUVX92QwU2AZD4CCn62Qm7dX9bDGLR2fjrRCRR7I516ELayRjauXnuwuqtpySaixte70LNn0AgiqRn9uDFs/kAgu0csmuFsRMlql2HsxMn4xIjj81ccgjpYEM8c07X3qZD7LW2FDcjcdsI9rNLNpeGBGpBFer1Ipur51rMA4UAZ7H+MBSDMUZFIA/m6gRWI3Zc4oUNoNJATn6iN1u13TbS+a5dCNboOx4TrajIrlWiAoRumCT0bvSJOXOdvxt1h04j+A7rzZLmttneiV1u+F8pMJ2yfCev69Oa6JC8x6LR3Yu4qrnj4ZWYQ3idf2RXMGDsIkvl2wwUo7jfvrp5ePLdCr9PFv+iy+Zp3O+/7HjxsfJ4Nv7pvuxcuD4n++6Pv9Vw375+FJ7CTDrcbzaZF30PIb8u8PVT//eu4pJxvXxDnd6RTa2b4fyrRNN/yTpJSn8rmnr69emzLr7Ie/HF7drpn8Z0Xx9Hma/3B3Mq/vJ+Jvab2elbfm1cqaY3t9g5oGfOG3wvIyeB87gwSvIVeI1X3GK/BrU1eTq883HdEI7vfp4+f3/AR+3NisMJgAA -->
