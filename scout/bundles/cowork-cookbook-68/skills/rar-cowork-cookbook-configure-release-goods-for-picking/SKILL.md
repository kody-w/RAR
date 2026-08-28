---
name: "rar-cowork-cookbook-configure-release-goods-for-picking"
description: "Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_release_goods_for_picking", "rar_sha256": "9d161e71d48a846e968a4c2114eeda9a323287ffa6d30693539941e9d5785f86", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_release_goods_for_picking`. The original RAPP
agent is preserved byte-for-byte in `configure_release_goods_for_picking_agent.py` and in the RCI capsule.

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

Release goods for picking Configuration Bulk Setup — Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 9d161e71d48a846e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_release_goods_for_picking_agent.py` first:

```bash
python3 configure_release_goods_for_picking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_release_goods_for_picking_agent.py   # or on stdin
python3 configure_release_goods_for_picking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release goods for picking Configuration Bulk Setup — Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_release_goods_for_picking',
    "version": '2.0.1',
    "display_name": 'Release goods for picking Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-release-goods-for-picking',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-release-goods-for-picking',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf924e23a2ff7814',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/release-goods-for-picking'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-release-goods-for-picking', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReleaseGoodsForPicking(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReleaseGoodsForPicking'
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
    print(ConfigureReleaseGoodsForPicking().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebOb1pbvV6FP/xGnsQ+IQYBvpeoJhEBIgCTEpDhlMw9iEqNQXr7720g6x0nnpvumq6uebJcF7L3m9VtrbfTri9O1cVm/fH7RAqeABCfLkjioIafwIa4cyvoM/ivPLvgHeWXR1onbtWXdvHx88YPGq5OqTcoCbF9UVZYEDeRAbpfd14ZJ1NXO9BjyYqeIAqgtoTrIAqcJoKgs/QYKyxqqEu+cFBEU1mUO2EJJUXUtxF+9IIPCJAs+QkPSxlDvZIn/oDbJVpdZ5jreGWq6qirr9hUIFFydvMqC5uXzz798fEnA95fPv754mdOAWy/cU6Lg8BBBmCRYlfXuwR/sz4CQYGE1AosU4LoKaiBgDm75QQg9rz40QRZ+hP7jP86DU0fNj5+/FNDz8+Vl+nPoCqiNJ2Wdpg18yHMqx02ypB1foUU2OGMDjNB2dTHZqgEGLaLXx87vlMoK+ml69uHB5DUK2g9fXkogwt0CX15+hIDlvrzU3fT9daJSffjxNSuHoP7w43c6TeemgddOxIDUr1+f10+yYOH3pUl45/oToPpwrBt8efmdctPnIfekJ9j58pqWSfHhQbiqyz4onMILPvz4V2S9OPDOWdK0/xLdnx+E48DxgU5PwX/8eDfyLxD8VOid5l+zrYBb/44mYPkbu4/Q01B/Rftu//9EOksKkAZvFv+n5P7ZBvgn6Oe/1O2/2vARCr+8LIMs6UF0uFnwGfr1q7bjuZ9/8L/f/OGX3wDp/5aMVna1d6fwNXeKJAya9uvXn39o7rd/+OXnH7oKxFrg5F+7OvtnNP+ZXe98/mDB56oPf9wL+OvFuSiHAnqPdOjXsvq3+rdXyJjS//v95jP0+3yZPjA0KfHG9GGC3+VMA2T9nR1/fPkNQEQBtOm8+2OQ5f/+75CceHXZlGELaV4JYAg4uE3yYBL+GCcNBP5OuV0HwK5NAgz7XAfif/LwJHEZQt/+j3eHzk/eEzqRNzgMvj4B8OsdAL8CRPn6BMBvr9ARkC7rJEoKJ4MOi93uS+FEQdFObKs6aIK6B4Dijm3wCWz8NH0BcAl9+xeof70Teq3Gb3f4TB4YdeDWEz41XRa8TjqacVA8NfIAFAfXwOsAj6z0nAcYNx+B7k2Z9QDfJns05yTLID+pgfJlPT6guSs+T8S+ffvmOk38pXgAKg49ykWDgAXv4kCfPgHNwiyJ4vZLEXhxCf3w628/QP8X+q923YlPPHYA258eARJKmqpAIMO6HCwDzgLuBfBx98ivvz3tC8gUoL4B/yXhVK+mzSBCz4H/ZmxNXHzCyDnkBsB+wMD5VF+mCpW0r9A6hN7lBUynRxOOx2XTQn5QBYUfFN4IqDpAnXdLFmULNSAMm3D8CHVNcOf6za2du4g5SHWn/QbJ3A5UjTK718lnFQGbyyIB5n8Phcd9QKT+oYHYNxKvkDLFJFQ5tVPFtfPkEToPv4Bq8bYdEHegIhi+FFOFDCZT3RPkYR6wCFjGe7r00+RzUMtzgAZ+88b7vsaZatvxXuPqL0XzDH6nnlzhgWIAmEYdqNigJPzjGVJNXHaZf7cfkHSi9PSC//TKPQYPf9khcH/oKdipzdAAklTQlw5DZwT0/7sFmaRfCMKBFxZHfgnxyvFgP6w6dU6T9R/NFmgF7mzvGfS9PXgDlzeM/VJkCQiRevzHY+XdF881D9wCGe8DnDjc6YNAAFad6N7jdIq7ur6b40vxBuYfgW3uyAVUAEkNgn4yyBvD6embpDHI3On6e2G/+7X2J9VBLEJV52YgTsIg8O9GaON6yrWnK0DQBlPeDXHixX/QCgLUQWwA+hAQIgHZAwD/bjqlBGq+eeF9eTK1S0AKv/OAtKA1DV4hE6TLFDINyFHQ80xrgBV+uJOC8gDYGIj4buEmdqqHMFM3+xTQmXxR5iCKf++B58PvAX6XZRIfUHWA74Ethwlz/eD68Oy7nE9fAWHzKSXvm/7o7qeu0O+rzj++FHcZ32EeZHo2FezfGQcCGZY395CbgKoBYJMHzwACkXCvza+P8vqo3++yfP5TC//h73X594Kp/9Fzn6G4bavmM4I8itxbjXsFMIGAGEmqoPle7z49s+3TPdvuZeuZbX8g/bDUZ+jvifcHEs+4/gzNXtFXdHq0TbxgCtznB1iD+8Tan4jp6YQz3938jIUJZ7MRFNj3ovO2BFSeqA6iafGjCDVT7RpAubyjLnDEl+I9FJ6J8kAcUDGb8ncJfK++wLEPv70XB/CoaAFvf+rYomAaZ7JJ/CZ4+Vx0WfbxpXDy4F8aY6YSAMIVmGMaf0DqgBaoTYL71Xs7NF38cYC7JxVAA7/8POXWR2hqXT9C713oR+htLrjPWkUHBqOfpw54YgmWgv/e175Ph27wAkaxdqwm0R/DztR4PRviPwsxpRSQ2Aumsl6+5+jE8U9EwJcoCuo/E1HvX5zsCRRN60xFOmnf0rsBcvrdBOvAeSDtQCYBgOzAhj+zAXzq4NKBauhP6n6333e1yocuv93N0D4mxl9f3gDj6YNndwiWg8z81Ez1EAGBChiC60dIgWf/k77xSQKgHGhaAA3Gn81nATXzCdqhiXnAzGmH8LDZjABQ7TAOjuEYTYWhM/dxdM7gJM4wxCxgfJKiyZCeA3qP2Pw61f1kEitAwwBnZpjn43OMJAlmRmEO4zsE5Tg+StMUSoU+oP59KxDMf+r60G0y5HsLO9nkqfKvL+6cACtFolkvHh8OYQzHNRH3EG/hOoOvV3y+x4My06y2Hztjf8WNcXEq0URUrNWGWmyb3GiX1urk5mfxNIvLJZz0FIeQ0vyEO3qpFY4jLuYim2fpmepuDbIbb0s5PRg8GmyUUXJQTcPkcXN1cv5iqFvcvK42QW6qcabTmZOja9oNpa3nUJcq1hCkH7cqV2wtrqkrPi0P7uWmZLhkXzLe1Q+zCjmsTv6JW53X1gmQa/CgGhuDI7HyXBcmw2feOCPzo1S2ssG5O57MAq7t9MopLqPJDnR/I3NqV0gYsutjqaiZOQybRIJfCH1jbOoydsaLEeRobwrL+czCykrP0u1BPeJL96abytxsN6NlRbOhyJwBS5kZpydyM9jrvD61m1OwVcZDYwI9403s1HMiI3RdGQyXb9m8Pc3X5sjsY6wzNoYUGrfzjEwUYjikFxXfe7DRcv28d25yplXns1bb26VhHFovIMT8SC5Lg5vrY1/ATFRqsmVw9j7Kb7zi1YVDYlQiR51/2bsLfuWvZwho1m1KsljE3rYYbRKOYwxh65xRUc02qX7A5+R561zyhpMOnZvnipvC54UptbbUNuiqNredVvk73pCCJk+OVE6ZjeGHF0ZwKns50Ddy0KqlxWtu7CwvZMxo0pEih8JEMNqbL8/C5YS7bTarKTr20xYfghtG2+zsjHajXDTIDdO5K0a067wyag0Xjfl8q42tebrM6F5e3qpLprFOI3kegYCSJJ/Zip4ZSrqNd7REUOpK35KqTe0bltlSHB3HM28eGedLMIwnhLnNZvrYzOsL2sBnlLSxCr/50s26bBKFy5pW3Z/MuqGxWg6OpjDmamjMcOl2jm60KW58zSIEaS7FpCyeB5DvlKGuPLNEBmVbrOdhmIbwIoFZadWDMuXXTV8JEtvGKHqx2hMmSO7K2ybdrJL1K0zH6hjNOMFhrptlFqELZ3EcEnFT2PwNP47ZhlwixbGLqm47tEeOyIwDAcfynhk0txwXvi0Ty/jsXOGN1LHFXtI2bh2zDqpf+Uy7bWWnuV1tLD1bbTiCzMFgwbqlVkpIXbvDtn1KpgzvyWEThiIq90OW7K8pttzG8Iqscuw0oqh36+NBFYhsY/ppSNeIMOeWZkKsNUfecbQ69ORpmzCotUfZZUQs7avinpcnlBLXWYyCia1x9SvN9ase2cu7ObXNC/KC6CoyX6wXHJ273fJ0rYr1ZrkLPJtnM6Hm7TCj5yoj9Nje6VAnV3YIchQxxcg8lTTG2wpOLB719Xkwq1chyO/SID2HtqzDuOnzQdoNpbRB/GOptZm9Mnx0wIt6XK1Ztmx06rIr0JOnZ63CmxU2t9YFjZ4Rfk6dmqO83/UXl891x5ktkYWJs6NhuHu3DgPYvs5vu1ygdiI3q7gVo1yqyNexiyVywfqqaxodmwCGR31wCtPjL1merebpdnuRCcER6PG2sDgB5wikcC+ZkFLHDt+1zklmDmoW4fiMMM5zz9pFJ0PJ/B0XUNysGwtbok5kg2uXnvWHJUwiCMWHC/UsHuE04kzl5s9W6lrA/Hi/pkU83sn9gRMRSYyrtcyS8jLG+Jm90hXBWa1p0l2s+ZN6pK0jNexVwgHw5TkHGtmusCG7VRmHd66zO55W/amMSJnrlsQi2F780zoT4dRZ7JNBkM6Us1hkc21/kEZhvz20iEnWXS6fI2Oz6Got4TaNTHPNjLRP+5uf+ep6XGSLkrUEjWxiZcMUrAULiE37tLavLjxi2qx97na2vzuKLqOemeGsU3XNqI1VYUF/a5i1tEmM5lRdybl6PpdXp0/VlRkwksqylq9mlblESHS/5d20U3FbXy97cWVdGaY8kMw2pttVgcAjLffhZkkcDWHb1beb5aHxwtY4UcuN0kNvoKKt9puzxZEopu5Z0AfBl04/Kss9b+3n3SlYWHCShnWVOMX1ciRR3kv27HC6CJnB0Wy62HH2QonZ3WbFWGx2xOZCvYwp/0rpJxbXQp88aaKb3Uhf64VE0flSXXirM9Efm4KEr05y0YnVehvXK/+K7Nq5jm8TV221nDYzEOmqGfkofMb3C4E3r7VqqQ1SAbxZrnbEOB95a7UU+OiwgZXYH07kKsLKzi1NbbyBAIRNRU8Xt+yiOvODWYcUUbhnPzqip/0JPTZmFG0x+yANrWU0+o5KWu3imIp/QQ48V29K0pJXkt1yOnlR0WYnbfjTiqoH6Uaxc8B6flp4e3Phz2wL1OTDAdVoVukceok5sVQvcaNp9weLPejmDT9kc1zY1KLIjDqsXFKb9zV5cbqklmarGA+P+HqZ3JzOvigIGfDDMR8znzFWM2Wzv7JMXMsbeGut5TqJPdArzPf1dqBJZ8bKGokt9yfEOjqOki8cTYmtYuOuU6HPYBQJxdnYHdGrqMmxiJ6rJOM3Ysg0nXROzZtu5HE7lwbG8vIpEcJbo1bJ6jr3qmPin4LjQgqdrLqA6rdAjNYv7Jq/CYQYDQJ/K5LepriuC5JBmovWdbVc6XiF7s+0wDXZYdats6BjvVJv4UMcD0ZmlUWWaB59wIb5dTXjh/bAXmt6WxK7en2xaJa1uSBto7XvMqEmzsqxPBjlDk5C5OS3c+syUvYgLq4e3e4Feegst6pra3PrjnzkF/SZDuDeDkEvw9hr5bCN1GSvjGzazvE+StTCJuGZUDjnAcPCIquaBieCpgpSaaZmbthamdejIFwOzSKwMLRYg+zjDG3RKFQZ2R5vJOciQtBYrpREgNlOLtOdRcK+3nlYxpqls16asjCL0DMtz3SREfy1NrvEhuaHRm5vU9zarze+KeEXJ2JmdmfwZBq3Eyqq3AlmWZlNOX80e4WPsto+HnlfPW1Y0ZJEnF/Efrex194cBzDF3SJ2mQ/bSpBxMTit2x19xi9iIWrk0ZMlNMvJZXDcsY6JeGs3Jp1j0roHGVd4m1QOyRYU1JlH7pszh6+twchBg+oheaSU64Zdk2vJr4wVGIzMAOOv7Eku+Q0C+jGiI3etaIqE5F7WvDHDbhsXZa5atjBwB1WwlQZaxRr4d+a1HNkQYDYzLBilrmKFVaakX5SVeN7laTGAxqEGGJ6vcVfuSBD7+iW/3M5YpiPYuEcutZbPb6KjdoU+t22bOO3o2kxPCjOMIzPs+v0yMHRUR1E9WV50W1xkq9WpJspWofZnfbk6zZUV53sI1zTkapu66qJb+MR1Tpk6s440hxRcMJyEN7Uye0II5wQVUCnLV45QcUyBdmfJOPBl5Mx0F0+UyCfLZSOvBufY2StX8vPT5laNFrth0XkFGpetQZ6NjWwJDBVRPp9fL4Jd2MnRTpg91yoCV1WmKDt637mHPCEjKhZO+uVUNRg5EkVGM+eWvOw1tucRVUkVsuMUf1k6HrPheYnxnIWuVntZr0tXSgWclRe+2gVCwl/xWBD7o8Sweikol8PVIEzQdPqdqwiGJEWHPsalUJmvG5KMlEPHKIba72W88aK4qdktNQ5UvmDhpXRxJQ81V/aMEDV8kK9H6RYl+uDpDmjHqttGvywS7TrgS5aQWf5s+7eziK8cGb3o8rhPLeW45XDfT2HqsFAsEtlz2wXbdrt1uwrm3YVBFXmjRwUf2XSoKosr6C1T0dmeDEpu2129EdP9PltqQB/Wz4zbjUP0guKZ021NLZVjb510Jo9dy8KldLMuE3FlhMrR7G+cizWEHiTGMHQqHA3mXCc56gpaPbHHhIgCrOWZutwjxyFzMWfnz1x4aRV6HFDbucfgYbfcxXPh1vdw39jiQdfQjpBPSo0b/KGChcK++qsyHEwvtcYKP94up6g/7hlPbs/BkbxmPH8wT7nB6ymRDkRPt8Ga4SOBUK12STN2wIYO6Dbj9bAUGDZEYT8g+kV/ObSWnxyZ7WpGNCzbDn5DbQJW0BHajHq88ItT4DbKuHC3KUEUKiZ2dk7jJmh1igpB4KbfwYuey0y1YFwE3vYkdm4rCnd33Yj16LF2jjh/yLfECnfWsLquaRPXe57GbvPhaLgIu5sny+NFtqxOlMTAA7HDg4pGJ+p6x7n4oRWv8e56EmO8dxV52+IqRmKbhWvIBtVhEYMvxNo4bU4FV3ZkaPUb2bNvi4ps53u57Et3THmFHsFsW0U7l1YQfYkx8xihkvUmvyYkSXnrUCExbGatbzjVNekhMAIuP9LHFSItZ/ieV+N8QAvEUg5eF+xYoU0Ruz3AYV1mImIiMOGg17MW7PD1LBLKJgr63YCpHeXeLnifr/PBYfyaJa4rd82211NxgoF9Apfsja3XdfJyK+BaR8zcDm8Cn45zNdHSxZHBO/O4twoi3x60I780Kf542e6sLbaGA06lHGaJDxHLMs6wE1HwMOQv26u3C7fest2wtDdM6FbKCr0CQ5xY7PtU6m9SAcZuyw9PLE0sWbM59JorgCGYgV2SpNXloaSzM1HMI7ViS6mu/aJKtxERqdxWzkxOK7EKlZSuqGQVFrmuD49OvMfDi3zdwEjCk1p+TgcGgOqe6a+4bdoJ2evYrWgrKXYFDy9wh212o+jYN8ZI+qVDHkQ4InsyrCPVz2djQyk9xuldvIxFg0JXSC9v+mXfCU7fDwqjumLprhixYupG2MkCcATlHqMuAmnv+vWhzfxGKQKSNGCzdVzn2K/QWo6uMzKz5cPVoyJ/Du9AwVrYXKIgxxmH1ENotelhscwI+CCWRJcaTXqlgwWTuFJ/iUPUtq8AiOe8QO+X+6KnuEPT9bXfMrNm2+AnlyHVPkCCFTVqa6sYCRJpXZisRGZ91kJyyxNz3K8Ra1DWujO7WQqyi9N1Gp6CZmhvFyosEWTkRiBrfe2JpRtoMzrnjxILIChfs/UwWyWzwsbJmrS9dFMxVyGt8rjvshAM1xaBKwuUPxNbfUYbux2D1oma6mBWTVExvUlb2BTgXrHrXCEzPlKsmI25Ag90TtzfGjhanFJtOOede85v7S1G16QcWyBtBLNsGRx0JGoQi0SjH3GOj1OfIaydPgZDRO9EljZnSrBi6Ii4sfSCM4Z4t2JKzkOioUzAiGnSuXJE595skQthvMf2RL7T0urYnkaao3BPuoIZzsC6+rxCOmrNw4uxnwUcTFJWvWaUbYaJNI7ZOcP0+5MbNicj9JS9CGbtcS0eqvXM9fLderfap0YPx1ul7Qu/dZeFQJA0e426W+K4MLqS9o7DJjxP7Y6+hCRgHsy36u6kEjAsidtZrxVgVNoXPqhffOW7V2LJgPRxh+NYLhaLn356+fgyHWE/D6L/zkvn6WDwf+188nGU+PZa6n4IHTj+5zuvz39Lql8+vtReAmR6nMQ2WRc9Dy3/0znsp3/hfcZEYHy8zZ3eoV3bt4P71ommnyS9JIXfNW09fm3KrLsfBn98cbtm+nVE8/V56P1yVy2vphP0d54v0y8VppPqEmxuy6/P33Xcb0/vhgI/cdrgeRk9z6c/vvgj8FTiNV/xOfk1qKtJ3edLEqAl9oq+zl5++3/D82ipASYAAA== -->
