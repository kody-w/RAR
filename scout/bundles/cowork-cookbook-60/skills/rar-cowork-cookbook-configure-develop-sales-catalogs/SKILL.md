---
name: "rar-cowork-cookbook-configure-develop-sales-catalogs"
description: "Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_sales_catalogs", "rar_sha256": "21175272b2fc65993e2db4066ac109b65184794040d72a18bad0245d65694bf3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_sales_catalogs`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_sales_catalogs_agent.py` and in the RCI capsule.

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

Develop sales catalogs Configuration Bulk Setup — Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 21175272b2fc6599…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_sales_catalogs_agent.py` first:

```bash
python3 configure_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_sales_catalogs_agent.py   # or on stdin
python3 configure_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Configuration Bulk Setup — Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_sales_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop sales catalogs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a413df5a0fdc726b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopSalesCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSalesCatalogs'
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
    print(ConfigureDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObWJbvV9Hk/GHXyE72zR0d8ZCEQAuLQGIrV7jYQaxiFapX3/1dJGW6PFU93R0xEU9pRwo49+znd8695G8vTtfGZf3y5UULnGLGO1mWxEE9cwp/tiyHsk7BrzJ1wf+ZVxZtnbhdW9bNy6cXP2i8OqnapCzAcraqsiRoZs7M7bI7bZhEXe1Mj2de7BRRMGvLmR/0QVZWs8bJALHntE5WRs0srMscyJwlRdW1M+7qBdksTLLg02xI2njWO1niP1hNitVllrmOl86arqrKun0F2gRXJ68Az5cvP//y6SUB31++/PbiZU4Dbr0sn+oEq4d8bRK/fEoHqzOgHyCrRuCMAlxXQR2WdQ5u+UE4e159bIIs/DT7r/9KB6eOmp++fC1mz8/Xl+lH7YpZG092Ok0b+MC8ynGTLGnH1xmbDc7YzOqg7epiclMDfFlEr4+V3zkB3/x9evbxIeQ1CtqPX19KoMLd/q8vP83KGsiru+n768Sl+vjTa1YOQf3xp+98ms49B147MQNav357Xj/ZAsLvpEl4l/p3wPURUzf4+vIH46bPQ+/JTrDy5fVcJsXHB+OqLvugcAov+PjTP2LrxYGXZknT/kt8f34wjgPHBzY9Ff/p093Jv8zmT4Peef5jsRUI679jCSB/E/dp9nTUP+J99/9/Y50lBUjqN4//Jbu/WjD/++znf2jb/7Tg0yz8+rIKsqQH2eFmwZfZb980hVv+/MH/fvPDL78D1v+UjVZ2tXfn8C13iiQMmvbbt58/NPfbH375+UNXgVwLnPxbV2d/xfOv/HqX84MHn1Qff1wL5J+KtCiHYvae6bPfyuo/6t9fZ/pU/N/vN19mf6yX6TOfTUa8CX244A810wBd/+DHn15+BwBRAGs67/4YVPl//udMTLy6bMqwnWleCUAIBLhN8mBS/hgnzQz8m2q7BgBSNwlw7JMO5P8U4UnjMpz9+n+8O2p+9p6oCb0hYfDtiX3f7tj37Q37fn2dHQHfsk6ipHCymcoqytfCiYKinWRWddAEdQ/QxB3b4DPAoc/TF4CUs1//Getvdy6v1fjrHTaTBzqpy82ETE2XBa+TdUYcFE9bPADBwTXwOiAgKz3nAcLNJ2B1U2Y9QLbJE02aZNnMT2pgdlmPD0juii8Ts19//dV1mvhr8YBSbPboEQ0ECN7VmX3+DMwKsySK269F4MXl7MNvv3+Y/d/Z/7TqznySoQBMf8YCaLjVZGkGaqvLARkIEwgsAI57LH77/elcwKYATQ1ELgmnJjUtBrmZBv6bpzWB/YwS5MwNgIeBd/OprwB8niXt62wTzt71BUKnRxOCx2XTgoZWBYUfFN4IuDrAnHdPFmUL2lybNOH4adY1wV3qr27t3FXMQZE77a8zcamAflFmU3Osn/0DLC6LBLj/PQ8e9wGT+kMzW7yxeJ1JUzbOKqd2qrh2njJC5xEX0CfelgPmzqwIhq/F1BmDyVX30ni4BxABz3jPkH6eYg4aeA5wwG/eZN9pnKmrHe/drf5aNM+0d+opFB5oA0Bo1IFODZrB354p1cRll/l3/wFNJ07PKPjPqNxzcPXXY8HyhyliMQ0WGgCQava1Q2EEn/1/HTomvVmeVzmePXKrGScdVevhz2lQmvz+mK1A+5+BpHrUzveR4A1Q3nD1a5ElIDnq8W8PynsUnjQPrAKF7gN4UO/8QQoAf0587xk6ZVxd333xtXgD8E/AMXe0AiaAcgbpPnnjTeD09E3TGNTsdP29md8jWvuT6SALZ1XnZiBDwiDw705o43qqsmccQLoGU8UNceLFP1g1A9xBVgD+M6BEAuoGgPzddVIJzAQFdo/CO3kyjUhAC7/zgLZgEg1eZwYolClZGlCdYM6ZaIAXPtxZzfIA+Bio+O7hJnaqhzLT8PpU0JliUeYgf/8YgefD76l912VSH3B1QOyBL4cJav3g+ojsu57PWAFl86kY74t+DPfT1tkfO83fvhZ3Hd/RHdR4NjXpPzhnBmorb+4pN0FUA2AmD54JBDLh3o9fHy310bPfdfnyp4n947831N+b5OnHyH2ZxW1bNV8g6NHY3vraKwAICORIUgXN9x73+Vlqn++l9vmt1H7g+3DTl9m/p9sPLJ5J/WWGvMKv8PRon3jBlLXPD3DF8vPC+oxPT78WavA9xs9EmOA1G0FTfe81bySg4UR1EE3Ej97TTC1rAF3yDrYgCl+L9zx4VskDa0CjbMo/VO+96YKoPoL23hPAo6IFsv1pRIuCafeSTeo3wcuXosuyTy+Fkwf/wq5lwn2QqcAZ014HVA2YeNokuF+9Tz/TxY9btXs9TbBYfpnK6tNsmlQ/zd6Hzk+zt23AfWNVdGAf9PM08E4iASn49U77vg90gxew72rHalL8sbeZ5qzn/PtnJaZqAhp7wdTLy/fynCT+iQn4EkVB/Wcm8v2Lkz0xommdqTMn7VtlN0BPv5sQHTgQVBwoIoCNHVjwZzFATh1cOtAC/cnc7/77blb5sOX3uxvaxwbxt5c3rHjG4DkMAnJQlJ+bqQlCIE2BQHD9SCjw7N8eE5/rAbqBMQUwQBGEIlAKddHQIwmGwQLUd3GYJB0PgRmXJBAapxgcxmGfQh2Edh0fRnHCJwmSwd0QA/weaflt6vTJpBPqOB7tUQjuM5RDegEGu5gXICjiU1gAEwwW0nSAA/e8L00BND4NfRg2efF9Yp0c8rT3txeXxAGlgDcb9vFZQozuuAbkqvF+Xmfz6xUjD1hQZuERYXv1dpFzvD9sRd4LyN0Qm9bWzbX24uB7wa9U1LPIDVTu50PfGX6eXdXt7kQdh7lwGHZIRnW3htoPcxE5nFRHLMjUzapYNYjmstNXFzunTjpB2hZp6r7m+NLGJRsaba8X/eonLTOf64aXGUZ30JD1IWqr8831R37XxisxkWmC1O28TTfmQdVTygs5Unczi9Sv0nWHoDzGnT0CIfR6v1F5c1S2QtW6C8Sw693t5Jwbcg6FRXFl/LxOxjDB+7zOGEi57jppk+TerhoPrd9ZWt35xjbbdRs0L+HOJrdjgGu0gNcXuM62o0xXyKnJLgyVFtsV53Dx6nRxmjqzctMe53bva+tLlbT+Wbkim/VVd7lEzVrAxxjdaJdhu/Mu7RNCc+ZXnqjK80XR1YaU2kVPduRNPGtVmmqVevHVE68jVCz7SNq1p3p73M0VomMH3CYpeojVbb41cExuMZhKFLbzS9UduEUryj06bC4BSgw9um99n9Zw0tGHPrOL014+O/XpKIxYeiJOvrFes53icxHaKajNW5cuQtHbadfanS2nmeifkGS0txBq1UVQXQrdNZZNvaLpYX/Qd6vC0ioiiAwjoUfGr9ymOvU86y/dy5p0CWceeKLU+J27RC9YgTOWVKf53lUQGhlyUb4GG3pXOXlv99jWN9fdVdQbHWINQ8IMfZfHUsL1c5S9jIf1bdC9udSdqKG4JYQurLIa47m4Jy2cWHKrNVUt+EtFLTMcqqX+gpuWvA6dqzkGdGPB1LbL7HMnqPNYQ830aOWlE+X17nDU2+hS75G8LTc+ITUJKeAiu6cDoYGDQdVrSr1oG2EVzqO4V6qMYRSFFhJyZzrGzbXMStn5495e2q3RFSqKVSvOq9EO2V421s05FPaJmq94w9PiKmRUR4G11W30UbaW4KjSugPtwm25kxJ6g1vu+iQvRt9xF+6AW+qpHcpz1Q9nXrka0iiRi516PIbDBY3iMr0YhH1c54HCw57Wr7Fd3azq+dC2GRrHuYsPOL+UcovWJNFzFgedPdNhsllLKX2jDq1H5ft8UALxYGDu9mi653MCEZcTT+Q0RXA4NbeZm4kXyNWhatreLG4mbS18N2V8mCqi5JpmbWrx7dnmb6d+zG0owfcqwjgNsgzpxU1fnCiWVKzVETssPIMezypdQxlFufoqRC3K4ORC6im8gZmzbptn22Y3fLatT3OsPFYwU3sHCCG2mimPMF40IGV9JNI86eDo87o4rRlktV7pSIval14XY0I9XM5wqJRLbL8KtF17LJBG3QiwEvJJrXI32hDLjcDnnOp2KhFtqwu2W7Z7JEG6TSnSRB+zbeSnRr9YyL21NSlLtLbwWCw3GMxfxux2xpRKsgk1TuELdNipfixwrBfGiqcSRzRamSwdIqbu1NuQhrTrrR6TIOMQ5aLWeK5EMueV5FgWQ+RpjukfSwKyiN50Emg7+GeUnAdIAbVUGtoqs8UyGuXS4LhVj3JtBxIMJ0q9lRVF3QmUxMVNuYeJfXWNYIS7RE401/frul/vwqVMY8qVCL1ljLFeNdrnAitQRgLG6+tjUefcEUZV6uoOUsSWLOUJxi5Hl9s1VN4GmLEpW5ODs0B4qY1rgpQQJXrb+1mOK8qiTtnNUWsue9jeLsdTpnRLeY1Xhy5cN8ss6hqD9w9MeVv0VFSfz8eeN3BpW7grda/sDfmitXOzUC6KmEp07lHnGiK6griGyn6JbrYL3miuGYKF+FDT5mpstUJkyhVA1yDRaNqdt5my7oq6zxUrLDbRiuDDUImvbV+dlKzKSJ2G5smwPccbVDXQhLDRXnAbzotBxXGc6Lik1unGadPrl8oXSRWtXEF2j+ZuR0oRbh7IyzpgSSup9JbyklI8pfNVRW76DWbB8FGvWrw6dfPT6QIpZHWMcLq0bNo/caskPhKo7aXb0M+T0o5H7aZ0Vz2+WEKVoVBpHcz9JhtNM9l2srLGZYdrXb/uDjiqB4GUx3vy6MDINkypkFPWsQU2+R55m6edPxdP6llwRd/b0yuxw7V2tEIHcyEV84+BsRKudoaydjku0svKkcfrZjunliQFelvE6b5dHo2czWEmx71oJ2PNaY0kVHC58EqLKJYi7le75kQvHVpjBegUps1+x1/NY0WFrWnsMdA6+jE6zdt+5aDnLbLVgy5x91jHnRZhoXBITNV9NXAMq41rHarGugJdbzX0nqu0ToVmIp2Pm0qST8Sl3bJsM5jZftcY/Xl1Jgh3NHfE8nTyVUTVCotXe5DJiRm53frErPddk2AHdb7kxpWRFRdhs8Lh1rClfB9EuznRcaO6d6QtuUBWNdZR4jH1Nxq86sXl9nA4xzSG9fl4rnh+v1sWsNYZHS5CurwLVKFiTZ3btzBHLJaXkeZ9moZT+6JzzALakY2ZWisTMiKYbcU1BZkbRPF2gsmmzNY5VFCiCRWmpsR66W1VWeFEKB9buF/Ttq2Q+0u6uV23I70JAZrnmHOT1N11z/Hupj9zZD+uDwNHr9bVSN+qonLnnJeLO2khwTtodXWtueITWOfIqn8linTZxnSBrhQ5pvpTuTVucrIdWobB5zcdXW8GM+0Pt3LRjYofGPEZV0eGKm6a4y2PgmvPPQMdsVBFb5kj9qerDsvIIh6pQ+lJAsuSIUV6dtSVa5Vd3gY1WfAYWWdyuGDipa25nLQ1SzRJmNDcXo+bm2Os7UWeIkt3PPCr4LCLlAsSbpZjvHL8XXeh5DV767c3eHOxKAyJjNagMk22YLFgaWTftyEbXFnLXIVn96YOmyu3dJRVBRw0XObbOX6w6/NQFYsb3DnpzS6WPC8lxpKzuyodVSckUzMR89C4HcvNOtULfIWa0hrX5rRVJZ66H/Ws4AhPYGQhlJ1yq9ySarPOo1Ql24sI327mqis1jRPZKNME/UT5ex2VW8HmXbbltRNGnR0ZdwilFRwBl+wLt9QRdLyUInNVPV7wYR/ltAtZukR+RLpqSSB43BC+EbPYlbWTygA/5Ha1CStF2epXp7VMuTy7YCMGYJfQOqeWj4Z+Y9ztbV4hkoDIUktSrTaXztRyi4Mp0c8xjA33CjsO6X6o1dtZC8aNvFXn3lJSQ5nFl1exYUpyt+gaYpfEYjdXT5vOV3EhjPcsLzaLGD4rzp41OjPPulPRmvUlo5Y3kj63K1wy+fiSpBzR7xB1HbNaotdmp5yE7liIqSsuLDSi8JiPzao7lo7NdVoURCt5t6mExDlZSECZ8QrmPJcXfdpPXDmJJGF3utW7IN566vnsN/5ZzBAWUyWtOt2OQdYXC9nFKT4cjSjb0QmHo/Q5NSwMFv0zZwtsxktZJbPjmo2NPhYvcn3g0oWuUbiaHoROtI0jy8FXMJRBB++Ci6WbbjHcmzsnLl/yuRCevZt/XN9GZXf2+d3FDyKkseL1quK5EMsyVGJXS20hRufA4ZLGQYTY4VArTq2bdhjCxsGOY3Xbny55deQWjbjmBzFPktFjGa6+tVbD9qlIHiPs6teae5ifNeYw+Cd8f2CFssnMMscWmBmesMPWWNLpcckfoXBuHLQhqfgjaY4szwvR0UTl5TlGpA1d4vvmgnq3bL2NHUHfaopFs1J+DA1YWhzlXVk623rOH9u+RDgyZAZ+cWB5j+5urVOc+6xbd7vrwOykK8lcTvuQCSpMhOJaPkHkiCtX0wSbRUkPTZbAmMRGIxz124Cb38phNxgx1YDmWBzK8nbkpPwWOMJ6z8KbSCdgX/Kh5qSErm8WDWzY8HHHwbubtaEDbhutIabnIJ+T+NwVVO8QQi3oB2TFXHHZY+tgCw0rT8UbdhN4zNmMI0kMa3UtrOoSKjtxIMUWzyX/EvBnEewSAaYpxmZFE0VoeJjSBhiSKerAuxDk1nsoWqDi5QrjFgRdD1Bhs7IezTdzqDRCWwH7QWuBGn0q1yq/RfhIDTyNtkZH6WM+uc3jGE7O7Kku6lgA+CT7gWzd0u2cJbTclvBKttGjQnca3MJoD4nUOrJy1ZG7C73rzoMnBXVblrnHR1BGLOiSGAqB2Yp7ZjlcxqQnuQ1248YeTOFkpzPw0KYhPucJkkzsWCqo4MQI2zmGmd562ci+hKaOdtUH0pCu7XHMQ3POHmERNRKSJ5PdeMWZtUNKq5svEN3lrEOMNYfi8mb42xQ6aA6r9dqCUEKV9FeYWZDnqix9yGj9VLVjVrX062jXDrrK7EDQeh0+H9JljwiFXJFjeGWgMfLwbbIRFCig1sxaC5fLTq+4g09FKo8XQXGwjJHh3LZmyiC1BpnbryDlyBylQc2jima0YyQXC+Gce6mnbr3I5bpT1eONIMXYRg2HIpN6OSVjHDQfce2oGr1xD6pxxualcMNIcqfYrmxBpwWykTaK554hkTitOZU421wUaaIMSvRoueOe9bqo3mMDWlZ1KdGnJOpxkNZVxdNCy2D0FXUFL8u6TbcyK1kehXznKFnTgV2h14Xs/HqszGWvlPiGQjUjnuMk2fVpXfs9xp66TFjLbmRxuHXikBQXxrh0aMVb5bTA66Y2h2icPY60UXsmmg6bzXpA0SK4uYRgrypM6RLqat5McocwXlKRgnzb1EdYNxXY79cblAq2u1W5NVEpaskzhdLiilzghYKkviBo4jllBBfOTiyhM/YxaKODR53meHSD2Db0+hu2ukYoxrhXukFzzGeQUqHybm4mLA91fCiguK/FlLobpbnuaec6pEwPS7RDitVZZzPQgtocAUMCcnIXCsseGpORv20opLPOYahl8I47LhZYtlbAXiW+1FKtXL2tqW4IEjEE3pF5R5iPerOHj+H1Yi3KxfYY1xe873vhqnIMX0hXWbEcRWx64kTxjJp0lpmL2hLxB3h/ulJJxJI8U0TsyrMCrrmOHtxZnSXHih1fyBxe7auWRHEkkDsC1DWdOdHC4lOwQbwKCbJSGkIWjuX85uQ9i4ZNoLLMZqnjEbtmyqUHDUOUXKATivPSQcQ94lDswthCDeIUVMcjjwh72G3oSFgbsK0wtiCH831/PiaaSViiBykBsm4UjxAlpF9dRYCmguSdaZkqd4tluCLWsbcmVN8oad0nXVobdJbRIBJvbvNOh0UvJTGBPYjNMpCzomUOVqJWZ26zNV2Sj5VGtcOTqg5CCa3NA4cHRbv0blU1uCVDUKxS+8ohXG3z1I7oC8uyf3/59DKdVD/Pm//l98nTCeD/2kHk48zw7b3T/ag5cPwvd1lf/nWVfvn0UnsJUOhx2NpkXfQ8mvxvR62f/9nbimn1+HhFO70eu7Zvx/KtE01/X/SSFH7XtPX4rSmz7n7Y++nFBTuFImiab89D7Ze7UXk1nZC/CwTfy9oP6m9tCSxo4pfpDxGm9z2Bnzht8LyMngfPn178EUQm8ZpvGEl8C+pqMvL57mPy/PTy4+X3/weriOucxCUAAA== -->
