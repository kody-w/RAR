---
name: "rar-cowork-cookbook-demo-data-define-customer-classifications"
description: "Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_customer_classifications", "rar_sha256": "86daf0e1799b3a45f367fc9d833c6d66c07015430de796f47a2e5e90f80a891c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_customer_classifications`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_customer_classifications_agent.py` and in the RCI capsule.

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

Define customer classifications Demo Data Generator — Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-customer-classifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 86daf0e1799b3a45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_customer_classifications_agent.py` first:

```bash
python3 demo_data_define_customer_classifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_customer_classifications_agent.py   # or on stdin
python3 demo_data_define_customer_classifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer classifications Demo Data Generator — Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-customer-classifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_customer_classifications',
    "version": '2.0.0',
    "display_name": 'Define customer classifications Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-define-customer-classifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-customer-classifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4c8de195b9b8a9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-customer-classifications'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-define-customer-classifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineCustomerClassifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCustomerClassifications'
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
    print(DemoDataDefineCustomerClassifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abeiSLruX/Hu8yGzDpmbSabs1WtdGURFQRFFrKyVxRBMMskkULf++w3UvbOyq/ucrrPuh2uu3AIR8Q7PO0bgby92U4d5+fLlZQ/sbCLbSRKFoJzYmTcR8lteXuBXfnHg/4mbZ3UZOU2dl9XLpxcPVG4ZFXWUZ3C5DDJQ2jWo7kvdEtyv4VcSVXXkTjyQ5vDWzUuvmvh5CR/4UQYmblPVeQo5uoldVZEfufZIsZpE2cSeVJCYk3eTGmR2Vt/X1aUdZVEW3PkUUZLXk8qFw2WUV69QLNDZaZGA6uXLz798eong9cuX317u1KGYIhRDtGtbvHMXnsyFH3lDKomdBXB60UN0MnhfgBIyT+EjKPfkefexAon/afKf/3m52WVQ/fTlazZ5fr6+jP/0JpvUIZjUuV3VAMJiF7YTJVHdv05myc3uR4TqpoTqQl0huFnw+lj5nVJeTP4+jn18MHkNQP3x60tejGhDYb++/DSBqHx9KZvx+nWkUnz86TXJb6D8+NN3OlXjxMCtR2JQ6tdvz/snWTjx+9TIv3P9O6T6MLIDvr78Qbnx85B71BOufHmN8yj7+CBclHk7mssFH3/6V2TdELiX0TP+Lbo/PwiHwPagTk/Bf/p0B/mXCfJU6J3mv2ZbQLP+FU3g9Dd2nyZPoP4V7Tv+/0A6gT5WvSP+T8n9swXI3yc//0vd/qsFnyb+V+jiSdRC73AS8GXy27f9VhJ+/uB9f/jhl98h6f+WzD5vSvdO4VtqZ5EPqvrbt58/VPfHH375+UNTQF8DdvqtKZN/RvOf4Xrn8wOCz1kff1wL+R+yS5bfssm7p09+y4v/Vf7+OjnCnOJ9f159mfwxXsYPMhmVeGP6gOAPMVNBWf+A408vv8NEkUFtGvcR/19e/uM/JpvILfMq9+vJ3s2begINXEcpGIU3wggmqOoe2yWAuFYRBPY5D/r/aOFR4tyf/Pq/3Xsa/ew+0yg6ZsJvHsxB3x4p8NtbCvz2Dynw19eJARnkZRREmZ1M9Nl2+zWzAwAzIWRelKACZQvTitPX4DNMSJ/HizFx/vpv8/h2J/da9L/e82n0yFe6sBxzVdUk4HXU1wxB9tTOhVUCdMBtIKckd6FYfgSz7SeIQ5UnLcx1IzbVJUqSiRfBhA+rRX+nDfH7MhL79ddfHbsKv2aP5EpOHmWkQuGEd3Emnz9D/fwkCsL6awbcMJ98+O33D5P/M/mvVt2Jjzy2UMmndaCEq72mTmC0NSmcNlYWmIxt726d335/ogzJwAI2gbaE4IDHYuitF+C9Qb5fzD4TFD1xAIQawpwWeVmPhSiqXydLf/IuL2Q6Do05PcyrGla6AmQeyNweUrWhOu9IZmPxgoao/P7TpKnAneuvzljhoIgpDHu7/nWyEbawguQJ/DOKeZ8EF+cZNGLy7hCP55BI+aGa8G8kXifq6J+Twi7tIiztJw/fftgFVo635ZC4PcnA7Ws21kwwQnV3kQc8wVjexzJ+N+nn0eawH0hhZvCqN97BswXwJsa93pVfs+oZCHYJ7sUfitJPgibyxvLwt6dLVWHeJN4dPyjpSOlpBe9plbsPiv9NvzBW9slY2ifPVmSsig2B4dPJ/x+9yajETJZ1SZ4ZkjiRVEO3HuCOjdVohEcvBruDB7ExkL53DG/55i3tfs2SCHpK2f/tMfNukuecRyprSoigPtPv9KFgUJGR7t1dR/cry9HR7a/ZW37/BLW6JzNoMRjb0PdHl3tjOI6+SRrCAB7vv9f6J36j5tAlJ0XjJBBZHwDPsd0LlKocQ+5pEOi7YAy/Wxi54Q9aTSB16CKQ/gQKEcEggjXgDp2aQzUhtH6Zp9+nR6MdoRRe40JpYecKXicmjJrRcyoYqrANGudAFD7cSU1SADGGIr4jXIV28RBmbHafAtqjLfIU+skfLfAc/O7nd1lG8SFVe0y3X7PbmIA90D0s+y7n01ZQ2HSMzPuiH8391HXyx0L0t6/ZXcb3nA8DPhlr+B/Agf5Xpg/PHvNVBXNOCp4OBD3hXq5fHxX3UdLfZfnypw7/41/bBNxr6OFHy32ZhHVdVF9Q9FH33sreK8wWKPSRqADVvQR+HvH6/Ii0z2+R9vkfIu0HBg+8vkz+mpA/kHh695cJ/oq9YuPQOoIBCkF5fiAmwmfe+jwdR79mOvhu7KdHjEk36WHNfa9Ab1NgGQpKEIyTHxWpGgvZDdbOewqG5viavTvEM1xghs+CsXxW+R/C+F6KoXkf1nuvFHAoqyFvb2zlAjDudpJR/Aq8fMmaJPn0ktkp+Au7nLEqQNeFoIx7JBhGsEOqI3C/e++Wxpsf93r3AIOZwcu/jHH2aTJ2tp8m703qp8nbtuG+IcsauG/6eWyQR5ZwKvx6n/u+kXTAC9yv1X0xKvDYC4192bNf/rMQY3hBiV0wVvr8PV5Hjn8iAi+CAJR/JqLdL+zkmTSq2h7rdlS/hXoF5fRgF/RpAk0IQxBGFUyWDVzwZzaQTwmuDSyQ3qjud/y+q5U/dPn9DkP92FD+9vKWPJ42eDaPcDqM0s/VWCJR6K6QIbx/OBYc+5+3lU9CMO/BbgZSYmnP9jGAMxznkPaU8kma8V3OY0nSpT2adjEGw6kpiXmA4Wh/ytgEoACH+SxmsxzuQnoPP/02NgTRKBxh2y7rMvjU4xibdgGJOaQLcAL3GBJgFEf6LAumEKf3pReYNJ8aPzQc4XzvcEdknor/9uLQUzhzMa2Ws8dHQLmjTRNTR+0cpKT9wMjQpXM9dliKnUpndcYXpussZ6l4Hqp5fiiHxSpVlhlui4HnNl0u7lQuEqkwI/bojW3dYh2u5re6mjHADBEjnDoJSw2Vqx8lDOxXZhXuKpvRdROXh1Lj7Z46bZqVfMW1fkUIJRHyrZblyR5X+zxtSZrt0XBNS+c1qZm4u0K6KyfY0WZIao020/11iI+OdVwgcteuLpmcLvfd0aEu+mqPqCfTu64v9blsMCTZ9wfLKEVXII5xBAyM8LfrivYzB1qNXWsnhqYQkUqdwbH082Fn6WE7SM4Ra3r3uiQPa21zNIgjP6DC6Qb2KRbYitODuSHXgOloKtrX50iczSWq3Kjr05JwT0WoH7blaaZIUa0Oq6kjKFS5923LWVyKI6Y48oHC1uZVZZm5cD56lnPcMwsLk7eG5zpI3F4T5+Rt9Q1QW/2696bkdTeP1/l+eeEoLzC9pSCTcRQcS6UwGdmKK5YMtrN+T3fk6pzwM7ntacWU++RWZgE2P9VeQVz6IyWibWbsLE6ll+bGr5vbjShlMsjmlknnxmWK1jvFSiqeQGwDL3n61jdZZF/bUr66jIIQ0bJHcDO5MPYm87DrDg/FhcsaZ2p2NtfktsOztMddluGxorFOZZZc5wy6SzuiTNe3ptQ7rZRxQk9olIimwsUl8It0O57bkx6cqnLYO8vtlIP7zoFu0iHYVx3sgBBmfjxvFloiktf0uDopPhXrNDtfc5fBEebhtq+77fLgnqrqcL5m+MY0EAuJSt6rrAOSzftDks6JM3I69wWzu0S75CxkOH8d3OTgUp7BUrzB4nONAwfm0JNWSGdWgsxgQpFAF6AR38WUHi23li6iImpNUxLlUP82iNK00TUvWtz2e2fNxfSOoUy2VejV5rYCi9Lbk6Yqpl1Wr7r6oM6sLnIuYZU6ejytNwHRzm/rraWioE6Urpdb7erzhHlcuUs5xFKxPElrV67ozWzRG6tZQqWRUW2cxsMEKcpMbGepsqAbZnstkyN122Vxem5aTXcCb1EcoVIsMgtpypTa1XJa9gavsNlSwTdt7zVGuMCVeUBuXTqFGzxkX6nbdqeFZrIQUq5uWZ/gicOGmq+0DLcM6YyHDYInIaftjvZuM6cTIjyqimF5Gzu1bS1samu1FEjRIa9yzLUKpvim6e8WcVC18vl42clzeik1Ar+arwnBZ1uboqQV2U7565kGxtZHL6x0OuCn01W1eLs7tqY21LqDESV7YDermb6JQwMjL1npJItgv6qNqMAccxeBqFXseH2s0GOg7EzZztfojkXyq8D2RmKmVmP1S5Tbb4lrhIUbvzmVPbdaF1JFJehSSnX15J12ThIzrVr5hN2JYpaEJhsKl4C8Wh6RqJltDZR0I2Aic/HLNDUvcUTdZuoVTfpqh5REp+yyFLrXVCBKY8EOHr4kHC9dNX6v3s52wZcYilPLYyIHJzU4J5uTupVApmGt0J5XnipXtoczAcLxioNwyA6I6GbOgTruq6Vbe8mKrxTCq3erYNEFmezFyUXm+kTOpyl1o0Rnw9fyUrnonolSjrWcMxC7+EQOajVN+AVl2Mop7lAJr5o5uFKlnwxH3WZ4sNzGUhVKLt/QEbGnajZfTqXAhCGticNsuYc2cbblvO6Ek8mVrbm5BuZ1hpX7yIl0Wc5m5BFgy5Ia8HS3UfZQgkE+AkFa1ngxPZ6KgWjXkXwRbJys1VlVHhZVoQ0BzGzYRUlWpGFeCARkFIH6C1xbXmQqWVlTGmHI/f5wDkvuWHhlszeC3elk5JdhhqKJJGIaRcchKfAHc4kIA7MM3W0LKxBqrLkgQyg2X0Rz7FBz6vXoTDFVsGdHRgoL0SQAe1muZxeC2lUBwUO9Kwu5CXJm8MlNKHWnWp2CWi9tdWm7dLW1dUHQF+rlauPWulvIM3Y18IQmIbuM0xXZIBIplUI/ZQ6ktGarGCyuVYzMFcNXYQ1RPdcdCu4kXOmTGrXtwJqJt8/mB15Rbs5uK9dqQ2q3azrw3sG8DjWySneYGife1JH2/PpGOPQ+tOYZoAi6OWvOgeAt+bgHSDzU1CXPRELQ91xbcF1/pqspqyeL+VwwYslI3OKEkb6NmhwVBq2WHPpYd2U5ZkBvl9ht2Vhsddv5pw2YbUySyL1Bcv0Zjl1E4lgbTpOLDuoThdTa20sWSNGuPCryoAcalEyem2vY9jnIOg0LAZFKMs21syLM8zUm7sLFeenx8xr6WCukg3iGoKwO+Xk3nbVbW10nB0bQb5duS2iBiuni1gd+orGmHQv1VVgy4BacvYs97HXiSg2GPD9kSzNpJfu0OzP9ubeE5DBHwxVGila2Vkt6V7d2T2pgXijJ9azHFYmU16OgAzcGZ0PgMcvz7Nl2JzWs66VqZ15jp7LJAoPunc6yuS77lkCasxATWORoiTzLFDJPSIl2gKm2s+D+YkaYZ2WGWvPjgkj0UpsFuHY+R0y2II8DreNqlAaSYpQowePNza8HPFppK6Gj4xnf3YDngbgs5DO+9o7zI98aCUWvGzRjmG7tTOeB3tVbd+fRMs5J0ziQt3uiwhkmbegbp1RlAtBU7X0zmmbG1bcJEtSt7BdON4umGNs263ymA2k5F/gKnzpnD78sp7Jn+eu5e4b1F3Tn7YWz22GDFHDPf5OlXRNIbdH0yWk9dIOc7Te1tcNiJb42vLI69DVhLJUjjXnNQVUYah8aBxgqJ7u05O3llISstGvDGlkf5MJWLHE157lOPK4yPOWVwT3uLIYKzaJXkNlBc4T6suwwZbrCeuXErdRptMLx5kDVmhY0sGnpqbzVsyGGcXVNpjfGTEpbnPOOebaRpd6FqZIgoj0sVdbhJU3CwX4v6mdaWrChiYlCmq/oE3+pj5u9iZeKtChMRzq4sxN0oSAWS1YOz6RhNYaZbHswHM3V4ky4V9xWkLpQsNMKsC7vhKXD7HuH2p7ZdbHPd2ZQ3xaMPkzZcoWv18emvGrhMWKPYtVRg+NqyMI00CjodywYbK25YAN+iHiZuQzs0fBbk8sbllVddKahtqQk/cUKVWV3zsTZYR9YG8k9lQtsqB2C7vVLvTdbPTccJ7mpmbCA9dWL+fwKLrDM7ctD7Jn+oBXpiRW3xRWQxK3TryBOA7OjD1gtKpZczU18OkxFz9wtZjwcpMBs3y/sUCkqbg1wkT7wnt7R+rzihmsmlNmRDBhPSrsrbB69pGh0Ny/MPOb3mKOWmwteh+tVksGKvulXLtKf6+rQyUNFRug0MWcSG08pgu2xeTe4lCku9zqnuGtFF/hQ4fcFUM4Hj7T44+YcElbPaSwfb/vlBknP9MxfCrMStXtNMZpbg+E5tZQ2rILKOG2la4JI+rjeJWjdzSusCHNK588EfSYzvtvOTrfAtC8E6SyXjdZhdbXAEvSQacLK4CEq3lYhj8k+gD6ZLqYwlgP7EogdCGpWieqjyVv5uTopYV+CFEO4bC6XEZ3P5NtM3Ie32NU1saUZVhLS1VI3rjuTtRpv1mn+MbhAr5xP5djTSiWLd3Y6T1phI5RKmWV6u+NcgsmYbFhpVNXLJw0prqWAuAd9N7ds2hy4/EprOQO3UfkVA/PN2jqdbv7aU9iKw9qeWxNYJjHg6MxbHj2w5IrGNbaXb7RWluhUJcHx5ooJ0Jy4kCOyii3yZNq7w16acs2qyDs6DbDUDKqG1s5tNUwX8SXOJHLDuN5Z4jyF0xvjOA9m+kG/XKu57u83vYAi5G1NxbODVU+lqk8dxnJnPl0iMd/Z++am3AqW5nhz7h8SN+YigyOLorMUjZkNDsERCtX69XVtdMQ5RZOTDnaibfkLF4jWAnTqbTCn0yyjSxRhYxXZradKqRrIMKCSAbcRredyMwahdzqSgD7Ruq2lEEvPpPdx73KLVb5CWkeqjMZ11v5ltb0cDjGeMWo0dYLZYcq41So2REToZbV3up3XIcaWbsJpJfUNuSnnWV7xrYR7Tb1Y0Zo0qwZbyPuMoFDF5qj9AKReafT5/hyeuPnhROHxOuk72JQjnODAndJaL9tmWgrLvI36oZLaBG7FcX9Jkj3bc0sLwmgs6G23TXWunsriUsfqOaEOmGMsoKBlTpJrzKd7Z2OgeIw2sii3tLCmhZXNK2tlkZ2mp4XF1RTikINkWKpv2DNzo28YgaiK7AwTFAOcpD2KbttsxHWK7rUpYWkDohLIznB03gjOBIMvk2tvcHGipOtqHoHegJvWC+x43FbRKJsTxNuF55GzBfxlcy59qSw7V/M3rMgpPHs+nxfbZFeptxO2sQAX0JsLF5CmO90zcJe+zWZAmUclzZud2KNXdoeqwQ34flguKr+eeXvhmLQGgRCqs0hCbLeKmpsQ8rxKn63tfBkih+lRGRDU2im4SW726MD2SIDlXLVCKMdVHZcjcaJfOa3arojhlF+p1Jv3xA5VuIRcLQJw3UyN00Xyp8cuXqMnwRNlvNfwgGT0zWlX9DHNSZKPN9sKaHrlWpq/4KINfp1GFU2rqEio6VYH157RLL7HzBhmJpeobzWd+fqOcqcYaZOwi83NMCtIk7e1dQB4MpgCYbuZ7VRp7u9T/nQ5kyvMkg4iI2/74rwoj0Kcs1lLSTlCn2njykbbFUdo3C1ahKJNOlW6WHQt4fMeel15eIYyLoLQ7JIGMViLW4/ztdpi89YtuJhQWpDbfp3NyWu3k5gmQQaUuVSG58ZEz7jMjuHmKOKYayAMrcnEank1W1MUwLJhl4dupgLlitEas0J5txEvznGbKpi3wT1ufrq15hyVV7kcXBKebtqo69B2fjAwG5FkSuWPFJF0N9gsptjJSeoCCLjizLF9bhfsghMjbHpT841YKBLvX8M4HGJsw2zC09XZC6fcY4iKAgToBro67jeCVAeeiBy2F8S78VNt0bEHnLMlklqRqXiZzdN+zi724doQFmqvXdmCok18OeTxZnE+K7xInWpLVcRLzazMgAaUTmvV9Ao8EXgLXyTLgeXXFRx0wnbbkzKhGXvPKd2QyRJUtzE2awg21LSu4a1TYUrrlJSqpD6i9kXO/TxbEwbYemAtAQfrp4tsppIXW83OAlZsVnNiIa1Fw5sugvVwvaxXW0ljccRC1jlqUlXcaDu8wYkYJ4TFAUVmdC+IC75XdrPZy6eX8Qj6eZD8198jj0d6/89OFh+HgG+vmO6HyMD2vtx5ffkfyPbLp5fSjaBkj/PUKmmC56HjP5ymfv6331CMZPrHy9rx3VhXvx3F13Yw/gbpJco8uLTsv1V50twPdj+9OE01/hCi+vY8wH65q5kWj9Pwp1rwOi89qE6df3PtKnwZf6QwvuwBXmTX4HkbPA+Z4cIeGi1yq28kTX0DZTFq+3zfMR7Jji88Xn7/v1Th2SHxJQAA -->
