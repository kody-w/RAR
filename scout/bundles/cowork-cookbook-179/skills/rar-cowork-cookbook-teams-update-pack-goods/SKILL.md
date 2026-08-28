---
name: "rar-cowork-cookbook-teams-update-pack-goods"
description: "Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pack_goods", "rar_sha256": "0b907e4919d6b55c5f52f449ba1df44b07181f09732e5f5a63241585dbc9a40e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_pack_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_pack_goods_agent.py` and in the RCI capsule.

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

Pack goods Teams Channel Update — Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pack-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pack_goods_agent.py` and embedded as the fenced Python below (sha256 0b907e4919d6b55c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pack_goods_agent.py` first:

```bash
python3 teams_update_pack_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pack_goods_agent.py   # or on stdin
python3 teams_update_pack_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pack goods Teams Channel Update — Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pack-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pack_goods',
    "version": '2.0.1',
    "display_name": 'Pack goods Teams Channel Update',
    "description": 'Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-pack-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pack-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c774ef10fe5a05d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pack-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-pack-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdatePackGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePackGoods'
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
    print(TeamsUpdatePackGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716adPiRrbmX9G894Ptq6pXu4Dq6IjRAgIJhEASErg6ytr3fcfj/z4poKrs6/bt2xETQy1Iysyzn+ecTPHrm9W1YVG/fXpTPSuHBCtNo9CrISt3Ia4YijoBX0Vig3+QU+RtHdldW9TN24c312ucOirbqMjBcr62/LaBLEjzrKyBnNDKcy+FyqJpoSKHSstJoKAo3AZqWqvtGmiI2hCwgaK89WrLaaPegxjXKh8XnFW7kF/UUNVFYCFgawXeO2DqjVZWpl7z9unnf3x4i8D126df35zUasCjtwdvvXSt1lMAQ2HmBxalVh6A0XICqubgvvRqQDsDj1zPh153PzZe6n+A/vM/k8Gqg+anT59z6PX5/Db/OXc51IYe1BZW03ou5FilZUdp1E7vEJMO1tRAtdd2dT5boQEi58H7c+V3SkUJ/X0e+/HJ5D3w2h8/vxVABGu24+e3nyCg9Oe3upuv32cq5Y8/vafF4NU//vSdTtPZsee0MzEg9fuX1/2LLJj4fWrkP7j+HVB9esz2Pr/9Trn585R71hOsfHuPiyj/8Um4rIvey63c8X786a/IOqHnJGnUtP8juj8/CYee5QKdXoL/9OFh5H9A8EuhbzT/mm0J3PrvaAKmf2X3AXoZ6q9oP+z/X0inUe413yz+T8n9swXw36Gf/1K3/27BB8j//MZ7KciH2rJT7xP06xdVWXM//+B+f/jDP34DpP8lGbXoaudB4Utm5ZHvNe2XLz//0Dwe//CPn3/oShBrIHu+dHX6z2j+M7s++PzBgq9ZP/5xLeCv50leDDn0LdKhX4vyf9W/vUMXK43c78+bT9Dv82X+wNCsxFemTxP8LmcaIOvv7PjT228AF3KgTec8hkGW/8d/QIfIqYum8FtIdYquhYCD2yjzZuG1MGog8HfO7doDdm0iYNjXPBD/s4dniQsf+uV/Ow9M/Oi8MBFpZ8T50j0g58sMcl8eIPfLO6QBckUdBVFupdCZUZTPOcCwvJ1ZlbXXeHUPQMSeWu8jgJ+P8wXAQuiXv6D45bH4vZx+eWBz9MSiM7ebcajpUu991sUIvfwluQOw1Rs9pwN008IBQvgRAM4PQMemSAHGtrPeTRKlKeRGNVCyqKcHbWCbTzOxX375xbaa8HP+BE4CeuJ9g4AJ38SBPn4E2vhpFITt59xzwgL64dfffoD+D/TfrXoQn3koALhflgcSiupRhkAmdRmYBpwC3Ahg4mH5X3972RSQyUGBAn6K/Mh7LgaRmHjuVwOrW+YjTtGQ7QHDAqNmZVG3AI2hqH2Hdj70TV7AdB6a8Tqc65TrlV7uerkzAaoWUOebJfOihRoQbo0/fYC6xntw/cWurYeIGUhpq/0FOnAKqA5FCv6bxXxMAouLPALm/+b+53NApP6hgdivJN4heY49UChrqwxr68XDt55+AVXh63JA3IJyb/icz+XPm031SISnecAkYBnn5dKPs89B4c5A1rvNV96POdZcw7RHLas/580ryK16doUDQB8wDbrInaH/b6+QasKiS92H/YCkM6WXF9yXV96fLv1W6p+9APfqBZ6FGfrc4ShGQv8/GoZZHEYQzmuB0dY8tJa18/VpprmXmc35bH9ADX8sfqTE97r+FRW+guPnPI2Az+vpb8+ZD+O+5jwBp6uBLc7M+UEfeBaYaab7CLw5kOp6Dlnrc/4VhT8AAzwgB6gMshRE8Rw8XxnOo18lDUEqzvffK/LDUUBt4FoQXFDZ2SlwvO95rj0brw3rOXle5gZR6M2JNISRE/5BKwhQB84G9Ge7R8AnAKkfppMLoCbIG78usu/To7nPAVK4nQOkBc2i9w4ZIP7nGGhA0oFmZZ4DrPDDgxSUecDGQMRvFm5Cq3wKM/eXLwGt2RdFNkfI7zzwGvwesQ9ZZvEBVQvEE7DlMAOn641Pz36T8+UrIGw259hj0R/d/dIV+n25+Nvn/CHjN6wGqZvOlfZ3xoFAAIKQnbFyRp4GoEfmvQIIRMKjqL4/6+Kz8H6T5dOfmuof/72++1Hp9D967hMUtm3ZfEKQZ3X6WpzeQd4jIEai0mueherjs6x8nJPr4yO5/kDuaZ1P0L8n0h9IvGL5E4S9o+/oPLSPHG8O1tcHWID7yF4/kvPo5/zsfXfty/8zWKYTqIzfKsfXKaB8BLUXzJOflaSZC9AAat4DOoHxP+ff3P9KjhlXgrnsNcXvkvZRQoEzn776hvBgKG8Bb3dur54bjnQWv/HePuVdmn54y63M++uNxgzeIC6BDeZdCcgR0KS0kfe4+9awzDd/3Ds9sgekvVt8mpPoAzQ3lx+gb33iB+hr5/7YAuUd2Lr8PPeoM0swFXx9m/ttY2Z7b2CH1E7lLO9zOzK3Rq+W9c9CzLkDJHa8uSAX35Jx5vgnIuAiCLz6z0SOjwsrfSECQO65vEbt1zxugJwuaFY+QMBjIL9AygAk7MCCP7MBfGoPwDmA1Fnd7/b7rlbx1OW3hxna557u17evyPDywat/A9NBCn5s5kqGgOgEDMH9M47A2P+0s3stAxAGWgywDrVX6MIjV9jKpW2Kciifwn2SXNkW5oJvG11gS8xHVwsC98CYRRM4iVFLyrWdlUWiHqD3DMIvc5WOZlE81PeIFYY7LkHjFAVoL3Br5VrkwrJcdLlcoAvfBSj/fWkC8O+l31Of2XjfmszZDi81f32zaRLM3JLNjnl+OGR1sWwDsc/hHq5TeBwJ+kTopZ5kXR9sCxjbGo65YzL+dkejZnfBOYNKQJx3zGS20uHOK+ftivXxdDXcm2Vj6vZeW+XMVl4HdkZNbn7DzRtF3aRTxKFGdzN32eVgJRebMh1jK+BpnnWHftMmTilFlxWCJPpy7xlTk4h05Jz3m8PNGDo1ojfaVU0tbKN5tBF0N47CzKo8i6UFX45rLB002Jm03UXFjpK7MIWhqnWnMjnUi1HYP+6XsJfbS9iPetm0Jxjml6bdniUxuNLLdS11WGXr2M0yL1kjH/FTeKWI8wEZjZMddPbG5MZUyEhMMvAJdsiNmFehwJ5ETHetVHXMDT14VXpPTdHK9UsUOpeN6KWXOB4sTr73FxXPOn7A6AoVGl/WttIGu13Klj4S8Q2rLddHPUywLMrcKxshuuxyNjEML+65ZRwf3Ui6qJY+wtXKPiV7yXaoQ3292dGtwrWVQ1Esr5rGSpSR1tqFdi6Stmiynb+/4OItS9A8Fo8G13e5e9otMLrUCz/s9mp7xurkAvL3wDt5AAuyIfJXqU+wbW0orRHax3Uqe42RqYiwxFOWWdWro51e9/clP2Lnkr/onHc+EiLK0EhemXW/a3OLIg/87u4O/anf23m84uytFZ7arsXgA87bCVffD6iznAT1OOS6s24CguJ0N46RuxTV5k0Sl320n8qJPKnaNSAQQa6nzeQI2qLKtI158EntjC91tHeotuWHLd44Ucoz6kjwe0tfhQ3Vu/gB28BdJXXjUk5a8urtzfCa3+4ic+5SFr+k65VmdF3LZRf0pu0rCZGPxrXzSxDJJxS2QZg4flD4uxNhwu1avyxo5R6vcF+tF7Tnk51ZnHKdXalbkzpmbbT3ObHSOylu6zMnUUZ5qc7O7jwuDWE822W08q+pOMBWoXQRyQ1X2mxYeVtg6tUN8X1xKrQTVWdleDDq/rA3JIOLxd2wYzZRLAlVdSjqdWQHLqquuYyezlqzcVhJb6Iosw/LoxiQ6SJfdvLQ9mM6kQ46AY0D6xyhm/XhGpBsdkTueaekMc0iI0ncMbmN0LErULtnCQ41LctZLwgJGbxJTruFJomujwGCXlN3tnj1tVTQXG9Hx9YkVn0pHo+icPAw9jpawrAh1/24vyN8XFZxUS5ojTY9lxmn0Gfbi5iUl3Owwe90tr5Ypd3pVZsIJZwQp70L9+tzjqxw3DtLRT8ObWectuTGNVWaKGtjlXuYeFAlqSKuzBRz2o2IVVU+SX3UXPibCmu667RbocI4puFHVqH5fLh5ulnLV6PEyZyBl/Taj9xTTxV+fF6RhwLTY4JO/OToS/B+XV7bVVf7wmU5mAYv9bwkt9zm0OaliV/MXA7DY2JKIuae9qaZuQcLu6eilO81fZpqNHU2G9aT3dIOHYtpzPsKNtpbiS6ocVlulLwSsUrwkL180gdVWvNJbtwSj+E7OfQxJcibNFsVuUkER5OVz4hHB4eTv2FrfmiuKtJywlWo3BtVkIrGeCspTJHqRGBHVDupKhNfupIReCuYLht8bNW7dOJwNyervmc1O4QT7DCF+QQg2U62qYxiHYWglJxnRD5xeBCtBTXAM10YtXU/bCfNljPZFqfLdcXrXRFuqW7d4Lhi+113HTAZH7yVtdHPqphYyqHQDXqX31ufG04Cmq5jXTngOm9lRbY4RDcQOffN7aQ3jiMN3dLIMzIriXbc7ozbZHnoJc3NxZI8EghGlaMe9OS1GlMfKVkjjO4U0Z2zhvbDE7c4F4Yn+0qksZfYXZ2kBTdcnMsN1IkqtZScRi8iIp4pONWIKYLXF5ZbcMtlTmyk0zoJQri8CVv5QKW385UrUrRzMTZj7D2t5CWQGh/UfSFeHGQtbVm5l/PL5nQldsuSppkKAJ81bvAoO7lJuaNhzkl4tIqtvMG3OsfDijYlgy1sEPQspTnBNdQSEzVqXTYJK3QrwVpJ6TgcuHRRBHYErgph60SYbQdWl9Na2tGhdTfuib5d7AOToXlmSHpczZxb7sl4zjHDLVYyPtoKzlo7jPf2jqjnsivI6+J+Tl2KNzrKI67LLEljXF6vtYKPUktb6qsoWYwOz3dit2M3t/Lgl+5KPTic0Vy7I3V3E+9w3a/xZbnOo5iK4ADGdJK92h4eTJWqkYIHdqfSbW+gqHYTFzHpraqLQYr76MrklkWMmilIdw7OOZ6t6rx2+nBxunOq5C5D1Fqj6Wmt4+fmlF5ZPxgnaTNJmnujm15bJL2+jSXzJGB9lFWp3I7SPZR5ZRQTgWNBxb0gCbUUbu2hLYHDqjFw/fX2hu1s3jHHpJhOZJtG54w7NIKfXUOD6fu23a7lSu+NvsNxJNsfVxtJqzYpGKN629SzddFRAokJOl/n7Wkq85Qnsp19ypaSnvqRtC0JNaE2dE5H0TpajjSuSyjM3KVKuTeNth7E0tnti81ytC56reu6pbGBtS8mqWyiExcmKEgNHulux0SJrqeEcUoZgSfEPm6RUmyY83Q0FVFnN9w2IXyGzJjMVXHM3bCpTIRquEAoCm6vypIZdOl6wyu+GTq/OPPLbDws0qPXyGV/MNU9vTp0JeHd+UhK7GO52i/cDCM3ZeonnBgbFb5QN4O2PTBbiY1AuV3KhmR5PDlt1ARnbseMIaOWXioxHFuG3qgrDmerzKpuZZW6mXNatveUM5a6lXFx1Wqhwy2MkdMv3GpBU3fPWKS6cCW0VG2wRVUrA2cGB0nrjZSq1zynnmXujNJJkche4js7KUVJXT0tqLt8KoGbN7wxSBtOcT2LcfQGRSrfK9SLb8s7Vbs7RVtsg67yp40zTPuETAg03ovsNT9a0ghS4FjmkpzwGajT3GEnqNewk8/rzkl5cpPrVDiCyr3dWbSXyJmjos1U4IdKPnfojfSDi6B4az5u0wtS3q91wVFurOJXQ6zVqjduyqXCxuweHaf24iyIE3LTtnigHwjm5Am8e6KWN5cU5EKxvZ0WMhpr1JGyW5f4ViC7lqRWut5uR0HAXbee92TS2kWkfFdvem9X6ZmNOIwZmRsX5AaZX9OtOOzCE6YcRefe0acscCwxbsqoztw05JOyuyxJhmaxmOj7Y3NFjdrbLuOCPZ6vIgGz6sZZTWCLMK1b3h2IBLu16gU76dWmv4h9sKZFLAmE+3DeFEe/EOkLbQdwlpWiWG21KlInkTEl3wBd+dX0djBamuvCQuUx6+BUzRaWeRB24RK/Cht3GVnn+3E7cnfQa+sZUsVyoC4QTDWjlD0ckX1DY3LfSqc6qOyq18SQZ00BNGSjzrcSbQtXvBnk0wZ0h1nF7pAxFkDewEl5ZLAdYkp9XPZRbncrsVV1cn1bexx+l8JzD8tVYnrxIjcr5eRe1d1V2JpXIaedtbpkXTi75Of9rYomdERgnb1LCiYNRrgLlg1+zFMni7qLTPNrxjmw2cALUSQ5gbarx6zBA1MSfHG6+YJZtkqPiUa1PlYHk2TWoG/QfW3L4vdjs+BgVjrpwfkA33JjcPK+ZiKeQ6slPA7GpoxH8hyxpZ8J9iXB7gjlNLZLrhjsThyiEHVdHTHcQxBxtwqrifKIL+xM0GJejWWcv4f+dHdttm/v9YCgnsJToPMOURP1YMLLzbuBXSuCm2CiHDrXQBy7d3w7udbtRBFj0Sz2qF1nh+TCBauOkM+oTedhkpkeafGCfsfFM2tc1na6yNLuiAZeBwslcSuj+44TYcnNtD6hd6a0RxYuo5zXYE9ytKr67iE8FdhItbCQ5aE7E8yCyu+7I99bcEkPIp0pq0LjsxF1lzwAt2tD3boBaxT+qtwMItdFQ1eWNB87k4Gb3qIXvfg+mcrdNImFYFJczXNgA45clKXtmhPo6fNs4xMGe2xqXBI7kWYNjZe2J93bpAep2B65kboxsXtd6vBVuInBcKj62+WqCRFbnFGK4pR1XPFTtmRs1tHjcb+jjy5ll+WloYihGa97vXMQF5e3Eclgm1q8HNaYSOyNFXmPW8Hgt3I/iWG63HoosWmzoXR4Y7NwZHdAEN0ZiK1zk3fNtRhdQt2Onts6xCTDF+Lolj1Xsyd0OXQsMvVtDwo2I2/6Y9ihcUOtVfTg1sT2iPdLrF7ZsBLH4VYKKjqNYeZWcSLSKKHr8Hc0vyl9d80G6+5WLDVu/NtqNd7M29iWW8/e9hfON8MDXwuIcSSnM3GHZRw+aTYrasENX2DKJtppSy09hHy0ifxoJ2/zaLPYXHNNWba+HDPBhsXP13xB7kcVG0V6ZWr3aR8Qt0BRjsKOWkp3YWBtTxwXS4bkzOVEaeNIEAAEfZkZsEKoydT2NnqurFRlG2MUQIwQJrf0SZpuaG/nJk4quzgK7qwdRBObAgWuxz0bHvTh0tYrX19jhLDanfbE8pZzNxRecj6I6bA9ewt1sT61ZE44q119UJ3bnrVXpTAgRzeLFcHgVnKdrn0SRNUF7goK901p0eALR5zo9XHtm8ywQXpyRYyDnPMnhQSdv3w9rqfjsYEV2LejPLEbj8qYw3UT4JctcYmdfRfKU91kLr0AmxIM751gwPZdfI0jmljn6KozWFlYMtI+CupRO4XL3o1ua/ayQ0INtfMzjaskrJzZoUwJTO/pw2GvUYjL1/6Opc/4aplofE0TtuJp8DZb1ApSojulzhrEGVUGIRRlVerKnkGKdRivKNLqGsKCq+UBFWMrsEGWxDFmOnv3aiqHezPGBLlfLNH1aYH51+OwvNR0UKing1cdD4x5CyRfqDrSu29XLpmxxkKVBXXlO+cLzeIbP9JQRTvxTKmamI+AUOyv1m5pASy5h2hqZhbhRO3KoEeF5+/teSW7V1TS4fs9YOmtmw8Mg962nLM/ECybL/JNcaYty2+700Tb/qrqzDZuS6reXPlTuB/gEJ62uHss9NWWJ+FKWrTcGVFdKqAY1iJPRESjvHUdqOZ88TPZjY+l4HK34F6Lw9W33E5RA6rubiq6vSM7ZsQSsP3v7DuzIOGVZzOivwnG2nEpPzvhI4jV0lscFIfM1krT0169uDPomXGWdOegkikb200d1bC+22hIUqbHDnZxpeEcPwY7H4nR+NBye5xfq7LSssN64dvOdmmJPB1Pki8DBUZ5y8KrOG6OWZT2rUjTXpz4CKPdrbAkSolhmLcPb/PZ8uuE+F+9xp0P7/6fnSE+j/u+vhd6HA57lvvpwevTv5TkHx/eaicCcjxPRZu0C16Hif/lTPTjX7xEmBdNz/eg88uqsf16Wt5awfxLnbcod7umracvTZF2j8PYD29218y/H2i+vA6d3x4qZOV8gv17kd/m1/nzYXEB1rfFl9ePHx6P5/cwnht9ndV6weuI+MObOwFHRE7zhaCpL15dzlq+Xk4A5fB39B17++3/AitpYnn/JAAA -->
