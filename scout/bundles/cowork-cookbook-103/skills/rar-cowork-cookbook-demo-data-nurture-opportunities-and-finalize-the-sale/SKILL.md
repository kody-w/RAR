---
name: "rar-cowork-cookbook-demo-data-nurture-opportunities-and-finalize-the-sale"
description: "Generates and creates realistic demo records for nurture opportunities and finalize the sale in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "67e2728ba828faa4a78e8d37df7bd35acb789020b038d075bc61918e330116f9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` and embedded as the fenced Python below (sha256 67e2728ba828faa4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` first:

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
    "version": '2.0.0',
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
