---
name: "rar-cowork-cookbook-messaging-drift-audit-and-remediation"
description: "Audits every asset in a given folder against an approved messaging doc and brand guide, then returns a sortable Excel report of findings by severity with fixes, owners, and fix order."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/messaging_drift_audit_and_remediation", "rar_sha256": "703f96d0a26dd50221744ccb985db4a09c7aea0218b074f45c7e69a44131667e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "advanced", "read_only", "analysis"]}
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
