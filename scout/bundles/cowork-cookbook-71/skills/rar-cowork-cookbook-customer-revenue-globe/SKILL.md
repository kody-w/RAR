---
name: "rar-cowork-cookbook-customer-revenue-globe"
description: "Builds an interactive 3D globe HTML visualization plotting customer locations sized by trailing-12-month revenue."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_revenue_globe", "rar_sha256": "0e52328a49528e4ac340a5af212a7355325f55afedd6c9344ffb5b5c73d44dd1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_revenue_globe_agent.py` and embedded as the fenced Python below (sha256 0e52328a49528e4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_revenue_globe_agent.py` first:

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
    "version": '2.0.0',
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
