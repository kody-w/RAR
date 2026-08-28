---
name: "rar-cowork-cookbook-dashboard-purge-and-archive-business-data"
description: "Produces a self-contained interactive HTML dashboard for purge and archive business data - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purge_and_archive_business_data", "rar_sha256": "85b59e79625b4aeba5f3010e6be87be6a30ca1a229bc03d1279abebc620cf620", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 85b59e79625b4aeb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purge_and_archive_business_data_agent.py` first:

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
    "version": '2.0.0',
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
