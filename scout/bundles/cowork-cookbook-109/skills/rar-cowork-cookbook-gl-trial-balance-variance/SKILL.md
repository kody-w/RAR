---
name: "rar-cowork-cookbook-gl-trial-balance-variance"
description: "Compares the current-period trial balance to the prior period and highlights GL accounts with material variances."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/gl_trial_balance_variance", "rar_sha256": "551e3f9e867735ac4ab2dff898356682733cdc32ac836dbf84a535ac49d887ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/gl_trial_balance_variance`. The original RAPP
agent is preserved byte-for-byte in `gl_trial_balance_variance_agent.py` and in the RCI capsule.

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
