---
name: "rar-cat-agent-skills-content-quality-auditor"
description: "Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/content_quality_auditor", "rar_sha256": "d8b1870486fa4ca8f04150a70925851ae31980f7535850af3297aa10318d464f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["content", "quality", "audit", "documents", "productivity", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/content_quality_auditor`. The original RAPP
agent is preserved byte-for-byte in `content_quality_auditor_agent.py` and in the RCI capsule.

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

Content Quality Auditor — Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#content-quality-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `content_quality_auditor_agent.py` and embedded as the fenced Python below (sha256 d8b1870486fa4ca8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `content_quality_auditor_agent.py` first:

```bash
python3 content_quality_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 content_quality_auditor_agent.py   # or on stdin
python3 content_quality_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Content Quality Auditor — Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#content-quality-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/content_quality_auditor',
    "version": '2.1.2',
    "display_name": 'Content Quality Auditor',
    "description": 'Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.',
    "author": 'Simon Owen',
    "tags": ['content', 'quality', 'audit', 'documents', 'productivity', 'governance'],
    "category": 'productivity',
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
        "upstream_slug": 'content-quality-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#content-quality-auditor',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b2eca5049c1ef246',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.636, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'tag:governance', 'tag:quality', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class ContentQualityAuditor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ContentQualityAuditor'
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
    print(ContentQualityAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716a5OiWLruX2HnfOjqbVZyk1tNTMQBVFQEFQTBro5q7iBXuUPv/u97oWZW957umX0iThwrI1Nlrff+Ps+7oH59sZo6zMuXLy9qlOYZtO+87OX1xfUqp4yKOsqz6ZKTlx7k5k6TelldvUKFFXjTn7yaPuUlZJW151tODSWRXVpl5FWQFVhRVtWQBTl55kdBU1p24kG3xkqieoDKxi4jB7IyFyo9J0+BZBfyo96r3oB+r7fSIvGqly8//fz6EoH3L19+fXESqwJfvfB5VgNDjg9RbONGNXDh9SWxsgBcLgbg0uRF4ZV+XqbgK9fzoeenT5WX+K/Qf/5n3FllUP345WsGPV9fX6Z/SpNBdehBdW5VtedCjlVYdjRpeoPYpLOGClhcN2UGfISquoyy4O2x87ukvID+MV379FDyFnj1p68vOTDBmmL69eXHKWpfX8pmev82SSk+/fiW5J1Xfvrxu5yqsa8eCCsQBqx++/b8/BQLFn5fGvnQN/Ww5J+6QFCjwgPCf+ff9HqY/hT3DMm3x+JPefEK/bnkyZ9/AHsfdWEDuX8uFsQA7Hx5u+ZR9umpo8xbL7Myx/v041+JdULPiZOoqv9Xcn96CA49ywXReobkx9d7+n6GZk/fPmT+tdoCFMz/jSdg+bu6j0D9lex7Zv+H6CTKQGO85/JPxf3Zhtk/oJ/+0rd/teEV8r++LLwkar17832Bfr2XyE8/uN+//OHn34DofytGzZvSuUv4llpZ5HtV/e3bTz9U969/+PmnH5oCVLFnpd+aMvkzmX8W17ueP0TwuerTH/cC/VoWZ3mXQR89BP2aF/9R/vYG6QAF3O/fV1+g33fi9JpBkxPvSh8h+F03VsDW38Xxx5ffAOQA6Cob534Z4Mff/gZJkVPmVe7XEIDDpgYAltVR6k3Gn8KogsDPhBqlB+JaRRPUPdaB+p8yPFmc+9Av/8ex6s8APrP6cxVHSVLBzgPNvj2R8Zv1wLNf3qATkJeXURBlVgIp7OHwNbvvnHQVpVd5ZQvwyR5q7zNo48/TGyjKoF/+QuK3++a3YvjlDrvRA+YUfjNBXNUk3tvkzDn0sqfpjpVBXu85DZCb5A4wwo+SCfiB7jxpAUROjt/dgNwIgAhQMjwgvcm+TMJ++eUX26rCr9kDk3HoQSsVDBZ8mAN9/gy88ZMoCOuvmeeEOfTDr7/9AP0X9K923YVPOg6AFJ6hBxZu1b0M6Ch4UBU05RHgxD30v/72jCkQk3klBBIV+RNVTZtBKcae+x5gdc1+xggSsj1/oj5AQHlZA6CHovoN2vjQh71A6XRpooIQsCHkegUgMi9zBiDVAu58RDLLa6gC9Vb5wyvUVN5d6y+ALe8mpqCnrfoXSOIPgHjyBPyazLwvApvzLALh/0j/43sgpPyhgrh3EW+QPBUfYOfSKsLSeuqYeHnKy0TTz+1AuAVlXvc1m6jVm0J174RHeMAib+LmR0o/TzmHJoYGia3edd/XWBM9nu40WX7NqmeVW6V3p3RgygAFTeRO2P/3Z0lVYd4k7j1+wNJJ0jML7jMr9xp8Ejz0ZHjoSfHQ1wZD0Dn0/3kemSxiBUFZCuxpuYCW8kkxH5F6Nhr0GKImMaBcHl3xfWp4R4Z3gPyaPYwa/v5YeY/vc80DdJoShENhlbt8YDWI1CT3XntTLZUPh75m70j8Cry6ww4IP2hUUMhT/bwrfH34fLc0BN04ff7Oynd3S3fyHNQXVDR2AuLge55rW04MrCqn/nlGHhSiN/VSF0ZO+AevICAd5BvIh4AREegIgNb30Mk5cBO0jl/m6ffl0TRFASvcxgHWhl7pvUFn0AJTGVSg78AoNK0BUfjhLgpKPRBjYOJHhKvQKh7G5GX8bqA1AXDkdb+P//PS95K9WzIZD2RarlWDSHYTcrpe/8jrh5XPTAGh6VQ9901/TPbTU+j3hPH3r9ndwg+wBr2b3Kvte2gg0DNpda+3CXoqAB+p9ywfUAd3Wn17MOODej9s+QLx7AliHzh1pxDoU/pOTnce0/6Yky9QWNdF9QWGP5a9BVEdNvZblMP/xEd/e9bK52drfH7Sxx8kP4LwBfp+avjD5WcxfoGQN/QNmS7tIsebqu35+gI12Ufnf/rd+2ey7snw3FeAUhOkgVKZ6rIKPfc+Lije92wCU/IUwNcU5AGw4QdbvC8BlBGUXjAtfrBHNZFOB3juLhvE+2v2kfFnNwA0zu6YUuW/69I7bYL8PdLzgergUlYD3e40UwXedIBJJncr7+VL1iTJ60tmpd6/OLhMiA1qEQRtOuaArgCjSR1590/AGXAhsqb3fzyW7e9vrORRs1UNrLPKe+c/e+AJea/TXJoB1JhOFxMtPSAcnImsJqkna+uhmMx7HGam8edjNvpnrfcmBTrc/MvUqwB1wRz7Cn2MpK/Q+yHhfpDLGnD++mkahyc/wVLw52Ptx0nT9l5+/hMzntPxXxgRTTgxIcvD3e/FYz2yVVg1wDpN2b1+cMXEDdVwJ8t/dhsoLL1bA1jPnUz+HoPvpuUPe367u1I/Dpe/vrzDyDN5z3EPLAf9+rmaeA8GXQAUgs+PCgTX/teD4HMfgDswkUxnWdpGaQqZ06RvzR2L9pE5SiAWhTAYQROo5eEoQyM+ReDgI2L5OMZQloUiOEq7c3LuA3mP+v020Vw02UIwlI8wDObPUQxxQWFgc9elSZp0CApDLMa2CJtgLPv71hg06NPBh0NT9D5m0ikQTz9/fbHJOVi5nlcb9vHiYUa34Dlly+FuZiAwp8GzDjduqGURxnw77nK3infHHYLVXWoba1OI5jVyrrGLFieFcZb645aJFkSYzdSZoIvDVmovJ2PD1EvjWKv6sN92Po73i30wLubL1EvUvOxtuky9YtjS5E3ZesTShhn6Vs8FzxUiVT3cOkzAxDgnxHN0oNLE7oPkZCVnKSJWt8IVhBtWxVtXvVCmplUKUdeikVzWO32T+q3Rn3Ymtg+dTjV11bEHlliqLXOu45yXyBl82NHYxc1KYs6snNnMz4xZhkT0OWrUbijFWzJmYa5W1Vol0MReVgW3G81dXzqn4FbyiWZsTvsNil2ZkU1Mc+8HgaCvVxfhct7QlDyugpmenIW+yccl3Yv81a3laitcjCixT6VwtbBzNV73CtEu9UvhEhUzatTFR41lQxXNbDVYjL4tZZPWL/KxrPb0rreK64JTb0kselJJssctr1f0MEoJXRhmmZ1pqunXx93uEp87jjPU7YGppG1bkT1MDiq1HGZnExYWFco3VaYfOwalb7m6HuAkMqQMTXtdSGfFaW3CebCKTIy3L/tAsnp3oLdFXFSlHqP8vNTPGCgT0k+ToEni6KybnLu5dOkxUvukMn2p0qyZu+7buhWqwFnu+y7bk2NrUMte2RJ8Z+KnuXhe7JcbYZTamDktbhhz0NRilC6DI2pkQ22j7DzTrr09P1iMVArsuNGpoUcsJTXCgYlvTuWphj4WcqmErSv0Q0rCIu9cYAw2+JM47qqSHxFGTvW1Wgz4Gb2ulZlQtUO40+hKHUuGlXxBdWa8RsYqJWLmzodTIypk5nqQ0UavXZjsts2WY9Zr5LinZ1q5joLdDh6dk26avXczwhBflxKebgyLV29OoGWJHGjswqq1PD0afMME5HLRJkIChuCmP+wym+8RTS9Osyrk8YSw3GOy0KlukaIaxfHVEKdCbB6E4UTFc8qQhIVS4VWxpMMFMe7iZVkNQ8sdzyW1UdXBseYRFd5CdrNSu7N7nDerRuwbNsl7UpDRLvId/sJv5i0v+J3WB2lGZUgqd0WrELTbSDJlzgSm8heecEi3eG0izCBUsM3NsjS0i7WI31jNPzpE2qx3Z5rczUY0tKzZmo9CPWdv9Uyni100OsYGmx0RXZVa4UoOghUu5rjKSGdQq2kLW+HO3PZhzLVyq3emscLTS+yVbu5RDGW4Koluqp6fx/4qgxkyz4a6TlZYTm1LJB2d887muHCBSkcaXoz0dSyQunC9kZd8ZXHo2VZoBrnfzNCul+SYcOAuPm5UXTKvJxQ9uuaKUqW9dVTzFWVxu0OUa8hVOqSzrgPIkV+FWZBGhTa449mLkc25F+NNkRCb/Xne42IzcNguLQa+YvxUA6Uxg53Z5pzqpDzbbOg9N1o9Zu7HwBJ09ZyBtltdzkhfV3NdviH12e6vMdd49DDb+K2E8KWqpIPQHdQgpnZuXVyJ44LtbXQ/H+njzcKoS9ioWyEnNEkfKJqZ7U8t7bg3xudPJwpnsTGPbscNf0AKLZ8jrthgCbc/cpqjGVh9HbZLMnEtoyKQ22WtarPlYmhNfHsRnC2eKWu5Eso0Dw9wnZxSDbSXQAjJTkuN1EX4PJZnC7vTR0S73Ybe8/BsE+odPRwbl81DP7ly9S6m+mDfwqK+5m7BkGVFON+UuksMcb1Rcd4QLt7y2shkJXpnHtNB2ao7XutiGS8YZEhSvW9PWHmKd+GccvdJpfiLZLUXjqJXbkFxwceIs3MpCPbHC49xwjyodX6wlnioEqJjZMzmetqu+NZEz9o8YdgbqnIajik6mg0jF2mXrR23O8GXhJrf6KBd9Gt+EiXyaqGiDrNqlS2sSlxs/WhkFESKhHylKhm9NxjzJFlcqMXrYHO7SoWlq63qhkhvLo50NqP44uBGvq1R9tAFCG7XjbLnpFnN7TcscymcxZhF27JlauGoRKycpOxKGNfe5tqsdsvmmvSaXgcZzxWb8w6laQ/fKE2zDmFuSRtqPYtTLycYBJ3dxtMS/Gxtec8fVFrqN21iiFLcojyh7G+Si6+SbR47TL9mzzUHC2y8cPk5zum3cNcj5VaPQn5tXaNIy9LVYU/mC/6Y7lwtW61aTbPGHgYYs16shLZRyuzI76qVquvhcpZjlWAmrIC5orq93Ejpst2KabGfCWXEh4sNdUpiaw5rLLI8hr1aKdsbBc5655sgp5y9W+a+dLoVt5GLy1zSAthaWjHar/zLTK14Xt5m7sZm9RWro/ZWVDHAypJgiVtV38/p1Zkc92fUdwKJQ3gBqWp6ZUZWyKJXbl6OJ10vd5dgdj21OCGG+ixRpOPGqyLA+wbX7BKWrXBrNgza3oplNTfp8ojiVot6J2QlF8nVTCkeS92qrhWviXjxiiS7gWlFni3azQGv5PFYn+KVkl5P8Ha77NVUmNcrb5bGy0tjSZTMszOFXZUqVxKhHF1O6JxifTSOFrbbt6XR+0J1A9VIRN7oS7dmFTgANNbHrUjJaZ2UM27nKfqeLOW1rrdro73U9CjpSH7ZpAItt2NJmjKrnvgL7ndEZFq4Ni/2KUtV+zK5ptKZSffYxdcSZn2mOBSz5csgtaWaJzismim8ybBTytAS1um31QKnqoyrWLxDKYmK8mVCn+SDsGPblGZLOK53/I1ZVEuAEeh1MCJ6R2mHusAjdp5K7TE+xB47w47hgd12l5G8KBVcztdLOedjFHGZzUGqg02wQfJTKGe6krahHuj5sN3f9qHKCZ2GcTutUXMj2TfycDlsGeXWi+gStzjW80zp5rVWceSQixnNHHUX8h3vWTljF6Lt2YosHwA5HvvelM54F3iYshvWo3BtZkmaJsayPZQXofX9yCTlaIVw0k00bitdxHpzl5V5wHEcQdaI1V95mpAGfsXvYYFQOl8T/ORkt9z6QiVh5/Ezkr9pZF9EOXK7IUqjW6KbHVXH3SVCNiZasqY2pi0SlS7DoKSEYN5dUSFK0rO/JTJLRA9sl1lo5geg+Vwr5VcHkzFIZGz38XHbpHP2ous2HexoHLV27sK8EcchN+fibit3FHpb7BUNaFo0WbK4uKNh1dh5JsKyjBmh3xgIoaQuYUQekzdRIZLtdbHmsiNdUwqPR0WmdszOFX27la7dBRUCY31rCTnsD1p27q6OWzC4V+8wBh8U30/axWxEyB22LW2P8Zy+5cXqukcRqUIpscQ1bG9U45oj96zorM4rs4mthmU2OEiLCGOHYxml3LznpQbBVoJ+s2IF2W39VFpUZNrLMBgv7YaVCAY9r3u+vKJupt+O4ooxleRM4Ig4OrxYd4c97aM4CCNmktxstVNSvJlfG2fX0erpdtloOywltVO383f+iJEDPN8y5q3XxrKF5wVcal23aGUEnpW7U05g9Ibf3GrDin0Zu14RE1nyRwLR8ZW6Klvjehqio+OGpaB00YG0FiS1PK3T9VzgNxkhz7tseYpHbEOTWr84tAsJM4Wdpki3mErxo8eEHDOe1WCLwTZJExGeCOJlK/mekKzSFUyHg+PJVhCS3ojRxXEbMPDiUJVUJZJILFG+bF9Y7gBOvmW/xnGS3J/7qFo0bW0a0rAu97S90pxDB6eVPcwtpo16aw2m20ViGZinzzKcmVOmEpxTDjf7UDCDyIMXHYYv1JpAbHzcnI4abFjdQVCr5RzTLSc1sba9+FmIXNA5lhveOuGssW4uawe2i/OhWnamE/irCvNDY93Fu8QKlwvfXJ6aLRaZrRnOnfRINGy3VYSjxrGYbGYlKfcsrhgqY3Tddd7X29K6Zlju8JUgs+khJeqUzbdrzaHUfrTHaNUtEpXU/YhXN7HB+NGarIRF2M2u4nrj33ZBdXR0Z4m2mkce1lp+XHRhsQd8zOXFfE/jZF4dqDoUbzuNgNnZYWnM9URSBpm+ehpJbu12VykOLp28MVuWvTtunAXRcpg+brOaTeJBove5ulwz2v5KSyjJlTHR7tuVYNPKIrqKDMXiAxxk3ikr1+Si7ODNrJCNjX5gCjf2xaC3xgE7EAPrpKsWy65+COb98w0l9NmZsXw7ixKklIIBPdVL8xrNycAl6TV7HQVAtQ6Vo8W+yWBzrrAX9YBocN46lhxLcdzwsrKIcRRfoQfJX2Ei0wXrcAF4S67tQx+cW1e064tkEXTf4ivP96TUa9dhFjJ76lx5SHPuG7QZOcpXcK5vo+TU98cMHzyyI3thRG6U38EeLZg4SZckh+FBg5sbsdFO3tIyA6HltXN1SG+17UdHQkDVVSSv1do1zM3iStv7q+XIjSco20NhhpaGbG22bCR6qFA6Gba+RPCkKp8lW+Q2C2dLtrPdOeg5jUr2FFmThuaPvbdZ4tKWm2v9gJbDUiMVqljnYtccI3cl7eYbZAgJmsI3QSc75PG0PJFdLKS302q/OzVUsNR8MUO93rVs5lQaxUm17TIDZWHuE8e6VkhZcpcDdTIcw8cVqsp1mh3xbJXa0XW5En1ebt0jRyNpLJkeGu1xPoQtbZFs4Q2cXa5uZFvucKOl5Oi2tgIg0hfO1dkJhpJBt5m6LnK1G/Mcr2e4OQSAMK+E2IyrMzPm8EWeF5m5QElP0HM4EPdORwZMHkpELO2O3X4dkCu5PWgJcqT3+tg6q8aLlHqUrGK3W+jC7lI5hQ0AvK6StjE3pIIgUe8zdnDJb3utF+eqf+sNRkxFQ8fVWVCX54Iw0fDsD2PBX2frE4/kqCzgGT1cSRzdN/w4bgxP19VoRMBgsvGG65DECEkyFzg8UxJNyfOTclrPPOZWHcI5aV43Wbk8x4shXzsVmKkW1ige5NXFNdwZOlvhjNSum2BtG6rhs1KxArgVSnJdE65aDrqSHc9EmFJgxLg64nUYdYIS54eVXqH9YSgagxBBY3bw+hDBq6Qh7a1iJXvpAM493AJ1WWNDMDcJptRDptoomi3nRych8fNBqcmhKtWZYXDbtoBDF1O3Cw2UpZNKATkvCXvey71yUMX2KqzVQxCvCs8M2Yt87VI2y5FMCAfkrN7Gygk3p2axnftRiq/HYyNc7HLGmjyxHkaE2ZZSJthMzVVLRtjHOY4vkW2vAADJ8XLNz3BDs3trxhdwY2M4bpx9SmydPUxoy52nRUntiniR7XBGg2Vx2AZsG1zzMeRMOCIyhEUQ2mPwhqL425W4BUTNmaDGlgbLMMwW3bvUFhxgqcIB7Cx7+aHl5v4IOyUTYC2OdNYsUBQ4DeRypB166bdd10mWUrrX5FyFC5zpl3k6ussK3uGcl8s03OyrZRumpaKwLHNqfDTFeHLObrIiT8VlWZC3i440xI2sizlKCqsT12UBcTroDNtszqiCeIuZ4seb6NwbBLLqe/yqBPYYBkzcdA1+oOamIWB82MOnVJodPMsXgnEvr4gjpl7byzzAqy2eHAdqLnf06IrW9mbagY5QLpf79dXARXgGX9edaHHInC/2LeEJLRadwMmvauXDPCTh69xoB1VXrsfhMKucVlV9zm/llY1F9MCy7D9eXl+mG8fPm/X/7in6dDP0/9k92cft0/dncvc75p7lfrnr+vJvLfn59aV0ImDH4zZzlTTB8+bs/7zJ/PkvHu5Mu4bHc+hpQV+/P7morWD6X1jv0QDrnjvBu/ve6R7++5PYl7sT7vQYrH0sCabHwA+fgJHPx0LANuwNfcNefvtvNIEnLYAmAAA= -->
