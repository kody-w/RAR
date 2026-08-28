---
name: "rar-cowork-cookbook-ppt-exec-label-received-goods"
description: "Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_label_received_goods", "rar_sha256": "67120746e84670641df0fbe640a0be9ba71067ea7951772ff2733fdfd621796e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_label_received_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_label_received_goods_agent.py` and in the RCI capsule.

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

Label received goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 67120746e8467064…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_label_received_goods_agent.py` first:

```bash
python3 ppt_exec_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_label_received_goods_agent.py   # or on stdin
python3 ppt_exec_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_label_received_goods',
    "version": '2.0.0',
    "display_name": 'Label received goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on label received goods status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2d2caad3af5620a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecLabelReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecLabelReceivedGoods'
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
    print(PptExecLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaebOjxnb/KuTmD9vRzIh9mVeuCiCEVhACAZLHNWZpFrGvAjn+7ml0de/Ysd/Le1WpCrNI0N1nP79zutGvL07XRkX98vlFB06OyE6axhGoESf3EbG4FXUCP4rEhf8Qr8jbOna7tqiblw8vPmi8Oi7buMjhchnkoHZa0MClCBiA17VxDz7WwPFH5FDcQH0o4rxFfOAlSJEjqeOCFKmBB+A0HwmLwm+QpnXarvkAOWVlClqA3OI2QrzIqdvmIVLrpEmchx/LB628gPw+QVHA4EwLmpfPP/384SWG318+//ripU4DH70cylaCAu0mjscnQ3niB1emTh7CKeUIrZDD+xLUQVFn8JEPAuR5930D0uAD8h//kdycOmx++PwlR57Xl5fpz7HLkTYCSFs4TQu18ZzSceM0bsdPCJ/enLGBmrZdnUMtoJI1VOHT68pvlIoS+XEa+/6VyacQtN9/eSnKyarQxF9efkCKGvKru+n7p4lK+f0Pn9LJtN//8I1O07lX4LUTMSj1p6/P+ydZOPHb1Dh4cP0RUn11pgu+vPxOuel6lXvSE658+XSFhv/+lXBZFz3IndwD3//w98h6EXR3GjftP0X3p1fCEYwZqNNT8B8+PIz8MzJ7KvRO8++zLaFb/xVN4PQ3dh+Qp6H+Hu2H/f8H6TTOYeC/Wfwvyf3VgtmPyE9/V7d/tOADEnx5WYAURnLtuCn4jPz6VT9I4k/f+d8efvfzb5D0/0pGL7rae1D4mjl5HICm/fr1p++ax+Pvfv7pu66EsQac7GtXp39F86/s+uDzBws+Z33/x7WQ/ylP8uKWI++RjvxalP9W//YJMZ009r89bz4jv8+X6ZohkxJvTF9N8LucaaCsv7PjDy+/QXDIoTad9xiGWf7v/47sY68umiJoEd0ruhaBDm7jDEzCG1HcIPDvlNs1gHZtYmjY5zwY/5OHJ4mLAPnlP70HXH70nnA5L8v26wSEXx9Q9/UN6r4+oO6XT4gBiRZ1HMa5kyJH/nD4kjshgLAGGZY1aEA9AaM7tuAjBKGP0xckzpFf/iHdrw8Sn8rxlwdexq+4dBTXEyY1XQo+TXpZEcifWnjvcA2QtPCgKEEMkfQD1Lcp0h5i2mSDJonTFPFjyAyi//igDe30eSL2yy+/uE4TfclfQZRAXstCM4cT3sVBPn6EOgVpHEbtlxx4UYF89+tv3yH/hfyjVQ/iE48DRPKnF6CEG11VEJhVXQanQQdBl0LIeHjh19+eloVkYEFCoM/iIAavi2FUJsB/M7O+4j/iFI24AJoXmjYri7qFyIzE7SdkHSDv8kKm09CE3VHRTCWsBLkPcm+EVB2ozrslYUFCGhh6TTB+QLoGPLj+4tbOQ8QMprfT/oLsxQOsFEUK/5vEfEyCi4s8huZ/D4LX55BI/V2DCG8kPiHKFIdI6dROGdXOk0fgvPoFVoi35ZC4g+Tg9iWf6iGYTPVIilfzhFO5jr2nSz9OPp+qLkQAv3njHT5Luo8Yj7pWf8mbZ8A79eQKDxYAyDTsYn8qA397hlQTFV3qP+wHJZ0oPb3gP73yiMHdXzUA0lvj8PuWYTG1DF86HMVI5P+vzZhk5mX5KMm8IS0QSTGO51dbTn3RZPPXVgoWfQQG1GvefGsE3mDkDU2/5GkMA6Me//Y68+GB55xXhOpqKPCRPz7oQ/dDW050H9E5RVtdT3HtfMnfYPsDdPgDoya9Cw+G+hRhbwyn0TdJI5iv0/23Ev7wZu1P2sMIRMrOTWF0BAD4rgMt2UaThd+cAEMVTNl2i2Iv+oNWCKQOIwLSn4wfQ3NCaH+YTimgmjC5grrIvk2Pp8YISuF3HpQWNp7gE2LBJJkCpYGZCbubaQ60wncPUkgGoI2hiO8WbiKnfBVm6lWfAjqTL4oMxsnvPfAc/BbWD1km8SFVx3daaMvbhLE+GF49+y7n01dQ2GxKxMeiP7r7qSvy+/ryty/5Q8Z3WIf5nU6l+XfGQWBeZa9RN8FTAyEmA88AgpHwqMKfXgvpa6V+l+Xznxr07/+1Hv5RGk9/9NxnJGrbsvk8n7+Ws7dq9gnmyhzGSFyCZqpsH6fc+/jIro9v2fXxkV1/IPpqo8/IvybYH0g8I/ozgn1CP6HT0C72wBSyzwvaQfwonD+S0+iX/Ai+OfgZBROupiMspe9F5m0KrDRhDcJp8mvRaaZadYPl8YGy0AVf8vcgeKYIxIk8nCpkU/wudR/VFrr01WPvxQAO5S3k7U9dWQimzUo6id+Al895l6YfXnInA//LJmUCexii0BDTtgamC2xw2hg87t6bnenmj1uyRyJBBPCLz1M+fUCmxhSi3luP+QF56/ofe6i8g9uen6b+dmIJp8KP97nv+z0XvMAtVjuWk9CvW5mprXq2u38WYkojKLEHpgJevOflxPFPROCXMAT1n4mojy9O+gQHiN8TUsftW0o3UE4fNjcfEOg2mGoweyAodnDBn9lAPjWoOlj3/Endb/b7plbxqstvDzO0r/vBX1/eQOLpg2fvB6fDbPzYTJVvDkMUMoT3r8EEx/61rvC5GGIabEzgaprBcJQhacCSNIPSJOYHaOACmkQd1AWc6zAYSjPAYTgKYxg8CHCGIAI/8GkcYzgaQHqv8fh1qu3xJBDuOB7rMRjpc4xDe4BAXcIDGI75DAFQiiMClgUktM37UlgJ/aeWr1pNJnxvUCdrPJX99cWlSThzRTZr/vUS55zpMBbjHiOXq2lwvtjztRufKsP1L9oy6elrqSqJaAgJhcfs2sRFiUoqJ1P5IXckv5bVaMHxObNZ9V2w4U8bo22XZL8UEjL2cLcjdklAUSRjCsdlgXPkNiytGL2vHUq+p+aWunRecFTO54Ms9NgaL4gxusj9ZX9ZBg1GcfOzzklbq+wi2WEv4maf+45Icf0sLG9WtVmbEeNqUdnKBhZnSnqKrjJPoNVwaTsHW7sJtWdGMunMykrTS+ltZqwVobNutxyCbIcSQX7nrhRNeDbBBg1hlrwuJ9KlX8n18tTeL+fW9Ii9lVUWe67yphLy2R4LvVQpeQwlCnSbKc6MMDhCKvVBytbrjWE5jtzC/nNJnVnzHqNLp1EWS8bRRbKO7ct5Z0Sledu6urNv8PbooGlutolpRr3pJuCqeSyG4T3dO7XZ6hGVacl4pcu72ifrO9WhiZC6YinnK+mMOvdtp9h0qTerU9LizcV1garNFtSq3DVNXkjZ5aSM5p5L6yhQre3O6jBad6/lzubneWZo3gyrJHvfp+39NqsyjL+pp7uHCqwXWOiyWeMLN1A0x6w4ijKOx/bc7Iz+YsvoUSZmBdr062Nyb1Jd7tbkPSGClbaoKEDNVJ7FQZ3n2j5V7iLnsV0H5uim8StKxF3bQH1LYch4i/X9kgxn6s65iws1JupQ2+JHqvRh7p31w5KIgGKfsvPClom2OtT65u5XbnPyZqcuqYd0wLnlKeaXXCTecsoic36ruqO19Qadxg/r+R509ezSuKcxpRjlcon8LEjxfb0Jo3Wmpdx2rO4bfXTl+u4I9ejAz0qcG5kVqEHJOYGWzEAXNOw8Os758Eqw0f60MugDsxDwwKgZ2p8P3aLQ8mPHnWn7orKtzvj7C2M11w293GppUFvVUDTZBo6r1YiL8v5wTqXb3EmJ/nRbnk9bUlpL29ouXN3zYuOeLm8enxZnoVyU3spST4NRzxa8qIS4Xm61DM1Fo722MU8eaWtUinWd7bYlZZ7wVr2qnrqpSPay6QXJXdn3LDfWij0K+w3Qt0OexOJm2MEasQwYC1vzEW0svcPdVquKVJpEP3DcTWm3kkePQRHMV0dtFZl3LdHp+W52F0Gj2HLV9MNNFIRQvhmuVsnXOgD7new4qtBhRa5ti/2c298DZTgNOTPOq8WhCXVd63l8r9eb42k5kBvK6IvWuyV1xA3mnroG63Yuru4rYxwu+17CljZJ2vaWPbBLzziOdllbNREo1D3cGUsdVw4LsOmyYbO/FUe3l7Fkl5+vYxbSpLPAziIQ/MxZkujhUGzJWrS8Crsvh+q4YqrNbFCsgYu5at+vkqRLjnZ2pLUFWqmdk8WExUUsf8Ux+mwmrLfGE/7UM4POdE0bMQvRX1/VcUtesybnRxQ9Q/+Yqg337bGNirg/LtiYjmxhRGdnImdmpWzsikG5z46dcTgZ6VbhZmC5EDLpTsoXwyS0gff5dscWuBgcj64a+xqkwMrmipvfFHqFa37CkYeYFYYBPyUSWW8wkw/XgSx6Fy9ODjNdWPVn0xit/LrfNCPQxuMSc/O0RMNdw6i4EgR7fIjZe2R0Z9wyx3kwXM5a5Gwace6fUs/Er9dwkYihdODFmIh5ah5avGjaIO5WUEhW1S15jS9HjBVgamHdbeWj64CX2VIwl/RWc6SFYLrn3FbXzV24ddopVoqRGW/y3nYadnMnKSY3o4VeKperXMcYW/OYyvUDLd5ac1FdG5aeATvF533dqudEcrGNY1V3SsM2m6iTAnOb4GBYq0dB80HkZsOdK3nF9++MzDQSf0yujLrCgUdh8xt18Q+r6zw+pAu2qMKlVfdjyEgRb+riSk+5wsPudhYJpBjbOpVgwklo+2KWCCf/stBkW9s2FLhhY1wulTMbl6KVAwnzIkY/Kg62JMRW96WuoC0RSAZepVeBZuKOjwKrPinSgoZthwk3/dwe92dYqlvVacN3+9Fdne6rKDhVkSnp3mru3Uh/UPART0/4pQ5jbGa2Q0NccLUy9jeC5/fHQkYxMG7VaN3O9vtDunUbHfVcfnTLg5PYJxx20l6wTyUygZlot7TaAVvEGuqmrdd04uzXstm1+gFf2bZEnLXZOtka6Wy2ue4jR9vnzpD4GZ0ZsX62AjuQU1FccbFlwHmatCBm0WJxJqL1ygjj2UjVO+tyKULmiPZAoXdASqN9vFFIz8oWdXg7NfqRR+VdR0fYzA0jSZPn3gpqm5RriJxaM8ZrZrFwN3axThTLwrl+Ezrnk27uE1E5qK1jb0tcvN2yIWWym7wtirQfiDsDdoolWISQOP35JnVje8HOLuerZbE2Bmtd1tySTg4HLnMSf3TEeR66RrKLGkZrb84438E6vMmqyoqa1ax2KPUI1nefPhxFaZf7Fbo093MeUONiPOGp06izMgE5J2uJtBzNszPX1tFZNMDxPla7e5c4u7N+oo6EtqNiNKOs3SZJdHGh25vk6C6lkBKNywyVV4x3d05zRbQyGSwKTpnPznw/22DEVRUqilxIW43Xbf9O5MXGRDetqZhH+9Rs1FXf9wxt9AGHdedRWdUaNwpR6xNRGKv5+UKgXVuiI24FuZWyHYFeMofLFrHvZHO3dxy7AOnyuhbuPSA7UYiFvanzjbTM3bwtoPDGOSAErzQjGZTBQapBf03mxfyS3eVG63jhWByz3N5Z7D1bpaq/1rGrGBfdYWvvFwPTb6VsRdr9CduQVNFDLPchRJSXrK+8O7+R+XvUzVxbSvX9pdmVsZp55jmqkys98KXfbYu1x956k1q6vANCjN4WEn0RdjM0ZTWJpomtC3Jbs9xwRXloXt6pIWJWR509X2qd8IXy1lcaFkg6ebsvxbmAXpKeZ+Slfho8Pd4Fl+1yxV72eUBLI3UXnWvi4+poC6V+igqHWF7qc052aHkOChM/AOl67bCh1/LL5SRS/lWnL+m2deK+1rXWHE99LmFkxSzRJprrGURLqVpRa94X1RuY9/LgW6xwa0t8YCypgikWKv6MdKqty4ngKBsVGMwmzx0610rjnAdj6SgV0TZBErmsyeeDodxi/YLvjxm2PhllHFoJ8MZZ4p/mKV+7R1lPN+7RavetaKu4BwtFZTJENl/qS3Ysho4LZV8xUDZfreSCXmxFdxUZOqpswsXNdE/CIYQtD38O5S1tpGfxsHZpqcpGtvVO+gD7yHQR59i+AnTbwvYnYFhXL7y43Z6hQZjQlCvlutMIWbrrpKr0VqdvvBuz9g/DTm5ww5MVinZgUJuhoDazld967QpuV2TTH6V1oOZilWihJuZkZY6JKbc4n97ls5fBvqfnz3c2uh5yHITuyN/iOcFezwnN3VvFkWJhcRBzvAXZJubawKuY0yYgWG3V7sTpqCg8XwIN2OSNPODcebu0fCXJ6D1jSNrKDf1tT60HXkqHBvVyw0rxzb4QNf8YqrIwnsV+c+PP62a3oNylHmXj3lluU+AYdRcYzihUt8bRFGzVjSUrk9t7gR0CSxOMfbNdYvKGbWwbQvdhTQQcKV+jfblbXg9VBndKImxvxDrF2UqjPJbr3fxWH/glqolXptzSTXtdSqYQbvtzwrjQmqU6CjLNJDIVzwgOY5cxIXazubdm+hTcWRDPrHxkTnS+GMyk9t01c9iFAo3NVRuQ6q441z5Oc0LYMmdWwZahtEzSRW8vHZTEtIo+UjCRfDmZoxdvIYzDLmaytlHjBnSwuBKbjHMLSUsouVQTo4msop1bJGzx+MVByYQlbg2zFS2uxo7c9qTtLNorga0SjT54qe/H880sO2DFeiFzqN/s5PnW61vXjGrSke5g7PuuEJr9gShUhdx4gs907JI+HNbNXPGDoDkfnKUlpH49n+XzAUXbnCHsQ+1wHSquSjstjIuLikMlbdSiZu2DVtCHW43Tg1RX1phzfHtRZP6Kze9FvFyHiqrmB/6MkmzIlldPRu3VPsju6rUGlu7Ybmeyd/bE49tzR4CoYFf8Crb3IkWIhUoFdr8FXseQM1FXk/tiR8Oesa+Bzac3lbfb2xIr5/Pdse468i6ui96K743Up3BLjgVrglp5FzzZY5YYbmZXfYHlgQuEUJfAbuYLnqISSbQ7zfDa8xgdkoFVbQ5UVQrUbV05h7MAd415D3cPwZH1BdzNmYOxPvodRjJncYh55WIpV8W1iabfzR2F7s5LuC+iCo4aiP3dZ5nIPzR7XNJsMjMb7jq4zZ5wqKsQM8M5a5LZdVkMYJAV/D6XiGIRr8KbcKsNjlkym8s53Xj1hmIOmlHciOt2vR7YbdrtRby95r12uG7gdiWtD1LgBReBJReC1Vx6XbbIk+XPFZ4FvUF6x/uKCQ9maB4dr+37QMaosyIJZ7cQvZvGdfdAIAtJjXG5sA4EIx6tCqfE3eyQ2aiVytyNwUs3qi2im3W4tvPLllJxwC1X+3vBWvGKMlqc2nNEquTilvNX3TJw4jt+IyzUoQ5ubtsQS6RoWGT0KrnfuHlxVgfy7MyuPIFSjRB2NmrmxK0lwIkd3CthEnzKd3J8Y+iojv1E7o8cZXaGovjYjHDQ005jCHertav03glESALxsOc1RVpC5BGIRCE26Fk6LRj5MKaXVW2K14JbrdDsFJgqV248K09UZmWRx8Xt2jIdaixqmnAPgTl3Bx/LWYJTRZpdVWABdouDzwVqq7HF1eu5At/1nuHMLXrXG2p0yc2FQvS4f66Yniih3Uq/R4M56XoNWcmsO5PwjnJmJ29JxvXtakgSSm5zvagbgeVmvSpE5oy8HtGrCXfTATjM5wG60DSDL3V78OZzW+/X281KvHt+NJKDQTZu39qw7arwe++KV6xi1tLGnN3HcKAlf4WKC9SUxW4r2OICq6R9dKp2QLDXFxpnOYB3ZMLJaikLonVTo9kWNuZqIXGrBTnbbulWPM4MnwopXrg0USCghY7eort3rfq1y7lOckmEfNEUCT+wFc7KiTDa/ogVat6dhGut7vP8RGQCceNoFuN1eieMFrm790rEXRM0t1h8DajB21vtYcO0/dq4Fm5oLWkzEql22G1cM8BLoVrRm5FLiCths7dVxu07gbotfEq+HnGt3V7Fox8exRvKAZ4UWboUR2NY9ArcE8f0gXYzsCfL1RbmV7qrusOxv8mCVR3nRzHhef7HH18+vExHzs+D43/udfB0nPd/dqr4egD49urocWgMHP/zg9fnf1Kenz+81F4MpXk9M23SLnweMv6PE9OP//Btw7R0fH23Or3bGtq3Y/XWCaefA73EuQ/31vX4tSnS7nFg++HF7Zrp9wnN1+fB9MtDnaycTrnfxH+ZfiowHSYXcG1bfH3+sOLxeHplA/zYacHzNnweIX948UfolthrvhI09RXU5aTn8w3GdPg6vcJ4+e2/AQmzh/V2JQAA -->
