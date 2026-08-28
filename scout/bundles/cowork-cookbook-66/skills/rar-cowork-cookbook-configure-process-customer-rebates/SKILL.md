---
name: "rar-cowork-cookbook-configure-process-customer-rebates"
description: "Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_customer_rebates", "rar_sha256": "bee916b55162c3ade3b9c39a521b9f019e4aeda4412bf92278372360a8f92d50", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_customer_rebates`. The original RAPP
agent is preserved byte-for-byte in `configure_process_customer_rebates_agent.py` and in the RCI capsule.

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

Process customer rebates Configuration Bulk Setup — Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-customer-rebates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 bee916b55162c3ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_customer_rebates_agent.py` first:

```bash
python3 configure_process_customer_rebates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_customer_rebates_agent.py   # or on stdin
python3 configure_process_customer_rebates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer rebates Configuration Bulk Setup — Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-customer-rebates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_customer_rebates',
    "version": '2.0.0',
    "display_name": 'Process customer rebates Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-customer-rebates',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-customer-rebates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74fb36817befa894',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-rebates'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-process-customer-rebates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureProcessCustomerRebates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessCustomerRebates'
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
    print(ConfigureProcessCustomerRebates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaebOiyJb/KsydP6p7qLrKDvXiRQyKiCKLooB2dVSzJLuArGJPf/dJ1Hura/r1vOmJiRjuNWTJPPv5nZOJv744bRMV1cvnFwM4ObJ0siyOQIU4uY/Mi76oUvhVpC78IF6RN1Xstk1R1S8fX3xQe1VcNnGRw+l8WWYxqBEHcdvsPjaIw7ZyxseIFzl5CJCmQMqq8EBdI15bN8UZMqqA6zRwXlAVZ8gVifOybZDF1QMZEsQZ+Ij0cRMhnZPF/oPYKFpVZJnreClSt2VZVM0rlAdcnXOZgfrl808/f3yJ4fnL519fvMyp4a2X+VMgoD8kmD8F2D34w/kZlBEOLAdokBxel6AKiuoMb/kgQJ5XP9QgCz4i//Zvae9UYf3j5y858jy+vIx/uzZHmmjU1akb4COeUzpunMXN8IrwWe8MNVS5aat8NFUN7ZmHr4+Z3ygVJfL38dkPDyavIWh++PJSQBHuFvjy8iNSVJBf1Y7nryOV8ocfX7OiB9UPP36jU7duArxmJAalfv36vH6ShQO/DY2DO9e/Q6oPv7rgy8vvlBuPh9yjnnDmy2tSxPkPD8LQqx3IndwDP/z4Z2S9CHhpFtfN/4juTw/CEXB8qNNT8B8/3o38M4I+FXqn+edsS+jWv6IJHP7G7iPyNNSf0b7b/7+QzuIcRvObxf8huX80Af078tOf6vbfTfiIBF9eBJDFHYwONwOfkV+/Gvpi/tMH/9vNDz//Bkn/UzJG0VbencLXs5PHAaibr19/+lDfb3/4+acPbQljDTjnr22V/SOa/8iudz7fWfA56ofv50L+hzzNiz5H3iMd+bUo/6X67RUxx/T/dr/+jPw+X8YDRUYl3pg+TPC7nKmhrL+z448vv0GIyKE2rXd/DLP8X/8VUWKvKuoiaBDDKyAMQQc38RmMwu+juEbg/5jbFYB2rWNo2Oc4GP+jh0eJiwD55d+9O3J+8p7IOXlDQ/D1iX9f3/Dv6xP/fnlF9pByUcVhnDsZsuN1/UvuhCBvRq5lBWpQdRBP3KEBnyASfRpPIFoiv/xz4l/vdF7L4Zc7eMYPhNrNVyM61W0GXkcNrQjkT308CMTgCrwWssgKz3lAcf0Ral4XWQfRbbRGncZZhvhxBVUvquEBzG3+eST2yy+/uE4dfckfcEogj1pRT+CAd3GQT5+gYkEWh1HzJQdeVCAffv3tA/IfyH8360585KFDZH/6A0q4NjQVgfnVnuEw6CroXAged3/8+tvTvJBMDmsO9F4cjMVqnAzjMwX+m60Nif+EUzTiAmhjaN/zWF0gRiNx84qsAuRdXsh0fDSieFTUDeKDEuQ+yL0BUnWgOu+WzIsGqWEQ1sHwEWlrcOf6i1s5dxHPMNGd5hdEmeuwZhTZWCSrZw2Bk4s8huZ/j4THfUik+lAjszcSr4g6RiRSOpVTRpXz5BE4D7/AWvE2HRJ3kBz0X/KxPoLRVPf0eJgHDoKW8Z4u/TT6HBbyM8QCv37jfR/jjJVtf69w1Ze8foa+U42u8GApgEzDFtZrWBD+9gypOirazL/bD0o6Unp6wX965R6D+p+1B/Pv+onZ2GIYEEZK5EuLTzES+X9uP0bZ+eVyt1jy+4WALNT97viw6dg0jbZ/9FmwDUBgYD3y51tr8AYsb/j6Jc9iGCDV8LfHyLsnnmMemAXT3YcgsbvTh2EAVRnp3qN0jLqqulvjS/4G5B+hae6oBVWAKQ1DfrTHG8Px6ZukEczb8fpbUb97tfJH1WEkImXrZjBKAgD8uxGaqBoz7ekJGLJgzLo+ir3oO60QSB1GBqSPQCFimDsQ7O+mUwuoJkyyuxfeh8djqwSl8FsPSgu7UvCKWDBZxoCpYYbCfmccA63w4U4KOQNoYyjiu4XryCkfwoyN7FNAZ/RFcYZu/70Hng+/hfddllF8SNWBvoe27EfA9cH14dl3OZ++gsKex4S8T/re3U9dkd9XnL99ye8yvmM8zPNsLNa/Mw4C8+tc30NuhKkaQs0ZPAMIRsK9Lr8+Suujdr/L8vkP3fsPf63BvxfLw/ee+4xETVPWnyeTR4F7q2+vECQmMEbiEtTfat2nZ7J9eku2T89k+47yw1Cfkb8m3XcknmH9GcFep6/T8dEm9sAYt88DGmP+aXb8RI5Pv+Q78M3Lz1AYQTYbYHF9rzhvQ2DZCSsQjoMfFageC1cPa+UdcqEfvuTvkfDMkwfewHJZF7/L33vphX59uO29MsBHeQN5+2OzFoJxJZON4tfg5XPeZtnHl9w5g//RCmbEfxit0BzjygeaH3Y/TQzuV++d0Hjx/dLtnlMQDPzi85haH5Gxa/2IvDegH5G3JcF9mZW3cE3009j8jizhUPj1PvZ9XeiCF7gKa4ZyFP2xzhl7rmcv/Echxox6Q+exSj1TdOT4ByLwJAxB9Uci2v3EyZ44UTfOWKHj5i27ayin346oDp0Hsw4mEsTHFk74IxvIpwKXFpZCf1T3m/2+qVU8dPntbobmsVj89eUNL54+eDaGcDhMzE/1WAwnMFAhQ3j9CCn47H/RMj4pQIyDDQsk4QLAYbRLURiNewRcNxEu5xGcQ+GYywVTjAOkA3yHJDHcDTgcZ1iCwQl66rDwyqdGiR6h+XWs+fEoFe44HusxGOlzjEN7gJi6hAcwHPMZAkwpjghYFpDQQO9TUwiQT1Ufqo12fO9eR5M8Nf71xaVJOFIi6xX/OOYTznTck56osw2aZ2ikXNmBn56XTa+0hEheBV4jTHdW3wDp77bTMsf7Kt4lklIe2Zo5lxewlli+o9aBPzWIlbee1HMT8213jtXHynQqm+Lacpoah5O+pJTKmdrAOnv4JVqqw2W3N7Ph6Fwy2zU0Xy1tsptj3VXQMzyrWLRTOrIaWqOfxvJ+7Qy6X7CMVZtpQa7Qi62YLH6K1XRt78xmSnldHZnyyaHNmXotOcwhlNIQKfpU8dXuvNkoJ4lMXLGzy3x5m4KEvdBou6lYOiAYKnIjlu1uF5TKyC47phGmmQtmjTkcLJRXczPtYwKLZjMs2ezXe0JQ+yBuKqc92KubnNvWsHSZi+GlirFaz9XKa47Ty1W1KdHV7LZecbGM4cpEOoa2tK/n5XKJ5WXprlu+sr1L7RiobK9dhnfbIpGm1uXgDURzrihhz4BLmlltIUueyps+IPe5a7oXez6YcpegbjjVZmYbKuXBOMV5iyVlwHCYFErabe2Tc/4cSwFKXi7asO4D/JL5PrcjB1cNq1zEp5rmg8thr18Js6CnrmGKp/Ry2xE7Ui+TU7zF51XR7EosZszKsqPNntjMirTbdWoym9poO62z9VYqSdsOY2PZ9ul+jkk+N6NNJ7SJUvYDZUEupJWA2e2NWdcEMZsznXsO/a4r46W1l7nVYDFsfdq6ApNs43xZ4FmHV5hqqaLVkI7O25ZKT/cOHarGErCer6VCGoc0Rx+9qxp1k8WwV0RzQso7PCmSW6oZXhImHh1mtQPC1ptw5ykm4l3uJPVEYxvqeGXwmy3ftKMq0WJ1qq9R6kTVHH6E8ftST440HrYBLErBlplFIIg7/8zUBLiyla2JblagvCrai34yIRh6tTtJJg5TA59x+0MVxOe+clWmwJvzzVhvZMwpd/Kw1vDDDjfPk2gwk2Xh7CcHK5gseBYtuXAtqMrmwBTa2Vdh6jit3GoLGHaZJxlRb5GiPJxWvqxMk+3SKVt5184mu/VOditUPA1mnybOrZKPzS2K6nzBcGA4EnO6C28ulZWqQmjSMu1310pNt6dbwmubYpHEbEKXSkJ2jYxt2gORLFyWEm2gZKrfa9p+kq+HxFRJwXCEgCrUawfzN+YI+0hvxViN6gPeyVlN+nt2SzrDdFDcLahSSWclca9NqsPyCNBe4kJxGRiSdrakNpaPGWsuG6ASmA/0iQGTYhVrVVDOrhNOM01VN8lFbG+21XS4lfsO4/KtMeF2spFb5ZSsugQkfjOzwG61Xk78/WXXZAfT9afNwcx7sYg47EDdFq6espPV0mMHx7bb1bBdl0t0XWLQI6tsEh1kQ4yqGRmQosIuyb2P8W03jUV0UxxIcrgurmETLrqZagLSavDi2O/LTFkYEilgmWzn58CiKznci8UUFFnMaNpqexXmKJMMUjMXtRM5cbECwx2MQrOtbWciU+8PaLmqr0o+91bUrjlcN5F8XV8CTD/s8Wrjt6YITNzS3YrjHICCXTEBKd/F7s02hrViiuu4yciJYhwCy/AAuJx1y1F58XiiBvuWGCvscKlPIfCsuU+FopSvr6s9M7Fbfpu0tidqPUHcrqh+1o7iosayiVZevKqRZqSkLO0QDfn2tj1F7Jk9xFnCnI/YVA/1MG2NLatuiqg6Vrg5PXEDnxZhHGZH0iyNWGjWlgvSprjSjY+qW34TEh4s1fLJ8g50t2wVFSVPDGmeN9vTmZ3GPo3N6eTC4IJeWabjMKtbCzoXI8lus2bZNjbsbbZZOD5HoPqFWfRsapeJ7PI9JRGrog12bnm6cU65mUv5WSIW/Y4aFC/YVIqud1XaHdlbczKCiWYL5DyKDtwqsziG6itxsxK4WXLdr1LttLHMUnTMVZfdys6gDQK1RG1j2BdXMkhR3KjXHUTby7W2Un+5P+SDF8wW1JJZ5INz2XSYltp0nkkUd2o9A78mCbOOZT4OsMte3e/by0YKCTM5KAYuZ/N1Sci64DV1rM03ZkBn1a1kZGvWLmdMGmqZEgCdIvXLonH9pj0VuG+Fm3xX0b4zbeYT/YxuZ8pGgnYhdqdDRrQRx5wTyRZyfrpptcorJdwqIrrbkIHRu0Il6oWWmldZnFHS2isWXWA6OXqMecVyzek2OCtnPO1IKhr4ag/KrWNuVLq8HFDiQOVeXyuXq9uviXLFxwxAjb4u3cyXcwzF/KMeHFtC0q57GmNVxlLyQ5IN1BLHOq8JBV2z1lVCmOk+lBW+beUNNAOx30mxnqAk7Vuq2Q1X/jwch5tqHVt80c1xWGAzzO9tJxi4grjal0wIDxaPXY36iO/b8EIadnjci0dMkpu6ssMdO8fkWYtVxWInMVCXlevtnBm+zkiY1v1g7KcpLU06s3XTgt5mtQhIxeCjmcBU0UTLpK2iLS2BKHJP9YcTekk9Fq6yTB6/Dpw3U+09fbwIRGKcjJrYztGWSzljZcyl+pgcTqHWAk662DRzWUjZag8WfGHmnJZ4RDEcwljDi6yDldWaZ0SfTUP+atn7QsDifUNu2564bfKpBVethsnr8xKc1yY4GLNwtT3b+4zKdxKMxtVpcTzQ80mRs7pYpSSH5xZaUCIhncFWwaXB9hWWXlmcEWa5wpD5nCAIbqLnR1uYOc6O34ZLZnXFGGdJRJJU+yi9t7Ol77o6Acvd3qX96cm6SZiSmLOm9/12KthCxM4O0jCcCX51ieot7/XLoj8APosznUfxaIiU5DwtMFfdoe2tpLYWdjrrJ16yl9nsks+3t3p+vNGcRK/r1RbP5apsq3KrbIZgEs9T0DCuWe1aypRNdXHq9cYgJxK7nvKa2NuEzWZHQb+usoSng026VbvBbRe4Q3LyrveauV3GOETiLD6KSrLcnDElsyL0pNLhKZnWB0KYUesTusXS22CJ3WQuH+2VwR4o59omBX+oLoXpLYrT1c7k29ZSdqjrncr8Ukv+dkhX2xms++BSSrS9SX1HGwAuOlqGr4VE1pjwJPmSDLuF6CzOMwof5FrhdhbOJ+5p6uOL4XK9tNkybkzqUHeHU7qmWY0AfHWST7HpdMcNJVGrNQYhanMRxGbu+sPMO2iubE52p7lCdF11UrtmRx3p9sqluL+ZrVxVlFCouzxsmAyuKq2jE4nlmiD7SAfpZFEAQ1jQYjvYi+1KZNrl7qCa0sk6lOV1anH8INtLmp0FfBYlehsCercQsWo19Yd+cvHNvc1KWhUDQu+vwLHieptcOAfjzcVOXlmNRXG9QWkDuqt5MXf2TSjKa/98uiTlVGPl2ZQub2Es70jblDXb4sgtpy7Ea7IM8mN+o+vZTm5Uat6Ve0lxSSKQir3obzlyd5gfEtNtLsaKb4PJEWcPR9kI+ETbJGsKxConKM5RkMnF6larES1uC002D/75utnOs3BZ2frMhmHWJ3PyBOsWvMsQEhtDf6OJNoHQI6fZdoUOTHax3Njy2BUo8Oh8ye1w7lrKduv4seRjC084wqoS39T47Ehx6pBS5Cy0Y5Yep/sVKeGqW5IYlZ5MxbCu/ZhXykxJj+ZmJXUifirF1ZqNpBM4W9mZZixxOgezk+2v5geep93Iptfc1VcntVssyhkwNkkicm2wX62PJytusHXGbyShn5WMtN5dnSLXL3OBoaNMMueFUhvkPKuI4aCfUhPDhOEwwFZyczXtm4G5LBlwF1Xoj5mnuLdOVkS4wt6irElOZhV1vWi2CXKm2xXgSi58hs1R9jxPsStL2S3bbYojw+EnMiRxrgEL9FaQMm/lxCme+Fpk7s5n0lHzxaA5Bl/vFt2tQAGT+yVoe6ZDqaJO+vxgR+IRuOl1p8w7PZpkTJ+vLqfWzxh+omCdMXGuVN6s+mVGZpOtfpWybLFP0kauNzPqirrUlPQaQVjscKk3J7OewbR+qiZcfkSZ2TDMgnxNWzf95hIds+8q2khCFuMm6C6b8G4kM5t9RF8nsTugRcgdBLqiqS3KpYAV1aN+XKJbppkeUsNRl9xagL1kiKI4WOv0XIedtHBobXUBFLVYUwwlaNv8KGUyleLG9Jqf6htJEX57zggmnyjCwticmsMkN6dAiOzq5MhYzhc6BbaBDLz1IBj7+WRbr+qUQeOFyt60igRrrRO3sPuNKzbrCc02/NvibHdXXglyd8txoSeHFG4512wluHq5sueo5vhsQKradr9zb4V7WTHqIpn6eXGQ1Gl3oRzORbGEmSz36nHq7NHZqZ7LnCKlApuXBwmA7uKdByi0mbTxZrESqnmr3RTG6r3LZkubdHuO5/1ycmhJOic2qK6jB19aa9sQm8D8VNOVT+4wtlnEUufFK2zBYFshZu1i7bfBtSJ3worZKsKEU2Y6Ecnh3L5N1zjPeClQTvtTvzDxORtz2zPRNv5SCCKTUMFiQJnbGZZ/Ue6zOttvo2GGOUqA5wE8Jhxu3c46xvuDsBUIm9JvmjlbL8AR3xXFIhOacrvAl2zcLzeFPHCsfhETPyrCdCqyOXXL1LUecR3OFYBxGDFsrnnvcRQz3bLUfn1sRGJoqWzKS7RjyyR2o7W5xhViEbRaU9lDQIAuXwStKCw1N/UXK8NeYCEDl1yVo/DE7OYIidelx853+ZIKb0K7YRzYPkPgcYXu1HiVH2UM0c0nwz6xGMOnUTFJVQ6crHxFtxzsJqzbLaaSxWxtBlO2L+mWoRllP/BkLuEFJ5mGF6SctJ+eU54yVTMBnWKkm+2E3DFwiRmA7nATrlsUZwL2cvSphmYmGWgtFJUVQQl4fTK59jSEh0gkA9aqE+k8aSb4IJVDfmiXVEHVQRfp15TG1NYL3CbvBlsf5ichyLg5o1/t7nKN1/yJLKhhXvWzPYmZLZcdUS1fHRyWvs1C39Z1odtdcB9d6Tyn8IoCF/0YxsKMEsIi0jYHkkuKKXFja6Z1zdnm5LrOjBQPhWJbp4Re8MFU2ewlHg97v5yFZlkwfd1zgkbMTHkgFuZtCZpWt5OqPYCbpCQHfjOTdhMTrqX0gwKInOTmMVPFDps03JVazaf97BD3K6vtZ/0kkQV5yVZqsTxCRZhhzR8CmWt25cGjup2BSRtiI98ETekyWF0Ibx0w6DDT16dAlIWOImxdjdxuE2kZ6ZVVLl5u9moitfQ83OY9ujsSpnGw9xddDMB5kinCVjd1NJZUpjr7AgEz/dovhA2f7KMjExyWq9Q5zeZzE0fzxZ5ZWDYmWs7sol/307VmJyDTToQYaqQG2p1AE/up1F/ABfUaOeT5l48v4871c//5L7xnHvcD/8+2JR87iG/vou5bz8DxP995ff4rQv388aXyYijSY/u1ztrwuVX5XzZfP/3zdxjj/OHx+nZ8bXZt3jbrGyccf4H0Euc+nFINX+sia+8bwB9f3LYefwxRv8n6clfsXI675u8s4XlR+VD+pvjqOXX0Mv5QYXwPBPwYcn5ehs/N6I8v/gD9E3v1V4KmvoKqHNV8vhEZd3DHVyIvv/0nb4MEMuglAAA= -->
