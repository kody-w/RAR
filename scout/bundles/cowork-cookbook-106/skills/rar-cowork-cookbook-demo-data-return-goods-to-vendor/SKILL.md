---
name: "rar-cowork-cookbook-demo-data-return-goods-to-vendor"
description: "Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_return_goods_to_vendor", "rar_sha256": "10493da0b7a7796303585c763d7fa036bda5cc29f8f938eb3d9cc06907fe5ab7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_return_goods_to_vendor`. The original RAPP
agent is preserved byte-for-byte in `demo_data_return_goods_to_vendor_agent.py` and in the RCI capsule.

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

Return goods to vendor Demo Data Generator — Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 10493da0b7a77963…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_return_goods_to_vendor_agent.py` first:

```bash
python3 demo_data_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_return_goods_to_vendor_agent.py   # or on stdin
python3 demo_data_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Demo Data Generator — Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_return_goods_to_vendor',
    "version": '2.0.0',
    "display_name": 'Return goods to vendor Demo Data Generator',
    "description": 'Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bdd80779c8ef8c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReturnGoodsToVendor(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReturnGoodsToVendor'
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
    print(DemoDataReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjxpb9K5qaD90edRf71i8cMSABEkJCYpEAt6PNKpDYd+Txf59EUlXbY79570VMxKi7ogRk3rzrOTeT+vXFaZsor16+vGiBk81EJ0niKKhmTubPFnmfV1fwK7+64Gfm5VlTxW7b5FX98unFD2qviosmzjMwXQyyoHKaoL5P9arg/h38SuK6ib2ZH6Q5uPTyyq9nYV6B701bZbNznoMbTT7rgswHt+Ns5sxqIMPNh1kTZE7W3Ic3lRNncXa+iy/iJG9mtQceV3FevwJtgsFJiySoX7789POnlxh8f/ny64uXODW49bIEqy+dxlHvi4rTmnp+vK8I5iZOdgaDihG4IgPXRVCBJVNwyw/C2fPqYx0k4afZf/zHtXeqc/3Dl6/Z7Pn5+jL9U9ts1kQBsMWpmwD4wCkcN07iZnydsUnvjPXT5nqyEHgyO78+Zn6XlBezH6dnHx+LvJ6D5uPXl7yYXAv8/PXlhxnwxdeXqp2+v05Sio8/vCZ5H1Qff/gup27dS+A1kzCg9eu35/VTLBj4fWgc3lf9EUh9RNQNvr78zrjp84wV0BTMfHm95HH28SG4qPJuCpIXfPzh74n1osC7TmnwT8n96SE4Chwf2PRU/IdPdyf/PJs/DXqX+feXLUBY/xVLwPC35T7Nno76e7Lv/v8fopM4Axn/5vG/FPdXE+Y/zn76u7b9bxM+zcKvILGTuAPZ4SbBl9mv37Q9v/jpg//95oeffwOi/6EYLW8r7y7hW+pkcRjUzbdvP32o77c//PzTh7YAuRY46be2Sv5K5l/59b7OHzz4HPXxj3PB+kZ2zfI+m71n+uzXvPi36rfX2REAiP/9fv1l9vt6mT7z2WTE26IPF/yuZmqg6+/8+MPLbwAeMmBN690fgyr/93+fbWOvyus8bGaal7fNDAS4idNgUl6P4noG/k+1XQXAr3UMHPscB/J/ivCkcR7OfvlP746Zn70nZkIT7H3zAfJ8e9j+7Y5335r82wPvfnmd6UBuXsXnOHOSmcru918z5xwA2ANrFlVQB1UH0MQdm+AzwKHP05cJJX/5R6K/3aW8FuMvd8yMH+ikLtYTMtVtErxO1p2iIHva4gECCIbAa8ECSe4BbcIYIOonYHWdJx1AtskT9TVOkpkfAywHRDDeZQNvfZmE/fLLL65TR1+zB5RiswdD1BAY8K7O7PNnYFaYxOeo+ZoFXpTPPvz624fZf83+t1l34dMae4Doz1gADSVN2c1AbbUpGAbCBAILgOMei19/ezoXiAHcBAimisM4eEwGuXkN/DdPayv2M0qQMzcAHgbeTYu8aiayiZvX2TqcvesLFp0eTQge5XUDWK0Avg4ybwRSHWDOuyeziaBAAtbh+GnW1sF91V/cicWAiikocqf5ZbZd7AFf5MlEgNWTP8DkPIuB+9/z4HEfCKk+1DPuTcTrbDdl46xwKqeIKue5Rug84gJ44m06EO7MsqD/mk28GEyuupfGwz3nibknhr6H9PMUc0D1KcABv35b+/xkd3+m39mt+prVz7R3quDO60CVcXZuY38ig789U6qO8jbx7/4Dmk6SnlHwn1G556D6163ARNqzibVnz+Zior4WhRF89v/abUwqs6Ko8iKr88sZv9NV6+HKqUOaXP5oqgDzP4RNZfO9G3jDkjdI/ZolMciLavzbY+Q9AM8xD5hqK+AvlVXv8oFiwJWT3HtyTslWVVNaO1+zN+z+BKy6AxWID6hkkOmTzW8LTk/fNI1AuU7X33n86bbJcpCAs6J1E+DQMAh81/GuQKtqKrBnHECmBlOx9VHsRX+wagakg4QA8mdAiRiUDMD3u+t2OTATuDas8vT78HgKH9DCbz2gLWhBg9fZCdTIlCc1KEzQ4kxjgBc+3EXN0gD4GKj47uE6coqHMlPX+lTQmWKRpyA9fh+B58PvWX3XZVIfSHUmTP2a9RPK+sHwiOy7ns9YAWXTqQ7vk/4Y7qets9+TzN++Zncd34EdlHcy8fPvnAPyr0ofCT2hUw0QJg2eCQQy4U7Frw82fdD1uy5f/tSqf/zXuvk7Pxp/jNyXWdQ0Rf0Fgh6c9kZprwAbIJAjcRHUd3r7PPnr86PAPt8L7HOTf34U2B/kPtz0Zfav6fYHEc+k/jJDXuFXeHokx6AugS+eH+CKxWfO+oxPTydk+R7jZyJMyJqMgE/faeZtCOCacxWcp8EP2qkntuoBQd5xFkTha/aeB88qATCenSeOrPPfVe+db0FUH0F7pwPwKGvA2v7UnZ2DaduSTOrXwcuXrE2STy+Zkwb/cLsyAT7IU+CKaYsDaga0Ok0c3K/e257p4o87tHs1ARjw8y9TUX2aTS3qp9l7t/lp9tb/3/dTWQs2QD9Nne60JBgKfr2Pfd/+ucEL2G41YzGp/djUTA3Ws/H9sxJTLQGNvaC+w/BbcU4r/kkI+HI+B9WfhSj3L07yRIi6cSZKjpu3uq6Bnj5ocD7NQOBAvYESAsjYggl/XgasUwVlC7jPn8z97r/vZuUPW367u6F57Ax/fXlDimcMnl0gGA5K8nM9sR8EkhQsCK4f6QSe/cv94XM+wDbQnwABCIwzmO/ALuVQFENiMEbQhEeRmE+FDoyRru8QnocyIR0yGB24mM94HkwyMBUGhONSQN4jKb9NFB9POqGO49EeheA+QzmkF2Cwi3kBgiI+hQUwwWAhTQc4cM/71CsAxqehD8MmL763qpNDnvb++uKSOBi5wus1+/gsIOboUKbs7iKXqciQrS/MtRk2x6bq3KqSgzKocdTrYUdzpabZDTuth9bsFVFdlneOXUUbfQgcZ0lMcpP7hZanh4zyKEW/7FpZ3bODZzLK3vcMnj9cBEpuy+um9tfklpRP+DU/pQ7F81Sm4tfEG+YbWxYPRwS7oCQ9h+by/Mqbohq7mgZxKeSlxzKxyi2SGCOimrzsirkSD6GgrU/cZa2F2q48eapw8/fVJnGETWLVXaIRVX6Utse+cD1ZJfe6XTNhdgMhyC60SoxQ2HV4K4iQaZQaeV5HzsCjDFKcygZxjVOUqkN68kppDHCHdq5EpyE7DtvSxdGozSNTiX4raAQjbPvcSKOmvvEkszdljnBGqxLKS27c0HoNykWwo6jBr+umcK6ZshOP1fqmRV6EBHl2VDZQeLk6TNZ2VqVkXd1Ipr9XDaXYq6Xh41h8IFw5NbbXLma4NXkwZJGJGXhtHYO4bRGt8ShiEA+miEhNzi7K2unIfp0GZDLsowg+Bcluh6QqTHEQUuoHb4Qr0So6BOObsrT6dSESXWkRyp60OCvdRSJ6M06NVeOEXOJpKycpkipjt+vjddccC1s5LaRqt7nurIOAeuuK4ZFKIK50bZN1Y+6Vg79xU44kCRskcq5b1RER6KFd5YzVYJFwTN2OwFKvl0VfVbka8WzRJcmNNu5PQbzzu+3y1paJtnBqibYsCHDPdrCzNCeIIrSz8x5bwWrtCMHaagTltuJzXx8V8aili9MYDUuiYtBQN0ySytub2aMalkRk4wilT215TiwT0RZF3UgMGGk2V5hIHAfJmsIg8xYRilLGSNs28bWMyxmurHpjX8vrY18V3K3Fw9tyCYTLFGlDQ7zoc0ipaQqOrygj1FfTOZZlffOGfRzIx7JYV2k0Dmd4sNxotRK3TmrvEZXEUHMZXEk5cTVdWZzMQtY8L7aRJOy9I38AduSlLCBFzLWcSosH2VeFfQZfFtKwTomVv76whdjxR501D+rJJGz9mAYrvvc0RYAE0cp0OgpNGVm2YqaK6naUq8s69nnfIOsat5R+pVwW+oW/ba4hgRfG3B123drtlhDZRCCszqhDGSRY5Fxf6o1GUJ6QJUw4jO0SUf3LmheXPMgStfV2K5On+UC5bg9caI0ye7SqkGH7cIcedxlS7mFuXvYr/hwYdTCeVCU/LUKDcWV9y5NQSx9vio2OsttHcLFjlCSEBlkqo77LxHVBlPT5klOnE7MtoWSr83QkNLZEh4reFHHWD/w8J/j5riw1yV4JgoSMsBkPkT8eTtr5zCwp8nyQ+qQ+isXNolg9RNhOLCt1Ec29hXEdo4OWQzgnWvy29PIN2qKn3TyEB2KIRs7LXHZna5vYvyY+4li9XyTbq4rlEuyuNpU3Xg0zEUWpODpJupJzD4ecBX3Tru5CRDc4lLllIepufVMuiJou3ZN+nO+ZQCeWXCfcLNHWCV0fWO3SyJCMxsYtqMSL30JLBFckjILSOb1CDiFLz/ctxXEwtFnYi11joSv8vL9I/LZBNGFvb2LGW6CE2w4ZC4NKZUUJEUl7UcoXih/ouY2xUmRH/tYCFzKBEkvpqkEHc6tlbR1jHnxwN5IqomulPXLtdZQZdb26CfZNGFyDZyNSPatrrT3Fy1vk5g1W2GSg4Oyl2WzaxLIcYyn68jW5ypIoDJa/3hwXJGfb8jkt1VVzUkTI8xh8cyhKPjtZrDm2K7MCReuEyjXps+2tqqhNl9lzr8OIUQf7/9xVD5dbO9e0i1zOecsMqm2GG9wBdoQszCg87wUaCw2v7WtFWIihlGTo3Nnv913jzqvECwtiTpxlQT4UTqecjrvbacXJrOSXh2t0sfc4M6zP1xgxNyU8HoSGxmD6dtobx4HpeVdzYsI7l2DgbmkQiLaBY1hnd5i0h53+BEiRxeKEq/oj1ndpDlc5aiG1udoQOpZFnglpqXE+Ef7c3d7sPD5ym91ZZglFrrO1GtbHvryOyh5q17SOA6bDCsfbHWHCSRT8orTIzje4yMd3i4K7Wkv7VoYbT88sSm/5olOTG68Kl3ThRiwBhcVygzUdJ3bu2R/ocXU6wfGGsMycvRwXpQmIfEmZ5gJrt6DYaNJYIMQV35oirfSl2Vhz8kKc4TMhGvi2crdjFJaacvBclvFU/WgnZBpLhiyERGmvjkknUWyh94SWFLCgJgNvn414D5roZUQQ1bgvgnbcrNabdeEulrK55nJuiW+luPXiC1HHpt4QC0HboakojURLjvbhtKUZyW6lXVywa6kkXa/BQuZYZQ1/2jLbtahHa9M+bWpTD6x+c8Zj+BIvCngZeKWfWpG+6LAdIrUiaFmq4y1xg9sqCxwhLxPqxHZ257tGyUciIeKIyC+BXGvkLhcMG9fSIUUkswljbVVg2pUQeFPSkGDNKzIR5qzNaLjEmIKfL5P04MMaajW3hTY6p/W6YueGYl3W0DZZrdV4LyYRQ4EuBWJy7Xq+9RuoQCDiDKoyM30aE5vsXOqnnh2p7lTbnIRGO6cox9smC6Uzw8xpSG9IoiEYXYE3xRJbC3NEP6KLNemHmak5cKrLNqgOJ71RoUoOCbmtePJYz5HgNlaHepTEg2QHfocy6/3ILyIWdTYjwem2doqyekmsCmHbHOpaUhnFPc5VYHkLCrjbj1dFohyvOErp4YTRpJpUnCgbNVmdN4dkVwWhtkiCZuUKS7XFS3NbWmnrOsUgmuMGP8+Xa/Nm0raxiMiN7S2LWIwOoWdgmjQOPehk43HJQwiMieyVVFmi1kbjjK2MeKXv+SywFK+RwSp6WMgKvKDbQIMTxuohDjY6ntzVg95buxsZC6a6OJYOGeOsfD0tq2KpXqKtuSji2+kQ8QslhfAx95fxiMapJNtnZL62jNMg7A4SRW5pud8Qy3ShIuhY2jAxaAl3DS24SQU9H+sqiTXDqeNbiQh4Yof2yYCK5T7yFwlzg5ftGbNOoaLEvjYgYLOnA5hvr6q7xccqOCkspoebiy7W5KpUmsQgmRSnVaxO/bi0mVuARJlcVyuLw46q0tWFuNa1qyjBkgaIRbP3hjJgvof60drwJKGiJV6OwhPXWYeN7N4OB1+4jPGQVOnc7jCpWrmoA8UE1SbNDt4ZTlWc1lITHMkyTfjlabw4tEQv2x3rA/ZzVa9hJVvuDOnk70doOCiJugkM1dlv53kfoxjos+wcRreHG+/GzS6WEXaDGdYmvvCoNRAuTZ/UTbpsF/Z11JtdCs9V3s0unQCJicDqo3zJ3JuiuzFzSfMtIwlw0XslfNhKh81R7rXNpU1Zl9e2Cuq4sNmLW2h9Hkk7yznQa287hpKtYg52DJdTdD0fbn0FVcqGWdKW3YF2XqiaShIxLeYuCS9UbpGdjBVPcz7dHklV97NrjPeyhp3VQp5Loo+PKShvgwyO+0ITIlJDRR7PV/55XWdLRY1bW1ZTQYvScesQcuKIetWGprPhSmzrsGzDImPir3Dxls9XwenA6Yt6I0UcD2FI3nun6xHslQ+ttht6+uCcBtLYyjpuI9rBDU9XZyjJwhUxZTtf9xR2xG6LpTLPy3JsQY/G4bzrLHSmckCHTFpW0mV9mMhzjarWe6E9Bts5fsShNdfijMAgYYIW2LSv5E5UqmLBamEjLlO2zNk32cGkkiFeqi465G4lckbCN6saW7Ywjhxo8mjva7RdjiG+VbiEMJqmSphayeoApdEUk3L6FizWzvaCZqQEH2DAWCdmESxYyF7JAOKWDrQMVKZyfeOsiBgL1Yyv4pMTJFPHrCukUiStcJcAV9BdBDbNR7r2j06gXLZYXVJyzLr6kiaXmb/Atm7gVmxwGfoOgk5mBvHLvDheClOAoFiYB+es6RTKYloDCWJX19A+ru2QVVxVUHHRjUlcoExAPEZzTsfbPNrj0fJgbSGtUsR+LSgKtl6c6QE6nOMLnTIHk/WuF0jO54pvn4riSFOYqfTt1Uzg3SrGz4haiSe/L5eoCVNjBhrybnOyV5qUJPTKM3ChSQfVW14FypvrAOFgr8dWnj0HfISuawoQWtfO64pY4CRVbeEoLno42sKoFdTuLei3orYYzCGXiwL1YslZzRH30tmmqu2hBiKHob9crilpX1DWjhcSRe81Cl9FuXJrIXt0F1WCdiudPdWHBSqc/JREu4zwTnMjgGmqX2cuc6AuBUoEA0mNcGhJJcvuKaUiaGERLg5tkvOH5nZWFTwLpGWuxgzPjICMQoCSy3qIgiBvBTnkC2nwdqboLZsNR3t9fEn6fLulhWad7oM+FLUwPiayyYdeaHM0vuQAcXWLTYobmh/uaDrodElCeQs9MwY3yAInh+EC2xE82F1ZjsUHvSq0t5Drc16JUTGv9xQT7eWj60Uith9lfKklaR/NRxR2UZvq5FpdYBtXuaXXbghuW0te5RxqUutU28+Ph6JPW1OlLhiPd4zHYQ3aqqjNoLiO9GvPIlsu2nuEfhMv51AUL1UPWdnOUvhRUbog3+93g3tDTitfZsG+tXc3l+p6bAVII4kEPSoMQFIspo7pwSIbxNyqg0+xKqlg5/NtCbOcAxVab8LH6kpttQ1LX1a04XRxyR3HcDmQKinXKdiGdGbSy7uq9dYNfhAjTCaknpaRpJ0DwJ6jI3RpA44JiWSOxDwHofOQ0vLA4jqdipDRpivXpGz1NFcdUfSNHRaGgzLsiHwfuCe7CbvehIjGSvqNwlTtGjPhxLuqUn+m+kjnWQQvc6ymat0TRktRG2NuVSp8O1JlEnKMHOL9joX5Ky4biGfs90xfxcpFg0RslZ+6HQz1JBYVmVDvmy1Cc0a2z9QgGgFGwYqsJyx67pVrfiC60lFWyv6A1CMRtI1EBHOsc24JZVF0iFjrc8APukJSfWsWiH1e4sF+iReVQ28ogkPSZc4KVbRQ5OogEB2XqoIZGCid7g5b0kPYVAyjAxpa6V4DENHYI73o9540JPRGo5BgZDsMOi5Mzt4vLlwINuz7+pCmJHUZdGorqyQKKKVDvWKncOXCwgSbl0uY15rWD9NsketleovMUxh6Nzaw4JFeXc47+IrvBLBSvj1K8MKQWT2ByrML5ddNuV63HgxdKh42FGxLB5E+t9HrAJqoOrhA/WK5tlBCiK8sy/7448unl+m8+Xlq/E+/EJ5O8v7PDhQfZ39vb4/uR8aB43+5r/Xln1fp508vlRdPCt0PTeukPT+PGP/Hkennf/TOYZo9Pt6xTi+5hubtcL1xztOfB73Emd/WTTV+q/OkvR/afnpxwbY0C+r62/Nw+uVuVFo8TrqfRrxMfzkwnSjnYDKw4fl3Fvfb08ubwI+dJnhenp/nyGD+CAIUe/U3jCS+BVUx2fp8kTEdv05vMl5++2+M2bUniiUAAA== -->
