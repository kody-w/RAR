---
name: "rar-cowork-cookbook-customer-revenue-globe"
description: "Builds an interactive 3D globe HTML visualization plotting customer locations sized by trailing-12-month revenue."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_revenue_globe", "rar_sha256": "0e52328a49528e4ac340a5af212a7355325f55afedd6c9344ffb5b5c73d44dd1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "customer_revenue_globe_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/customer-revenue-globe:0b818c4523529cff1b4d7b8b18790a2264a08f08b2e7a61ea521e48cacb2a1e8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/customer_revenue_globe`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `customer_revenue_globe_agent.py` is
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
