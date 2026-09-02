---
name: "rar-cowork-cookbook-dashboard-enter-sales-orders"
description: "Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_enter_sales_orders", "rar_sha256": "5314af7c06102cac4bb51e6b687364c5fff89cec07b4ceeb438cdfc4fc872f02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_enter_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-enter-sales-orders:0c86c8a55d2757e0621f9370e8edef0256c8ca6482f951c89a13b3c2b6f453d0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_enter_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_enter_sales_orders_agent.py` is
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

Enter sales orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-enter-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 5314af7c06102cac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_enter_sales_orders_agent.py` first:

```bash
python3 dashboard_enter_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_enter_sales_orders_agent.py   # or on stdin
python3 dashboard_enter_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enter sales orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-enter-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_enter_sales_orders',
    "version": '2.0.0',
    "display_name": 'Enter sales orders Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-enter-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-enter-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee287bd0c2d0f527',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/enter-sales-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-enter-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardEnterSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEnterSalesOrders'
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
    print(DashboardEnterSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aXPjRrblX8Hofajyo0rEDlIdjhgCBLhhIbGRgMuhwr4QG7EQi8f/fRIkpSq37X7dEfNhWFESAWTee/Pc5dxM6Lcnq6nDvHx6fVI8K4NWVpJEoVdCVuZCTN7m5Rn8ys82+A85eVaXkd3UeVk9PT+5XuWUUVFHeQam78vcbRyvgiyo8hL/yzjYijLPhaKs9krLqaOrB61VgYdcqwrt3CpdyM9LyBsfQ5WVgLl56XplBX2B8sLLKjAT2NFDdpm3lVc+Q1kOLTGSgCwHKKqgzPNcIN/uoTr0oGvktV75AgzzOistgLin119+fX6KwPen19+enMSqwK2n5bt2dlSsjHqlm1owM7GyAAwpeoBJBq4LrwQmpuCW6/nQ4+rzuL5n6L//+9xaZVD99Po1gx6fr0/jP7nJbhbVuVXVwEDHKiw7SqK6f4EWSWv1FVR6dVNmN7AApFnwcp/5XVJeQD+Pzz7flbwEXv356xOApbRGwL8+/QTAAvrKZvz+MkopPv/0kuQAg88/fZdTNXbsOfUoDFj98va4fogFA78Pjfyb1p+B1Ltrbe/r0w+LGz93u8d1gplPL3EeZZ/vgosyv3qZlTne55/+TqwTes45iar635L7y11w6FnAO58fhv/0fAP5V2jyWNCHzL9XWwC3/icrAcPf1T1DD6D+TvYN/38SnYCwrz4Q/0txfzVh8jP0y9+u7V9NeIb8r09LLwEJVlp24r1Cv70pe5b55ZP7/eanX38Hov9HMUrelM5NwltqZZHvVfXb2y+fqtvtT7/+8qkpQKx5VvrWlMlfyfwrXG96/oDgY9TnP84F+rXsnOVtBn1EOvRbXvyv8vcXSLeSyP1+v3qFfsyX8TOBxkW8K71D8EPOVMDWH3D86el3UBwysJrGuT0GWf5f/wUJkVPmVe7XkOLkTQ0BB9dR6o3Gq2FUQeojqb8puw3Pv6TuNwjcHdMdlAirSWpoVVpRAoF8GD0+riD3oW//27kVU1AW78V0+lEE324F8O1WAN/uBfDbC6SGQGVeRkGUWQkkL/Z7yArAyFHZLSyqJv1yHfXdKuzNAJnZjLWmahLvH9C3f6Xg7SbrpehH479mwBv3Ul17aZGXVhklPWSN1cnua+8LqKeggpR5ktiWc4bGH03xMiJyDL3sgZMD2MPrPKepPSjJHWC0HwGFz8DVVZ6A0l+P6FXnKEkgNyoBNHnZ32gGIPw6Cvv27ZsNbP6a3csvBt3ppZqCAR8GQ1++FKXnJ1EQ1l8zzwlz6NNvv3+C/g/0r2bdhI869oADbliBEE6grSKJEMjHJgXDRroBnrXcm79++/3uhNG6DPATyKLIj7zbZCDtu/PHFdw98+4WsObRxJHIbpr+iBvUhgAXKKoBWiCzq+ev2SgiB0PLNqq8dxDvk+/Qv/v5rmf0SfXAEPjJL/P0NvYWd6MzHeDkF2jjQx9IgeUCv9ajR8O8qkGoAn51vcwZqdOqv7swy2tAxXVU+f0z1FRgqaPkbzYQPYKTgpJk1d8ggdkDdssT8GME6KYezM6zaHT8I1Dvt4GQ8hOIMfpdxAskegBNqLBKqwhLq/Ju43zrHhGA1d7nA+EWIPkWGincG310y+Nb5LF/7ho2/9xnfDA99LVBYQSH/n/pUcYFLFYrmV0tVHYJsaIqG/doGy0aF3/vykDHcFN/S53vXcR7wXkvxV+zJAIeKvt/3Ef6twC7j7mXt6YENsgLGXpfcXmTG9UgTEa/l+UY2tbX7L3mPwOIgJOqsXyBbD6PtSH/UDg+fbc0BECN19/5H7pH4JgZILahorGTyIF8AMQtDeqwHJPs4RIQM96YcCArnPAPqxpBB/EA5EPAiAgEL+CFG3QiSBbQM90j/2N4NHZVxd3DLgSyyXuBjmNwgwCtINsDrdE4BqDw6SYKSj2AMTDxA+EqtIq7MWPb+zDQGn2Rp1bt/eiBx0MQqCO5AH0fWQikWq5VAyxb4ASQZN3dsx92PnwFjE3HjLhN+qO7H2uFfiSnf4yZCGz8TgKgUx95/QdwQPku0+pWkQDjniuQ66n3CCAQCTcKf7mz8J3mP2x5/VOv//k/2w7ceFX7o+deobCui+p1Or1z3zv1vTh5OgUxEhVe9Z0Gv9xy7Mstx77cc+wPMu8QvUL/mV1/EPEI6FcIeYFf4PERHzneGLGPD4CB+UIbX/Dx6ddM9r779xEEY30DNRek8zvNvA8BXBOUXjAOvtNONbJVCwjyVu1utPERA48MAcU0C0aOrPIfMndc0+jRu8M+qjJ4lI313h07usAbNzrJaH7lPb1mTZI8P2VW6v0PG5yx6IIIHS/AlghkC2iO6si7XX00SuPFHzd3tzwCBcDNX8d0AgQHmtpn6KM/fYbedwy3/VfWgC3TL2NvPKoEQ8Gvj7EfO0fbewLbs7ovRqPv26CxJXu0yn82YswiYPGtrI7U8EjLUeOfhIAvQeCVfxYi3b5YyaM2VLU10iJg40dGV8BOFzRQzxBwG8g0kDygJjZgwp/VAD2ld2kAEbvjcr/j931Z+X0tv99gqO97yd+e3mvE+P3eFdxDZtxn/jtd2wjnO9u+jUKtceqtt7qhe+tD38DKopFVf3gUjC3C2z36nl5BcfGen0YMywg018Ntx/x0twQs4XsHCySAMvGlGruEKUgeIAlwdzGafwYl7gcF4+3IvY0fv7z+fdv7F/n+Cjsz0plZBOGiFEF5MIki/hyjYG8GSNSHUQI8dSwSn6H+nECc2dxCMBtzUJv0cQJzR7tG/6XWw4ApMiIPTP+A9z9qw5/ucwEtAM1gMoEhuOVTDkwiMOpYDm7bBOKRNjmjMBJ3CN/3Z3PHc2DKxh3Ps3Fs5ri+g/vOjEKB+aO8RzN4N+jtvfF+98U95d9AgUyj0VzUssCKKQR355RFOh4Gg+V6CIq4FObBxBzzZzMPB/M/pj78MbrrvuYxSkEfCHqT66jnt4d/x8gjcTByjVebxf3DTOe6RaKULYf2pCQ9wzxNN3akXYYjiTHocX6RKtwyFunSGyou18qKFfstiwiOHEiWppcrKVzOFxm13Tdu4y9S9JiSx9XCljaZkKrJQCT9ZEagYRAtDNAY6bttlqYuLSTWORdPNR1jodLLV/qaZcMsuaKJVCPlOjKrZD6d5sc5n+jWloilVLZNp7jkV2nTc32qtrheVBhTKJGN1kTe60boGP0pnhgUV7jFRdMIo6xjdT+dIszMUO2dbPLnw27iryT9eKXti2pE8caJNdLfUzPcxyiSuLaFhE0RotmtzzxGC1K6LOXoeqG0i2lrQ4q45UXPGKaj+HhLhSKx1Tkqv9DuRBDC9HQV23klSychFCdMZGuKfjxp0jKab3gCJ8xVueuY+WXH4PxOM7e8HDZuvzsdkOCUNA6rFE5hFQR9KXdzvZJJ0RuGoyDzs1Nh57LkzNRWu8gtu2gVtWRmQymZwu5YsWvhjF5zepEdOTvb0brI1wnGmyJMLbuUwrZcRQf6OfQnqKQNqNJws4mR1wqlF9uJdAYAVidEQrmLtkF9tzyVqz7MxOhsnevBWXcdbBzQNjbEEEbCWi9PSSjq66TWJfHsU6cw8QChaeZxUdnL2fxwOejFcs3OiU5z7eMS2Xena9lrxpTo2rwx1kWpX0kq07JuVZZ8Ebr77mxifrQDamcZqs3CVLSjgWYJ1lJzm1v7F8w8pigbdS5+qvVkky6QLqLEDrZkSa1V4hJmSoKtJ0Ij8cFpj57EanNkpxuMxUO58/owTHe+1pl7cqDIijgirp573nA8bo7blHDTXSwuaTZkSC5TNVNU1ft/WzURWS/LQczWlnvU8c0WG2J8v8aPe2G/q9XFgSum1ZIlOvE6JcJJ6AhxRLAkcspcOEuxZC2RF0WTLT3zzyWrk7VSrsLe3PZxi+7WK8FoxejEx125b+Bug8Sdz6gorQz5VgEVTUbyaWvPiTK6pIIpn9Blzi0LrZwws8WQo1G/c1OOZ1U3bqJDeyCPipQG8ZlXElzTyL20ZBxpmxkzomto2OdOSOSqFKEeWZPr5NXBYfVkHYtIZMJba0pEArmdZFromBisexPWDR1GZI98Qy59wtfEtDRb6SDuG5zdq+WOopTjGkbokNKYjekWnH6E0WzNDpZk4ehgyTBds8HJy619Su4iFU3K3WCgJp5fOEXHlWAi7EH6JYdwMZ1WO8dL2GJocFkxyPZ8jjXZjkNXyFu/13cAzaIiLbkRMVHxhKjPi4FPZdBlkl0nTHNZvVrJOVLO8uQAu7a4Jdla35+5KN/sD5NJDhqmTh/4jjE3+M6cHKrTiTPSw9Q7XJStvCNYG2GJDaPoIB5stdQH7ySf58I54pKMX4gms8q88Hi1l4IpwX3Wb6bn1WVHDLtBaLamqYSMlWRbM1RIUV2YjGfWRzHYWbzgDyKq1dsGNTJ5ukXoyyVBynh6Ok+0g0U7KJ2ejgY8O7BnSqH6eZ7A+mWeY9q+9bJlGE59infCubY+rPcqdc03npnQ7NFCKzWebdbdOV2dBJBr51B2Gk5x6swYWpOMYo49hZG+wnfMZRlQBjKdtjyz7d05Wyjm8VQSONsVEiE1/cVF1OToUZK1EQb2HGIL1iYOVjE7zoNQmcJy0F9t0Y7PtMJGbOt75aUYYEys82GptebhDNuanu7OdOCqnUHmsarhFUYv0o11GHTBkEgVnqceh88MtyPhoNiQYjuordWcAiuzj84kqIbkMMupvXTNkM69UpdZ0bFBnBf8aX3EvImqxJvLNKESqxQyXKMXsMVlfkbheiChVHyRKENgZCM4xNMpaprtRAnJLCZMf7+nFNoobG55WFiINSlBji22YiDDhWftJcFE8oMolIkWmQh9jmxqIuZdwlm+Q3PwqpRO+co3UlnVJ6oWLdVrxDQHd7tLRTOgaM+UmJNQZ7TUy6SuJDKhblWGEC6YhjBLIo+lNaiqE24ZXGhsQIUUQTf787HLHU3crteTPTfT2JPj8Vqpbiy4tswtgm9PVldeLlO6RVKJCBMMrp22l6plLW3YElmZ1SUQzxclRwmsnM+353m19E3EQ40VYZaiheD0foGdBEXbcPxgHK6+6gbLTSQXc4WizpuWKzZ93XeiumQEUZ371sBQRHXdyRMjC2f9Ys4p8VoO5xddyaUyMC79ltpqia/SEneO/JQ6FgeqDRYRoDO4U08k720AX7vWsILldjY5VgyrlgETLdh0Zx9ixWCcShCEIGparscid4tW2XK2qjTO2aUGR58SE9mFR9uzNr1BOFuWsYyGtXnRsO3aKXIGx7VuYUqgwTHkVWzLMXu8MtuIuwqKetAIlEDNCecwU/+kpbjNbo/1SZdraqXwMMg8rbZaw1GZ6wU5yopQutZSYWA+MS1sqZzBDul8pHuNjHojmao5IpJCyF9ZhNMo5pQbvX1Yx4R6EK5DdVYxg5FNmTrwRIBpxYrf5ueIwc+qDOqpJC0izqu3ixnGUsmUOiRbOg3WlOpPm+XSsvyawUJrpSwLhF9wVDSjFGOtWhvkYpH85iIes+UAT1Uvs5FubZOLSJadvXNwraPrDxs1JEuvP8MktpL6YU4ml6SZJKhZtsYRwGfOm7lbWGGmHYWAjeZWUk/lMOA5ha7gtWRTScAbR83wKVrb6tEKdLZSXl1PBOprjdERjG6nuRNhqKmU4aUzt8tufaw2VqLEebPc6A7fz7kzt3OtHTakCejWT5sLP2ns3cXUrmeBXrCrwzRqJgbMXsmd6fBlsQuKyyqi5yAtG0o/sJJnZpczKQbc/tzuzIVQbxJG3IDewVK9zcSp+UQ8qVnBSy0zazwFLuZmS8RFIe2O1kwMWxMwS8yd5KVzsfrIC7Bg0NuCWRCS0WxV9iIkzIadaw0sryhl4caXDlXS7dD23eyKX+qIzQN1CpuGH+tRePGDgrFVKZP6Q86ty1VcDYKeDx4pmDv4JGmzqrPD2KaUPiM2Js6Th2s4Cep2TSkDPiu7zl5YQ3qgOHdNdhV9pBOsiy3ca3DKiS5eiNMpWrt8gc5iLnKzXZanmZ/6lmxOSJSe0K5eKXObkSMNL2lGAwW2oukgieaHPvcum3ilcFwVpcdtZFnBUb4aB3JRDdTV5byEN0sl5qZ0ibhrlTk72q4skg1dNwqSyExE87K8l1iURs7BKjj4ei4pwapKmrxNZb5tTXmXyoyniburFhWXCKnzSSlhvcrkciCC3n3CdWHuY8g556ZLM7dtvTEkxTNaCpeFcGLhWH0wWZkc5nA94eWIbs7X1Tbci+bBwiTPHeCNJmVcsaVBTuzDY5kKF6E8r9AV2xNi4Zy9TZcRy9Vpz85pzVnyCVabJCIi9tWztEXKrLz1XnQmlzOHWgwhprlVN3iMuQuXSRZKV8FDIi5ba9ZMpjyyyRv4oLqmnlvGtthNiqODKykTKzDp6f3FIjiKWW6ktl3NF6hIrytq4eU6bZIC0x0GU+L2hFKLxZyStsiJRsCWJp804SL0qtpZGzDYhnICo8WnTSC2qUMxHd7EoLasle1griaGstrzHrpZbn3c5I60zZtXfpVJgwODwUO9BHsRS2ouO6NbsKecqRFCSuH6bKlVHK4mCV0drmLn2rRWt8XVRXuJIk7VdJ1fz8UMJa/q9GyB0lMWy3ba1OUFsxN/3jp6a3pzxqKYVhhMx+zoA75USHc6PcScFBaLamK6raXuzawV1puzU3jXeY9qyx7NdGYQT5m9YLRoo+tDVLfbs17O0HYJh+sEFwO2nGXl4BjLhqTyetKalyO69LWJS+fi5ISs+Gl2Uf1jW0n2WsZawW5mUYVwSC+Ghi9Ru35mtVLfXZUYpxYnfGmjk4oj9+uNMxVd36+MvTL2ims0nfrafuaKW3PiIh3ZX+tJtHcZr45s2ltM9odFCHN2hJMcrw7hMdEXdX1ItWnOmdugFcyrxxnqVqALGTHxSErW7DoRqABlcGI5O8qtOyfsbaHDBIYJ3YI3GmeoyFU8VLgrWw7DSBLhq9ed5LQ6ogwb8iBU14Dqo0mNG/SphRdets6k05SMgUhq4Nuo7Sx+gh8mK9s86U7oTrkuI7VO32wBJotsj8rzBl9xGxmuiLM4wLaisnMbt8R5X/NTwZqupnNjNpergG9SeBKkGuDFLizqGdfBexv1z67QcejcRtCWi9kF4Gp1ZaDXzPROTWsjIKL4bNnLBRaj22w+m4O9UyWgi8MJT3V4vuzsSsAsZElHVGdkFdki/Vk+disRHab86bpU1kFLt7E6JzlqaxrJVii3OLU/qHmLxcxm0zm7sBEYtI6z7LCPt5JdJ/yJ9R3fpGf4kj5W5pWxjrimgKUHU++q4o4crebBXg/0wHLqa+3BCGEILG3Y+cJpD/Nm8Ok2Z6UIXeWrPUox3rFECYZv9smpPSZM3VKpabv1MW4mDbrh3aLCpd5zOV4YgtkxWhGqyBDsHEuElNnNJjG2BN2KTeFqeUEnClqjlLNVSFZiHSxos6YKibhrxXgpYziKZ6Ihsb20qv1iW9tRlsWVb64WQs4FqL621avDSyHcr1H9OJfgGtPnuy43yLoTV2pEkoFOClgQDEt4Qcs+jB22ZOv23ormFhM5mujqZmrlB2eNzyZnJqaKrKDtfuOElEFhzMZjxbJmes3xV3NzSpxmVy47+u50wJflFCtgEa+ECYbMSGTZB0ifpaJxIdqmmJqzk5NyzNBcOGrvS1InEt5e5WrVnV7b05SgjKTdSTOqEdCqOM53Ao3HVBuq7ALBL6WcU9TUmfeGJNfaxIhleNCpgPPpeefjrbiA2TPOa4ij7/dzuIykWJ6y2DpXrgKMDrw7v5id3c/ruTtHxAJswUuDaFl3mWLEggYsG+7Y1M0Vc0K0FtukPo8hhMifUJRC4czIAE3yncG0HmtjxoTqkUVZ4ftldzhxoupHh6uwFxY2HexyJWZglJbs1tTMk38BGx3xIJAOskhXfnhAQee9V+LiVJv9jGn3zrZLZrwyb489fcWamjnR5p6JaT9Pin11SFOSijuVEniZRPPt2q/Mo+0sD2w3bcktJhebwnYvzXa/PcT6FQtSeGoRWTBrC6SS1gs337YejyTEwYjUgsmVRWZT/gKbypuj5skOURBpJctT3x/ofr0vjjavEZUWovtpICl1vyF2ynmxWPz889Pz0+1F7dMrAgoP9fw0nu0/Tuj/3UPeYIiKt4cUjELQ56f/d2eR93PB93d2t+N6z3Jfb9pf/z0Df31+Kp0IGHM/EgadRfA4evynU9Yv/+rUd5zZ398tj68Uu/r9dUZtBbcD6Shzm6ou+7cqT5rbcTSAtqnGvymp3h4vBJ5ui0mL29uFd2Xg+03FW52/OeDm0/j3HuM7Ms+NrNp7XAaPQ3swsQf+iZzqDSOJN68sxgU+3hmNZ7HjS6On3/8vav85ODInAAA= -->
