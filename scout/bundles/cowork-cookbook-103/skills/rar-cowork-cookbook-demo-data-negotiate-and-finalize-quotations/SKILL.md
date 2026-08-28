---
name: "rar-cowork-cookbook-demo-data-negotiate-and-finalize-quotations"
description: "Generates and creates realistic demo records for negotiate and finalize quotations in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_negotiate_and_finalize_quotations", "rar_sha256": "1719513173aab59033daa4496b51d8982afcf9efb22cc1682e338d99ce57b787", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 1719513173aab590…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_negotiate_and_finalize_quotations_agent.py` first:

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
    "version": '2.0.0',
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
