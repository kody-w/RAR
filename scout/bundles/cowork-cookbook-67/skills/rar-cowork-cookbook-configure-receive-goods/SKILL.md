---
name: "rar-cowork-cookbook-configure-receive-goods"
description: "Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_goods", "rar_sha256": "fe615efa546e693b7ed88e3b188b2cf364d1b858aeb89bd1785fd2b028414770", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_receive_goods`. The original RAPP
agent is preserved byte-for-byte in `configure_receive_goods_agent.py` and in the RCI capsule.

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

Receive goods Configuration Bulk Setup — Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_goods_agent.py` and embedded as the fenced Python below (sha256 fe615efa546e693b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_goods_agent.py` first:

```bash
python3 configure_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_goods_agent.py   # or on stdin
python3 configure_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Configuration Bulk Setup — Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_goods',
    "version": '2.0.0',
    "display_name": 'Receive goods Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e20ccf7ee06717ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReceiveGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveGoods'
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
    print(ConfigureReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOjRpb/KmztH22vugvEJegJRyxCgCQEujgk3I42R3LfhxDy+rtvIqmq3evxzE7ERqz6KAEv3/1+72VSv73YXRsW9cvnlyOwc0Sy0zQKQY3YuYfwRV/UCfxRJA78h7hF3taR07VF3bx8fPFA49ZR2UZFDpdzZZlGoEFsxOnSO60fBV1tj48RN7TzACBtgdTABdEFIEFReA3i10UGRSFRXnYtIlxdkCJ+lIKPSB+1IXKx08h7cBj1qYs0dWw3QZquLIu6fYVKgKudlSloXj7//MvHlwh+f/n824ub2g289cI/tQCHh1hplApXpVAd+LgcoO05vC5B7Rd1Bm95wEeeVz80IPU/Iv/xH0lv10Hz4+cvOfL8fHkZ/xy6HGnD0Sy7aYGHuHZpO1EatcMrwqW9PTTQ3Lar89ErDXRdHrw+Vn7jVJTIT+OzHx5CXgPQ/vDlpYAq3O3+8vIjUtRQXt2N319HLuUPP76mRQ/qH378xqfpnBi47cgMav369Xn9ZAsJv5FG/l3qT5DrI4QO+PLyB+PGz0Pv0U648uU1LqL8hwfjsi4uILdzF/zw41+xdUPgJmnUtP8rvj8/GIfA9qBNT8V//Hh38i/I5GnQO8+/FlvCsP4rlkDyN3Efkaej/or33f//g3Ua5TDh3zz+d9n9vQWTn5Cf/9K2f7TgI+J/eVmAFCZybTsp+Iz89vW4E/ifP3jfbn745XfI+p+yORZd7d45fM3sPPJB0379+vOH5n77wy8/f+hKmGvAzr52dfr3eP49v97lfOfBJ9UP36+F8vU8yYs+R94zHfmtKP+t/v0VMcai/3a/+Yz8sV7GzwQZjXgT+nDBH2qmgbr+wY8/vvwOgSGH1nTu/TGs8n//d0SJ3LpoCr9Fjm4BwQcGuI0yMCqvhVGDwL9jbdcA+rWJoGOfdDD/xwiPGhc+8ut/uneQ/OQ+QRJ9Az7w9Ql1X+9Q9+srokF2RR0FUW6nyIHb7b7kdgDydhRV1qAB9QWCiDO04BOEn0/jFwiMyK9/wfHrffFrOfx6B8fogUUHfjXiUNOl4HW0xQxB/tTchUALrsDtIN+0cO0H1DYfoY1NkUJMbke7myRKU8SLoCyI88MDeLv888js119/dewm/JI/gJNAHg2gQSHBuzrIp0/QGj+NgrD9kgM3LJAPv/3+Afkv5B+tujMfZewgcj89DzVcH7cqAiupyyAZDAoMI4SJu+d/+/3pU8gmhx0Lxinyxw40LoaZmADvzcHHJfcJp2jEAdCx0KnZ2D0gGiNR+4qsfORdXyh0fDTidVg0LeKBEuQeyN0BcrWhOe+ezIsWaWC6Nf7wEekacJf6q1PbdxUzWNJ2+yui8DvYHYr03vme3QIuLvIIuv89/I/7kEn9oUHmbyxeEXXMPaS0a7sMa/spw7cfcYFd4W05ZG4jOei/5GP/A6Or7oXwcA8kgp5xnyH9NMYcducMVr3XvMm+09hjD9Puvaz+kjfPJLfrMRQuBH0oNOhgP4bQ/7dnSjVh0aXe3X9Q05HTMwreMyr3HDx81/P57yaD+TgsHCFKlMiXDsemJPL/MUiMWnKSdBAkThMWiKBqh/PDe+PMM3r5MSbB1o7AFHpUyrd2/wYWb5j5JU8jmAr18LcH5d3nT5oHDsFq9iAGHO78YcCh90a+93wc86uu7y74kr+B80fojzsSQRNg8cLkHp3wJnB8+qZpCCt0vP7WqO/xq73RdJhzSNk5KcwHHwDv7oQ2rMeaerofJicY66sPIzf8zioEcoc5APkjUIkIVgkE8Lvr1AKaCcvpHoV38mgcf6AWXudCbeFQCV4RE5bFmBoNrEU4w4w00Asf7qyQDEAfQxXfPdyEdvlQZpxDnwraYyyKDGbrHyPwfPgtke+6jOpDrjaMPfRlP+KpB66PyL7r+YwVVDYbS+++6PtwP21F/thF/vYlv+v4DuGwotOxAf/BOQispKy5p9wISA0ElQw8Ewhmwr3Xvj7a5aMfv+vy+U/D9w//2nx+b4D695H7jIRtWzafUfTRtN561iuEAxTmSFSC5lv/+vSssE/3CvuO3cM7n5F/TaXvWDxz+TMyfcVesfHRJnLBmKzPD/QA/2l+/kSOT0cM+RbaZ/xHDE0H2DDfG8obCewqQQ2CkfjRYJqxL/WwFd4RFTr/S/4e/mdxPJAFdsOm+EPR3jsrDOYjVu/ADx/lLZTtjVNXAMaNSDqq34CXz3mXph9fcjsD/2ADMoI6TEzohHG7AosEDi9tBO5X74PMePH9JutePrDuveLzWEUfkXHo/Ii8z48fkbeJ/r43yju4pfl5nF1HkZAU/ninfd/BOeAFbp3aoRwVfmxTxpHpOcr+WYmxeKDGLhgbdfFejaPEPzGBX4IA1H9msr1/sdMnJDStPbbdqH0r5Abq6XUjgMOQwQKDNQOhsIML/iwGyqlB1cH+5o3mfvPfN7OKhy2/393QPvZ6v728QcMzBs+5DpLDGvzUjB0OhekJBcLrRyLBZ//bie+5DGIYHD3gOh/QUwr4NkXSgGYJZwY8hgGEM2UYB3d9gia9qcNQjA0chnW86YyhfA93MJwhp+RsNqrxyMKvY/eORlVw23YZdzYlPXZm0y4gMIdwwRSfejMCYBRL+FACCb3yvjSBAPi072HP6Lz34XP0w9PM314cmoSUS7JZcY8Pj7KG7Zioew2XE79mo4HoSdlJTjiOaaTYG/pBs9QDNws7HefX+0UzaMQsdiL3kHSyn1S8Eu0GHlU2k+TWYA0Y7F2CC8bhKvKRQHi4l1sgv6ZA4I6xOpTmJK3WrSatRdPN4MXUcMNjhl0ZwzZOZCIbxpGaTCbGybXqvDIs8zhfHvbtEMaaO5hDe5BSEdvKpNxc9UG41ZtqKrsXsjXk9EwbB/VaMJ3are1SC/tldjQjRUrswQ9lnK93mrHcHqqdRjGony/gf6fLpNVClPUdlb3trl61KxhxnZbW3Og0SdzkXmTty4NT743GvaalqNJhzcqCCKjNvklbWtUPpN54CeOtzukhIfkgarpKX6Wki1YSrndedd5YdL7KTuUhOM0PDMqKppVXqbPI5puKMs56zkyVwwnnMHGq+Ac7IvJDW6iohZ2otEyVojFoN9F5YzoLt56RbstzvT7Ik90snYf90cjbTIlOyrG9Nt7mVhIC4NyZEBPBiqfnMurEcjFbn+aoI08xYrqI143Jd25u7HtKpcu9gi69Q2lH1WJVr0rTlujNnHV95Sj1hrfuFKk52bE7eGvZJs+tkNAe21h2bpsVMNrzZmAW1+u+XOhn3gvtOKMDz74dNtNbmt0ShrHnidgVRJml9pRC95MrThUbe+Yph2FwTqVk4n5Zy/zK8WzsqFdwHmcrVremnukoVxOcJnNKnxpXrrSFiczvbja/mXNbX9VvZ5qMUB5sN+HBnWjZFlM5350MWqIIm6UutKGGSTeCxR1H32ezjTIzV5OYSOPZzlfP9dbrBxWru4GJo37KOgJGGWHlElvZPAc7gY7V3r+0+3gAO6tg+6YgtqmTpCjpOzmDo6Ce0cakj/jhqtIB0R0tdYYdMeF27jxxZgMdOw4Xk9alJlq0SeeVzoXcUOdrJSWsKMbenBE2+eXMQ1dFCU4v2nyf7aPspq01Hg7ftaIdeO2g1ZJEc8u0EVfW1FjZ4XYuEatZKZy3ikrw6TmS+T3QqNQFNulq8ytN5a5cDdsLoWWZ6uC42gTs4rzC91Z8Ydg6np0nK58wble1ZaZa15f1ZYZ1l5s5S71tQqE35uhEuOze+CPZqG6tUv5Qn8RZ01z3Nc43JxCqZipSJJmfw6shtrmBhwtKVqwLKOwdPhsSjSQ6ej/xVqbEMwPZaFZUpKtbl6fqucK0xW1SoVOMJFgJDEGfYo6ioD46O+nzEwW2iRhhEjqPO9rM2t0KjXepvW/E0rIZXz9kalP11NYuRA41ZuVeTSE2edMePwQXAwtrcz9omL8LjoRMgeOxjVPMna9nmIBKtLxXboy9vQimFAn7DUwEzlyIl2Rua/U0YvyNzlBpyFl5m5iXOUfnVmnOOMVcY0POr3YkXw2pFhK7Sl2X+yQZZH8ve54l8r1rh0v/QF6HkDfPjD9tdbte+y56DLVyiLahgO2qYx3Qm3zXb3XDEo7kfks1NV5OE7bA8Lo9zGGZr9QZkaM6YDfDSvVMP4dVF7BKKspRq5Oady48k3cBqMwlu6aDVJH3lhxetTOhV8q5I7GFPc9jTmRm26vo+/z1xveHzgkXREKdO0JhzrTnEGkW91PTKZ1+A7iIG9zlNopxfhWgBSGcrl5vRepGRGVyvUkAuhHxrXrRCftsbofDYd+LXFycDep4XOzmpuMLYH8Fqd2JPbcJdFfV26Nluvp0Z3hnR70OuFUrchK1pSE2aT07LXSUZsNhWelZ1qoexU6Y7aJFvZO43XDSOlZN93SjZRkVCkrrtAxgEOJEv0guOxutLe3qrOmKSnGJrFYce9CuM5EBxaY8UCzanOINq8lbsvbFhWalJzCR2SRNVllw6EvruFOVMrVgLznWsFXU4iptXCtgdTKjTa11eTkxydDo11MbN/RUWuj50PiesJZaIYts2LTEbWJGeSqFnlyBZhk6Urp0mqpY7Mh2d9S2TXPJhoNe42RKbLrKPtNRf2P6/Qlc5p10nJ2zTmfPFBpfi9SDsFtRwy012cjMee/qpmGXF5xwnTUYd5b4cEV0KUYdO1frtueDfVueVFaQdsUKbBxXm+IizUzBMpmlxTU1rcveLQI+kXk6FQfpqB6X4okkhL3bVHEfrhVL0VfMJOa2AaOdsUpyQiMzjEropug+kIzy1KRn7rwy5kvWEI8mlycHCwUtAdaEucv7hXBi1QXvDJfNdGW46cl0fXftzbG5fTRvrS6oxrGZy4XoXLU5wHPlvFq07gQVh/KcuJZzlhlz7fuVsD7xMm/rnj3YnSArJ6qT1W06hN5VFEU12ZcSG1ic3M3Ts1hf99VxGCAFRfp7VY7UTifnXoTKcitKN+miqAf3pPjrVNkt20KCXfx2zsrjNrGMW77VlsVqO7BwDIvXeiOlmzVHY7uO7lhlZnDKBOCYEeDX6OYCSdPoc3Ij9HBbmpbOTzI28Y6rI7aBI6ZuBV3Hs4uSp3cVJ4aFBoSO00+sFOtEMehBtL3M9xfMljM+IRqFrKcMveYKZuvm/BKXrpZKJjf9WBzDedJv+mFbY6GuzDfc1d7XKmPRJhou1zEfQ0DhLz1jZvuSaKA5h2GR7myLa8/+mr2xbW1ZU5k3Vjc/cje+D3bYzJvMmsV6Iwgm53RzuBMkypzfao3C2v5Jx/aUc5n1w2BStIK7dZjQWd9d8AJmsr2pw1XPL2r0vOATweAGmTNNZugXOGO49fW87FZXRTuH0YqVSP1UM+iuUuAs1W9WTULnrMZzitbPtdI/3K6SiQl26dZVp4V7ZUaeCV7OTHZ6tmqjo/QoVTm9ONnpjcz7ZbeXxJ4gcWba8KsDBxGJdrXE3V4ivxMk2Mpkq3dZOSuFzOqjMD5TQSg55VSB4DUpVTJcp9MGmwycJVodx6a3AxAuuSSfc+HIJJZ13S7nk2NL9Fkz1+jDPlVu+x3cKNaS7VGbMNdFi5c4ziyFuq32pRvXFnbEyetVb6c2OYTdNDvcDkM4iW0r2JfAa6Ka3elGF6xK3Ft64arqZHtiJaxWaZW3XTlbzbhcxNleOldGnVVgWA1L+nAbDC+LTVGrVvhsI1Hn1USvsuiWTFMdNTEdrZwooQkJ9zw4GNtTNhTQoR3kwZnldWpn/vEoUuKgh0cA1tv1gXH5lW6YJh/qs0466KqxNEw9DK/9kYXhO0m0O/e4yzzCQLOnD4I4jYqpOvRo5RmHCyl5A+W4s3hOwmlqzoMcK5O5cRCCwE5PMRHuklkcin1gQ5MxTl+FuHWSt3ng1EWuFdlWXpXL6KCvpmB2ihZTzNUkQZlsr9scP0uxJTtXcXcMtqvhAJhM21DTOXFQj+X5Fttpl863Pjlb+8MxSGUmJsmMiZPt+YopRrwsl24qbXLdnQfy/FgCwdI9sxdlvgrxHlW8nXK+NRW3Kytm3rHzac3RUcfNvFBr632kr+3iwKq3VWvBGdG6EeohRdvpog0ErIkXeHwOT+C44Gwun8qZleDxDtM1k3M3qBAKTSzCiWnOxCYJRGDJ1smQz8UuDGp9vsJ0UyuWpWh6tViITJgf3Sy7trRjL8dxNVtU6dzmOE89yR5Gk91A0xIcuvenJCKLwZ+l/cCYglFU7bHagx51OXt77XXXrMp8Ks691rwtE6HcUSmtBQvcFlnNtwUlqBZgJtVEKac0e56Xu2sMoZW0bhNFGgi5Xmy8DbMM99VlWVyKksHp/MQe+AupxeXm4mVuN52TpkG4Xu7jVr5kNRufXurZdq5U8zXa3kTZ9o7VWV0rcP6iAjcJ5v2wwo+xJ3ctnlObZT2jqnhwK1fZCvPIyPZXjFwR2w2q2TKIFqXa0AqPZQy62SxPrIcbPkZTk/6ArhR6wfuTPTYjpeVyQePronfVhResZuyKR8OzgcekQ17N2+XCBpQV+LcCqNbV6bwZbCvsMk8atO0ulwm3JPla1LoLigo7phU2lsli8UxuHFbIcNFbCSd5ssdZTl7uTSCWU7mX1WLScbaM0kIeCVtQRW6HHQWVhPuOdbzbL0khhbs1IuLIvBRYht7FMDtZN25O88GC1YvLNxnfggAOUWYVw0606PKWGowL7zpk2nu9zDuKjBZ2BJh2NdnIp2ztEapv7dBwht2mmMgenS3WNLPtgrp0eLOhFJdi8cQ+9kZPrzLyxFElcSUCrOTUtOgmXRE3lLDH1LjWl2v80mA160yIuI4lbasT25jmrIZfs8ou9Vz1dspt9VKd08FgvYpjqmhoJjTZhI2zxdvL4qpX1bbWwIKKjRruoTXYIEJt1yhXTsvJzOtYfu1ECiFRfHEkr2fifNxpNDZTz3E3s9C67gRXDIKVQ9FOZ3X8CaN2OfSidyVXpHtj4nDYNPx52iXqRSI9c+mG4qSAeroeRSyuixQO687cxlanvD2tF6wZH7AJuEnnG0suqz0cWacbZ3YayN0qDAMrV4JDww+gV5tpqYb4yTXSmvH0pTGlJ8peIxhIcsZ8MD8xNEU5Xt7p0U10wG263Hj8TRSkAT85stWdtj04l2QcnuDMT3oTasOhnudpxmBOc2IWqCc+jpciQfC7vubl3mMpzVAni8v8ZrOxfQmcHWrntGtEjBVNmIQLuZbGyRnunKRb4emlh51AhZ/RFrRV4ql7G3NEGkQDOYlVsuCdaZ8UQNj5oTwnyEvj9L1SLDMXlSzMU/VhG2P+hbcOC8PBA3ZowG7WaE4n7NwtwQ43ERLOHbjRFCLccib9yQzQS1X31SrPJyRFes6EWsG5X16d+tlVli+zxaEDuchrXXWiljVKuca2Kdnb1ttiAIWzFmvF08kJ2zSoCCYpvUzmyyjOV/KFE3excZptrRhNGxAY12kWc3bX6SJYtN2JDJgF1nP9oKfsyb9hGLnlox3d5DmnxNp6h107qpmSbZq22fLSHswpuCm7JFxkYWiv3CUmLZqVKzQqHJMyoznjhVR27cwkNxBaJkRRAnVL52SjxwSnR1t6eVv5JUmFcs/4i9m6tpvNbMJh8Zzei3XIgU28F61L0AdRheo4KakaRipMpIkw19usMxa5TIszXSE6fR5vFPnSUjvlAtaXGwEOy7W1a+K5D4wKc1l1k96WA6NgLXE9B8yAlsd256qHXdymxqHNUsYIrza6QsX9HG5UNpfrZPBxTL9QM20TuC4HJuug89xTOA9LKWf35wpc1ooIPCHzQlsgpBwVSTwkV7nCVMyWPJ/QiOtKkp2zlecXYccnHMf99NPLx5fxIPp5nPzPXgWPB33/Z+eNj6PBt5dI94NkYHuf77I+/1NNfvn4UrsR1ONxgtqkXfA8ePwf56ef/uKNw7hoeLxLHd9sXdu3o/XWDsZf93mJcq9r2nr42hRpdz+4/fjidM34OwjN1+cB9cvdhKwcT7vf5byMvw8wnioXcHFbfH3+9sT99vjGBniR3YLnZfA8S/744g0wCpHbfCVo6iuoy9HE52uM8Sx2fI/x8vt/A0PuRslRJQAA -->
