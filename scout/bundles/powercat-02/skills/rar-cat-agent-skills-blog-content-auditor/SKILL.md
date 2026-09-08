---
name: "rar-cat-agent-skills-blog-content-auditor"
description: "Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_content_auditor", "rar_sha256": "d164db261994db6d69cdd075d45da8ad058dc87bea407088e9fe06935dbd58d7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "content", "audit", "writing", "seo", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/blog_content_auditor`. The original RAPP
agent is preserved byte-for-byte in `blog_content_auditor_agent.py` and in the RCI capsule.

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

Blog Content Auditor — Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#blog-content-auditor
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_content_auditor_agent.py` and embedded as the fenced Python below (sha256 d164db261994db6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_content_auditor_agent.py` first:

```bash
python3 blog_content_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blog_content_auditor_agent.py   # or on stdin
python3 blog_content_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Blog Content Auditor — Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#blog-content-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/blog_content_auditor',
    "version": '2.1.2',
    "display_name": 'Blog Content Auditor',
    "description": 'Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority.',
    "author": 'Simon Owen',
    "tags": ['blog', 'content', 'audit', 'writing', 'seo', 'productivity'],
    "category": 'general',
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
        "upstream_slug": 'blog-content-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#blog-content-auditor',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a5c6bd31581e4eda',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BlogContentAuditor(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlogContentAuditor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(BlogContentAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7166bKb2LLmq9D7/LDrYm9AIBA+cSJaAwIkgZgRlCtczCAxz1J1vXsvJO1t172u07cjOlp2WIi1VuaXcyb4jxena+OifvnyoiZZkUPHIchfPr34QePVSdkmRQ6Wlp2ftJCbFhFUFk3bQEUNOY/faeLWTn2FQnDLS506aa+foKatO6/t6uATFPSJH+QeuHIAkekKCpMW/Mp9KMnKuuiDLMhbqKyTYjr8CpgHo5OVadC8fPn1t08vYFf68uWPF0C9AbdeVoDtushbcOqOC4D/9JI6eQTWyisQZsJfBjVAlIFbfhBCz18fmyANP0H/8R+Xwamj5pcvX3Po+fn6Mv1Ruhxq4wBqC6dpAx/ynNJxk3SCBS3Twbk2UB0AufIGiA+ETPLo9XHyO6WihP41rX18MHmNgvbj15cCQHAmbX59+WXS3teXupuuXycq5cdfXtNiCOqPv3yn03TuOfDaiRhA/frt+ftJFmz8vjUJoW+qxKyfvOrAS8oAEP9BvunzgP4k91TJt8fmj0X5Cfo55UmefwG8D49wAd2fkwU6ACdfXs9Fkn988pismzvA5h9/+TuyXhx4lzRp2v8W3V8fhOPA8YG2nir55dPdfL9B8FO2d5p/z7YEDvN/IwnY/sbuXVF/R/tu2f9EOk3yoHm35U/J/ewA/C/o17+V7d8d+ASFX182QZr0wO/cNPgC/XF3kV8/+N9vfvjtT0D6/0hGLbrau1P4ljl5EgZN++3brx+a++0Pv/36oSuBFwdO9q2r05/R/Jle73z+osHnro9/PQv46/klL4Yceo8h6I+i/B/1n6+Q4aSJ//1+8wX6MRKnDwxNQrwxfajgh2hsANYf9PjLy58g3+SP9DUtg/zxj39AQuLVRVOELaR6RddCwMBtkgUTeC1OGgj8nbJGHQC9NglQ7HMf8P/JwhPiIoR+/5+e0352IpC3PjeXJE0bZMqg37xHLvvmPJLZ76+QBoiBZBgluZNCylKSvub3YxOjsg6aoO5BcnKvbfAZxPDn6QJKcuj3n5H7dj/5Wl5/f6TcR4JT1vyU3JouDV4nMcw4yJ+gPSeHgjHwOkA0LTyAIExALv4ExGuKtAfJcRL5LgDkJyB9ACbXO22gli8Tsd9//911mvhr/sjGOPQoJQ0CNrzDgT5/BqKEaRLF7dc88OIC+vDHnx+g/wX9u1N34hMPCdSCp9IBwp16FCEQRN1USoA9gAVBhrgr/Y8/nwoFZPKghoCJkjAJHoeBE14C/027Krf8PJuTkBsArQZTdSrqFqR4KGlfIT6E3vECptPSVARiUA4hPyiDfKpyV0DVAeK8azIvWqgBntaEoCp2TXDn+juomHeIGYhmp/0dEtYSKDlFCv6ZYN43gcNFngD1v9v+cR8QqT800OqNxCskTm4HlU7tlHHtPHmEzsMuU6F+HgfEHSgPhq/5VFHvVfceAw/1gE1AM97TpJ8nm0NekYGA95s33vc9zlQYtXuBrL/mzdO/nXoyhQfyPWAadYk/Zf1/Pl2qiYsu9e/6A0gnSk8r+E+r3H1wquvQs7BDz8oOfe1mKEZA/z8bkAnLkmUVhl1qzAZiRE2xHjp6hhb0aJnA3jvTezx87xTessFbUvyaPxH+87HzrtnnnneYPghz5U4fmBXoaKJ797rJi+p68lfna/6WfQF46J5qgOJBiAIXnjznjeG0+oY0BnE4/f5eie9Wqv1JfOBZUNm5KbB6GAS+63gXgKqeIuepduCCwRRFQ5x48V+kggB1oHRAHwIgkskiQ35XnVgAMUHQhHWRfd+eTJ0TQOF3HkAbB3XwCpnA+ScHaEDEgfZn2gO08OFOCsoCoGMA8V3DTeyUDzBFfXkD6Dxt8aP+n0vfnfWOZAIPaDq+0wJNDlPC9IPxYdd3lG++VAfZFF73Q3819lNS6Mci8c+v+R3he44GUZtO9fUH1UAgWrLm7nRT0mlA4siCp/sAP7iX0tdHNXyU23csX6D1UoOWjwx1LxvQx+ytIN1rl/5Xm3yB4rYtmy8I8r7tNUrauHNfkwL5LzXoH1MUfX46zOdn1fgL2YcGvkDfB4S/LD898QuEvmKv6LR0SLx7nD0/X6Aufw/4jz9cPy11t0TgfwLJacpkwE8mp2ziwL/3B0rw3ZQASpGBrDVp+Aoq4HuReNsCKkVUB9G0+VE0mqnWDKC83WkDZX/N3839DAWQhPNoqnBN8UOI3vMDMN7DNu/JHCzlLeDtT01UFEzjSjqJ2wQvX/IuTT+95E4W/N2YMmVp4IVAY9NEA+IBNCJtEtx/vaWn6fqv49fxfuGkU8gUU8WbUnL7pr47ZL8GeKYYi5IpMX+CAMyoje9SDFOcTWXdBVI1DSiS/gS7vZYTzscYMzU+713Rf0VwD1WQY/ziyxSxn6Cpg/0EvTejn6C38eA+v+UdmLx+nRrhSWawFXy9732fLt3g5befwHj2xX8P4plGHinccacKM4n4E5kAtTqoOlDS/AnPdwG/8y0ezP6842wfM+MfL2+Z4mmlZxcHtoOQ/NxMRQ0Bvg4Ygt8PPwNr/73+7nkIpDPQa0zzKUYSvjsjMZoG36RP0p7vo9TcJ+a+s3B8dL7wvQXlBg6BUuhiEdBhgJI0PvddHyxRgN7DRb9N5TqZgEwZEsj/GXh58H0Z3PKfEjwQT+p5byfvHvgQ5I8XlyTATo5o+OXjs0Zow0FmlKvEBzhH4XFEiLiyT6WYezS30w6FSTrbJddlyebYagkR1UVi0E6wtw/+TkUPccHAyg4eNPwQ3tZEeal2zQ7VJdfcMEx9oY63Bun7NMNmjLVK4Qx2DCLPgvR6KUcjMckbjxNzJwhxMxhL0d+6l6ZebK8kRaYBm6UzqzA4T63EQ+5rlt5qo2mk2FYtnPmsOAhWvlY5VHVGNDFpm+/VTJAAq3Z1jX1mrlnkmjje6pqGYViqG9zq+pFve7zGae2qBbVt8r1BXvett7iUXoPR1d5c2dfKEMk4W6Sr1Nsa29WVwc9YXler/XxWBZfkbF0PQV5j6cLY5dd6ZZ10NzHkfDVmcRrLw0xohdrW09FzZgJ2umTo+QoP3XB15865pczAmeUnejfDMyZ3uu12dOODExSbHNMORmNEZaqOabg0fX69jb2ZPy8vKsy0HXYGyQ+RYz6umdhElyvNpiz7vLHFWz5Lsdk+9S44vOCsythaEpkm5CE1lcsp6SgdeOXlup9b1c310FXbhI26HnV31TJnlW3N1j4y2NVbmJVqIkjb4CXsmGvSVHe2EW3ROF/b692BNcd4cR0VcUFK55ONzVcJFgWsr1P1kQ77jXv0GlZE4Y0R3QL9MrNbOK+M27o+tVSy3dvnQOdV3JjZnk7i1yg8hCvqVKbWYNrrXJI4pWTtgKNmWnkd55JQ545tnjceKda5aMA6QyCIT3s7oRa6a3OQNHRm6/4+P/iuKfgc4VyRPdNq1/Fw7FF+UZ2YcRHs6H1qYF01Q0YhPzai2ItkRR1m5khjArIt6W2O7n1qoS8CT+upUNvK9tglRhxLbO0hF652ELWyEh2Pj7rOKTbtVZmsrUzqhHO5xovUQbdFxzePJHO20E4Fnd4Gy/kr2p0PWT5EtZ8Xsz2nbo2jkAyeuKJmC4Xs7ZNTHthl7JJ6vByW3rwfVtLMtk9RdTCwbFcqgujZ4aAPcbSOncMxYk5rZCvgSwcl6A3rLJTjcXWML/oprjl0TxCKRt9IjSVMvLgujiHDdiYXnw6HoVZy0hRvihgud5pEZuGOLszKH1qnSjeOmAmGN+9ODYUwN7reGgOKBjUV7OswDQ8q0eDbZCtbmnfiM4KHm/OpGEY3idY5ijqVF54vxT7UMSzOxV69WUaKZ/bFqzt1tSNnBlyv5dW4P+hJLO+WMmqHiNufw2pEL64de1WnAjeyKGxtu0ptrRf0hlpEyJzoSt8c11QtbxCM79k8EhUewVZzUTzuW2TJmnK3tLOlHc8aQ9nOS+l4WipxSlmrmpfLOeZYoWtHinHU4tVtoRiMOkfJzGv35ZCvNGLP7K9CmMU3QxfJbdWL/OWWEkgz1526ROYLqxcPqEN7IuZvkmHT8LAVoUKtj3ueXhwqukzAjN2629K/VHLMrTpvsWbqEFEK0kEXth43G7TYsVfMdXiYWQ6CSWudEK5TbYbbO3Ee86k0LJCuucKhmOcg5AREP6V61C/25FFRyz7iI7Vzr6OMm1TKL1F+bxOVhbbafNNjrVly1zb1U42NxNWcs/DDNV7BJDEQ8Va/bechMTN4UZubkuOpepsovp1bh/WSmovhSu9X+7I+7Agq0OM1zi+Naqstj9h87UsZEctSdwBtXC8Q9aIcyDTjbDR3fZtSmZZPBvaU7VyOW0shXrNZuZPkVcVkG/bSwTTXZhYvwXQlzzZWdsBuc4XNm5E7p+ma7cig5TWsoKP5leCXF9AdyeuMpQi5ldfrZsPgZZioXM6uV8ciMy56iUS6oI46jy66xbXkT2O1uTSJlp/DGWMqwj4xqt2o73K2NXJ3a5JRGcghfWSJy21mwZdwY6XFiikMRCsXpo4wEW9lK4s9FJv9Kb3UY55tRROR97swO1S3m52bozTzioNIXwlXDxNNOstasjzu9/6K2A1n53xwR5RxIjA4Fl3Zj1xywFbq9cBjgZGq8C6KXHVbeT2ej8h6hw4Laa7jCWn0w+WGrftu1qN7x8hPRHwoS1kmmTTdCaTh5aqCqHtV4u3qxupjabpLTvKVYVvKiELvluPQ+YTu6Mb8WgUCqXSrRhmVPb45XvSzILaJ7m7IlFFJtIBROT67IwMC8XaLcgfeVqmqK9dTs4yIDbk/OqF1FXj1ptL1Rbtl2ay6rZbybpMnrFm5M74iBd4IZXa7W8+SVpV9VF8sx2LJz5TDLlKly47xEMzvtALhiwN+VIh0n+h7hRWL88zXb7tkLDyKT33hdOqXlEWZ/FaOLmsj6Retba5iQ8R4eVUjfjVbt6agLsAkA8ZNOpfZfF1qs5PJrhThogBT3YzDqFYarFnoHLd1YZTUxc3UOFAhy/lWK5MAlXai7CfH/Y7NLzLT2fvTsulI1ZcPKNvt7ItotG0qHdnadpFYbXnp4PUef+qd/jpL2wi9EXPWH+N+yw7bsK49VFE3zYFvlJReC64vCvuVnSCajM3rHj06kdkxbN/KOJcZ6bJMzvMgrqOLGpEXYRfP123GH8erLXgz8rj0avl0qGqOSun02psiGdkssZ4Fl7H1w4H30cRGCR0h0KRWt6LSV/bSkFkz39ea3blzqTipsYXNlMoNmN4Zl5ucLA4rwdmundZKLJTmy1kDH7cnOozRqO4zY+3DW48Xg5tvREa87zutOwvoaX7SkKQ7quwIG+a2pTBmr0v7g5rGdtkvxEbVOb7eKbsMS418j7SmU9PyKiA4UDrj0im5ahe1V5RQKVmlCyw62+NsgTIKSYIkJVDaYaddEJGwtMNhI8drLlAVA00VO8UST01mCD839tR6sePD3m3KMj856rUOJbtgUDMXDgoPD/UCZUeRSlsCiVZGaaTGTqayY5aYJzXi1tapFlcKphXhVl/vwz2Yehfo2LfrudNIbHLqV3hBuEHFV/OVXDlsKBmF6lkNZh5jJ3YwH2McDi6ua2s4dcAhYLJyGkYL276bY2aAsxR5oLyWDGdBBkwquhRS31gh0hshnpFcfcurQvDVxby7rT2uIJfLgU3KoDWP+Yo4zqoW2fYrC0PZk49dVuy4DPWEYy9HLWSsXDak/VK6hbKE6RizkYjUMF2f7MXlULR8OBRw4cWhvEpO3ubUb3xb4H1rdlz2desKMDLjjTaGuUj1zUOomB6er4OVvVgjiDRoYSTzMsp4A4fTMnJFhRalRkNyquuMZOh+H6x3kTErOcWMPLjmig3odrb+UMR7EqQUOiJxzioW3EmoUP4QrNFGEQIrjCw+8XVpsRuYkkEShL0I6KzHhZsdWZ0odzmPi11EU8uNZTas6y76Gk8PR92O9eZK86ZhEj58O4kDmbXdhkQufkoR+s2PkKEnQf+1DkYxokFAMQtKpdrLThBN8mjGVb9h6p2AMyNH7eEdDR8963QzQdcnHm+2QHMEKa6u7YE67vuTCzd+y8/5LefDgqVkPJ/3w+LQDigYC1l6cWXQ7QGbNZsx2ZND7SY3dgTzFrqQbmrFYgE1CM3BbNuRp3oKjHiLCATQut/kbm81Od9Ko6BX2yNvHmd8jgbZbHtjpPNlRCx8j67gJc1slkPcncoOPXtMz6He2Rw3W3PwQcWncfrMDbWgDduWqCUT9OwayJ1Yek5muS4Bl47LClmKqEz0ZJvjGJiBpPyiKjZHyWwCmtMro7v7fZAhqMmXgwwiUOa3p+OZdKztVorxC2Jsz4h/ORij40s6ciMSZNmUuRNSGOYZ9PmKW6aV0L01u6VdaUcu61E55awaLY4kkDB3jDH3y46RkM7hCKVE3dPBzTS/0scW9ONbzCXWeYdHOKlkNbXYcPocCcbtiQg5uB4InKwlzuo7lvWybT8DVbm/WZqZYK0Bm7QT2rltoLUQXUHUWtY5IcjIJxfc8nxji826xTVRMbwMHtHzMonCAkGyY9zgcuJoBL9ljppm7PEgHXrNqU/rQ8CsCmqgiyZkN2B2psrt5VafsCLo4AVc2jx9PGw4gve0I1Zz7a4tqUZqovAEujmTD3Rq5XtBJx+9kh4EP0QDpKnqfh/11O3kjblUzgqiIDbGeV3xK428YA5MmIh6Cqyt7PMXe4NhdW6pm7oh2XPDprftxUIzllBJP0lXnOXPsW03LzwdtqsVxpiVnckbxSxkrG+MdiSZgtuHs/SEN9YtoRfeoefZ1bjrk4pDxUI/45nEy7GAbcm9LI8xHa/PGI4k9RrdrLhjfU6Xo2OXTYG2wfmyVOZjKY3zrdHn7YrWM5i4zRSXJl3BNFcVd03IlkVv2YnGDEQ4nQeFIlfhsq1vkbYZlbVTYHGH9UWE2tc1K0jXOePOZWRdhSODVHOEToCKkwoRUjnoDwaNH0/bYOEEkXpGsDKXOX2hDueixlsSs65Nnwk9tT/irCniNRgu5iUur7Eq4AyCSvawPJDDWMWL8SLU8nDkImIr1oK+gHcBtyekbj2TVkd8nu30FIur87aYHUHrZ9JXXMVvIuPzwGWtHm4EAd1uDhZm8T2ucKnbLYpe0LCDBbfOUII+AI/j27YcRTNdVLOLF/QUJx5wa5mjI20CZe0OoXthmJLaS4KRy5TGhZaAz+vUCoNgz9cjTu8yOuQkxhbmloomobGcX1bScVWrtmJf+n3VBHi/qBCePAbdpW+OMUyvbPVwsdo1GDjcBE7dRFFy2ZzH2ZwAcdhtbcreo3S6kJLKdIgctOYpHJwZqdmPNTLMpRQNdHuMCcORC7MukvlWapUUcRS4ugVNQ/TrzaU3SeUq9qaROviVJHYb5LjYdNdx6cSRZ1/GC3cCsxpobrv9jtQMTx5JRWCjdjMy/GbXBMLA+KJDoEdzDWbSThyWancWiTBJZpzm9+zO3Xb7zTngvB1OA+PkR4f2xY4R19LFomaMDqbHfgsXUr1c13BXUPMQXtcLJ0fCLliQs3kQbZCk37FRuaXYhdEfVieJnCHdkciihFgeKZ7dUsOeJeDVeUPPORZpF10nZNUxu4i1Zzen8HYYcNe7Yl4OH8N9c8VPDu4MOMzNh6MI9/gGJvw2xFaBYxARfbMml1n7CSh7C1mQ1heuhOdtxoWoriSuiO7x0AwW3HWupf4O2dDGdbZe7s8h7Codgw2cIm10kdkqWYaUdLdRNAN1qVuFXvj8bO82V1iunZ0jt/u4WPQgP/E215LnoaDiqD+WSzzcbFzFPdOwjw9WJDT07hyErOsdr2iQctmiEoczaSaSSCUn4kCqsJIwGb2oCzNNuvgkt/rxDJvbcEGdSRjplyWxUSOnIRAL7RHGdDExTQgbZ8OFNefqaJejMiZs1GtOXfRc1pDlzNKX59NJWC6XL59epifbz+fT//Zl8fTU8P/ZA8rHc8a3F1D3B8OB43+58/ry72H89uml9hIA4vG0tUm76PkI8z8/a/38s9cY05Hr40XrtDC2b8/oWyea/nfRXQnTs+nHMXB1Pwi+hzqZXv1OBILi5Y7fn1739El7R/V86QHAzF6x19nLn/8biLRl60klAAA= -->
