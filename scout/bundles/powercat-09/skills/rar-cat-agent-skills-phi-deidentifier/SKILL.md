---
name: "rar-cat-agent-skills-phi-deidentifier"
description: "Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/phi_deidentifier", "rar_sha256": "71b910db638c5d408f058fbd63d0f7482e247e2dfdad6a3f4c1d73a4de70d1dd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["healthcare", "hls", "phi", "privacy", "redaction", "hipaa", "compliance", "scripts"]}
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
