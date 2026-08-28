---
name: "rar-cowork-cookbook-dashboard-provide-ongoing-support"
description: "Produces a self-contained interactive HTML dashboard for provide ongoing support - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_provide_ongoing_support", "rar_sha256": "6c26cf2108a8d25a1cd0ceccd52d4a9785a10e117356be62dd6b9faa8e05039a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_provide_ongoing_support`. The original RAPP
agent is preserved byte-for-byte in `dashboard_provide_ongoing_support_agent.py` and in the RCI capsule.

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

Provide ongoing support Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for provide ongoing support - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-provide-ongoing-support
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 6c26cf2108a8d25a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_provide_ongoing_support_agent.py` first:

```bash
python3 dashboard_provide_ongoing_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_provide_ongoing_support_agent.py   # or on stdin
python3 dashboard_provide_ongoing_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide ongoing support Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for provide ongoing support - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-provide-ongoing-support
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_provide_ongoing_support',
    "version": '2.0.1',
    "display_name": 'Provide ongoing support Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for provide ongoing support - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-provide-ongoing-support',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-provide-ongoing-support',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e072985b4b639ef1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/provide-ongoing-support'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-provide-ongoing-support', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardProvideOngoingSupport(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardProvideOngoingSupport'
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
    print(DashboardProvideOngoingSupport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
