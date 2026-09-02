---
name: "rar-cowork-cookbook-demo-data-analyze-sourcing-effectiveness"
description: "Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sourcing_effectiveness", "rar_sha256": "93e83209aa747caad617eaaf6f7c79606d4dc21ea1be4eab757056ced153413f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_sourcing_effectiveness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-sourcing-effectiveness:8bc59a8cc2bc1b922e85db9074a83c309e16d579fb232236ff774e2f15d1264d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_sourcing_effectiveness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_sourcing_effectiveness_agent.py` is
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

Analyze sourcing effectiveness Demo Data Generator — Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 93e83209aa747caa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sourcing_effectiveness_agent.py` first:

```bash
python3 demo_data_analyze_sourcing_effectiveness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_sourcing_effectiveness_agent.py   # or on stdin
python3 demo_data_analyze_sourcing_effectiveness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing effectiveness Demo Data Generator — Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_sourcing_effectiveness',
    "version": '2.0.0',
    "display_name": 'Analyze sourcing effectiveness Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-sourcing-effectiveness',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52a2823dd0d5985b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-sourcing-effectiveness'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-analyze-sourcing-effectiveness', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeSourcingEffectiveness(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeSourcingEffectiveness'
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
    print(DemoDataAnalyzeSourcingEffectiveness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
