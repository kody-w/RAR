---
name: "rar-cowork-cookbook-demo-data-monitor-product-performance"
description: "Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_product_performance", "rar_sha256": "66b500afd2579c6cd0cb3f9224daa00a19dcb08fc172eea1261f2b5fef1b26ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_monitor_product_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-monitor-product-performance:a26877183dee548a997a59119c5fc00abedb22adc2a9664176ac86924d5a2173", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_monitor_product_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_monitor_product_performance_agent.py` is
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

<!-- rci-capsule:v1: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 -->
