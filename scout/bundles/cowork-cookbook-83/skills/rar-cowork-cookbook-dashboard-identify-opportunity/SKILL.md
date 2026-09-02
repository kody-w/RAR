---
name: "rar-cowork-cookbook-dashboard-identify-opportunity"
description: "Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_opportunity", "rar_sha256": "166691be42768adaf91c0430a20d680fa144c1d998847c194a3c5547b24b3bd5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_identify_opportunity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-identify-opportunity:6da76d2f59d7f0b24c453cc68b2de139f1b76fce34f6f57b78250a7277c9294e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_identify_opportunity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_identify_opportunity_agent.py` is
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

Identify opportunity Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-opportunity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 166691be42768ada…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_opportunity_agent.py` first:

```bash
python3 dashboard_identify_opportunity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_opportunity_agent.py   # or on stdin
python3 dashboard_identify_opportunity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify opportunity Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-opportunity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_opportunity',
    "version": '2.0.0',
    "display_name": 'Identify opportunity Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-opportunity',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-opportunity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31e761787878f3dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/identify-opportunity'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-identify-opportunity', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardIdentifyOpportunity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyOpportunity'
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
    print(DashboardIdentifyOpportunity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
