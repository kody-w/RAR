---
name: "rar-cowork-cookbook-customer-revenue-globe"
description: "Builds an interactive 3D globe HTML visualization plotting customer locations sized by trailing-12-month revenue."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_revenue_globe", "rar_sha256": "abca6750385d896c1613aad5415818a74f380f196990d46a3c0856872ec97ad4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_revenue_globe`. The original RAPP
agent is preserved byte-for-byte in `customer_revenue_globe_agent.py` and in the RCI capsule.

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

Customer Revenue 3D Globe Visualization — Builds an interactive 3D globe HTML visualization plotting customer locations sized by trailing-12-month revenue.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-revenue-globe
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_revenue_globe_agent.py` and embedded as the fenced Python below (sha256 abca6750385d896c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_revenue_globe_agent.py` first:

```bash
python3 customer_revenue_globe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_revenue_globe_agent.py   # or on stdin
python3 customer_revenue_globe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Revenue 3D Globe Visualization — Builds an interactive 3D globe HTML visualization plotting customer locations sized by trailing-12-month revenue.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-revenue-globe
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_revenue_globe',
    "version": '2.0.1',
    "display_name": 'Customer Revenue 3D Globe Visualization',
    "description": 'Builds an interactive 3D globe HTML visualization plotting customer locations sized by trailing-12-month revenue.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'customer-revenue-globe',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-revenue-globe',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c9f1bdc62b7fbdb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/customer-revenue-globe', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class CustomerRevenueGlobe(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerRevenueGlobe'
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
    print(CustomerRevenueGlobe().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
