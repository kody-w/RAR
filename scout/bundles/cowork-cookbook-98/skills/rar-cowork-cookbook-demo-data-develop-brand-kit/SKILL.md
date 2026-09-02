---
name: "rar-cowork-cookbook-demo-data-develop-brand-kit"
description: "Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_brand_kit", "rar_sha256": "c1fbd4a35fb8d0ccfde5702a6ba8adb746eefeaea75df92831b76a090c455f76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_brand_kit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-brand-kit:eac7214268131c317586f35ec7c32d1c05304b09fc1af2c90cda4dfb0d40c961", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_brand_kit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_brand_kit_agent.py` is
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

Develop brand kit Demo Data Generator — Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-brand-kit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 c1fbd4a35fb8d0cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_brand_kit_agent.py` first:

```bash
python3 demo_data_develop_brand_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_brand_kit_agent.py   # or on stdin
python3 demo_data_develop_brand_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop brand kit Demo Data Generator — Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-brand-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_brand_kit',
    "version": '2.0.0',
    "display_name": 'Develop brand kit Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-brand-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-brand-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40d440249a059588',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-brand-kit'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-brand-kit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopBrandKit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopBrandKit'
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
    print(DemoDataDevelopBrandKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
