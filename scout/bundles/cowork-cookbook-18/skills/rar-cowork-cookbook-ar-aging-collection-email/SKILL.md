---
name: "rar-cowork-cookbook-ar-aging-collection-email"
description: "Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ar_aging_collection_email", "rar_sha256": "26f849e5b3f79a82bf6030257d03749af721f19c39c4e822225a981fd0c80579", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ar_aging_collection_email`. The original RAPP
agent is preserved byte-for-byte in `ar_aging_collection_email_agent.py` and in the RCI capsule.

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

AR Aging Collection Email Draft — Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ar_aging_collection_email_agent.py` and embedded as the fenced Python below (sha256 26f849e5b3f79a82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ar_aging_collection_email_agent.py` first:

```bash
python3 ar_aging_collection_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ar_aging_collection_email_agent.py   # or on stdin
python3 ar_aging_collection_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AR Aging Collection Email Draft — Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ar_aging_collection_email',
    "version": '2.0.1',
    "display_name": 'AR Aging Collection Email Draft',
    "description": 'Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ar-aging-collection-email',
        "upstream_url": 'https://coworkcookbook.com/recipes/ar-aging-collection-email',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee17c25e99830559',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ar-aging-collection-email', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ArAgingCollectionEmail(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ArAgingCollectionEmail'
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
    print(ArAgingCollectionEmail().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aeZPiRpb/KtraP2wv3YXQgVBPOGIlEAIBui9wO9o6UgfovoXX331TFF1tr8ezMxEbq6qKQsrMd7/fe5ni1xenbaK8evn0ogEnQ3gnSeIIVIiT+cg67/PqBv/lNxf+IV6eNVXstk1e1S8fXnxQe1VcNHGeweWbygmaGinyJG7ARzjpYxBXKVyTJMCb5iAgdeKkRpoc8dq6yVNQ1UgfNxGSd6DyW4DEWZfHHqg/IGGVtwXwEXdEagBH42ZE3Na7geYVMgaDkxYJqF8+/fTzh5cYfn759OuLlzg1fPTCVEwYZ+H6nTE38YXLEicL4XgxQoUzeF+AKsirFD7yQYA8776vQRJ8QP7jP269U4X1D58+Z8jz+vwy/ahthjQRgGo4dQNF9JzCcWOo9PiKMEnvjDVSgaatshpxkBraKwtf31Z+o5QXyI/T2PdvTF5D0Hz/+SWHIjiTwJ9ffkDyCvKr2unz60Sl+P6H1yTvQfX9D9/o1K17hTpOxKDUr1+e90+ycOK3qXHw4PojpPrmNxd8fvmdctP1JvekJ1z58nrN4+z7N8JFBX2UOZkHvv/hr8h6EfBuSVw3/xTdn94IR8DxoU5PwX/48DDyz8jsqdA7zb9mW0C3/iuawOlf2X1Anob6K9oP+/8P0kmcgfrd4n+X3N9bMPsR+ekvdftHCz4gweeXDUhimAaOm4BPyK9fNJlb//Sd/+3hdz//Bkn/r2S0vK28B4UvqZPFAaibL19++q5+PP7u55++awsYa8BJv7RV8vdo/j27Pvj8wYLPWd//cS3kb2S3LO8z5D3SkV/z4t+q314R00li/9vz+hPy+3yZrhkyKfGV6ZsJfpczNZT1d3b84eU3iAwZ1KZ9YMAEDP/+78gp9qq8zoMG0by8bRDo4CZOwSS8HsU1An+n3K4mzKljaNjnPBj/1yeK5QHyy396D2T86D2Rce5UX5wJdL58g7svD7j75RXRIcG8iuGwkyAqI8ufMycEWTMxKypQg6p7IB1ETQhAH6cPEAmRX/6S5pfH8tdi/OWB0vEbHqnr/YRFdZuA10kfKwLZU3oPAjsYgNdCyknuQTGCOJlgFnLPkw5i2aR7fYuTBPHjCvLKq/FBG9rn00Tsl19+cZ06+py9gSeOvCF/PYcT3sVBPn6E+gRJHEbN5wx4UY589+tv3yH/hfyjVQ/iEw8ZwvfT+lBCQZNEBGZTm8Jp0DHQlRAqHtb/9benVSGZDJaqqT4EMXhbDKPxBvyvJtZ2zEeMXCIugKaFZk2LvGqgTZG4eUX2AfIuL2Q6DU2YHeV1g/igAJkPMm+EVB2ozrsls7xBahhydTB+QNoaPLj+4lbOQ8QUprXT/IKc1jKsEHkyVbvqWTHg4jyLofnfA+DtOSRSfVcj7FcSr4g4xR9SOJVTRJXz5BE4b36BleHrckjcQTLQf86mIggmUz2S4c08cBK0jPd06cfJ57AcpzDz/for78ccZ6pj+qOeVZ+z+hnoTjW5wpuK84iEbexP8P+3Z0jVUd4m/sN+UNKJ0tML/tMrjxhkVORRi5FvxRh5VGPk0S0gn1sMXRDI/1fr8BCJ51WOZ3Rug3Cirp7fTDV1NpNJ35qhaQmMl7e0+Fbfv6LDV5D8nCUx9Hs1/u1t5sPAzzlvwNNWUBAVWmGiD70LTTXRfQTfFExVNYWt8zn7isYfoD8f0AN1hpkKI3nS+SvDafSrpBFMx+n+W2V+OKvyp7yFAYYUrZtA5wcA+K7j3aBU1ZRAT5PDSARTMvVR7EV/0AqB1KHDIX0EChFDv0DEfphOzKGa0JlBlaffpsdTvwOl8FsPSgtbR/CKWDAHpjioYeLBpmWaA63w3YMUkgJoYyjiu4XryCnehJm6zaeAzuSLPIWh+XsPPAe/Re1Dlkl8SNXxnQbasp+iwQfDm2ff5Xz6CgqbTnn2WPRHdz91RX5fNv72OXvI+I7YMH2TqeL+zjgITJu0fuDlhD41RJAUPAMIRsKjuL6+1ce3Avwuy6c/tdjf/2td+KPiGX/03Cckapqi/jSfv1Wpr0XqFeb+HMZIXIAaFqyPj+Ly8VuSfXwk2R8IvtnnE/KvCfUHEs9o/oQsXtFXdBo6wjydwvV5QRusP7Lnj8Q0+jlTwTfnPiNggsxkfCT0s358nQKLSFiBcJr8Vk/qqQz1sPI9ABSa/3P2HgDP9ID4nIUTUNT579L2UUihO9+89Y7zcChrIG9/arRCMG0+kkn8Grx8ytok+fCSOSn4R5uOCcRhbEIrTHsUmCewYWli8Lh7b16mmz/uph4ZBFPfzz9NifQBmRrND8h7z/gB+drFPzZEWQu3MT9N/erEEk6F/97nvm/VXPAC90vNWEwSv21Npjbp2b7+WYgpf6DEEFYf0Ps1ISeOfyICP4QhqP5MRHp8cJInKtSNM5XZ+B38ayinD5uWDwj0GcwxmDYQDVu44M9sIJ8KlC2sZ/6k7jf7fVMrf9Plt4cZmrf93a8vX9Hh6YNnLwenwzT8WE8VbQ7jEzKsHl0XlAOO/fNd3nMhBDLYbMCV2DJYETQgXTygaGeFucESxVGMpHwUpwjaCShsESxoD6c9AqwweJEOvVoEPuqtUJKiIb23QPwy1et4EgagAcDpBeb5+BIjSYJeUJhD+w5BOY6PrlYUSgU+xPpvS28QBZ8avmk0me+94Zws8VT01xd3ScCZO6LeM2/Xek6bjmvNXTU6zqpkNgzzOmxJMxcoHLVac1VKJ6JVWJG/xuShL+yzENy0pnSIq+Cdcko6iUyAmvOzjR/l+5oM1FMiYauTj55Y4SJRNXXsZydKNDhGu6J9M7SNThrFeDluRaEw0Pbe+NplJhQHFZgzycoyGs0OfakvjUIkqNI5Zhq5vaW4QnPSYcyvt6awLuXicFiSi0Y9pp1W6VaY+t3dWxr2OU5Kq1iT1gGspbovy1aMD+1tbMzIkdVlIGfbWSDr9AzIg51VNAkCFhyasd2Gc+FAXizFd42x47eRlvBNw1rCkdfqE17y+JgrC8JqtNi2c/S+K7Qevw54pKSg3CtbNjPVxVq7tflmNiT3whZc2TS1CJg86yVJcdkbfpWCdls3JqcxW/IIUpdXYu9WUaLn6s54TDX/Zs23o23cMQsctnw5CFpx292WfXda3jMl3t7KpDbGds+eiIK/l7ikHtK9RdhtcmscS2Ykf1SofsuKmz6iMunsCjbbVWxAQCttmtjZ5mUmzK01UL3SPGyJpjUrTr2QC5c7XGUb7lkWw2rYV6xZpwTp9HRpHoX+VlRDjGr6BV8OSREUVkFaSdjtenlnrm+iGgoL8TL63GKmk+aO7DNrnq68kbntYx93mwSraE9pSYw671wKnLRx1MxL6mLBRT/w53t7jLnSdNCWH6KMTFSjUg+SvMWvYMFb8XljRHi32ZkFc+Fy1pR1OT3Ul8ALWH40+9UwcA6dSpIyCCM4pCp3cNBotiHvMPHunlaWIQzSe3EAvBzThCVY6iraZ1pECVxdkHvNE8sEJXW99OZyap3ToGj2gULMvDSIFTv0dqmcOEvlqjrunJnjcnGbzdI5sY2Xp+PCzQxpgemVDjHCSIt4lQNR01R7TR4bTY/jzeLaY4cNczqPm9i6XxclPrure/MqBFwUndFVIxk5WC2FniNnDlme9a2RUNFyq21w9Site9bNx6hcXQ+HYZ8S/IXTQmNh1Vu051CuiLHjgYgGlsA28SKTSDMJ/WBmeKcUXTExzVF7K1+hR86OrlTmk7NGvkVHOQ7BhSwtTB25u+XJxCGjdDe5S9FlXq2U5pqBQZX8uVjHZZMEo2NvqboevKiLE6Hbp2WfKp6nn85ktb7HCzHcM4omHO9zdrBNHY3t0VhEaSwo7vrYhur5djANy4rZUyRApSTHGbSrE5VBsooxuWeXipsu8lSUu25lOPrhfL3jXmyFNlmMClkt6Eodu2Wd5ObFcDzbueGQWmmLoMzAwi0MMTmSgBY6vCorg1sPMrcVcilgzUENVIpHpWzL7vCrJhOdfQTljoAm4krB2NPLajds8rU8jof1zvOrbCwD/sz1fkEIadMrdYtrRXS5AF/iuWWkY/qBYjFGOQDPwe7Jhhki+5yXI7GQDnXYcbW57S8N2R5hpAvWDaNE1IAb3NrZ+GzWoVd7kIkYyBd1kaq7SPY3Z5zWzwIlXDpHpf3ZMcETNJBn41U6jrbbryR+u6FU9haVuG05G3ZxxyuDFWctZYqGfo/1bGO25Z7fOuFobcehw7A63NWUNAhyxzJURHOL05jsxlVtuzexdYtaHfnL0pHF7sRt6TwM+/VOWexa4yLN2YZAfbW+xKcqmavKrd7LJ//GZdbi6JrNzA5kxdzRKK+hVRhHek6i43C+KKiZuNJGYZLhyKYluNTxLvGdU9Vt3BZYqCBk9gmvDky5NHflUrofrRUYLqlwhQbJl3SQCdgcZKJ0FLkt77TRcubinmaAJBhCr5IB4TJZersWOXGezUVuXcHiem0wniFypVCplWhnhLbDSVIFwU6nl/TBkLfHVeHIvAkraC6tNUatmGuhYTegne9lH+q0dYhu97ISW/lyzNmUy61x7YZ7I+F8CdbtWaATaKBHF1Qbpk2De1McWgwtbdOJJIPnesgvjV7wo1nOrbbbQuftncky57EEZqofjDteo+ZGxDSw7ncMs9T9tbjEygMqwTjmDf4IWwm2aYSkcnhdrB2iTEvd2xZoY7li6h0tZ5E7QbcC8z0AI1qfSxpNil0uYqINVr7He5u9udlWvkgpGZkt2ppSD7itNb2z6tjkeKnnfCQY1+3+ZMA9TBzf1BHH5h1GpEREGLDQ0MludhrYwQ/oYjRuZztwFoeuJBxc17BrFuGNfrZnwMJh5kimyrX89bZaoUurKcIsvm9s2NgUphuGnpCvz0VRbUV33ArxKmOObEm2UPySEMTNMXFGobyVTsiOInV1iBvB22g4O2xHXvOFsZM3i21r8Pkhc7ZqsJXNUnfjkk/Ca625rMjoutz35BnMl6QtLJlYwE8Km0Wy7UmF22Jcb0bHUWN3Ry4/bYbzxk7PjsDKR9exTs4ZboCCw7ahPENEb41YMI4ubu/K2BZccXQT/6rAzig90fcDM4uWy8Wi3ncaebLOt4yWYiPL70aEKmZiR8WBqXvmStxDcXeva03phdHbU7lYD87GqAzFcNT71XPJ/lDUjAIi/0Y79w1VO9JNvp1VLtSW7rxpfPe0mxVsR6nxyZYFg12dNgnuKQTPaL5mLfwtm4rYTIvcOT3MmotMnXv/oF0WtVjfq64kNzU/iA4pgUgsutPOqpbkqS0SsKM4ez/6+tLCqBO1P1wP454LVKuiqsGONoQSKj2/upsys3ULtZfp3N9D9GkYwey3xwUZ2CTP9LmzJViLQefigcOLscPccHW5F+t1bTjpeiFaRdjK/kLxtTICtG9QlRmThnoVUdI8iM4svCssd4o61h8Dzzmqvtq36X5pKkbMd7Gc8vwaBYc949OXtjT4Sx+z9Hl7K3b8plQ2ZwF2O8x8r10CV9yl+v0Ei/Fu1R5kbHvqR/1GXG00E9yYOpM5moyavdiTSp94lB73DeBvAqdFTCPq+uWy3FxXYV46Y3ot9zN775QBJ0JEyofk6KmarLhHkztfgrwG4HYUdLG07dsKVBdOWq4H0TVdMtOTc+eRNzJeRZbdLgh89O7mmV2L6olvlbkmBaMJQHfe8O41PRtZl8RkHrPH1j4ng+8O1zGkCnZ5rYAohQtC3+OjtiCqfQdbHcNyZ2oYELbpGskx2dOCOeyvm+XeXit7jmpvUr4rY8U9nEvyKpxDUspOmMcUoZ7Ty+W9mhXzpNrM2JtyuVmcP2cM2pa9zPfO0VGhveNFNKvrYW1sT5G7UFyClWL/smdrf2+huMXG0ak59UGmizmR765lpK8F1i5VYxmdXbxlGrR0+a4MxcFKZ9xYkjCftsqASsTdIYiivmaeHHL3Q6oLwtK2AoOb7y7HmWVyoX6Xr7gLe1N3I6VjfUoOO3ToYXeungrlZB7J+HAdMTVZpedTbuIEFZ4uS3WDo0vZMK7hcJnVF3mnB0cJ3970wy3v9/dxdUtuZnz1VwYttLRsSoG3yZ1iu73wvE3w6VLs7dXRpNMkUxdFG/Lo3ODlXaZVM+1UpHSPGrDzWFqkkd02Wtv3BzEkTlv3Rii9WKeH1SXi8kt95VMvtZNK9+8arfa0cTk6jNwLcTlnwzWu85GLYcxBMSLVG88ZhnqZfOXi6zouTyMenWSDr5r0AAPbuZCqZruLFaXfWvLeHnLP7c5SW8mFwysqW9OtSaGJO9sOgjCyhdouWErpSCltugsgTSIjzF27sp37uCzHCiaEXZMR7Hz17GJHlOfIRofFSxzuZzaZ2dpWLomda0fy7bKJAu1u0Z5O6bmpu5V+mt2V81E4Mr4XS2OBS7is98HxfDW6BgVqxt5wTuGLdHs86U62Gdy+szh6y4hnUI5tt3B7GS9qh9rmbNT0Mrmzdy0bLHw9QX1M2qFg1q2zXGxp+nrGCSwJ5LlpZdf8LlISNhKhQzLBbn9xUbCI3Xtz3sAVu/k8Icl5H/bn6jCLU3SOL6P5tSDdI962s7FaEsOBToCeyHcQmmh/j1BuFzn6uj3PlBpY/R63ZS67MwvhJF1P+KqthevIoD3hrYbNjcVYUpMIMawlZb69eTuebNC+xT3KvZ5vbGWDS+vrKtEypnYYjUHJWrqTFJpQo0HT17hS7+uwmkWUSPYi3pOh5JKuL88LfCVHrdeG6Vkn5vpqm+9kDKMopsvcm1vXV8fQOhAKQ3ehF5m3k9h47O0eE1lo6Mu4X9wAlZTy3TeX1Xy5mGdsGR2lcJyFa4vR2pEl5YDN/Q12z5ZZcdu3lEM3tX825e5iwn1z5czoZAYoNTPRq1KvusVW3hmArM4rijRPHrdYMxns9muMaWUIWzG63vPYldNLweZJagubpB3dBGLGhDzA4nNGEeKg4AudXHZZF0mbZmRXfk/t5EghJMJC12dAsxovdMN6TLL4mJlYaItyb+ZctUznq8MgdeVMvg6r2eYkK4HDLDm+aZ15fT8J3o4DQ3QJYfvLX0/Ubey99WYTsGF53K3m+aUqxXTgZHmReEKlbBRtju/OG/dE4wm2b91I6MilBrtsYkxPc0rx09mRTmBVzznCtX11frV5WfY9dtFgMzV16BmBU6FCROMK9vYEj2P1TlmeRFsPK4yu2ai2ezPDiWLojrzTDFTlMkpob45n3z+IQ7vk8KM1O+JCmrZU5jbxcWNIMxC3u9yLOwWD6HP2CcbYsSw+WqG/Kv0hD5mxDnp1Kd9D0hUIsMv3RDo6y9ymj9VapDdtxHYcgx4oQK+4wQaY687WGWW7MwitVIPbHZ/b4Tzq7zjAN7EhLwX02GEd7EjuDbW89pSSiqXVLonZyT4AIl3eOVkUm9lmTh1dtOUUnAp6HlslFHHZW9qpW4snRddDCOFl23d3nJTP/MKiYpHHnBkxVsSmO8z5nePLynl7UGZVRYyaR7Eqt7EyeVfDLenqrlFJ1FV3SyAdyalksqr4yEkxCd2AK4Yue68/75RGucQXZ1ZewB1DnaXjgKZGExSjKcvrdjYEIl4aeBiouhHgAaDui82uJoJNZGeXRg/CczfHfAZbswdC7eCWZF3PV72TmLPCv3sL5u6kLroavQ01ZpcrWmEe1Q4O3RajTszua4HEGvLmr2TQSQzXrvCabNer5n52z6QoLGRxtm2DjN6m+kw2GzLMT5EkXWzJ2R55ahcPkTo/NFtlbjSp1GIAo2+MN6+SXvaYnc311Kzf7mHdoK6rPSbdKjlg7IOT3Q+yIBEYLe7EYYAN6VnMMm91pQfeNohZSEthMEOX65BhmB9/fPnwMp07P0+P//dXvdOx3v/Z6eLbQeDX90aPg2Pg+J8evD79E7L8/OGl8mIoyduZaZ204fOg8X+cmH78y9cM07Lx7X3p9EJraL6epzdOOH2v5yXO/LZuqvFLnSft47D2w4vb1tN3Deovz0Ppl4caaTGdcH89Rva/uFUMAvgkr3xQfWnyL55TRy/TtwGm9zTAj50GPG/D5/Hxhxd/hK6IvfoLviS/gKqYdHy+upgs/oq+Ll5++2+M/PcULSUAAA== -->
