---
name: "rar-cat-agent-skills-phi-deidentifier"
description: "Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/phi_deidentifier", "rar_sha256": "71b910db638c5d408f058fbd63d0f7482e247e2dfdad6a3f4c1d73a4de70d1dd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["healthcare", "hls", "phi", "privacy", "redaction", "hipaa", "compliance", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/phi_deidentifier`. The original RAPP
agent is preserved byte-for-byte in `phi_deidentifier_agent.py` and in the RCI capsule.

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

PHI De-identifier — Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#phi-deidentifier
  Upstream author: Rafael Lopez Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `phi_deidentifier_agent.py` and embedded as the fenced Python below (sha256 71b910db638c5d40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `phi_deidentifier_agent.py` first:

```bash
python3 phi_deidentifier_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 phi_deidentifier_agent.py   # or on stdin
python3 phi_deidentifier_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PHI De-identifier — Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#phi-deidentifier
  Upstream author: Rafael Lopez Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/phi_deidentifier',
    "version": '3.0.2',
    "display_name": 'PHI De-identifier',
    "description": 'Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.',
    "author": 'Rafael Lopez Alcaraz',
    "tags": ['healthcare', 'hls', 'phi', 'privacy', 'redaction', 'hipaa', 'compliance', 'scripts'],
    "category": 'devtools',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'phi-deidentifier',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#phi-deidentifier',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4c6bd1961fad5f45',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PhiDeidentifier(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PhiDeidentifier'
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
    print(PhiDeidentifier().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
