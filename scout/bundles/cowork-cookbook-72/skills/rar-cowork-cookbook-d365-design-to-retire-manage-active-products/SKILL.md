---
name: "rar-cowork-cookbook-d365-design-to-retire-manage-active-products"
description: "A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire_manage_active_products", "rar_sha256": "611f75399b0b976ef887b57fffe80c9303a2daa1224d0b100fa12ed181374033", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_design_to_retire_manage_active_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-design-to-retire-manage-active-products:2cc297df4af4907d7730fcfbc23225693c90b2505e30056a9f4771b4648a7ef7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_design_to_retire_manage_active_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_design_to_retire_manage_active_products_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

D365 Manage active products Expert — A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire-manage-active-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_manage_active_products_agent.py` and embedded as the fenced Python below (sha256 611f75399b0b976e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_manage_active_products_agent.py` first:

```bash
python3 d365_design_to_retire_manage_active_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_design_to_retire_manage_active_products_agent.py   # or on stdin
python3 d365_design_to_retire_manage_active_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage active products Expert — A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire-manage-active-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_design_to_retire_manage_active_products',
    "version": '2.0.0',
    "display_name": 'D365 Manage active products Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage active products area (a level-2 subdomain of Design to retire) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-design-to-retire-manage-active-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-design-to-retire-manage-active-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b126a67b2b00efb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'design-to-retire/d365-design-to-retire-manage-active-products', 'uses_skills': {'custom': ['d365-design-to-retire-manage-active-products'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365DesignToRetireManageActiveProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365DesignToRetireManageActiveProducts'
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
    print(D365DesignToRetireManageActiveProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjSJPmX2FzzLarR1UpLoHI116zBXQiARKHBHS1ZXEEh7hvpJ7+7xtImXVMd89Ov7sfVmWViSDCw/1x98c9iPztyW6bMK+eXp5UYGfI2k6SKAQVYmcewud9XsXwVx478D/i5llTRU7b5FX99PHJA7VbRUUT5RmcziKLa2ankVsjBDVDVv9T5UUEDAWoGqR28wJ4SJMjTQgQ0c7sACC220QdQIoq91q3qRG7AjbywUYS0IHkE47UrePlqR1lSO4jC1BHQTZKqEATVeBn5BNUpwNVjcyRPTFKcUFdg/oZKgYGOy0SUD+9/PLrx6cIXj+9/PbkJnYNbz0toHoPcVqu3IU9FGLv+hze1IFiEjsL4PjiCgHK4Hdoip9XKbzlAR95+/ahBon/Efn3f497uwrqn18+Z8jb5/PT+E9ps7vVTW7XDQTBtQvbiZKouT4jbNLb13o0qa0yiABSQ3yz4Pkx85ukvED+OT778FjkOQDNh89PENPKHtH//PQzkldwvaodr59HKcWHn5+TvAfVh5+/yYGQXoDbjMKg1s+vb9/fxMKB34ZG/n3Vf0KpDz874PPTd8aNn4feo51w5tPzJY+yDw/B0B0dyOzMBR9+/iuxbgjcOInq5r8l95eH4BDYHrTpTfGfP95B/hWZvBn0VeZfL1tAt/4dS+Dw9+U+Im9A/ZXsO/7/SXQSZaD+ivifivuzCZN/Ir/8pW3/1YSPiP/5aQESGMuV7STgBfntVT0s+V9+8r7d/OnX36Ho/6MYNW8r9y7hNbWzyAd18/r6y0/1/fZPv/7yU1vAWAN2+tpWyZ/J/DNc7+v8gODbqA8/zoXr61mc5T0kgPdIR37Li/9R/f6MnOwk8r7dr1+Q7/Nl/EyQ0Yj3RR8QfJczNdT1Oxx/fvodMkUGrYHJPz6GWf5v/4aIkVvlde43iOrmbYNABzdRCkbltTCqEe0tqb+ou+1+/5x6XxB4d0x3SBF2mzTIurKjZKSn0eOjBZDMvvwv986sn9w3Zp16kJNevTspvTb564PjRswhL70+iPL1nSi/PCNaCFXIqyiIMjtBFPZwQODArBkXv4dJ3aafunF9qFv04B+F347cU7cJ+Afy5e8s+HqX/VxcR+M+Z3AsJOWRzkFa5JVdRckVsUf2cq4N+ATJFzJMlSeJY7sxMv5oi+cRsXMIsjccXVhqwADctgFIkrvQCD+ChP0RhkKdJ7AqNCO6dRwlCeJBzVxYcq73mgQ98DIK+/Lli2PX4efsQc8E8qhF9RQO+Kow8ulTUQE/iYKw+ZwBN8yRn377/SfkP5D/atZd+LjGARaMO3YwxBNEUGUJFqmgTeGwGhmDBZLR3Z+//f5wyqhdBosnzLLIj8B9MpT2LThGCx6eencTtHlUcSxk95V+xA3pQ4gLEjUQLZj59cfP2Sgih0OrPqrBO4iPyQ/o3/3+WGf0Sf2GIfSTX+Xpfew9LkdnunnlPSNbH/mKFDQX+nWsyEiY1w0M5QJkHsjcK5xpN99cmOWwtMNsqv3rR6Stoamj5C8OFD2Ck0LKspsviMgfYPXLk3v1fquGcHaeRaPj3wL3cRsKqX6CMca9i3hGJNgOVEhhV3YRVnYN7uN8+xERsOq9z4fCbSQDPTLWezD66J7n98gbS/5ftR3LR4vyucVRjET+f+liRq3Z9VpZrlltuUCWkqaYjxAbm7DR4kffBtsIBLYhj3z51lq8s9A7P3/Okgi6pbr+4zHSv0fVY8yD89oKmqawyl3+mN/VXW7UwNgYnV1VYzzbn7P3QvARwj1qPnIaTOH4gcz7guPTd01DmKfj929NAfIIuzEdYEAjReskkYv4AHj32G/CasysN5fAQAEjeDAV3PAHqxAoHQYBlI9AJSKIPiwWd+gkmCGwkXqE+9fh0dhqPTwFtYUpBJ6R8xjRMCprxAGwXxrHQBR+uotCUgAxhip+RbgO7eKhzNgYvyloj76APm7A9x54ewijc6w4cL2vqQel2p7dQCx76ASYWcPDs1/1fPMVVHYMnIeXfnT3m63I9xXrH2P6QR2/VQLYy4/F/jtwIGdXaX2nIViG4xomeAreAghGwr2uPz9K86P2f9Xl5Q+7gQ9/b8NwL7b6j557QcKmKeqX6fRREN/r4bObp1MYI1EB6ntt/PQoVZ+a/NMjcz49StWnR/p9ek+/H9Z4QPaC/D09fxDxFuAvCPaMPqPjo33kgjGC3z4QFv4TZ34ix6efMwV88/dbUIwkB4nXuX6tNe9DYMEJKhCMgx+1px5LVg+r5J3y7rXja0y8ZQxk1CwYC2Wdf5fJo02jhx8O/ErN8FE2kr43tn0BGLdGyah+DZ5esjZJPj5BqgN/Z0s00jAMX4jKuKOCqI/EGIH7t6+t1fjlx73hPckgO3j5y5hrsOTBNvgj8rWj/Yi87zHu27eshZusX8ZuelwSDoW/vo79uvF0wBPc3TXXYrTgsXEam7i35vqPSowp9kawoy7vOTuu+Ach8CIIQPVHIfL9wk7eiKNu7LFQRl/rRw319GCL9RGBPoRpCDMLRmoLJ/xxGbhOBcoWou2N5n7D75tZ+cOW3+8wNI/d529P7wQyXj/6hEf8jDvTf6WvG+F9r8ev4yL2KOrefd3Rvneyr9DSaKy73z0Kxibi9RGaTy+QicDHpxHTKoLt+e2+AX96aAZN+tYDQwmQUz7VYx8xhZkFJcHqXozmxJAPv1tgvB159/HjxcufNs7/XXJ4wV0XZ2jPJ22fZFDao2kC9V3fcXECx2cUQ7gM6uAzdAYIFJ1RNuOTNI05JEXObRr4NFRo9G9qvyk0xUbPQFO+wv9/1dg/PWTBGgOVgcIoDPPpGcEwDuowNAX8+Zx2ZrTv+2COugyBEjbu2TaG46SHOhiK+vAaeNgcI2gSJYhR3ls7+VDw9b11f/fVgy9eIdum0ag+btvu3KUx0mNom3IhDA7hAgzHPJoA6IwhoAqAhPO/Tn3z1+jOBwZjVMNOEvZx3bjOb2/+HyOVIuHIDVlv2ceHnzIne3qmHSXcTw10Mgy9JLtRo1yaNuUmp3kpi2R75KR1E812fWGYgh+rTWmTF8FFc1oWJX5DcQdcBSQxQVdqIvfxQRn6hSfoZEvLt86fW2UQ8Kxz6LLLfGV0K5cm9QsPTh1n17vVyRZmp9SazPf6yakbjJlYql/jqpPZsyRXAgCmEyNiOF3zEjQrQ7YoB7U6tdvJuer1bIuS17mKXXlro0neUDaWO4v7Bl/I4UzbZnx5zi0+lvHtMaGSUk87/OT79UrX0yUW7zbBfCNEg59ZV0YmCpIxcdARM3q63O+IdnFSgGpco25NnctEPYUtrvMGGVtwfyTzw00OrC5c7z17WdV7EViLbQucZGZe3Nbinfkq7Vmc0IXWnR1uATab88XuiFnnrdFYgcFZarBRuLQFV9KAt8NBSYZ94kiicPLOuylJnbvTvKpCgBre1ouwKyQHPo9AqXHZAe3XACOW6ZI2j9scm7nBGRz5JVbU4Wkfh4V0ba1q78SmzblOHuBsL6rnxCXkk4af4/XEF+NzcSqJ9LoqdvbA9LK3S3ghJiiGHNycwq79OXXK8KBwU5uNhsbkWhRdX857Apbw0zI5gbWk01SI6RXq6VSl9qtk62fl+cy3rDnLut1ugVMBo/UnmkKT9ZRyXZeNWzPGrrQ1y8wj6bjoCu6MMnYuOgbH2VLjHMSQXtQ7bH3mjV2jWiuSpOdqJZ/OQZftaX5e1s3yuG5Fw4oOC1W8eWUpljtvZ7gGeSHRlhOnFo/1Ya4xi9qZrBYrerde5wVzXOXT7OCcLjJelgV/oxxt4AaR2Me9DurisNyejzGjhVIfS9ryWnracqjD2DkKjRlIDRnIDSCNE5YPzLrwPL6mLGsyKIALgNmenPQYXk+du9ldUu9wwMJ5pJ+5CYgaZ39jYdgSNEcGV0W5lntVp+cJWTfJzrJRWduv0XQ9BDpzWVtAFY62JNCXrboy50afM2EeU6zeRfF63RDnRXdY+Vv1dNntsKt3vGTJsjPFWO7XOlAWklmZolN7McdzWuL09XmxDoqtMbhqL5LGsveidjtdChVLTWvNtgEvWj2qncXVOtmmrXnl8rTObaFbr9eXItR23pLelgY1ozJdcU0idqZ1T6YzWU0hBxOn6czTaS+9GXHk+lbuTzrxZOCl24V9pHpaHy3x+HSytUYUh/XcxpSEPsvZ1kBv0tzgvFOxY+KkWRHFglHQHExKEFk3PvailcavfIIQtJuO6hNvH4nXRo32pHcdkvNiqhe6syyHW5FuaMNFiwl6Pq2WFlkug7ZYXhgA+RU7c5xy3U2FbpNeNH0fnK+mcA0aZnEjw2K4rjOxgQ4uAq+jrKmdlgoZTubpKYmiEy/sSwE9bvJSr9ULTxi+5R4W6ICajum62jnfGgEelStL6dR2vbwebTY+XReSdbaKoTJEvS6bna1Wx9A7CKHGdVu0o/qT1MqHGU5vzyThSHQ+j/dHjBY1xyWAeylkdw4I52zpprNBo4HQJXCYbWQqOnuTmTpvZ/4xnEynBzWZ0NjZaw67PMYcscivalOZ1HySUDeiig1DM45RUkr6IAshQRF6dDODSJ2h9pJrMtZGZwfcE/01Tw6iReXY4aKWM6879nLqL5eEYkyiedrfgsHl3ShdshNOanUnnnJNcY3E5ZG0DOkisepGUMFuRmgeqjOlY56pS1QfzV7TD6WS7hIuC7XBNPtY09n6Gi9Oy5L0hFkqZDBpEtN0m2CYccKSagJT5+Vsf8J26WzWro3Atq4liMub5mATkFX4ROZlyC7DTp1H1MTA9Eh3VgTVuJXh5vRm2S+zqmRId2rjKtaSs7CZiWugX+aUHAz+dMB87uhv8mI1FU631caFEb7rZT+diBHFZazO6Bm/SCfuHCW31wLra2slZNjZJHEUv611V2IC0gjUtgxJb3O5go2B4nJXHj2KziMSNeOj6dUB4HWrag43Rd5t9EqSupO2MsNdobD5aWFQR1NfEil1wSuBwKYqQIXa4Wf7vbIn2SXfSKGxqjDbhDm78ahOTpcXIzx3XGmdtZyYNkV0ZHX9XDSFKnFO7grV7nA+ldZhq5/549kfUEGNLkXeOaTvHtfdYp/2Su7wcbkqT+WZjClROrdKe+PQcGt2jMdES9vFuEHQjoOnOep8S9nWmqyoGd5FjLJhl8OpPyhVZzOr8hL0W5XNwHW2N3QU+l1qeIk+5c1w5MP4svSz3Vry8znJXmFToJ3rob64mr9G8yY1FtjKP0l6GrHxnuR6NhPFgC3APL4arS9cm9Viz0d6pQvpcZcbJwvbDbYJeJSwFHO7XJmDF0xcGy3a07UNdpfgsuZMSu2P4jKT6rWk2K7IXfcskE332GfiTSd5/2Isqbm9hVtXQ1q1zPrcY1EjnJlzJIYXdY4XlsCGqDQE4nGjpLciRymUm3OU27cqqR9lTwOZwmu9E/nqbhdVOI/Cyu+A5BaeFfpUOLke9AlsgvB+dxNOu8Ss+Uhtj8p1g6fK/swG5JYbYiY+4BWBhrS9bFixz6YU0TKRHsoyvlJQsTpIOt/GgpBOaHw1u9nJuaSo/dZmFXbVVZPN1esIVeMKAaD7wNjS5zQ07LkwY8IS7qG8/SUDpBwQp2vlaWsqHfJSmdkJ2jZYkQ+ZbR+CrStVlddq7G55XnDKomL8Mt0xHn/mqvUmGk68SYW73F5Q8l7C1QRTlxJgO23my44DYL8X9KeGuQwLfrl1EjXcGkIMfU3J5sCpGzBpXKwyfH55pdq6WuNlil7ITZcveHJPVn6EcgQeZBeW8rUwoVaoxDhs0NIrRyv3nIjZcehut+aZc7dKWE4gZKqtUQJDhsKaqdGFyoNQw1gmGY6TQyeHtKlFN89dk4HICzNlR9dxsxIsxV+6tUQSsr0R0iYiY1YzVV3ekOCwMWaNvKUO63h+dNKCFMONuNCMIbuI9Ta6cmpnKcepstv6+i3S8v6a2Wqts2y0nu1AeYr286Y45rUmi1StERlb7wG+aXeWbvQXv5qxXG8RUr8YOk1oONeeFcesttr5XlBpCk+OVkO686jUg3mMzxsP5GJnATOdDXojozRKHa43EbdicbOPat5h9JOrJiRppQFNavl26TaEyunL0NPznVlInYoPqHWclr1YcdtqVkkts3QmsVI11KJuzhuNbFw/CvMsXlM+nyacvmKBoEssySiVJYulkptL2Ks1XN3HfCkeNmq/jHV+lhxnHKftMREyeSvJYBE7qBBmM7Cmec13zcGVLIoLQ95YG5ybgvR0222AaKeygKZMdZF4tXXa03TYicuq2odX57xQLkucutxiELqwcjaW0C83wmSXuMNKKTyWQodyIyTDZUVe1l4sKu7kRnIoK/eGTGwqGNUpPRTa0tzapjs/3ajyaFgXRdscjpjm2rqs2rNwcaxZIpckopqvaTXdxckFzJfaadmsLpy3I9DEJCLX3OB7YcvsPfV0zUhV7FU+kHBYlsStZe7FfuKl/XExW8j1TO+aY0yfSbRWyvSWBpynzJsqW0gR3JycexCosTXbaubs0HQmI2/43XJ/2V52m7XfctJeC4SbXQyLyWWZ3irBxHf06pZWkMIZphJuecaB9dwduBazPON0jdjtYXFyutqTSEdMMm+3dZiGbtQ5OqdVJnESLXKaEziEg8OSGwYzCpxCbbr0rjfFuNDAAIcdSk+czjWKG6HhtIQS+UbGO8a9mgSfqxkRFowkN7qyzrbl9sYF0027KCIwZAo+h/2w0Kah4+zsch4fNLZcXSilVC4kI9T83p91+uFsTlylMVZZykwrRafxdhIejynvuIUPt6Ec2rH78ozvWpijFXYya2blEQ1Ky1ZbWmkjKVW7pqXbvJxhV65ylN4Pk8pzCKbBsVzm+gmYTv18Pw2E3jqeJFUmjMNc87W0p8tbp/vGeUHECWEWN5bmztcNU150sMDzrBasFWVKkd3fLAeGAhnxRrGdWkUmAX2zXmNxZPrmIdgL7E3oltx1aYlM5O05TOPp+uqlcgQFULcdUZIH0FN43CjbeaivG8i0t0UmpttBunj52TwflekRSycSuJB1AagZASYb9DLddFpnHLVJLMKN7a0mu0uCY7ixvZ20Fr2pZzVdaCah5RNa6fY0V6isfzufGK+RCTJd6Dje6C6hTm/nbujo82HFbxIumJCKxEpqwU5uU5UkKbmT6XaSR8beaBoD323bPvDWp8i9rbGa3s0xPMEzAnBbGuS8LBNO3FxoInGxXou3so838s0UyYk1A/tgv3LUtSoq/Hy2MbMZCTcaDnHzeVagmTCk5tEsbki126zQmRcHB0zYXBaOacont6c4UFw0ouTZQbhx9bUkM3qQEinbwN1aJJDH6WURa9Wk1sj5YZHveoab5Iv8qPYS3d7wYXec1/hSEldzXmfXNMElF9hgbYA3GAv/BgJ/Y1TsIBPT25ZUz0FknmgWJ23cpJu9lAIi8qQbGsRDe5PNG93IuHPd48cVZx33BF6bCh0agi95HsfUVOuhlDTp+dU8J/NJB7jOBey63hzOBrbwL0O/swiXW7tNNCVuR+WCJVGdKTbb2hzszFX8WuOc1oH5zdhVKSwIDYWtYtKk3GurXSKK2Owxi5AP6SFYrmZTheYI2NTpubigOHKxYc5iOMcUlpS5cL5NVtips1Vjw86O+NC05JHpad/yVoE2llhGJFeWS91ou804d0p7h0k3Cwl8AmjtAHSus+veWV8OAO9I72Klqc61dFGkPvAh6lhz0ET55vh+0E0hrTJRxgyEaNW0Wt1c8zKsiGR1CBZGVDbrMDMnUPdNy9gX7yJtFtKic3f4fhb5Q2RyOSdobVWSKfBpRVlK62HCVUIHt08q4fOSl1ZKUcZ4ji7K+a0XTuAWBSy1brKAXejmnncFkVC4lE65nKeseecbAdr4jtNpqufCfCFhowf3wMrBu9DtXl+2NwipzMyE0p7zK2oyWy7QfFcsWbKV2FM6xfXlSaNUp5dKkHHpHsXU+Z660qczlTA7plyfuz3LBNnS6CsIRJOnU3nKLd0inqriZlKvq/MNRWE2+pAYjwSEawEL2uaE04tSmLtzqnXruLvUYDivjHnJ2pfJoMlWU0+xSvBubWuwpsnh7o3rmKOecsU+3VqaSWneuuZcYeeLuRubt24emD7QxFm0QF2PcD28v9DrRb+5LjJjoKa7I8s+fXy6HwE/vWAoNac/Po0HBm+v/f/Vl8XBLSpe36QSNIF/fPp/987y8f7w/aDwfgwAbO/lvvrLv6bwrx+fKjeCyj1eNddJG7y9svxPb2s//Z23yaOk6+OUezznHJr3M5XGDu4vvqPMa+umur7WedLeX3tDV7T1+Ncv9evbQcTT3di0aF7f33jfj/YfZxw/WPk0/nnKeHoHvMhu3r8GbycGcPzbsfXrCBGoitHqt9Or8cXueHz19Pv/Bjex0RruJwAA -->
