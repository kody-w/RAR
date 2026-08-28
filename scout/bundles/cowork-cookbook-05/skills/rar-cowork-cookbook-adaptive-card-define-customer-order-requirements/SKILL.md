---
name: "rar-cowork-cookbook-adaptive-card-define-customer-order-requirements"
description: "Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_order_requirements", "rar_sha256": "9c79ea68666e24f1b2c30c3a0e6a4d0b2aed8908e0c8161bc8afab115459a86c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_customer_order_requirements`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_customer_order_requirements_agent.py` and in the RCI capsule.

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

Define customer order requirements Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 9c79ea68666e24f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_order_requirements_agent.py` first:

```bash
python3 adaptive_card_define_customer_order_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_customer_order_requirements_agent.py   # or on stdin
python3 adaptive_card_define_customer_order_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer order requirements Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_customer_order_requirements',
    "version": '2.0.0',
    "display_name": 'Define customer order requirements Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-customer-order-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49c9f3e8ea2f0a07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-customer-order-requirements'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-customer-order-requirements', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineCustomerOrderRequirements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineCustomerOrderRequirements'
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
    print(AdaptiveCardDefineCustomerOrderRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166beiyJbvv2Kf/lBZTeaRQaa86671AAcGBWUQsbJWFjPIPIlQXf97B+o5mdl1b3dXv/fheQaFiNjz/u0dgb+/2F0bFfXL5xfNt/PZxk7TOPLrmZ17M67oizoBb0XigL+ZW+RtHTtdW9TNy8cXz2/cOi7buMjB8n1deJ3rNzN7VvtdYzupP2M8Gwxf/Rln195M1BR51uR22URFOyuCmecHce7P3K5piwzwLGoP/K/9qotrP/Pztpk1rd12zSwo6pmfOb7nxXk4i/OZZzeRUwCqzUcwYMcpeAdzdN/Omlcgm3+zszL1m5fPv/z68SUGn18+//7ipnYDbr28yTWJtbwLwT1lUCYR1O8kALRSOw/BonIAhsrBdenXQJ4M3AIKzJ5XHxo/DT7O/u3fkt6uw+bnz1/y2fP15WX6Ubt81kb+rC3spvW9mWuXthOncTu8zpi0t4cGaN52dT5ZsAF2zsPXx8pvlIpy9vdp7MODyWvotx++vBRABHvywpeXnycjfHmpu+nz60Sl/PDza1r0fv3h5290ms65+G47EQNSv359Xj/JgonfpsbBnevfAdWHvx3/y8t3yk2vh9yTnmDly+uliPMPD8JlXVz93M5d/8PP/4ysG/luksZN+z+i+8uDcOTbwFEfnoL//PFu5F9n0FOhd5r/nG0J3PpXNAHT39h9nD0N9c9o3+3/n0inIMqad4v/Q3L/aAH099kv/1S3/2rBx1nw5WXppyDM6ykZP89+/6rtV9wvP3nfbv706x+A9H9LRiu62r1T+JrZeRz4Tfv16y8/NffbP/36y09dCWIN5N7Xrk7/Ec1/ZNc7nx8s+Jz14ce1gL+RJ3nR57P3SJ/9XpT/Uv/xOjvaaex9u998nn2fL9MLmk1KvDF9mOC7nGmArN/Z8eeXPwBc5ECbzr0Pgyz/13+d7WK3LpoiaGeaW3TtDDi4jTN/El6P4mYGfqfcrn1g1yaeoO8xD8T/5OFJYoB3v/0f946on9wnos7tJxB9dQESfX3g4dc3PPx6x8Ov3+Phb68zHfAp6jiMczudqcx+/yW3QzA2yVDWfuPXV4AuztD6nwAufZo+TID5219l9fVO9bUcfrvXgviBXionTMjVdKn/OmlvRn7+1NUF5cO/+W4HGKaFC6QLYoDAH4FVmiIFRaCdLNUkcZrOPMDFBWVkuNMG1vw8Efvtt98cgOtf8gfUYrNHfWnmYMK7OLNPn4CaQRqHUfsl992omP30+x8/zf599l+tuhOfeOxBBXj6Ckh4L0kg97pHtZkcD4Dl7qvf/3gaG5DJQVkCno2D2H8sBrGb+N6b5TWe+YTixMzxgcWBtbOyqNt7oWpfZ0Iwe5cXMJ2GJoSPiqYFBbD0c8/P3QFQtYE675bMQYVsQIA2wfBx1jX+netvTm3fRcwACNjtb7Mdtwf1pEjBv0nM+ySwuMhjYP73uHjcB0Tqn5oZ+0bidSZP0Tor7douo9p+8gjsh19AHXlbDojbs9zvv+RTHb1Hxz11HuYBk4Bl3KdLP00+B41CBnDCa9543+fYU9XT79Wv/pI3z7Sw68kVLigTgGnYxd5ULP72DCnQKHSpd7cfkHSi9PSC9/TKPQaX/30boT3aiB/7kS8dCiOL2f9HjcukDbPZqKsNo6+Ws5Wsq9bDylPrNXnj0a2BpuFO+Z5R3xqJNxh6Q+MveRqDkKmHvz1m3n3znPNAuK4GplQZ9U4fBAbQYqJ7j9spDut6inj7S/4G+x+Ble4YB1wHkhwkwRR7bwyn0TdJI6DodP2tBbj7GZgTRAaIzVnZOSmIm8D3Pcd2EyBVPeXe0ysgiP3J1H0Uu9EPWs0AdRArgP4MCBEDW4PScDedXAA1gZmDusi+TY+nxqp8ONmbgd7Wf52ZIH2mEGpAzoLuaJoDrPDTndQs84GNgYjvFm4iu3wIM7XDTwHtyRdFBqL6ew88B78F/F2WSXxAFUBwC2zZT4Ds+beHZ9/lfPoKCJtNKXpf9KO7n7rOvq9Pf/uS32V8rwEg89N7DH8zzgxkXNbcoXYCrgaAT+Y/AwhEwr2Kvz4K8aPSv8vy+U97gA9/bZtwL63Gj577PIvatmw+z+ePcvhWDV8BbMxBjMSl37xXxk9Tufr0SLhPbwn36Z5wn75PuB/4PMz2efbXZP2BxDPIP8+QV/gVnoa2setPUfx8AdNwn1jr02Ia/ZKr/jefPwNjAuF0AKX4vSK9TQFlKaz9cJr8qFDNVNh6UEvvkAy88iV/j4tn1gDEz8OpnDbFd9l8L80T3Dz89lY5wFDeAt7e1OiF/rQjSifxG//lc96l6ceX3M78v7wTmmoFiGNgmmk3BXIKdFFt7N+v3juq6eLHreE92wBMeMXnKek+zqbu9+PsvZH9OHvbWty3bnkH9la/TE30xBJMBW/vc9/3nY7/AnZ27VBOajz2S1Pv9uyp/yzElGtAYgD0zSTLW/JOHP9EBHwIQ7/+MxHl/sFOnwgCQH6q5nH7lvcNkNMDvRHA9uuUjyDFAHJ2YMGf2QA+zwD2JnW/2e+bWsVDlz/uZmgfm87fX96Q5OmDZ4MJpoOU/dRMhXMOghYwBNeP8AJj/9et55MewELQ6gCCtEvSvk1QBEH46CJAHNTFYBezYZ+wFx7soLbvUTRM+bBLIQTiuJQd2A6C4AuctinCBfQeQft16hbiSUbUtl3KJZGFR5M24foY7GCuj6CIR2I+jNNYQFH+ApjrfWkCgPSp+EPRyarvXfBkoKf+v784xALM5BeNwDxe3Jw+2gQmOO3tBI2Ex8gjLYi+rrmelBR2q6zXKYpZyVUgc/nM6gpbN9ukiM14NHsJz482Z+0TLdgl8wPJ7M+SWZA6YYyXxEQq98T2ZOeSJnNmd3zRHC/CaSulu8o5czviqM+l6zqDy6pRj7jtRevBvUqNqBhrwqTW3WAQuE5D192VFI+mfTaEfgzRo+DwmRod5v4+xg9t5qaEddGqs1nz8Nx1zx59k2zNRhsj0jMbOo/rXBq1s7nYVJmpMEM/h0JfwxZIoV1gN9dLyMt1mPbzEcnOA3jHqKBpXYeX9GGV9ueaqmS43rqmQ6ZqVJmUsOV3lZxDErxyj6ZlFHtPEpUbntfYwG46ca8PIscVSb3VhOyUi5Bv7i2PQ2vpeHZjPzW5ptW0+rK1qBT06kOcNGAUTrQyz4yqa7atMZ42sNl0eHjegkDij60b4XkYWuJic9zs5vrqjJ9czdLbSIgvp3RgzznTn5LLcWQanR/GxM2ysqeWZxK+YGHPaXJkYf6hRw/Nem4u3fToOGkU23a6WiDEuRHIg4CeXOd0ET3cctZCusPApgq54ZaK9rUlRzASXQwwHonplhiKfDNc6Xowcq3V47Zm/H3k+9VKkHL2UvkULu0cc4nsb8drPhgWRN56IdaWQn68EuTVsK3aG9fUreMLtHH4m3ysHX8cBaeRkLXJ5TBScpFrnKGzF24Ev76wQN/UWKzqnWNFAWZxWzEsqaryq9o4WsPc4YXI3xH+IgxFCMmUw00cOtG6jdJWXp0uUANBNet1xtlcmRSWxvJwhk54XJBqrwqHNsLbMUfDXk0p3LUbrELE+oyIJWIQLXnZ7q0wR61yDSv7ijmR8r4/BCEj0XNJXS8Z6EL1A5Q3GUTnOSrfPA639XlrJYrG8VaLjZxqryvzjAwH9URAiMnKtzOLZH0m8d3OGpbx8XoRy4KSM9XhY2hdhYKam1raHiJ8rIPe9/DLRUwaUTspy2pNBgd7HyIHbuWpR8mr19v1xbs0sXiQdIdl894S1lkUrEehGCPKYREJywOu65UraUNmaipEedMTXYnPt7FoCzw5HRWEPynocg+fY9NfUllPB7KRxdtLR4QQxbsmWdieu3YwdQ4HaSDah8iPRHngb2ZMXyG1Dmn0ZN0O6iBFWHJcn9VDtS/R3j32jra5KRGcrK8Hag5udAYt5fl+SydcuTEMO4tl3KhYHTWUo7FLjNqf1/iG2TcXOEIoUd3pQeCs80GJ4jmvabjNBBUGX3K9JjdJEiDyTSpZVbJOR34EbdNJoKpDRiUGnFBZCzAsWbQqV2R8xtHJfh8SVGkr7k0exVumqgu4gAo/aJQVKQRB0IlGkSRSTq/omHM8aZX6Dn/S0gHaO9tzLI/DuHVCVp2jaAUUuS3ycXMWSuUg1bvcSzPPHbQhhcq26rRymaMUetQ21DBSJ86A8X6/P3XRVvcaTFVHEYm6Ol3wcVA3hH84MF4h3WC10LFU4buyLSCQw5XsYyQsl1Qi5+Q5iOnaX4buGdMoNMvpdRxfhIp0HdCizivW84XoOJcOJbKFPSf2T8uuq057SdwyVIsWsMRcVBerpes18xcq55CLVHIM4Oq5RbQ7rnauC1PY3Yy8g814ZRm8YMIMq2smoR+u9LqxL2qEBkvteEgKzd1InIQvkeUhLJjVZtk6RsfoixJdIwK51hg/Lq3EPY56xnaBGFXidn0841mYFWcb09Y7yvXOBMmWQtWueqxC6erUztNypPJRWe9vOa95wfza0Mq4vqnZjV3iuppsT5g/v2iXmzRPndSur/zC4A6Jtx2zC0kNNkdhJ8NFB8pfc5sgwI9UG5S7+erUR0TDz3eb0z5dUmXFlAPv5CgtbdhNcSJXkbjMMp/a9YJUrYf2LIqpzcPbwKkd11ErqGPiYXkMa5jhdo7UxrVYqWsRy9YnYZmkiW4ivuXYe2lvk5uC8ixRkBbGqnBx9ThHzpVpd0RMkZ6shstyL1sHT3R5f1Pxyv5cWBdBseeCrpyQZmUYR94D0LkML2Jnu6VnHZXCOeIyQFcK28dpeOqDU0wySMOFeFJmGzOlFcxJLLqFUDZEYwK++dWFtT3FmgciOnKw2w4E4wyCm0vSNnUcL9EczIfSbujwSDByRqZz0udG9uyPnFhvZBkTFrejWF/juib2pLCMcOakGYdRtkBEptIyZMRgV/naBpNMSzp47H6VwXXBe6Yq2aWKac6FK+RIC2PhxAlmnfExvnAqbThTDWyOCX4IrI3ahXwIUGmEh5K4XdYe3lx5KmEZYMXhsNGWZ/WYpUa9xpcWmZGcyKaHKgviLbyCRlnNjjC7cu1Fv9wPlrA8tHmrss32FAn+ZZtv6JUM0WOh56smvIIepYzX6AASh9qd/XXe0ymsVcfYXM7V9pxb4SpW8E1x21jb7uabaEMvOohZxzYWeUIKLSw/9zg9OcVOLInJuFjbu8UKp4uUu+mYvokVGfcPLmzilqwYUu8SscaIiurxq3jTr9l+ZejidQhaXYMjKuashNv1PN2Sc4sWThcvtzxQuPuUKRAuxq83mmRlpd3ZVRUPykUJlyOMefT+dO1qFmkrOCm2zbLp3fk1Wu94NSOzPHdWBJbxNYK4FeYiHd7a2+Qsiz597UYP3rmjF7PSslVPLd/bkXLoD/0G6QHm8z6nrBcmD/VH7mRFrWVdKml7RP1cXhFyd7C4WmqPgUoznVmxhd0lZzjamtLOYO2kNnqe7+aNU64POWiSXSREgtjqOyapTnbtePuQF8Ld6nCNWmhr8aDwisdOPBzjzTXe18buuFgYhwNJ6GuzPJ84jpdDU1vZRG2siFIWoVUGqclAYERQgQ7y3DHzdFT9fJ9vVo1ipYt+ga0HannZuChtL4Sm1HfG2PNDZlJpoaG6sL6Jh45OikMQrRGa0lTkcF5qaZKXSXuT43zdUkYxVxWhZzhdQpBIyk69Aulw7mW6mSH44chlUaLSxbhWu6ge4FygXXzEbzIw3A1AzzXB6yqI+YqwDJdTUhfyj/iCLnZRvR8TFsYtml51rt2fb51Y+VIAi4iwP7ZX/uQTgt1dbiKZtJo0pNi5w8/ZPFttcSQ2IoX1t4qoxStpn8qWoRiNLvLHLXmQO1AnyhhFDITbIJg7nnut4m5bshr5Xbo951qNz9kGPfPAGq4r1TUlsFffXqfaKmb3qro/GIhei9K14Vajwxy1AwYLRzmlbF1IM0HdSzy7rUyjpB3HHDfkCOla4catBJyskuF5U4sXoed9oY9xduvTcOriEaZVzkU7im21uIXJiJGKQ2mXXUXolJutIdjjMO8M4ipa3uBFez4IK6aE7BTUYrXUGUe4Zbx4IVGyB/2tYI04zYd7npHRK32VUL211wraSrod9+vecPLSiDpyiSk7ZIPRc9DUjUwUMsJW6TUlgfcsqIhZMxpZR5LsGiWRyDV3tTJPLnKVKGwcj9q+dQrNP6Kgp1RCS8EYU+T4Hcrmlt+Na2sdR9ngVqdbq8lX2tkIx5MIWuJrAeEpFok3vVhGuon2rL6rQD7a2A11ieMSpzcr2zolp9yS4SFpjB3UaHBK63LV23iAtLFciB15Gmsk2zPpwd2Oy1hy2y12lKk+5DaVWRfePoPIHLrUxySvDvyoM7BMMrw57vMTqEju6bLEWWTPl6crSbZesCd2FYWf6TLg05H1NGq3nXfbAeIVLMMcayPnjnPZH5OMVZcmvcHXWe4VJWbAFTEvwy6BWOAMP/VxjthaLYLuQEwdeQPWLasoC80zuSJvJZgN5nJypIau0JxCtnH5hPaLEsIC2FO2y7TjMMiHti7aj6jinGjLmuskBIMdIEEoKHvZD1lKN1XbBMtDdkY9D0WYY8wFoM+gE96/If3cLPA1T9RziLrIELOFB3KpQ8g4X+lDwF49l57XBNGraqoUqdLsLclTuSUc630rRhemTE5exYiYHKV7dBNrgsCe63lmGsc1kxCOoljRwHmhb+jd0pIuyf521gWcQCFdIo9j06nRupMl3LzBMn+1KgQ+A/CGrinuUwI+tKOmWeawjo7NOoBt9ro1CIhn9Rt+hOmNrc65hZPXhUgkBFYMY7O6Aksit5NwIkEPSIsWDDre2+0SL5E84P2llDCZGRMbPFbGRbY0ILR23Vybj9r1dgV7W4PjU5amKd1k7GZgCRMwWGzaWoFPwU7dmjVJGstbLBnWBkl35P7WBsHgtlBxqXA09F2MqC4XaX8luvUO6vUVywZxiZKwkHa97tWJtNl2ANIIj6tzoTnGClbz9FFH2LBZsZum3WPFqUlLzsSHLuevCqugFaWqic73hckSCtwYFMklOx1Ct7Lpix7R9acx3Mn2DWyRYz02VWxuLJEFtWejjeAA7DZZc10wmDiFRxv2h3XmKfR6pQAZVEs5r0PlQJ0kDEaLrm5k2Mrya39TVnXlNMq8w8yLQ3lwapJb5yY3OGFrVtEP5oDiB7miC7rkDnrE+oE6RhjeNzQlI8g2EB1zHnRM61aKuKtDdzWvDQYpFptbVBDU1l1mFL85npZ2EM8ZLDOaTQEhdG8dtlHUZKS6dEkl2sEBppq4DNNkSdtIMSDLnG06s6Bav1j6W5aSqG2yZEEXdwxbQm5vxYWJw6DHIWPkXDkhlAt8arSzRxsjFHsRHBzJQnVujMx1GLZm3RPWXs255bBFm58CuUXJek5KDHtdRVgHXTGj8A3m6nT9doNdVSSgpEuNnAqLN696lrUj3126TuVPoFSGc2gYoGUEeqAttEI73Ieg3Xpx2Q6XrBCLfi2nKt9u8ZrauBeuouN2w9CBKx8pFsODZtnvdWbJlBqPBPP95XK1bKGyUWippzB8yjQs4DzKtG5ePaDpQoBJ2WiO282eGQsL7Vbskg1bkQlHz1CszlIi/hxXEArL2w70qBTiKx2xyBsv3h2YRra3YOfl4UQUocR1qR5OZ1nHwuBK7QXGPLFeGO7XeLFx52EfxtXcMBdbOzz3OKhjuysXtSnq0ByXe4RkhmTthtja7P09mta7di6jtX7TTrgDuxjvD+tmDzBLRK5yf3WpK7k1L7iHjimnOctFGYHtguplRZS2RL1IejuEomB/lgtIXrTs6Gcos6BYsxND1Cu2h6JPTlZ5sGz/KgI8KCV9V1AhOZ5w1ZoLUTt6vHUGMGrz/LZBFfVKsS3sdWHkVgzD/P3l48t0bv08ff5fP5OeTgD/nx1EPs4M355S3Y+efdv7fOf1+X8v4q8fX2o3BgI+DmObtAufR5X/6Sj201991jFRGx6PgaeHbbf27VC/tcPpG08vce6B1fXwtSnS7n44/PHF6ZrpCxfN1+ch+Mtd6aycTtR/UPIx0JS+235ti69VV7T+y/SliOkpku/F9vtl+Dyw/vjiDcCjsdt8xQj8q1+Xk/LPJyjTue70COXlj/8ArgGe0GwmAAA= -->
