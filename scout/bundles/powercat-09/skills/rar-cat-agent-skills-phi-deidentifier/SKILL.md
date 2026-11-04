---
name: "rar-cat-agent-skills-phi-deidentifier"
description: "Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/phi_deidentifier", "rar_sha256": "16e1403a1f0863adf1bb25718efd284fb7ff0d47691a8a8a03966fd450a14530", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["healthcare", "hls", "phi", "privacy", "redaction", "hipaa", "compliance", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `phi_deidentifier_agent.py` and embedded as the fenced Python below (sha256 16e1403a1f0863ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `phi_deidentifier_agent.py` first:

```bash
python3 phi_deidentifier_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 phi_deidentifier_agent.py   # or on stdin
python3 phi_deidentifier_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/phi_deidentifier_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/phi_deidentifier_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/phi_deidentifier/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
