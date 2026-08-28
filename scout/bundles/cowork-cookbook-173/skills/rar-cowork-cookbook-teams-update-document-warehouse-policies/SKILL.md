---
name: "rar-cowork-cookbook-teams-update-document-warehouse-policies"
description: "Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_document_warehouse_policies", "rar_sha256": "0a3afefe6ed23305d6e25cb7258f409bd6224fc8a41d0e62d611f928fce4001a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_document_warehouse_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_document_warehouse_policies_agent.py` and in the RCI capsule.

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

Document warehouse policies Teams Channel Update — Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 0a3afefe6ed23305…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_document_warehouse_policies_agent.py` first:

```bash
python3 teams_update_document_warehouse_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_document_warehouse_policies_agent.py   # or on stdin
python3 teams_update_document_warehouse_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document warehouse policies Teams Channel Update — Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_document_warehouse_policies',
    "version": '2.0.0',
    "display_name": 'Document warehouse policies Teams Channel Update',
    "description": 'Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-document-warehouse-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1df7d79fc9e42459',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/document-warehouse-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-document-warehouse-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDocumentWarehousePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDocumentWarehousePolicies'
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
    print(TeamsUpdateDocumentWarehousePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOjSLLmv8LL90NVP6qSU4BqbMxWJ5eEkAQ66Gqr5gjuS9zQ2//7BpIyq/r1zLzptTVb1ZECIjzcP3f/3CPI317MuvKz4uXLyxGYKcKbcRz4oEDM1EEWWZsVEfyRRRb8h9hZWhWBVVdZUb58enFAaRdBXgVZCqcvC9OtSsRENGAmJWL7ZpqCGMmzskKyFHEyu05AWiGtWQA/q0sAH8WBHYASKSuzqkukDSofrosEaQUK066CBiAzx8zvXxZm4SBuViC3OrAjBOpheuAVagE6M8ljUL58+fmXTy8B/P7y5bcXOzZLeOvlroyeO2YFlk8Nzm8KqM/1oZDYTD04Ou8hFim8zkEB10rgLQe4yPPqYwli9xPyX/8VQRu88qcvX1Pk+fn6Mv451ClS+QCpMrOsgIPYZm5aQRxU/Ssyi1uzL5ECVHWRjjCV0ITUe33M/C4py5G/j88+PhZ59UD18etLBlUwR6C/vvyEQBC+vhT1+P11lJJ//Ok1zlpQfPzpu5yytkJgV6MwqPXrt+f1Uywc+H1o4N5X/TuU+nCpBb6+/GDc+HnoPdoJZ768hlmQfnwIzousAamZ2uDjT/9MrO0DO4qDsvq35P78EOwD04E2PRX/6dMd5F8Q9GnQu8x/vmwO3fpXLIHD35b7hDyB+mey7/j/N9FxkMJofkP8H4r7RxPQvyM//1Pb/tWET4j79WUJYpgfhWnF4Avy27ejulr8/MH5fvPDL79D0f+jmGNWF/ZdwrfETAMXlNW3bz9/KO+3P/zy84c6h7EGs+lbXcT/SOY/wvW+zh8QfI76+Me5cH09jdKsTZH3SEd+y/L/KH5/RU5mHDjf75dfkB/zZfygyGjE26IPCH7ImRLq+gOOP738DnkihdbU9v0xzPL//E9kG9hFVmZuhRztrK4Q6OAqSMCovOYHJQL/jrldAIhrGUBgn+Ng/I8eHjXOXOTX/2XfSfOz/SRNrBoZ6Ft9p6Bvbyz47Z0Fv72x4K+viAblZ0XgBakZI4eZqn5NIclBzoRr5wUoQdFAVrH6CnyGfPR5/ALJEvn1313i213aa97/eqf34MFWh4U4MlVZx+B1tPbsg/Rpmw3ZGHTAruFCcWZDrdwAUu0niEKZxZCVqxGZMgriGHGCAsKQFf1dNkTvyyjs119/tczS/5o+qJVCHiWjxOCAd3WQz5+heW4ceH71NQW2nyEffvv9A/K/kX816y58XEOFVP/0DdRQOu4UBObaHQToNuhoSCR33/z2+xNkKCaFNQ56MnDHAjROhrEaAecN8aMw+0xOGMQCEGmIcpJnRQX5GgmqV0R0kXd94aLjo5HR/bHUOSAHqQNSu4dSTWjOO5JpViElDMjS7T8hY/0bV/3VKsy7iglMerP6FdkuVFg/shj+N6p5HwQnZ2kA4X+Ph8d9KKT4UCLzNxGviDJGJ5KbhZn7hflcwzUffoF14206FG4iKWi/pmPBBCNU91R5wAMHQWTsp0s/jz6HtT+BvOCUb2vfx5hjldPu1a74mpbPNIBxB1GxYVmAi3p14IzF4W/PkCphSMbOHT+o6Sjp6QXn6ZV7DC7/Rbfw6C8Wz/7iUduRrzWJEzTy/6UJGRWe8fxhxc+01RJZKdrh+gBybJjG5R49FuwD7pPvSfO9N3hjljeC/ZrGAYyKov/bY+Qd/ueYB2nVBUTrMDvc5UPfQyBHuffQHEOtKEaDzK/pG5N/gojcaQtiAPMYxvkYXm8Ljk/fNPVhso7X36v63ZXQbOh8GH5IXlsQMMQFwLHMEQO/GNPriT+MUzCmWusHtv8HqxAoHYYDlD86IoBOgmx/h07JoJkws9wiS74PD8ZeCWrh1DbUFnak4BU5wwwZo6SEaQkbnnEMROHDXRSSAIgxVPEd4dI384cyYxP7VNAcfZElY8j84IHnw+8xfddlVB9KNWGAQSzbkWsd0D08+67n01dQ2WTMwvukP7r7aSvyY8n529f0ruM7vcPkjsdq/QM4CAxAGMMjm47cVEJ+ScAzgGAk3Avz66O2Por3uy5f/tS5f/xrzf29Wup/9NwXxK+qvPyCYY8K91bgXiEzYDBGghyUj2L3+VGJPr9l2+f3bPv8lm1/kP+A6wvy13T8g4hncH9BiFf8FR8fbQIbjNH7/EBIFp/n18/0+PRregDfff0MiJFf4x5W1/di8zYEVhyvAN44+FF8yrFmtbBM3tkWeuNr+h4Pz2wZmccbK2WZ/ZDF96oLvftw3ntRgI/SCq7tjD3bY1cTj+qX4OVLWsfxp5fUTMC/v5sZ+R8GLsRk3ArBJIKdUDU+glfvXdF48ccd3D29IC842Zcxyz4hYwf7CXlvRj8hb9uD+74rreH+6OexER6XhEPhj/ex79tDC7zAbVnV56P+jz3P2H89++I/KzEmF9TYBmNNz96zdVzxT0LgF88DxZ+F7O5fzPhJGZDaxwodVG+JXkI9HdjvfEKgB2ECwpyCVFnDCX9eBq5TAMj3kHNHc7/j992s7GHL73cYqsfG8beXN+p4+uDZJMLhMEc/l2MxxGC0wgXh9SOu4LP/6/bxKQeSHmxboCDcpEwX1lgGOCRF4ROHAeTEtlhywrk0PrUchiRp1+ZMmnBwwJAOQxDulORcG9A4TphQ3iNKv42VPxh1I03T5myWoJ0pazI2oHCLsgFBEg5LAXwypVyOAzSE6X1qBBnzafDDwBHN9052BOZp928vFkPDkQJdirPHZ4FNTyZGstbB36AXHO06jPbrySVTFLgtRItYV5zO9nhTEZZHmc51WqbE2NoT3flM53PSuZozFT+6ZTRtqZIto8Mx3uGl6uOLeWUJEumkBuqqqnKMV3p4YMxKSbLMty5lLBU44cXHXC1Oi7K4BLdJCaRyc60WE7Bht/mOWBXYlLtV9Hkbx9b1gq9uyUUWycqHwpzM2Z25moFzTIIs/QXDb86x3hfu+bS6AWOjJsKWiONrEt04q4ArnzO5Jy6yzyiaz2FN6GOuWvSYvKJdzOrp0rk267aIDkXW8mZ/c0CCN+dzPDWKpa1E8sFmctKli6vR6tMb41V8eFlwt/OZhFQtbVKz9GbZKimMSjbAJpiKm9ORILOgutx2vqGaQVDL4U0ReCLKDFcmfIWm8fx0qlWu1qOmtDKSvVi4UgWTODWUZgJO9Uleb9ZiLOe6KayjM7kP1aQ9cZJhyMa+kjpiutxzBrrBe99fJzLDnnbE0KQrZ25bekTN9Vm425mMt60Bb/TNWYxjQzOd7WpiyqB3lWNaXuRK7oAsVGa3Jg6H82Z9qIso4rsOHcRifeB4nDR9oiBYCY/z8BZFpDYR0CHbDzkwKFDMj7aPAmNLy6Uf3iRDkkOTCqa9srfWXHpWfc7mN8kcBv7VKdVCo8PTJu7aGiNu3ebqn9B5HKYM6Ft9QVLxSlTqfSnM8Gng1cUpsEJ3M/HgTjCPshy/HuhWQ0m/HFYJ4MPUj4fanmN0Haz3TYZ2/tXEkp2y71YykPWLvarikBEGdEpcB/vIFFHJ7oZYAmfhRnDnnDRaT6SOObuKlblmVLV6TDKTSawToewJiiC0SoXzhLMTXui5MpFCRmG5C8XtDCs95vJJ5QQ2DCy3UcPpcscJazLblCI6H44TNyhhaAjaMQeEuo+C4NRXcqEH9HW/NIDSB9TAm2Qn64eAOINF4VXzOAftigbRSe5IwavzwI+9i28m686sg666Gra8D3AxmNnmNlqcz6a0k+f1PD2IR9kq8rWL690qPg4b2agGz1eEFQbQaF6vK3TXXC59IuqzWhajzdGXF1FxmB91ad/FzMHp3byOuN3S5gbLrmwr37X41YG1uhJ2msuqLt0w86607Vgw0u6KZheiOnVGIdDEPKDxo3iorhFkJxjdq2ENlLmxt3h8wa2KbjNQy3BS93mOMbYpuM6en/muVMGmItKHNPaFareVZz1lFyczu5RTqYrO7WGVD9aEIzhUIw6nsHZh26n1MhOEOHY5VxsTs4Kjf4Ec0h0mM/GMmrMIXezli1fihXGYny7O1p/w3Pw42183gbeahiyThMvOOMqVdurNwxojRJXHrEMwoJNLJUdJrB9VvIlnhpwfs+K8cS2WajvXPsd+uen60Nr7dmEy1/XpxGHXq5avY/N40RcEwab7ms+JNF0lpwtMpE1v1vsubIKyifdxUwCV6c3qGAHUjVYTfHJAcZ0UfHeTa6Io6rvj0jhpmURd+QrT3bl6bZTkAGvmmpqpcppSlI/KTAsoBghSPuDc1eTtSMmYS3veqs0COLsgVv2jsdziRmYa+zDb4uX6rGSuvBjOaL7cbGJ21XEco86kePBvdkT7ExoFh2gAbeakm4Yj5trEyaxyxtHXeCbQ2uY0790Wxrmyn8XX0KTtzW6xj6VBJHP5UO2o1KIOOLUA+4UkG6eDNk/4YkboJCPNl2m6aO0rvhb9+FqWpwFWV2+aHg5LoTku6kw+GLY6K1c8Fc8AFVkLQEt0Y29WbFYsXFcNIxZycpCujwtjnhT8dY3GxJVX3JRf8+aQo+uZXfG+RkscttmuU4UiZ0W5WeftlHTlDStC4NHkwhQqC9FDc53Tm96/iYZ/aW7RRLrOT9xie1LMbiIJu2Kx3BD2LdUkz9UH1+oUw8maheCvYo9YcdjMUNcJPt3rhLgvWSYq9GsP2TIrU0/e5LS2XjYzCZ2ocqLcdhcTa/dLtBq0/Qyz2vQYU3FhiOK55ffs6ezKxlmY5jvWTNWdCEv9MZIKfsZ5htJLhFIfTSYsTiQxj1kJ7DjbKXfsNNuL5sbo8g11Bji1brogDYzBCK3wFCwFriJnVVqEfJxdSInTJ5TTO4WHLW9G0BvXizJbydHKguGxZOoJ6fAdm7EGq2t2pstab2KDgybXPddcJYMfdtQ68s2zxF0PNmwF0sVhUfDBIb62qHK09JXSasRanOIGqPLAOxB7TigO8cna57pULiK818/L835alv0yKvkiIYMLevFVc7K9Uediz2iOvji4VzNcuAHRLxI6S0XjtItMhlMnZ2Hf6jfHY3n0JlVbnlode4WXgLRalIwsCdiG04XbVAnjSjwJOrmdF9ckn803maX7jrxtHEtcciuDFrHtwJNr1bLMy0y56c2lSVEKSzb99HTUbuv0PGsmjXXRk5VPMsKV4PVlEVbXnkvLgZLFZp9MJb1yA17IqWM0WTMRc+vXEdeB3VXO0CicYe206POtzAzS3JSsLd/MZULZRMe9aSxyKbwNctx6e3nLR3O3CbXcQqOVv13dlux0i6E9C1uUXcjjjiBK+rTy1p4INFdaeoY+ITZWzJ92lRQF0+0W02KMIdsDn5p9vlb2Di+r00ZMI3KehBJLSMAS1viNazTLdC75tF3PlVRHT9N6cOQFPRz7+XpfJa5TXbceIV4lfWlep1TUV3g2EQ6tynt9uxTxXgj0Js1RFzf3eOxf6Au9qLc7SSs0sXLkOYxMeaWQ+QlP10Tuz2mnPy+jOo8tWOFAX1/km2s0cEPQlRT0nCcIooVf7LJYHg0h8jzGDjNtz6tnNeHXxx7IkuhwVn7bro0+mIfXOMhX9XU92yXAdIl5o+dyVdX+yksmML7Uta030WbSeWep2zU5rK7LpQlwPGBFT9J2uCvN/IOLyvRxi3cLW06kerIT2PKE5Wc2i6RydyBoVrL0tT3RW4HcFgq5IwxaC0/Msl4NRRmvqXxAE77sSediBOuTo59MVmJOdmgD/UhOk1uK9ox126M4e6WWc7S00e0tWJ7bXYWtyk5W432R7MRFjYsJXVZxyhWKbIalkzGspsUnV1w5rJTSxaqp1clpZ6G5l3oX57KaxG1yjVW5vcZ7YsZLSZiwVzIDjLwsc16bY9Z5IS7tatIq1ELQ6DNwnMOkO5fYJDr0ttcNxWSBHxk2TusqUgBfFKkoT8GJvSVZtHRuoTWX8GWjzJzIw9mjXc2uxKbsJcdR+yE8qMpC0/U46qXdFq26vm9r7jAtjjvpSJSaV01jOd7yJPSPtTLK3jVZ9oB7uq0G67T3NS7bJtJJFYCGnuOVpw1NOFhkrRXrXQIdfIwh0axqxxD5Y8abMbcxw/ZcLbaavYN7azJt+S2X+QVjC9km8tSymaIZvd5hW1Y7+7m3p8RSKhIHdGC7vig1saBQTOfxAVK0J6m7Vla35S7OFphrD0pwY/G1QpZoXG75JMxPbc6LM7wm0TAKuNy+BfJs5dnbedvOL4tAtmeTpDgEDbnXZN6VOiu7nXJHrQlYEVe7m33JZsJVzU9uys5JTaDZvp/Jre53V7FTpxyzU/l1fF6QupWkAace+bBMKn7eLmw0k6wG7R0bZbNrRi3C6UoJAxvnziGbJcxQpevVaR6TTRKxV6X2DLWcbxJUX6Ww0z+z54XLNpfYjTjQ0OiBngrWrrEULeRUhbpU81x1CFphq2ZS0XLjxJjq9zlpVbawoIrG30WGDGkR3w12wF6q203QOnMZXvHzwZ0la2HiaPW+DhIP7buEE8ziGAn8enEQJomhaxM1UIcA6yEq+HFm65PwpB2tZauiuMo56nkusn4xS8OYUrLDVDuRKqmoOKAa3rsS9RILrxfOid3d5QxS7zoorEz2tM/TnivYNluDSW8NjhHiANwwjGR6jF5g8unKXIgGFh6sud5I3HW22HyzlFcFyVStWJiX/ZLZwk7qEHN6tEKTYCKtEjvbXjD6aIgZzhcqIU880p/REjmRNGG1RBd9spWtbu90nQY3Wz5tTGJQ5+ehOcyWTl7fbH4qeLTNRpvTeRspM8pKuIlGhbxISVsVbjTWMe/iyqZJ+ATjsxmJqdZ2XkUujfKQD8JS9DpXYDbdzokrilxi0mVDDr1y6k403Hxtpxng2MFot/wxRM9DtvElllst8K1TUMKObALcmlqoGoa+sIlqBgvRmXFbSBjcRlfOcsBTQ23qa9Kag3ObT7p1I86nnXExuioXgMU2p4V92ddLIrwUgm3I7ITiWVeUKjEq2i3rMOuSWkvo5rT1N8E8cANR4YU0ZteuejxPbGy5nEXrOXm4piyjdHBrLzPTizYMG48yPFXdyeKEkwehnVtgo1HZuls1rD4IaWDZrjHn6OXyXBrq0a3pkz5F5WTioBiKacGO2mP6vDNN+TzF1NoiRVlc9kkrqV56nFbXRdDa5CCCvG0satHneNWvKs6Vm6za6Vbg0jMqoijVCKZ4se106oYZA3ksO+nQKBO1T62QDEl5vTiJBUGCq4ZN+COaMkx4MTCblVtrSkcb0WYPhL6cuXg/czh7abT4ElXZlVHMW94gCAGz4J7HLMOTT9ntMsxKvs/ISWn5Li7VsRMNzcXZOAwkg4jfFc5VW9mNk0tT1Yo9ba/O5gcHV22XEdWGLTVxJhcCyoMwYJRz7wodMyfXZQ3bGWxvBLKrWZltTWbKscZqcdG67pm12Oq6NmpmwG7OzmG4DTWz9546HQbMPC37XmVE0cbaHWT0imoId6ksMrLtdjB0B7WO67IQUoOkO3YaT7E2EF2midQrWBDTBFfFObjttrOL4ckuf6sZMAgoRZPzM3tU+OPUtQ8nVCIVN1jiqrZfzvLjhXAxGIrN1RTtI2W7XQ8RHZQChXkMzRdu4eScL5JGXi5itYS8D3zhgM08ZX3wQo8iuKMBusGMzHRvtbvJUiXJC0vi1HXbhj2le5vZ6tA4Gg0aXQaDz6nruXMmVCABtOXaebmdOW21W1flyqayPuvTxhzMQ7Ln7R0T7AWBLKzW1AXFIk/VoeX6DreNLpqyPM3s0GUDd+eLy86gzHTuVlKmlHZyYqgAXVLqUA+UiKY1ynmSsKdm5carFjHso7srnmPEca6rhDYJYeGsGmMmqAxrzwdvRdNJ6qKevwo1y/bnuwFvjuoqaJk86LVuD7aN6fdTgqIU+9Df6oqqPLNu6Okam6kr0uk1Ud7PZi+fXsbD6ecR819+lzye9v0/O3R8nA++vXq6Hy8D0/lyX+vLX1ftl08vhR1AxR4HrWVce8/jyP92zPr5331xMUrpH69rxzdmXfV2Ql+Z3vgrSC9B6tRlVfTfyiyu7we+n16suhx/EaL89jzYfrkbmeTjKfmPRr2Mv5cwHkhncH6VfXv+Fsf99vgyCDjB26gKeM9j6E8vTg99F9jlN4qZfANFPpr9fCEyntqOb0Refv8/DZNYaOklAAA= -->
