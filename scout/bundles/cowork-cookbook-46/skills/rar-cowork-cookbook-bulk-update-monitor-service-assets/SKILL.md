---
name: "rar-cowork-cookbook-bulk-update-monitor-service-assets"
description: "Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_service_assets", "rar_sha256": "04d4eb275a42eb84f67e8e0edf42fe84275759d315b1f84bcde2f96cdb27f6e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Bulk Field Update — Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 04d4eb275a42eb84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_service_assets_agent.py` first:

```bash
python3 bulk_update_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_service_assets_agent.py   # or on stdin
python3 bulk_update_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Bulk Field Update — Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_service_assets',
    "version": '2.0.0',
    "display_name": 'Monitor service assets Bulk Field Update',
    "description": 'Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77eaeda621d19829',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMonitorServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorServiceAssets'
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
    print(BulkUpdateMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPbxpLtX8H0fJA8aInYQeqGIx6IhQCJhQTBDZZDxg4Q+0YsHv/3KZDslj32nTt+8SIepe4miKqszJOZJ7MK/PXFapswr16+vOw9K4NWVpJEoVdBVuZCbN7lVQz+5LENfiAnz5oqstsmr+qX1xfXq50qKpooz8B0piiSyKshC7LbJIb8yEtcqC1cq/Egy6nyuobSPIvAXKj2qlvkgI/r2mtqqPKcvHJryK/yFKwLRVnRNlAS1c0r1EVNCLnV8KlqM6iovFvkdZDt+XnlAXXSNGo+A0283kqLxKtfvvz08+tLBN6/fPn1xUnAAkCzJdDncFdEeSiwf6zP3JcH0xMrC8C4YgBIZOC68CqwQAo+cj0fel59rL3Ef4X+4z/izqqC+ocvXzPo+fr6Mv3TgYZN6EFNbtWN50KOVVh2lETN8Bliks4aJkubtsomjGoAZBZ8fsz8LikvoB+nex8fi3wOvObj15ccqGBNMH99+QEC+H19AWiA958nKcXHHz4needVH3/4Lqdu7avnNJMwoPXnb8/rp1gw8PvQyL+v+iOQ+nCo7X19+Z1x0+uh92QnmPny+ZpH2ceH4KLKb15mZY738Yd/JtYJPSee3Pm/kvvTQ3DoWS6w6an4D693kH+G4KdB7zL/+bIFcOvfsQQMf1vuFXoC9c9k3/H/b6KTKAPh/4b4X4r7qwnwj9BP/9S2/2nCK+R/feG8JLqB6LAT7wv067f9lmd/+uB+//DDz78B0f9SzD5vK+cu4VtqZZHv1c23bz99qO8ff/j5pw9tAWLNs9JvbZX8lcy/wvW+zh8QfI76+Me5YP1DFmd5l0HvkQ79mhf/Vv32GTpaSeR+/7z+Av0+X6YXDE1GvC36gOB3OVMDXX+H4w8vvwGGyIA1rXO/DbL83/8dUqKJonK/gfZODtgHOLiJUm9S3gijGgL/p9wGBORVdQSAfY4D8T95eNI496Ff/o9zp8xPzpMyZxMXfnuw4Lcn/X170t+3B/398hkygOS8ioIosxJIZ7bbr5kVeFkzrQo4bxoP+MQeGu8TYKJP0xtAktAv/1r4t7ucz8Xwy53QowdD6aw0sVPdJt7nycJT6GVPexzAv17vOS1YIskdoI8fAWJ9BZbXeXID7DahUcdRkkBuBJgbrDncZQPEvkzCfvnlF9uqw6/Zg05x6FEk6hkY8K4O9OkTMMxPoiBsvmaeE+bQh19/+wD9J/Q/zboLn9bYAuue/gAarveaCoH8alMwDLgKOBeQx90fv/72hBeIyUBVA96L/KlKTZNBfMae+4b1XmQ+YST1VlxAEcmrBnA0BEoMJPnQu75g0enWxOJhXjeQ6xVe5nqZMwCpFjDnHcksb6AaBGHtD69QW3v3VX+xK+uuYgoS3Wp+gRR2C2pGnoBfk5r3QWAy8CeA/z0SHp8DIdWHGlq+ifgMqVNEQoVVWUVYWc81fOvhF1Ar3qYD4RaUed3XbCqP3gTVPT0e8IBBABnn6dJPk8/v5RU4tn5b+z7Gmiqbca9w1desfoa+VXn3Kg5UGaCgjdypIPzjGVJ1mLegFZjwA5pOkp5ecJ9euceg8te9wVS7IeHeSzxKOPS1xRCUgP6/tRuTssxqpfMrxuA5iFcN/fIAcWqPJrAfHRWo+xCY90iY773AG5O8EerXLIlARFTDPx4j79A/xzxIqq0AUjqj3+UDvwMQJ7n3sJzCrKruOHzN3pj7FYBypyngGZDDIMan0HpbcLr7pmkIEnW6/l7Fn+hMGQ1CDypaOwFh4Xuea1tODLSqptR6+gDEqDelWRdGTvgHqyAgHYQCkA8BJSKAOmD3O3RqDswEWXVH/314NLkFaOG2DtAW9J/eZ+gEsmOKkBo4ADQ40xiAwoe7KCj1AMZAxXeE69AqHspMLetTQWvyRZ5OMfE7Dzxvfo/nuy6T+kCqBSIIYNlNDOt6/cOz73o+fQWUTacMvE/6o7uftkK/LzH/+JrddXwndZDYyVSdfwcOBBIqre9MOvFSDbgl9Z4BBCLhXog/P2rpo1i/6/LlT336x7/Xyt+r4+GPnvsChU1T1F9ms0dFeyton0EWzECMRIVX34vbp0fOfXom26dnsn16JNsfJD+A+gL9Pe3+IOIZ1l8g9DPyGZluyWCxKW6fLwAG+2l5+URMd79muvfdy89QmFg1GUA1fS8xb0NAnQkqL5gGP0pOPVWqDhTHO8cCP3zN3iPhmSeAwrNgqo91/rv8vdda4NeH295LAbiVNWBtd+rOAm/auSST+rX38iVrk+T1JbNS73+zY5n4HgQrQGPa6IDEAd1OE3n3q/fOZ7r44x7tnlKAC9z8y5RZr9DUpb5C7w3nK/S2BbjvqrIW7IF+mprdaUkwFPx5H/u+AbS9F7DpaoZi0vyxr5l6rGfv+2clpoQCGjveVMPz9wydVvyTEPAmCLzqz0K0+xsredJE3VhTRY6at+SugZ4u6G9eIeA7kHQgjwA9tmDCn5cB61Re2YLS507mfsfvu1n5w5bf7jA0j83hry9vdPH0wbMRBMNBXn6qp+I3A3EKFgTXj4gC9/4vWsSnBEBxoEEBIhDCJTwbo0mLwDx7TvgU7c09xHN9AvO9OQHu0OTCxVHSRv05YTuuh/kLynHBHJ/yUCDvEZnfHjUNiMQsy5k7NEq4C9qiHA9HbNzxUAx1adxDyAXuz+ceAQB6nxoDfnya+jBtwvG9W50geVr864tNEWCkSNQS83ixs8XRonDZVkMbriifqa+LuKHzGHNRrKR6nKpCTb2qalqJBn3WHW7X7mNpb0lJxDYbGfU2ly2y9+sY7nGuZuWNmqxbWhsRZLT2jN45ItPis1grWUZalguliBuD3bSbVY9UkoUeC/28LW+6tVWd0nB2uLdfy+szvYB1t09brzgmpsS7IhGAmFMH+tolQYXmfiLsc0w/yUJ+XVaSoYU13ZW6VTSaLtlni+QP6Sjq5ml9Exj8lKJ8sbTSAythFH1o18R2SV3qswA7N6OBPX/ItDMNL+AVEeElmWtsczwGhZnsG4MSparmy8MGQwVZVEzK3HvEsV0Px2M7IPJ6seeOh/1Kpo8K7liCcTzMliGbtyUiJUQrI0F9lAGXsP1B2s7tDU9s1oHUjSelUWT94O2I+HI8Fo1SsBbct9VeVQEYGzzbN/nRd+ayQylD6gjMeN10e0Nm5kOxcffdaR+d9OsGDvlhF9vbm2Ly5SV0o9qVR0u7wAy5Wst1cDggMothp12HnVpujh1lc6amdWRmly0cR6WY7cNjKVWkOxxlBg7N1JhjK7LliF1/idGgxIydpV48dEPGhHFAh9Eq5NpeXA5LHauQebjvziGRXYNkv2qluAsumntlqCSN8GuyVW8FSSLcWj2MN1yWq3O2YCvRboMma5BOrNaFG5u+Cad1Ll1TpJHi4lixiLnKmhhFrXoUKtKTxMw4nnk2uRhEIc3UvFL6dRbmJGE6PR5ucQEpdY6VaVYIb+jlks03mj3ueKffY6utNFvZ5+Oo9Zv65oylbaRLf+U3CD83SEHXQgfbZwmmhgm6iDLUvf8kx6PX1QtBmXG224brOavMeGKeXoe9pvjSyd3wxkLsr5G9Het2JvgKFxGHDXq7+Q66OiNVXmKdY4kjEtPVxhIcOWjRQonDdh5q8wiJVs72kmjdzNqOt/kgeMNpKGgm0ihrV4gX36HsTpAxz9xczsJBMCMK0Tl8ufY4aVkHI1vz407pLykhukzIhO2NF7KlweyFcav05bgVooumr+az+JQKCCydx1EOMc6ur65GSCDgWZqgd+1pm+vnkIuLXWYqFeVZ6yari+a0mvW5e7UrwddqgcZmHaZaOOoMa768DXhO3U7JWSjrW5izy6Ek/L6xYtREbpogcZvthsnKhtsJJ8WnEnMWEWNc41gWcbfG0jY8dinXBhus6fIqrr21W23zdiEvN4YvuRnLjyVGmPPZ7NTmUdYRC6ISUnmO9KaloUlmbLaksd5lUZdI1fZKm8VlkzSzE7+7oQfqIJuH1QF3lTVJzAWH8bVhJVJXcs6fBckw9gJoaecdCKD9tl+3qR6PPEdTTCglq0Oxm3VqJl0j6ZaraOv4Guw7lRkex75rrF14MqzNORTSuXy5GP3qUhsgIFGUSvVVcjB55rAydtFiFwo47GjF0jPdrRyy1kKxxwY5JXqLXdJ+VvbLpFxT3gqebUtcuwojsTKPprjvGY9p5DZv4kWOYMWaWlBb0JWcb/jszBH+LehBumhqvxx74hCXjL1GF1YUwApPDKrGBQHn7I8CTCSLDq9WgKKbw06KFpf5xaokXtbGej/S3Q5gu9cMZ93P4SrBuszI6QKkSeynw+iO4bKXBJFhgxt7KAd9fVusAiucHKQXO4UV1xLLJ4IVUkKzz47GLcTJUo25E59fo4zbMPIxijF4TRrRyBLOLhakwJeV+Hg22fJI+YJH2G4z4OGaKS+Va+7U615aXBFb8RpkCFDENDTtBtjXzUhq3ox8EJ/MfU+6/o0u1hvlUBFjesxueyPYHYHqloHO5qUihCqKinIt88tdmOFYWvBVXCBzb02AOFq0xohjAcwflwGdzucJvpZ2wjwIkSK2RNUhE0s32ELoavc4ZIFtW9vSSnjfQjg5108g7a3j8nClqDwuCCuG3aUoRYwDW25xDLTZZc7dUo07M0Yf+sfgEsyGAEvYzFhlK9WWt1qvFWHTjVxPy8EmUZFCWBczNyaKzt2H/AFtmRnOnNYXo73imuUoKwQFHsMT+LQJAzIH3EAwfHwSqu1Zi/HiJPvcCvicGsQzD94d9xJM+yl92pw1Xj4sKowS4zrusP6CcSgf88k+iOMaoD90sLdYXWKYJ8e6XnLnytflNOYEpNOX47DrmkvJDlu53UX0RsMu8GUhKWqyZ04W3ubZECflcrhIZbi7OE1/5ZcjvcWm2mHvckdXNpfWEVZCEYxxzEVyfarSfYjDdhCgh/Ysr5XyUJSRKMn18rhLiBXX72/LfVHJa4L0DuHIYKVBkQavjHIdlwjvahZ6GAVzN9bswYJXs61LYGZyaAoWFIo+MH3eNHHCbhpVj8vTqNbxfnmgMRI2W5Cmdru1VHbXnm+ZhS0i+eQqlXHcqjkoVz6lVQdylY8qGigSt1tZC/SoLHq6o11eLN2Ukg4jfNU3BmJuJP10zosztVwaoU4P7W6lZaEjpEF7IpejLhcBKq33ebgLuavLaN2gVUhwcEJRgq2Yo9s1KvvYdROuLCZzlRlMKCpWwIjvqQEhbTKVZ7xW7hvt3LoFpxWV0avrYLGA5zOjoenG7JZrRCs4XBJgdPRWrES5fuYfrFN6lU0Tdk7Ynj4Ho7mHV0bpsxhu3cj+nHs6f82F9obN6uXOC2Rhz9YoGY6gEzg6V/kiDlKvmFZI8MiK8E72fFRLW7IGRvSqA+jN+31yTl2J9LlePNWSVThV0XKF7sgDrSHCxrWkc7WGLV9OdhvjHBaHGpVLebvTJ0yN274h85pjLdZyrkUIOjKKXMN5IMhNf1hyWVpQ5uakMIWrM2RcCO2+YLTIM7dUiA5Ie8AajwJVQ5KH9VzeZ7OQU7bG3jmproAoqahvRC/aR/y14NjDiIjbkJ3v+Z0uGQJZECoaS41UlmmuJlrYm7Rp8GbdkVR2OZ1wflyv67G7LWVEI3TxbCvFzcgEOV52i+seu5zWrHo04+YsGxtbkypZP443k4MT5bCGq7atgwXC00uaGKy+lzn9hitud9br6sigmdRYtdvkBXwUhXWPaYjryoVdlhrv0uuMKFPfwdXiMC4SnWPaIVondiL1m8shGLRlFWLLoNN7L4Zzd8MQdSGyoMPOgkviyEWn4qywq1Ze4+rI8lST1FkHxSLR7WJlc+thzbWzw3kujqZ2yWwxE0pqXbKV3BUun6yDa38yHHYbaGbPBoFoWEaSs77kY8dhLL3V3tpcqHUwRLROpEdOPWE9GdjuLh5KMc+CyKi0BaIkCj/ecphmzDm82VfUGlkGnjLIwXAtGzTR1yZRof5wqhN2ay7aq0UOlRMi6THJrAPcahx2iDR+w4GdFX88RKtOyCMzwMKzX7dMnxXC1j8XC9YgOKOaXQa4ptKT21Y9f9yYgS4ms3WzHqQ9TfaWblNw6Xu53aIDWw41fyPWXHrhb7SlcMepkhouey4jRsKL2f6YCSuDXboLd7vJFbDPKJHVRrxcODSgFEGMieVJPV1VuGbqg4IZAYq58t7y/dE46p17yDmCOefm+nzb40tM3fI0O+juNWBIqSSWlGsvIwRGeA6T91dkpDdT9VhdI2WV+vElwRrXqHkVx2D1Fu4JVzX6xMyuhyRp/B2hBOXmRNRXsmTT9aJcqBhpY5amiVV9UY4tqoXt4kjC8pLq5sLi6DdYQdnnBGtVShVbR4NBP90uXfpAaxoMeuzYoga8vm7PZ+WYl8Vm67aukPcgG5AECy87R8xniOlwoOE8785a5TQ2A2BZHEFHQ2YH/qisV+ZKMbqIyceZijEwfz0dHDgqK6GaqTf2pl3YK8uMsq2LlwPsL/OKuZUWYnggxe0FQtQq6Er1G03Re76adxY781zsmJBoZ8ahl4g9qbkggfumb+u+225RfLYgT/58uRNksHmhKhyWbiTmLBIal7c9FaD0xs029qAhKMLQDZKIAUltbNYPopSjCMA0s9yCpaAnxxspFLodMEWPkISuKltCli74+sYv++2wnpGIL2pKhXYbzAUF2T4c43OqB94iHJugOUpDcAB42WMqeodLcIh7FZE3srSZ5d3oK0kLU7GIzjZ0y5Hr2XKLLgRktYhEgfZznyGxI36+nOcLJ1kktbljLJIKbvQi3p7dZUCBLGX9hYMKCEJquqZdfeemz65lhW5npy1MXHgyM2b+QZcZVTcZsCcNHWeB4RmZ+YquRijYt3J9JLWdbEfjqp/TNjLHR69MUY/ulNp2JfpqtpTXw/jA2hfQMXFbXCtMZen50aYRJGXXGLWu5VfvcK71uaPMBhU/+OyOF8mKmfuGozfzfXYTusW87jQkF/uRPWk+G3RYd0Iix3MZWIlnG1k+eRuYgDuOJFZss7t6vDrr8piCq55YeLd1rBQpwaE7UaoRpFnUVwePd90OtGqBJy6FFa3O+XSr4+nsuAxndr0G+y18G4n9nIJZhAzbzfbatKem00AU8Znar/Ca7knk4IwaB9udnShIlVzx4TDfSRWKeIS7mI9bnwOpWMWL1nUdpXX2Iq/ZVWH4y/MsDGg6TCt6zmzXo7UIL7egEpFxHB2rnptX2kOWCdNQA0FbaJWYiJamLnpsDXfr0RpqxadV7hAzwRH3KA9fVULiu6rj83bD+JsFS1M3m48YbtPPgVmpK15N7gr2IDSfnv0jOyt8sCtFUko8zXfcrmoW+uXE0QNu+44zs0gTxXtk0W5IONwvqLm38uhh1lg9vdv3CQz2iuezXc+CVrSFU2Gj+E4cVgsL5/HzASM794Z4s7Uz68krQp4RtZkJFtymQrwUh+uVEZALm/VlhVX1OOM1NThqyFUHQYmvjj7XwGciWHAIwnSbQ7g4+yNB0Bgb8VZzuymArFAyTekYzcrxtKIi+FTu4KqxQiXDvQMrgvYMDhjrWuz2BroaJAV3iIZVDdfGmuF0dG36Zu6BP9AteinEki9OJoJjDmyQOMMFhC/2xhmVDHwwborIMPKZ5efnU7AZNVGNNsU8V0nFygqELJeKcmPDOsHsxYaNPTSTO1uZdyJ/6ky/sU+OPFOR6iBx8ozn13Ti6vVIYO155443N7RvVLc8JnCPmnAH2ntR3lZXlU2iY9hbM2kmgOZxRm4Ko6kyt7G5bEWQ8+UQZPqonPBmGV1WqdczrHsrC37bC+FCN1dimc138+bakKOOK/PS10jMA32pa/cEB2Mbf5dYQ8wwzI8/vry+TIfRzyPlv/GseDrj+3921Pg4FXx7vHQ/TvYs98t9rS9/R6mfX18qJwIqPY5U66QNnseP/+1A9dO/fiwxzR8ej2CnJ2F983b+3ljB9CWilyhz27qphm91nrT3Q91XgGA9faGh/vY8vH65G5YWzf3euyGT7KcJTf7t+VWMl+k7B9MTHs+NHmOmy+B5zvz64g7ATZFTf8Mp8ptXFZO1z2cd0+Hs9LDj5bf/Ahz7sxysJQAA -->
