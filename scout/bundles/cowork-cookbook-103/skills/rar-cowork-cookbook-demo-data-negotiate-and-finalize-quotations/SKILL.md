---
name: "rar-cowork-cookbook-demo-data-negotiate-and-finalize-quotations"
description: "Generates and creates realistic demo records for negotiate and finalize quotations in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_negotiate_and_finalize_quotations", "rar_sha256": "e60b3530a67142a6d3ad040d796d5db0bf310c79439979fb0f102692963c46f9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_negotiate_and_finalize_quotations`. The original RAPP
agent is preserved byte-for-byte in `demo_data_negotiate_and_finalize_quotations_agent.py` and in the RCI capsule.

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

Negotiate and finalize quotations Demo Data Generator — Generates and creates realistic demo records for negotiate and finalize quotations in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 e60b3530a67142a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_negotiate_and_finalize_quotations_agent.py` first:

```bash
python3 demo_data_negotiate_and_finalize_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_negotiate_and_finalize_quotations_agent.py   # or on stdin
python3 demo_data_negotiate_and_finalize_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate and finalize quotations Demo Data Generator — Generates and creates realistic demo records for negotiate and finalize quotations in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_negotiate_and_finalize_quotations',
    "version": '2.0.1',
    "display_name": 'Negotiate and finalize quotations Demo Data Generator',
    "description": 'Generates and creates realistic demo records for negotiate and finalize quotations in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-negotiate-and-finalize-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '603b34782b7b8a60',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/negotiate-and-finalize-quotations'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-negotiate-and-finalize-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataNegotiateAndFinalizeQuotations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataNegotiateAndFinalizeQuotations'
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
    print(DemoDataNegotiateAndFinalizeQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
