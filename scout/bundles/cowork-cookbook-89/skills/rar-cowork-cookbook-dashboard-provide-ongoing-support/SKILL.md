---
name: "rar-cowork-cookbook-dashboard-provide-ongoing-support"
description: "Produces a self-contained interactive HTML dashboard for provide ongoing support - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_provide_ongoing_support", "rar_sha256": "ddcfaa336f90831c9a94877937723e5674d8eebf15b01e8f4165297f99bf7537", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_provide_ongoing_support_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-provide-ongoing-support:49af6a14dad6838c2cfa3d68071256755a8db9fe54366ffa420e25074e8a5089", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_provide_ongoing_support`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_provide_ongoing_support_agent.py` is
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
