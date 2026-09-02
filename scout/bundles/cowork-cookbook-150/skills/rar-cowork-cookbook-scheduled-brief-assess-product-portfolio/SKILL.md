---
name: "rar-cowork-cookbook-scheduled-brief-assess-product-portfolio"
description: "Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_assess_product_portfolio", "rar_sha256": "1efab3ca9c5ce687ad4eac577122e12a7a1ddccf8b067776bfd556fc695c618a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_assess_product_portfolio_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-assess-product-portfolio:2a21113d01127198ec81c8183a980ec3e0a43cbf1f2449e300378aa681dc16ae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_assess_product_portfolio`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_assess_product_portfolio_agent.py` is
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

Assess product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 1efab3ca9c5ce687…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_assess_product_portfolio_agent.py` first:

```bash
python3 scheduled_brief_assess_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_assess_product_portfolio_agent.py   # or on stdin
python3 scheduled_brief_assess_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_assess_product_portfolio',
    "version": '2.0.0',
    "display_name": 'Assess product portfolio Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing assess product portfolio for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-assess-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-assess-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e206d618375e136',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/assess-product-portfolio'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-assess-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAssessProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAssessProductPortfolio'
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
    print(ScheduledBriefAssessProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
