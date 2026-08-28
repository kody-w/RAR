---
name: "rar-cowork-cookbook-dashboard-provide-ongoing-support"
description: "Produces a self-contained interactive HTML dashboard for provide ongoing support - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_provide_ongoing_support", "rar_sha256": "ddcfaa336f90831c9a94877937723e5674d8eebf15b01e8f4165297f99bf7537", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 ddcfaa336f90831c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_provide_ongoing_support_agent.py` first:

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
    "version": '2.0.0',
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
