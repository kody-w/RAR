---
name: "rar-cowork-cookbook-demo-data-nurture-opportunities-and-finalize-the-sale"
description: "Generates and creates realistic demo records for nurture opportunities and finalize the sale in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "67e2728ba828faa4a78e8d37df7bd35acb789020b038d075bc61918e330116f9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_nurture_opportunities_and_finalize_the_sale_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-nurture-opportunities-and-finalize-the-sale:75120b1c5d9b6860772d1d0db67d6b24a40c43c73fb1e6267ce05c2052a21ce5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` is
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
