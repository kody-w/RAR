---
name: "rar-cowork-cookbook-weekly-external-customer-email-review"
description: "Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_external_customer_email_review", "rar_sha256": "5373398169c59c6aee6a9e1bf089f3da08027f70be046073178e6c64f43ae64d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "read_only", "analysis"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `weekly_external_customer_email_review_agent.py` and embedded as the fenced Python below (sha256 5373398169c59c6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `weekly_external_customer_email_review_agent.py` first:

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
    "version": '2.0.1',
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
