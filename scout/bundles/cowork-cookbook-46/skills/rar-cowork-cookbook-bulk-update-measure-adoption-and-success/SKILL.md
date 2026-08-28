---
name: "rar-cowork-cookbook-bulk-update-measure-adoption-and-success"
description: "Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_adoption_and_success", "rar_sha256": "5f4de8689040760a1a0a3e32f5febfc0bdec7bbdd3e71c520e52f385ad3deedf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Bulk Field Update — Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 5f4de8689040760a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_adoption_and_success_agent.py` first:

```bash
python3 bulk_update_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_adoption_and_success_agent.py   # or on stdin
python3 bulk_update_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Bulk Field Update — Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_adoption_and_success',
    "version": '2.0.0',
    "display_name": 'Measure adoption and success Bulk Field Update',
    "description": 'Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb7a04f62dee1a46',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMeasureAdoptionAndSuccess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureAdoptionAndSuccess'
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
    print(BulkUpdateMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjSJbnV2Fi/siqUWQKCRAo29psERJC4j4EiMqyKG4Q9yUEtfXd15EUkVVT3T1da2u25BGAu7/7/d5zJ359sbs2KuqXry+qb+fQ3k7TOPJryM49iCr6ok7AjyJxwD/ILfK2jp2uLerm5fXF8xu3jss2LnKwnCzLNPYbyIacLk2gIPZTD+pKz259yHbrommgzLebrgaPXnFfdWfSdK7rg8Had4vaa6CgLjIwAMV52bVQGjftK9THbQR59fC57nKorP1r7PeQ4wcFIOYWWRa3X4A8/s3OytRvXr7+9PPrSwzuX77++uKmdgNevWyAVKe7OPxDDPIpBZl76kMGQCO18xBMLgdglBw8l34NuGTglecH0PPph8ZPg1fov/4r6e06bH78+i2Hnte3l+mPAsRsIx9qC7tpfQ9y7dJ24jRuhy8Qmfb2MKnbdnU+masBNs3DL4+V3ykVJfT3aeyHB5Mvod/+8O2lACLYk9TfXn6EihrwAyYB918mKuUPP35Ji96vf/jxO52mcy6+207EgNRf3p7PT7Jg4vepcXDn+ndA9eFbx//28jvlpush96QnWPny5VLE+Q8PwmVdXP3czl3/hx//GVk38t1k8um/RfenB+HItz2g01PwH1/vRv4Zmj0V+qD5z9mWwK1/RRMw/Z3dK/Q01D+jfbf/fyOdxjnIhHeL/0Ny/2jB7O/QT/9Ut3+14BUKvr1s/TS+guhwUv8r9OubKu2onz55319++vk3QPp/JKMWXe3eKbxldh4HftO+vf30qbm//vTzT5+6EsSab2dvXZ3+I5r/yK53Pn+w4HPWD39cC/if8iQv+hz6iHTo16L8j/q3L5Bup7H3/X3zFfp9vkzXDJqUeGf6MMHvcqYBsv7Ojj++/AZgIgfadO59GGT5f/4nxMcTWhVBC6luASAIOLiNM38SXoviBgJ/p9wGKOTXTQwM+5wH4n/y8CRxEUC//C/3jp6f3Sd6zidYfHsA4tsTCd/ekfANIOHbEwl/+QJpgH5Rx2Gc2ymkkJL0LbdDP28n3gD+Gr++AlRxhtb/DPDo83QD8BL65d9l8Xan9qUcfrlDcPxAK4U6TEjVdKn/ZdLWiPz8qZsLANm/+W4HGKWFC6QKYoC0r8AKTZFeAdJNlmmSOE0hLwZQDkrEcKcNrPd1IvbLL784dhN9yx/QikCP2tHMwYQPcaDPn4F6QRqHUfst992ogD79+tsn6H9D/2rVnfjEQwJI//QNkPCoigIEcq3LwDTgNuBoACR33/z629PIgEwOih3wZBxMxWtaDGI18b13i6sM+XmJrd6rDagqRd0CvIZAzYEOAfQhL2A6DU2IHhVNC3l+6eeen7sDoGoDdT4smRct1ICAbILhFeoa/871F6e27yJmIOnt9heIpyRQP4oU/DeJeZ8EFhd5DMz/EQ+P94BI/amBNu8kvkDCFJ1Qadd2GdX2k0dgP/wC6sb7ckDchnK//5ZP9dKfTHVPlYd5wCRgGffp0s+Tz+/1Fji2eed9n2NPVU67V7v6W94808Cu/XtZB6IMUNjF3lQc/vYMqSYqOtAhTPYDkk6Unl7wnl65xyD/r1qGqaRD9L3ReFR26Fu3hBco9P+5F5kEJ/d7Zbcntd0W2gmacn4YdOqgJsM/mi7QD0Bg3SN5vvcI7wjzDrTf8jQG0VEPf3vMvLvhOecBXkARD+CEcqcPYgAYdKJ7D9Ep5Or6bo1v+TuivwLT3OELKA7yGcT7FGbvDKfRd0kjkLTT8/fq/rTOZDAQhlDZOSkIkcD3Pcd2EyBVPaXZ0xMgXv0p5foodqM/aAUB6iAsAH0ICBGDxAGofzedUAA1QYbdrf8xPZ7cAqTwOhdIC1pU/wtkgEyZoqUBDgCNzzQHWOHTnRTwMLAxEPHDwk1klw9hpq72KaA9+aLIpsj4nQeeg99j+y7LJD6gaoM4ArbsJ8z1/NvDsx9yPn0FhM2mbLwv+qO7n7pCvy89f/uW32X8gHmQ5OlUtX9nHAgkV9bcA3XCqAbgTOY/AwhEwr1Af3nU2EcR/5Dl659a+R/+Wrd/r5qnP3ruKxS1bdl8nc8fle690H0BWTAHMRKXfnMvep8fmff5mXKf31PuM+D6+Zlyf6D/MNdX6K/J+AcSz+D+Ci2+wF/gaYiLXX+K3ucFTEJ93pw/o9Pot1zxv/v6GRATzqYDqLIfRed9Cqg8Ye2H0+RHEWqm2tWDcnlHXeCNb/lHPDyzBYB6Hk4Vsyl+l8X36gu8+3DeR3EAQ3kLeHtT7xb60+YmncRv/JeveZemry+5nfn/9qZmKgMgboFJpg0RyCHQELWxf3/6aI6mhz/u6O7ZBWDBK75OSfYKTY3sK/TRk75C77uE++4r78A26aepH55Ygqngx8fcj+2i47+AzVk7lJP4j63P1IY92+M/CzHlFpD4DstTsXom68TxT0TATRj69Z+JiPcbO30iRtPaU6GO2/c8b4CcHmh7XiHgQJB/IKUAUnZgwZ/ZAD61X3WgInqTut/t912t4qHLb3cztI/9468v78jx9MGzVwTTQYp+bqaaOAfBChiC50dYgbH/6y7ySQdgHuheACEsQD2fWBFrGIXxFWwvbNhGfGQZYIHvBC7seL6LO47nIT6+cLEl7GPLACEw20M8AO0BoPcI0rdHkQMkl7btEi6+QL01bq9cH4EdxPUXy4WHIz6MrZGAIHwUmOljaQIA86nwQ8HJmh8N7WSYp96/vjgrFMxk0OZAPi5qvtbtFYo7QuTM8FUQVheCgNflkHSLFDV6Iz+h+VLeCPtmSIybosmrU7LMLIZOdSUrUoTfkQEw4Pm4zq8MfTAHAk1WBnuzj+SyTUKfKXHOw7GtKMcULDepo8PVQRc0XagTuQN9MWOo7P5K64i+PFpYldpm3A2snirsfD6vHJHKWI1q6vIQlQGfX1qlM1Uj611GDBb0IS2ToTWOVhb2+4hYsZ3CWq2g7JAurbhWuInDWJiKnXWtUyiNXtjU7spblVi7W3nlB04zF0dr8LuxJkxrWAe5hGrx2qr2BFynqbVZtJqd1vWZqmB1sUjPSVNSt7ELrWtqnM2Nv2RL071sD16Kc66Un7V0LLVRUfjqyLMlfKFnboLFmLvSB4OLFDz2ZXNjuVm23y+SuvTZS7ylW7VoGa0YB0U39JXjXZKzI3mBWncpfrLKOnUb4uShg8X2St56tzISbzpVCZZ5oHOVjCx5nhzTgOJ4UzDioM4D/qBSK+RItySpI1GONe4xb0uXwwjMGH2tdZKtOASLMIdNtlUjn8Nbu9/V+3W0bkYX3vRuQAwUSgdnIVouolqvDS0SNCanqyQbrutU5iS10WK+3vhS5PvV6cDCkRYfG0wM93qz1tauhTWtKYm9xzrZZoVhlreeF9q51keauHUMuj4LeBKzuIQ08Lh397d8p+9LN+Mx9iJ65iK7CdE1RXvDFxDDYulIiMnrbEkVA73y9xekrEba4OeEpkSnw0EieGN/tS6xy5eYtFFv44azz0RE4K1nEgjdVQUrYnNhl67OM+YUgajexwJFNxeJbdmca+xUqrNMM2mhEa/mcaEEV257MpmVFZnoQcK4FN1v0QOz3CZ7DC6oVJtvZmc0N/FFP1e07QEXdd+LmF60NY7QCd05l4JCW0YgpLu40yvdhn31wBjm9ly06O1CLo/qjF/Gl96w9o3lYKoXcsj6yOqXRBA9bbWt55Kr88eYZWe9ZxeRE+rBpqFWJ0Ve2EpJo0WGMt4uIsuu2enzjUmqKXcogGGkbXwWj3tinioZDc9Zcxxx5bbbNqmbrI5XWoxvcaLQh444EZafbN18MMvdJlv65bowMu+2H0/nIGqylhYNHmcCVFoJcIGdODnlip5ge0OfH1PXrIaR6YuTRTqUUDdlBTOn+U5k0fYg5DZFbTOOQvYzLizZS2DPCn825OrFncXXoQqHRE3Q3T4lsV5m2NZY40PDzxJE5ZThsrtd1+tAkg7pyUBR0+RchkjVDPE40AKmDmIuy+Nq4+lGvaOHrbK4xIEQ0dz61LXq8nRJF4h2UPwrK4c7kehlsRSDTXpTrWYBWgYngqlgPF0ItW7zYYfGXmCsjqfDQqzy2WZR7m5WKmy6doZh6xHP0h1P+cbOGXbsHvcAGoGqhW8p75B2KovGhpjzA7ooLu2GnNl2ZlY80VVaGBTOjeMjl3Nc/DLzu0EvhW7kl5InFnxrCQU6X2CaXfBydyFHruZt8bDeC22wEMK8SbN1kZtXCu+ZyLnheD+n16jkrJltepbXpk8f9/F+6dVK1UiXjchf5B4tNvkpUsruWLqigWXkUtL3FCcZwdKA442tJXNaH4mDwx+svIxP59mFJtZu1KziLMnFRY4VxJJAlcDf2CGJcmYqdMmWmyuhXlbknkssc7tRBjWMeGWJqomjtitjdvKUZXrYNBHPomU49NvdLhWaWO4xtG+Y/XGjHgAkCjS/LDnlOoZFfslb0dzRB8aRRm6zaTGZbr26viB05mZmtLewxZqYjzAumvT+nOyW2tFAV6MjDbZu0dpwcXPBSuZU6FOxTMzsmc9IdL5ZLhCp4dJIjtgLSs3zEJ6Z+WXBpkxTStLc36CRS3OyNgICetSrPZXbSXk4L7WlntGnfWbG2OKU+WR3TWbX7KxunPDYkZE9ujrH0xXviBWbbyoFy/ggPm1gjGUzQ4VPWs/QJ/QYR3P/tNfpUtubjE4Vq+K4Nqy2IOf2AUlXNbtcBWIVsWK2Phu+ax7LOb+LDRtPj6OXrXjOu5i03qqnWNp16WHA956xRGmtGsCeZYEazeKiwAafI1E/HNotVV29o6U0/oxRg75YZ3wH8IWXe7MZTRGJ5cpFrUpjMEzELL5a54S763ZZycZnWndBjmCzcQELNxo/XG75Od6BdnCmNgeKb86dGVFtY212WeubVqnfDE2P5jcR3na0TLM1e4vG6qIWBzHMlpRcGssstg+K5zJzMOomDcmHO14ITn3dMn5okOoAwHrUF+lNIByytPiZXbFVdS55dXtAiq272fY8F1d+DI+G73BLoiSPm8ao4E16WCW6Xq6rg+GKW6s7xKTW07v13JxpOGxl8LBMjraVRf6u5km0uXnmrQD1igmS1SbC97e51ZV1JtHCfi3K3V5rVUSvuZllcaMiCG7L9tKqrROMPl8wpFjvDnLnE4uS3t7WaxzfaYVmMKya3+gLjBfDKYzaQ8led9Q1U1O4gAmhkOyGE/ZhQ2l5vMc3V94odWpB09RuIwuVVPOV4W6oar7S6LUvdNx1GbEqI5C8mAfzM7NEub4UW1IZeFM6nkAyM6kZ8KvVLvNUA2lXmo6tpHae1+OS7kOep1J15x9Ej1/NbielxxlNTBbYyOxntzXf1MlylQujtDx3CszWi3aNl2CXhFq8fFyuaxa3FXIH0+SmD8+tdAkuepzk4RyOTqUQ7o0yFg9FZ5ZL75TzcBobhRkKkqZ7UucWPCwy+d47qIsqOsluoFdn7oKoMH+qCvPqh9qKK0ku1fe4OaanAqlxWuypWUmda8NY3KrkYjjU6nwpdXJbG1K126i4p5MyhmV+pqU5SQUnd2OxihHFibyqsQSptjmjYprlkiUnDBQRBypczlF53MJwTu9n+YqJttcLV59pc68PUcpi2XYE+0Y52e3UHebb9ra0VjsGbYnZrBDYnO8KbGVGSXvj1XzL32yrjB3+LKT7m0R54rUX+NwT+hLES6Bv5L2wV7jy5mbKZbmyktSoEdYSretBzyQA47NcOO/Wab/uTkS8gXl8UxM3Z7FgtRsKSx6m3jhsOaQb0AwZvTdfDWpc4Iwvdgk8LszdYBDJSOha0BkVxvFz6aSiXNfEXIUZvJrRh5MWemhQnPkTKLeMvr3Jx3V6OLk3uuWVHRddxE2HyqwYjGNdiUcbycLRFpl0P3CaMPaDG8v4dYHNN+uF1h2Xt5Vid/EQrm7EaVaxcKhatVDJeb+Vkr4PtzF2HAg6CsktSx9vCuctdqK3O2KKVRLakFZ14BLh8VpolrVt9Bu7w4ertz1qSoPboO3aW1IeV7OFR6KMxscon+SVZsFKMWPXJhHWR/mCBi67XLolwrZcalliLtWXcJ0Ul4gK1xW7pfVD2Wy1c34WigWyNkPeWikasqQCeVGRM3aO8NfmWCK5UxFH0BOcdwoWDKuevclmsMRlLpD1k7MmRWMp64YXp8Gx8DUynW+szKI9pGad0vd0ddMt8pXaYIV9UDnpUmLmsahTze1vMr4llYa5FQWRH2iDha1eL+g4ygZQn27pytHwmWpV3ba6kBq5bTmcFcDGR8TrWS4bKpeqJLOlzdAYa5I/50ah7ZXM8I8kpjn+gALfhTCoQocOrtk0BvudYGjhIs9j1sdE4HI0YkzQAZeafAgT+1TNVlobo8sFTHvcSBQXlQnaDdwg3IJC1LmKzgPZ1W4rsF2bI3Z+HQ3dY5HZII4DCrb2AUXj3TZe7VnE7xb9mfOX0tY7Dw5VpKU3YNtlvqsaRkNs4aL3hjLflIN4ZXPX9DbtZra5LJDVwljwO57rYzE9jOUy9nebfD9ftOccDfeLbXbQdewqVT0vMCMJy6f9ikVdnE1HB8nP6VrRL9vFMcBVihEuBV5Qwvy0cIfaa+uzwYzd0F7FBvRVDlzMhP64VjxchPerOXNw50EQzBs9gJk9Xw3wvOsCNCOuDWgBJVWcdwkdWGZz1BINoeqYWXRJQTCSspQV4nLqA5OS9vl6cznye/Kmz7masvpQEEHQkTKMEiFRXtx9rzGHIBvFbe0btm06nU6MxIlEnJpH/AjQI5nGs9gypwoRC8wr67rncVdiiXXIDLP3blpiLB0x7SXZbPvF9cStLksKxcdjQV9ABzZD5Rk3NnU1k6/LBZatTjf9wCJSsrsGxGXlhDwjj9Z5BEIUWSrlxQV4oTOK+WJhVtd5bc5d/nS0YMFEdmq/PRmylOeoyZDrFps5yLjTzi1wLUmcY72hlqAGNoG/XF+FEKnKq9nxW24/N0R06XR5E7TEVLRVELprpPIdUs7RC2ep2x13AtWu4pA8xXfnq2pg9szOowO1bW6RHxQdzQW7mru5UrBzt2t2Q7h9dcn7ghcJuj1kzFWWLkdpjEc6jx03sDYEut0YjXWluAw9ndYzh54R4lYpRpJHZL8icTrr2+s1xRMiFimSpztSO7PDVTM3fbET4+W+aCR8He2raolR+kzKzP6UUu3NJLQWXXQjEpjniu52SyK3BD+uM6s3OGVL1Evc7X1yKMCu1e0uc/KqKQ6OarXdunk71uUtx0MZjW7ednBQoZfP4g0927MLuR7cZYiaHMopOELMkP1cMs7rhUCWMrdpOrG72CvT29Y14+l4MmpIwLVGSUcV4+c3cwN3ilTgPrXh9wTJbuM8h7dyN5t3t0NIDk3QWytpLBbOgQiYgjlng7Oq87VUb5tlhvQDEpM24109hOoD38ADbDgLaLfC132Xex6B8QBOQmmN3OYrfTuGAh4RXONcr7U9NxIBwRWZxLtoBm9mPOgzrgo2VrhUr2fUfH6kGfGoIZw37u1ZwjAnbj9srxS9k7d5VE3H/eN8LorhYr+43MLWNHkz6HXCRJP59gRve1sO16Z5Q9E5QsXsqvWdJbre6hicLg94YGSEPogEYkaClgjqkW9cYutHo03IO3i/gVNqK4wyNmC31c7LjLpyTnyXIbUzLnAbT3LtQuiVTIe2cvUu+FU6Uf4YERK9cY2F4B99oif6TcOTet+KdNuQLlIMxZBfq9FWMnnvikMsb5mhdi6nRFLzorbHFE3zBh0vHNrVVwQ/UPPglrAunbsswawXWTG7UbZZdxItNX2L1244zObWkBDovjhegvKkdbWssEtMICxXjcQy4FuhXK9HcYNdNK73fRJRtRDWc24Ib3AuW3KzEaVxSV1nsSwWRIyP2uziOspsPRrMwRNOte9IJlN62rja4idfODMqK5Pky+vLdG79PH3+y5+bp5PA/2cHko+zw/evUvejZ9/2vt55ff3rov38+lK7MRDscQjbpF34PKr8b0ewn//dbxoTleHxRXf6mHZr3w/vWzucfknpJc69DmzQh7emSLv7YfArsGkz/a5E8/Y89H65K5mV7X3sQynwZHtZnMfTF9e3tnh7nENP7+N8+k7ke/H3x/B5RP364g3Ad7HbvCEr7M2vy0nt57eS6UR3+ljy8tv/AfiR+JwVJgAA -->
