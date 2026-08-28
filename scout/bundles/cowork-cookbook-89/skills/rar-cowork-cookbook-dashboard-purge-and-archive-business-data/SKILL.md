---
name: "rar-cowork-cookbook-dashboard-purge-and-archive-business-data"
description: "Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purge_and_archive_business_data", "rar_sha256": "570ca5c8028242859b546c859610fbfd551fdb6789fe173d301427703a82cdf7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_purge_and_archive_business_data`. The original RAPP
agent is preserved byte-for-byte in `dashboard_purge_and_archive_business_data_agent.py` and in the RCI capsule.

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

Purge and archive business data Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 570ca5c802824285…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purge_and_archive_business_data_agent.py` first:

```bash
python3 dashboard_purge_and_archive_business_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_purge_and_archive_business_data_agent.py   # or on stdin
python3 dashboard_purge_and_archive_business_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purge and archive business data Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_purge_and_archive_business_data',
    "version": '2.0.1',
    "display_name": 'Purge and archive business data Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-purge-and-archive-business-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b14a47f062b51d68',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/purge-and-archive-business-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-purge-and-archive-business-data', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPurgeAndArchiveBusinessData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPurgeAndArchiveBusinessData'
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
    print(DashboardPurgeAndArchiveBusinessData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
