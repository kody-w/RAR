---
name: "rar-cowork-cookbook-scheduled-brief-retire-knowledge-base-articles"
description: "Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles", "rar_sha256": "e6f0079856f6d03be10ebaf851aebafca6a924b5d350caca7030cad0c8fdedce", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Retire knowledge base articles Scheduled Email Brief — Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 e6f0079856f6d03b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_knowledge_base_articles_agent.py` first:

```bash
python3 scheduled_brief_retire_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_knowledge_base_articles_agent.py   # or on stdin
python3 scheduled_brief_retire_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire knowledge base articles Scheduled Email Brief — Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_knowledge_base_articles',
    "version": '2.0.1',
    "display_name": 'Retire knowledge base articles Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing retire knowledge base articles for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
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
        "upstream_slug": 'scheduled-brief-retire-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e074cebdafcd5db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/retire-knowledge-base-articles'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-retire-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefRetireKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireKnowledgeBaseArticles'
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
    print(ScheduledBriefRetireKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abeiyLrmX6H3/ZBZ18wtgwLmWWetRlGZBBFEpLJWJkMgyDzJULf+ewfq3ll16pzTXbf7Q5uZS4GIN97xed4I8tcXu6mDrHz58qIBO0W2dhyHASgRO/WQVdZmZQS/ssiB/xA3S+sydJo6K6uXTy8eqNwyzOswS8fpbgC8JradGCBJVqZhevnslCHwEZDYYYxUTZLYZTjA+0gJ6rAESJRmbQy8C0AcuwKIXdahG4MK8bMSqQMAh1V5llbhKDJrU1D+DYFrhpcUeEidIWWTIh4U3SNwfAtAFPevUC3Q2UkOxbx8+fmXTy8h/P3y5dcXN7ar6oeawFuOuh3uiohveiyhGsxTCygpttMLnJL30EMpvM5BCVVL4C0PmvW8+liB2P+E/Od/Rq1dXqqfvnxNkefn68v45wDVHK2pM7uqoeaundtOGId1/4owcWv31eiPpkwrxEYq6OD08vqY+UNSliN/H599fCzyegH1x68vGVTBHt3/9eWn0QdfX6BL4O/XUUr+8afXOGtB+fGnH3KqxrkCtx6FQa1fvz2vn2LhwB9DQ/++6t+h1EegHfD15XfGjZ+H3qOdcObL6zUL048PwXmZ3UBqpy74+NO/Egsj4UZxWNX/R3J/fggOgO1Bm56K//Tp7uRfkMnToHeZ/3rZHIb1r1gCh78t9wl5Oupfyb77/x9Ex2EKc/rN4/9U3D+bMPk78vO/tO3fTfiE+F9fWBCHN5gdsHS+IL9+0/br1c8fvB83P/zyGxT9vxWjZU3p3iV8S+w09EFVf/v284fqfvvDLz9/aHKYa8BOvjVl/M9k/jO/3tf5gwefoz7+cS5c/5iOGJEi75mO/Jrl/6P87RUx7Dj0ftyvviC/r5fxM0FGI94WfbjgdzVTQV1/58efXn6DYJFCaxr3/hhW+X/8B7IL3TKrMr9GNDdr6hFz6jABo/J6EFYI/PtAKujXB1A9xsH8HyM8apz5yPf/6d6h9LP7hNJp9QZD3+4Y+e2BiN/eEfHbiIjf3hDx+yuiw1WyMryEqR0jB2a//5raF5DWowY5BEpQ3iC2OH0NPkNU+jz+QMIU+f7XFvp2l/ma99/vBBA+kOuw4kfUqqCY19HyUwDSp50u5AzQAbeBy8WZC3XzQyjn04jdWXyDqDd6qYrCOEY8uLALuaO/y4ae/DIK+/79O1Qh+Jo+YJZAHqRSTeGAd3WQz5+hkX4cXoL6awrcIEM+/PrbB+S/kH836y58XGMPsf8ZJ6ihoCkyJJtLk8BhMIQw6BBU7nH69benq6EYyDcIjGroh+AxGeZtBLw3v2sc8xmfk4gDoL+hr5M8g06E5BbWrwjvI+/6wkXHRyO6B1lVQwrLQeqB1O2hVBua8+7JNKuRCiZn5fefkKYC91W/O6V9VzGBAGDX35Hdag+5JIvfKHAcBCdnaQjd/54Vj/tQSPmhQpZvIl4RecxUJLdLOw9K+7mGbz/iAjnkbToUbiMpaL+mI4OC0VX3snm4Bw6CnnGfIf08xhx2B5DgU696W/s+xh4ZT78zX/k1rZ4lYZdjKFxIEXDRSxN6I1H87ZlSVZA1sXf3H3j0Ac8oeM+o3HPw8O9biHeaR9b37uPO9sjXBkexGfL/R6syWsFst4f1ltHXLLKW9cP54d2xzxqj8GjNYKPwXAZW0o/m4Q163hD4axqHMFXK/m+PkfeYPMc8UK0poTIH5nCXDxMCeneUe8/XMf/Kcsx0+2v6BvWfYArccQ2GDBZ39LDlbcHx6ZumAazg8foH7d/jW3pjqcOcRPLGiWG++AB4ju1GUKtyrLlnQGDygrH+2iB0gz9YhUDpMEegfAQqEcIqgt69u07OoJkwQH6ZJT+Gh2MzBbXwGhdqCxtZ8IqcYNmMEahgrcKOaBwDvfDhLgpJAPQxVPHdw1Vg5w9lxt73qaA9xiJLYDb/PgLPhz8S/a7LqD6Uant2DX3ZjjDsge4R2Xc9n7GCyiZjad4n/THcT1uR33PS376mdx3fkR9W/CONfzgHgZWWVHeIHQGrgqCTgPc8fTD364N8H+z+rsuXPzX8H//anuBOp8c/Ru4LEtR1Xn2ZTh8U+MaArxAupjBHwhxUP9jwUYafH0X3+b3oPo9F9/mt6P6wysNpX5C/pukfRDxT/AuCvaKv6PhICl0w5vDzAx2z+rw8f56NT0fo+RHxZ1qM0AuL2+nfeehtCCSjSwku4+AHL1UjnbWQQe9ADGPyNX3PimfNQJxPLyOJVtnvavlOyDDGjxC+8wV8lNZwbW9s7S5g3AHFo/oVePmSNnH86SW1E/AXdz4jP8Acho4Z906wnmDXVIfgfvXeQY0Xf9wD3isNQoSXfRkL7hMydrufkPfG9RPytpW4b9TSBu6lfh6b5nFJOBR+vY9932A64AXu4+o+H4147I/GXu3ZQ/9ZibHOoMYuGDk/ey/cccU/CYE/LhdQ/lmIcv9hx0/0qGp7ZPCwfqv5t4z9hMAwwlqE5QVRs4ET/rwMXKcERQPd7Y3m/vDfD7Oyhy2/3d1QPzaZv768ocgzBs+GEg6H5fq5GslyClMWLgivH8kFn/1ftppPaRAFYXMDxQHSR1FqQc9Jn/RQwgEYChzbp+eYPX67Nmkv8Jkz94g56tquTaEE/PZQl/Y94LkAynsk7LexPwhHDQHqA2KB4a5HkPh8PltgFG4vPHtG2XAiTVMoBedCZ71PjSCEPs1+mDn69L3rHd3ztP7XF4ecwZHcrOKZx2c1XRj2dEY5XcBNTHTSWT6lmppw0PMCDYzWbIy2KTxuvTr1hAoYnhIEV7Oaa8P05mITzTlhxfXLfaL5pUyt5sLR5+d6vL3sXBK/XitKGarprYuKsJCE48LMTllaonV7FGs6i45FGYitkx5MMUx8y2iOtVHpht7kK38jlPXBnk73h+EkbPLM1RVMPDbyVDkanaHjqU1ElDlZu4uN79OBjSmSVdSMFdb6KUKr4YjnZOaGBmbdtGDwt5stkbvXJQgXjE/uj56z3QtzRRqGxRTczHnnK6VOm0Y08fa3GbFxKVbU5SSrgm3vOHaCVQTgSLHut2p8xAh1N+22c8o2nFMWe3N5lVOnatHS3szIWTaiV5erVeJBoe0lbNY3fRxk+s64ws2A3DPumaBO/TpVsLSoHUnW19cOWn5KMP4IrcYX7ZVDT4Xq9rc6TsmbfZO12JF22rKxCnMX9ES/muOYTa77KnZzPTEwVkhZHj+sYtHeNrVztciko9wlvRxuJwCYis+WtXTKTDENri6LWxaGO+Z6oiS1K82BVS+HAi8MrZ/gbrFdbOeb4pIP6qDNprlqhRa+cm6ykGMhFVsnvZN1UxJg8ViN58gHlaS0/mgwELE8ZSXwNrVVm+2QzC+eI5kS1sfNENG0vYz2qxuapzEqDZOgvtYDc8LwmavHEdZoO0gLUBdHpA+oHZAWmh4UUaHrRCi9Ih+05GYr8V5NAnY/2e7SfiO425Iqcp0zRZ8UK9wT40YYOHEb7CfnmRBuWWwoNqckp9icmu4l3TgmvZOXktRp0vVqpf4G95J6tuTIdWkFKrYkVaGhKqEkMtNMd0LJwd+Av+oYJtKp1bFsTXrxRFpM1hzNrGof+v/QTLPpcVfGU0G+zbtFuHaTuKb2xHKNbnG+RiW8O5Fk0YXoSut3eGIEVajXgSsXFE5vs2qGrfrO1oflgXZwwz5tcSPdyfzFUiLS2uSpYoS0tEavkuCIy8hPt02LV9twvWA9IQpWlabxIPQqwdT4kAWLqF4eDpJdF0PDV64iZ/PakhpDPqcmVZWsureaXI6oZb5OgJ2zsqwWlnBJkiTNMZgc0K5tvtgPw762UbE5TleuQ8cnE9DxRpntJ/6UJ1BuZnV+FXe3uRUHfr8jNmXt68J6drpd+X25TWwladB5cs4LbFOWZ1w1HYlm6bE8PMxbpZGbZsejtbUvfSXj2lVDM4gHXov6LNSMgs7cLQZRHZLp0OkdHRcFmYj9wl3eCrnwPfTmboF+u/inKJ7vTgl6Do4XjPPqUAPLbHOe1uyKgSgyjxJyTkadLWq6uIv2RgaJvZto9QoLOKsn13w0Ja+3kBT7vptI4KZESbPWCfnWrfGVqJBFyHnno4lefFttu+VybqV1y9QHD2NicqBOrivQbIElGM7I4dAA226kVBYas6mx9bRmZl24oVdUm7IyClR2ny5AndyM8nqlDo2xP6r+Ur5O4tWM72iSOcSnzluD9RTnTjNxEsUVeppnxKKJ54JSEeGwdOjbVGhpx1p2ynythJerSHpmJjX+sFZunGoThKhdY1FxO8XK0a3dHC4yOLqH3M8uDE3Pp4Lm78W6Xa1dKk8F3JpM/H1LW0VrkFfseimjPJyiWnoJ1lbAaCo7xdiGG3hC2DFLdne4nhsNrLS5eG2JZgXq4kZxB6vVVhazPq7AtT7JXZRJzhYUt2OzkSRC4vJzf/KKk+Ko7rHNeG92zPNW1p1qFelest40cT2j9s7sJjEd36A7JVlRZTmb3bgYs+TUoFUt2nXnq3Nr/K42ZzXHG+QZbfqdImD9TipRfrHniE2R1k7Cnlv6sORuvLkA7J7Dz8UAjmQ/TMXjhM78eH+cn/ZgAnf3McqCSzDL2xUnW5TYhrWYmsUCwwKLB/Ttam5qfqNcLy6TRKcsS1sJO+POUd7qx6BX/Uq8aBCZ+EaiJ4d4Ao4xRuA5KqrY7ox6UbG5YNLkxnKD6uY+q4Z5K/Vb57KRW2gj4VKxyJxNZ3bdbQ7Neb/KhMNJINN1n+yN01AOIT9pSuNgqnHSo3V6YFvH320aSIPYhiqzYukQ6GzYylyVxx3VLQ+ihkUWyyr8tBaNcteadW2qzGrR5HOxU5YVa0S56qTSscpsiauJzE9v3uCqC4k9CJNo3wnBrHSFiFwSgiaUSxvFiqRsTuTKpCZs6nqXDSq7O0JJkyLbXlJ6xV2Kfa1gDjhbqaxg7DBBi3quH/IokGZGmDiWqgTLXDNStiiOZTIN59mx08XNooc9AnpQszN+qJl0FpqMQW3OGMfXVY+nwWLVkivNcDKmSIlTLUX4Odio6IW/rPdRkdxiHIW1KmO1ji7XGnNG2f0KbFcMJC/ijBsHqddWDM2wc5zhFimTRtZc8odsmYcxji04MEU77VppKB5ZNcqT0kTHzjFfKUGzyxOGtCTCrR3sAqHQPOvAsK2mW/koyYtAl7VS35zkiSyqO1IRpm57ge2ZIeuZPW/UHXpanL0sKpfkXF5fMDXWDqkRGOWWuapn+RxPbgqIbzNVO7ZHm0mz22S/KSOeJoOb2bvqXMcVtTyx/a1xvdoRlNyBQJ7x22WiBc50PqG9Yc/p13S+xesWIkA7ITo5H66ZsgWsWRYeP6k5bOL47GR6chhj3Xs6ZRoUxqlsJO5rSWW99Kayq2htbXuRwU+XvmVx2nDL7sw1PLHVz0HIW/pcSE1s4R2vLhbrRq/D9up8uDJr4XbJjk1utIFki/JhY2DmvC22Hr1zAllnwGI9RYXDsoyN5XHGboNDZhLVRA1Ipm2UxelWHxhvrQoZfiv2WjmTza2/cxWMn530CzVrHXe2kwKGbdpyqYk7O1grzcSSycAK0OqID8xcsBoVi4bhtLkRK/Fs8hp9tOxDhTFzTxN6FV/G9DnXcpuZVJIZC1ddYK5mcmVoWw3U66oIxCLY5G5zwEKSd9xoJvi6qvAFswI8Siy3ItGyq2ES9i5mxzcSZOwGtlbNrNG3uTG1+PnRqJIV6R5wNylhLlGW6KAmmaqtxc55AZNupVSxfF30sinIFp67gbHEUikls7hGJwsDq1lMkSuSqtV4GUyDaNrXodKWVNzFs5OnafIcU9GrAmz+5rJKYObSlV+vXIJdG2x32BuxqLnpqT5h0yhlKFcwWD+mMMgZV1viXY+rcWaj3LKUlrThuOy9bsDqqyrxNgEwqQiyNesWFbW06Cs4nbdHVgsEvN1AV09FY9lOOS9f0x5jHQ68QF/DVCl9QLf2LdJmqJ7GtbSiRB6DTSdwS3IZd9vtPg0Sz28yfWWRh11yMuHGDuWPe84y6bwUtKs8mbLVOZc5qRY253MgUmhrMGoyY5kjG9uTo9Du6lboGbF06b7irqdyLfs6BIK0ZQkIsGGzU2/rmsCyXlzXKr/CFzHq6uH2vMCaDJ8QRWySfFtn2QWlGJ4e0Mn2Iiz0TWKx7bDY7GA1s1LYwQgKW2aNKtvJNSEB1hhWrK3zardp2y27NCxlvSo2eXdLzod+6/Ed5Cp5bjWg6/wsO+UrLGPYiDFLbrjNQrdtW0zN7eUuMiUlxyIRkBepZA6Lq5bRkCU4rFaDzNJ0jQi2gpcaA05CMN5dZUIiD7OVKIpU0V72m4qitMmNtw7G5kKuSrIUm01Z5bpzSeWpfXG7a68oWFItaWN+EsL0hpUaCQ5Y7d/wTBK5xpgTfdO1QNf2W3qmmF3blNWZYknrls1wtvbXkyGPRPWU7a1Q95TcOG3jnS2nFaqQNsP0q+326oZNg+uLxQE718RhzuDuqVnnjZFoFk3zy2bvS4W5P6yvGSWvCofzbkbLr9bpkrlY8mC2hdJJCSEvu4Esbpu17funK6Zw3IFQK2+iCrBJESmdlsPzZY4Rt6OC8yxNXVvaJW4pyBwF6ENXTCdmmk4ZdruxLvn0NIW0MVk2XF0Cspvsj7ISZtSKU1aN7POXU2gPobAP57METczNcCSi05WdBMosDFFnNrWP1SnKDju5sM4dyU6ZthrohD6aKogGvKymCuuYZe2F5F7n2zUh2/Fpju+4gIpKG9cUdSio5hhzcD8GrGjt9lU0sCUpzspBOu2TDblb38pMMo/SpMYDaEwmJkPolBPqMpGG2glDlaN6Wq/lcwEbU47cDnvSWHizpaQOli25fsGXAndFD2mG72XUT0hHNqfYlWq25bayV8JkWcF6Bgnbg0lIU1zD7TFGtzQK9p047A7W601gckLilXD3YNCe6Jn6cilQvsUx3oGIZxzhi2C4JPwFTD2pMdFjQQsYWfH9pnG1Hb4u0Wyhdado4VXTIUcjfNleMmdOOvWZWEpw4zNgg7JbuGugWLNDN4/x5U5fagkRTN0t5wbypFOOOLS95EJfXrdGzpndTqTtFvieOwF7drkk1m7TLo5LTJJnnH8WTXm+lteCVZ5X1eVAAxxnOm1nGYlsnv2EYw6nAu9CB+wzqK+xddt8EoKpTfBcbWah0exwOi3lZcimoi0d4XbDJNDmzC8XR4tQKvUwDQjRrq/eHHXJRsfP8gJdbdpsNu8X3JKbxa1xVjo6tyGlmO2iOkD+RU/mdKlugd23VDg9DjCrzatjewsVQ2ucU4/dRCTEJkkhC9s5p6Pbld2BNOvO26s3q1KCbaNMueT+CazMfE/IszN3ZIct0dVemhq7oaJTpw2PZ+y4yK9uwMUKtcapgCXYelocTcgQKOWvymVVN/iUkTGJoNrS5brdZUrs99fytBd4ovBactEBJcAmG9RNy426o5qrpq2mGcENZea7i2Cw9352u3VH7TqNF0tn35m3bBsKTD7L5v2qbJf6DDOmrr7zu2mUb1zPmrVKWSYHszUdeSIQzGLH7Hax4BsYvVjg10sWAunYrfQLupBmmdM4HpAsy7G7mXosKvMkXIst4+52ks4y+KUF0UXdTOztbr9j1KFqNyCvGQEExIW8xrM5tdkXncGjjIYuUWJ+nOgBwaqH2WRPJ03Rwg4pdW1FY2qXN1tXXJc70d3z5LUXJ0ZyZJXVrvfmUSbsY4Bf0Fxxzay29ZqKuawf4N6qtubzxSygFRUaZ9y83t1MlVM2H6L2ZkJKnw020WA9O3CTq7ie93KEy0K52IiomVQNaxocPvaeU0Ft/IVLVe7c6gLFZ87ZCihGiU/43WGNouF6fa0XWpviWXQrdlFCo35YbnEw9VNh4DJfpbI5Peelyt/z/vq23vqHc8EwzN9fPr2MZ9bPk+f/5jvo8fzv/9kx5OPE8O3t1P3YGdjel/taX/67Cv7y6aV0Q6je4xi2ipvL85jyHw5hP/+1NxyjrP7xynd8wdbVb0f5tX0Z/1/TS5h6TVWX/bcqi5v7ofCnF6epxv9YUX17Hn6/3A1O8vEk/R8MHM/ZR4vq7Nv9Pf2biDAdXx4BL7Rr8Ly8PM+qP714PQxn6FbfCHL+DZT5aP3z1Qk0Gn9FX7GX3/4XkE8LM1AmAAA= -->
