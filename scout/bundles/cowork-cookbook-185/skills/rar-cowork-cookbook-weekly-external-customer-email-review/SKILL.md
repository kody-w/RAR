---
name: "rar-cowork-cookbook-weekly-external-customer-email-review"
description: "Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_external_customer_email_review", "rar_sha256": "dd29a3bde5d5effec8061353884ddf9b61e2c461d5cd8801745a270d9d6196b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "weekly_external_customer_email_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/weekly-external-customer-email-review:7e93e3ae2e3575a184f164b8b63a183153d8d508e04f9acb91ee59103ac301a2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/weekly_external_customer_email_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `weekly_external_customer_email_review_agent.py` is
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

Weekly external customer email review — Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/weekly-external-customer-email-review
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `weekly_external_customer_email_review_agent.py` and embedded as the fenced Python below (sha256 dd29a3bde5d5effe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `weekly_external_customer_email_review_agent.py` first:

```bash
python3 weekly_external_customer_email_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 weekly_external_customer_email_review_agent.py   # or on stdin
python3 weekly_external_customer_email_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Weekly external customer email review — Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/weekly-external-customer-email-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/weekly_external_customer_email_review',
    "version": '2.0.0',
    "display_name": 'Weekly external customer email review',
    "description": 'Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'read_only', 'analysis'],
    "category": 'analysis',
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
        "upstream_slug": 'weekly-external-customer-email-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/weekly-external-customer-email-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f90ab884b7eefd5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/weekly-external-customer-email-review', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class WeeklyExternalCustomerEmailReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WeeklyExternalCustomerEmailReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(WeeklyExternalCustomerEmailReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
