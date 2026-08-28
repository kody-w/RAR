---
name: "rar-cowork-cookbook-adaptive-card-consolidate-requisitions"
description: "Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_consolidate_requisitions", "rar_sha256": "88c1347cd1d0cc467fe355430134edd9840d97f7b8b60aebcbb83b0ed31d7eef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_consolidate_requisitions`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_consolidate_requisitions_agent.py` and in the RCI capsule.

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

Consolidate requisitions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 88c1347cd1d0cc46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_consolidate_requisitions_agent.py` first:

```bash
python3 adaptive_card_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_consolidate_requisitions_agent.py   # or on stdin
python3 adaptive_card_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_consolidate_requisitions',
    "version": '2.0.0',
    "display_name": 'Consolidate requisitions Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd39bbfe80f8d0c24',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardConsolidateRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConsolidateRequisitions'
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
    print(AdaptiveCardConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZObyLrmX9HU/eDuK7uEQGw+cSIGsWkBISEhEO0ON0uyiH0TS0//90kkVdm+ffrO6YmJGHkpAZlPvuvzvpnU7y9WUwdZ+fL55QisdCJacRwGoJxYqTthszYrI/gji2z4b+JkaV2GdlNnZfXy8cUFlVOGeR1mKZy+LzO3cUA1sSYlaCrLjsGEcS34+AYmrFW6k81R2U2q1MqrIKsnmTfiVVkculYN4JyiCatwBKsmVW3VTTXxsnICEhu4bpj6kzCduFYV2BnEqj7CB1YYw59wzAlYSfUKJQKdleQxqF4+//Lrx5cQfn/5/PuLE1sVvPXyJs0oDPttafW7lSFGbKU+HJz30CwpvM5BCeVI4C0XeJPn1U8ViL2Pk//8z6i1Sr/6+fOXdPL8fHkZ/6hNOqkDMKkzq6qBO3Gs3LLDOKz71wkTt1ZfQY3rpkxHe1XQqqn/+pj5DSnLJ/8cn/30WOTVB/VPX14yKII1Cvvl5edR+S8vZTN+fx1R8p9+fo2zFpQ//fwNp2rsK3DqEQxK/fr1ef2EhQO/DQ29+6r/hKgP79rgy8t3yo2fh9yjnnDmy+s1C9OfHsB5md1AaqUO+Onnv4J1AuBEcVjV/xbuLw/gAFgu1Okp+M8f70b+dTJ9KvSO+dfL5tCtf0cTOPxtuY+Tp6H+Cvtu//8CHYcpTIU3i/9LuH81YfrPyS9/qdt/N+HjxPvywoEYhnc5pt7nye9fj3ue/eWD++3mh1//gND/R5hj1pTOHeFrYqWhB6r669dfPlT32x9+/eVDk8NYgzn3tSnjf4X5r+x6X+cHCz5H/fTjXLi+lkZp1qaT90if/J7l/6P843VytmDKfrtffZ58ny/jZzoZlXhb9GGC73KmgrJ+Z8efX/6ANJFCbRrnkf+fX/7jPyZy6JRZlXn15OhkTT2BDq7DBIzCn4KwmsC/Y26XANq1Ckeie4yD8T96eJQYsttv/9O58+cn58mfM+tJQF8dyEBfv2O/r9+z32+vkxNEz8rQD1MrnqjMfv8ltXyQ1uPKeQkqUN4gp9h9DT5BNvo0fhnp8bd/b4Gvd6zXvP/tzvLhg6lUdj2yVNXE4HXUVA9A+tTLgYUBdMBp4DJx5kCZvBCy7EdoAbgApPd6tEoVhXE8ccMSmiAr+zs2tNznEey3336zIXd/SR+0ik0elaOawQHv4kw+fYLKeXHoB/WXFDhBNvnw+x8fJv9r8t/NuoOPa+whyz/9AiW8FxuYZ00Ch0GXQSdDErn75fc/niaGMCksddCLoReCx2QYpxFw3+x9XDGfUJyY2ADaGdo4ybOyvhej+nWy9ibv8sJFx0cjmwdZVU9ckIPUBanTQ1QLqvNuyRTWvgoGY+X1HydNBe6r/maX1l3EBCa8Vf82kdk9rB1ZDP8bxbwPgpOzNITmf4+Gx30IUn6oJss3iNfJbozMSW6VVh6U1nMNz3r4BdaMt+kQ3JqkoP2SjrUSjKa6p8nDPHAQtIzzdOmn0eewZCeQE9zqbe37GGuscKd7pSu/pNUzBaxydIUDSwJc1G9gHMLC8I9nSMEWoIndu/2gpCPS0wvu0yv3GGT/qkE4PhqEH/uLLw2KzBeT/++NyCg5I4oqLzInnpvwu5N6eVh0bKBGyz96LtgM3JHv2fOtQXijlzeW/ZLGIQyPsv/HY+TdD88xD+ZqSmg2lVHv+DAIoEVH3HuMjjFXlmN0W1/SNzr/CG1z5y7oJpjQMODHOHtbcHz6JmkAFR2vv5X2u0+hEWEUwDic5I0dwxjxAHBty4mgVOWYZ09fwIAFo4HbIHSCH7SaQHQYFxB/AoUIYeZAyr+bbpdBNaGZvTJLvg0Px4Ypf7jWncAOFbxOdJgqY7hUMD9h1zOOgVb4cIeaJADaGIr4buEqsPKHMGNT+xTQGn2RJaPjv/PA8+G34L7LMooPUSHJ1tCW7Ui5Lugenn2X8+krKGwypuN90o/ufuo6+b7u/ONLepfxneVhlsf3yP1mnAnMrqS60+pIUhUkmgQ8AwhGwr06vz4K7KOCv8vy+U+d/E9/r9m/l0ztR899ngR1nVefZ7NHmXurcq+QImYwRsIcVO8V79NYkD59l2afvk+zH9Afxvo8+XsS/gDxDO3Pk/kr8oqMj6TQAWPsPj/QIOyn5eXTYnz6JVXBN08/w2Gk2biHJfa95rwNgYXHL4E/Dn7UoGosXS2slnfShb74kr5HwzNXIKen/lgwq+y7HL4XX+jbh+veawN8lNZwbXds23ww7mviUfwKvHxOmzj++JJaCfi39zNjFYBRC00y7oVgBsFeqA7B/eq9LxovftzO3XMLkoKbfR5T7ONk7GE/Tt7b0Y+Ttw3CfeOVNnCH9MvYCo9LwqHwx/vY972iDV7gvqzu81H8x65n7MCenfGfhRgzC0oMybwaZXlL1XHFP4HAL74Pyj+DKPcvVvzkC0jpY50O67csr6CcLux6IJPfxuyDCQV5soET/rwMXOceuJBwR3W/2e+bWtlDlz/uZqgfW8ffX9544+mDZ5sIh8ME/VSNJXEGgxUuCK8fYQWf/V82kE8UyHewdYEwFOXMsQXpuHMXcZwFQXoAw/EFhsC7sKTR1AJxadIjbcomEAvYjm1TmI0AF5u7JAAexHuE6Nex+oejZKhlOZRDzhdwokU4AENszAFzFE7AAILTmEdRAIJ/mxpBsnyq+1BvtOV7Lzua5an17y82sYAjV4tqzTw+7Iw+W6S+sHedTZeE559Sem0XZzVJL4ah63ShVISlmjuxvprSITeS1SbZrtO5xfmm03QZd9jRIYcHKXrab06JF+VoFFJ66J9v0mEm9VQKdejx1UFl5VOsN+ejebL9Q9mZ9dZKoigtealF0BjV0i3bK7fl6RabTj6dTs8GXeSaZWrr4eTr5025StSrPK08we2n5pAmwY7K2lqXNp5ZZzUVb2Otqy64mMgxNSS2ohEIWq35ei87yziopxdqXrblAV9l+C4dKHKf5ii1vzVWas8pz8O5XsBvS2UequLiUlKdGLtSVQr9EJmwFVfYblB8c3bdXoylYcVLBusT1aFSCev4uXM0B/FEifz2Kpy35w3qpZumMxQzpLfb+GhGQ4vwMaFF+qJH9xu4CXIQzS0jPXdsXN9axy3RokWdKGpS0bvBj2ZnVCPiMtrzs7WyTljGSMD1xlLhVTGrjXawnP60nfo86yxWjZMJomcma3y3I4dWjqrK7XXzcFiWVFPFQZU7W3yx686EYdX5rkPitTYUfI4ugmOgDCR3AlWpsK4unoqgsf2pKJehiAj2plHEal9wx6mzKQqqKvKuKmdWVFTkuQBqfeE6iuvmx5zTedlRBaNDGOKWFsa13O/SDMcRbqPyfGPsJIzEpoFwrTH+HNC6GrlgV1alNPdy25RFpG5hPtZ4Jl9PWL+lENQKa+omc0MRZifGqjo34We7LKvQbdKrw/xMhKXooV2/Nq5KmvAS69Vm6Mg5vl8eu+tSKi6UT+E0bfTYpcsDVpraQ8fi8kzKWs2t8HW01g/VFB9IxlyHhOuqm2IeoVmZLtO8NUh5jxJ82l4kOkwX1r7lNWsaXxJf3huzC4xI9OzMBo5cLZTAqffknD9yG4qrdBIPlGMcXfbWNFVXPS1VurWJPP10yio3CxJO3J2oSszCg+jxVCLiaLVc7dgiInJktdrmVOdTKQDMao0GmMiVwvJSzmfLiNn6tnoW3VxY8dcabpqZhUqIR45gMl1iA1xz+kpJFUfZhARldrelZq+MobwNYontWGLTs2e168/qvD9fJepiR/2B3qR7fZgrebgYblla2FwrRWoWtMLtYs92VNDUttQd2ZwWBVXfUpi3RbtpupadrX/gyGp9jK0IXV23XSrGvuNaKsK0qWCfZGxwhOwypd2O4+a9rPKmsHRnKoNHJzYLtEXNzTG04fMOeGTDnGBkZxU5oxR1E8tnnChVSTaIulenXlGKCeLFu44psfVRXO2v1wGcrwmYL5XK15pgjQseMhP1q1pJjHqSefyggQCnjkcev5KJHjrNqeVndCgXbdllwZRKjJgNz8flauCxNdec1/rGPpXx0Hgnja7KUBhuElObsjC7qZtL7Se7lX4Zcj7ul+4qssJqKJOjzhdWkp97ExHBaXfaai6dxlmx3LjXbmaczRCF0Z9TV020CuMC9jTQUZ1eS2kr98UgXkOG5izjfLI39MasLXNOLgC2RHQKTJ09M9O5BDv5+E5W0l2wER0RcVOrYLySUeTksMXS9bZPC7nuZDsYjKoVq4vfq/jcxoNK87UI34/xKYtdSA25WlxQT6BoL8Avi7lj2MItNPty7zI5v7oIwpo5s6aT1cj05G3VChHLZdCslqUfLY+XcHchVqvzqdvcWDIJNsPxxhhdru669VW4hNY2tXhDJpFBFvlNddwWw7BbirxuUYutsFiQUtxxx+XZnqOpj+5KDt33sIjleLqNF9Dxrje7UbQyxJ2abJYSfXTYk7+4uZuNmoi3uY6jDb5RlkvLVQJ8f5pR+mG/Ja+FQh5kQdWuBHqeXQGrT4F0ItYpqu33pLNc5J7AQdqYg+nudIl8QWnXvYbUq3Qr98haas7FxpQLhmpruuTnCwISgLMURs2NTOIviWqLxqZQNznWLc9rlU9PYtAD5uKmgSwruJ922XydZ5Srrc+DNSx6i7ezm4IpWah0+8SV234/r8rzsTDbEIdw8e6wYYbpbNdtz/Mtfz6cl2BJqUzVNYhT9XXVl6pQOKnn59WO885zENOMzzK7aBqViX5G6rrumHCak66v84MlnvUNiQvk2Z1lWFCi1ApybLJF1YuHrM3jTjidtijYrBpudgvsKgM8K2zak2c26KFa60bFQEHNk9pf5b0i3dLtfL8iIx3ZtRtNbuRAX01zgmM8k8Hd6ITq+XDslgiXKDPicsQvxOHiF1RxqYGxFebHRSq1HG1JwoC3FLVba37iKTFPmFuNUdnIppYuc63kvEpAtegMAGmFCrieDfQ8WkbZ/KLnWpFebtsL7mCWyqwBW4CZ6a1pvJrzpu2IarG7MkdyG6dB0KHYXvSDW+gM/A0xpwdshpqh6ceIMNtbtXJoxNOVwISrhDRXIwqtIrbE1iN2ZYQL2dXFMppfHwIXLbXzaaAWpLA+bWxL2LYkEaq9h5jsCWyKdUsy54vZ2wfrhJ/b3XGoohN5OWq4Sh4kwUf8XJeELArZFW+o6rqulgcQdDxlMxxd4PR6lgTSkdsvsWmpzVCWmzlu7V6jSwPWLctWq9jWZYLggHs0zmdhGc9pcAxIksIBQG7LvvdzmZFD7nYQvBvKOyuVWBRp6lwwLFnl8dwpMGfe4LUlRa6S05LtEovWVJI9z7LXSz+76L7KHw+tthbJ062uV/rh6pvzgKrOh0TPvFDIptdw7kZ5fcKvMO73cy/Q3GmvFbidKHZLHeYlK0YXzRV6k71eAWYzfn4qVX2qIeUt3pq7YyHiblEXzHR5QZlWZacitqh9Q0N4BF+dtqA6CP2J3kbnZrU58eB4SYmoqA8bJWL2NlPFa7qP1wGtsuvl7haZclMT6XKDo4KOcFNDWBEy6lwUfK7dlJVVxdOWWHTEnNNVvpHlztgd3OYiqUkQ8MHOiEp/oR98LewLp9+GXi4r6lzD17ZI4iqNtRfYxq9ghzHN2na2zDWPL1bpOT5NU6VnahaQyrU6yWcNFG0kuQ4+4J0AtsrNldYekseHW7ecbxCp8bGL4q1SoHAWh+rd7dLdRF0Kty1fIbZtyQRbTvXjUbwmnjqPklQkWkJtOmUWHxDoCtv1YH3r2uWNrzlOngvrqxWL/FECPLr0W7UDmavtBSYpTTFEBVuFutW2AS2xdhnqjCPTQTrCFjdTq1lwpvcq0sYrgS2IPGRsLD8dNSbzj4h2GuKd75qbc53rMX5kwl4kAhbunznd5QuT2eAHJKdPfVyUtoUejOmMR8LVulSjDRaBBcy5/tIjShzIVMNcbVSJrqms9MYJFte8js9iLV+b2WXjsZrlk7nS9ZpKitTGHWoNJ3h5dbpqR0bbBidKK/Lr9rqdM/0y3jUki0irRjaB06YD7fmSzt0KEoV8uZsvPMvS/KiwZWW2MKMNetFpR4/0aZMlWLH15tphdhFFY0hiQlY4eq6LyTw9eJsp3IFK+CLapHSEd6rWHgwdO/WNoBrrggp6LpOXROuKzK13GLOR2JbQOy0zq6uYOKWRRASZwv2CX1SDGHFndUoVHgPYitjVZI8yWzUNDkmr7usKp/bLXNjyJG/GqS/vePF6A/y8ygqTVhnDPleJ2ai7lnARKV2pi4V1bAoJ3y353TE0FB3srsb+bOzZSMrMFX6kkR2hro7DNj1KjuRwV5pednupuCn1DLVSlx5ce53OrNWSdiPMaqh+RvpwF967g4PqO98UCWIo2PCQSDmW0KKszcSRymNDncs06jGE49uLHh/suF6sygrAfYa1rlh2Q6yv50OzxcNINbx+xgAkL/qVvSxX62KKrnyjc4kOOVd7zvZvKFD8KTsjiagOyOroFTQNVoyaOitb6W9IvCEN17wA5SoPVUHuQqY8bSgnsOcHl1wZsDxcI+DFtxlGsBjO1Ny2mu/J/Z5S9xtSpOcDZt/KfDkQB5LVFhHtF4uANDP+FuKEkLGJClDvEDsRqs0yg177vsDdpqapAobJEdShltxp0y1xVVns/EI5zIRYvqalhMtFbSg9Lm6XdmxH9uqAADpYlmvM3wZkPgAHIfs4qjaV4bBsMrA3QoTlvdS9VcxIR8PFNC/aL2hRIUi2yQWhEg23Dahm2jcFzs7kMt0jgV+0WrJH7LVXlaTdyuKByy0ps+MMvfGdhfWIPaSWMbXO092M6DrkijOGa2i0L178ENDX3KVWKrIyG69y5UCY02WHtELJs1bf2MkFvd1MYEwRc06hmQFWyXVIV86wx3GMJbzLpmGY26CV5wV/hAnZzFvhusNCVcFdVkrX4TlUyDidFs3CWAOOWbH1HsuMKs7Dc9w3adrslsqVAzCCN1xrSKAVanK3V3yDP06pUtLBdrqYthy+ENn6kAPe27dZhs/K5YIGt3bB8XvMBzkjsVhAejZbX/t2sWZa47Lc+aXkJigXHNZeLAvHalajfFHc7GhjLKamtzxqa4z3TLdJ6kghCdLkazTBfHKDI5ozKBxur+1Yxsr4hIhn9rIuB2JPiRQd326B0pQ2LlmYXbexlB0W0fS2XK5muyspXn1bFLm0m12uu0vD5Ao68xC6MUPECKvbUWecSvBRS60jsxJSi8BLbFMmt4tYorTAIgosg5mk4oA+iJTILVSc07ilYsznvotbde+KS4GZBleqTDTKWmvuKsOcqC+JPK1lkpOnCXYgsHDtEVaZogua6GfBbabaSjWlyKw1jHmPtWjIzDBvNcu1vcIY1ekiDLCcFLdZrAZkiKx35MZups1gCwa40s4RVVJ0tpzN4njYs5k93BacRcYlsW6NUL6xO/lwOvmFuw1v6n4wqGohCgYZ7laHnQHyM8VhwW0eWMtsvfH1vFxUnkd2Br8T67nteAGxmJ/ItX2r90DaFSgyu2yjTUHp2aGAWxsmQGRynzFiRmj8xTKbkNthinS4aphOl04cG/qURLWbvXI9WmdbMdieE5ebJfto6rbMQll1iDanj7xLReSwbBmWNFkglQdhc+WSTjgDbUpLVmQim4STq5QJqBy13S0XNXgsHbw95XOwgTl7NQksyVti5ZAtpapabezr7ciiIqqcjq49OAGZxm1nIdS1QakAbpYwToa+ZeMe7skspJjFR1bbo5I5bOp0ehOYlULgznLwV2ZfiUO9PJ7FKMQ5dnfNj8i+Fbr5EY9XUapbM5MT8JRurIxcKkRiDRfcBSqxnzH8maqSUNoeGObl48t4Av08R/6bb43HM73/Z0eLj1PAt3dL9yNkYLmf72t9/ruC/frxpXRCKNbjKLWKG/955PhfDlI//XvvJUaM/vFSdnwd1tVvB/C15Y+/Y/QSpm5T1WX/FU5v7ge6H1/sphp/1aH6+jy4frkrmOTjKfgPCn07G62zr7k12jVMx3c8wA2hJM9L/3nA/PHF7aG/Qqf6ihH4V1Dmo7rPNx3jiez4quPlj/8N05lpc9AlAAA= -->
