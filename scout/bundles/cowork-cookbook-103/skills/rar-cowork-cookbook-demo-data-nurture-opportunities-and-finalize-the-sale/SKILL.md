---
name: "rar-cowork-cookbook-demo-data-nurture-opportunities-and-finalize-the-sale"
description: "Generates and creates realistic demo records for nurture opportunities and finalize the sale in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "87e56af0ae4f7d11ccc3c2c2ec57a293f094beaf69853dc3ebac0e54dd26dd8e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale`. The original RAPP
agent is preserved byte-for-byte in `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` and in the RCI capsule.

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

Nurture opportunities and finalize the sale Demo Data Generator — Generates and creates realistic demo records for nurture opportunities and finalize the sale in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-nurture-opportunities-and-finalize-the-sale
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` and embedded as the fenced Python below (sha256 87e56af0ae4f7d11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` first:

```bash
python3 demo_data_nurture_opportunities_and_finalize_the_sale_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_nurture_opportunities_and_finalize_the_sale_agent.py   # or on stdin
python3 demo_data_nurture_opportunities_and_finalize_the_sale_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture opportunities and finalize the sale Demo Data Generator — Generates and creates realistic demo records for nurture opportunities and finalize the sale in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-nurture-opportunities-and-finalize-the-sale
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale',
    "version": '2.0.1',
    "display_name": 'Nurture opportunities and finalize the sale Demo Data Generator',
    "description": 'Generates and creates realistic demo records for nurture opportunities and finalize the sale in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-nurture-opportunities-and-finalize-the-sale',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-nurture-opportunities-and-finalize-the-sale',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c0cfe5a1d597d3cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-nurture-opportunities-and-finalize-the-sale', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataNurtureOpportunitiesAndFinalizeTheSale(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataNurtureOpportunitiesAndFinalizeTheSale'
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
    print(DemoDataNurtureOpportunitiesAndFinalizeTheSale().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
