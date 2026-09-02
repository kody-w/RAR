---
name: "rar-cowork-cookbook-gl-trial-balance-variance"
description: "Compares the current-period trial balance to the prior period and highlights GL accounts with material variances."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/gl_trial_balance_variance", "rar_sha256": "551e3f9e867735ac4ab2dff898356682733cdc32ac836dbf84a535ac49d887ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "gl_trial_balance_variance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/gl-trial-balance-variance:cb1c3945be812cff7a02b03371cadc2c18ed919d1144931acc95c2c23019d5d8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/gl_trial_balance_variance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `gl_trial_balance_variance_agent.py` is
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

GL Trial Balance Variance Report — Compares the current-period trial balance to the prior period and highlights GL accounts with material variances.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/gl-trial-balance-variance
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gl_trial_balance_variance_agent.py` and embedded as the fenced Python below (sha256 551e3f9e867735ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gl_trial_balance_variance_agent.py` first:

```bash
python3 gl_trial_balance_variance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 gl_trial_balance_variance_agent.py   # or on stdin
python3 gl_trial_balance_variance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
GL Trial Balance Variance Report — Compares the current-period trial balance to the prior period and highlights GL accounts with material variances.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/gl-trial-balance-variance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/gl_trial_balance_variance',
    "version": '2.0.0',
    "display_name": 'GL Trial Balance Variance Report',
    "description": 'Compares the current-period trial balance to the prior period and highlights GL accounts with material variances.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'gl-trial-balance-variance',
        "upstream_url": 'https://coworkcookbook.com/recipes/gl-trial-balance-variance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b20b898873061ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/gl-trial-balance-variance', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class GlTrialBalanceVariance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GlTrialBalanceVariance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(GlTrialBalanceVariance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
