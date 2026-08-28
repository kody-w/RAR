---
name: "rar-cowork-cookbook-adaptive-card-manage-supplier-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_supplier_performance", "rar_sha256": "ec7446aa03323249f08591cfb48548122d69971f6be9443d1692d9c73473c994", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_supplier_performance_agent.py` and in the RCI capsule.

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

Manage supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 ec7446aa03323249…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_supplier_performance_agent.py` first:

```bash
python3 adaptive_card_manage_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_supplier_performance_agent.py   # or on stdin
python3 adaptive_card_manage_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_supplier_performance',
    "version": '2.0.1',
    "display_name": 'Manage supplier performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage supplier performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4eaf49ac79a364f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-supplier-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-manage-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageSupplierPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageSupplierPerformance'
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
    print(AdaptiveCardManageSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejWJLlX9F4f8jIJsIlFgmIOnXOAEIgxCIEAkRGngh2EPsmCbLzv89DkntkdFbVVPaZD6NYXMDDlmtm1+yB//bi9F1cNi+fX7TAKWack2VJHDQzp/BnTHktmxT8KFMX/Jt5ZdE1idt3ZdO+fHzxg9ZrkqpLygLcvm9Kv/eCdubMmqBvHTcLZpTvgMuXYMY4jT8TNEWetYVTtXHZzcpwljuFEwWztq+qLAE6q6AJywac9cDJzun6dgaOZ0HuBr6fFNEsKWa+08ZuCcS1H8EFJ8nAT7BGD5y8fQVGBTcnr7Kgffn8y68fXxLw/eXzby9e5rTg1MubQZM90l279lS+/64bSMmcIgLLqwFgU4Djp2XglB+Eb3Z+aIMs/Dj7z/9Mr04TtT9//lLMnp8vL9OfQ1/MujiYdaXTdoE/85zKcZMs6YbXGZVdnaEFUHV9U0ygtQDaInp93PldUlnN/j5d+/BQ8hoF3YcvLyUwwZmA//Ly8+T+l5emn76/TlKqDz+/ZuU1aD78/F1O27vnwOsmYcDq16/P46dYsPD70iS8a/07kPoIsRt8efmDc9PnYffkJ7jz5fVcJsWHh+CqKS9BMeH44ed/JtaLAy/Nkrb7t+T+8hAcB44PfHoa/vPHO8i/zqCnQ+8y/7naCoT1r3gClr+p+zh7AvXPZN/x/2+is6QA9fCG+D8U949ugP4+++Wf+vavbvg4C7+8rIMMJHgz1d/n2W9ftT3L/PKT//3kT7/+DkT/X8VoZd94dwlfQVEkYdB2X7/+8lN7P/3Tr7/81Fcg10DVfe2b7B/J/Ee43vX8gOBz1Ycf7wX6j0ValNdi9p7ps9/K6n81v7/ODCdL/O/n28+zP9bL9IFmkxNvSh8Q/KFmWmDrH3D8+eV3QBQF8Kb37pdBlf/Hf8ykxGvKtgy7meaVfTcDAe6SPJiM1+OknYG/U203AcC1TSa2e6wD+T9FeLIYUNy3/+3dSfST9yTRufOkoK8e4KCvDwr8+kaBX/9Agd9eZzpQUDZJlBRONjtQ+/2XaXXRTcqrJmiD5gJoxR264BO469P0ZeLIb/+2jq93ca/V8O1O+MmDrw7MduKqts+C18lfMw6Kp3ce6BHBLfB6oCkrPWBWmAC2/QhwaMsMMH03YdOmSZbN/KQBQJTNcJcN8Ps8Cfv27ZsLOPxL8SBXdPZoIu0cLHg3Z/bpE/AvzJIo7r4UgReXs59++/2n2X/N/tVdd+GTjj1g+2d0gIX3vgOqrc/BMhA4EGpAJffo/Pb7E2UgpgAdCMQyCZPgcTPI1jTw3yDXeOoTslzN3ACAB2DOq7Lp7k2pe51tw9m7vUDpdGni9Lhsu5kfVEHhB4U3AKkOcOcdyQK0wRakZBsOH2d9G9y1fnMb525iDsre6b7NJGYPOkiZgf8mM++LwM1lkQD43xPicR4IaX5qZ/SbiNeZPOXnrHIap4ob56kjdB5xAZ3j7XYg3JkVwfVLMfXMYILqXiwPeMAigIz3DOmnKeZgGshBDvntm+77Gmfqc/q93zVfivZZCE4zhcIDjQEojfrEn3Lvb8+UAtNAn/l3/IClk6RnFPxnVO45KP2LWUF7zAo/ThtfemQBY7P/H8aSyX6K4w4sR+nsesbK+uH0wHWaqCb8H0MYGAzuku819H1YeKOaN8b9UmQJSJJm+Ntj5T0azzUPFusbAN6BOtzlg1QATkxy75k6ZV7TTDnufCneqP0jgOfOYyBYoKxB2k/Z9qZwuvpmaQwcnY6/t/l7ZAGOIBdANs6q3s1ApoRB4LuOlwKrmqnanuEAaRtMGF/jxIt/8GoGpIPsAPJnwIgE1A+g/zt0cgncBDCHTZl/X55Mw1P1iK4/AyNr8DozQcFMSdOCKgUT0LQGoPDTXdQsDwDGwMR3hNvYqR7GTFPu00BnikWZgzz+YwSeF7+n+N2WyXwgFbBtB7C8TtzrB7dHZN/tfMYKGJtPRXm/6cdwP32d/bEH/e1Lcbfxne5BrWf35P0OzgzUWN7eyXWiqhbQTR48Ewhkwr1Tvz6a7aObv9vy+U+j/Ye/Nv3f2+fxx8h9nsVdV7Wf5/NHy3vreK+AKOYgR5IqaN+736epM316VNqnt0r79IdK+0HBA6/Ps79m5A8intn9eQa/Ll4X0yUx8YIpfZ8fgAnziT59wqarX4pD8D3Yz4yY+DYbQLt9bz5vS0AHipogmhY/mlE79bAraJt39gXh+FK8J8SzXAC5F9HUOdvyD2V878IgvI/ovTcJcKnogG5/muKiYNroZJP5bfDyueiz7ONL4eTBX9jgTA0BpC4AZdoegTIC0HdJcD96H5Smgx83efcCA8zgl5+nOvs4m4baj7P3+fTj7G3HcN+LFT3YMv0yzcaTSrAU/Hhf+76DdIMXsFXrhmpy4LENmkay56j8ZyOm8gIWA1JvJ1ve6nXS+Cch4EsUBc2fhSj3L072JA3A61PLTrq3Um+BnT4YgACdX6YSBFUFsOvBDX9WA/Q0Qd2D3uhP7n7H77tb5cOX3+8wdI+95G8vb+TxjMFzbgTLQZV+aqfuOAfpChSC40digWv/84nyKQjwHhhkgKTAwzFs5TgLFEVQBCPDBbEkYS90MWKJETCC+CuSxOFw5QYkhqE+vCIRn/RwFMNRjyQxIO+Rp1+nWSCZjAsWYYCSMOL56ApZLjESxhGH9B0Mdxx/QRD4Ag990Bq+35oC0nx6/PBwgvN9uJ2QeTr+24u7wsBKHmu31OPDzEnDWaGie4staFyFp+2Z3AqaXgoctiqdTtmwBoKeUv+8UpEUZrEVJZzSuKdNOhI17rTI22y9pIpR2KOKVVBn0b9U/s69KSLLFmsYJ7MBIpaLLBqo0yWglta1z1crcVsxsb31amPXeIR+1fCajw0HdTSi3mkytvOJs5Bd5uiwQzujbg5KzDle5ojmXsJZVSnDDQmR9ropYn9VJnVqIOPqesZdHOO9vGs22+Myv+TezR4ux9zImKJCz7R9sudbS6qgjcOXJC+0SFjYBKmILQSdTO8iEuSckYvs0NDs0ra2OwKQfS3vzACR0Lw8y8cOu5qKvdD3hJFymFgcDLVblCnKCwO50Hd4oikCpUdHxjf4Y3UsbMjL8aO3LM707mAayQa30s3NPFbD7RrxadLH9ZB53iDvRMNSpMrwTqiZ5T1aNq4/Rou9hi/Myk0P/XzD7Q4Sx+9Zkg82OJ8fx5NWRotlm8LudstxmO0tTwIR4P1hcGyUj1x5eVoupFsU7ea3MSfkTLxZCg0FvdYYXWzx2jFWkSop3GSzY/F9KzdwbC+XALxMQYXt/nzGFglYeHX1quZ3LXoRGbPei04uucIcacQdycNKA9vMGO1HWG7oTSr7+phtDnP/2nfLXYeftLWL9MGa0pgD7bZ7bb0i8K3hup7Ed1BbbJGt00ZLXybFvWRzTcMajuDVF2HhR+cLabcl7jJLtU0aqBzYkHJOtzC/EY5K652xrJNCy1Ae2pKyGOl7RJfbbcDOS5Qt1Yi92OqAZvtyq1zm9pk0Gdep68X2styvWZHFvV6XD8i5HNTYp0e8nKbXm2jjTm43q9yuEGfV12iT1df1qNxqYpMRpUByZ2zHQ7zcjdtDtiv69fx2Uy6XVUxm5ws9+MnosmKUppCF81iM6pqWi1oLkZqkWyt412p6NKS+ELdHmcHGI1LpjJSfD1fb3rSBiJkRteuUztjdVlyJ1FSM8KmCyRssM8KTUlr6cDYZTl2Ph4xPV6O2Q9YczpFsTFVwm3JrOoqOmYjVtmQGCnv1dWjECxPjUGxFthF3gtQUPm7LamfvJA1yYrZwEqnQ3EKHRYTTx1VtQYGWwWlIh8tCx44F3ZLXS2PjIT+n5DCQhV6yZZOvHDm05hx86+tGOjHJIRfbbY0MeYqtika4WVwXteTpsKCuPHxRpT2yEpMCr2+nNEA4TdjFRyNkvb3NrrbbzU6I99q8WXKFXiCAaQ5pWe/3l3k8ClKVXPiDKdh0WKMCv4Tq1nFukGVJzHWXMOIi5WQX6bxxvFG1gVlep63YcyqjGmEf9oIaUQfiqnexjfEWvOnHXOltcysKBZPw8Mby40Vq70kE14ydYNYZdA52NGvom8RsV7gHGbC912UujoVhEC01DhsYMUXHOB/gXCIPohehxoarz9JqmWXxDqpqwzMcttlBcspxc3HkbPo4N7AwK8xTV0PegjvUlnFsSJ2D0B1kRK7gLZhBPEtaSNF5j/VEOOx82Owc0DpOAbwW+zGcn7bXec8SvBndTj52HNQc7i6BdYNaGl8kG4vI6PZYHGpa6BkldLXrJr3FbTWe0PnaWVKXahW2qxtxks+8UTjnoy1z4nIZxKWxgwq7N/ewvOyyNppfqQtTHimvlHX7IhQ+ze/X2NWxsky6Mmy1t7lxn2TwgnRcI4eEJPec01qT66wX5NEs86FC4s3chIiBiTXXS/qWGFU13iAXJUkSRYE3nrpI/RyKq1IGjdYviI4GHc0GbZ5dFoU1x+d7vV16R7tW9fMxa5JGvITV0lgY+0EeOgPRCYXGd8J6xGECEiSulGGU6nqeIWr1hu0ufDEXUpwkBn0+xy58rS290s149bojbcg5DTuVW0QxVDUcLx+Xy0p1qMoYehumC8ptuH1LZzw7PwkbgqtpqxXMskURvE5K1k6Do+9H1u4oyE5EqLdyz0iLLqf3PQ0ZWmasdB5lNheoPZ73DMQZfJw1wqWNPNoOuzA+jWy071Bi20mDHoCD2AhO+yzQtYNga7twS570kT0XbHOEFrvj2HVnpNwB/jTiDAOh6+belurXYVg5IN18CWToabetA/TU0R4CNmeJN78GG39tHnxcMFD/7PbJwtOjhHW4Q6XEWmZmhb3H15Kbh23kH7W1ePXDU88fu5Lz21Q73s5n7cpL/jaz4COUjcQQXSXMYA1osfXzsqzXNCbkbR0MsHxsVVV0mICGRa/0S+90RJS9e9rczi3bC6hGs2Zya1VCD83FTtfFOE/yU14f6kiTIWZU9Vw+RmVAYIPVh8Ktz9ZQclnUrJBjm9QybHh3C5wAkkb7oAoSU9t9WUj6SoE521U3B3KTUKtQkHkiGSCY5aIuYL1cDNTcPBQb1B6cOmtpaB8q/dayhFthlbcM4kwRUYVdZW5Oe8BgfZccDxieBmfWVvtxU6+b7QrzF5GQkh2THSw8j1f+QlAOgaBsy3x7UdnjGOnFolZB7VTHTIiV86A6ieXS5ZVJAXnbG7ZQqySxHZtpWYaF50i5Xh61TgwXUSpQmRrMq2KOWDp9wl3EkhZtm+k7jdLUbqU0J7mCxeYI24O82PvzPZ4tjKvHWRsxojvVz0FZetsiXUmoBAbOE69AV3LXNVmwzDtU0m/e2THWTYi3qLzmpdGLtBTnDPxGUNvMZJmMQrhgVDhn4Np1LO2zumQHjO4xLVkFvIFo2f6QC34U0Ktkvr7tO7PeFgSYT5ZqdtlwQlRizRHjKWTeWtlGLQKo99C8h9g4lYnq2Mm+7BWYoF25zRa9IvP0ROFpqqupL1Xrw5KDSLW0NtlBWBepBJvFoWUFJ6fdkj5XXWRlKduMKZqs80aD9UCaI9rYUmVTJG0dmp538nTxluWXdUxwqHSrQnhxUHd9WxblnpVIj1AjRWc3N+HUh+nWp7pVcUpKmNPXqR8oA4h4wCZh7HJGqkLHXQid+TXB9QdCKwOfM4KVhwtMZBXtSrlJN6M+ygtHB/oWO6U9oF3UNMGKdxn3KGJaqGsx0UorRiQg98rZ13yZISOt2sjKNglaOBdceu7L5ZxNs81tlEsHt/S57e5ZV9GVmymEps8d7dXSGUzKh9ODiSt2wi4qemQXaLYGnMO0qMbCa/Sww1ZqKZfIIt4x9qq+7nGGVwfAndoJbQU9dDoo2DqkeVsMFb9JSsduc75bmW1NHdTKEYTlkF+VNqslctS8itIM0VdjJzfjM5QYxzihA3c7wvvaqXvfDNYKetOZ8nCVkWMOZbdk6Zy36/ZGIBIyYFLlG1Lp4xWkropEh7sW9PEqJ6053VzV89HSWSQzIzBrJp1iQGuxOKowWyaqdoZro9iACl6srYbDpFruT2v6NA7nRCwSSHWP9PEGdUYAXzLV8mui6pw1Y1FgPto4G1wSvNtZFS3L091xHTv1NiREqluOKpnv1/3pvNEdvO5Y9FCtaiKxORuqTBpLcnpMFliQQYA66RWjS/RVpeeUuWFYaU6nJ39t5yy1VEdcMUTc9OWGdPItrFbogUEPpC7uGV2TMOXqLtFoh6Ux298oN26Xi80a9jlWOxmpnmoKM6RtcCTbE6vNQd9sFcQsmvTguTJ6OAQK0yzrPGBSMGb2R9UGVGrZ6Bnu+grvlpiahCkVyiKuWjvKd6Xel7tbdw32KBiViSDr+Ut/gV2UEGHoesVdIrB2G9id1z2UQNZ1aZIavqevYHLB9Hp9psRNbXUoL8G4U9OL2omlfruvLpHKnMm6wmlrb6mXw2nsdNno9E0MhqWTkzopa+81c0jmBHpdwxnf2PK27Am0wE6LfQe5UE5FAWUS+1AKXIrGua4OiF1QdXN3e122PhgVbxCoCd20nC3CxwTfNuLtwuI7DlLUEmdMfHRhqI1XMr8O57jvhwTtpztC3uEWTqrzsctER+zzvQfjwSlHteK2LbZWtMclupKpJBAHzVQDc8PlEqWY/akYaRpMAutKHoeGOWBqt80MPhUI0Nn5jYxFClVWRWultehLTT/ubsZqS7k3OPfBZovg13xudzRLHI5829towSvbPW8LMakSYH/SQAnYkdp2cYUpBc8uNrFZNMTmisJWZJDpkb8tz4SKDtAKp5u0yUR/ydUkcEc4nxWEv3AE2q6ZNIKMZMVgmjIuc/00IvtjiA/41ZyTFwzhFPayo1xcTQkKttL1IEP87SqHZpgpCJbgSsXjJ2ZMQKpay2LncmJXNqPnr2qDGDZXKHV8DD4L86JoxYqMcozS5rLWW9FBBEe4GZkSGmxYMpY0ptoY7WEg7TBt9qPMXFXWLhfzIIYGBREsfbcKlOWCxSUZuyZYJtKeTFIm2i6IFe0dxDGxz/BN7pX2Cnn0rTF3RQzqUqmUy+oWXvSyJeaMJKrzIw1tK40jUas4dZRn8hsmZ0Z6txAddJNFWMuxS502ziEeRCHvuUS8LcKb6Qm86p50XGlbuRVQ23Klomf7sKg2cmKchZPYdAJijWXbBvQQ6RUceAe8UdSltVqdLyXUB33HoYHADLyy5E4RtgPDYLAssd0tpmQoRKir2ZSiTlYy4aH9zWFEE411queYqyvvlMFDmLHXPRnPYN3qRXgeJJHDK4Vt0uWqC8qzd1mvNEAj66gQcU+lybobfI7OKDI+E1V+JBzh6PMl6h2HZtUUnVxw5XKP3NA+peZQ3RW8Z5L2fGzpBLFtElFSmgyX47yxt+s5gA/JVKJdQ/maCxn63DTuylqWN3lIFzd55/d7ZHHzl/Ve58/6ed5frfmSPMHXWiHwWELayiFriV6d8SjWUwrG6uZQ4oTlbUZPsbsjdDofFqOBt5tTTN5C7CpLsA+5PQTteT64Lg7Esp5TerborFxDw53v5/gBDOMIjFGLZZEadXcuqMNCcQFZ0eVgsqVm94mloAqvZum4DPuLUAUQigZ1hp9wck87ImXyt7OC86hsVoZ/pjFHWa8qQBvMkoyX6fokbRYM61l5ZI+g9SS7nqy6gYWpsRqPjLeENmuXTDCyVvKuUazIPOCRsrtE+dzO26sF4cWxuHIAJVBCotNsWKFr+9PKgkYGDeVkfSjmvLFYRlKk8/N1WfhcOmQdUmEpkTGyOQ8YVyfBBLVeMwVyxTwaSTYRYgHaim5pofpqSyvokDFgF6NKJZFsRn2ETxcBItETvzUhMOV35xyh+RMKUYSpOyUD71SKevn4Mj2Wfj5c/uuvlafHfP/PnjY+Hgy+vXa6P1gOHP/zXdfn/4Ftv358abwEWPZ4xtpmffR8EPnfnrB++rffWkxihse72+l92a17ezzfOdH0K0kvSeH3bdcMX9sy6+8Pez++uH07/V5E+/X5UPvl7mZeTU/If3Dr+0PTrvxaORO6STG9BAr8xOmC52H0fPj88cUfQOASr/2KrpZfg6aaPH6+BwGOIq+LV/jl9/8Dl7CCQgImAAA= -->
