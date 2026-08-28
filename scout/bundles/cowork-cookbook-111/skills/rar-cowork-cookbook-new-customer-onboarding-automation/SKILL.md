---
name: "rar-cowork-cookbook-new-customer-onboarding-automation"
description: "Close a new customer and trigger the full onboarding sequence in one prompt."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/new_customer_onboarding_automation", "rar_sha256": "203da81b0f7baff78fbea9bdb279c2f76e9b513e9de554acc57cc679edeb642e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/new_customer_onboarding_automation`. The original RAPP
agent is preserved byte-for-byte in `new_customer_onboarding_automation_agent.py` and in the RCI capsule.

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

New customer onboarding automation — Close a new customer and trigger the full onboarding sequence in one prompt.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `new_customer_onboarding_automation_agent.py` and embedded as the fenced Python below (sha256 203da81b0f7baff7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `new_customer_onboarding_automation_agent.py` first:

```bash
python3 new_customer_onboarding_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 new_customer_onboarding_automation_agent.py   # or on stdin
python3 new_customer_onboarding_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
New customer onboarding automation — Close a new customer and trigger the full onboarding sequence in one prompt.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/new_customer_onboarding_automation',
    "version": '2.0.1',
    "display_name": 'New customer onboarding automation',
    "description": 'Close a new customer and trigger the full onboarding sequence in one prompt.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'new-customer-onboarding-automation',
        "upstream_url": 'https://coworkcookbook.com/recipes/new-customer-onboarding-automation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '618b1e2db4f33a0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/new-customer-onboarding-automation', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['word:trigger'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class NewCustomerOnboardingAutomation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'NewCustomerOnboardingAutomation'
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
    print(NewCustomerOnboardingAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616aZebWJL2X9HkfLBrZCcCBAL36XNesQiQAC0gEJTruNhB7Duopv77XCRl2jXVPT31npGXFBA39ngi7iV/e7HaJsyrly8vimdlM85Kkij0qpmVuTM67/MqBj/y2Ab/Zk6eNVVkt01e1S+fXlyvdqqoaKI8A8vpJK+9mTXLvH7mtHWTp08uYEkQgO9N6M38NklmeWbnVuVGWTCrvbL1MsebRRm47c2KKk+L5hUw9wYrLRKvfvny8y+fXiLw/eXLby9OYtXg1ovs9fRTxv6d2xoollp3dT69JFYWAMJiBNZN14VX+XmVgluu58+eVx9rL/E/zf7jP+LeqoL6py9fs9nz8/Vl+nNqs7veTW7VjefOHKuw7CiJmvF1tk56a6xnlde0VVYDy2tgaRa8PlZ+55QXs79Pzz4+hLwGXvPx60sOVLjr+vXlp1leAXlVO31/nbgUH396TfLeqz7+9J1P3dpXz2kmZkDr12/P6ydbQPidNPLvUv8OuD6CZHtfX34wbvo89J7sBCtfXq95lH18MAZB6LzMAmH5+NM/Y+uEnhMnUd38r/j+/GAcepYLbHoq/tOnu5N/mc2fBr3z/OdiCxDWv2IJIH8T92n2dNQ/4333/39jnUSZV797/B+y+0cL5n+f/fxPbfufFnya+V9fGC+JOpAdduJ9mf32TTmw9M8f3O83P/zyO2D9L9koeVs5dw7fUiuLfK9uvn37+UN9v/3hl58/tAXINc9Kv7VV8o94/iO/3uX8wYNPqo9/XAvkn7M4y3tQ12+ZPvstL/6t+v11pllJ5H6/X3+Z/Vgv02c+m4x4E/pwwQ81UwNdf/DjTy+/A4jIgDWtc38Mqvzf/30mRU6V17nfzBQnb5sZCHATpd6kvBpG9Qz8nWq78oBf6wg49kkH8n+K8KRx7s9+/X/OHQY/O08YhADCfXtDuG/fweyb9Y4/v77OVMA5B8gXZVYyO60Ph6+ZFXhZM0ktKq/2qg7giT023meARJ+nLxMI/vqvmX+783ktxl/v8Bo9EOpECxM61W3ivU4W6qGXPe1xAK57g+e0QESSO0AfPwLI+glYXudJB9Bt8kYdRwCb3agCpufVeOcNPPZlYvbrr7/aVh1+zR5wis4ewF9DgOBdndnnz8AwP4mCsPmaeU6Yzz789vuH2X/O/qdVd+aTjANA9mc8gIZbZS/PQH21KSADoQLBBeBxj8dvvz/dC9hkoK+A6EV+5D0Wg/yMPffN1wq//oxg+Mz2gI+Bf9Mir5qp70TN60zwZ+/6AqHTownFw7xuZq5XeJkLOtMIuFrAnHdPZnkzq0Ecan/8NGtr7y71V7uy7iqmoNCt5teZRB9Az8gT8N+k5p0ILM6zCLj/PRMe9wGT6kM9o95YvM7kKSNnhVVZRVhZTxm+9YgL6BVvywHze7/9mk390Ztcdc+Qh3sAEfCM8wzp5ynmoIOnAAvc+k32ncaaOpt673DV16x+pr5VTaFwQCsAQoM2cqeG8LdnStVh3ibu3X/Pzv6MgvuMyj0H5R9HgR+6/vdcnn1tkQW8nP1fDg+T5DXHnVhurbLMjJXVk/HwyDS/TJ57jDygic9AWjyy/3tjf4OFN3T8miURCG81/u1Beffjk+aBOG0FzD6tT3f+IIhA3YnvPcemnKmqKTutr9kbDH8Clt4xBzgAFCRI2ClP3gROT980DUHVTdffW/I9JpU7OQfk0axo7QTE2Pc817acGGhVTXXydGs2uQXUTB9GTvgHq2aAO4gr4A9cB1QFP/rsEbQcmAm86wNvfiePpkEHaOG2DtAWDIje60wHqT6Fuwb1BaaViQZ44cOd1Sz1gI+Biu8erkOreCgzzZRPBa23XPB+jMDz4ffkvOsyqQ+4Wq7VAF/2U9hdb3hE9l3PZ6yAsulUTvdFfwz309bZj/3ib1+zu47vCA2qNJla7Q/OmYHqSOt7Uk4gUwOgSL1nAoFMuHfV10djfHTed12+/GmQ/vjXZu17qzv/MXJfZmHTFPUXCHq0p7fu9ApKHAI5EhVePXWqz2/l9Pl75Xz+XoB/4Pxw1JfZX9PuDyyeaf1lBr8uXhfTIzFy7kX6/ABn0J8p4/Nyevo1O3nfo/ym1eT8EbTG937xRgKaRlB5wUT86B/11HZ60OnugAni8DV7z4RnnQA8zoKp2dX5D/V7b5wgro+wveM6eJQ1QLY7jVqBN+1Dkkn92nv5kgH0+fSSWan3v9p/TOgNshW4Y9q3gMoBs0sTefer9zlmuvjjLupeUwAM3PzLVFqfZtPM+Wn2Pj5+mr0N9PdNUtaCHc3P0+g6iQSk4Mc77fsWzfZewB6qGYtJ9ccuZZqYnpPsn5WYKgpo7HhTR87fS3SS+CcmT4D+M5P9/YuVPHGibqypv0bNW3XXQE8XTCufZiB4oOpAIQF8bMGCP4sBcioA9qCRuZO53/333az8Ycvvdzc0j63eby9vePGMwXOsA+SgMD/XUyuDQKICgeD6kVLg2f/HwPfkADAOjBuABbJAXYuA7YW/si3fXxG+7Vmk7drIinQQf4V7pI3BqEe6HoYtLcfBVo6Dr0jP9Wx8iXiA3yM1v00dO5q08ha+h5Iw4rgojoBFJLxCLNK1livLchcEsVqsfBe0ge9LYwCQT1Mfpk1+fJ89J5c8Lf7tBQgFlPyyFtaPDw2RmoWjoi2H9rzC/XV9JeNm2GmFjO6vleiVXo1bumXJezluSHmQlUEIwm0ZpevtIq/0JRbPT9t5r65EvzfO6M50ERclFkvSGNen3smkBu0CqaQFcUuvNlfFkqvmdNbOC732tpedUcPLYOERSVkEHYSOu1UnJCdLqnEByk5OUY4tdmnlW3diawvaEeJiL2ZDc9oCfuuc2OzGFha9ppeuCTTv1JJoMwwn2g7Z6yIM+3447+Ek8sqS1U4L0rA1J8Fvt+0mKLWUVkhM5GU8rMi8wu2zq1yWbiGK7V7UoIpzUylx5nRqLOgTfF6m54sJ+5y/cTYNrQ1SjpsSWdK7ZblT1Ws8LjqTNhcHRyrshZ7gnoIpKd63id24V7Uk3aHvLA5yrME+X9a4RZ8VzdLidJ16Msq2LGZsY8cgWmOzj7dryxnMmCn0AT0baUpsMI4+XTxMkOPFRoTkXJPkWAz9A1WESY2wKKcoLQW5UhqYSxssOfq2H8pWax0r2cC4gndQhihPPNsEO0RVvMbwdS6BDVVzFwZsh2jnhXZ2tvV1bTMEeSyPWsHwLIndFGflZEKJJuGh6XIMWzBb8Tx0qLpdVLc61JIG7b0bTjhqPjRubHoH8rB3Bl5uzFDWIyTN1cCOa/uq2gK9dTuJuZVlrKyteiDrgrApzayDJrlmZQiziASR1+2OYEUyPNmjgIi4z56dLEgMLEoWpXecO/Owwsz6THrJJVrqkZYaLa+BfmaIJ+EIFFoGjmfMHc90r/W4OuxrsbmaYOidZzo8p+k5m3hDMKcpMsCo1kw3wwJCaCGC0gtKEFA/Z2IlU+bABaeF79Tode9q4q4mne0h8kP8YsSwauBShJ6MVchvORGHjwxVQB40Cm7WGxG6YIRVUSixG5JD0R3P3Wapl6ljHs/6odJY0eGSpbTe7NXdQdhy8aW+yrCMUzSlXi2h4phtkJcXzB3zmqC3ARa7IhTqBq/ioX+RULHlUGqDuQvF3ePintekrA9TpWBGeneCcAzPzqazQmMXiqAzY1WhqhfsqoSGrQWdDMSPr/hqWQfdapVaS1SDYSmWNaUki43u6dKht8whX3JXPfYN2dl0XmpoOUusdwmHnVb5WTmh2q4rMZAqQXgbya11knD1QAnGCODOqRpkTpebsrLiuYWgV7E755CMjcfdrkyktcs4KWKvY4gI13kam5djrISt4ruaNceU9bbcUUx4uC2lbrcxdMl1xvrIOu0u9mvTaRLBr09L/3ZW8lML6Qd6k7OOpulsxEID19tYTspsRMeZvW5Mmk8pVC/wqyDviVsWyVBMlTvstkOldrvBlJi+aNctU9mn0L4K7Ni0fTNibT0whwvsySmvXd1sGZ+RNj964YGZ+xhLYZuh4EzVvKgD7weXy/zULOYxgZgyTi4PQexdOhS6MAvfzIdu4TS3tXkhFRV0y+qyIIxwaW6HeIwJj4itrdBXaNyVqX/R1vhxr2hne0w2QnSM+g7BfEdKsTBWtVO5bG2sJr3QULl5XBTlHvdjXRGjnj+fj+GcyJs8Uv2lzB+8BDGuYXOGB34r0GzClz1Moxtbb+rCuM5p4SA13A6JU0nmKLlsepVO0tseoqlkXYU6rmALmkuaG1GhjN+0OiELZ7hGdwalpi2vGq0YaPXFsVYRZcIw4SC3iKgv1bhsjOK0U7ABhggvjvPR6mBug4SYsKe2uruPNtkAzQuKnZM3lGcCjhZa9Raic5FfFrzlDybZphnE8um6Pjdgl7iQlc6HaSMO2HkvjOex4TPaGZHApMubSpsyk4U2E7M3bIyoQxOtszCEgmO5jnVYjRfSdVHlWRmro2LmyNa1i2CbBHu8PJedfjZkjCHtQXf6TivJJVEGNl+McG/HieMYy7xeQqAZS2uDRZyNepjaA5GmTkkNiCvj+sk+SxmRUwe80jc9qKE5KcbKxrWQ/Nh4Njwcx/3mEBwpgb0yaldw2DV2VxxWaotBho11VOYr2bMJpmwOiwQBehbOrmdJ6KIIpQMVoI02R6NWrF0WbBt4tzmyG35pIcrV1q8kwcB4iEF665uayXG3oVCMotAPu4b0eTj2mKNwCuB9S154PVesYEAoX2SzOt/JbK9wW+cUUI3uSVnMHQ7MZsetjhh+YjdEmBppBigxJNlzmEOf5e1ZU0J2dxyKxDQEk7q5wS3p9qnCmHs+HcMznexSY3/rrNLW6BIh5CHqtWXSC0mAhbkDY0wjR2UmqoFCn+qlYhksu7zUXHUynP2VAQGoYj4Z41t9Y/2enbctJvfIVrlZrVrZiNTcktZSil3ZmQUGQY170co4kpbockzPTL4A2W3t/dwWCEsS4wZAwU2cZ6e9ipgR4213XIfwLHwRG1o/aPy6k9pynRBoXPbXNriImyulxDabx9G6OV+U6GSuqKMSkfVgBuqqxUhhnobMkQm37pw/4sjI3/RG36nREfH0gC2Wh10bDTVsklbcRpmYbYqAaCj0gs0ht0AWir88o+qB5fU4vFjzzZKKFrEoe8lw7WpfETkw2WCrdkPo29i1Ssc+QpYiGAh7ZWmrUyJrFZsCgIVApE4V0uLnCGETnSd6bacZVDweioGtYMy7JHQn7TRpQ2F7n2/EuV7lCaEjCn5Mqg0nxvmyOvc8j8xrIW+3LskYm6veepF5w5GmBLmeLNXlWpSoK+0Scrc9BerNUFXWlYrdwF+2PJxSnInscsEh0INWsPZ6f9kG+iiYuL+j2I1iqXNBdhoxlbMLU4j7niYin7POUL00hsUi2/CuxyWGCGONeq6MeAHL5rFb05oZrJzjUj6m23C7rMNY0NZBGa+jorckJnb1/egNocfynVWHQqAKZ5Tk4BUv4SJ1MxYFqiZGWQssmZlIoQtdCcdXxUnQHt2UbAMVux3Imn0oC8lwSqnsuvVdZp+IlrPB4auDhY2VYzSj+XUUlt1ctqIuXUUZvCZwPuBsC1607WqQ9C3ilF5kuXOrytFsVRib5QbVhh1Vb7mtGtWsCWpe6lmO1kWUwW2ksGpTOOvj7mLo2yI9GRwZMoJwUAp3vk/os42UbLUXL+1OjxOhP2qusYn7zSKxlgXQOswNNOZydjUOnSI1VC+tdyC/uUQpFG1RUtKYW8fwai5DlivNlbOg0aWKi0yg5zS7Ens8yhNQ5TuG7FOLyxo7XcaGXu8RaSVZaiHHyN5n9Rpyb34kGYJdiQNjyDd3QTV9lrEks2HUwVIWR35QYa0swvLK4QhCxaf6yroytbpydiaaDnYBOR3ATUKNXU5c3JI0kxNksMbSIQ43gBTd7QCzLUlrcsdyqmVyfUFvbAXPcHeTu5hbt1ql3kw9oBequD6PB4WfK9Kth2phs9kuicpVpN31BnGGGgUusq5HScKiXd0vuOGcb4OQm3ulztX4SmfL+mi1tzReb0+EXFyYZu3g+0tW9uudGVPrcgh8l7AxnsE0moVjPr4WO7lGwlI5k7UjHaF8XlTK/CzWdtNf96idVLTbzDeLRaEp2jBnhAMV2RLYazqXfZKxNEMS7nVeuBaHq9fEvl66S6ORq8KDFFttMD1uCY5yG/9U6aNJHMKFoSkQIVbeNVpyJeFc6EjedDY3tLW0WedxQWGOaKtXjeELO16YGzBY90PSy90uaa5O5Q6LVEXg6wLB5OzqCZEVCrC5izzWrjcd2cWXijuwuL2ktE0NweS4X4rdDoWoTFqFDHnEMETwx6jY9QIfd1h+VqNx4S9O3KpZVa7qXOyzzl/bWwPt5jQRcIsFuQeONhAysKm2K4YtP6DoiqRUMtBuiW51fpbNd1lCqnt8iUXo/Hbc7RPPCcF+7ch7+cnBaXdwGrrKb3Gn1r2C1Ledv2COMRiUdRTs5wSdXi8WeE1QjKqOzJjIvU3tnHBuS8T+tKhjLHFbdeglh0bKY77ahzHJ7xjt1K3PTHXJnKJCE0YyVKEyWU1IaQjfH7MhKw8MTO+GC4mtiAIihKFr0kAj45hv4CuxRsf5akVXyeoquiYXS1q0D0yuIa9w5dg6dVV6Pcfk0JX3t+ZaGcRePPurERdOEAxBCLdnu50iYpRsUKUo8KmN+2BP1xRg63uTVMP1j9bCk076bY1IRWy2TYXNL1qu8c1hD4Z6BFL2S9zdq+MB9c6qTcnHYAMZsNMEg4qFMJytEQreT8MiGsEGa3VbHbMgkl1EFDWaxlzdzjHGZS15dNqL5KiNQBGGLWd8dKz5/nJe2x4ZrCQWiy7BYCqrW7MX/LVnnQLT2YhGOOxhOT7cDIm/DjiYtAPoTCFCoXA4dLSNZO3oPLXh3AXJwi5uGfuNEJLnpSbc5pChjrCOSop8I/D5msi9midWtumWBInCyG1jN2K2RdRLXpmpsynhI7QjE5Rf+23B5uolZr2lNtBVj9Iuw8GjDAfo6iRdjsWoIiTLupC3r939qXaMPcRTkQSXBnXy3RQZbhd7Ux9c02XONGaIal3sWxHpdVLL0txJPWvVFK3FnpnjChZ3gczDS3lt994hFGM+39O7S7tSWxJtByFYj7Xfb0ddjGFbwL0sPhjJaO2KjOREStLTVT+g0dri3U7p6P441xl3vhXJJoFMZ7mCb9kFTW/ny83Alq44YDlP8jbbUefBhTNGXCJGOcjlRXQXvT4d1oRVJXnpcMrwgx903Wp5vLYaSa88E6CDRjnmFaPgkC4FSp1niY3WJ6zClw6jlEzIXQu9Q7blPKaRCinwTSFsg3OxW7Z+dxuO5w1bzM3uYKxc01xl+9XqcotuViPzKZoT1oEm6cRwiFzyQvFErgNycwqudNZCS0/2wRDRuLY6YmTnwZmIwCjWtYMu9EKEuIvDcGxVHF3zAe7z4eUC5yo6qt2eX6/FIhaWbbPW0/3eZrULdhQXcnnKTqkljaPD8GNloLi22drIuTkR0MjkuEppJKyB/Sxx8Du5Z9sSdXe1TER6jg+jZVcufxYcvEF1EuygyWynqoEZIPJwHmi8oXhxlahY0pcsnhBEgmTohSb5VJY6arlk3O2e0XSn2zHcyaU2dM9ifmVwEL6lx4gWM/mwl0PsgAKRTnjFQ2SJ7m2udNVuyRiUdjWQOF+v139/+fQynRw/z3//wlva6Tzu/+xY8HGC9/Yu6H7061nul7usL39FqV8+vVROBFR6HH/WSRs8jwr/2+Hn53/9DmFaPz5efk6vrYbm7bC8sYLp93deoswFDKrxW50n7XOF3dbTrxLU354HzS93w9JiOrXOm9CrHjfqwnOab03+rWzzZjoWtdxuMn065pxMB3Ymd2ueLx4mJ78uXuGX3/8LPH5bUdokAAA= -->
