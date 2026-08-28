---
name: "rar-cowork-cookbook-configure-request-travel"
description: "Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_request_travel", "rar_sha256": "f2397b52536cb7cbec0b7a9f50e900d26908c5a06522c6f15db2ff5714b00d32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_request_travel`. The original RAPP
agent is preserved byte-for-byte in `configure_request_travel_agent.py` and in the RCI capsule.

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

Request travel Configuration Bulk Setup — Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_request_travel_agent.py` and embedded as the fenced Python below (sha256 f2397b52536cb7cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_request_travel_agent.py` first:

```bash
python3 configure_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_request_travel_agent.py   # or on stdin
python3 configure_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Configuration Bulk Setup — Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_request_travel',
    "version": '2.0.0',
    "display_name": 'Request travel Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to request travel from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80b449ba83b48e6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRequestTravel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRequestTravel'
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
    print(ConfigureRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6a5OjSJLtX9HmfqjqVVUC4l1jY3ZBAoRASOIhJLraqnm/3yCB+vZ/v4GkzOranp7ZMVuzq6yyFBDh4X7c/bhHkL+92H0Xlc3LlxfNt4uZYGdZHPnNzC682bK8lk0KfpWpA/7P3LLomtjpu7JpXz69eH7rNnHVxWUBpjNVlcV+O7NnTp/dxwZx2Df29HjmRnYR+rOunDV+3fttN+sa++Jns6Apc7DWLC6qvptxgzvdizP/0+wad9HsYmex9xAxKdSUWebYbjpr+6oqm+4VaOEPdl5lfvvy5edfPr3E4PvLl99e3Mxuwa2X5VMNX32sq9+XBdMyoBB4Xo3A+gJcV34TlE0Obnl+MHtefWz9LPg0+6//Sq92E7Y/fflazJ6fry/Tj9oXsy6aDLPbzvdmrl3ZTpzF3fg6Y7KrPbbA4K5vigmXFoBXhK+Pmd8lldXs79Ozj49FXkO/+/j1pQQq3A3/+vLTrGzAek0/fX+dpFQff3rNyqvffPzpu5y2dxLf7SZhQOvXb8/rp1gw8PvQOLiv+ncg9eFEx//68gfjps9D78lOMPPlNSnj4uNDcNWUF7+wC9f/+NNfiXUj302zuO3+R3J/fgiOfNsDNj0V/+nTHeRfZvOnQe8y/3rZCrj137EEDH9b7tPsCdRfyb7j/99EZ3EBQv4N8X8o7h9NmP999vNf2vbPJnyaBV9fVn4WX0B0OJn/ZfbbN23PLX/+4H2/+eGX34HofylGK/vGvUv4lttFHIDs+Pbt5w/t/faHX37+0Fcg1nw7/9Y32T+S+Y9wva/zA4LPUR9/nAvWN4q0KK/F7D3SZ7+V1X80v7/OjlPWf7/ffpn9MV+mz3w2GfG26AOCP+RMC3T9A44/vfwOmKEA1vTu/THI8v/8z9k2dpuyLYNuprklYB/g4C7O/Ul5PYrbGfg35XbjA1zbGAD7HAfif/LwpHEZzH79P+6dJj+7T5qE3qjP//Yku28Psvv1daYDeWUTh3FhZzOV2e+/FnboF920VtX4rd9cAIs4Y+d/BvzzefoCqHH261+J/Haf/VqNv975MX6wkboUJyZq+8x/nawxI7946u4CrvUH3+2B4Kx07Qfbtp+AlW2ZXQCTTZa3aZxlMy9ugJllMz64ty++TMJ+/fVXx26jr8WDOtHZowi0EBjwrs7s82dgTpDFYdR9LXw3Kmcffvv9w+z/zv7ZrLvwaY09IO8n9kDDjbZTZiCX+hwMA24BjgREccf+t9+foAIxBahawFNxMFWhaTKIxdT33hDW1sznBU7MHB8gC1DNpwIC+HgWd68zMZi96wsWnR5NjB2VoFJ5fuUXnl+4I5BqA3PekSzKbtaCgGuD8dOsb/37qr86jX1XMQdJbXe/zrbLPagPZXavfs96ASaXRQzgf/f/4z4Q0nxoZ+ybiNeZMkXfrLIbu4oa+7lGYD/8AurC23Qg3J4V/vVrMZVAf4LqngoPeMAggIz7dOnnyeegQucg7732be37GHuqYvq9mjVfi/YZ5nYzucIFtA8WDXtQkgH5/+0ZUm1U9pl3xw9oOkl6esF7euUeg+qPdX/5Q3vATh2DBoiimn3tFzCCzf6/dBOTnowgqJzA6Nxqxim6en7gN3U+E86PZgmU9xkIokeufC/5b4TxxptfiywGwdCMf3uMvKP+HPPgIpDQHqAB9S4fuBzgN8m9R+QUYU1zx+Br8UbQnwAgdzYCJoD0BeE9ofC24PT0TdMI5Oh0/b1Y3z3YeJPpIOpmVe9kICIC3/fuIHRRM2XVE38Qnv6UYdcodqMfrJoB6SAKgPwZUCIGeQJI/A6dUgIzQULdvfA+PJ5aIKCF17tAW9Ba+q8zEyTGFBwtyEbQx0xjAAof7qJmuQ8wBiq+I9xGdvVQZupGnwraky/KHMTrHz3wfPg9lO+6TOoDqTbwPcDyOlGq5w8Pz77r+fQVUDafku8+6Ud3P22d/bGS/O1rcdfxncVBTmdTEf4DODOQS3l7D7mJklpAK7n/DCAQCfd6+/oomY+a/K7Llz+14B//vS79XgSNHz33ZRZ1XdV+gaBH4XqrW6+AECAQI3Hlt99r2Odnin1+pNgP8h7wfJn9ezr9IOIZzF9myCv8Ck+P5Nj1p2h9fgAEy8/s+TM2PZ1o5LtvnwEw0Wg2gqL5XlPehoDCEjZ+OA1+1Jh2Kk1XUA3vpArQ/1q8+/+ZHQ9uAQWxLf+QtffiCrz5cNY794NHRQfW9qbWK/Sn7Ug2qd/6L1+KPss+vRR27v+zbchE7CA0AQrTrgWkCWhhuti/X723M9PFj5utewKBzPfKL1MefZpNreen2XsX+Wn21tfft0hFDzY2P08d7LQkGAp+vY9938k5/gvYQXVjNWn82KxMjdOzof2zElP6AI1dfyrW5Xs+Tiv+SQj4EoZ+82chu/sXO3uSQtvZU+mNu7dUboGeXj9ROPAZSDGQNYAMezDhz8uAdaZoBTXOm8z9jt93s8qHLb/fYegeO77fXt7I4emDZ3cHhoMs/NxOVQ4C8QkWBNePSALP/sd933MeoDHQf4CJwQKlSQdf4CjhOqTr+C7skDYd4LBPw7C3IGiYcnEbJvDFwiUCBPecRRDgJII54DG6APIecfhtKuHxpMvCtl3KBSM8mrQJ10dhB3V9ZIF4JOrDOI0GFOVjAJb3qSngwKeBD4Mm9N5b0AmIp52/vTgEBkausVZkHp8lRB9tCJUdJZLnJ3jOnqH5ATWqcdGfib1/pAzaQ9wqq+B0dHuYXCMBy3DV5mBcVTlcW/C6hWAxqLnAkkkv5LWNZKS6ifdOVQ02njJ8eaEpf4GWklgKDWLs6UDa9Vzt28romoRUHcljdtJtfic3u4YyM6o5VkHSZQjEm8ciN7M0Ug1xZZt031cOr4VZoSrGqbdvW7WNloQktYUTYYUn3gq73/TKsZdNPG2S7eUQ2VbNjf7mJtF8c+41ZIcvzAime30zYm1hEVR/ibjTDZnTkMDlpxo+kj5uYGetRb3KWOQoD2f6snGMY60NWVkoRNRQ7qbzM88ytRwR+hSuzAXszcW6UPWtwO2KI1Lp8kD11yzGfcJgTRkxsbxISrGJy8VVCJMliXKi5l6HclHLUh7k0MGuFwJrJa3tBKqrkX1+oS4SKkVLvs6X5XGjWye95SzypNm43h4PNQbtSEVTU2cfLHmuPldO5BGo7u2wOYMLldyGhgEzBOSE/ZmUC3Z+ro8dCpMC6M34vbMnIpVoMjOzepnsTlpch23DVaZj4vUKw2grVcJysTo73dlGbCQjdGNAbna1aRvI0iSfONa+mp2BnavbTatWJrcMIjvJicgzZV1GF0V+Q5YUwaZRf0abPiNp/HqobwuylC3S3qrEaJ0s4bQIKlJmRdIzjQN2NOF2QPw+XrQNktvJobkxFGH3Rmg2y9N6s0Y6Hm/D9b6v8a3nbqBIWWfXOoIY1bGVeL85EEW63TaFy7SZvhBuawgOdONkzz1pd6Nw7ZRFQucoRrPFD4ZeGl2ub5qToSx1HVl6+hEf0Rs/UgVseUuNv+JzWV+c9xaDDVSNKHyoFnMsSAqYoKF8RXKiyMY4vQ5dGERKWaXSYrAJT7bShSXJvN9oNVK67bhrHWWMoYTfrs5ZjdF2g7kttY+iDcquN7ei2u1Ujhz3WBfHW26wVpG7N/OzjfGn64lxK8H1xtRSR9lAObRMFU7J4KSoJTxeVlaWKSZAtkhia37ZMCAK1sORxgKYOke7MeCuh3zwKBGTmVtekmaQHgQHx/OFpRGoq+0xD960PTLg9tVRoSE4OCd92BpWfeHnhuL33onP20tUJqh5wfyhc1Lah0k0jIc060JnZQ7tMuVlqBJ0vNdSPzAve329aBXlFq70W9IV83iZZlUmpGsTktERJCTUjui2QbZOAJF8sVCOma/wxrLgoY1ZdYVW3qrKxC260dTQ3BEohnGJrB/RUNN3rMzAniONknBrnPJydOoDW6uH6gIH+1LCajSFVRv0m2m8lY2E0uQuTLaDTC+jc3hLggiFMCnAlF3dSKx3QWv+uC64+KzBy624SEWTIkAQgh61WwgcoR6IFBmYzvPxDMTJbovJYqNs5COfB1I1ZIZCFEk4Z5VqP0D88VhTWX/bzveef1YQow+ogKA2MSekJyW0MjRT9lynKZmHKGHRFTlN1aUbtfNVTBM0QnaHub06r5KKWqTcuqgO+i2rLvHVilbYqK9k1IjGMSgtfZn5Wu3qW2eUEiFZ+amTthTHoAWI12Z9PSwwV1V09ww46FbVQwZ4ERSmdOHnsRzcIt47cwfhfCAXhrk4cBdKIBOXL7ZHEae3XkTo4QE+LEQzAD3exTy3VCrEJTN2giQm1/EqJUbG97GskOdrv2Uq/iAimixnFqKaiVdE3l5Y234nSupuwafmQTak3fo4osU+1yzJwUV951/kDoZ2Mo67pw0rGSMfK+0CgwDTbty9hEjukOuUxJ6lzaq46TfrRltX5UgPJE9vJUacBxuWuqyi0wBE+MHmOkJH/iZyWhYanZtIEkKRqzALOX8QtUPXrduLK5Ub7nK81d0WY61AoaHtNVtmV91dCXBeXgpsA58XnrYr2BpE8vYQg7jCN3VuaqihhwJiYBt7Nd9xxJrPEllJ6nDJYbxSVOGa5XFkc1wau5soFMt+lSO7XAFYx1UZYuJyjPA2DRk1aNVr7fbbNUqdhsOhlbAFbrsbp1vChNVK3sK+eN4Jo5AqIQ0zatanXQtV7DpIeBm75jfhxOprAVO3c4H1wmDuCA7voWcq5bIUFmHKYaDDwA+nNSJqKHDeiYy9UDcs12o1ygwTGQ4imYlu/nBQBVkh6vI8Rw083HLmzsD4LVedu+V2Xu7gVmYv+gbyu5PNIuY26LTiRHlhbAoXuR173OOQMXC1ji1iSyTXC4MNso0UprlUYc2yxXbGUZhvMFav5wtW2AL4eN2ztnajrUTb4A+Wd3IRBKJQVgKk3BhOp+50P90cgrN5WxbxOWDP1FFP25jUPGu5DlaHMrZPu8OJuZwspBJhzE4LI5azHWOtDpu9uSpNEzptarerBCPmx8OAjMv5BWw/udHwDDiySm8euQxSVBFWRgFox6pYGKRTc2Ai278JG5+wqjpLCSbo0b4oj/ER8hL4nCw36M1saWYfBBd3uYwU6nAdvAAmxNFPWE0rUT0WgkY7SfwtMK/MnPWOkW8Lm1O2Jllna5L6FuFlrj2cyXi+TWpIzNaMttuaeTNCfC9fFomk70CHNi0N77v8VHmK3yXpee5vrqy6lbMetlBYpol0kNZWa+3Wl2ZOLvzLNTdWJQILgihgDIIsbM5V1zLc+/SmqjbbLitwxHHkjt7b3EWNyMKuwgWJ7ExipavlyDA3MkCNUpQi5cC4ooBc127P99mFuS0iKtrGuVneZEUN9kWMVVe7JoX2sAydjYD0zCaGOQqCz2uC7cQDUiybql9VuiuPUGvwkmdLqJwn7lifpDo4ovvOxBYJJQzYmuVkHOzTFHZlpnkhEudbqm36pVNxg43R/FbFN3GQ36qEMQMxNBYba6fmo6pZeArVyknW8JvlCZvVboypMBixCjob6IqjCt6cZ1ZQKn5F6yx5jYdeo0pTY4tU4OzESvKdbx9cmDEPCZVQ9WWsM6dydyri4qKzXae1kBetekQtUqRFQCqHmLqWrrJbWHpUSCJcchtn17TX+Hg6rox+9LOTiPId112aGt7ltGq69RH8mCAC16R+w5a9jDQcfts6Cu/4pWYncVuJzglC2iIYUyMN1mdSR+A6pR1T4rxrXZR5EbgW1VAoo7LBsl8r/HqNFedM2FzF7qCwB0wbdi1dEhIbtrgQR7ueVo3crYtBuSzXjLw7r4YKVAVt07k3Rfa7vXUxbydK3jf1DkWvg2r7kRYJA2ESXC3G5qGzS4W85tcdBbMLYXnp2LFdenmvbwsLHjZuxhCeEREqn1KAQNeyrFEinYc6hqy2t1a1WtUtIzNNWPcg5jfe89CbVx36sw9LeSZktjOv3R17u0DG4EswF65x6XYzxrmPc3MW792VxHGbW6+EEm+UO+loKPmgBHESCsUpkPzVgEbCOrxtaAY+80it4EfMVIiUpNFOqZc6m+xXF7O3+k1M4kHteYJUe36I9OeKX1mCEKBZttgy6yViqv2x0INqntiIt1u6jBsv1FSxguWgxt5eKnZdHNoaqP3Yebdn1I2wdgcWH8xEkbLVNhWRm0Fc2+J0hnr4oBznIJhYm7GymvfaQh9pbJnz4kGPNdAFFGYIZ2I9xF22LVfeAOdIl9xKUYuqUwYoPDvd5o6mnU9yzQfbs0gvVP1ojHEs5Z059znIbjvPlXy4Zxn76FD2yWWCxgVQeovLdS6zIFkEx75svGYhokfU70Yug/w1oyIk7F925V4uz42PetcQM73W54ghlXha3tEari4KrsxR42B7eQgvLIpFRpEsZHrVdz1LdTHq+aiJC76gb1XG6s9GO+ziDoqgJW3o8IFBorESId+hS3lRURuM2e6SXlzj+8LxllBDpCf1dE4hLTpOCl3ctcMOPbWS5pXZdvu1mlvzEy3HbKOvKKK4mPGC8vw9Eu9VTFAgyGlkKGQvbj3A5RmCBgYqjtfdKaTcOVSahSV3+EpVkUUfCngdlWOyVW1Ko3z4FgTLjj/RSwRnBQYhd4EmawKMkVS7KfI1xqVukKJxSBQVB43EPkETiaaXl8IfMaFTrCNmeOsQc+mUL5vcFSIoG1gKw8dEjtOcpSLLctQTwi9IPJRP10Xon9ZBu4dah+av6OJkyILknrprQq0LKzj6kStebpu0S2pG1Pfq8RTDe5MeOkyQZfWcYDAPw+ReNbsEOncqdGnKzIFMCMLO1JBqxyBXSWarbjja31e0txrhwoKCrapER5puWGzgO4vuBquw5kmF+Q5/Oa7mF9cQDsq8dAcKagsquFBhvoi1hLlBaO07h0OBxY2l6dzaIDm9ltAiXXPniybg2tyWI265aofIB1my6QlxfzVxP5LOa+mwwvCUXIvHw3l9lm12F3ghsU0htlFAtVcGpFjfwj0vDRktypiqssg839PYli8KCsm30Jwl0mWce9Zit2D61SgS4nY0MfEaWjm9bZWMiSjjeuQTyAGJhpiICGofVc/DtgradRDvLwva35EEyR26Mbu6eLWhTtRNiAcCZOAcsYoEUg3JlZrbuF+OuMMHTbwDqY4TBOx4WCqLLqneTHbp73dM6+/Y9nzeQXuUsxr2KljoBb04t8A1KdpLeidcSepZyVTyIvQ8eiCsEyn1QE+yRwmkV892dNOo49VTDJleO9fDJkQZVqOrJWCpzeWKnlOQONq+xedbucRt0Q3WJeqmY0NURbdpMmMZQgccjRmfo3uiExhi3hE36HLm8Z64kVhfdwReXpZixAb7pJjD/TpPA9gpk2AZ8NnxMpeV04AecrSOchKbi+b+QnnEwCAKOofUAEqPCZ0d0MK7CsQ8a9CtmGury5LfHlanqG6UxotE4+IN47YuUM7e5faFKhvs1BZQwsCrg6aHCdj1nykIjXvRVpb2DsNXGZ4Vcxt1FzljjjB8O0GDeqJ9cbsz5qt5dLW31BoWVq205VqFDLhcb91FtauqDrS7slR1NNpWPuiQUaw1DvslnCyJNdYfKgQPWczfr7CqsSmJxFkkX5UM30RLVm4OPH5hc5U/zisa39qhBeM1u91ellHbLc60tEwVUjLDhYcvKc9SO6glkw16VeY0xmiYrGD19QTpdkJym2reY5Qxvy1R30kFEyX5Y75mYHYbxH3MwrammOimGPXBEBEdqqSbQOLoeX7dDP3uELrnlYub/a1ltaOQ9xi0VJIqhpMrPyAaj3JuAba1pB4RVxzdUvZtgyFT9ZuXoLGBmM2ARBkxSgeGefn0Mh1HPw+V/+VL4em073/t0PFxPvj2Mul+nOzb3pf7Wl/+tSq/fHpp3Bgo8jhIbbM+fB4//rdj1M9/9ephmjU+3qtO77iG7u2MvbPD6a9/XuLC69uuGb+1ZdbfD3A/vTh9O/1FQvvteVD9cjcir6ZT7/eFwPcoBrp3JVC/i+834mJ6a+N7sd29XYbP0+RPL94IXBC77TeUwL/5TTVZ93yTMR3GTq8yXn7/fxB3IalbJQAA -->
