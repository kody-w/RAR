---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-portfolio"
description: "Schedulable morning-brief email summarizing develop product portfolio for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_portfolio", "rar_sha256": "59898f0f6265c9de6bbb77a4293ed81fceb0f1ed511b0960e8639048e5da76cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_product_portfolio_agent.py` and in the RCI capsule.

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
