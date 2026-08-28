---
name: "rar-cowork-cookbook-dashboard-maintain-asset-leases"
description: "Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_asset_leases", "rar_sha256": "23104dfbd95b88ea48c90443ac97451b445ea9eca4dfc9fa5e9b57bd563dbf4f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_asset_leases_agent.py` and in the RCI capsule.

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

Maintain asset leases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 23104dfbd95b88ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_asset_leases_agent.py` first:

```bash
python3 dashboard_maintain_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_asset_leases_agent.py   # or on stdin
python3 dashboard_maintain_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain asset leases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_asset_leases',
    "version": '2.0.1',
    "display_name": 'Maintain asset leases Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for maintain asset leases - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-maintain-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5f172e71398d16c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-asset-leases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-maintain-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardMaintainAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAssetLeases'
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
    print(DashboardMaintainAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZObWLrmX2HyfrDrYiebEMIdHTEISSAkQBKLgHKFzb6ITeyopv77HCRluqqr+nZ3xHwYOdIpxDnv/j7Pe1D++mK3TVRUL19eFN/OIc5O0zjyK8jOPYgt+qK6gF/FxQE/kFvkTRU7bVNU9cunF8+v3Soum7jIwfZDVXit69eQDdV+GnyeFttx7ntQnDd+ZbtN3PkQr4p7yLPryCnsyoOCooIysGpaCdl17TdQ6ts1kPIZKko/r6Hp83yEnKroa7/6BOUFtCLmJGS7QFcN5b7vARXOCDWRD3Wx3/vVK7DNH+ysTP365cvPv3x6icH7ly+/vrgp0AFsXb0ZID51M5Pq/V0z2JzaeQhWlSOITA6uS78ChmbgI88PoOfVx8nLT9B///elt6uw/unL1xx6vr6+TP9ObX43qinsugE2unZpO3EaN+MrxKS9PdZQ5Tdtld9DBgKbh6+PnT8kFSX09+nex4eS19BvPn59AZGp7CnsX19+gkAEv75U7fT+dZJSfvzpNS1AGD7+9ENO3TqJ7zaTMGD167fn9VMsWPhjaRzctf4dSH0k2PG/vvzOuen1sHvyE+x8eU2KOP/4EFxWRefndu76H3/6Z2LdyHcvaVw3/5bcnx+CI9/2gE9Pw3/6dA/yLxD8dOhd5j9XW4K0/ieegOVv6j5Bz0D9M9n3+P+D6BQUf/0e8b8U91cb4L9DP/9T3/6nDZ+g4OvLyk9Bm1W2k/pfoF+/KYc1+/MH78eHH375DYj+l2KUoq3cu4RvmZ3HgV833779/KG+f/zhl58/tCWoNd/OvrVV+lcy/yqudz1/iOBz1cc/7gX6tfySF30OvVc69GtR/q/qt1dIt9PY+/F5/QX6fb9MLxianHhT+gjB73qmBrb+Lo4/vfwG8CEH3rTu/Tbo8v/6L0iM3aqoi6CBFLdoGwgkuIkzfzJejWIAS/W9tysfxLWOQWCf60D9TxmeLC4C6Pv/du8QCsDwAaHIO/R9e4O9b3fY+/aAve+vkArEFlUcxrmdQifmcPia26GfN5PKsvIBCHZ3wGv8zwCGPk9vJpD8/i8kf7sLeS3H73dojx/YdGK3Ey7Vbeq/Tr6dIz9/euICNvAH322B/LRwgTFBDAD1E/C5LlIA5c0Uh/oSpynkxRVwuqjGu2wQqy+TsO/fvzvAqK/5A0gJ6EEXNQIWvJsDff4MvArSOIyar7nvRgX04dffPkD/B/qfdt2FTzoOwMdnJoCFgiJLEOisNgPLJu4AwGt790z8+tsztkBMDvgN5C0OYv+xGVTmxffeAq3wzGecnEOODwIMgpuVRdUAdIbi5hXaBtC7vUDpdGvC76ioG8jzAWV5fu5ObGQDd94jmRcNVIPyq4PxE9TW/l3rd6ey7yZmoMXt5jsksgfAFkUK/pvMvC8Cm4s8BuF/L4PH50BI9aGGlm8iXiFpqkWotCu7jCr7qSOwH3kBLPG2HQi3AW/2X/OJFv0pVPfGeIQHLAKRcZ8p/TzlHPB+BlDAq99039fYE6epd26rvub1s+jtakqFC0gAKA3b2Juo4G/Pkqqjok29e/yApXfCfmTBe2blXoPiX84D238cIt45HPra4ig2g/4/GkAmNxiOO605Rl2voLWknsxHeCejpjQ8pi4wC9wtuLfSj/ngDV3eQPZrnsagVqrxb4+V96Q81zyAq62ADSfmBL05Xd3l3gt2KsCqmkrd/pq/ofknEKU7dIGcge4G1T8V3ZvC6e6bpRGI1XT9g9nvCQaxAyUBihIqWycFBROAQDi2ewFWVVPTPbMCqtefGrCPYjf6g1cQkA6KBMiHgBExaCOA+PfQSQVwE/RbUBXZj+XxNC+VjyR7EJhR/VfoDPpmqp0aNCsYeqY1IAof7qKgzAcxBia+R7iO7PJhzDTWPg20p1wUGSjn32fgefNHpd9tmcwHUm3PbkAs+wl4PX94ZPbdzmeugLFTYT2y9Md0P32Ffk87f/ua3218x3rQ8unE2L8LDgTKOKvvGDshVg1QJ/OfBQQq4U7Orw9+fRD4uy1f/jTLf/zPxv07Y2p/zNwXKGqasv6CIA+WeyO5V4AXCKiRuPTrH4T3+a3NPt/b7POjzf4g9hGlL9B/ZtofRDxr+guEvaKv6HRrH7v+VLTPF4gE+3lpfp5Nd7/mJ/9Hip91MIFtOk4d/cY8b0sA/YSVH06LH0xUTwTWA868Qy9Iwtf8vQyeTQKQPQ8n2qyL3zXvnYJBUh85e2cIcCtvgG5vGtdCfzrIpJP5tf/yJW/T9NNLbmf+vz7ATCQA6hTEYjr1gJ4Bw08T+/er90FouvjjEe7eTQAGvOLL1FSfoGlo/QS9z5+foLcTwf2IlbfgSPTzNPtOKsFS8Ot97fv50PFfwAmsGcvJ7scxZxq5nqPwn42YeglYfAfXiaqezTlp/JMQ8CYM/erPQuT7Gzt9IkTd2BNNx81bX9fATg8MPZ8gkDnQb3cWyFuw4c9qgJ7Kv7aAD73J3R/x++FW8fDlt3sYmsdZ8deXN6R45uA5F4LloCU/1xMjIqBKgUJw/agncO8/nRif2wG0gZEF7McJDJ15gePRpLNY+PZs4dLobEbYLk3NSMyZzUjfpn3XBotcOrBJn3ZIyvHIOeE5wSwA8h5F+W1i/XgyyUcDn6Ax3PWIOU6SMxqjcJv27Bll2x66WFAoFXgA/X9svQBcfPr58GsK4vvwOsXj6e6vL858Blbys3rLPF4sQus2ZewdKXLoah4wbo5snVi7KmrQVFVlXf16Zp9tRZKlS0NLg6QM22MkXOOM2aJb6jwjL/BJgHuV2uezQr7sRL1sK/GGz0Z1ZE69a6yRW4Ia+vK0KQbPTUML4TzP5jbmtir07IYWiV3OLF8xTAmn/QPnH1p9nseNS8KIkRt0XJ1bXYryzLX1dV2S2SheVJnklxERk+61LJtVO8Mtu1DKs4N20jg2G8c4N0dVjysc3h8O/G3nmwoiKfFmdIRNm+mXvRcbm8ZOEtRPLnPvcKvnbu4sZn5NyYazmCMJfXFWgrQrEkWUcFBXWYZ7OXxLyzLt5F25l0MriCVLtXVpH0SZLsYo2Rm4cvOG3bE+ldmSvZBZFoX7XIDdOt/HuHk9C7gqrnpDa0blmqwUJNWy8Baa5/a0w9NdmkX1pa2la+UlF3uVZ50ZG/POzrVUScksbLRYoxhnj4inPPHKrSrjEYMpeYqxAhr1RBzpOwtQfNtiN8mkSJw7GhwtSIXIoi2LzIdt5s/Tvsv3m7QybE+QBjQttVulkedZYw/ySEmqXzst6+pL9Zq1TghzYhVz6NoR2sO5PlwlG3aF6xVuduVQV4jtsoe5fvVPqbkaFquBUMrVeS16N6dLCi41OxfhZd/Z67dbzSvp1pSdoAaHnGC9a70WX+KIb2zntWVYnAGk7cPd6eaczWNkJb692qL0eOkkLCuSYH9jFvNrKfZcJQaOHWS9njmSapn0/Nqc0rhC6vneCAWj3e0VtbZGTS7J1comc3a/1+CoHhCqK6+3xuF0voAzXMdN3zEGK7dvS+ZUR8Icix1dYlUNYx3wo2vGvLihwkDnnECzKgmT8AAHLAxHJJ+LkajlyOxQ8cwcCSpqri96eVUY+Vmm56NuBeumvFKSrV+cQ18q6wqzsbPEX4ZDyQ+0djbNIXLWFcdThkwvsmNlZOQ6L9gKOY3pllx1udKGRbfXoiwT9aPtCOgq8QvdWIbLxdoS1tX2pnhh4iVyfESP8/Mo10WS7e2U1LV5J69YXxay+YJctks02Bi3mFBnQiBv0Lw/nQX6okZBcsDmDqopi+MS75awT2KCsfSAMQHFz/J1dbolFZwQcDIwc1sO44ulUu0mFOc9Ftj2CHOM6HAXdSM13NWWE2bWX5xyRnAL5yQzHHthb8RqQLF0vjn4mdlKfmDjF0ffJsB4+FLs/QzwRMSRp1XMEZi/1eIFQiyEldiIQlK22zYqum5TWOSV1jr7vAIoiNoV3cjbjW9elT5C3XDcaVrlS1fTMU6xEndzPt5jV673t+T6iJ4jkt4YGyG+pVxrtedRQKQjot0I/KRI2QG57sJKjDR3PIzLJfCE0DVuTuBd5sKNkPGHPc/SDbOJhLrs92dDL5MIvmijJXjHRDEiS7akar9ldeGWi9T6cPVq+SKQKS62bHPVBkQkPEXMCCt2cjS0uRAZnX2P7OequOVD+cbdriGg7NC+0Sd3DcfK3N7YBMVIvW8cumhvLJJsCWvERVTjRUUrR2NZE/aZdZcLc9ULoZN00TBuuO0sHWbEymHYK7c+XFrvPC8VfJt4kkp3BrESOlMVSc2JD9ngiER91neFXjlxQuqWw3lb2mHKQWH5cKk4JBMgvXWNDkI3GKtkEcF8uVmug63JYByhO3FLzkZuqWzZvtntWkEzbXEl6Y6Z97JQ35b9eNRiqR+p/ihfTXeF+xtqYdLEHA3LddbcbsrRhs9Lm7DnM1qyztcIPWW+dzBo3O+ckT5lwnK3Uc7trsbpRZ6ejyZymet2JeYzbSmi9iY3DWpx6S2cCEy37Wtpw/L7aNFRxq0/GvQNoTgaufk0kncpszDbeAPqbMwDLgqVI2vYl83WxFUAlkufSwyWTLHolMkk1YV4vtTO2KpnjWNcV2F39AMVXtD5ipwpKxFPFD4XcoXNm3C3U5KGZlaM1q/6lFmZjDpEgb6trEAx7eLA09f0hM5WTUyT62vMd6CpDICR+lVppX1oYBS/3O2vQ76zFIU5IAlsr3Ywz92q88339udC9Xe77KZJvLdKQzJkxCBEUMsfd3K0lmBRTNKdU9to6DDjqjzYYTXMEPdkbqNqnHHGYZ8IBAcOgcV6lV0TaqPHjULj8JxYEzbPrlO7U1BY4MTlzplpVmX5QlTBDhwWhnlerIKzhIdsLzAyWzccL0e3Ve/TDA9Q43yub7fTsktqGHE0hRYsJqyi7dWQrqEKav20ZsPBu+lyN7hrItT6xhMwNhX6I73kLgp3MkyTFLa02evdmN0a0t2s2PacX0LdJPFOJTe74ewzqIiYc6Y/bdY0HMAGNfpXdIcX2+REccsUVyu55MOqosWl6q1nmOAXgxsFSH1bY92+2MP+spGPLXdrYpyu9ovWMi6xfS1tbq2j+zYp9Nit3ORiJqxAOM3J2h4Uvlsc0Uwiz9dV0Np8SRwv5GaWzvJdvXTDbKYzOpKuGY06zMFBNyKNCy+tm2zvmem2TpVBsJRq1W/nu8Jdrq6wrW6oVmr3HR7tVF5iuHOOICZ/ppcIxp+Vglzv+avIHPklic2Osn9pcq3BNF1bewc+L1qcloku3jNMHchWicSr7sgEzXntcgPaA0C9YG1bG0o1knpXYv5t3hvruadSZ5zCeu3midx2HbBNSuMSo4jHKCyOUpboji43kcGM1Yo2q2RbH2l8f1rklY77OSbjon8kxk3KlJ7sa1XpqLJxXBz7iuUuluZtRou9JT5hm2FpVCecPKJVlyobSTlzpHdtShNmTBmkjYVtYpYeXakQyqH1SWbnaoQiYE6IXrDNhZPgwqpcNomWq6y/CuzByxXGc7MLEhvBVrECBxNH9VZvmy2/aHcBbomz0VPBGdfF8XIPMON4Jsq4i7eu6cSCH5ILWIuaSyzEWiMMQl0veWszaKiGrffKzI2uwqjgjXRM6H1ixlXILRLFXZtWUNkR32dcjpUqnO8GZbssHTlp1J13LXZjI4yYIbC4eyLaosr9kfJYG61QtZDriEZFKtqPtDMMZp/BWOIIsAkDPrApciA1kZhri1gkjouYsmS5wc7RKR5kJFVR59Q5zkFgCVpYHsZ2Za1vm1luppzQ981qtyWWtYWm8wEDXLUcm4u117Aatdc4Jrk3C/AeW+adR4nSzrjJEXeDNwZKH1RWc7VddbW2y8bHaOHIxsv96dTJa3yJ6SEb9kcwm2v7Pcv45ZhZe2XwTrvsxPmatDu44CzNYp4KdwdidNjiFEu4lpGbISnStXQpdsTKKp0Fl3eYsG5ND91lxwHxHOHKZsLKg/szstkODKF4STbLcaZQKHBOJudrkVcTTWG0XaQutGup7hKOYoZlKrcUMJdvRct3+/yGy/3mtCJInTpHqeK1FJrpWyE8ddHtdqzVmg7wy1X35rvW8deBsTTUDcO0lCdSt7Dnu6q/7Bt7R0noxii2MwGX5moQ6/lScEKzaOS8ca5aeVyG19vKFVdhv1GOUd8dzYw/4XbJiJqI71OFRHPVRs5DvNIHDwV8eohKfWbVh3yJis7ZXariZbvBdvuFaJxD0zsUvSLFSrighjpDm+iU0ycWTAbc0ov0EbGuAtZv8tPq5uNzgcA2hpJjdLLbFiPPpD69PctYwLHqwI43vPAAca1ujZkYnd5gNDkQbikNc7oaqIDaqJUrBGe2pOpVCLfDoSK8k0+Fsy4aS2xfizxLNFGfg8k91FVNJl2dUmNdoQpwQrFJ9HxCls0oqiu+rVo7Y2BlsMnErtw838Sz04rKbA0Z5FiqYmKwM2EcmYbBHE21nWR2wDQJ8xaOz+ALnsqTkug7HC53M5Za5/PuZET92iaW+K12FuXoD935nCfFTaJ2+DgLObRH5IIkzOa2IbJ5zxeLxRpBsJREBgYvdXNn4B0yi4K8sCiHaGFAlZJTXAi3qYsrbhxXBXq8+Kd8VsNLHUOsE5jk9rpOR+I8invbPWwrI1HWbL6yLyfRN5HidFrOVX9+KGTWQvRLwMuL7oJecZeiLqYodVp5qr3ViWqPkm4vlr3s+cGYdb5Ww9E+ri4nLTMt5ISmsOiMs229VFm6ZZDDARnWEo1hnGnxG0rUGqZZtC2MVqRM80TmlWAUCgsTOeZLeOyajuktVt50ctSeE7tA/Zr2OJg8R8hZdeIArgNvNpo6ccSCo7o/LlWrR8HZ05zzTX4ANWPGlFRheLhJ1ke4b6qdhQPE8gkwxmFHYk8lzDh0WNJKGVVSPBVsy6a4FP0a8eZ5hpoCPMa4scYZTLYEbO2MMh2LRnFwmyA6zk5MSIl1sL847tDG64ZsjX18PuEXBhab5JaMxZm19ldWIvyFx7H+QFFnV/BIIueJ8LBh+7RZV7Oo9LGdGGR5R/DJuJ3REV2srkfl0gwwjXf746KW46Wow+xhC8BDdZazQpRiji3PCEGykV/gJSvByEVHLw3vhQSmUuBwmreLFt/uPUui5LOCbAhxKGo/5K2gw60tMseWOWuTHg8Lrh0jWM8DViI5Kyec6GAw0ZBcZ9waGb1DbctgWrbljiXWZLfsMx3FK3zTEK6+oK2EcFAG8Dc3zubzsoo8VG5VDzNaVTp4uI/ZqCscqZmz6xt+o15ZIuwD9sAsj96aDNTdEuAuLqyPnJYgm4NSWnxlrZIZvebXmRHoIlJE5jlHz3OeWxxXx6qhYDBJUiPhBNYCccgAI/qb1yrzRX32VzC/OtCkK0uggCuzoXF829W5jSy4fafaUUp4qybPcX3WzvuuUqWbTQUFgozXIRg0aU64QuMpGHwDR/ENEXHZdln1OpefCHNP7jHUTXYlPXBJmVUdd4WXVI/MeolB15cZ4JeFfjg0F3DWT9Q+J/jC7MQLvLMdSiNigkiokaKv+3q/TRXs1ktzXqoGRj2avHLesoQu5fucL064xXYafhGbo4N0lkLXNNth5i6014LKznn0GpQoGa5m/mE1Kyt7sePJJZatCmZzHtcLgKj7m8xL8a5anCq0uZ7yY2aK4+iy/Jib/VzbCBSuNcsFPS4XnnUqYMoHx2740BoZGNoHC1WIFRgGLlLttpe50d5WhCy0LFaRB70jWc1buWwPRt+dIWV7C6AfrG/BgdCsDbGF/TlyYVykSnteZpx8h84BJQmarTiX9RaXM+cYLA2zQtTLqPp2YFKbtUcQ9cIdRs7BMdRvnX7OdygvE7NzcV6UDMP8/eXTy/QM+vkk+d/92nh6uPf/7Bnj43Hg2/dJ94fIvu19uev68m9b9Munl8qNgT2Pp6h12obPh47/8Az187/4EmLaPD6+h52+9Bqat6ftjR1Of0H0EudeWzfV+K0u0vb+EPfTi9PW098z1N+eD6tf7i5l5f3J95s+8N5278+OvzXFNy+uSwAZL9MfHExf5fhebDdvl+HzqTLYPYLcxG79jZiT3/yqnBx9fq8xBf8VfcVefvu/TrjZkLklAAA= -->
