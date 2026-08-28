---
name: "rar-cowork-cookbook-report-test-software-releases"
description: "Builds a structured summary report of test software releases activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_software_releases", "rar_sha256": "4d36f0465635e3d084653670a5da1717bf86752e61e86c43785311cc023311db", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_software_releases`. The original RAPP
agent is preserved byte-for-byte in `report_test_software_releases_agent.py` and in the RCI capsule.

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

Test software releases Summary Report — Builds a structured summary report of test software releases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-software-releases
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 4d36f0465635e3d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_software_releases_agent.py` first:

```bash
python3 report_test_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_software_releases_agent.py   # or on stdin
python3 report_test_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test software releases Summary Report — Builds a structured summary report of test software releases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_software_releases',
    "version": '2.0.0',
    "display_name": 'Test software releases Summary Report',
    "description": 'Builds a structured summary report of test software releases activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-test-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f20dd5b4d9c1733',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/test-software-releases'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-test-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportTestSoftwareReleases(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportTestSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOi2LbnV7HP+yOzHplHBgHJGxXRgIiKMspkZUUWM8g8iVhd37036jmZ9V7VffdGdDQ5MO295vVba2/8/cXpu7hsXr68aIFTzHgny5I4aGZO4c/YciibFJzK1AX/Zl5ZdE3i9l3ZtC+fXvyg9Zqk6pKyANOZPsn8dubM2q7pva5vAn/W9nnuNOOsCaqy6WZlOOuCtpu1ZdgNThOA51ngtAGY5XXJJenG2ZB08awrOydrP826Jih8cJ5kcZvASf1yKNpXwDq4OnmVBe3Ll19+/fSSgOuXL7+/eJnTgkcv6p3dEbDSnpzUJyMwNXOKCIypRqB2Ae6roAnLJgeP/CCcPe8+tkEWfpr953+mYHbU/vTlazF7Hl9fpj9qX8y6OACiOm0HNPWcynGTDKjwOqOzwRlboBwwQvG0SFJEr4+Z3ymV1ezn6d3HB5PXKOg+fn0pgQjOZNOvLz/Nygbwa/rp+nWiUn386TUrh6D5+NN3Om3vngOvm4gBqV+/Pe+fZMHA70OT8M71Z0D14T03+Pryg3LT8ZB70hPMfHk9l0nx8UG4aspLUDiFF3z86e/IenHgpVnSdv8S3V8ehOPA8YFOT8F/+nQ38q8z6KnQO82/Z1sBt/47moDhb+w+zZ6G+jvad/v/F9JZUoCwfbP4X5L7qwnQz7Nf/la3fzbh0yz8+rIKsuQCosPNgi+z379pMsf+8sH//vDDr38A0v8jGa3sG+9O4VvuFEkI8uTbt18+tPfHH3795UNfgVgLnPxb32R/RfOv7Hrn8ycLPkd9/PNcwF8v0gIk8uw90me/l9X/av54nRlOlvjfn7dfZj/my3RAs0mJN6YPE/yQMy2Q9Qc7/vTyB0CH4oFI02uQ5f/xH7ND4jXlBEIzzSv7bgYc3CV5MAl/jJN2Bv5Oud0EwK5tAgz7HAfif/LwJDGAst/+t3fHx8/eEx/nD5j7NmHctzeM+/aGcb+9zo6AaNkkUVI42UylZflr4URB0U0MqyZog+YCoMQdu+AzAKHP08UsKWa//VO63+4kXqvxtztOJg9cUtnthEltnwWvk15mHBRPLTwA88E18HpAPSs9IEqYACj9BPRty+wCMG2yQZsmWTbzkwYoXAIIn2gDO32ZiP3222+u08ZfiweIYrNHHWjnYMC7OLPPn4FOYZZEcfe1CLy4nH34/Y8Ps/8z+2ez7sQnHjKA8qcXgIQ7TRJnIKv6HAwDDgIuBZBx98LvfzwtC8gUoHABnyVhEjwmg6hMA//NzNqG/ozixMwNgHmBafPJrACZZ0n3OtuGs3d5nwVrwu64BAXLDypQiYLCGwFVB6jzbsmiBOUMhF4bjp9mfRvcuf7mNs5dxBykt9P9NjuwMqgUZQb+m8S8DwKTyyIB5n8PgsdzQKT50M6YNxKvM3GKw1nlNE4VN86TR+g8/AIqxNt0QNyZFcHwtZgKYjCZ6p4UD/OAQcAy3tOlnyefg4IO6jMosW+872OcqZ4d73Wt+Vq0z4B/lGsPFADANOoTfyoD/3iGVBuXfebf7QcknSg9veA/vXKPweNf137t2SQ8qvbsa4/CyGL2/6+dmESjeV7lePrIrWaceFTth8mmfmcy7aNFmuiBuHmkx/d6/4YWb6D5tcgS4P9m/Mdj5N3QzzE/6KLS6p0+8DIw2UT3HoRTUDXNFL7O1+INnYHIszsUAT+AjAURPQXSG8Pp7ZukMUjL6f57pb47rfEnpUGgzarezUAQhEHgu46XAqmaKZGeRgcRGUxmHeLEi/+k1QxQB5YH9GdAiASkBrDd3XRiCdQEORQ2Zf59eDL1P0AKv/eAtKChDF5nJsiFKR5akICgiZnGACt8uJOa5QGwMRDx3cJt7FQPYaYe9Cmg8/TFj/Z/vvoeu3dJJuEBTcd3OmDJYQJSP7g+/Pou5dNTQNR8yrb7pD87+6np7Mci8o+vxV3Cd+wGSZxN9fcH04DIbPL2HmoTBrUAR/LgGT4gDu6l9vVRLR/l+F2WL/+t7f7473Xm9/qn/9lvX2Zx11Xtl/n8UbPeStYrQABQtrykCtpn+fo85dTnt5z6/JZTfyL6sNGX2b8n2J9IPOP5ywx5hV/h6dU+8YIpYJ8HsAP7mbE/L6a3Xws1+O5gwL7MAbRNdh9BvXyvJG9DQDmJmiCaBj8qSzsVpAHUwDuUAhd8Ld6D4JkgAKmLaCqDbflD4t5LKnDpw2PviA9eFR3g7U+tVxRMS5JsEr8NXr4UfZZ9eimcPPifliITpIMYBZaYVi8gW0Ab0yXB/c7p/WQyx3T954WWdL9wsimhyqk8Tvj9jpt30f0GyDVlYJRMKP5pBsSNABJO2gxTFk49gAu0awGkBv4kfjdWk7yPpcrUNr33VP9dgnsiAwTyyy9TPn+aTf3vp9l7K/tp9ra4uK/Vih6srn6Z2uhJZzAUnN7Hvq8j3eDl178Q49lV/70QT5B5wLrjTuVoUvEvdALUmqDuQf3zJ3m+K/idb/lg9sddzu6xLvz95Q1Hnl569oBgOEjYz+1UAecgigFDcP+IN/Du3+sOn5MB6IEGBcxe+BgRwgsCJzA8wHx4CS4xgoQd3HcQEiHdcEmQOBoQSLAkvAVGLnEMQTwPRjFw9l1A7xGy36Yan0wCoY7jLT0SWfgU6RBegMEu5gUIivgkFsA4hYXLZbAAtnmfmgLMfGr50Goy4Xujeo/Sh7K/v7jEAozcLNot/TjYOWU4BEq6auxCDRHYJ2u+dRO4zjDbMo7OXqqJ48pn8+iE+WVBr8mK9jRDPO5W4grtbIe5lErobaHRIoubTCda4WqWpTFMjmce6krFKrdI7FrULL1Ve0hvbKVbdyYicqWdaVmVqVZBWWV30x2vdrdDFp4RHJlzCVIVtWpo6KHRNUN3M6VpqmuKNUaydZrlMjeOhJZ5ruegTeYkgpa7qLZWeVxLodOJEFA2xnPVtXoF2ZSQaDVLXLKu6FyaI06xx3F/floJItFlXCJc1jt8Z6p+o1QrOHbWnG8IJr7Z6q1NlGi4qJf7tC+1QKvxTW4vRH9zy3cJDldVWV1syducoGsgZLeTkbRNur/25S6yb4pv7zWzN8jIXzOWxWZn/8TvGy7qW7es0R4pO3F92wWoME9w0XOMMdf8NBWUQVCRRSz5SCFl3H6nCjYwpZL4W00s7ODENYc+RLQkaJrwsNW27nprdDRtYPHiVm9Gf6FLawha092x2V92Epst7UUNH+tVocWpkfSU1cZCfqvRrWGcPPg6eOFyZK/rhun6vBSdqz/6u0qv4r2RIgQ097tjC1ls7RzX7ile63HB7qSqkY4lf3ZlHbPOczGucQRerX1vuGxkoStkCnJXjqR0fLek+GaXeWmJnSgkzW0yQdohZGFh6K6ImS/htjFaw4HMhMEWF2dHlygHCV6IwkZu58coogg91qxDuDgykC/gPdC2Y4dN2nrHZI3xV8wyzE27NY+QTXXHA8nXdbcH6Ctx6/EEWadIJ8YiUU6hcMxg9qjF5C7F0OOuaQmvg/Eq32HEybQWgoydssVmtRA26CblcbhMUmy+utmL3L0t7HCLM6lf1MUBgD9ptt0uJRfoVlxuc7UKjOJ4Om6bzOMbMx3VNXld2NmhINa2eRWqGEJAKu5S4ZpeMo2m1xd4WUmSguPwuRRWS3Kg65wuG5JB6mTds4rH03tGXa/ME69bSe9GPqxxbE4MinFYHxjOMXH7aOTBnhtOnHuDDMe2jsvMkoVK5gUKVrmijJwjrIm75QnqXC9mrZg18jGoqNrM/St3DjVZ6Xy0tbY8Ze/nIXZ2BYlJkrkLuf7GaIR5Cud75KomuJXKzUoZbcTSguWJs6+kvu7XpUvbCy0Ut7f5vuyFeSMGa2nb6jdL6jyTV68GSF99sy7hEsSEU1k11lH71abBCeVkIotcLC4knsDJyTvfMCcx7ct4O8QRaZqUVM9dwmT4nVqpergpcrwpDktHs23KJU21y7a44cOXomhaZo+qEhEp4uq2YHuhM9O20XGPjlSIAGsb12hXyoW7WCObGKyM1tgyJnYcV52Pitt0C+io4tc05zJ5xSIVsyb7wRJFMRMKxz4yq/moGZyGw3h+3Kw5dJ06Fy1hC9TxticmOHnoPro5+4N780EMqRRq59d5hTBZLWAW388lR2Zi7oYTp87LykUkKqgx11E2GE0XTX0FZD5FGBuKHEqSwRtoCOTVrR8UUR7B+rZxRSEiRRLIx1t9TMlprBrBWve6epEryNLgpa3MS745OGy/inBOoyBOTDj4FlV6SZguAs1ZvIBFwbTGuZSOe1lcbTj+xqbKUqDjU4ml0CqIKqLI9tzJ3F+yq0ZXqytvH8O93Q0mcvIrLbEVK9rUcEnXQcK0aT1GyHWN+teFQTN6NLJiurypKp2hjcx6kBTguK3obdgelIttFo2eV3gbWIpzgvVl5YrSBcso79Lk873KbBwAAy0y3+FGashCPm4vyLlUKE43N8XZvQ34so2kvsepuDMFegtZ+yu+5p0wXs+LgjjJMrmHCQ/S5TEpD8bJKrKjp0d0ZjIbLaPK5VVYNEPkUaYQp7dyVR8QND1qR2FzEgcOCAU6mmjLJKc1YuGithUlaCfgazSvHaRetQyRLra+itbcktlUSVRLhMPC/Iao2DJfOa4cYFLld8PcN2orc696D6XYRfMaHLp6Se2UUTi/Nmsqm/MsAgDo0qd7fVdwVX3VRdIIS5qgaSlMDqRgSYdzY5HHhKkWDZIf+g1/OIwHdY5R7EnNXZGzKWmPkuu0ai9oHHBnZOvpVydMhFR3ZGhk+1G+RnQsBg0my4l6XiXZeX097JDlZbuN1XokJdFaqyKxIdmCIeBqEOZW11E3vcwUP6SZ1ti7Jnth5E0+ygVpVqkYeYpagux1C148Ry13YL2o5ZuciK9QE6XLQ280O77Wq57dbDetmMX74bBPkoCFRzMId2PbrTrGK2XHkhR2L9e3xohPERrzdn2LRVrfrFJzxEI+Iy5JOaLpIVZdic48HS6OXY8kDa+tTzycS5HVU32Yn2qRkRtXMw8OB5ZDobTuSM/kCKMT9euapy+ni2/pNVdCOL9AeG7VnDtlTItsjvVbV3FGZ72HzurhCJ8ERbVMO7vAIZ6xEZaMw24I8vLAR4mJMzd1f0oQc6fVsR0l1xWypey1gSpbSUngudNsyHbX7edoLGgrmR4kUN9Jej0PfN+8RU4fsBUb0Yol4ki2FXn4VOhIbp70oyhtLg1ELsNLyM1lfiewW072itw1KQzenmskp+qz1Xq2u5exuk0jkKRtFdzWoxRnFxRHTaNmM9UeaYfEqrygmC09GFseNByWtHF3xnjoonCbwNqek30WDlXIvxw5tAqunUD3K7PE6Qg/afVNUgIlZCRN8zBRDkDduuraRVjBXK3DXDxi1mateae1L5ix4KWECh/Z1C5oxUEyp2/Gkq+4JQ6j1DldRwznwS0p654dOvy2muepKGibbifUkSuxOnNCmWTYbqsSPvAiSD8lFtfV5bBkqyUU6s1a4y198LlW6vXr0qA6g0r4yLOQ/X6L82PHy3ZHF7XgGhRhjdlwRbFVt9rapBoMmQDlQ16nEO+Req8cqNz18ptCx9jqOpBXi8wjZdXESK0R7BoBPfjG9fNDfXCzraBJjtWh7sGL+5VR7TarnWlK9NrC03TBUkbVJm3WO5KkLxdBt8Dn0YrZy8htN8Tl0g2J0YYYvltFham7p0igjiW6028xw1k80Vv6AWiEGzDet95GceqMJ6PKJa8Dmx0xylKLMa237sbQmetR47bIddUDW6E2nTmQtvD3eVP4ukB681NADM4G16QwFYtQjrqzhObseg7RZL04gxYil9egPVT4Tkn1FXXa41cK8YQVe9Cbq5+iec/qiE0jarbMNm2AMHXH5c5V5LQCDVc8drNiWLmUucG4nLNUzHNEbpX0cJWJszk6+8XGdcIlrCaHw8Xpb53snwdjRed6dboIVN0XzMhrnJu1pHEaJbwkDd5l3RujGTDCZ2UqzsPLzTITFhqFYwlHRwcrkHisorLeVFCXVjd3fzCZUSVbFe2jC6irh8w/ZFzpBzdobne6fc4Zd8AUdLwSwanaNu0S8SLXOC1tWJLzrN1kFAfZiTgES2PZLfqTWLgbYBllwDh+YxwYj7J4zCoUgMp4BSNFcdZ9f2ttDdyL2P0wJ6S1ao6+x9hq7ToeITB6jA23bm9q1NDpF7OXSUqtZTLp0g7psqbJjk6rB66ylPdlSFCIbaEL+bbw6i4nNszQkbbHwKtc2ZqoA0uXK1pIqWidaJMUV2enUPgNnSqNv+SvjB1gC4oEY7ylWFoKomf8wLg6BRWKzcfOTUp4aBGN9IW6lCG+FbmVvMgMAPOU6/jJWafDmCKq2544XlIrwa7DBaKTJtMI16Q5EaMQN/C1tWvPG8Z2E4MeF0S3lHFPUndkDc3n2yFsd067Y9xofrmu5rIyYufLWqf8fSXLGnUWQl7iMzRjVCk6L629QjtCvCcjnUXIzeCOq7N2ZKMe8cZ6SJHFXlntbjeOokF/IqgEF2mbbZjf5NXZM2vbcnujBUnOl6dj6hYKHOyj9Ulrec9a9g2WyZJ+yvR2FNOVsF8IFL41iZOdLQ6LTQch+Kqm+DnjidQaZq/JfjcPt94ORw0k3FpzxNtB2cFUFbMiziRYQoVuwNBj6d54f+VRPIwvqTVBiP5IbSDQZRok1Ib+4qpkxfEcDKu9whxPERGGjO2vULLA5eNB7fgr6doQYEYMzTG6mQhF7pcUdg6aXNTIYZk61IJMTijkX3ts5F1lKywZCQti93A1w8SOua1nt8f2JJfNCbZATffb+bWDsSsz7Bb4npuHcSCYiZBY9SJD6p2Q0QsBZ4+XofSY5dqn883Fk847eeBHpkjCXmqH3gvgxtkW8V48aPvggp/nwVlNRz/m91XICsj55o0LDDlr9pizsrdrWb1ewoecYlVb8neRrCwshBx9XQcy+wdLvgyJxKFNA1noSIAAvjSt4mG8G6za4qKqt8NCxi8MpAOU3W1Ac8CVR0vs5IEcmryHOAJt3B3pO4R3mjuctPUsGs4Dud63nsS0ti3NN2fQfiULliOIjjKWqyPTyL6DYGu659mBJFaN7af8pfYRsz+Kon9FUVc3+dIns9VSBisKJ+oWImA3MKXEHqxuftSoW3/dRvTYhkMF70FbgyoDGMtcdxmCaBfCQOmKyvoYuXA0LJABka8iaNmiGHmRzd6iDAiX90kfuF7HXDZxA6/RLFogKyhZM818u1j1CelA6+Xqkvl2Cp1ZUurXyIjAstyvCocqLoOM4eutehOgAe8XpAX7ipZE6+Ag2BEvC4bZuEi0zCgJZTqjX5xV+GxgCuKyFG4tBoqGOW4Q9GxpyXMErsA65axLaYtgKKZywYnyR5tETnOhG3vAnqyXqn7SSFlYbUoVDml5fhE43l77IZeDrgGt+KrqFii+F6pujoHGAQ3EK+I2NGiXzDUsQzZ0xDF6Ey1CMrYspFTk0b/IG5reWyy3tMxof5NJMRGqZSXiByc6waeaAsjPQm2H2r4ApQFS7LHmsBw2nDn4oZ+Zh81cRkhtu9rPOW5HVh3bjhzaW4p/w/zYvRADY2TQDTlBQ8spG1neFyKbnY34auLq/JAw+hzXTsfmUvhnly42C3zJjFF+vR0krAPNOZ+b1y3rX0ppFV7XMaXi601eLA3vuIqJRX9ODzly7UFG9m1fDRQD2Hh6eBojmqZ//vnl08u0S/zc6/3XPtNO22v/z3b5Hhtyb9967rusgeN/ufP68i/K8+unl8ZLgDSPPUzQlkTPTb//soP5+Z9+IJimjo9vntPHqGv3thPeOdH0O52XpPD7tmtGIEvW3zdQP724fTv9bqCdflrigfPLXZ28mraFH9zAhePnSXHfyP7Wld8e27bBy/Rhf/rIEvjJ99vouaP76cUfgVcSr/2GEfi3oKkmNZ/fHKa90Omjw8sf/xclrLgJ/iQAAA== -->
