---
name: "rar-cowork-cookbook-configure-process-customer-rebates"
description: "Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_customer_rebates", "rar_sha256": "7156ea78c90e6527141fdc17f4fd58026b9de697d6be797c0eeadb4f2f480601", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 7156ea78c90e6527…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_customer_rebates_agent.py` first:

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
    "version": '2.0.1',
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPiSJbtX2FiPlTVkJmS0J5tbfYksQihBSQBgsq2LC2ufd+QqKn/Pi4gMqumuqennz2zR2ZYIOR+93vOdRG/vtldGxb12+c3A9j5bGOnaRSCembn3kwobkWdwF9F4sCfmVvkbR05XVvUzduHNw80bh2VbVTkcDtXlmkEmpk9c7r0sdaPgq62p9szN7TzAMzaYlbWhQuaZuZ2TVtkUFENHLuF+/y6yKDWWZSXXTtbDS5IZ36Ugg+zW9SGs95OI+8pbDKtLtLUsd1k1nRlWdTtJ2gPGOysTEHz9vnnv314i+D7t8+/vrmp3cCP3oSXQWD/tEB4GaA/9cP9KbQRLixHGJAcXpeg9os6gx95wJ+9rn5sQOp/mP3HfyQ3uw6anz5/yWev15e36Z/e5bM2nHy1mxZ4M9cubSdKo3b8NOPSmz020OW2q/MpVA2MZx58eu78LqkoZ3+d7v34VPIpAO2PX94KaMIjAl/efpoVNdRXd9P7T5OU8sefPqXFDdQ//vRdTtM5MXDbSRi0+tPX1/VLLFz4fWnkP7T+FUp95tUBX95+59z0eto9+Ql3vn2Kiyj/8SkYZrUHuZ274Mef/pFYNwRukkZN+7+S+/NTcAhsD/r0MvynD48g/202fzn0TeY/VlvCtP4rnsDl7+o+zF6B+keyH/H/b6LTKIfV/B7xvyvu722Y/3X28z/07X/a8GHmf3lbgjTqYXU4Kfg8+/WrsV8JP//gff/wh7/9BkX/UzFG0dXuQ8LXzM4jHzTt168//9A8Pv7hbz//0JWw1oCdfe3q9O/J/Htxfej5QwRfq378416o/5gneXHLZ98qffZrUf5b/dun2Wlq/++fN59nv++X6TWfTU68K32G4Hc900BbfxfHn95+gxCRQ28693Ebdvm///tMidy6aAq/nRluAWEIJriNMjAZb4ZRM4P/p96uAYxrE8HAvtbB+p8yPFlc+LNf/o/7QM6P7gs5kXc0BF9f+Pf1Hf++vvDvl08zE0ou6iiIcjud6dx+/yW3A5C3k9ayBg2oe4gnztiCjxCJPk5vIFrOfvnnwr8+5Hwqx18e4Bk9EUoXthM6NV0KPk0enkOQv/xxIRCDAbgdVJEWrv2E4uYD9Lwp0h6i2xSNJonSdOZFNXS9qMcnMHf550nYL7/84thN+CV/wik+e3JFg8AF38yZffwIHfPTKAjbLzlww2L2w6+//TD7z9n/tOshfNKxh8j+yge0UDI0dQb7q8vgMpgqmFwIHo98/PrbK7xQTA45B2Yv8ieymjbD+kyA9x5rQ+Q+Lkhq5gAYYxjfbGIXiNGzqP002/qzb/ZCpdOtCcXDomlnHihB7oHcHaFUG7rzLZJ50c4aWISNP36YdQ14aP3Fqe2HiRlsdLv9ZaYIe8gZRTqRZP3iELi5yCMY/m+V8PwcCql/aGb8u4hPM3WqyFlp13YZ1vZLh28/8wK54n07FG7PcnD7kk/8CKZQPdrjGR64CEbGfaX045RzSOQZxAKvedf9WGNPzGY+GK7+kjev0rfrKRUupAKoNOggX0NC+MurpJqw6FLvET9o6STplQXvlZVHDe7/0Xgg/GGe4KcRw4AwUs6+dAsUI2b/n8ePyXZus9FXG85cLWcr1dQvz5hOQ9MU++ecBceAGSysZ/98Hw3egeUdX7/kaQQLpB7/8lz5yMRrzROzYLt7ECT0h3xYBtCVSe6jSqeqq+tHNL7k70D+AYbmgVrQBdjSsOSneLwrnO6+WxrCvp2uv5P6I6u1N7kOK3FWdk4Kq8QHwHsEoQ3rqdNemYAlC6auu4WRG/7BqxmUDisDyp9BIyLYOxDsH6FTC+gmbLJHFr4tj6ZRCVrhdS60Fk6l4NPsDJtlKpgGdiicd6Y1MAo/PETNMgBjDE38FuEmtMunMdMg+zLQnnJRZDDtv8/A6+b38n7YMpkPpdow9zCWtwlwPTA8M/vNzleuoLHZ1JCPTX9M98vX2e8Z5y9f8oeN3zAe9nk6kfXvgjOD/ZU1j5KbYKqBUJOBVwHBSnjw8qcntT65+5stn/80vf/4rw34D7I8/jFzn2dh25bNZwR5Etw7v32CIIHAGolK0Hznuo+vZvv43mwfX832B8nPQH2e/WvW/UHEq6w/z7BP6Cd0uiVHLpjq9vWCwRA+8pePxHT3S66D71l+lcIEsukIyfUb47wvgbQT1CCYFj8ZqJmI6wa58gG5MA9f8m+V8OqTJ95AumyK3/Xvg3phXp9p+8YM8FbeQt3eNKwFYDrJpJP5DXj7nHdp+uEttzPwvzrBTPgPqxWGYzr5wPDD6aeNwOPq2yQ0Xfzx6PboKQgGXvF5aq0Ps2lq/TD7NoB+mL0fCR7HrLyDZ6Kfp+F3UgmXwl/f1n47FzrgDZ7C2rGcTH+ec6aZ6zUL/9mIqaPe0XliqVeLThr/JAS+CQJQ/1mI9nhjpy+caFp7Yuiofe/uBtrpdROqw+TBroONBPGxgxv+rAbqqUHVQSr0Jne/x++7W8XTl98eYWifh8Vf397x4pWD12AIl8PG/NhMZIjAQoUK4fWzpOC9/4uR8SUBYhwcWKAIGiMpYNOMy6KAIhc0RmC+52K0T/geyaALymE9QLG0RzmAZmkXBRC1HcJf+ASDUigG5T1L8+vE+dFkFUB9gLPYwvVwakGSBIvRC5v1bIK2bQ9lGBqlfQ/SwPetCQTIl6tP16Y4fptep5C8PP71zaEIuFIkmi33fAkIe7Kd6z5WeXmep/NQGZiRQ7NNe1M6fE0MS07DTw7f3AHh6Qe0zBe3OtJjUSkvTENnZQUkkeF6UvI91MC3roQ0wgnzLEfAmkt9smuLZLsSTYzjdb8hldpGLXDO3EUVbtSx0s1TOl7sKrUcQ/PU0iJ6AeuH5T5dpDUz75WeqMfOuKHRzpTsce8VDH1uTklBbOeVpZyYxTVSE8nSTy1Kun0TnnZXmzrx6lCymI0rpbEmqWvN1Xomy8pVJGJn3VtlvrmjIGYqat7JNUP5OE2GTsgw/b2akynRp5ckxLTTipYwm4VEOZxk9BbhWMjzWCybkokv1ZsftbXdHa3tfZdb53Hj0JXhJoqxlQS1dtsLWg2qRa4dzeqaLRvtsIWCiJfAEs1GKDcbLC9LR+q42nKrxjbmO0tyaM7pilhEz9XRHfE2q8mlSYMqSc9dsRNdlTt5gDBz5+RUljCedn08dwJU409doJRH4xrlHRaXPs1iYiBqd8kjBC6LRH9OVJU2Sjd/UaWex+rE6KhBna8XqKZ5oDqa+wE/FRTqGKf1NanuOq4T+zK+RoeFUBetXmIRfarPViibuMwXSa/3asyj1rxDm1Q6iCVhWUFkbLpbYgqY6LE8dbIDCy93nq+siJW4XWJWd6elBsd5ge6dLPD6vow2Z3PHbsczzTTXg7Ok40OUb4pF2i9qTD2r63NL2HvOOqsUatpUoBobwLieliyTKKBY6uIOatgjq9FU1ieE2OmLuIjviWa4cRC7VJA2Ngg6F2EzFFsv+tyOG0RjWvIy0Iu7tbtrF1Wk1vW1GcLEDmsB/iyn31WDXKhF0PmQlPwDzYfAj3ovoxscDExtaWsnLeacurZWNwTBaWqrX8XTArbGgmfNY+1H2a12VLpYtNndkOQdZpf6bpS0xVFfnDIkHE/xprBN5Hj2kRXHzEs2kJaqIh/pQss8FbaO3e06bQXLLnVFI7ydifVuvG69nYLGh41ddju94xFd0ndOPV9fx9Mtie17vbu09zBs8hXNgvGCC1Qf3B0yLVUF18RNctOHWk0O13vMaXKxiiMmJo/zE8lYWeik+M4ZInXujnW3EbKesJZb5J6QOpUxPClxPYOKBE7kp8Gma8bbCoMwLGznnAoLTyOpretd7etGKvancZl3YlzmDlqZiuZfROQmxFq5zA1YPYe1e57vYqPb0PO+F+nCpjdr3dI79MbM57lWZXnFCLycFuv59Zq0ONXhpbSnyvRqVsfKPeFDr3eLpN5vk1XsVyV2WYwVjAh1ruR7IWCHjqrdMlLzCPiJqYGrJ1f4ytuukthfJXP6HK9M5FatJQFFg2bPCgtbcK8dFVgmrRv0CrVd93qJrrfNbQlruupd2aJX26uEjrkgLRm+GlM5xve1ekoP1wy19wdj8GJxdXGDcO8NpLkIBFxhfJZC7VpyGMQo5XqM2Eyq/VVgXRZmoK3cYkFdklvqJtieyioJOaYdvouQHSWLLTqft3vfV1C/NzjYc6Gv3vJdlAxnau5n0m5f88q+90yxXm8CodGYq0wO5epSnc7ard/IvMbchCWdESuJRWSc2w641Am97TgDgeT3tRJVZ3tE8uNJOy2WBbPMlhAaDoJ1LZTb3HR3un1n76sLld/WN8OStmCToge2O9E7SgEDZxwP5sFowO5Y6vyiKdXeOKMEe+z8TcGlN6c7D+e0iZUda4VWtkFchWV2plop97Otd9gl9K6YR0s5Jgut6iVXfO/3FONaabIA1sBLxZhGarcgERHzIwIc5COZq9zFjZ3kbO2LHm0Gpj224fJOL2nhsmVITdmnbCKKOD7iDbiem3KP9FLoSsZtBzJDBixDeEGaSPNAv5WJsddSebeI1F1mGeQClzzZQZZCnoYSpsalK1R5RgRJsIPFVRtaXEYmqYlB5MZ+ZA4w8TgFi5k1DUhRDa5JzmUYvGRYB9c9hUlJKSGndUw41RCtJHp9CBOUTPOyOS90kYcHH9ZgSZRtJc6SOXa8iEa270UGXWMCPF2fcQ2lN+VhTVeYt2ntRennpr/lsnVYjC1dNNWBxi8Me7+GNX8P7BRZn7pjSMvHA2u18710UUMsStHc3kLQCJg4aY6R31atySoDt5HbiNj295VJGyfGvdEcVvbHQt2lG+yMVda1Yu7N5axZF5VY0cdE0Nncky7g3BpdblLIpWvEvsHNOL+UrA02bJ05lW4MIKYNrDsTy1yUN9hwLyDZwOK0rHVKV4NTFrEu3hHmpNVZhJFEYF6Vq5PVq5MjWKFzBNRod5Ss7mlwdIj6ZMS3nSzYRHhWaB4/nFxZPihy1Bhhep5b9Y1jeDvlcBtDhW3M3h17o2rblqNXN+aARcSVl6nRWyJ4hanG0duOC653NxJ3KEIWu7G5ERebXJZ4GjW7TUcqyOmgzQGKVoVzIUHHbeKSVbwlrYdaeTYLHrHACMKVFC4Xih4pt9xXQYxJLMtySyORemF73t3nua6Z6HV30EXaPeCUuJZDgyaM0eCIWipRnhikxXyLX65keifkVtfLKhBDtDdXVb6VuNtma8rl6NJVXJrsSolg//A+ep+voxPlAtqsfdQN6Pi+32bmkqyzBLCKBMqLcd94czN0aHoOu1uR40Bdb4PisvSSC8G28vUW1wvN96R6rJW2zcnFhahbVqOU+hpS2bUKFoTWWTZfhwTD7Zb01TSDFXZYbLmNvUQP2z1nD0Ye+M5hOGTD3T5SbVL4voMyhWQ39LoJlmVsFLjJc86CX11ZULOr82rrmO0JtU5osVHJvT/wxh6w7Q6rcLdKd5tIIcRF6SI1s6K2okDIJDzOdbxIJIZeePs1tdtYwx4XTNUF6ZbQQCijg6MQ/G1odokeq4Od2fUBWWXsYXWnFjsn5JisQTh7JElZsPB4rSwzCQhwFMNNlBMsWC2dcFSI2kivhbzZIWqnoHf2vNQCx1hxXIid1dOxZuV01Npc3ztRuzYcJRzWondr6iZey6xwuwvhiJLXFGxAETucnnZUdxeupwNmGbV5rtDqbEXamGBAdHrupKTaAMfbJmVCJlGI3MJSLIwWodrRXLcT1XTHFk25ciwEazJkUbiJbxGLm6OlQdJ2Qeyvd8T6umZHbDHIinoQmIx2L4e8N/zouJf56CTg5DLYrgQEj7fFZhc39c5dENTSDci1HHuA6zn7Noi4sWe3gWBjma2Rto9pVVkv+Bwj9454s3t1qZ+3VxyodrQTuHRVA3i0IGQ3v3rbxVa4tzx6E9pNZyq4jo5rkHKUdxxGfb1l5KoVZfnMbOddIBBkvL83Ogn1FilIGFjC5TLbM3QeomXUFQDdVfxOr9QFRMqttUcSB+xWa2kf6PmaTJj+uprzmarwKRCS62Jzw7jiuBd3lXa/rAveOMinOg/qULlSOn9UIG+JReiRMdCXa8Uyc6S6SalhFCv/6o2srA5LDazEo3OgT6ZM8CrM+1bV7stujDQ+gaxCXjPdgd4bqru89UK+MkbFkBJGJjcqw9guBWcSSb5c5DBQ4WA0Kts0kfHIUdAoUeaHOGnN2rh7bCxQ/F5o5CzhdxzntTfYBHOqyxBUPe7OwV5aD0M0x/dltmpWtX6mkjFQw/CyRdllUxCtq+cniWfZyy3ehefNmXf5ESPJndiNFUWFV+Eqrdqc2MV0SaVzdz/HNzyhGJqmkni7EnCj3yLnLeMXGEOwolz1JmsFiz3BCBq70BFgLg2KYNwaca01A6f+O5wSXAcscs6/omAdyDrdkF6XX4rCNF01u0dXCGHcYhtYJOrtWbpB977tWbiLnq+UuZPHSBH3I+RJ3upHxGAJc3WCg+bIBkhn45LfXpg7mhBLgzGQQoTnuFHgh3HRntccSiEtSrgaiMNoSy+JHRIQJyon7NUA7o3vBfQ16O8JpOWcbGmcLXHM483b3J4jyHZEuPUt9dr6xh6QoR384w0UvOfB4zvE6R5wmSJ2S3/rLyjhILVaCFYleUVvELH2q5zl16SSLCscniH6zQZdMSzD91uzWd5SZnQk6nJvzte5S2e4adDs3c/4SILTSOXfK3vP32Ssa1NjCI7ivN+K6V6DDCVJob+FKRtPrB7BcUw8Mfukt6Ktf1kO3twgHMg2Gzq6yxgRaPt7W4D5YSMemLukXqiEV3M0qUNfbDVmz2wgGRQ9eVxjK7aLdGozoNUyoSwMtPMWsQeMjaWss1uJ5ZQFv55nyzGc63BNu8cxxSRtkq0GTF9XKx4LT+I18+uLZq2L05a1TJ0nln5luZ5Jt4iYI1stTvLtzUBgf2bjSptvqcUxGpZYN6zsyKMqfjjLaNJh+wvLbPnEKzKJnWfblD6kBl+TxMrh/G7cbxQpoYTdfQn0c2HSyLGLpf5W3bM+unoeeecHMUov4/xQbi80R7WrPe308IXMnaVzF6lAu0oV79RMTvbbIIn2isOhR8GOF2ggOMuzflmuF2sSMOJpN3QH9GBQu7nJkLds1Y9z/A7Qvdd6EXEm7pApGIzaArdMGgALyXdHiluy6jJ37YEVQ9FFI1TFRYDXpEj2OB3sLSGOc/WmCYoMpw44OZQHTNUEhyN7fshOY+M3LXdkbmSJr71WEQTJVdoSb87dqTtQLI1DACrJ2pM2rB+R4wbkSm1CHAcEDWSdHBgy4mC1UeBwZi0P8TY8yTFmTKMgrsqNOoK4pEybc6uuGHorkQy18l2ORYJN31uVExKQe9l8flK0+YL12LG3JB9RN/xmD8/2OEV4Rkgeqvl+Lh/1mPYXPu0s0UGvrKWLMnMVP+TUyBoZru3bhYnQskgulRDGLfRSQkawi64Eint0Sd6juJKxK/x8axDRTKo1PNUVN63u89AKcEdDNmJwTrhMM5LCoOaIf+UPRyNfVy48GNsOOT97uFoF66Zt1S0jVO5GllcDG3EqtVHrmDMPFw0NbjsG9S7gAsL+GuxaxxEEMu4BJsoDju/21zjT4TmiiAu/CoVcrDa9OTCg1L3ToIJhzhBuwtsEV+jwgGNdtoSvp8t0CU7ZcalxCuqRSbHbp2BRoJXmWkVpxy2drvUwz6xxyBZ0B1EAIbd50uRBysPSr/vkpiLpTTQYDWXvEaaXCRJDyLnszIu1a5yo3sklLkZ5ayKwX4t9kSNXPmPZu8bfs9y6EQLfBrpEdF4fLVeGqgQhv6URJ5DYSpKpqFQDViSkcZXXZG/kChkdRFfc+7vQM2tqicNBDD+2u4Dj3j68TU+uX8+f/4Xvmafngf/PHks+nyC+fxf1ePQMV3x+6Pr8rxj1tw9vtRtBk56PX5u0C16PKv/bw9eP//w7jGn/+Pz6dvrabGjfH9a3djD9BdJblHtwSz1+bYq0ezwA/vDmdM30xxDNu61vD8eycnpq/k0lfF/UHrS/Lb66dhO+TX+oMH0PBLwIan5dBq+H0R/evBHmJ3KbrzhFfgV1Obn5+kYEerf4hH6CIfwvMNEcEuglAAA= -->
