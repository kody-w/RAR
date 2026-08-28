---
name: "rar-cowork-cookbook-bulk-update-conduct-a-compliance-risk-assessment"
description: "Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment", "rar_sha256": "33312cffc115bca8cd1d6bf76feea0c91f911f2fa11bd6a0d32a45203f360c44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a compliance risk assessment Bulk Field Update — Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 33312cffc115bca8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_a_compliance_risk_assessment_agent.py` first:

```bash
python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py   # or on stdin
python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a compliance risk assessment Bulk Field Update — Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment',
    "version": '2.0.0',
    "display_name": 'Conduct a compliance risk assessment Bulk Field Update',
    "description": 'Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-a-compliance-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58963460909c788d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/conduct-a-compliance-risk-assessment'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-conduct-a-compliance-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConductAComplianceRiskAssessment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductAComplianceRiskAssessment'
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
    print(BulkUpdateConductAComplianceRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZej1pbmX6GjHtIuIpN5yru8VgMCgYRGQANOrzBiFqOYwe3/3gdJEWmX760uV/dDK4cQsM+e97f3OcRvL3ZTh3n58vVF9+wMmttJEoVeCdmZC4l5l5cx+JHHF/APcvKsLqNLU+dl9fL64nqVU0ZFHeUZWM4XRRJ5FWRDlyaJIT/yEhdqCteuPch2yryqpvVu49SAxMlTQG1njgeVURVDdlV5VZV6WQ2VnpOXbgX5ZZ4CLaAoK5oaSqKqfoW6qA4htxw+l00GFaXXRl4HXTw/L72JZRrVX4BeXm8D7l718vXnX15fIvD95etvL04ChAA9BaCdeVdLfKjDix/K7IEu/IcqgFViZwFYUwzARxm4LrwSCEvBLdfzoefVD5WX+K/Qv/973NllUP349VsGPT/fXqY/e6BtHXpQndtV7bmQYxf2JUqievgC8UlnDxWwum7KbPJeBVycBV8eK79zygvop+nZDw8hXwKv/uHbSw5UsKcAfHv5EcpLIA94Bnz/MnEpfvjxS5J3XvnDj9/5VM3l6oEYAGZA6y9vz+snW0D4nTTy71J/Alwfob54317+YNz0eeg92QlWvny55lH2w4NxUeatl01e/eHHf8XWCT0nnkL7X+L784Nx6NkusOmp+I+vdyf/AsFPgz54/muxBQjr37EEkL+Le4WejvpXvO/+/w+skygDhfHu8X/K7p8tgH+Cfv6Xtv1nC14h/9vLzEuiFmTHJfG+Qr+96VtJ/PmT+/3mp19+B6z/j2z0vCmdO4e31M4i36vqt7efP1X3259++flTU4Bc8+z0rSmTf8bzn/n1LudPHnxS/fDntUC+mcVZ3mXQR6ZDv+XF/yh//wId7CRyv9+vvkJ/rJfpA0OTEe9CHy74Q81UQNc/+PHHl98BWmTAGgAK02NQ5f/2b9AqmsAr92tId3KARCDAdZR6k/JGGFUQ+DvVNgAjr6wi4NgnHcj/KcKTxrkP/fo/nTuYfnaeYIpMKPn2wMe3JzC+2W/fgfFtAsa378D46xfIAHLyMgqizE6gPb/dfsvsYMJMoANAw8orW4Aul6H2PgNc+jx9AfAJ/fp3Rb3duX4phl/vbSB6oNdeVCfkqprE+zJZfwy97GmrA3Da6z2nAQKT3AHa+REA4FfglSpPWoB8k6eqOEoSyI0AwoMOMtx5A29+nZj9+uuvF7sKv2UPqCWgR2upEEDwoQ70+TMw00+iIKy/ZZ4T5tCn337/BP0v6D9bdWc+ydgCC5+xAhou9M0aArXXTBaDMILAA2C5x+q335/OBmwy0AtBZCN/6m3TYpC7see+e15X+M84Rb83IdBs8rIG+A2BVgSpPvShLxA6PZoQPsyrGnK9wstcL3MGwNUG5nx4MstrqAIJWvnDK9RU3l3qr5fSvquYAhCw61+hlbgF/SRPwH+TmncisDjPIuD+j7x43AdMyk8VJLyz+AKtp2yFCru0i7C0nzJ8+xEX0EfelwPmNpR53bdsaqPe5Kp76TzcA4iAZ5xnSD9PMb+3YRDY6l32ncaeup5x737lt6x6loVdevduD1QZoKCJ3CkX//FMqSrMGzBATP4Dmk6cnlFwn1G556D4X5kopo4Pyfd55NH4oW8NjmIk9P/JyDIZws/ne2nOG9IMktbG/vxw8DRwTQIeMxqYFyCw7lFM32eIdwR6B+JvWRKBbCmHfzwo72F50jzArSmBF/f8/s4f5ARw8MT3nrJTCpbl3SvfsnfEfwX23+ENRA3UN8j/Ke3eBb7evfPQNARFPF1/7/5P70zVDtISKppLAlLG9zz3Yjsx0Kqcyu4ZEZC/3lSCXRg54Z+sggB3kCaAPwSUiEAhga5wd906B2aCirt7/4M8mmYqoAWIHtAWTLTeF+gIKmfKngoEAAxGEw3wwqc7Kyj1gI+Bih8erkK7eCgzDcFPBe0pFnk6ZcgfIvB8+D3X77pM6gOuNsgn4MtuwmLX6x+R/dDzGSugbDpV533Rn8P9tBX6Y2v6x7fsruMH/IOiT6au/gfnQKDY0uqOshNmVQB3Uu+ZQCAT7g38y6MHP5r8hy5f/zL5//D3Ngf3rmr+OXJfobCui+orgjw64Xsj/AKqAAE5EhVedW+Knx8V+PlZep/tz99L7/NUep+/l96f5Dzc9hX6e7r+icUzyb9C2Bf0Czo90iLHm7L4+QGuET8L58/k9PRbtve+x/yZGBP+JgPowh/N6J0EdKSg9IKJ+NGcqqmndaCN3tEYROVb9pEXz6oBYJ8FUyet8j9U870rgyg/gvjRNMCjrAay3WnGC7xpL5RM6lfey9esSZLXl8xOvb+7B5q6BEhj4JlpGwVKCsxPdeTdrz5mqeniz/vBe7EBlHDzr1PNvULT3PsKfYywr9D7puK+Z8sasKv6eRqfJ5GAFPz4oP3YbF68F7Clq4disuKxU5qmtuc0/VclplIDGjve1Pnzj9qdJP6FCfgSBF75Vyab+xc7eQJIVdtTH4/q97KvgJ4umIpeIRBHUI6gwgBwNmDBX8UAOaV3a0DDdCdzv/vvu1n5w5bf726oH9vN317egeQZg+doCchBxX6uppaJgJwFAsH1I7vAs//rofPJD0AhGHIAQ4IgMNzxfQfDqItjs46LufTFZ2iA5zbqcJjPYZiP+zaGXVzaRl0Ct0kKRwmfoFGHJAG/R86+PXofYInbtsM6DEa6HGPTjkegF8LxMBxzGcJDKY7wWdYjgbs+lsYAR5+GPwydvPox/04Oetr/28uFJgGlQlYq//iICHewaUK7rMMLXNI+X125uO6XLpGskwrbntzL0rLd5SrG6YzEi3Ok7mJMMATptjuUjjP65wA+W1zcEiv+dDPJhMJd/Hhx8GjJB+R6hB2K2PEHYTXLx+NBkwuLj9ZFxWLGUkv0CG33mn5MT/U+PSbw0lqW7O5augsJWfBZlRjRyCGItHQoKmq0YlfZJ2RBUo6VnISwVP1VXQjObR0fov6idvNBGvPLhl3Gx9vFiPdHDG/2B60q4uMhuvQ7DCvq3lRrw5ZVSrJP5DFE4fba9352RSk/I8hytAa29YNSHkZzbQ3HRYIdqXVuNm63LPdadjSlNnVusuHl1nahW6dGR7WF4V0PIrs8ep3XqImW2QUtRpdgKR9DKZN7r1KiwqHM7rgMQyLUd5mwr6RkPqeyorDVq67Ma/FWrxeJapxwGbOtsl6knVXAro1fD9wY1GNpLLLl5by6LJYrVuvtYpYfdfqoh+ehzYVVvNgMi3G+X6bL07nMjixTYMpOWfYqF4tiE+gtc7aM7WVFKsDEOmXT82DIQcl0uL9zaHQpn3Mf69XmdlW1inZTnVh3yEzSpLCS8cG+9qWAa6dNFulpc5wdFtzVuUR5usGOSVwceXYrwQ7ICayXUgl4tD77ZmXasLPoW65VNgHF26mLM0XDeb60bNwGF3AYn0lNFR+OVspltDXwjofL4TxZXu3jTEW5KqpKLLWvvjbyLH2+nYNjKfpzEcE7Mz3HYwcqbAVbt8BHJHTXyJJCrzTDqPp+qZjsNQwPDK+pJhdWnQ+S245OB4vKLNwJtbGro1bslXZBBmqm18wujAn3EuOcGeOJuwIm26a1Bj8v5WWjtuteqwu8OAU8kafbgGlD3+nYAt/Iu2OFdN6YSTgCHzN6vrMUmS6xWmVlQ2fOkXPY4Np15x2TLR2l+9MSXda2tpCMdhW28cY5Y+FFKr357LQntdX1VNVV4XXSpcljbY8r2aZmBYrLUj2V+4NwPDe1tOO65TbA+cBe5bd6hUXVfuYYm2jX7fBTtN0ERayKRZaZ2CUTRGezSEk27hsZ9ZXTGCMGnihVtgqoBaJtoqNhbiInolC9dljLy2dOOfiDNJMrxGCMtcmkGh0Q/oxZgfk0twgPQX1Si+rTudlIae927dbL0OLQ26XG+vy1uwkAlypdr2hGCaI+b5d8uayvO2FYnRhjhQzUYFYE3kbrLajMfNzmJXnL1wtlsTGFYjd3JHko95nDlrNtsY5D1CmOq4vvlzJFSTe2VRy6t65IlZubsXAtFL/COHxYKPpKvxFnPtXtZbUxvHgZ+rcazY9DXKUVTWl9b9skn2Dxas9pIzlvlvhiI9ezArf3BnnbwyqFYpTomG3bWlJknufJBeFhNErUCA5OF7bxWgcm5b10zpJwzoYi1R5ulqukG8I+G4Uss/uDpFMonZ7rpcru+DZOw4QG6VvHpEHPWX0kT2KHHsltpuXJ0nCrcX0ljGi2PmjdVoHbmYV5kYye59ahmBn9LBgb7VbWEpeix3pOu90pDVjNK1dbBsvnM5w4dBS82jCtGCeLmbup20OqUEE23+fnlSMYg5nTGc81J8sZu/PxNsrSqeX7eXCT6FnMSBzCLjR+YRF9JeV0UaCcF1YDTVfllpkLtyrbEbtRF9NOXmpKuKtMaYnsm0NxO+uaBGo0cjudL457hXfz0gp5Hi2dxZAuIjPYkmgeXKUZgNt1G20HatEFiirweq7sxmJh4pYQ5DOyzGZZs1FWsuoexewYCY5YbR3Rzba652vyctws52OWjQS1GVn8XI9SkAzWbZwfT367oA5xsl0eBqdPDXYpqMv1LOOMscPYmtzgOMkFsCeLkq8wyG1gYcQbNA9DXHgoYbZluJ73lqd+h8arrjxRpiNVfIMv5rqyztn4lhyEpUw37r5PdhpttTWZorlJX8tATQNMYhE+mM2Hm1kMdqzbVwKN+Wa+T6kiXbs8Kxj7rWjlLpKsiogvrvq1SdFaEhFmh6J9SVIUTh3mB2/bH+CBFGmTaWfd0jauutsm9mLkrrp8SPanqyL5R+dSX5XlyRls7GD3Cxobjnaf0+Vmw6idK5HoOi4J3UabpO2vimMb1rWM99FsW9W4eM1KfHnYZO0hAWbPzTol4U72RFe8mcmuR/PGU3S16TFs08uMeh3lczTP/Tmsr1RvVe2aS8rXrSVIdeKdrPAwHN3THulkVFnKziIsl33Y325mrnJBMYjn/RHPVmdVdx0Yke3iHDvkKpBs7HgYTFsqBYFN2HRTpWUqRhaIk9ncQKDlyt2YSi/ENcyz/A6eNXmeqcXhIN9gbivq0m5HaO6u2MD0spJSQtJNfGtUujYXg4OhdAy9bk+Me4tr9SDN09VMI7MFf1CqusDcpRwPirUPLLivfNy6hVSwM9LWiLWQZPSaPA9wekLBSGKcNLOawVeb2uz1hVTT270oLbJ2bfX72Cc29F6mJawRE8Hysv3SQM/L3DqeyCixMVkPoxMWB9o1259lOIxMas/sNCvAnMUxL/IgWvAqhVjykQ7VNS9G53UrwIQDx76xSwohzEW4NBF8rcshTlw34Y0ixXi94vPmQrTeTm9LY56XI8MsdiMCs4ietIQbZFJ628WKE5wvYMI8q9eEmU2AjKmVm2QUZ1ma6yqteMoHx8iPBHNgDM0VUBW1eLygMbnXRUfIb7v1NbBygfGWjRmzCiyp6aLaDclq38saRfsZJgE3nOX5nF+byCHhN+ZNQldKDruqjkXXwyx2QSEur5l3WqNRYbR65NvCRSgTc+miYiIyh2bdwXyV8t1ehG0irTvvkC+KYZNKpLRS4cTArgEaY3I8X8P27SYJ1kAz8Xm/ymZajsQtt8sp+rS8MAGlWrB5jGfwKdky4vxsZzFZXGwrbgMSzrCt3kTa0hwTfuDZ+NTmtDRbLM/N2pCIKhE5VmMyglvIBzHBlprOOmFTDDvyTFA6x83O1211w61OLxJYaGMkb+QVXlzhYuCJ86BSG40dxVuztBeHlBtS43YR1cv1cjR8yz8KW8vZlyGj7lxx03nIKq0dnUF9Dt06jkixgnWUCe16O9utXA55Q5+iVY2S9OmMHExHZeDDdl9vYMqmjkVLmaIvOMnKCE4RF5l5xkfY7CjPEk2i95jOmiJniWtZHOhU0K2hO/G4o7r8wYIxLDvEtmFeXMVHo8WiTq28zshgxbiW323dhBr2jYfqt/wMpk2tq10pKYK4PxpOuA02bi+GvFLYRpLPFjw/PwzjLZq79tKhF+EQMXsyTmaHI0yRwcXdxcOgkNfALLjEo+d6Gu0J9MpFq83JWNS4RAfdKrXkzuq5Y6rnyZl1qS1lmbqw7cDeoa4ovTrT/nIYk5V/UgTmtpdBiVEmKlhmBJqPGbkBmIN9xuP7rJC3/nnBiWQ+Q0rEGeCOzo5uU3bpYWkFeyVBtJofZZFhUnt/ocVb6IHxHR/E21BJLbWYpWepZdLV1SybgDJdsS1vvEo0vr7PZMUQBZdztwv5bFPmoVqZm65TwOhLmhsjlDe9vTovRzHcjdZma1pirRUcsV1jioDp8ToQ0kDFbDhkFct1ZV/dpJ7gRD0p3nZMOPKwpGvoGs6xxRbwv60Vw7VX66s5AkSAyXxZN1ET+2OCwonV9bt2J+y3c4oiMcHyT9h8pi6DpIlUxHaKq3/ITLe9zcQwGxB3FOAaLzAOs7cnijk43hXjTmOK0ViJI3SaoiniKQJyGIl1Ox+2Y+CXzeiC1nd0K3tO96Esu5rJpdQqzaRbTex727323XGPCLHKHw86LdKbi1wxShm5ZX2zyLMmyKW4T/elxKnH2woZnWDbS1ivrNUbPYLsrve3dSqoHbsCm9cel7fZmC57jU5rhWh0ovQ8ZX3NuVxcI6eD2yXucD0flbEZqnaOzqpKQ3N408mI1HBtKXjXcTC2zHZLMMqMDq2oOB19pNcQxRhwonVZZFNql7zC2WTMS+y0kyTUjD0hIyt4AYuM1Zaz+nhi5fG22QhhB6eNdch3e2d920s9FcEh2D4UayaAeXKhIOme9TjrVBaHisFPfKeWebm6nsn5jGj5+nAeAnPrNpcxVTzznJpxv0a1paZukHwcfYBlsCLNSES7NMpigQirNZegcy7ayqyftzyFH4nTGejijKWm4iEfjbhqlMyOs4j5GJyrSmbX193JOLWkOdvBONhoMzY86i3WIt5mIzk3h6m87VlIVTVrO27dBt48YNYMd11Uy6atnc1crUi+bpYrZtvXvj/4IO8uCVPzEddis3STcjFy5dpExTvDVEW/cY/jWSRhqfC1nRpcMjVy9yK3bc9Xip6dtIxz3EWwc9LVduDmaH7Jw8y7JDQZxn7Bb6/pceXAByGQgz6Xeo6Y5YPByhVhkdlJOTr+hmfNcn7qMiVSZeQE5tbSa00WFp3tDjFl7LycW0hmM9ZAbtVrEIybS5BEQleieOcsZzNfCG6lwhK5V97W0S7zWypxhNIgdkdkq2zqC+sSCa6CYWXRUkxknFMqXS04ImAWVHhZK6Gan0n3lEk+sx6yDjlJLpdyI4rlONOr5o6CQ3q1miPranZmHeG86zx4e5EsTe7mFoyfhDZqzpxFlhp2ChRNOK+TPY7tCHEsODdBEuxq1NkB8aOgn2X7qglvW+1044mg88WWtwNSXcJ7VGrHujLUTs0Vdu1fHXozjxSlp1fEYnWDbxazAzPYFmxbNmsyUELlwohBpxBYe0SQUijl7Ojva4xiShru9pEkIA3sM3runYXWvYbyWLCSe0H8gPEbjGd00nBbG+tdnN82W6WAR4LUGLaQAibxdzDBHkr6kEc7Ed65590t4k14ffDQOm3hzbCa53jsrcIbTdks77QRIp9IOw2Ogh5vbzS8mSteZ+6NQ82Bhpar7Q4lnJvLgcmUkMex0BXMK001hpEx4GnFzTp+Zlqa6GjmRY1Hd4xQFVtjrU0srAPWNlyi4SNewcxcnofiEaAEl21j1t2pzEbpWVPuDYkjY2YURl7su9AX0FyPu3B0rrd2efSum2LuilYwaotO9ZduSuhgh+sNWL7JGnNzLVerNsXa3aENGIxe88mYumjRnbjInl2UReHVZBtwI8tU9bBVmbpVjWt+CVIZS8BOb92r+SVG4JpfKnSC9hh6pYmqU1J31QhUN6up+czDg3p5nRlutAe7PMQ7kiJLFys6GmbNumXDnuMpYs26Yea26ywAaRPiWyTYsNnM17Uo53n+p59eXl+mI+3nwfR/+031dDr4/+yQ8nGe+P4C634s7dnu17usr/99FX95fSmdCCj4OKitkiZ4HmP+h2Paz3/3NcjEbXi8HJ7ew/X1+3l/bQfTr0G9RIBHVZfDW5Unzf3g+BX4upp+DaN6ex6Qv9yNTov6/uzDSHBlu2mURdPL27c6f3ucWU/3o2x6xeS50ffL4Hmc/friDiCmkVO9ETT15pXFZP7z9cp06ju9X3n5/X8DhuGPkH8mAAA= -->
