---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-certifications-and-compliance"
description: "Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance", "rar_sha256": "93fe72dbeec7ab8381dcbb09e66efbeafadc8a14ac13264dee8e3fdbc7eafbcb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_track_supplier_certifications_and_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-track-supplier-certifications-and-compliance:0c668f23d0e9e49fd0fd9b4bf75b12c521e2eada50462eeb399556a59ecd17ac", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` is
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

Track supplier certifications and compliance Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 93fe72dbeec7ab83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_certifications_and_compliance_agent.py` first:

```bash
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py   # or on stdin
python3 scheduled_brief_track_supplier_certifications_and_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier certifications and compliance Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_supplier_certifications_and_compliance',
    "version": '2.0.0',
    "display_name": 'Track supplier certifications and compliance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track supplier certifications and compliance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-certifications-and-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b671e8e5418187c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/track-supplier-certifications-and-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-track-supplier-certifications-and-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefTrackSupplierCertificationsAndCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackSupplierCertificationsAndCompliance'
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
    print(ScheduledBriefTrackSupplierCertificationsAndCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
