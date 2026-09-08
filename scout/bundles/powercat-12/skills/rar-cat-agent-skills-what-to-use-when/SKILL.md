---
name: "rar-cat-agent-skills-what-to-use-when"
description: "Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/what_to_use_when", "rar_sha256": "e80b02d38ecd766df8a02832be60359de48e852c670e6be8764e72cf25538337", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Gaurav Mahajan", "tags": ["productivity", "automation", "copilot", "routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/what_to_use_when`. The original RAPP
agent is preserved byte-for-byte in `what_to_use_when_agent.py` and in the RCI capsule.

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

What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `what_to_use_when_agent.py` and embedded as the fenced Python below (sha256 e80b02d38ecd766d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `what_to_use_when_agent.py` first:

```bash
python3 what_to_use_when_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 what_to_use_when_agent.py   # or on stdin
python3 what_to_use_when_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/what_to_use_when',
    "version": '3.0.2',
    "display_name": 'What to Use When',
    "description": 'Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.',
    "author": 'Gaurav Mahajan',
    "tags": ['productivity', 'automation', 'copilot', 'routing'],
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
        "upstream_slug": 'what-to-use-when',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#what-to-use-when',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd9b46fe1f7df7e9f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class WhatToUseWhen(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhatToUseWhen'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(WhatToUseWhen().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOj1pbuX6HzPLjcVCUSg0B1whGNhAQIARKjwOUoMw9iEqOQr//73UjKrPKx3UNEP7SqHhj2XvP61lqb/O3F6dq4rF8+v7BOVzs9JDqxkzrFy8cXP2i8OqnapCzAa6Xs2qCBmqSIsuATuKm6FqqDSxc0bQO1JdTGAeSCm09h0kJJ4WWdH/iQmHh12ZRhC2ELAlqXVZKVLTSvICcKCrDRKXxApQnqHhBfl0NZn6GwrKGsLKJPdVcUgB8E7vMua5M3ttOqVyBhcHXyKgual88///LxJQHXL59/e/EypwGPXszYabVSbwIzDiZ9MqeIwONqBApP91VQA045eOQHIfS8+9AEWfgR+vd/Pw9OHTU/fv5SQM/fl5fpn9IVd1Xb0mlaoKDnVI6bZEk7vkJ0NjhjA/Rpu7oAukFNWwP5Xx87v1EqK+in6d2HB5PXKGg/fHkpgQjOZO0vLz9OKn95AfqD69eJSvXhx9esHIL6w4/f6DSdmwZeOxEDUr9+fd4/yYKF35YmIfRVPWzWT1514CVVAIh/p9/0e4j+JPc0ydfH4g9l9RH6a8qTPj8BeR8R4wK6f00W2ADsfHlNy6T48ORRl31QOIUXfPjx78h6ceCds6Rp/1t0f34QjgPHB9Z6muTHj3f3/QLBT93eaf492woEzP9EE7D8jd27of6O9t2z/0I6SwqQA2++/Etyf7UB/gn6+W91+882fITCLy9MkCU9iDs3Cz5Dv91D5Ocf/G8Pf/jld0D6vySjll3t3Sl8zZ0iCQEOfP368w/N/fEPv/z8Q1eBKA6c/GtXZ39F86/seufzBws+V334417AXy/ORTkU0HsOQb+V1b/Vv79ChpMl/rfnzWfo+0ycfjA0KfHG9GGC77KxAbJ+Z8cfX34HUFMAbTrv/hrgxz/+8R3OqV45IWNXtEkeTMJrcdJA4P+EGnUA7NokwLDPdSD+Jw9PEpch9Ot/eE776Q6Nn5pzkmUNMgAU+9qWX7sm+DoAIPv1FdIAobJOoqRwMkihD4cvxX3LxKR6gqkPuWMbfAL5+2m6AIAM/fqvpL7ed71W4693GE4ewKas+QnUmi4LXifxJ/R8Cus5BRRcAw9UAgDQHuAeJgB+P04IXmY9AMVJ1bvgkJ8A2GjLenxAfFd8noj9+uuvrtPEX4oHCmPQo8Q0CFjwLg706RNQI8ySKG6/FIEXl9APv/3+A/T/oP9s1534xOMA4P9pbCDhTpUlCCRPl9/rzeQ5gAx3Y//2+9OYU50Jagi4JgmT4LEZBN858N8sq3L0J5RYgAIHLAqsmVdl3U6lKWlfIT6E3uUFTKdXE/jHZdNCflAFhR8U3gioOkCdd0sWoA42IMKacPwIAZfcuf7q1s5dxBxksdP+ConrAyg1ZTZV2PpZesDmskiA+d/9/ngOiNQ/NNDqjcQrJE3hBlVO7VRx7Tx5hM7DL6DEvG0HxB2oCIYvxVREg8lU99h/mAcsApbxni79NPkc8socJLrfvPG+r3GmgqjdC2P9pWiece3Ukys8gPOAadQl/oT2/3yGVBOXXebf7QcknSg9veA/vfKMQaedLACKOXSPxy8dOpvj0P+5pmQSlmZZZcPS2oaBNpKmWA8jemXRTsZ+9FugXbhTvCfMtxbiDSbe0PJLkSUgIurxn4+Vd9M/1zwQqKuBPgqt3OkDvwMjTnTvYTmFWV1PAe18Kd5g+SPw9B2DgGdADoMYn+z0xnB6+yZpDBJ1uv9Wou9urP3JPiD0oKpzMxAWYRD4ruOdgVT1lFpP34AYDaY0G+LEi/+gFQSog1AA9CEgRAIMDqD7bjqpBGoC24Z1mX9bnkwtFZDC7zwgbRzUwSt0jwjgiga4F/RF0xpghR/upKA8ADYGIr5buImd6iHM5MqngM7kizIHQfu9B54vv8XzXZZJfEDV8Z0W2HKY8NQPrg/Pvsv59BUQNp8y8L7pj+5+6gp9Xz/++aW4y/gO4SCxs6n0fmccCCRU/ojLCZcagC158AwgEAn3Kvv6KJSPSvwuy2doTWsQ/QCxe0WBPuRv4X8va/ofvfIZitu2aj4jyPuy1yhp4859TUrkT+XpH1NR+dSWnwD4fJqKyh9IPrT/DP1xtvjDkmcsfobmr7PX2fRqn3jBFGzP32eoK94x4cN3109P3T0R+B8Bfk1gByJlCssmDvx766AE31z59PcEndkICuR7HXlbAopJVAfRtPhRV5qpHE1q3WkDY38p3t39TAaA00U0FcGm/C5J7wUVOO/hm3e8B6+KFvD2p/4qCqYhJpvUbYKXz0WXZR9fCicP/mJ4mTAcBCAw1jTigGQA7UmbBPe791Zluvnj1PYGnH75ecqWj9DUVn6E3jvEj9Bbz36fp4oOjEM/T93pxDK7j4Hva99HQjd4AeNWO1aToI8RZ2qKns3qn4WYkgRI7AXNHZPfsm7i+Cci4CKKgvrPROT7hZM9U79pnanKAlR/hkED5PRBz/IRAq4CwT7Bs1N0YMOf2QA+U5EA5cyf1P1mv29qlQ9dfr+boX3Mib+9vEHA0wfPzg0sB7n2qZkKGgLCGDAE948AAu/+657uuQGgFOgxwI6Amrkz1MeowPPJxcIPKWeGUhjqBosZRiz9AKcCikC9BTkLFm5AkQs8IFEvRAkCozCMBPQecfd1KtPJJMQEfED3TyB0g2+vwSP/Kf1D2sk07y3kpOVTid9e3AUOVnJ4w9OP3xpZGo5rIa4U7+E6Q1b6DbHcfN7O2sX8womEv2uw1T6ZDarden7k7BNMkepuvPC1KpfO9cgtNyG6RUZtzugdMpKJvY00i99kTRJTsm0TC5sPMLLvQybrvMaAB3LvRweTYAcMQ5apgZY8GPMcO2uslGMyUuNN1YYFS5MlC5NbXGgp1kSzNNdUJTqdrdQSrlmuXtr5LSVJZIs0iV5lNbdHRdag+OtOJDbnjWBU5/mVgRV5bvjNyRRy+aqmzq3eRGothkNohJtOHU+Vwa4IAkUCjruS4olAUf+AulKPZSS1R1d9qcvlOR4TVkXG2qvOYcqM1AXT9/KxOlG5VXQbVzDGs9xQGwzLrydWp+TbONJLb9x2+pFZp+teTIbc6m/rUQ7GmXJWLjeRRqwxhunmvIzoJWZRZ7O1LK/EuyuwRFKvTg1f33hHGrtT6QLcybqmDXXq5qsztSiP61WUGdtq2x6YoTfqjYgaF94RT4wAR5u1zV1Vh1cHX3VI1xuxvYsOI03IxKpZRfqZETB0rd/Q1NvDlrSdV4U7t+RhtplHiHDel51i2utdtKKVMcJ9xSLNs9im1Bi1sTzsHcW4ZqaLZRdJ5ZCzefFIYYkeVr50WYouvJ2fgxVh7/S4TmRRuZE5Fi9NTd2Pt+Jym3nUYnVOOwurLxlpLLAjNaJkubeX6uGwYB36Wt4wnEh6XEodPhlOID/W4s7dZabttooo75E1JdS748BexF7bhMLslJNiQZiY3e32MHEu2AY9xSe+QNeUD88RbVWgt+thGd6aelUaLqvCe8NZGawX31CfHYkz2jQ4jDYHvJnfpHUyz4OZEumLvQ/vxiW+ObH18lz3nY5QS4uPyYYIrhG1XpHR7bTMBDo+kQ3sbY8FO+7NzYZypBt8DCyMUjTjnFC763AMU828bqWDvFzPJeKGVMZ5HkkuZ0eySBQ5fBm8plNdTbVQiYur8jbnGXxErVFjhozMLCvEPbHTUn+l5XtcSeRj4FXpfIWM1k6mj6nh79KLnq5PGxcWz5yPFXtbydfjaJA3HqCKn55wxbWoIBRvWOKYeRcO2g2e74kDvCEjMkjqIkH4rdd6+4AVdsEZ9lLZO5uFat+YWwWfbiDZZ0TpZ4K73VetjlsBltmHW7bYn/QZJUgGOzB1MYYUjrEo1SmEtfROiZgrcxEVejbe9KVptqfSwkGiy9cSVzWaYIW0ieTWcjdaRu0QQUuv11Q4RZk2DEqyg4NbcMY352Xt6aMGmg0HEBzqSKaz1dhrHoLXXli7iVlaZkLiLhxvyVO47QaOGKv9KO7YtYUMGkVbSzs/n0e7bKO9yYesNjCFTlpMzdPY3FLH4BINx8sNhJ91Om9mGckanVqdudWmVqyUOXBrXjLXHBW7q3nsG0eZI9DFcJwhF59zYX3J1roSsuWBZDY2EfIrII+pDymG9+s83wn5OJ+f2CuvV2GwinxkFMoQ09uRx47S8WZxV1010CzJd42zor1+5HQLJsht1114iY95I3SLBQH7NXViloqrwcdiJPxo16vRVW0jqSboVCoUQiCYMzfgWxo9yXZ0PKxztnGx9ZonNyubsdRWjdUuKW/laW3rBhtdWyzdnG78IcFPjFjTZ0kHQ5G/YM4n7Mb2mnCqBWs7y3E/FOgwM5WR6KhEUBJ7NP1iv8F4de8UZDled4YEL1DBOeYdbY5aMUtUSnGyyL2IZpTJimiYh81B2Gnw4qBIh7OHzGvmKCXHDtuf6UtwLVBQd4/V8ooXZVh5t4OQraIO1tSkoDL/UgteqKMH5lAuKRXXHY8IIk9JIm1fdepFXWxzk/d1R/Xd89JSCCJY8rWUjYIi74D3TD4jme0x6RzjZGry5brkA3bFHNcLq4AXJNXs0B1tKBVRlMYOjFr5ctueDF9iVUufIZJpJNHihtjnK+Hz8g0eURpzZY7D04SWt6qttPO2ytZ+AxQtV7WA0ATToFhyQFkRuWkCLpS9tWvo7W68BX1xQ4mlPB9CZMOTyWAUi/NGdi9LpQ6O/ko/DawnqMd4VpkajUVxrM60dHt1qo1wsdexrY11fYqYfkhXjk4BNKWpIo/nqkhkerJJLGkThpeNyuXsydmWiX4S9K2pRMKx4WfMcLms8LUQL4lLr+iD4bAks1dX1W3GxQ490LiKIlmy2rPRGaclT1HxbXtO8Tnd+qjAr2XK3Vz45BBxHDuoV/Y4X1vRbr2rDmWG6XV/1k56vVBvzWqzp/MkobPgbA6zYnvwvXynctnVUD3XiY+3C1YFPD9TY2ldnkyaFbazQhiynZ6Mm010TEde0cftNh/lurAP1lXS9r5qF/MeMbiOFZhwn2aMRYoLewajakW3tNxyQW5kCsJuwNgV84GJ94OaLSvbh3MRUTTBZL110aeHPOY0arNWA8OaCzmAk/V8rl+s2rEo/NY53vVWWb15W3MHp8i3nkCgl8uVT+3ExIRrjdZqcQzk24I/zoI4l46RwVbaRs/K017QJXotbxWOdVFmdsQM2bf5cWmudqxuXTb5orU4f8VfisCRZL447ZLezVb+6EhLddZE27Xi6lR+Wh+Q0k/ocnMWUuVwOhn8Ud9rM1W6wJsg2xWjuJpxp2w9PyfMNr+O1Co2xo5BnTWK4cZqJh5Xtng+GMP5EvHsJaGauDQr/eLl6ugMZHVsrpQ8HPf5rl46fY1EhkwnFJkL1/VZ01Yn2vVynZc7ja7I8+YQpUQmLM2MzWaNdxAGMTX9lY+nbHgWVx6pUVv57ERHM/Jb1slu3dLRm5gR15zfBcebGrLiIjUviYoxCWdWYmrT8XrZlullt+r3HStvLXeR8lsp7I/CuAS9XByOSlb72z2bRbbTHiSjuhAbPRWOnhKhJlMNOy9lGmM3ayMaBRF0tJuUNaRljeYzJJcYitCEfDtLqcva22ZON2O2o9eqIZ3x1wmZRxUbB0xmE4fPcrM5bkhrg/PZDHSzUS7YS8Wu7Srj91Wt7/bKClO6zeKyz+TkrDYFGhyXtS8EWhBvtrleYevcoFtxy4B5VYmJjuhWikp0ij+WBjfvdl0+2MKs0JZdK3PLuFFHxN1fQz93MLlh5Cvl4OTtuvaPe6YyWv/YOz6lblBd7MhbhcwUb60kvOtLM3KbnzZykDoGl7o4qhfSerHTLgZydalwrWfqtYnWuWr1Ptxv0dwl+p5xDiYizTVibsHkrLsILl4sdLEK0XWcDxu3I6y5mM8rO2A78drcXLSit3EEF9Gx1bd903qbBWWMBBK2fQ/zPYqXlkieSLgOcXSIYwIDgJoh7exYV0oSa/wp2u7PMiYirm8yx7Q/X9UZccLbwhuLJbOOuUXB7ZHc0zczWgikOqTpgfKOssphcI+feQ7O8VlW59nNzUM5SGbsWbFdq52ThWV1blvuOE9I/WwpU6V9i435XuyTbTbvF6APVQ9te+s2By6Jo7V67VIK6SRsPsdIQtWYsWxcWlqKHXq+2Kv65IOQSA3PHpsbR3L81eaw00qKF+McETvYSSyLChuq4kKvV+CUr647pObITooEf6akKmura4FkWRZDEq3usAbmHTvZ984pboZtbiyssdFy2+wL2zuFzsHxHH1fMGPfKDOyqWdhR5WFKVpFxMDXBg7hqMDW+9aDrVnYjEyy08CMmvAGZvVVzbc0Lx3xDcMPV9BaSQNPAETICa+rL9I54q5EK1jBGFlsZeurlkSlaPBzQXYXs0zL0UIjBmZt9m2/sC9DmS0Q9nDFRbYoBntlMcsjl8U7nVKTcFPve7uYDYdhZWnVNraikWRVeqXM/G2GliyYjGjDyFuUXOKeHcKdB8C0s8wr4uY3m/LBFEOuooWMB9JmL6aIZyZrr76we+m0QI8xLpkdv7xV+IU/GItle0alGrvEdrdi0lSgSHp5s9mWkOTGvcg9A8f6vMDbCtFbqsyPMhME5rXrWc4riAKt0y64NLtUd/D6tGvzvorqfL49zsDYOMaMQnhtufX6FboKNtUKOdp+42/nGnmN+JKLxDCzRtbw17v40KdnpgJNeNZ7+NV3JR8/RhQt1XNBo1Gs6s2+hh1jKTsVKWO3pO0vBiiBCOj00OrkEUhndnM/kwkfqy7MxqwEH3bUCF6w5IZT+aUMtwesQ6htfRXompx3+M0bM2F2YA08IvFYjWgdNra9uazqluY2ilHc2It3mV/3pa+GDDHbMQGIbLW81ZYk5RGLceYirfnbYdR2oKjyuaMJST5E6hFTgzRMs1Kkhb6r8tOpN+cctQzKtY2CVFPxpePDoikoy5NUFnhwU9u5wOOzpb6O5xhyYdelU3qLI2MXh2KQV7adWW3uL4/KbimEOrm9nvrrqgvO6BlGAfQt66YZGmHZDXWa2ojkB1d/Xi9796hZ9MludKIbRUUvRB69ojGD1HveIttqFMkxxngdKXeYTIERKBhdtb8l+E2NSBkdiLmAXSWS1VWiXTqbZZ+orGQ71CnVrjtb0FSs16WaNaWiRnYRXpFHekHtGUEPcSrCRLOUnfMuE+PYZpkAPxz9Xr+YcEkxytB7UivkHMj5nV5l8SVdlahsFLCU16HfsW6hxosVhSUKB1u0U6tUdTQQgdqC0aspQUWMdzGmUh2IMDBoLDaepeNFK45bNxUO5rLYbuM5FfdqyvTtLTJx5ODRowZnGGgbfJkKMDDKW70qC+IBxPBloE63KhaTrtH1FBMjPxnaCy11Erw97TGkDWBY0X0kXOz3uXw4czzhnNPSJTsi41Lu4it2F8MMtic9NEVOxmKhD4FcO3UuZ1J3kjZeAccLObTz2wFAiZdcBVk8rBlQgx0q3Z+P3bwLC/XAtm623YKmz8tGzDjw+dJwtlW4n82FvkJiBlV3nLNeXXOlO0qB6WWIyASbnXUyHRDniriOGni4buLeOOQeQ3GbIlfJyuv8GWiIUhPfgBFmJWL1MGsbbCsQ8A291nA6R5VOCjoWU9dxMZaL/OyJc6XYwgR34dSeaixy4XfbGkGzpTqvsMJD69mtp7KrPCfE7ngaWtger8gJwYd6HDZ7fuWKpXU6iLm7HLeiBHaQAapecNUp4foIGmUDRIHY911wvQmXYjzIaG3IDdHOVxeKg/F2QQTkqg0x+8hXhBz2LrdNyKAZDCteIti6Z0KJ6knMJXvY4lEup4gBFEeBkWx16++IZF8b/GZjrDEKLbxdG8mJnFROKaxNGauWHRNoBqqR8yor1bO3w8WsoLqItISZblWL5QwRdnjN24UVbLngsu/qHXtbWK4meeEJx3opprenSnAxKceYc8tVCiFfCo/vsnN6C/AtDKMZdw5jgGTCZXux2tKe7W2mnJlITWYh0s9raidxuLke5QMKs4dFonnVuTspskhSBud6fbf2V+MxN1DRQ+UkDJCBRQJklnjahqbpn356+fgyHY0/D7j/9mP0dDr5v3YQ+jjPfPt+dT/bDhz/853X578X4ZePL7WXAAEep7lN1kXPY9J/Pcv99K/fP6bl4+MD7vQd7dq+Hey3TjT9odLL40NWm/RJO+n69k3i/idJ3uNT5HQeXHbT9+VJkucXEiAA9jp7RV9+///si34KtSUAAA== -->
