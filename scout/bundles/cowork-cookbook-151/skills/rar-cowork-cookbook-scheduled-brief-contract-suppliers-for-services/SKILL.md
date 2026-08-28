---
name: "rar-cowork-cookbook-scheduled-brief-contract-suppliers-for-services"
description: "Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_contract_suppliers_for_services", "rar_sha256": "5cbbda9c9da6253e390e8c13cf5cf347e498c2547cd811ab577c6ae9d8ad5819", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_contract_suppliers_for_services`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_contract_suppliers_for_services_agent.py` and in the RCI capsule.

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

Contract suppliers for services Scheduled Email Brief — Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 5cbbda9c9da6253e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_contract_suppliers_for_services_agent.py` first:

```bash
python3 scheduled_brief_contract_suppliers_for_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_contract_suppliers_for_services_agent.py   # or on stdin
python3 scheduled_brief_contract_suppliers_for_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for services Scheduled Email Brief — Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_contract_suppliers_for_services',
    "version": '2.0.1',
    "display_name": 'Contract suppliers for services Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-contract-suppliers-for-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2735feb334a8748a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-services'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-contract-suppliers-for-services', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefContractSuppliersForServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefContractSuppliersForServices'
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
    print(ScheduledBriefContractSuppliersForServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZeb2JbmX1FFPdhZ2ME8+a67ViOQhEACNIPSuWzmeQYxZOd/74OkCGfevLeqsrofWnasELDPnve39znEry9m2wR59fLl5eCa2WxlJkkYuNXMzJwZn3d5FYNfeWyBn5mdZ00VWm2TV/XLpxfHre0qLJowz6blduA6bWJaiTtL8yoLM/+zVYWuN3NTM0xmdZumZhWO4P6DkWk34GZRJKFb1TMvr2a1W91C231cNIE7q9y6yLM6nHjmXeZWf5sBoaGfuc6syWdVm80cwHuYAfrOdeNkeAV6ub2ZFolbv3z5+ZdPLyH4/vLl1xc7Mev6h56uM5+U45+aHN4UWebV4akGYJWYmQ/WFAPwUQauC7cCuqXglgMMe159rN3E+zT7j/+IO7Py65++fM1mz8/Xl+nfHug5mdPkZt0A1W2zMK0wCZvhdcYlnTnUwNKmrbJ6Zs5q4OLMf32s/MEpL2Z/n559fAh59d3m49eXHKhgTgH4+vLT5ISvL8An4PvrxKX4+NNrkndu9fGnH3zq1opc4HnADGj9+u15/WQLCH+Qht5d6t8B10eoLffry++Mmz4PvSc7wcqX1ygPs48PxkWV39zMzGz340//ii0IhR0nYd38t/j+/GAcuKYDbHoq/tOnu5N/mUFPg955/muxBQjrX7EEkL+J+zR7Oupf8b77/x9YJ2EGkvrN4/+U3T9bAP199vO/tO0/W/Bp5n19EdwkvIHsALXzZfbrt4O24H/+4Py4+eGX3wDr/5LNIW8r+87hW2pmoefWzbdvP3+o77c//PLzh7YAueaa6be2Sv4Zz3/m17ucP3jwSfXxj2uB/FMWZ6D0Z++ZPvs1L/6t+u11djaT0Plxv/4y+329TB9oNhnxJvThgt/VTA10/Z0ff3r5DaBFBqxp7ftjUOX//u+zbWhXeZ17zexg520zgU4Tpu6k/DEI6xn4/4Aq4NcHUj3oQP5PEZ40zr3Z9/9l38H0s/0EU7h+w6Fvd5T89oaJ394x8RsAl29vmPj9dXYEYvIq9MPMTGZ7TtO+ZqbvZs2kQgGgElACcLGGxv0MVn6evszCbPb9L0r6dmf6Wgzf700gfGDXnl9PuFUDPq+T7ZfAzZ6W2qBvuL1rt0BekttAOS8E8Ptpgu88uQHcm/xUx2GSzJywAk7Jq+HOG/jyy8Ts+/fvllkHX7MH0OKzR2OpYUDwrs7s82dgpZeEftB8zVw7yGcffv3tw+x/z/6zVXfmkwwNwP8zUkBD6aAqM1B5bQrIQBBB2AGs3CP1629PXwM2oOXMQFxDL3Qfi0Hmxq7z5viDyH3GSGpmucCBwNlpkVfN1ODC5nW29mbv+gKh06MJ34O8bkAXK9zMcTN7AFxNYM67J7McdEWQnrU3fJq1tXuX+t2qzLuKKYAAs/k+2/Ia6CZ58tYFJyKwOM9C4P73tHjcB0yqD/Vs/sbidaZMuTorzMosgsp8yvDMR1xAF3lbDpibs8ztvmZTE3UnV90L5+EeQAQ8Yz9D+nmKOWjsoMlnTv0m+05jTj3veO991desfhaFWU2hsEGTAEL9NnSmVvG3Z0rVQd4mzt1/7mMUeEbBeUblnoP8fzFGvLf62eI+gtw7/uxriyEoMfv/ZF6Z7OBWq/1ixR0XwmyhHPfGw7+T0CkOjwENDAtPMaCWfgwQb/DzhsJfsyQEyVINf3tQ3qPypHkgW1sBZfbc/s4fpATw78T3nrFTBlbVlOvm1+wN7j+BJLhjGwgaKO/4YcubwOnpm6YBqOHp+kfrv0e4cqZiB1k5K1orARnjua5jmXYMtKqmqntGBKSvO1VgF4R28AerZoA7yBLAfwaUCEEdAe/eXafkwEwQIa/K0x/k4TRQAS2c1gbagnHWfZ1dQOFMEahBtYKpaKIBXvhwZzVLXeBjoOK7h+vALB7KTBPwU0FzikWegnz+fQSeD3+k+l2XSX3A1XTMBviym5DYcftHZN/1fMYKKJtOxXlf9MdwP22d/b4v/e1rdtfxHfxBzT/y+IdzZqDW0voOshNk1QB2Uvc9Tx/d+/XRgB8d/l2XL38a+z/+tZ3BvaWe/hi5L7OgaYr6Cww/2uBbF3wFgAGDHAkLt/7RER91+Pmt6j6/V929r71V3R/EPLz2ZfbXVP0Di2eOf5mhr8grMj3aADFTEj8/wDP857nxmZiefs327o+QP/NiQl9Q3dbw3oreSEA/8ivXn4gframeOloHmugdi0FQvmbvafEsGgD1mT/10Tr/XTHfezII8iOG7y0DPMoaINuZ5jvfnfZByaR+7b58ydok+fSSman7V/c/U48AWQzuT1soUFFgdmpC9371PkdNF3/cC95rDYCEk3+ZSu7TbJp5P83ex9dPs7cNxX2/lrVgR/XzNDpPIgEp+PVO+77RtNwXsJ1rhmKy4rFLmia25yT9ZyWmSgMaA0PqSZe30p0k/okJ+OL7bvVnJur9i5k88aNuzKmLh81b1b/l7KcZiCOoRlBgADdbsODPYoCcyi1b0C6dydwf/vthVv6w5be7G5rHVvPXlzccecbgOVYCclCwn+upYcIgZ4FAcP3ILvDs/3bgfLIDQAgmHMCPtC3LMVmbdUwKI3EXZxGXsVHc9kjbwwnaJVjGxkiCth0GRU2LpGmbMl3WYUyHZFAW8Huk7LdpSAgnFV3EA2xQzHZwwJIkWJTGTMCfoE3TQRiGRmjPAb3ix9IYoOjT7oedk1PfZ9/JP0/zf32xKAJQikS95h4fHmbPpmXAVh+IUJVA/fUI55tild825lKfu6S+pQrfNhRvRW26uWhIVnpQYqc3D3RR4zmxFqDwNvJwsYW3dLE+SVc4WnIns8PFdlDwK6YnJFmk+zwMTV0qh/KiX3iluZzN5dmydRPdyiVU6Woy13XsbCWWuRxs63Jsg7mHJmXTnxgYjlomvqRBv6VPxYHAGfLoyQlZYCyqorfCc3lqcMiev417S7oUiYwq5vG4USwzK/eDpJ9TVs4UxjiBJjfwS3pDC9C5TC0jYDUpcDwPxhmqbTdL1PFCs8k2JAkviVpfLM5iWa33dYphRWMpeACFlR3E0llxEEFj9q2LJRe0lHT3uCtdtNJcDd/KaBCQEL83kYujXRD1SPb69rIZT8h1s6JCWz/Oc6labTlZdTLpVEJn63Llw8YlqshM5EWPERCxj0oV39lQ0yxv1M2sFBPV5W2oVFfZUoPDOPJXCjfNxVifjfKInTGORPw1EJjI5qJ1rNAp25G2l+ycP+ouuW7y9RwYGJ+lrEltASauZ8zSLcZQKOQ81rAliEV7NtGQMaDG2kbtuTyU242LzBvXq0O+P9HzRmvjrUm7g12UBpRfzzG2h2tSVVZJ6eBpd4rWXtaeVb5ZG0RqN6tjSgbsUdItsstUGGNsiou5skesKEEqmgmcqME7d8QQY4/GfTtssxa2F6J1QXZI2ZDXbXRU5RVUY1LpUPnmkFaWupS7tBd0GOPTYSm5qwovinGByTBzvDZXOYHmhWgqoSYZlG7zdL5cmQV9TGK4xXdnpO2tayVvAncTCU7qJZCdOgi/MBfVdW9jV1nftGK2rvBU13El1zqYVI7jcnXpCjyG9/lu543Irbe9fg/PRRfmztlpM1IaLcikN25oyPQIV49bN3fokzKPOw9bN8gmZS+U2XbhZpHF10SthAOqYksGq27G2qTHVe4etoe9vdWidKgOHT7UtF+cRBXJ9HXDkKgtJtdVzml6cVKimkD7Fe4jvr9WF+khllFpHVCbtkucdbg+0tgBWS4XTYlVKhX2HYFFKV44QwHPMSg/j8g4EqXnKF1FSn4KHcbIljxpu8CRgdVW7HlxiyVaK3pXIqtLfx4y4jh6wdJ3GPm0pWOY0phFlyvYJtpfa8+Wx4qH4327wQ9Qxq2Zi2FJWsUnZtv2iFReC5MQdTS8ciof1NQ+gfDlSYGPx2EVwSGxiM0Y3Q/HjkUOxzCwc4QTLPa22HiQL3aaCGVbqYAh+qYsUOeMkJ4u1yIZURHuWBs+Q+DmLHfxJe6ul+Kor9klahFxYpzkRq+Ma7BAL1Dht62aORc+Cq7X0KdYYaT8VELjU1ltSYeLzzB1gZfNGXVC5sR6jiTZa9w1vUEq4sUePZ9UuiM2OQJ1e2lYHgb/Zu3214Eu52s0w1KCOJIiZylWyJljZgwIauiquWz1tkEXcI0YgyK4Vwfb+AS13ArjEr9U1xtC0/3BUZGtUyg04i4xT9l5gY1JyaV3EYYTO/FCyGyc1MiFzHG8Dpk4udKoFSyhDTw425W/VTgt6U8LWbKudMqRB8+Nu4FFS49JZPXSwWKMrRJD2PWXExEwY+XlKceGJCwdPC11On5lU2QmqaYMgY16eK3WZz6ijn4VFyGMHOpdIF8L7pQLMCr4GQLAf2vMuXofGepan0t8oi+sLthhvQ5FfkfIgUrwQqBJUHEhEGRjp26p7VYBQyw7ZLWQ+kbGRq5JjE6e20uPsKOqI3dXHiv2rLleNquObUKmFsQBPnTlbtO2t3CDMLeKJB2dXK5tQYoUl6Jg7Hw4nIwIJ6MDvSbibO337W0XVmsWrjkeh4hlJFArYWD1mwajTOVIGvi9hVsRz2B0DsVCn1JrNRKzLCWuAlf7SxWV5R1ZZ3XFy9zycEPHouI7wWOCoOGJmBd369Y/XzfMblwsMRazTop6PEWjb/lyaSbFxfC29iCMmSRcd0f27Js7rKiWxzLIVV41lXSvuVV3rcoNZ2/QjMD7eeXtpDbaxo3WVVKDB7pd0kbf708H0z8hmLJIPbNKM3zpOnu9GqhCZpPa9dQgb5nNkpznxnlO50TLW4Dd6M6FmmwGZr88Ynyf+KMg5tpFr9JrcqvkJrhdYffonsetfl3i84Oflcec9FFd03PFh2gKJ1Ix4IODo+i91cQVP0+odiOa18QARVS5+qlBEWTNsOyAduIBtblcxdsyv+QxxWtGqYPmzt62W+aQmj0LBrPKXVDCllu0waU0mooj+Usg5ZfNGXH2Cmx1Sc6352qTlm4RH+Zrsd5ggdab+FxnzrtTHWJjdXXFUeDy6/XU7lblLR0tfR92/A4tOW4nt3mR3OY4ToMJDZ3vkSC2GaJbNGEUc3aLsdlpuARRfygqRaROnECovTYfKB7Odt4x3gAs6kCDGdjUUNj8klaXyBBYFcWcsD5s6NA98saudQ+QULUezUFEyMrE4BxUqFjYOrs6hHh6KM16hwfl+np0uyMHhWyZ1ojCj6CmNl6t9p3cucVxv1bOxSm+osbZHP01vhIuhNeTN9KCEEk2ziUX5Rrj3KBO7lUVsq/oVtc4ZJ5yywS2WZoKz87BQinXZtg1A+v02Nmdt8qsoVnaB8fc+CyKXDtRONo1stQyl+pZo7ZiCM6a7oYZrYSUFdpEZNHG4gq57S4ERivQjl+sa3nBB2sEwMIoXKiLLWimOCywlWWGe+ZwIOGbVcZFWZRmN9f8Vd9FPGcXOpkb2lmmdkmlrPKwpCq708UWWiinNN/dXN8xt7mPUqUvn4TolOMVHWj+ghtWjILLaF/l++EWOAuU3RMXQmrjcVkF2KEX48sSMpTUni+ZcK4b57hYLhQkFHVYUiif7JH2BCCEla7tDo/H8ZLccH5FuJeYKDHkKDUgvrES9wA3cmRM+HHOGpebPIqCNDdb5QomuoA3VvMzfz7z4qGwoxLFdpgkFYcU9J79sV+0+6Llt9tbtxIzdpmQWC97CLtfXfmD5qBOKu26LDzvD4OxufbiFTR1h147iHQLb+dVEAwivhvz1W0j3MRlBJoCotu2acnnqWGQWCXRV8VD59cdCyYfUT+Up+12a68z6Hzb1xU7YEO+0cgt7yq2sjjGemjR/GjsqaOxEubikurRHQNcej0sMjmx9NUuJAcAQu2ijPqBpagoUpqk3l4ijOSCTK8yRjuOp/no9CPaHHfy2ryBIbUMioXgliHNXRHhVnHz2EeygxNxBrmpBwA42n687jVxv0pPB1nbYsVY4vhtu7SKRauc0IUVErdBXu5lhDnJaWzYfXMgCSfVN6nYrfbJ8ZqktNndwhM+YgosrXhDIjOA49Zts9hbeS0ss8LvErBH3fNBIc+HxJNPxOKiL2guWbYuqXJ9Viw071iw8wshYBUDDa26uy0aHM0HeVF3awFjE8Q+hmlpU/jp6tHszmq2xuVy2l0cP3XJwTl2W6bgaTUgrlC4Mrto3oxXpITjaMGZ+ua4Hx3NxGV/8OdrWpjbWyHuzq7lc+XZ3KJUx/e78doKQtI3UhPByqYR5+juAHMcy61kFqIIlaK0puNOXcGHxa7PICMX5UVbA9coZtVtxJV9STQxWK5XCcxvD5VcZSyyDi+OaLhzRLSicIEqnktdCbRwTH2EIpnLD/op9Rxb3yV6zCes4EZQEYyqSsTsmTpJmJjoGcWgF+fYkJeby6hmVhu0qIsjR3oRdO07SAwGRtVLWFR9SLRMVfNx3fdy6sqnTSlsTxme5Xk1HmJFHSlTNFmO5/nNKrIT0HcDFyrM2iXz0LdXZ2YvW4UBKm8bgpDiHAw2K5KgroHnnJsD7Q9z4AD7vJJo2sj4eMy1JXEODvoAqZI2TYVimGv1UbkZY1uMmS1hy54hbHoz3jh6s2QqbYR4IdTdzpm3N7LXNCyDaXYNU3w4P52Fy8apaEi+ERrDJjRuaWO6jLCz6O7I2OmsnBfMotLWFXLWF1A6EDcjtWPEgIkjtM6blaBR6GZZ8bwQNSOXarXXbdc1LN3OS0QEm9aS1kYfQylaN9oI7bb8iq6QCnOiOeFyinMZ9p0KdohD6kMnA9ulPZB5Sg0H3osJZJBXhqn3gQy3OxLawUNsZnSrdqG1YtgTyxUQju+YM1OoeoPGZoUVHVp7OX1ir3iP+8Y2WJWQboBcrJmLtofcyLCzA7RJbugNvmgtYtRyX8oZsxgWCx0jVB1HvMxwUprtwC3dcFwVW9SEH9QyQ2/HxnMHqolyukC73dnF030nWt7ACHSbcGx/XOzmXptgG0o9Q0ue0RcOj6vLFc0fqVI5bC4L3K1vuIUsWL5bx+hmAXs9JKuuZOol5rrMaUFtJYLsi1ibX6y5L1g94wp8yyXwoBo1Y1mVyGlZaMhoVBGJ2EpLzaMg2A2j40hJBBuxO/Hko6ceDmhkSDp7n+3nqYzPN4tNiEuJzyDpAhUC/eKRwS63SmUwEg8eZWpYBYduD0ctcsWJTasbod5uUzizpHlopRfk4mNCfbvZZO6v0X3GU+RchNbs8Vx7gRqlyODg81ub7tq5EGYbxN14vLdsBQeyA8PoPMhbrUesCtXNrb3x2jw22ISsJCbcbZK8UbHaola0YKgtlAgJHh3ZQIV3od8LPh5fOlbc+ABL9YJYM92cQ3SQdP6ePTa0t5ovOWgfwYa4J1E/JjUSYtboSj16l5PmV32hlI69dgh+rpXE1o0sw/GUJMAwwvR2R4zY4D27W49hNyIwHlUXTd5oNhyM4pwEJU9YAWXX6JZuzbm1FsGQEjp2ZGWdCu9pNmGZTWh7A+yXOHOmKSEPd7Inq1tO3/uytyozMiUrZm9HchkFqyjHmpZaenOWwAnU4ZDFopNPCaNrcOSXPB+au3aMl0o0Erfw3FKNQtwSsijEQDlWc9Au1BbsEDq6gTjOjCTi0K8vpGQTDKHw6nF9plZMkJQbT6BlPRJzB9osT1EXrA3cc5MR3Wb2WhDIwVs6Rz3QPUnddh7HJfb62LsUl2nUVl6XGqrcpOgUqZlykIKMOCuxKkVIQZlYTbp7R2w5goLCymurKwez3ZIrussRyTsdYcEGbSUVbouwp36UEbcJhY3IRvJmmuQxhTz1MuXMFxUdj2jalwuqhQZEzGCcJ8VU2NZzkhDYdRudL8xNFsS9Mt8GhuzeZLChcRaJI+UJvspYmoA69hp5mW1HDV2P4qa+qRLMzIM94wx9DQZY7u8vn16mk+vn+fP/9G30dAj4/+ws8nFs+PaW6n747JrOl7usL/9jDX/59FLZIdDvcRpbJ63/PKz8h7PYz3/xVcfEbHi8/p1etfXN25l+Y/rTnzm9hJnT1k01fKvzpL0fDn96sdp6+jOL+tvzEPzlbnJaTCfq/2DijwPWJv9WmJOvw2x6g+Q6odm4z0v/eVz96cUZQDBDu/6GU+Q3tyomy5+vT4DB2Cvyir789n8AZ/iA0lsmAAA= -->
