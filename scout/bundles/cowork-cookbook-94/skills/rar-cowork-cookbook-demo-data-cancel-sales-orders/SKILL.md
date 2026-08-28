---
name: "rar-cowork-cookbook-demo-data-cancel-sales-orders"
description: "Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_cancel_sales_orders", "rar_sha256": "8fcf35143d2a53d5ee15fade581d72c94b1b803615e0cde28304289f6dcf2b0c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_cancel_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `demo_data_cancel_sales_orders_agent.py` and in the RCI capsule.

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

Cancel sales orders Demo Data Generator — Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_cancel_sales_orders_agent.py` and embedded as the fenced Python below (sha256 8fcf35143d2a53d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_cancel_sales_orders_agent.py` first:

```bash
python3 demo_data_cancel_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_cancel_sales_orders_agent.py   # or on stdin
python3 demo_data_cancel_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel sales orders Demo Data Generator — Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_cancel_sales_orders',
    "version": '2.0.1',
    "display_name": 'Cancel sales orders Demo Data Generator',
    "description": 'Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-cancel-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '026333940c4518b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/cancel-sales-orders'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-cancel-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataCancelSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCancelSalesOrders'
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
    print(DemoDataCancelSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaebOiyJb/Ks6dP6p6rLoCsmi96IgBUVkFZRHs6qhmSTbZFxF7+rtPot5b3dP93rwXMRFjRV2BzDz7+Z2Tib++OF0bFfXLlxcNOPlk66RpHIF64uT+ZFX0RX2GX8XZhf8nXpG3dex2bVE3L59efNB4dVy2cZHD5VuQg9ppQXNf6tXgfg2/0rhpY2/ig6yAt15R+80kKOqJ5+QeSCeNk8J58Cmom0mcTxz4JPfd4jppQe7k7X1uWztxHufhnXYZp0U7aTw4XMdF8wpFAVcnKyGdly8//fzpJYbXL19+ffFSp4GPXljImnVaZ3XnqI0MlTs/uDJ18hBOKQdohRzel6CGDDP4yAfB5Hn3sQFp8GnyH/9x7p06bH748jWfPD9fX8Z/hy6ftBGYtIXTtACq75SOG6dxO7xO6LR3htESbVfnzagfNGIevj5WfqdUlJMfx7GPDyavIWg/fn0pytGq0MRfX36AVoL86m68fh2plB9/eE2LHtQff/hOp+ncBHjtSAxK/frtef8kCyd+nxoHd64/QqoPZ7rg68vvlBs/D7lHPeHKl9ekiPOPD8JlXVxGF3ng4w9/j6wXAe88RsA/RfenB+EIONA7H5+C//DpbuSfJ9OnQu80/z7bErr1X9EETn9j92nyNNTfo323//8gncY5DOI3i/8lub9aMP1x8tPf1e0fLfg0Cb7CsE7jC4wONwVfJr9+09T16qcP/veHH37+DZL+X8loRVd7dwrfMiePA9C037799KG5P/7w808fuhLGGnCyb12d/hXNv7Lrnc8fLPic9fGPayF/Iz/nRZ9P3iN98mtR/lv92+vEhNjhf3/efJn8Pl/Gz3QyKvHG9GGC3+VMA2X9nR1/ePkNgkMOtem8+zDM8n//94kce3XRFEE70byiayfQwW2cgVF4PYohKDX33K4BtGsTQ8M+58H4Hz08SlwEk1/+07vD5WfvCZezEfG++RB3vj2g7tsd6r49oO6X14kOiRZ1HMa5k04OtKp+zZ0QQMSDDMsaNKC+QChxhxZ8hiD0ebwYAfKXf0j3253Eazn8csfK+IFLhxU/YlLTpeB11OsYgfypBaQxAVfgdZB6WnhQlCCG5D5BfZsivUBMG23QnOM0nfgxBHCI/sOdNrTTl5HYL7/84jpN9DV/gOh88igLzQxOeBdn8vkz1ClI4zBqv+bAi4rJh19/+zD5r8k/WnUnPvJQIZI/vQAlFDRlN4FZ1WVw2lg1IOg6/t0Lv/72tCwkAwvSBPosDmLwWAyj8gz8NzNrHP0ZI8iJC6B5oWmzsqjbscjE7euEDybv8kKm49CI3VHRtLCUlSD3Qe4NkKoD1Xm3ZD4WJhh6TTB8mnQNuHP9xR2rFxQxg+nttL9M5JUKK0WRwj+jmPdJcHGRx9D870HweA6J1B+aCfNG4nWyG+NwUjq1U0a18+QROA+/wArxthwSdyY56L/mYz0Eo6nuSfEwTziW67Es3136efQ5rO8ZRAC/eeMdPku6P9Hvda3+mjfPgHdqcC/mUJRhEnaxP0bi354h1URFl/p3+0FJR0pPL/hPr9xjcPUX9X+s1JOxVE+e7cRY8ToMQfHJ/19/MQpLb7eH9ZbW1+xkvdMP9sOIY0M0GvvRQ8Fq/yA2Jsz3DuANP95g9GuexjAi6uFvj5l30z/nPKCpq6GlDvThTh8KBo040r2H5RhmdT0GtPM1f8PrT1CrOzhBz8AchjE+htYbw3H0TdIIJup4/712P202ag5Db1J2bgqtGQDgu453hlLVY2o9nQBjFIxp1kexF/1BqwmkDkMB0p9AIWKYLBDT76bbFVBNaNqgLrLv0+PRd1AKv/OgtLDjBK+TI8yOMUIamJKwrRnnQCt8uJOaZADaGIr4buEmcsqHMGOT+hTQGX1RZDA2fu+B5+D3eL7LMooPqTojlH7N+xFcfXB9ePZdzqevoLDZmIH3RX9091PXye8Ly9++5ncZ3/EcJnY61uTfGQfGX509onnEpQZiSwaeAQQj4V5+Xx8V9FGi32X58qfO/OO/1rzfa6LxR899mURtWzZfZrNHHXsrY68QFWYwRuISNPeS9nm01+dHdn2+Z9fnR3b9gejDRl8m/5pgfyDxjOgvE/QVeUXGISmGSQkN8fxAO6w+M/ZnfBz9mh/Adwc/o2AE1HSANfS9urxNgSUmrEE4Tn5Um2YsUj2si3d4hS74mr8HwTNFIHrn4Vgam+J3qXsvs9ClD4+9VwE4lLeQtz+2YyEYdynpKH4DXr7kXZp+esmdDPwvu5MR5WGIjjdwPwPTBXY2bQzud+9dznjzx73YPZEgAvjFlzGfPk3GjvTT5L25/DR5a/fvm6e8g/udn8bGdmQJp8Kv97nvGz0XvMC9VTuUo9CPPczYTz373D8LMaYRlNgDY+Uu3vNy5PgnIvAiDEH9ZyLK/cJJn+DQtM5Yh+P2LaUbKKcPu5pPE+g2mGoweyAodnDBn9lAPjWoOljw/FHd7/b7rlbx0OW3uxnax0bw15c3kHj64Nn0wekwGz83Y8mbwRCFDOH9I5jg2L/WDj4XQ0yDHQlcvQi8YE6g+NzHHGLuEwCgRAB3RcQC9SnMW+Iu6i6QOYkSAPF8gC3mCI4tlgHpewHmIh6k94jHb2NRj0eBABKA+RLFPH9OYgSBL1EKc5a+g1OO4yOLBYVQgQ9h//vSMwTEp5YPrUYTvnemozWeyv764pI4nMnhDU8/PqvZ0nRIDHd3V3dak0Go5zPercyDlGHXCuuP/gHJtyQj0LeOOoC1eGxwWXDXgHUCNtMjp0foAFrNFpb5hePE7lxiSLw4xqF5kfYzqV9shuniiilhTNu5VzRmlfVyah6zlXCIDpaK7hz+RIkGXliiudpIBh4FwYxMZ2Gjn04O323YxdZdaq7R+DGuHzdatd2u2uOR2QdrEb/xwfqsDdLNKvfVGc0Fb9GuyPM1dwjHJ5ea0Te2LdXaFT9GyKKTNlM/k86Un98W+omkgnyOBzFlOAK23e+NfXlKD61OclJ+2GLI1SeJhDuItxljxV5qumdo8SuWKnF5bqxLLFQEUnVFmW3Yzck8FgdhCHJphzuiIW6qi2RIfcO7YbHbpWErHE9WnLp6vor9W+zuypTXrWGDOmbZVurh2Ex3LXMhlWEmK7eSrKVhSe72iSpO4w1/8sSTuZZrcqWXq32jrm/nIY3MTiCL6W5H3frVuWj84XDa74UA909z5iQudrcQsHVY3VzNrxdRgulkYYOMMApDus4N51hU4SAOopllnRNOFfV4Ym2xDbGtfty2h+6kIKjsecdKc8UZpvFOBzHn7B7VTN6Xe7Nk83W/P5K7+siiEspd8sGwZ9S1LzrbKnPzQlIXI79u61wqE1+NsqubCzszcy8lmcn4LjnyYYzZXbvaLS1od8NtUGNqdQxhXI/XsD2uO2WlJppw8441XonB1lpbuH69+qKQCZtltOrneOPp8YbbUMVqa5cUuznPKvVSUbmdbs2OoHanG90ml4GUb5azjXcrokl2YjlkJ6erB0cuiR1nEqhglTdWti4I1tbhPrhY6lXm+r3asPzuWhHMoOIBxTJkoNcUCQJ7ziB1Ws1B49fNxVcO7OXsitwNaahKNDrCivxKPykWxSAukTRr2Xau4imdolICSkRcnP3UwfbpAmnSvRISBJJkYrEyklhm9mYm1Ye16m1DXKa3VUK4knIDpqYyxpy/lWtbkXdhXNkxudoDnUj9o417OnPFidwTi0G5zAUl80/ANhbNcNhJBH5OASaVKsthFYXsNI9Ojuommum3w+48S900lWZIsnZPdn1C+cv0MuV611xJbcmny8XRnVmkUeGtmU6Vc4CYqrR0j+Xu6EvU9cAPyRAKfW0iqyKTFmUW4J2MStN2j4cXKuyHq0STgc3q8/3WOeJacmiMy3QZ1dsFud1zm2liS9FyNvVMbROkOExvUbaWbRxhfuUqGRLEuRaJsWR07XR35ZEMM3HjvCxMema6JX0Qk4Y7oC0ShJ2Jr3Bp7SwLJWDM6wFvkMjh3LZZqTdDX2huGWtrPJ1OrbjXE2NfzHBD3q9tA+y5dlpbcjcrhNNVH/r+4u4jW6s2QRAnp7bxdkicaXw9MA7Z6kKyqnwh1GzN2VgnEN2iVt4NdeN5EbcvWQ1cBqTaHXNurg6pXg6wUTkj83JmCWtj5tGUXPOVIbQkmy3RTWthx101P7YKAWQWwxeN7AbRYc8Rut/vy+1cIc+pyFpKdTEKrg3zrV6kOnUO+326OeNpic9rbM9IO9vlvaVD8JrGx8udvgisOV02+IFdC4dFV6fYkiXODMqBk6Pq5gk2TMmtWRkszYNa1G0+yaeJKew3c/vII521vIXnSNvE3hKhTRRTs2vdbten3dpgNtuUs7axbCpCIPj4Qbp10oreS8zW5jENY5szIy7UuFnspgTuhkhkenvQIKumhV/YMVcLSi52/la+JTVFdFaJgU6Sr7xQZVpzTdP5BVlUg5akgFBO1Ilc09fNJiIoc7GQA8lm67ZTbTW+7iP2ii8VK7nis9nikrFTVb5wF5yoQnUj9YUTK0eTQhpl5dAatU7KFYaBYbmv6DNYHrsM18JNBavxWdeMyjmgvYaF6IacMYfbdqiNcqjCXcrhKe1uNb9MzztyjTNdKq8sO8gZZS71ZaIl1dnwxFLWbrtU3CwRIl2hmLBYqZhF31Ayvu3xdI4LS229vdWbzXS+PrKe3gIql5Sz5Do7JXOGucDu54ivlix23C6jLdelCKEpHqso+L67cZbChCyjH/JhgI29TdGEn03nwykeTpgkDjo74Eil0ilTpoNgbTocXXRUsmEU0Gf85YQ0gpoC6xSZg+mb12Xf9S4jGmvaT5w9jm5EY9v0u8vaQ+e2FxXJlrlRUzHVrjY+AJr3qnWrmuKa0ooo7gXmeDORQ98s0JPlVAG9YWl/bWQH5lwv1oCOyC3vmRLclFTxzQfcWToUKxzf5cLBLM6Yndp6csrwmF+rvafNDy6565aknUrOXlsxDb4yr71mYZh7Qtf2IDZ4xG+ykBk26vQmD14hTX20siMv4Lbmwtpa5+vZyjLHSZ00VBHXOmHigRW6AykfIpkgJEfxTgve52MW2SX+RnTJ7DAEyEncw1g/l1a1MbXr0emAtz1y/nEjsqQkn4kiRXoXp2ND664WL4lhgIPj6djhK9rAzme2loPWUkvOQESHdgj5MrO5LXKYYsmpL4i1lLc8zQF2aC+e23K6UkquuCD2zmkm7f35YgbAhXJhI8ewyPzKoIXKYVzUscXuROp6tjhRLotUQ6dTomvJMzdGutQAu0u3Oy1WN82PmbVe+H5XrBCBr2gmCnvyBNCsTgWVmUUrIXbX8kE7e5I2A7mAatlte2TMyGS1A2ogAzFkukT75xMSSUdxYyrXpUmf/QHX+uFsrnyywm/b2hzKVKojpDKcDVXnorLot7Iw55fLcrFS4DbIS8qGc9e+dw48fmVieBVGt5uByqmk0GvFZXdn+4qc7A2isYeZ0U0P54GcV7aX5SfT3auEZwSFdLrGQIebVm3ReBumn5cW0etHLfJ5R9va8W2xDoHcCBF+LnR+sKUwKPoSmZY+qbJn31S07W17EZlOqtfmes+dHQvdbjkcdk5D1CPUKVVJj0/8kNYbsrutDqZnUGmmo0qpQISMmuXOVJY5Qq4RKq86nBu4+f5WbC83puaMbpZikVqhmpT2m/7odR09R91DMhQdacVye8ZJ6yCZssdTU1M9tFsIeielvBANAxgvlTXPiv3YsHM6RtZy4gl0qHfLPpAvaMJjSCIlxuaU8IQnnXoGWZmWMSV5qlhr1lFMLKtmpyfUQ6YRMZOSluhkREsLrVk1XYoWRiuujlrrNAJFd4Ni9DQWM03LYBu6jTvdm9nInCbT/QIYB1LfDPi+mm9rbkX1y6zZ4xtJiRQ5x2CU33RHC2cLIbttDtIl5LSt1y95UxUVkcRMo0aiwJ8KztTgBXY++OlZaJdrTQCsb1CkwYu6hmN0YWohHpkHzF2blaDQju4vepzjwNoGSzlHWH7PSlyHpgsTJRvKtyK50nQ6mUndwTlk4oqiWodxSYgqoFh0yLDaDs36chHYzKZVEpMSs+5CQfcZtXTo9TwO9rniKBm7oo6kcjjYDmGYZ1lT+p6rGcQWA6FfhWS9FdETYxenJt9UTX1MkSmRp2QSkuV+29PS3tDqQARs44gnaoUx4l4PDzIQc6X3MrXCjuRKMMgqd2WJ2yahv2FXc1Qear7O4aZif/E7KpKyfRN7u8UQ3NqKJItLel7vUVrwZiccSb2Z6a9FrUvWYCNN9y5pKClsrUVAHvFg62cFyvkoRDGU8utqettWmT67sKFVldTJck8c2svmzOlK2pYUTGV9e+BX57QAM0+46aGp15UvT29HW+JndE9sk1LvlO6YRcC5kljn1F7ussLAR7IuixafHzjpOuudXiDFrdMTdmpa7rx3e/+Eznf8Kmp7i1Qt2IUHxFI7Ii0mqAjAoEA22rHLxLYgigdbzjxySXGTKRG72aGI9DPYx1I0IOL6Om2ug6oO1mxJHINFuNVSxUTlLpnN1uzU99UTWCI3iozq5bnDzrsDZ4sYDXcZYtLLy80VlzJVCY6CRe82+XJFXWmOnrtTvbLN/V70/E5bR0Q0ZQSOI3Z4qNCUkM/yg3ecnqw6Mxc3xKKxVc3nSlIsOJY7E21K6/GU2xE3/SLKgNTsjFzDBmoTINb1ctxsA/ZMk7LZzvfyOei77ZQkVyDaJkvAH0NvJrl1I06PndwNw67YC4vl6uxQa/XoXxt8K0mMneDIBkGpabpH1Laacwp2aZB66c7mSRJxItxAqwlGn+KVQC1U3cW5qIBN/cwe3FVdUxYbxdKWZt04UW4L15ovMimotgSg9vzFXe6JpLycVHzmEvquWaMrOqdqc4HRkRopVoWs+C0x8LmhXWgK468gVojjrLKi9YptrhEICmzDBuuivnpqsFmwrcgsvD5M8r6QZW/T8hmX79VEUK/VYOZx3akNPQVMWBviPGKlhSiCWUovgcoWxiHeUqFqhkZ468Ac680eHDiGzuQ5w605lToPvSeyrB2FVc0t5gWoq123j4MLkXqMpEt7bVblp50r+/MU4yM3Ey4EFet2RmTNJkJCSiB6F2IGXti4b+XrgFz2GD+z1v4yW94QtMCoK2/siWni27w4A01gLzzG3vf+VJXWJ2nTb8opWnsSiWasBxxswRebvj9yrtE2wS48U9x8A4idgVJgCeZ8s9sTJCniIB7gXmSH8+u+7teFIvoXpmVdPHDXMc2K1xnDFZQCdy/JdQFCNnaFS1XC6Gk2N0cKWBbwTOFjU16WmCXhohaZqBlm+egtmNdVG2RFywQSbLKRjsvCAPGKQxBfVqZ5WbjCfGD3zbxKO4qY8hjXLVCyz9DdfDpjglnuR3O6oNAOT/xAW16HdSIw82iV8UzSo2Ztze2AcNkeJE60gFvtOpMuh2Eq4UZwjR2mEIQ9qOHmGQRUZK6X2wTVPRCJC0xfbuquZoFE+M6pnk2L1mk3GTcEzHyPt4rMOizjaJARURa4h/uschNMdNk51s5F27Jbtru53kVTCeVXPcrfumhxy6uDaveAS8Kp6GQXOgI2OMFcZERcy1cIxihufzJORxUVWuFmswonHAQmIYw263SuPCAC1hBAOFGKDCXeucCRXHpOzTNGChuqtMJLwSMcBuvNMrja0SzbXHz3rJhzVzFyCBKM7F7E1QZzYrhXFi5LnTYkVCfyquTQjuhVmTzZ7K3nnMHbxu0BGNttRtLxJiyHWd7D/l0TkDZdEuWMPUJ/t5dTQbFKeXSlE0mWLITcPZguqxYgQ0jT9I8/vnx6GY+WnwfE/9z73vHY7v/s9PBx0Pf2iuh+OAwc/8ud15d/Up6fP73UXgyleZyNNmkXPg8T/8fJ6Od/+FZhXDo8Xp6O77Cu7dvxeeuE4+99XuLc75q2Hr41RdrdD2Y/vbhdM/4Aofn2PIB+uauTlY/T7Kf48PrO4ltbQE2a6GX8ccD4Ugb4sdOC5234PCSGCwfokNhrvs1J4huoy1HD5zsKqBj2iryiL7/9Nw+R/DFRJQAA -->
