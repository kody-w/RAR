---
name: "rar-cowork-cookbook-demo-data-analyze-sales-data"
description: "Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sales_data", "rar_sha256": "9a96e1894351c860ebefaa9baaa12214bc8320bf256f35baaf40b63010ec613c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_sales_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-sales-data:d0edc67bbc32500c19ab2a1a0ea050c9c2788dd7946cfd400d767f24a4fd56a2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_sales_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_sales_data_agent.py` is
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

Analyze sales data Demo Data Generator — Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sales-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 9a96e1894351c860…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sales_data_agent.py` first:

```bash
python3 demo_data_analyze_sales_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_sales_data_agent.py   # or on stdin
python3 demo_data_analyze_sales_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sales data Demo Data Generator — Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sales-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_sales_data',
    "version": '2.0.0',
    "display_name": 'Analyze sales data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-sales-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-sales-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c593819c483bcb7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-analyze-sales-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAnalyzeSalesData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeSalesData'
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
    print(DemoDataAnalyzeSalesData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
