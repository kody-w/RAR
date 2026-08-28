---
name: "rar-cowork-cookbook-weekly-external-customer-email-review"
description: "Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_external_customer_email_review", "rar_sha256": "dd29a3bde5d5effec8061353884ddf9b61e2c461d5cd8801745a270d9d6196b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/weekly_external_customer_email_review`. The original RAPP
agent is preserved byte-for-byte in `weekly_external_customer_email_review_agent.py` and in the RCI capsule.

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
