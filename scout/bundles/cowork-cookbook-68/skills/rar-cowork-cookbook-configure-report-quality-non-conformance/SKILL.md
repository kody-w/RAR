---
name: "rar-cowork-cookbook-configure-report-quality-non-conformance"
description: "Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_report_quality_non_conformance", "rar_sha256": "826f8bb290cc75da099919a06b1000d433178e54582a84e8af8c37334108935c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_report_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `configure_report_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report quality non-conformance Configuration Bulk Setup — Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 826f8bb290cc75da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_report_quality_non_conformance_agent.py` first:

```bash
python3 configure_report_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_report_quality_non_conformance_agent.py   # or on stdin
python3 configure_report_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality non-conformance Configuration Bulk Setup — Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_report_quality_non_conformance',
    "version": '2.0.0',
    "display_name": 'Report quality non-conformance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-report-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-report-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '184d2447414bdcf0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/report-quality-non-conformance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-report-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReportQualityNonConformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReportQualityNonConformance'
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
    print(ConfigureReportQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abebSNLmX2Hu+8FVL/Zl39ynzxkktCOBBAJEuY6LHcS+iaWm/vskku613V3d0zVnPoxsHwvIjIh8IuKJyES/v1htE+bVy+cXxbMyaGUlSRR6FWRlLjTPu7yKwX95bIN/kJNnTRXZbZNX9cvHF9ernSoqmijPwHS+KJLIqyELstvkPtaPgraypseQE1pZ4EFNDlVekVcNVLZWEjUDlOXZp2loXqVW5niQX+Up0A1FWdE20KJ3vATyo8T7CHVRE0I3MMt9iJwMrPIksS0nhuq2mMS+Aqu83kqLxKtfPv/y68eXCHx/+fz7i5NYNbj1Mn+a5Z3udhwfZhzybP7NCCAkAeaC0cUAsMnAdeFV01Nwy/V86Hn1U+0l/kfov/877qwqqH/+/CWDnp8vL9OfU5tBTTgt26obz4Ucq7DsaFL4CvFJZw01gKNpq2xCrQbQZsHrY+Y3SXkB/X169tNDyWvgNT99ecmBCXcYvrz8DOUV0Fe10/fXSUrx08+vSd551U8/f5NTt/bVc5pJGLD69evz+ikWDPw2NPLvWv8OpD5cbHtfXr5b3PR52D2tE8x8eb3mUfbTQ3BR5Tcvm3D86ed/JdYJPSdOorr5j+T+8hAcepYL1vQ0/OePd5B/heDngt5l/mu1BXDrX1kJGP6m7iP0BOpfyb7j/w+ikygDCfGG+J+K+7MJ8N+hX/7l2v7dhI+Q/+VF8JLoBqLDTrzP0O9fFXkx/+WD++3mh1//AKL/j2KUvK2cu4SvICki36ubr19/+VDfb3/49ZcPbQFizbPSr22V/JnMP8P1rucHBJ+jfvpxLtB/zuIs7zLoPdKh3/Pif1R/vELaxAHf7tefoe/zZfrA0LSIN6UPCL7LmRrY+h2OP7/8AXgiA6tpnftjkOX/9V/QPnKqvM79BlKcHHARcHATpd5kvBpGNQT+TrldeQDXOgLAPseB+J88PFmc+9Bv/9O5kygguQeJIm/E6H19UOHXJxV+BVT49Tsq/O0VUoH8vIqCKLMS6MTL8pfMCrysmXQXlVd71Q2wij003icw69P0BRAn9Nt/quLrXdprMfx2Z9PowVan+WZiqrpNvNdptXroZc+1OYCZvd5zWqAoyR3rwc31R4BCnSc3wHQTMnUcJQnkRhWAIa+GB1O32edJ2G+//WZbdfgle1ArAT1KSI2AAe/mQJ8+geX5SRSEzZfMc8Ic+vD7Hx+g/wX9u1l34ZMOGVD90zfAwq0iHSCQa20KhgG3AUcDIrn75vc/niADMRmoecCTkT/VsGkyiNXYc98QV9b8J5yiIdsD4AGU0wlXwNdQ1LxCGx96t/dZ4CZGD/O6gVyv8DLXy5wBSLXAct6RzPIGqkFA1v7wEWpr7671N7uy7iamIOmt5jdoP5dB/ciTe+181hMwOc8iAP97PDzuAyHVhxqavYl4hQ5TdEKFVVlFWFlPHb718AuoG2/TgXALyrzuSzYVTG+C6p4qD3jAIICM83Tpp8nnoL6nIIbc+k33fYw1VTn1Xu2qL1n9TAOrmlzhgLIAlAYtKOAg9v72DKk6zNvEveMHLJ0kPb3gPr1yj8HTv+8a5j80G7Op/1AAsRTQlxZHMRL6/6I3mdbBr1anxYpXFwK0OKinywPfqa+a/PBoxSbVQOcjl761DG+E88a7X7IkAsFSDX97jLx75TnmwWWAAFxAG6e7fBASAN9J7j1ipwisqjsmX7I3gv8IALqzGVgCSG8Q/hMqbwqnp2+WhiCHp+tvxf7u4cqdlg6iEipaOwER43ueewehCasp657+AMh6UwZ2YeSEP6wKAtJBlAD5EDAiAnkEisAdukMOlgkS7u6F9+HR1EIBK9zWAdaCxtV7hXSQOFPw1CBbQR80jQEofLiLglIPYAxMfEe4Dq3iYczU6z4NtCZf5CmI5+898Hz4LdTvtkzmA6kW8D3Aspso2PX6h2ff7Xz6ChibTsl5n/Sju59rhb6vRH/7kt1tfGd9kPPJVMS/AwcCuZbW95CbKKsGtJN6zwACkXCv16+Pkvuo6e+2fP6nBv+nv7YHuBfR84+e+wyFTVPUnxHkUfje6t4rIAwExEhUePW3GvjpkXKfnin36R9S7gf5D7g+Q3/Nxh9EPIP7M4S9oq/o9EiMHG+K3ucHQDL/NLt8IqenE+188/UzICbaTQZQdN9r0NsQUIiCygumwY+aVE+lrAPV807CwBtfsvd4eGbLg3tAAa3z77L4XoyBdx/Oe68V4FHWAN3u1MoF3rTZSSbza+/lc9YmyceXzEq9/3yTM5UFELgAk2mHBJIINEhN5N2v3pul6eLHjd49vQAvuPnnKcs+QlNj+xF671E/Qm+7hvt2LGvBtumXqT+eVIKh4L/3se+7SNt7Abu1Zigm+x9boakte7bL/2zElFzAYsebSn3+nq2Txn8SAr4EgVf9sxDp/sVKnpRRN9ZUuKPmLdFrYKfbTgQPPAgSEOQUwA6g+SdqgJ7KK1tQId1pud/w+7as/LGWP+4wNI/95O8vb9Tx9MGzdwTDQY5+qqcaiYBoBQrB9SOuwLP/667yKQeQHuhmgCAWp33WtnEOdRyGci2U4ziMs1DaxlAUdUmCwBjWo0iKxS2W9FjLZx2CIQgSQ1mOoBwg7xGlX6eGIJpswy3LYR0GI12OsWjHI1CbcDwMx1yG8FCKI3yW9UgA0/vUGDDmc8GPBU5ovje4EzDPdf/+YtMkGLkm6w3/+MwRTrNoQrT70IBH2r9srmy+VY6XFqYSeperurl0R1aRLCY7mLOjFNWtQvDXxSYJ+X15O6kzMlKpIKMNX2KCTaDsW0NNHevab0/4AR9NFkkkjjP3fDRH9caky1yXR62v2rLZrY+9aug9djinYrIpxtvMrMy8rIpz22/36a3fGHVK7VjvJt/Iq1rXg3aYb/T5EY8lQlZdbaiLXYSVEuNfkqy4XgIxv5RD6RgUjqnppUwG6bQgyoQWLXrcVfuIHBZKwo7DFgWtcFqIi7CUT7R9yCoW9jObpBCsdG7EOMK35nhbJiJaWvpJIaIiYaroaq+u5dbbDbLSbjq1d6qg6ks15cRzcumIHOsSTeubNddui43lB0Fy0K+eNu7VCuWcWk6sZbWM6jKW+9vGDsp0J1zXPNqYSprVPIkxm6FY0y06tHUYG6x7VUtOG9dmjCEJpcNJoNlFsSuq64bmgqucDiej1MJd6q8pejzHptSt9eVxdzsdCYvSW5clrxsxs+K0m8005WCMzlKVTYUkxuXQlHB2GdQuAfYV+dkrqWR7lntCLduTez6fouOAjQ46Yx2/HuZ9bM+aQ5ofLM7sLdU4YSe9WhYyxylWa7pIeRB3yn5GeyZ22aJhFV2qgF43BE/H55TACrm55RSFClvh3N8IW6yMzJ1Xot0GTXYg+3W1LJHN0I6cvGFVSbTGaBcmjbpwDCYuq7y/0FPKHEWZps3d1urSntcQe6abmxEhy5VrGYNBqn3vKht12ONDeBFgXdr2c6Hkznx1OFNhMCDMuiqZ5IIRWkFVB3MIGrUZqD2nW6toOU8OguRb2baM8VsZpzWt7GjYW7VF6wek4NeKMRfk/iJ3AzITr+vheo7TGX1jZuuVr245Tl7ji2N32FL4Xuc3zeF2sjfatsTOutmaWS8uwddEG4/UJfbM+tBF2XW1V51YzMfLzliaF19YqO3OM6r10XHKClsZvbsUc30WH5ZXCx1nxqKChQ3PbfBo2LnFchOrjtpGx+6YGooEB1W8KaugLuhREuaOtM0sNhIcJYelW7WGUyJeuedBrJJ9QG0vWzUvKLWP6eN+8LdeHKw4hx1NJ2f7645AFXfuzhtJT1um8snb8XCrzFRSMLkkS1mtaCJMarkYBDHMFzPEHqSIzQ1ivRiX0iqQFofoMi9K4BMH6RxN1rldgi0RPJznfLtdwVcdYDDOE4lZS/NZERfhzkY8XD+cDC7Vx3BbKDaNnBBksU/L9Rx2LlGWVsNcujamjQ5Ve6QPepzDMnUg0ZnJkHPTYEttpR22i7pq00XEWXZxPKLLKGGVPSxUQ7gz0aTWVoW6JWaq3Es3PNkoUQZTUnhI5kmiIt3NC0pQ0PMt3o7GceuGV/XKxnEv4YHSxzhKuZWYO33HqDt1k90uwDmSppvNLpfnUjAqJXba4fjcsai5pzVdk/CWvPdHjjtfzR69ECZcCNuq3OLxCkZkFo/HaMsKe6ouCzIjyBWGxLYrm/I2NTWD2s94eCepnEewNRYiTgFUC0R+6ajDcEy5q+1pPczy5KDNRNcJxtUxx40F3q7lm9kta8psjhGnNXSAB5TUH+Rb6F/Cw57BTtka3dwyG92mmkiXDqz7dCT6Y7jkyCVqWUee76Jk5HTuvEBZVQebNR0T+I0Skwt7AW8XmE24LfBYutv2XXAo0fwYoQD6BmsVLTI36E1cFrySa0ex2jppIShEwWpqOBKZGM3juRlSfcbjThniXl/3TDpuD/72uidpGLYp3AejiL2i2CQWhes8phXlKhRw2bUcbh66jXjNUWGPyMh44vdM6+WMOzu2UnZlkSEkYe+mZKeO9bZaSnObdbQMzg1yE3fNqK9nIr9zSyUOr6ZMcv0miAfM2JXocFxiLIGxo74/X3quW9iKFVFu0PRX8yCcqYMiHvqBVHjP35zO+qhHkcfnZTbbn3WGz4gcrSo875vM4EmZJjBMklnQjWi7OmdMdlvN1BmO5zhlbAduO54NZrXYlU5ohLcle96IjieijWTA9LE5p06fGRbeojxdcNKi5/N8EY6msXPGqmLUaMkgp3RcaavralWHC4I3XczqqRvFZhdnT2NpzO61hVdswmirOeP5SngIMTTYgtkk+ZB35IZvZrpfk3NDaZXdPj+FjXnYrkrKu6izWWg6cDQvz8dAZNHM0teR1WenAvEaQxcwfGFSQ9UF++Da9jeh3iWMLocxQnaXjS3yae2ZRxvz1xtRDQZ4V5Rxx6nmctYUMlWaay1JZzf+JqCa2hfobj7fhM7CPtuSrRLrsSNmF4V0lyjfaIUqLVantts783Vg2cuaW66v7rLN7CEWWWtrm2dJv+InF4vBxswscHJ0zMVc20hbGu3dLYGP2DVpFqc2DVFScXo3QjQsy5yINMuNpcHX+W45uqkVjwq9QlKjUmMxRJljuLIGOA0j9qy6hqjXAlyBYnrytpVLy6f5QsxuB3vQm3bGCZF2nrVphyI5qsTc6hzHJywVl3CkO2QCw2WyCtTotqtOF3Ef03lSdza3wGK0Pp2ORS2SpXTdD4YzAzlMK82p9l1DLtZndGcFJ3rpt6jcpEZdSG14Gva2LJ5XxV5MDL/m6F3ZKJfUdDCOX9+q1qbdGzE7b0h8s9I3K5JncMSiNqe10HIIrRpE5NqiTJRK6tu0g+9vp9DMlCLDGQI2aAE5kQN/ZpiaifNFctJzfrUSlK6E1etM0cOsFqh1sdw3x8E5nFx5Dar1aLXE0gmsGe3LBrFout1iBWP1GpaazRGzkkxxtHNKGiFzJZUzHWu3MzcnI9MZiq7d4uXFqkkpI0HJXO23xFpjq/MCt+aWcy2uh9OmpLZwflyKLXaeCVlKMdVW3/OFk87UTZhSW/ewLG6R6m/AZl9MDlgfxTVzFIctJyoZFwqOrCqObuPC3D0x7fHcw/AmNzUdlZezY7lw1uebub1mq1g8zLR442/Xu0ZBb64QDXiUbkUz3MPWxdOJtbxk3CyUlgY9R1P3EBQpt3PP1NHCVolo9g69t3e0GSer6pKTTW9tdQLX6B65oWa605QE7AeMNiAuui9Jkat3Uk2sxh40i5ey6Vea3/fJBQEEhAyVkpLj2tLb7DyT6wtpEk6pX62G6w+AI5l1cCC10TipJ4Df9hQ5802c6Fl0TexbvMlXw7Wzd+fywmvKZdgZK7zmPT7sYzkNUPq0SLCraBzoDkldQ/IDFMFGnGN0C9A6fpCaDC3irXZa5IGFn20iPAQulQv1folbanJZVluXLnZjMRiL3QwtC7WLRJPKtJ1k6BgTMIdF2peri+BoRX1y8lAnrzMLrQ/pgTaQfZLNi4AJUnMfM6rZyHEvJyTT+31yOi7YiKRwdoxXtHChSkFWTu7OAe5YCPPzPFHYRZQzRbD2l4LQpCmss7OrPGz2bWqTKwE9VHUzipcCph3mZoSLXBn5K1K1EivU5yUx7rA52D3FODJTj/0QzfsaHW+iEFl8OwoH7lK0G0VzZ0ljkStKv2TWqug6HGuvsWLpN1NahNEJX/FEvgZNPZttZFJBzUrLl1GYDg6Nb8HuQmVw5Wy1QpnxNs8fJF9pNIds6QJfsvNzkPHRxVHlpjf3xrJYWiIWM+G12YvrVRI4iTAn4NVJi/WR4DDTQjV8hjRkpwvO0uxxT25DsaLTy3G2pHXR09UmuNIWfWvbdHmcoRK8EvpLYTRaq8Gnvocjan1Fq6zgWkw+IJ4WtewydomwOwAK7MTRWWvdXoMZhw9InautFd0H2VYDi1iOl0Y6nNU2bTVRGgM2gwUxcFNNtmG6soVKWDexVjf05XIRwqW/OtHqbcFuvFJEGKeTw4XXC+n+6AfEuvOZ262wnXrOE/s1kl0rIskPnKLhS3wro+XJuHYLk5jhY20H9XgLl7Wo9iBlkMQ4eUfBuvjri8PUOnW1R/dyRT2p9BF6YBGS941d7e5ImWBVmSH2bkIRiHwrZwl+pvUzibp5tZmxVmHJ/Hg++wtkxh0IvLNPLnKMvdMskKXxisZo2EgSI86PaIcEdXh1Uva43vjxiIi5t/JMvSk1dkQNnrDssppfc3YtrJ3QGsZIOMI4lUkXjjpFB0VdMMc6rwMGDrYHdlAZEoBhR2PmrHANFkibEbs5FwlLxNn4MwrXMH9jOFduTokXOpgrI3pKyEbAKsfWZ8HQ6Rv4MHMP0hifqguCi2efKendCcFuCL6SFs45M1jU64SFcpKNK20YPNtscZcAG82L67VYR14iIpjhZD7WiI6xyDYi6BDPMm8Wj365dnyJEHCZ8M6iPTscgy1iYv4h2NjkMWEbPlq2TrQF/QKeutHeyNdO48NH0PsEzP5iZKUYKkS/wx1D0HqRR5TAX+93JOXsBGGc2cp2xqACOahsXnMWmRBr/OhLfKdVK7uLmHa5yPzx6MtZ0pFuuDrkssY7Sm8qBNFjo3cSZry+SmdbdmEZTRbkZ2F9soXzas3BXZaUXHtMqiuVsMtCyRwV2YlSU104AsN3oR0eMpNQjRxsVZxlhB6RHRcQyjrQy3OuGmLOdSLgYRhe0HhlbBmHph0TJhfSxjGObNqKzmUl1N5qdcs7ns0OubQc4HkNE+ScwI29TnIY15lHMQxqCS4tKjNnFQkyzI5H1fCyBm+WYbn2BGAv6mlSLnrCjBUdHhO6tKKHo4eUbb+/8lHgdz2M7XLK2jj+OkeceKjoImv21Sr2MuZIExHvLdybsxIC39cZmwGOpVp6RM7t6Lk+WQmrzXGN2BTS7EIKbN1MWCQUYjw1fqNtRMrITyZ+ZFwEkcUNkS04KjUzDEZmPpImyZrPGawlr66vLLHZIpsLt/lyfxSMqLx6fTu4o3E+UitMpaJmrR6Mm6Sxa7Txr3tUOCoq2DZrvcOCprLdWAefRRwPtEuMisxtb5U6etehmNEVSgK7S3q982fIkWyks2AJPK2EQgrnF9IhOUEfxYSm0SxhGI+rJKO53npEC6IZqS73TO7PCy/TUl4OSVaO0qbqbrd4rV+kgNfbxYZsG95I2ZW50FTqaA8XjB+L8Ty/mPBSMLnowu2k1AViA91jQml/C2iY9upOhpH2nHUrra86lSFsgVpsm7rNSQMe50R7gOeiyGW70Q8tPpJ6TZvRoDmuxKtGeWy52BUIWrhd27qpXM8d/5p0693cXs872kNX29gS7QW/xeEyPyMLfa0tzmfJ8nsOjSS5jWDqekV1lwCzxZEmruiamN1STVJ2Ac+/fHyZDrCfx9B/+TX0dCL4/+xg8nGG+PZ66n4E7Vnu57uuz3/dtF8/vlROBAx7HMbWSRs8jyz/4Sj203/6cmOSMjze9E5v1frm7RS/sYLp10svUea2dVMNX+s8ae+Hwh9f7LaefkNRf30efr/cF5kW00n6u+KX6fcM04l1DiY3+dfnrz/ut6e3RZ4bWY33vAye59QfX9wBOC5y6q8ETX31qmJa8/ONyXSsO70yefnjfwNQMolzMSYAAA== -->
