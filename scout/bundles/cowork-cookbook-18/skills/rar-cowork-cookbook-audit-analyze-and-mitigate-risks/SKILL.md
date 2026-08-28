---
name: "rar-cowork-cookbook-audit-analyze-and-mitigate-risks"
description: "Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_and_mitigate_risks", "rar_sha256": "34177c159d8f4aef5893ae051360b7c0f4e4df47c25605548aec757971de523d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_and_mitigate_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_and_mitigate_risks_agent.py` and in the RCI capsule.

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

Analyze and mitigate risks Completeness Audit — Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_and_mitigate_risks_agent.py` and embedded as the fenced Python below (sha256 34177c159d8f4aef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_and_mitigate_risks_agent.py` first:

```bash
python3 audit_analyze_and_mitigate_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_and_mitigate_risks_agent.py   # or on stdin
python3 audit_analyze_and_mitigate_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and mitigate risks Completeness Audit — Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_and_mitigate_risks',
    "version": '2.0.1',
    "display_name": 'Analyze and mitigate risks Completeness Audit',
    "description": 'Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-and-mitigate-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f56d347112895c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/analyze-and-mitigate-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-analyze-and-mitigate-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditAnalyzeAndMitigateRisks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAndMitigateRisks'
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
    print(AuditAnalyzeAndMitigateRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+bPiRrbmv8Lc94PtR9VFQivV0RGjDUkIEEgCLS5HWbsE2nfJ4/99UkBV2a/br19HTAxV94JQ5snvbN85mbq/vdltE+XV26c31bezBW8nSRz51cLOvAWT93l1B2/53QE/CzfPmip22iav6rcPb55fu1VcNHGegelU68VNDebZyTj5j/lp3MSh3fiLKq7v9aLy3bzy6kWQV0BUWiR+42d+XT/GFnkSu+Pz+9jOXCAhtOOsbhZVm/gfHbv2vYUb+e69fgdr+4M9C6jfPv38y4e3GHx++/Tbm5vYdf0VC/VEQmXe4YVDmWGAyYmdhWBUMQLNM3Bd+BXAlIKvPD9YvK5+rP0k+LD4z/+893YV1j99+pwtXq/Pb/M/pc0WTeQvmtyumxmcXdhOnMTN+L6gkt4eZ42btsqAgosaGC4L358zv0vKi8Xf53s/Phd5D/3mx89vOYBgz2b9/PbTAhjr81vVzp/fZynFjz+9J3nvVz/+9F1O3To3321mYQD1+5fX9UssGPh9aBw8Vv07kPp0oON/fvuDcvPriXvWE8x8e7/lcfbjU3BR5Z2fzf758ae/EvvwUhLXzf9I7s9PwZFve0CnF/CfPjyM/Mti+VLom8y/XrYAbv13NAHDvy73YfEy1F/Jftj/v4hOYhC83yz+T8X9swnLvy9+/kvd/rsJHxbB5zfWT+IORIeT+J8Wv31RTxzz8w/e9y9/+OV3IPpfilHztnIfEr6kdhYHft18+fLzD/Xj6x9++fmHtgCx5tvpl7ZK/pnMf2bXxzp/suBr1I9/ngvWv2T3LO+zxbdIX/yWF/+r+v19cbWT2Pv+ff1p8cd8mV/LxazE10WfJvhDztQA6x/s+NPb74AfAI9Urfu4DbL8P/5jcYjdKq/zoFmobt7OJJM1cerP4LUorhfg/5zblQ/sWsfAsK9xIP5nD8+I82Dx6/92HxT50X1R5MqemefLiwTBu/flKwl+eZDgr+8LDcjNqziMwaCFQp1OnzM79LNmXrOo/NqvOsAmztj4HwEPfZw/LOJs8eu/Ev3lIeW9GH99EGr8ZCeFEWdmqgGJvs/a6ZGfvXRxAd/7g++2YIEkdwGaIAaU+gFoXedJB5httkR9j5Nk4cWAvQHvjw/ZwFqfZmG//vorIOboc/akUmTxLAj1Cgz4Bmfx8SNQK0jiMGo+Z74b5Ysffvv9h8X/Wfx3sx7C5zVOgNJfvgAId6p8XIDcalMwDLgJOBYQx8MXv/3+Mi4Qk4EKBjwXB7H/nAxi8+57Xy2tCtTHNYYvHB9YGFg3LfKqAfy8iJv3hRgsvuEFi863ZgaPclCLPL/wM8/PQKVqIhuo882SWd4sahCAdTB+WLS1/1j1V6d61DA/BUluN78uDswJ1Is8Ab9mmI9BYHKexcD83+Lg+T0QUv1QL+ivIt4XxzkaF4Vd2UVU2a81AvvpF1Anvk4Hwu1F5vefs7kw+rOpHqnxNA8YBCzjvlz6cfb5XHYBD3j117UfY+y5qmmP6lZ9zupX2NuV/6jkAMq4CNvYm4vB314hVUd5m3gP+wGks6SXF7yXVx4xSP11j8D8sS94lPHF53YNweji/2N/8cDI8wrHUxrHLrijpphP280d0GzjZ9MESv1jsUeefC//X8njK4d+zpIYBEI1/u058mHx15gnL7UVWFyhlId8gArYbpb7iMY5uqpqjmP7c/aVrD8ABz+YCTgEpC4I7Tmivi443/2KNAL5OV9/L9wvO81WARG3KFoHWGYR+L7n2O4doKrmjHpZHYSmP2dXH8Vu9CetFkA6iAAgfwFAzK4BhP4w3TEHaoJkCqo8/T48nh0EUHitC9CCFtN/X+ggKebAqEEmgp5mHgOs8MND1CL1gY0BxG8WriO7eIKZu9IXQHvm6Njv/2j/163vQfxAMoMHMm3PboAl+5lUPX94+vUbypengNB0jo7HpD87+6Xp4o815W+fswfCbzwOsjmZy/EfTLMAWZQ+Y3EmoxoQSuq/wgfEwaPyvj+L57M6f8Py6R8a8R//vV79UQ4vf/bbp0XUNEX9abV6lrCvFewdZMgKREhc+PWzmn18pRx49z5+TbmPj5T7k9ynmT4t/j1sfxLxCulPC/gdeofmW/vY9eeYfb2AKZiPtPkRne9+zhT/u4/B8nkKaG42/QjK57eq8nUIKC1h5c/gvWeVqefi1IN6+KBV4IXP2bc4eOUIYO0snEtinf8hdx/lFXj16bRv7A9uZQ1Y25ubsdCftynJDL/23z5lbZJ8eMvs1P/X25OZ4EGgAlvMexqQMqC1aWL/cQV0Ajdie/785/2X/PhgJ8+ArhsA0q4etPBKkBfffZj72gxQyryHmKvYk/HBzsduk2YG3YzFjPK5ZZnbp2+91T+u+shgsIaXf5oT+cNi7oM/LL61tB8WXzcZj11b1oJd1s9zOz3rCYaCt29jv20pHf/tl38C49Vd/wWIeCaRmXae6vred4Z4OK2wG0CEF2UPIOXuo3+Ya2Y9PmrrP6oNFqz8sgVF0pshf7fBd2j5E8/vD1Wa5xbyt7evHPNy3qtdBMNBMn+s5zK5AuENFgTXz0AE9/7tRvI1H3AiaGSAAASFCcKFsY1HBqjtBxi5QWwfwmAEhxzChQLUR70AJVwwHMIwlLR9l8CIDQF7PrZGPCDvGc5f5l4gnjH5UOAjG3jtegi+BlM2MLG2N56NErbtQSRJQETggbLxfeodUOpL0adisxW/9bSzQV76/vbm4CgYKaC1SD1fzGpztVfI3hkiYZlBm0EJ0DCxmJBwld0Z9r1RBFUwttaHaq9pnBPlDN3vDiRDBaF8OMD5cScLI31K1aBqkAgSw73qHnkY7DS4inFuznpTBwiCExZNcSFxIKfMXKmKkJVenKslEqth2Uz7i4KRejrx58RdpwdZarSrmQTBitiuUrtHLchpLr2UKeWw3yvi+r7LnWtyl5rMwsZK5qDIHNQcSTwa3sX+fn2ILju+tYxd0x/YiCBbbUTrzAK/usE1pgRzV5G8T/R0N7F5eo3lpjT06EoEcW6X64Mqi6NRxoes5Tsm7yooUeyhaOgiMnG4agSv3aqWJ3a9KeKlXh7v4+q0T+7kdSfZg52XW46smKNlq94Q1WIyNZaa8nljdjvBLhnR0K2tayLe9XgIFB1fZfLNqpZVdxmU1iJxvbm5YUxNY7edGEnnSmvf7u/8raDPdaVPeePGqVg0aXut2A7hLKb2RsU5U9tRdYSj6ewz2seNilTULdZtzPu17YOkyC7sqfHO4/a47Exihzu1wli1rsMti58H836MpLV29o+mC+H7EkojB0thfScG0unepPDkVzhTT3osOpfyfkDP29IbtufluhZSf6wC/YbC6+l2ObfS1kRZ2MOIimDM/AK4/OBE6FHfH1FFs1Jk7VmdSDublXlOvLPDI7E1RryDr8Wb4WgUAekN16cOE/BMsIYuqSrgS3ufKQa/6U8rDhf1g7viOGWMzNtorBOMIZprdbnawpHRlSW8Mi6aNFblTZ1wTYtuZuZsR9Eo8lC4XvLppqbELsYxkpW9pazariDBwzXfT67WQXjf9KbRacf+RKAGQspWlVxCSVu5wSRQSz+YWIyWSWE7SZ3uDd6e30kAIoJmW62IuJIQxwtBgq2bW+0vWXfkRSF1WFc0q4HPfXUD7LuBoXYn16gB3acoaWzpUhmi7tkGKQj+Fbv0LX01WiG/coLL3NADxdusdNrv+IsRX4/9AaclmrKGGk2plIrWBmZq19Tf870XL6elfByOXbTdmB23JE0cnUT5fFhBZEiI613G7iDKgmyVPDN8Jy+DgiwvujPuVxS/Yta9I3p7G46QPkCVoEL542GqyA2k2wi82kroybtC8j0I1wEx7jSLvXo2G+o9dG220t0AgtWVpGRL4apdO8VxQFJGVXzUeBEFTBzzOx0pi0nVcVNKVt6qGuiNlkl4uNxezVI6nRDIVMECGIRHtNwYkUcoybUg+PwawBMf6ddzMXo+32gWfIu9ZWjZnY3rSaxryyhF1w4yXNWadrKSVqHTKWTQEpXsseSKmg+vHR4G8Vo629Fy51fbLV/eKeHaDSyuUkCP9GZU+l5uURJNLMrUmpCvCwrL3DLdrFKJG01tExfcMJbTIfLhMRGZEVYrC2SvJXNkuBLXvt5Tx316wMYNvHcDwkOsTbHdVSWHMux5ZSyvWj64ayVxDNmWOS89Zj4mQ1pqDz4oFQjlZ8rkkysSkNBmKwx7awh7HurGMMJujn4cNv2NgFJeL4tbdo8US96CLShyrnpLH+MtZ1R7m1W3tLcbg5h0Vww9MbbVXyQ3ONS4252XFtVFO8BF6MV3bODrikp2DE+XA+dgVHzquSrgk+xgbJP7sDQKnuaiU34+cvDWKUvIUmJ/JzLSUZLWTLopXQmPEZq/1hfT2EaXUFGPEDmpGr3l41Zt3eO6x5z+Em1MybNC2pFQz4ZWsnzB/X21jQ64TWgVtvSNaVi5Fy4+WxcpR1gDMcg00ZUL6dXxfjIFLke57RXG8cYXqn4KccJJ1gyKXkSF7LIJtYNq2GErr1utwgojVxqLTaEvrukzIpM1jmxNl6vF+3nL3Q+Og0uH8bATm+tYWiJOEdqR7ThIJCaYUjy6xBKUveHSEWtxsfT4Qkj2hpjdL4Ra9x66qwWPWfONkp2pJXS/KqnKXWlqVd7x0jxIt5NOtrlDD97xgtCiI8XZ6aYe3G3CeDsEmmrVrbFlcWFAsKMnC4cYdINdW0ycrGTJpN25QdfFseoJyNdI8yyWdOuO8HiTcPgA9aHpS5PF7KPhxohhu8RJw1F4R2ePuH6dAjal7t16uPA3mPIuherHaX3BjRbB9ZWAhqgSdwqeOfBpiAYVkCIoK7h+v3AiLFoGjkTW0mI3oXTfENs9rUXNVPF+YSbU+sDth8QTexMV0Xo53T0VgW81HbHibWh0WMlXHMO4/Y4SR3etlkIA1wzrUI7fm2UiSWE0MhOt1bsla6B5FpZ1dZPvhK5FY9hdhEhKzK3YlbewhXaHk8VbceTucsY1W5TYe+bN8SxB4bTtyPUuql4nJfaCVibt7U1Mvfii19B1eW43ay81YTqYTkMRb4fRK6+Ia/naTvWla2HvmZpeTj6uR/pu8HqZDg9iFmx9OmGF+tocznh01P1IOkmWYK2Uu0hvXUvV/fzcHXaniqv6isJB2baZnXnPDC6o5bq36cv+frlIBhNKdG6lKhKJW210zZO1W7XwhiYbRr9vdfa2kYXJCk9I0d1ql+Wn/kqBlEWiHIJv6+UdFK9ENsS9oPrtjQgAgXgStKGgWPIiIr51KlR1MOsKCr7O+Mq9InV90vf4uPc0x9I26e7ueXu5CX2vutBZPIQ0hJTLrOdEKlnmFM9vsKJ2LFVOEldYcnyqmHRXGlosGtlAuBf0OLGsnvOQf1+PK81KSt4ptiyjJbcwuqnlZbxclcpcOxPapkYTV9m5wrarRr6EAPeYWj1bl7mr1CNnX0bP0CEXvzfXHe2pbHsNcUuVfNUt2KvMDqrKCSlT5HSY2/s2sLIdLfMnj6XD8ajsbknK0i4sqCycK8s1Wtxxx3D6Oy1TY5A7fb4ymRW1hxm6YhsiPPq3XiPgcXQQDjdgZMQp1a92KbnmTd4NQ9QNCpU737N0A+0FWLLuQwbH5rm2Du7kjKgfx/TOamEnSXanjs12t+2xOyYK6W9OxaWCPBSOsjNPDj7s2jEctzd72pVF2F0xTd0Mt/sBRrJtumkEUq5GlXUbg1k1GLNmQEQhVcyE1nGQC8NBtcBla9vSQIrvoc1t8g/ZEdsNmgebJWOM7JAuMdt0sFg3QGd3W+9C+LAy4q018Jfs7hd8aFtcaniO5GwM2jgr136/x4mVUByga9FJtH7WeFMw1hgj3VSR9ULZ4QUatowaUPmppA2ocTzBtEjYUvwiIXG37dqVvF4hk1o5NO9f950ykL1Rg5ZaO/Euz8OnWHa5UzdGyjrh185WNHXn7oCqFNjaMXZPGgkZ+Khc1AtUBrJhmhRcJ4xPKYcpgUrWWuHonmcleF3sVDHe0i6mcaooxuestAwJ2wW2qnElp2E3U5M4fIjDpDC3cXMyj812690l7S6p1yLqLhlW3nSOLddVfckZCPaM1FW6kBU5PBkUIl6u2nXs2u0tOEdseTaPyxu1iUP9frrzRwTVLELfSlOLufbl2OFmWatbUHiv7N7icyG86+2I8pzAhmunMs+37W0yz25fwAzpRREF4K+k6ryUhLNR0WFzuIWot5Mv0aGx3XO018jkdGlt6FhwwrUxrlrvwlXkwna8tJwxOdgFGQ/qdHLlRIO5jiW7nV7YvL6l+9IUL158KKoJMFrAJYQT0vD12IxUNwXXYmsLlzuEkMFWC9PBRDfJ4XhnNm1MKoeScEyZxDXhZoLJnWrlmGoMDNjEjftGSskzvXOXm/GyvavLOIkIqoQgDcHbm2iu5FviYNfk2l1XWmTY+ZFeLktycr1tywpOjoRu4MEOctOFFva860peTjXBESd/aGxidUN5vVetY4EMykr2xxt95M7NGrTuS0Pk7BvYJhAnNaM2d6TfOLvV+iJuVhpVhx6P2o4vsK3tKqhQuPph6DY3se3QFegJKdBOs/p+4GLAiXilc6axtnwblbPlnaB7jAxs0d1M530LEoCXwyBSIa8hWpHIeLLZ7tbcXeYJzZNY0mqPTgjDm+Vw2/TduSduQTdpK76jz6D3MoneWK+UprjrO5o5dYVJ4PUAesR6f47ivJPPslTRG6Fb8m5x5zrVodHuUARBv67rHbunNzRGpdixj+Rzt8tkrSoc7rAkD4QVmo0i6qW3JnwWqQ/yUMIJS9PrDSLZDabcIMbZEnSjWlFG7tUVxyqnqRxwfFpvNhK2X578OGj7idyFDr5UoTHcB14TXccQKxBdKbujdOtKJ7YFQl6eXDZO+iytCRyzj1lR6hHp8SEmJ6ukCaZgWXu+2Gsd1bhWr4lnJXBCzAlo1QPFMkP2GnXeGDbpHa4Wfxj5cat7oIvuMixIo4sP4UQvZs6GwW8JYnUmucFAJ8P1mqsFQqtrlCGgaWWpLMfqBKeVoj7mqclu8GF17YL6vqfu2qXWNmsezR2xwuTKpDRy8MQNpIzYhWdklg+1DVwbxX3HZBhsqcRUyXlA+bam7s1jF9sierHdFdwF7ckIz1EpbCKz2lO1WsMooaFwyCnoGWZPsMcoztrb3ZAzasDO6F/2ELYR2pNu9NeMAUOWzKFfQ2skENwEa8XUNSxZj5P02juTr9V52m9G9haD3SLtG+d9fEqWloA6Vc63WkriS9PqBk6WDkh31lsZ3RIQhg9tTpB7F2zHCd4ymOUKj4No9KchPRHns35hkMpRutbvjtnZbmRCajfHeiBjr0TEw/FspxrnGsaF6YwE2x36DUXpxuYICcsuIoL1kaPk621JgViSQsXNxNHnlrEAthOSAY9oFyMnn+NJkz0jGXmO8jpw5GZp66zu8M1KyYzs1C0b6sjv2VVHunwTkCgFaJI/BUY8wh0ss04gbXbc6GoskZqoV97g+NpUsL+ihG5DKpv2uqGIYDC6vI3QEBSpjtlyZzZLpNtanBKEdYnb3bmKugh5B0TeOvf9FiHtNLQZ9SKUeCsJwoBeFD4/2usWNbHTtV4Pe2qyqm2RU218vzfm1Ve2nE/mlB4RFkmdEDqLJI4HsbPXq3C01K7BMHeZVc6UoDjRnBE37CxxHH0oWJvtNMJUUqOBsLsY24OGxEEnCwdqLzBbV1AjSWMFdpRLMupgK9lr+XQULEuib9i1cTbS7d4QOz0nfOyMg4ZuXCLiRtmQbJCVEGPIFqJWdFBjFVy7aYoj9JIRTlM7IiKZtGs3bPjAYA8VcmSS0YqHC6ys7jp7OUHTlKh4sMbSkzsUSX8SqMDeh6vMNxI6zvmIPNe0jEw40y1jVcrJGJu0pVwH+VQJMujcp1bLElh2rqPPBgNTawpOFhRF/f3tw9t8qPo6z/4fP5meTwr/nx1YPs8Wvz7Vehwr+7b36bHWp/85pF8+vFVuDAA9D2XrpA1fR5j/5Uj24796GjLPHp8Pe+eHb0Pz9di/scP5D5Xe4sxr66Yav9R50j4OhT+8OW09/9lEPf9ljQve3x5KpcV8Gv5YcDZ1XvmuXTdfmvzL69A8zubHSb4Xg9Vfl+HrfPrDmzcCx8Ru/QXBsS9+Vcw6vh6tANXW79A7/Pb7/wWO7iUm+iUAAA== -->
