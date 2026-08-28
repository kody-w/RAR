---
name: "rar-cowork-cookbook-demo-data-monitor-product-performance"
description: "Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_product_performance", "rar_sha256": "66b500afd2579c6cd0cb3f9224daa00a19dcb08fc172eea1261f2b5fef1b26ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_product_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_product_performance_agent.py` and in the RCI capsule.

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

Monitor product performance Demo Data Generator — Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-product-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_product_performance_agent.py` and embedded as the fenced Python below (sha256 66b500afd2579c6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_product_performance_agent.py` first:

```bash
python3 demo_data_monitor_product_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_product_performance_agent.py   # or on stdin
python3 demo_data_monitor_product_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product performance Demo Data Generator — Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-product-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_product_performance',
    "version": '2.0.0',
    "display_name": 'Monitor product performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-product-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-product-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0f000e552949f9c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-monitor-product-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMonitorProductPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorProductPerformance'
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
    print(DemoDataMonitorProductPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6Z5PbSJrmX+HWfpB6IRUIEIbUxEQcSNDCkQBhiFaHGibhHWEI09f//RIkq6TenpmdvriIo1RFAJn5mue1majfXqymDvLy5cuLAqxssrWSJAxAObEyd7LK27yM4Vce2/Bn4uRZXYZ2U+dl9fLpxQWVU4ZFHeYZXL4FGSitGlT3pU4J7tfwKwmrOnQmLkhzeOvkpVtNvLycpHkWQkqToszdxqknBSjh49TKHDAJs4k1qSAhO+8mNcisrL6vqUsrzMLMv/MowiSvJ5UDh8swr16hSKCz0iIB1cuXn3/59BLC65cvv704iVXBRy8sFIG1akt4cD4+GB+/84UUEivz4dSih6hk8P4pFXzkAu9Nxo8VSLxPk//6r7i1Sr/66cvXbPL8fH0Z/8lNNqkDMKlzq6oBhMMqLDtMwrp/nTBJa/UjMnVTZtWoJwQ1818fK79TyovJ38exjw8mrz6oP359yYsRZQj515efJhCRry9lM16/jlSKjz+9JnkLyo8/fadTNXYEIL6QGJT69dvz/kkWTvw+NfTuXP8OqT6Ma4OvLz8oN34eco96wpUvr1EeZh8fhKEhb6OpHPDxp39G1gmAE48e8W/R/flBOACWC3V6Cv7TpzvIv0yQp0LvNP852wKa9a9oAqe/sfs0eQL1z2jf8f9vpJMwg87/hvg/JPePFiB/n/z8T3X7Vws+Tbyv0L2T8Aa9w07Al8lv35TjevXzB/f7ww+//A5J/49klLwpnTuFbzAoQg9U9bdvP3+o7o8//PLzh6aAvgas9FtTJv+I5j/C9c7nDwg+Z33841rIX83iLG+zybunT37Li/8of3+daDCXuN+fV18mP8bL+EEmoxJvTB8Q/BAzFZT1Bxx/evkdJokMagPTwDgMo/w//3MihE6ZV7lXTxQnb+oJNHAdpmAU/hyE1QT+H2O7BBDXKoTAPudB/x8tPEqce5Nf/5dzT5+fnWf6RMcM+M2F+efbM/V9e6a+bz+kvl9fJ2dIPC9DP8ysZCIzx+PXzPIBzICQcVGCCpQ3mFLsvgaf4arP48WYMH/9t+h/u5N6Lfpf7zk0fOQpebUfc1TVJOB11FMPQPbUyoFVAXTAaSCXJHegSF4IM+wnqH+VJzeY40ZMqjhMkokbwgQPGfd32hC3LyOxX3/91baq4Gv2SKqzyaNsVCic8C7O5PNnqJuXhH5Qf82AE+STD7/9/mHyvyf/atWd+MjjCDP80ypQwoMiiRMYZU0Kp0GDQRPDFHK3ym+/PxGGZGDBmkAbhl4IHouhl8bAfYNb2TGfcZKa2ACCByFOi7ysx+IT1q+TvTd5lxcyHYfGXB7kVQ1LXQEyF2ROD6laUJ13JLOxYEFXrLz+06SpwJ3rr/ZY1aCIKQx3q/51IqyOsHLkCfw1inmfBBdDo0L4353h8RwSKT9Uk+UbideJOPrlpLBKqwhK68nDsx52gRXjbTkkbk0y0H7NxjoJRqjuQfKAxx/L+Vi27yb9PNoc1v8U+pBbvfH2nyXfnZzvda78mlXPALBKcC/2UJR+4jehO/re354uVQV5k7h3/KCkI6WnFdynVe4+KPyL/mCs5JOxlE+ebcdYCRt8ihGT//99yCg8s93K6y1zXrOTtXiWLw9QxwZqBP/Rc8Fu4EFsDKDvHcJbfnlLs1+zJIQeUvZ/e8y8m+I555G6mhIiJzPynT4UDII60r276eh2ZTk6uPU1e8vnn6BW9+QFLQVjGvr86GpvDMfRN0kDGLjj/ffa/sRu1By64qRo7ASi6gHg2pYTQ6nKMdSexoA+C8awa4PQCf6g1QRSh64B6U+gECEMHpjz79CJOVQTQuuVefp9ejja8GEiKC3sUMHrRIfRMnpMBUMUtj3jHIjChzupSQogxlDEd4SrwCoewoxN7VNAa7RFnkIf+dECz8Hv/n2XZRQfUrXGFPs1a0fvcEH3sOy7nE9bQWHTMSLvi/5o7qeukx8Lz9++ZncZ3/M8DPRkrNk/gAP9r0wfXj3mqQrmmhQ8HQh6wr08vz4q7KOEv8vy5U+d/Me/1uzfa6b6R8t9mQR1XVRfUPRR597K3CvMEij0kbAA1b3kfR7x+vyMss/PKPv8Q5T9gfgDqy+TvybgH0g8PfvLBHudvk7HIT6EwQkBeX4gHqvPy8tnYhz9msngu6Gf3jAm2qSHNfa96rxNgaXHL4E/Tn5UoWosXi2sl/e0C03xNXt3hmeowKye+WPJrPIfQvhefqFpH5Z7rw5wKKshb3ds23ww7mqSUfwKvHzJmiT59JJZKfg3dzNjFYAuCwEZ90EQewh7HYL73XtXNN78cS93DyyYEdz8yxhfnyZjB/tp8t6Mfpq8bQ/um66sgfujn8dGeGQJp8Kv97nvG0UbvMA9Wd0Xo/CPPc/Yfz374j8LMYYVlNgBY2XP3+N05PgnIvDC90H5ZyLS/cJKnsmiqq2xTof1W4hXUE4Xdj2fJtB8MPTGemBlDVzwZzaQTwmuDSyI7qjud/y+q5U/dPn9DkP92Dj+9vKWNJ42eDaJcDqMzs/VWBJR6KqQIbx/OBUc+79rH59EYK6DnQukQlE2OZ1anouT9MKhHHfq2DNvgeOEa1lwAFu4jj2dew5G4wBYGE5hHm6THvAwG6eAB+k9/PPbWPzDUTDcspy5Q2OEu6AtygGzqT1zAIZjLj0DU3Ix8+ZzQECM3pfGMFE+tX1oN0L53smOqDyV/u3Fpgg4c0dUe+bxWaELzaJ12pYDe1FS4GIa6N4ODW6wL7y2iW9UVEhivDovYxIP53sNX63JOLRSadXvIk6wlrf85Dl7pDdJ2kT9QMm2Ch9Y/DIlage3mxkfeyRJ0NqSWee4k2KkWsja1qrXxFW1gt5yruKwFJLdNRXXl0V8cNQztK0yLQfPQ/EaUWtz74nqgTPCAQ01S7sVMgeHE+XAaUK5X2MVXSdrcrrnVtNtB5TqmjjNnIg0jTP0Zt4ZNxVEgibs0+2Kwiqwyd2jHffA2MS0aGwIdN15opEMyJqoNSt0zvF6sz7omluqSHGlpkpdy/qB3yqVMLtub30hlH5tn0AmcqLYcc6tPg1udz0ftbOwXlObxuAC3TBJp9ol1yKujCsXyEeu9RtliuNbacOAa1KJzvYwu0aKVUj8sDob+gY33aiybE92FLpJb/j2Is7kKS4czUglFu1NoIaUPRXaoeAPYkkxpwN3rgKRjhUzTBosKkya7HanHUce3Hi1anzuhpN9KvVk6yX+dKsVYo3FZ5MconwLfVG/qrseTQo1pxY9p2+NNGhsH9kK+oG9cHWM7Up9V+uBKa0xEVT4VaG3czzcXxFMT2JSETJXvZ6wgMnU+flC7c1wr2m3THFt1O6GXDpti8xtcEO/HfuNLs28JX20g3Cnnzl634MB5U1m2LmBuawOqr2Zc+ZwRWr90Ijz23o1kA11XirVoZJ5tPavQuBlQb6g7KrDoiO6nqpV4qDrtY5Hl6hXpYJkWaWbsTynLoKqQ2mvuPK1qWluRNoHu20r5bbqpCFV1qHL7apIPFyVq2UhWX//Wdy4gl80pqUQyLnEkeUS3TjohgRLDlwk2Y7kfi14LYpLhzlSTY/Tft5KfKFmRr1gtmGPYPZaR+TmerlxQ5EXsdbXSqmHvbyh+4u92VRb4aJ3HB+E2B4sz/sk4z3OqJY8XZhK7gbDcN0x5o4ckuXyYverpMm2zUF3tiemWtYb1ZQiVZGlDuB7NthdzP3MXzWXkNtq8nmTuluVcM5iR/CRw+WIdMsMKY0M77LvNuThuAeh3e3ygtx1CcXVvXoAMavbByrDA8ucrW2RD5BDz00vpDpUNRqhl5kSpft6NW2yiCiXpjFPtQ5cS8FdBXIsV3u86dOKILM86IxNxVSlFiMnBaXkGLHzK3csVcnJFpebc436WEmumVJQh0xanTT1mm4B2cw1WrKSAqsJWXFwpLl5t7xT9UtrGNd4PcdAOhO5DqS1VRhIc7hsgLbNNvLUATaeX4BYC5xoHEVDaWOn9KZSrJdyxS9lGIXkSQUBOT+f12RIGVqoNmq7Rhcy3+XX6SX3bvvkoOaYcz1TKyddmquUX9dlnUS32+ICHHvtuzzesroT1pl8uLhBKu4s80yuk551N4o5JVNDqqDbdqJC49WpWEjZPjnNrrqxIvY4ju7mmpaWytlLydih3IttKfauQ8s2PbdW5+DL1NAv07lM5rSyuNLLo1luaLnx0RVOCMqsRDsZ31HtGaOc44FkpyShxpfcNnEIQYsIa6JfbPbePE65q99mcXfcDfrgX4OCJVdGOcv2l07IyMaL0iWxEXdieEm4Y4a7orF3pbTI5AGYiHUUb9LacHytvRyYFcequE1tMEUM/KbdbmKSE5iAU1r5SlX6lMyVWWFi8jS3NH+HT3OYGuWwOLmiUCl67hQXgw0Fv1BPJxJP0xW/XAPMJBxxGAimWFGFvzDbTcgRMDxRwR3mdDgIp0FqbhVOedlmvvCMYrmvVnXU24Z97C3N3Jz70slEM0ZXvhOGpzliIWBTrvoVTQ0JvukvxLBG9EPvZFRV3XazAes0jy+7vcftSHnK7Zty1tmO6jOFvtwpqZvPsSDVgs2FajTlMFO38eF22+NVqhqK7e8bH9Pa+ZIwNj1nNT0XS8VsGjOVIgdmkdYKM1+eguPqcnK75dGSKbVLZOzsGmx+vM4EjDvSsP0QrSpa6mfJ7PEBKnlV3fJIqxm/zK7aKSwKS5DIqCt9u6QvG3KKGUmdx3yqYG5Vba1s6vPxSg2AUdUO0UsNW0v77TBsbWGj6sLFxC/DbNaJydYUpkmEUTe70pV+YPJTaKwrRtaL6TWwy0JB8LaehUMtOEtSbI7FZpNTFe/MG5gQr0wzP5u3ky/JWmH7c4wj1bVyEnab/QKzrLrw06AbJCPTC81WbuuDz3GFZmzFKKwS3edKndVm2qlCRfJMpd5eYzttpyLBKuanS6INiC3TycelbpZHMaaBGmj+lAt1oeWpisJUW9hm+37dz8/M2m/nFq7bLXbDQivilVPPLmtC0Xq4qU3wUt8LObKv9sUlwf2yT9j5IFj+GoG7o0uXKwnVLbb6rO7AGe6/rcJM4gPOoxpmJftSkhtxWSypw2AIfkdpNRax0OCrRNSJoKbctXmU/aJTtXO41felivunXdcwhKqZeYr5ikPIs8uBDHul0PM8Z25TNjlTPZfcVicrEuLOJCO6IRd7JA3YE3s71Ah9QvB4N7PEix7Fpwb0PoMQR67Jun4aOlRchxQXHYpuXrMzdOho0qipLl+r3nlY7/Qg9VywI8SgMEOw8CIDXJrMwHrbPaeLlBaMPaXJFI4QWM3sRV7frwcpITG05f1klTPbLVsWNxo6txrPd8iaSw4V02lc1214bOFkmyMvQBytTchyKh6d7YyjhWE5YwxlXVu5tt7tMHV1bsuQX1uyys/KMhOs2uCugtQMXCEXRluBHB2YS5s59QzixRX5oeilVMVzST9e10uFdjXmRJIpSM9JxmyNg6/2jEnJ+Zoyl1f0egb70HXtRPTOUV7WBDtvrDNscvNTGhPXWRzxxVKPJe4IdzhalWfcNo7SS31jiN3Ary7goKwJNV0Ra1vwjOOVQeKW3GlDHFRDpQSWpnSb83pDbpNBDgJkebosckeUcPOMZNy+zZnElsqqrTQj2ZLmerUiBrPbmdS1celjPT0UbaOJIhMfGz87iV5qA6mwadEddvkcP3gz/FSILU3YMo5qcbLpcGnqunxBXNPD2qUPGbzwHE/Mq2HunVCmofq9Xib7jruofictvaBfnrppSMGFNB1OK3MbplwNYIZ2+KIVZ6vNyUEA6+Y5UPV9LcyOLFKI5gx0PMJnVwpM8RN2sqyYPRQRSODOLIl5/cqC+aGCHsjA7O2WJydieLOMhyXuSsqRPEmZxoBYNo8qVbR9P73Nj2a+RsTTALt9XpzzidhP4wu3Zc2qS6wZocVZJhzB+rxKz4VIq1tvbc9ujXnbWKuTSGQm2ZgeVwXGicAlkLArlWpEhtuq+ZbTpl3SLWxf87nU8MR6JdPR1shOh4UQOQx6mksa2ESgkGYufbb8uL0MLY0VqaYEYF5hh2axNCRU1W0r2bDFdgMbgoxy1us5C5hUy+TavIZwe7lb0WFZsOhhe8IgeJvtgVjwDjXrlwV/uZwDn5gvL/HFGeLNsLGE6VUV+lN0ls5l37tuhNAygxnmcGI2OaNrx0Rv622VndS2UFZOuMy6ipqya3Khr91cSIxYF6d9VQFxKagiPydarro2wN0mrDvYyKUBG4Z2jN1lTlPNteTJYrlmlZWxxL16aZwgp1XCWdEugFupLUKxhZ0bcdYkyLEDg+pEC1K76osZlQWD5ppchrQSi1AUUrudRjdsiOy4DDR16/AA3zHunpJXan11V0SCZ0xezLzWdDOhxc35MujFjMscz1nUy4XrY6dmppO76VaN5a3VXNReFsKbF6ArhDlPHWa2pFmOms92jEGeF920vqyixt8tjplR8a1NxWVkV4p3jWrAM3Lm7Gypu7UYh8z1vD7u5NRGNHdDMlgRzGEf2yzp9HATsfAok1SEorRdov6Scq7t9JajaHdCb/YZN26egKD5FjWPdXF2ZDytfbhfivM5e5RPgIXF0ddCs2VlFz2FiLxkJByNzVRU12y2s+NgDy6er8gdAvMJ60u9iW6m3k4SSmzKIS7N+7aPpUYjx4ANhhpu7S59oB7dxh7SI1AvwTTuxCnP8XsJzbvIE2IJ2fosTlzpYuUe0KUgLpLpdgjFDe1cPIbEtZl3MeY3B9D8Hg/Wt2G6YWazPWhoVm4FXGe6HXnliwIHYW3uENKKUEMDVxSpvUXbnZLstPAEmWdE2WQQ4AWOw+KzjIQ4yGKIUbTKduFh2/J2OGy7BW3jc5wF13QBiFao7MWFjsyGAh0y67f25cAJ7HEGCrJarrzQqpO9cKrPlSwRiWPD73CxpxOeLMH6tJeG7YZEQkKt58r1tmkXc6+VpvmuG1ah5K38lmx1WJsW9HJuHhBe16q5QkelcMwYh8OiA3GyBjYcykV1JkjgMT67Ps58UDDlIasWtzrk/XkorVhhk66UfHu7nfllmwtiuF1dK29AgrTJcXIlI2iitUm9qpf8gnJirB5mrnEJN80aR7Pi4IZ2arX6UWGrDGOrykV7/xzUThWh+4bvDIqIMrN2ymaw6zbj8xMh4/PtGu3co2NJy/nFkm4sGzqYT5z3BI1R2LyfbW9H7eLiAkNe+GV1lRpDJ4wFW+aGqdLTmTIDdq2by+g6g0lrt5nVy11OA6jLtmU4vsnsJXpOm3PV7XO2F4yudne0uopiZFdOM9UzxYUpA3nnN7RhEfK59Wu+mp3ZiJiVvJug9uAmGXpzkAVF5nALtT/tEJpEay4g/e3iDLYzbjdsaq+pNyUp58DETqiLoPtyPdOJBcmaGYagSw/NFiEMcnpoiMj1FLdP19FhMwtW6X4ZtZiWGbMLStmbE4isYN7pZZnyN59DeELxuqtFhmjpabP5QpQWfh6A0s5IaXfeANN2e26GmeXOUWDE7nmNiE7BmT5KzC53cY+Bzho7h7YanPXWaxw92BVFQeEkyxc13PiQAJfwGVVpvrha31hqRwueSVA+zCrHiMjL6/RAk+IsZWNmUwYrwJenTRGxabfREHW1SN2TQAndMtXP/gnXaQEkSwUsYv7kHR0f3ekn69gEN4m9RTRGEkwy1xfrejAyyWTtHV9ICV21iyH0/KZHD1SN7pVof45SbEgDpWs6or6oXp8sr0eiFkgMHxBs7rPZwmkY8sQ6pL47436wj86aEyylYdrJKBG2VDHvo/7cHG+K3C8grKm07ZSmnl2xlWHMgY/SF1yL43nBMMzfXz69jMfNz0Pjv/aOeDzC+392kvg49Ht7jXQ/MAaW++XO68tflOuXTy+lE0KpHuemVdL4zwPG/3Zq+vnfegMxkugfL2DH915d/XbUXlv++LdEL2HmNlVd9t+qPGnuh7efXuymGv+oofr2PKR+uauXFo8T76c6j9Pv0M++1fm3EtRhOTILs/FdDnBhXny79Z9nyXB+D20VOtW3GUV+A2UxKvt8pTGevo7vNF5+/z+z+zkFuCUAAA== -->
