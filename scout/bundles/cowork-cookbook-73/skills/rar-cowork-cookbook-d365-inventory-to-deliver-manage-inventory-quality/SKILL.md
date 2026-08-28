---
name: "rar-cowork-cookbook-d365-inventory-to-deliver-manage-inventory-quality"
description: "A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality", "rar_sha256": "221d51820f2b88d9a78284b82bd1a2fac978e6a5146011c4c648fcb32920a4ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and in the RCI capsule.

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

D365 Manage inventory quality Expert — A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 221d51820f2b88d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_manage_inventory_quality_agent.py` first:

```bash
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py   # or on stdin
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage inventory quality Expert — A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality',
    "version": '2.0.1',
    "display_name": 'D365 Manage inventory quality Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-inventory-to-deliver-manage-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc77cdea1b313a26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'inventory-to-deliver/d365-inventory-to-deliver-manage-inventory-quality', 'uses_skills': {'custom': ['d365-inventory-to-deliver-manage-inventory-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365InventoryToDeliverManageInventoryQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365InventoryToDeliverManageInventoryQuality'
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
    print(D365InventoryToDeliverManageInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOj1pbtX+FlRzyXW1XJIBBS3bgRLQESSIAkJgm5HGXmeZ5x+7/3QVJmldt2v+fo/tCqykgBhz2sPax9IH99MZraz8qXzy+yY6TQzojjwHdKyEhtiMq6rIzArywywQ9kZWldBmZTZ2X18vHFdiqrDPI6yFJw+xqih9RIAquC5gsC2v5fmRIgp8+dsoYqK8sdG6ozqPYdSDBSw3OgIG2dFIgaoKIx4qAeIKN0DOiDAcVO68SfMKhqTDtLjCCFMhfi3pcDMbYTB61T/gh9AkaBLxW0hPg5lJeZ5VSVU70C85zeSPLYqV4+//Tzx5cAfH/5/OuLFRsVOPVCAyPfRSoZ/RD4MO39/PlhGBAWG6kH7soHAFYKjoFbblYm4JTtuNDz6EPlxO5H6F//NeqM0qt+/PwlhZ6fLy/TP6lJ7wjUmVHVABDLyA0zmFS8Quu4M4YKKp26KdMKMqAKYJ16r487v0nKcuif07UPDyWvnlN/+PIC8C2NKRJfXn6EshLoK5vp++skJf/w42ucdU754cdvcgC4oWPVkzBg9evX5/FTLFj4bWng3rX+E0h9xNx0vrx859z0edg9+QnufHkNsyD98BAMggLgNFLL+fDjX4m1fMeK4qCq/7/k/vQQ7DuGDXx6Gv7jxzvIP0Ozp0PvMv9abQ7C+nc8Acvf1H2EnkD9lew7/v9JdBykTvWO+J+K+7MbZv+EfvpL3/6rGz5C7peXZ2obZux8hn79Kp8Y6qcf7G8nf/j5NyD6/ylGzprSukv4mhhp4DpV/fXrTz9U99M//PzTD00Ocs0xkq9NGf+ZzD/D9a7ndwg+V334/b1Av5pGadaBVvCW6dCvWf5/yt9eIQ0Uqf3tfPUZ+r5eps8Mmpx4U/qA4LuaqYCt3+H448tvoF+kwJvGul8GVf4v/wIJgVVmVebWkGxlTQ2BANdB4kzGK35QQeD/VNulM/WjAAD7XAfyf4rwZDFoY7/8m3Xvqp+sZ1eFbdCJvr43w6919vUZnAln0I2+u/ZslL+8QgrQlJWBF6RGDEnr0+nLtDStJyvy0qmcsgX9xRxq5xPoTJ+mL6DhQr/8fWVf73Jf8+GXOycEjw4mUdzUvaomdl4nBC6+kz79tQCNOL1jNUBlnFnAPjcAbfgjQKbK4hZ0vwmtKgriGLKDEkAzNfVJNkD08yTsl19+MY3K/5I+2u0cevBMBYMF7+ZAnz4BR9048Pz6S+pYfgb98OtvP0D/Dv1Xd92FTzpOgAae8QIW7uWjCOjHaxKwDIQSBB80l3u8fv3tCTcQkwJiBFgFbuA8bgb5Gzn2G/Yyu/6EEQvIdADmAO8kz8oa9HAoqF8hzoXe7QVKp0tTl/ezqgZ0ljup7aQWIDffAO68I5lmgD1Bklbu8BFqKueu9RezNO4mJqARGPUvkECdAKdk8USN5ZNjwM1ZGgD43zPjcR4IKX+ooM2biFdInDIWyo3SyP3SeOpwjUdcAJe83Q6EG1DqdF/SiUydCap7+TzgAYsAMtYzpJ+mmANuTkBa2dWb7vsaY2I+5c6A5Ze0epYG4H6Ayp3MB8hrAnsijH88U6rysya27/gBSydJzyjYz6jcc3Ci9L8eLpjHKPKlwRAUh/53TSuT9evdTmJ2a4WhIUZUJP2B6jRyTeg/prRJLUitRwV9Gx7eWs9bB/6SxgFIkXL4x2PlPRbPNY+u1pTAQWkt3eUDkwGqk9x7nk55V5ZThhtf0rdW/xGE/t7XQKhAUUcPfN4UTlffLPVB5U7H32j/HtfSnkoc5CKUN2YM8sR1HNs0rAhYVU619gwMSFpnArDzA8v/nVcQkA7wBPIhYEQAqgfQwR06MQNugjJzyyz5tjyYhilghd1YwFow0zqv0AWUy5QyFahRMBFNawAKP9xFQYkDMAYmviNc+Ub+MGYag58GGlMsQJxr5/sIPC9+S/C7LZP5QKphGzXAspuyyHb6R2Tf7XzGChg7Jc8jSr8P99NX6HtO+seX9G7je9cHlR5PdP4dOBCosKS6t9apUVWg2STOM4FAJtyZ+/VBvg92f7fl8x9m/w9/b3twp1P195H7DPl1nVefYfhBgW8M+AraBAxyJMid6s6Gn96L7VOdfXpWz6cHQX137VmIv9P0AO4z9Pes/Z2IZ5p/htBX5BWZLvGB5Ux5/PwAcKhPG/0TPl39kkrOt6g/U2Nqu/EA6Pedg96WACLySsebFj84qZqorAPseW/CIC5f0vfMeNYN6PGpNxFolX1Xz3cyBnF+hPGdK8CltAa67Qkzz5k2QvFkfuW8fE6bOP74Atqe8/c3QBM9gFQG2Ey7KFBWU6sMnPvR+yA1Hfx+V3gvuKkFZp+nuvsITUPvR+h9fv0Ive0o7lu2tAFbqp+m2XlSCZaCX+9r37ecpvMCdnT1kE9+PLZJ08j2HKX/aMRUbs9mO9nyVr+Txj8IAV88zyn/KOR4/2LEzyZS1cZE4ME7o1TAThuMQx8hZwJvIk6QsQC/P1ED9JRO0QCmtCd3v+H3za3s4ctvdxjqx17z15e3ZvKMwXOuBMtB1X6qJq6EQdYCheD4kV/g2v/AxPmUCBoimG+ASAxDbQJdYoiLmculvTLIJbbEzSVm2qiBgdlhRS6dhUGg+AJBUQu3FvjStcw5tsIQA3ddIO+Rt1+nESGYrHQQ15mvUMwC1mEEga9QEjNWtoGThmEjyyWJkK4NOOPbrRHopk/XH65OuL4PvxNETwR+fTEXOFjJ4hW3fnwoeKUZC5w0e/86KxeOXkVUrFyVfn+zqTKrKzRpr+fjgDfYgtapY3eec5FyMwNk0w/oLA88pWfScHNCmpm10wjGUJw+6A4ibp3l28wUmhvcslTGedVu7NHVko/JvXJYqIiYaEOUK6ZwIeXCWMy5UlmRUSG3LK+MM16Ht1WyTMSwwDxuCcM2Sw5yEMzN5KgUiKxKuVTaioVeZC+X4kO0iIo4QlxKi7eBGO/TLhi3A6aTA3UuUM0pjhtOYaR6WR35E563LBeshPLQa3aY6Sy/wq0rwKYN64Ui9rO2rDHXVpbSbd4PenlWTa6IB9MLCDvx9pYhgw2PVXPCcMKlrL808nyDJMZ5UQTn3jX2GBmqhVHMdUbQYlTdLKzFcSS85WyrbqPVNdb4rjqbXlbze4oO9QFBQKcid2evDC97/5gH8sw2m7I0+GtiDfM6KQlayLy2QoP9ubokMqcIkbdzNHRX6ORWPWRx5K4T50xtfQ87J+pCxhfk5YiO7UBtqR0bbU1vvbXxHC5pKidNeePWPs93yWiMNwpReQ8uLnzXaMY2ycoWLTlVumk3xkjVqyg4Ab2KzskhzMQ6QqjwUibX5kiz270pJLI768xDsrgUjhbr/LCk+17Z0FeOspSLVW5ENxayGifl0Vw6znEtXzntRtzs5TzbW3Zxo7BirnSmsOs76ZKYZb5IBF30L9xir/YA6SzdsnaSbrFkUFe9rc9jaVse1ihnkYS+PHHXfadv2yuTCBUH46nU3A43h2NK8aSw21NtDkdqGxbUpfMXGyJcYaaiXhckL5DXDgvg2COFlaiTx1sni0jZgLg4GzEpKSPemQGOyQN+o8vylJwXKBnZtH5ll7cyxvfzhRnjRxbpXJ3SzLlcDbvrih3C5Hbi0RVxOlW0h6sLrG4VOxOq/UXaVlHI8Gl+m2sX5EBcfK2QbjUt5olNxDUu5rf+YMchcgroEF/hvHnUKgBF4R+x/XpxQ9HopFXLwYMHJjdGBj3HudFdyk3kr7yRqtajLvSa2AvD2l/7TYtf0s11LW/Hk7CvxiPdC6xeysL+UHTHdn64JLWc6O2RCc8phWSKczowo4K5YoK5mXwtt0ytsepxTs/SJDBv5MHUfHemNbJ9FS9HWSObduUuzDpB2ihaurZ/jROXn10PeKtsGS4JvXRVnbFWDpKzE1ZqVwT9UJsXvyUCB3eEhEdEsrCPahsIcZFxM5Y+WA5C5OdANcY4hq/LbQpL2B7Fcq6P7e0p7nE04asrzliUbREISTe1VFwuJUNZe9Qx8qu6wLWFNospTNvE2qAEWbkty3wdV70X+wTOXomdOQb7HMyewR7emPAQOuJWiw8tGcvIQjc4SZzJMEPNDumwrroarY6ufl7hrk+LbBzsVhuqOWLqcOBEq+66RN4geNSc4zBHxYN4yLs0nq8VOdYEV5cGSxeJbXo6MnuP9WZ2E6iNiI0OchJlRHRQZj4XV1cJaU/emaxKrlBF0H2csmGNFmPEAr3YR5JewtuNVcLH3rKuHidc7ZoTbzDf5LkkN+l1URAnwnMvnV0D9hkuGTGu4eRq6ySiy1p0PJ924mbXnml6zAhGW8H8fL3v533FtEapDbCr+HGHqhfXs1jmdowxOlsyPC1wtEp5uif0MD6PNEPg9oHIx0Pk7emoankfU1eVCnf6+Uj7Ct6zXpqZam3dDht9ky6Dub9PrB2ucVyxkTpy6PfH22wvxYZurbye6HKmyELR2LOhFpLbUSWwkR541QfQiOZNHFYnJZ65ab/f4/Q+FGUnDhf7g8iUxDyRkgpxfW/fSAgvLmBYYoOun2MjW5ke76+5AIbp/TFmO/10JfELTS66sDmc+jMi3+JTG8C3/Y2CM8Y62Cw9Xg+3iyqZ2rC4HIv+fDyuVifA9Yxv4DbvSVeNstzTKQ+WDT0OxulkCE5yqBKcU9Mzd6tCldbacnVCfOrAIeW53GhnrasOOuIR9taOTrysIGAG1ZKxno8NLnTe1YxAopRCRQn2VWXL1cVMj0emsb101NHCS63r/gb64Jqu5yvB8jZ1vBOvtJp0CcYIARGJA+xJGyY+G7RgWBVb7I50cAu8W8ILvX5Qz4Rsb0y5ITY5761WbWkHY8MZ233Aunm52uoel7U1vb3iK5oyB0C5Bwyu51c0p3BmeagZiaR6vy8q1dvz66I4EGTREbK8S8kcw2MsDgIkjsetrG0ROOtym6s3ueSlTFEmZX7ySUWNUs3ED+BaQfnZuaqd9dlj2vUyOMTDQdMkoz0pKBOo236YqwefrR0tizA9NsI8j/CQ2C28ctvSc4R0SAQ7aIjP2A3ebcUAZah1g6EtN1w3YX+WzvuVt4LXgzoH5s6XZKFpNHE8oPwME1s/0Fr7gKByz/d5h5Y4sV1HxdxbMmvpaC9j/9ht4KUtUidkH1rrQoOVDBMXQky3OnG54r5moLHsF1e0ibjbKeh4m9bEwU+807ivrLgIYopjaVGi4eGQI9RZ2PD6YKYsrJKFCtc77XBcrR2EhskAwXpHzLAqO24sgpQ5lt0QO+Q039V1quZ17Fg5LdHcuYZXpBvUKSJ2SJQU54y1vLNp2Yu8C3Nk54pjXhlCHaYEatz4mmDLneZ1toJfr6SGK3xNMR3irIl4MV939WaQqsrb+q1arVetdj0glw0ZCApz5G6Lo4QxBLY6Kotg3FUZhfD00YS1zhMOGmOc+MKwuPMlCDU62Re9sO3I2qejQ4GTqCY19YWPtYOKs7IvlVf8aK/ZeK3PWasuR2nNNhiDOKwSqFTbrRRWYWngZF4YiFQU2XnPUsJODBMqUvU5xdnMcnBRNmRzPa8TypJHy3M5sFU/uDNG7VbNvr/U+U716OLgqutiyfWEdFSVPd0Wo5nJcapcwLSQ8SCHd54QFAe+bmSLOTU4s8b0pS+vVkc8CNcHvJQvjJ67a/tykm1vX6x4/nDlaI/nYky/7EuqaJI9rxXIkCgBGHw1i8Rat1e4aKbNtdN5ptP2QMJD0fXmukCtm8uMlyC60jvNtwfcyITLMrK0eDg7N7RmU63ksMjF98FSM90GDGXFbeZH2jK1JabwxzTz+eHssud4G3OZksz2hAyr1O0mX7aM5rqAy4n99bywmIPXCTOSlchexnKkwJzOWKU+0u/YbV8YXr4+ll1tq57nyfE1HJNTtAj9recZu/wo7BQ5Em7s4RiDNpHFSpYcD7uELW7qbmuabbKOyeXeZ4TZ0b+y2I0Ibwezp2lZbLh+Yy0ThSfQTXsR5VQfQyM+xv6BxsnYHVQvPixCXE+QMNL1GhE0lwUpa+/4q2ptNoMr5xfmpt4uHbulDH8YVcE6CfpY5d4pTdz16UwvBxLLSlVEyQY31C6hgGGnWh35QglTTyVGZGvNd4kdbcMtvUtNP6XOLGsTp4N2HLN652ZeUp073sLs/VWIDJHJ+zZyJEmXCU0rLE/0PaZcI/rB3HdUGNRHuhqp2XnMjyf1RtU80hBstPC9RX6+qKertAlat2Y22NXpHI/Kicbf9340m/NpigvrUkIOocot/Rm3RuwVF+GxrZyKNUUaURLmF2O3XOlLi0zZUT8YxHw1F3awGsc3l8cFr9glCyYkmiBflgtCEhaeAWvwLDlxFXnZIyRq+magW27X9J21dVZtneREq1klGWct31rJUkNvYLfS4A0PV4kta2Or75zaxckxZw4ZlqOSbIpH4qbsYs4QWXyc28u1aAh0uo/UuWlxThMZVXPLl14t5KNDCumpJxVxfYUxWJ5tQ1W+jfYluWpEdZLdeL5ildDzxSGBRxQDjYydEYpBlVt2cRHKPtvxpgdnmADnTE5uRalsdqQ4LssbOqxLU0Jchb2t5m3pliVj0eFKgmdulMLrKyKnR6Moi7bFGzg9h3OtdfEZzBnXm1JLdLnBojo6h9IhW9KtJC2VBTWmfnDrTMmGz5Elbca54AZXJSg5JqRvQ39w9ZPH77lx3zKbXhxuJLHYhWmyXSwiWFgxgyBqyDXRPGflj01uLNBonQmLRhlT1tHxYy+GZnbRL+cbfNaTmX7rl4jahsGqWQhIONu1CtgMm9PeIw/QCj/5M5JU+IgYiLkh5fxGo0HXVwrAgC2fbvJhbfCOtrLr4zxXV6xubFejzcPHQ3uBa32p6EM+7rLhlG2SM5fOu1XdesVhSdbkLNxXud2gOplRI0UZXRlW4w6tyUMwx+ImxVBKGVZn1bLquXhlU5fPSS/h1hZsGW7aqfvlIVhcPGk9j7hAlHar7MSlW5wjQ3OWHRnvfCR328Us1QvT80vHzBfklnEL6sQKS1x3NNAYuVHd+wS24fQI5kjRcLjGcnWFwHdUfR4dZmP2+Z6cqTSKL4+hZNM5yi68o7TPfIsHm7OWA53oxJhrYklJm/kN34jO2FWzgqRg1qKLgmjcK4AWXTL9yIr71t+2SV0fSYNk1nXPzKtVTyBna2zo3uDLWMDIZEQyTZC6EkUsXJvl/Mm0bZMqI6KxraXQWIedIJBlYbp0S4H0QbfiZY4DdXaI0MGCjuAbuw5HPqGtizGzdjpFZqzUoMpVHDNRZEmSt4rCsBcOWkS2eL7h/Hbh+EG/2pn9WWyugePhXD8TkV07aM0ePzNquBLc0CJ29G0XZstduxGKWRGTctCvT8UKEUUYUCFrkqTXUGQ/N2Ez3bR0enHPMUqS6QLtjgHRw83MJaVTY21aa+7Xo7dciGCqPJMnzQjiuU0jIQpLzSa9MhgBthKIA+8dMOam2OKK8BW8BZxy4aING4Qpd2jX21OoXetYGOF9I3vaDE3DtdE0ytal6+aKpxaNdOtuUOPV1R2jiMSogDfqNLOsXXp28pU9GCRq8DSop40cmcUy0d39ihXpDbLGT5mwzTiLQUTbYRKl0rFslzc1ecH5Q1Ov5lnuNA7aonrOFutcvSEn7DxT/PlG8fHZMQqa4pwAZ5adFW0MfF36uLpX9DXhSjEdizAvZgedvXWkvF+r7qFuUNlbyY1/RNm9ErPZMNL7BWotcWx5ddgU8ZpgXuXNZpWNbkMM+rW0+J1L+ObcIOjcniuxiI+LQdmRIxWQ4gYvzWic+d1hvciXA6qm5FwgyKNhm3TY7QzaYgP05uq7g2fIORXc0Fl+lsjotl5QiNiKJ3zbzwKaCG0WGYtFgjZuE3rkru1YUPnsxVeL9Xr9z5ePL9Pj6edD5v/G6+bpOd//2OPGx5PBtxdS90fMjmF/vuv6/N8x8uePL6UVABMfj12ruPGejyT/00PXT3//xcYkb3i85Z3erfX12xP82vCmv2p6CVK7qWpgVpXFzf1B8McXs6mmv6movj4feL/cHU/y+uv9jTs4zGrfKV+mv3D4o8f309NbI8cOjNp5HnrPp9MfX+znS9OvE2ROmU/+P9+XTGF6RV7Rl9/+AzwoZpNUJgAA -->
