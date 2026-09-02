---
name: "rar-cowork-cookbook-demo-data-negotiate-and-finalize-quotations"
description: "Generates and creates realistic demo records for negotiate and finalize quotations in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_negotiate_and_finalize_quotations", "rar_sha256": "1719513173aab59033daa4496b51d8982afcf9efb22cc1682e338d99ce57b787", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_negotiate_and_finalize_quotations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-negotiate-and-finalize-quotations:4149dd6843a469a9cc34f24800ebedb04dbd81a2423c7142236bcb56b05e503e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_negotiate_and_finalize_quotations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_negotiate_and_finalize_quotations_agent.py` is
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
