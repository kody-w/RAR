---
name: "rar-cowork-cookbook-messaging-drift-audit-and-remediation"
description: "Audits every asset in a given folder against an approved messaging doc and brand guide, then returns a sortable Excel report of findings by severity with fixes, owners, and fix order."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/messaging_drift_audit_and_remediation", "rar_sha256": "703f96d0a26dd50221744ccb985db4a09c7aea0218b074f45c7e69a44131667e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "advanced", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/messaging_drift_audit_and_remediation`. The original RAPP
agent is preserved byte-for-byte in `messaging_drift_audit_and_remediation_agent.py` and in the RCI capsule.

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

Messaging drift audit and remediation routing — Audits every asset in a given folder against an approved messaging doc and brand guide, then returns a sortable Excel report of findings by severity with fixes, owners, and fix order.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/messaging-drift-audit-and-remediation
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
    "brand_guide": {
      "description": "The brand guidelines document used for tone and naming checks.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "folder": {
      "description": "The folder containing the assets to review.",
      "type": "string"
    },
    "messaging_doc": {
      "description": "The approved messaging document to benchmark assets against.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `messaging_drift_audit_and_remediation_agent.py` and embedded as the fenced Python below (sha256 703f96d0a26dd502…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `messaging_drift_audit_and_remediation_agent.py` first:

```bash
python3 messaging_drift_audit_and_remediation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 messaging_drift_audit_and_remediation_agent.py   # or on stdin
python3 messaging_drift_audit_and_remediation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Messaging drift audit and remediation routing — Audits every asset in a given folder against an approved messaging doc and brand guide, then returns a sortable Excel report of findings by severity with fixes, owners, and fix order.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/messaging-drift-audit-and-remediation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/messaging_drift_audit_and_remediation',
    "version": '3.0.3',
    "display_name": 'Messaging drift audit and remediation routing',
    "description": 'Audits every asset in a given folder against an approved messaging doc and brand guide, then returns a sortable Excel report of findings by severity with fixes, owners, and fix order.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'advanced', 'read_only', 'analysis'],
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
        "upstream_slug": 'messaging-drift-audit-and-remediation',
        "upstream_url": 'https://coworkcookbook.com/recipes/messaging-drift-audit-and-remediation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b5f767bc9591547',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/messaging-drift-audit-and-remediation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A sortable Excel audit report flagging every inconsistency by severity, recommended fix, and the right owner - so cleanup happens in priority order.'], 'confidence': 1.0, 'deliverable': 'A sortable Excel audit report flagging every inconsistency by severity, recommended fix, and the right owner - so cleanup happens in priority order.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'brand_guide': 'The brand guidelines document used for tone and naming checks.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'folder': 'The folder containing the assets to review.', 'messaging_doc': 'The approved messaging document to benchmark assets against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Catch messaging drift across every asset in [Folder] before it shows up in market. A sortable Excel audit report flagging every inconsistency by severity, recommended fix, and the right owner - so cleanup happens in priority order.', 'expected_output': 'A sortable Excel audit report flagging every inconsistency by severity, recommended fix, and the right owner - so cleanup happens in priority order.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Run a messaging drift audit across every asset in [Folder]. Read each one in full and benchmark it against the approved messaging in [Messaging doc] and the brand guidelines in [Brand guide].\n\nCategorize by severity:\n\nCritical - off-message claims, wrong product naming\n\nMajor - drifted positioning, outdated value props\n\nMinor - tone, formatting\n\nFor each finding:\n\nCapture the issue, the business impact, and a specific recommended fix\n\nMap the finding to an owner using file ownership metadata or the latest editor\n\nBring it all together in a sortable Excel report - total assets reviewed, findings by severity, the most common drift patterns, an owner-routed fix list, and the recommended order to address. Route each finding to its owner through the report.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A sortable Excel audit report flagging every inconsistency by severity, recommended fix, and the right owner - so cleanup happens in priority order.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits every asset in a given folder against an approved messaging doc and brand guide, then returns a sortable Excel report of findings by severity with fixes, owners, and fix order.', 'example_request': 'Run a messaging drift audit on the Q3 Campaign folder against our messaging doc and brand guide.', 'inputs': [{'description': 'The folder containing the assets to review.', 'name': 'folder'}, {'description': 'The approved messaging document to benchmark assets against.', 'name': 'messaging_doc'}, {'description': 'The brand guidelines document used for tone and naming checks.', 'name': 'brand_guide'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check a folder of marketing or content assets for messaging and brand drift before it reaches market.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class MessagingDriftAuditAndRemediation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MessagingDriftAuditAndRemediation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'brand_guide': {'description': 'The brand guidelines document used for tone and naming checks.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'folder': {'description': 'The folder containing the assets to review.', 'type': 'string'}, 'messaging_doc': {'description': 'The approved messaging document to benchmark assets against.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(MessagingDriftAuditAndRemediation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
