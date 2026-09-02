---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-portfolio"
description: "Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_portfolio", "rar_sha256": "59898f0f6265c9de6bbb77a4293ed81fceb0f1ed511b0960e8639048e5da76cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_product_portfolio_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-product-portfolio:cc5f43e94129c97286de39e372d6e9c0cce44c450fd1c2b3da6fc9425313b2ce", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_product_portfolio`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_product_portfolio_agent.py` is
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

Develop product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 59898f0f6265c9de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_portfolio_agent.py` first:

```bash
python3 scheduled_brief_develop_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_product_portfolio_agent.py   # or on stdin
python3 scheduled_brief_develop_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product portfolio Scheduled Email Brief — Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_product_portfolio',
    "version": '2.0.0',
    "display_name": 'Develop product portfolio Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-develop-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07f780d065d8bf55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-portfolio'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-develop-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDevelopProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProductPortfolio'
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
    print(ScheduledBriefDevelopProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
