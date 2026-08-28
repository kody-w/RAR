---
name: "rar-cowork-cookbook-adaptive-card-bill-subscriptions"
description: "Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_bill_subscriptions", "rar_sha256": "b15abeb128afe3114623a32a1f6017e6be44d2bf758343a71df4313413037726", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_bill_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_bill_subscriptions_agent.py` and in the RCI capsule.

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

Bill subscriptions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 b15abeb128afe311…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_bill_subscriptions_agent.py` first:

```bash
python3 adaptive_card_bill_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_bill_subscriptions_agent.py   # or on stdin
python3 adaptive_card_bill_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bill subscriptions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_bill_subscriptions',
    "version": '2.0.0',
    "display_name": 'Bill subscriptions Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-bill-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd20239a552a96db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/bill-subscriptions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-bill-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardBillSubscriptions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardBillSubscriptions'
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
    print(AdaptiveCardBillSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Va+bObSJL+V7Rvf7B7ZT/uQ56YiEUIoQMEAiRA7Q43932DAPX2/76FpPfc3p7ZmYnYiJUPCVGVlfll5pdZhX57sbo2LOqXLy+qZ+Uz3krTKPTqmZW7M7boizoBb0Vig38zp8jbOrK7tqibl08vrtc4dVS2UZGD6XJduJ3jNTNrVntdY9mpN2NcC9y+ejPWqt3ZTpUOsya3yiYs2lnhz+woTWdNZ7+LaWZNa7VdM/OLeuZltue6UR7MonzmWk1oF0BK8wncsKIUvIMxmmdlzSvQxRusrEy95uXLz798eonA55cvv704qdWAr17e9JjUWIJF1T+uCWanVh6AYeUIoMjBdenVQIMMfOV6/ux59bHxUv/T7D/+I+mtOmh++vI1nz1fX1+mP0qXz9rQm7WF1bSeO3Os0gImRu34OmPS3hobgEzb1fmEUQOQzIPXx8zvkopy9tfp3sfHIq+B1378+lIAFaxJ2a8vP01mf32pu+nz6ySl/PjTa1r0Xv3xp+9yAKqx57STMKD167fn9VMsGPh9aOTfV/0rkPrwqO19ffmDcdProfdkJ5j58hoXUf7xIbisi6uXW7njffzp74l1Qs9J0qhp/ym5Pz8Eh57lApueiv/06Q7yL7P506B3mX9/2RK49V+xBAx/W+7T7AnU35N9x/9/iE6jHIT/G+J/U9zfmjD/6+znv2vb/zbh08z/+rLyUhDY9ZRuX2a/fVNljv35g/v9yw+//A5E/0MxatHVzl3Ct8zKI99r2m/ffv7Q3L/+8MvPH7oSxBrItm9dnf4tmX8L1/s6PyD4HPXxx7lg/VOe5EWfz94jffZbUf5b/fvr7Gylkfv9++bL7I/5Mr3ms8mIt0UfEPwhZxqg6x9w/Onld0AQObCmcx75/+Xl3/99JkZOXTSF385Up+jaGXBwG2XepLwWRs0M/J1yu/YArk00kdtjHIj/ycOTxoDRfv1P586Zn50nZ0LWk3q+OYB7vk2M9+0Hxvv1daYBuUUdBVFupTOFkeWvuRV4eTutWdZe49VXwCb22HqfAQ99nj5MlPjrPxL97S7ltRx/vbN59GAnhd1OzNR0qfc6WaeHXv60xQEFwBs8pwMLpIUDtPEjwKmfgNVNkQIabyckmmSibTeqgdlFPd5lA7S+TMJ+/fVXGzD11/xBpdjsoU0DgQHv6sw+fwZm+WkUhO3X3HPCYvbht98/zP5r9r/Nuguf1pABpz99ATS8FxWQW10GhgE3AccC4rj74rffn+ACMTkoacBzkR95j8kgNhPPfUNa3TCfUYKc2R5AGKCblUXd3ktP+zrb+rN3fcGi062JwcOiaWeuV3q56+XOCKRawJx3JHNQ4xoQgI0/fpp1jXdf9Ve7tu4qZiDJrfbXmcjKoF4UKfhvUvM+CEwu8gjA/x4Hj++BkPpDM1u+iXidHaZonJVWbZVhbT3X8K2HX0CdeJsOhFuz3Ou/5lNl9Cao7qnxgAcMAsg4T5d+nnwOSn0GeMBt3ta+j7Gmqqbdq1v9NW+eYW/VkyscUAbAokEXuVMx+MszpECp71L3jh/QdJL09IL79Mo9Bpd/bgTURyPwYwfxtUNhBJ/9P7Yak7YMzyscz2jcasYdNMV8oDg1RxPaj34KFP275HvGfG8E3mjkjU2/5mkEQqIe//IYecf+OebBUF0NoFIY5S4fOB6gOMm9x+UUZ3U9RbT1NX+j7U8AlTtHAdeAJAZBPsXW24LT3TdNQ2DodP29hN/9COADngexNys7OwVx4Xuea1tOArSqp9x6egEEqTdB24eRE/5g1QxIB7EA5M+AEhHIFkDtd+gOBTATwOzXRfZ9eDQ1RuXDqe4MdJ/e60wH6TGFSANyEnQ30xiAwoe7qFnmAYyBiu8IN6FVPpSZGtangtbkiyIDUftHDzxvfg/ouy6T+kAqoNQWYNlPBOt6w8Oz73o+fQWUzaYUvE/60d1PW2d/rC9/+ZrfdXzndJDZ6T1mv4MzAxmVNXcqnYipAeSSec8AApFwr8Kvj0L6qNTvunz5U5f+8V9r5O+l8fSj577MwrYtmy8Q9Chnb9XsFdACBGIkKr3mvbJ9nsrP5ynBPv+QYD/IfcD0Zfav6faDiGdQf5khr/ArPN0SIsebovb5AlCwn5fmZ3y6+zVXvO8+fgbCRKrpCErpe4V5GwLKTFB7wTT4UXGaqVD1oDbeKRZ44Wv+HgfPLAEMngdTeWyKP2TvvdQCrz6c9l4JwK28BWu7U2MWeNOeJZ3Ub7yXL3mXpp9ecivz/om9ysT2IFIBGNMOB2QN6HPayLtfvfc808WP27N7PgEicIsvU1p9mk396afZe6v5afbW/N+3U3kHdj8/T23utCQYCt7ex77v/WzvBey22rGcFH/saKbu6tn1/lmJKZuAxoC6m0mXt/ScVvyTEPAhCLz6z0Kk+wcrfXIEoPGpHkftW2Y3QE8XdDeAva9TxoEkAtzYgQl/XgasU3tVBwqfO5n7Hb/vZhUPW36/w9A+toW/vbxxxdMHzxYQDAdJ+bmZSh8EwhQsCK4fAQXu/cvN4XM+YDfQnAABNkJYtmcjKG35HoYgOIliFoZaiE/CCOWRtofjLmr7FEFjOGZRiOvjGILhCAZjFIWSQN4jLL9N9T2adEIty6EdCsHdBWWRjofBNuZ4CIq4FObBxALzadrDATzvUxNAjU9DH4ZNKL73qRMgT3t/e7FJHIzc4M2WebxYaHG2IJSylVCYG/B8GCA87Ai9OAiwXm22c2SjuwZDHPg2IvZ9aeAstkvtIzLoOl4uUde0GBlW/SZZ9FgDd/tyecwpb91b0koXcxdz88vcl+XDKeGOsUDpunppNm6XIJyeajq1vqh6jRa1dpaEZazs8ia5resbBG1T8ryrYO1ink6lVbXxSkQy2cDG+cJjy6vQV8Rh5wzqIF+jWpGgw/58zJAorRzCOHZOlBqmy8PRwPXDNvc4jKgH3cnkFezFMGpLAo16eU3PIc5zrgYC0dy2NqzxpCaIU9W42lTUqXTtc9q5Z0snNttjtqO8woL2ydixSHfmVv7eXd/2zvXKaeehysWD3JtHsvJKtfSEaLEV1iqB1kljVPtQk/d90KkwovM8ktSlvz+HB5PgrPO6c7TslHWNXYyUYcJoFxFDtCkpcgsfxsrwrF0wNhrjrnaygoXeQKTSsN6Xh529Oxgqu+T9BSape21TUUiTke6AL0dP1y9MUxTsle4aJGxKhyfww5CSxoVi7bjcn6qcbbUGbOXYxsAsJNs1xQUzS/2iE9UKxxeX5BAU6Mp0W9NCLCTBtdNA3Kxy19TQZeRKpD7h8b43YtzIq5Rl2+2JzJpyH+tIsNAWZ5ugU12e085+mwTjDrHnHYXsaKUiRnxfjU6MJGg3inUDqbeYOSAXZa1W2DoYD7K9rUnEzHBspI+CnFGluN732cCeIXupX6KbvFJu8I2Ia96fC8WpSR1ZFHX+eokjRywJeakOt6VgmXRID4uFQWPrrir2EgEduJQ055tzaMbmTdkeu3SH7HKk1ZR1T5Zn1Vqk+3K/uFwslphn6MVlNZIh5oJGrzc4y8o+mShKIJeQKMqXhdT4ZQ7xuBSylHarfQvaEetGsXFDg0XS2l/WTn2qkKJJFImO+EG5DDG/btTW9FuQyuiFbS42oR6ZZS0l6X4Y17mUQssBS6RM4MwRlKzc2enEsZivmGVTjGEFx9J+2GY4v+BCpuwa7uwvDUZNhW1RVgCXyJR2PA2lSraGoZ1xGyll0KROjHa9kmhSlMcybxQMtqVTXNtemrzyrXWZO0oD85s+oilDOGuVdoZgB5CsMnInfw8BJK3FxXAyfZhnhcjt4xDSkUQ7W5rZgfVED1l6hMX3fOlwhHADJpwQDa48R/QK1jzp5xOvjb2FVYFDl2iql5zhyxjbbIrBcu05x+WHK2gkaDo+K3Ycuk7V++N5b7tw3ZDWuWuwVlX6aKzauXTbIjDq4nByK87K1UrhiidzOixIzFoi5n6/dPNqCcOyHOz7mtHVsdXSQV9uqEpBlMI3TtvBXtCkGaqxqRZQcRaPvHVSjnk7z4wDQePaLbolkeKhgXrDa8SvxhQjzcIv11ymGJwId5cyHWpDOjWC1B40YX9ViR5NNsQZ7jo1LE7DVTYID8m6G4/Jw7akiePV6C2KXtRiJh5lxs2Q7Mxzw5yBJTIaYlK5ecW5Nhq/DgkHkvGFPKjoCq+vvWjlGzcOVCVZNoaOWuoK71fxDubaxbgUSysiHJXE7QMlLnO9EBPFa9ymPXJLBLCuUG/6I4qfB0kTi4GeCwRJLHens2R2RihrF6Il8AANtukS3UpZuuySUVgo/K7c39BdQigME5JKAPIE3eqxzbSwbp8cgm9wxm73+649mdVpw2oCl7abHb/ucUvYr0+G5JZlEOXKptUlHnIcF98fu8rMdWtpqI1s2NItTw+5o9sRf0GQRYfdGkgy0rmTcO1tp2/Rm53P/fNup4y2kx2IZsEePTYK8IU1tzYykjMIhm0aA+kLJryUBe3LPtWoUE4QOJSmyDxpjvTpOoZFf7kY1wrGd9vloWHFVLQVYh9LNcsKgOUzTQok+Ob7w2EnFRWMMYq7rISUZAt+l5wQP0G2AUzhQZ1sRqusDVPqDVQLUmpjH7Ux8VLxcnJPyDlQdgv90lTbaxeLhbMf5F6XxoCPT0SSlIEJazkXlTpd5Ly5cfLVsq40M1Lq7aafh6Y92icUFrQS8I1e3Fpidc4Km0Tr3l+yK7ZPbiifHeC8bgemmZu3SyQsO/Wy7y7xoqtImOoRojVcfbVdXhqZxcPN/ojX1gnjlW0F++0VWyirPjiWEmtTAjaeQ2Zsg/WRFlIxF8Qg8wwnTRDRb5QThgFMK8dERdnV+PNye1odB0V29ay2zB3jELeFZmF7wU5vTDGUUdo6xXAWIltmRMQ+GJd8dRvRUKkudHRSd3CoIRyvXPszx26CC7QWF+td19C60RLsRlqNqVys9lrZVKVmO2pTaOLNMXMT0PWOotf0DYuoQ5i22wvvoOJSwMudJG9840hf9udGM800i7CRheY3UWNOXXAlYLSM1sPo1gbmXjxt54LyWVZpqTPQuXVzs+TMOQGIh+duedJuyTjHlmi19dVM5E/ptbpsSkhJygOeVVXMsRDQbr+++duiURtI4BJ4rWJ7CWVRsx3ZU1XpWxAi6po7b87ZWZCYKPUPe3ZxXXfCFY336ubAsF1uQN1KcCufEuo17ARrDdUZebMi6pZzFltIKgWzi4qRdGXhuMBoyvdAy3i0lDUDGrIlVjg5TEXSqnDtTNMi0bapDVyhnWZXHiZCl4jYHKurjmFSii610BmYqkac3Km3TLgojntu5ZaDXY7tKcH5OSwlu4Yb18LQr9foXIrncZiZIH9YdFlm1qocxtTLnJ4ObyWrNycrY+Oq1ZaOR/GDlJxZlySJG1+fxype19exOlnrBZ8XDN7z4g4TdBrml/EhPIgKTCYFd3AS39myKYpXQXi7iYiUA6BOks2UyXaAZXwHq6szdMrmSjKSWKVzeX4520eZcE7XQrgMkaeB7YDaNM167MmCJm4KaNOcwlIlQIA0d4ouu5gb9qfslsA6U6FRVZkjGQqg61GR07C3xblboGnYKOpx5bmVw5kXPzB2MikstUN1gsoxEHnR0m8RIdprY0cczQOpVkZmS1tbNs7a9bKSQrlak3UpieEC1PdlTQ/2gJo9oLgeWwr8mJ443doS+G3PSldJU6OC3FRSm8A4dkpQkeao+XmltRJJ7MSraByPq2sTgfoebZUM2YpFCAjCWS6DOFocx8Lb75ZNycbZHOzMt62DXvoDxi61xrN9aJtju5inYCYnWykvSNwM2SPhyBdRtk+pd2KaUEVM+7ZcR+5lpWO1cHQIRr7Upxvo2IVR2R33+XnlJWtBPpFlNY7wlZbcKzdfH+OtHR0OtBAfRjgxeWlVNgNJYriX5LkozTmNcbxTBlXxPjhSEMIaUbssJFJrHIS7dtJR6DxA0mrIkK7OB2u2OEHrPfCHiV6PIrPW6mveLbfQEK9uWTJ3bHFp9ovu7CGxVUq5S2lWwK3dm1mjZz309iqFbKzQJsnK9gt9xJQVEpulIVmbYMD9QTdBVXbrMSOJrO/4jcb7xPbGF3VgFq20Kf1M706HpbBZOeKKD2wuWqF+0OO1kp31IGM5+zJefF2rWz82dwnHuvCRreS8PBF2I+VLrPV0eqmxyXaN7vg5f6t7UcpPpiopvO7Ne1izvAHX6OEIx2PMdGN1cWQnEmLFdxZp2nMepVelQCyX3EphDRH12oMhIcaajUnb3YQqnUhzelXasXbN27SlhmBRHZT5vBo33sJrEScTdHUHYWFvn40FInRVPMf5PdVgRnBY5zYfdo3JKroK+5du35bDvgxhCPXNq7NO/N504vNYYpxxwI6kOpCEYdVOVt8OwTbaqSLpbPOQJQZ/YRc7crusTMJZnz0bw+1m5SPY5QyFbe/20rykx1VAwVcLMZmFas+xXXgzSZlkYh9sapzSMC10HdJUUws3f6mrB/Lkb0wV2hreDQmgM04IOV5TEB0v58eq7+vah24raKOpen51nXlfoxAoo6lkhYfherT1QjmR7HVwXLYs5kzb6UfB0GUuXzDDTuRX6eG2r1nFDlpWzGVRg7d4QO+uDt8b6y0UjVKcX4XFYd/m0pzguaWdUom9OcLeol5WtXokLxjd1Vi6kZyLf2rGQ7ISBJyliz73xXBP80cBxW0qhOatG3QSPVpLc7AiqON80CcLZJ0ItOVdQA9wVtmQIANNWyS+7S2DkbMF6bJyFjycDLIyz2LfqVXoll2RK6TLEmwWLFUZcrFLt9u66V35GsylkHJvdAwYsYNKT0KZxgx2zZ6mRKT1vRFvFwVVEvGxo6/rTS7xRAbdhi6F5712YpZ+d9FvuLSec4ojHMWQyploQZArQ1I4gbOvukxWpMKFuMg4aeVfj9h6Y4u1gCiyTI6My4sLEW+iDZMf3OPuirebQ5BvFd+IU+EqNficXhIFz7QB4nOHeiySAaoVnPbknlrBGzSQwmW9q3MXKn0h6AOJFcQ1zyoFGjeasLwVzTLi2e7qa1aUdQFGRLsFtL70GTCdoeiDC1rjAcSaGQlXDr3lZbmLbF7tddDUNwaBNc6FHo9GjHimAhXUxlwtXAUbL9jVMGIh58JhlZH86dYjUGJKA25a85hZjQ4a4IaA8zesLpHrfm61A2ZiDMJ0PNtTaG2sKXMnlYvB8HTPAptgF8ML8UjA1L6w4gohgxYXN33dA35j2WtOMBSxwHawyZ1WJC8PmbuhzmxcLDYUnJ38s7goMeecJx618fDjqo9bzGryzWa46v68hezBRXK4XkgsSdQ6zYvqxqNIyN2HxJFdOHPuJBiogVwXNnsY/VPLU4VfQH5Rh3bN+g521Rab62gYFLMNof08WLQ4mHA5NoHpnTwzyGLmhMpnKqREnzIic621W/giIIthbQQb/zzfysfFgRHZdOufMXouSYugCOa1nQ/SRj17l9odKwy51BvneJUQYBsWH0ONkiUGdB6ozzCHocDVcJcRO4dycJeVtJWBtBFvaDbWXqJF6y4E2KQ4i9tZPOyj5vw2IEzc4P5mOBrrRsMi/ypuREbYsGt6o4aCxm4Oo1TRxZoUyeQC77KV2ORMCPaJ5mK/SlpqpwekRxx5qenHOeoiCVWwkEfBO0Bv9F5cL25oMh9Yy6g7eS03fbupzWCcQ+aY0Dhf7GK/hLWuPir7OSHSlqOGUuWLrVxSdeaubmyu9zi9XISHVWhSHgwaf+tSc8wOnV8LGeL0DbJJTp7lD+sxkjY1GUpHQNw8iUkGv3O1G7mijgsSpxf7I8O8fHqZTpyf58b/9NPg6STv/+xA8XH29/b86H5k7Fnul/taX/55lX759FI7EVDocWjapF3wPGL8H0emn//RU4dp9vh4wDo95hrat+P11gqmXwe9RLnbNW09fmuKtLsf2n56sbtm+qlC8+15OP1yNyorp5PuH4wA10XtevW3tgDXTfgy/ZRgenbjuZHVes/L4HmI/OnFHYF3Iqf5hpHEN68uJ0OfzzGms9fpQcbL7/8NuWe11oQlAAA= -->
