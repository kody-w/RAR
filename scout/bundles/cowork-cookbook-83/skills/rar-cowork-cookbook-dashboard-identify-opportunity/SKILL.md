---
name: "rar-cowork-cookbook-dashboard-identify-opportunity"
description: "Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_opportunity", "rar_sha256": "166691be42768adaf91c0430a20d680fa144c1d998847c194a3c5547b24b3bd5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_opportunity`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_opportunity_agent.py` and in the RCI capsule.

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
