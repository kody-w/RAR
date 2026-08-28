---
name: "rar-cowork-cookbook-demo-data-develop-brand-kit"
description: "Generates and creates realistic demo records for develop brand kit in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_brand_kit", "rar_sha256": "c1fbd4a35fb8d0ccfde5702a6ba8adb746eefeaea75df92831b76a090c455f76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_brand_kit`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_brand_kit_agent.py` and in the RCI capsule.

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
