---
name: "rar-cowork-cookbook-configure-define-product-categories"
description: "Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_product_categories", "rar_sha256": "d65c2e96d5d52b3ea795577fb6596a7d00da31b1d9594790640d84801f7fea79", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_product_categories`. The original RAPP
agent is preserved byte-for-byte in `configure_define_product_categories_agent.py` and in the RCI capsule.

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

Define product categories Configuration Bulk Setup — Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-product-categories
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 d65c2e96d5d52b3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_product_categories_agent.py` first:

```bash
python3 configure_define_product_categories_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_product_categories_agent.py   # or on stdin
python3 configure_define_product_categories_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product categories Configuration Bulk Setup — Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-product-categories
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_product_categories',
    "version": '2.0.1',
    "display_name": 'Define product categories Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-product-categories',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-product-categories',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f226c24cb3c350a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-categories'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-define-product-categories', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineProductCategories(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProductCategories'
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
    print(ConfigureDefineProductCategories().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOb2LLnV9HU+8Puh11iX3zjRgySAAkQiwQSUrvDzb6IfRGCnv7uc5BU5fbr229uT0zEyK4oAXlyz1/mOdRvL3bXRkX98uVl79v5TLDTNI78embn3mxZ9EV9Ab+KiwN+Zm6Rt3XsdG1RNy+fXjy/ceu4bOMiB8vZskxjv5nZM6dL77RBHHa1PT2euZGdh/6sLWaeH8S5PyvrwuvcdubarR8W9bQwqIsMiJ3Fedm1M+7m+uksiFP/06yP22h2tdPYe3CbdKuLNHVs9zJrurIs6vYVKOTf7KxM/ebly8+/fHqJwfeXL7+9uKndgFsvy6dG/uqugvbQYPmuAGCQAi0BZTkAl+TguvTroKgzcAuoPXtefWz8NPg0+8//vPR2HTY/ffmaz56fry/Tv12Xz9postZuWt8DNpa2E6dxO7zO2LS3h2ZW+21X55OzGuDRPHx9rPzOqShn/5yefXwIeQ399uPXlwKocHfB15efZkUN5NXd9P114lJ+/Ok1LXq//vjTdz5N5yQ+8DNgBrR+/fa8frIFhN9J4+Au9Z+A6yOyjv/15Q/GTZ+H3pOdYOXLa1LE+ccHYxDQq5/buet//Omv2LqR717SuGn/Lb4/PxhHvu0Bm56K//Tp7uRfZtDToHeefy22BGH9O5YA8jdxn2ZPR/0V77v//wvrFGRX8+7xf8nuXy2A/jn7+S9t++8WfJoFX19WfhpfQXY4qf9l9tu3vcYtf/7gfb/54ZffAev/I5t90dXuncO3zM7jwG/ab99+/tDcb3/45ecPXQlyzbezb12d/iue/8qvdzk/ePBJ9fHHtUC+mV/yos9n75k++60o/0f9++vsMNX/9/vNl9kf62X6QLPJiDehDxf8oWYaoOsf/PjTy+8AI3JgDUCB6TGo8v/4j9k2duuiKYJ2tncLgEMgwG2c+ZPyRhQ3M/B/qu3aB35tYuDYJx3I/ynCk8ZFMPv1f7p37PzsPrFz/oaH/rcHAn57IuC37wj46+vMAKzB9zDO7XS2YzXta26Hft5OYsvab/z6CgDFGVr/M4Ciz9MXgJezX/8N7t/ujF7L4dc7fsYPjNotNxM+NV3qv042HiM/f1rkAiz2b77bARlp4doPNG4+AdubIr0CfJv80VziNJ15cQ2ML+rhgc1d/mVi9uuvvzp2E33NH4CKzR79opkDgnd1Zp8/A8uCNA6j9mvuu1Ex+/Db7x9m/2v23626M59kaADcnxEBGop7VZmBCusyQAaCBcIL4OMekd9+f/oXsMlBgwPxi4Op70yLQYZefO/N2fs1+xklyJnjAycDB2dTgwEoPYvb19kmmL3rC4ROjyYcj4qmBc2t9HPPz90BcLWBOe+ezIt21oA0bILh06xr/LvUX53avquYgVK3219n26UGukaRTo2yfnYRsLjIY+D+91R43AdM6g/NbPHG4nWmTDk5K+3aLqPafsoI7EdcQLd4Ww6Y27Pc77/mU4v0J1fdC+ThHkAEPOM+Q/p5ijlo5hlAA695k32nsafeZtx7XP01b57Jb9dTKFzQDIDQsAMtG7SEfzxTqomKLvXu/gOaTpyeUfCeUbnn4OovR4TlD0PFYpoz9gBJytnXDoURfPb/ewaZtGcFYccJrMGtZpxi7E4Pr06j0+T9x7QFRoEZSK1HBX0fD97A5Q1jv+ZpDFKkHv7xoLzH4knzwC1Q8R7Aid2dP0gE4NWJ7z1PJ8Pqu1X21/wNzD8B39yRC5gAihok/eSQN4HT0zdNI1C50/X3xn6Pa+1NpoNcnJWdk4I8CXzfuzuhjeqp1p6hAEnrT3XXR7Eb/WDVDHAHuQH4z4ASMageAPh31ykFMBOU2T0K7+TxNC49YgW0BbOp/zo7gnKZUqYBNQpmnokGeOHDndUs84GPgYrvHm4iu3woM42zTwXtKRZFBmL/xwg8H35P8Lsuk/qAqw1iD3zZT5jr+bdHZN/1fMYKKJtNJXlf9GO4n7bO/th1/vE1v+v4DvOg0tOpYf/BOTNQYVlzT7kJqBoANpn/TCCQCffe/Ppor4/+/a7Llz/N8B//3ph/b5jmj5H7Movatmy+zOePJvfW414BTMxBjsSl33zvd58f1fb5WW2fv1fbD6wfnvoy+3vq/cDimddfZsgr/ApPj+TY9afEfX6AN5afF6fP+PT0a77zv4f5mQsTzqYDaLDvTeeNBHSesPbDifjRhJqpd/WgXd5RFwTia/6eCs9CeSAO6JhN8YcCvndfENhH3N6bA3iUt0C2N01soT/tZ9JJ/cZ/+ZJ3afrpJbcz/9/bx0w9AOQr8Me0AQKeBzNQOz0CV+/z0HTx4xbuXlUTPhZfpuL6NJtm10+z9zH00+xtY3DfbeUd2Bn9PI3Ak0hACn69077vDx3/BWzG2qGcdH/sdqbJ6zkR/1mJqaaAxq4/9fXivUgniX9iAr6EoV//mYl6/2KnT6RoWnvq0nH7Vt8N0NPrJlwH0QN1B0oJIGQHFvxZDJBT+1UH2qE3mfvdf9/NKh62/H53Q/vYMv728oYYzxg8x0NADkrzczM1xDnIVCAQXD9yCjz7vxkcnywAzIGpZdqskoSL+gzpER6BOphvUwxBUFTgkARD2pQHw56NIQ7iMQSDUwxM4rBH4zSMBFQwEQN+j+T8NjX+eFLLhwMfYxDU9TASJQicQSjUZjwbp2zbg2magqnAA53g+9ILwMinrQ/bJke+z7CTT54m//bikDigXOPNhn18lnPmYJMo5ewiB6pJ/3S25hsnNitjz5wkteUtNxAXWbLvt0RnOuFSHXZruNXNCDrqrrMXQoPgcmqhNS1NbKlhY5ajfKr5AldOwxlytt15fl2vuE3Y8knr7QnucijhpCrBOFy3hpQeUtvNrKE8YGYpochAH1HPOrXywTvykKpiGH0ozeMe3p+qE19K3tVNbSJuUinW9i0iBml2Ss5LArba/UFdQ0bF9Y1nnzL8crbsOW+fkxJBhL0ft+LluB8MG12DBFmk/IkQShgKrLKfaxaCzAEEXLEIoY/bwqrgw/YgldeFNNStjVdKJZX7lG+90zG9uQMSXZgeoQ9K6/O1WaQKqWxvpNm0+NzdZVKCnjbKSe67A+gRRgydrpsdJ561w2Ef+5eDnsbAhwKR16UjHxbrkqjNUqYEN+vccylJKpGkJ0drg33dpVdbjZEhO/oSL1Q3US9jA1vSY616S+m4r8wmoEwhOu+Uy6ItkHjkx0ORkzeEWCxj60hu2n6z7Gi1ySK69IVtbNXE2KE0qre8oerdYgT6H+JofmwiMc0Pza6iRxdekBsNPS9PlRqimGFKrd2dfQ7f+ibSDGdxjp5W9txHjLipF74V+X512kjEwmhk0831Ve2D6bzbNmgg54m+zRRkyWzprvMdlAMh3S4cy9kNWmbYxGZAR0YWt7eV0pY7fl9hfILW8JgjiN2M5pkI8HVqHOBsmRYGXm7mbTFuuV3RkOXlhoxriIN9a1lRNM97BbmhSyBc783G0wc01XRHCSBQNzF1PBysE3QcjvR2zeV9YzREvthg+4iSBnGbHBDXsKafFq9KDd2npZyQ287AeYpWRtrK8c16YFOfgYsmWs8NpsCzkaROc0OmOLxLl57rYIRyTBkJktqGy8qYrtUsRneWhAD3yQrnXTdRYx7r4pZaXCEIsqnirLY870wqPB5I16zjywr1uuMq01b+oeETSUIGzy4XTn/qF24LF3FZbJK9eNtkxFrkduFlPLgSEcuFuOO3xwN6Llk8kxPEEnDz0ASBqihbgWlhpohdbS9eEzIeb0xi0GJx2YZQNNCQQ5AZutvbmGlp64gMkrQUB/VqY3OZNrytenRhOSa3mtus0mA4WzxpNzfzslUiJhKQTEcwo/PjNe8eqcVVPl6g/siQUQE5RSVqtYUVKyha13Op2KZCKXWoT55v+5ArkJtAQVZy8egz147SxhAw7MYc/J1UXG99oqWIo6eNVebH6jyv94f0KiX7+HJYc8K8WnOQvbItstVPmpLKhE2IHbyrbiYXL3x9I8OaFgqYLIJ6b410cBdrqhYhMT2O4pJ21KuICBW3lw8jxZorvj+KTuLUlgllEXGrl/ygyZxiLwXY68oA1U3YKSOV2zuiYkZybmS2a6NjuhCrY1ekdi3JYkhwWxWKB3BXgG74vKoaxN457rxJcqPkKdM4+Wsm4IZwhY1Z3wz4iOaRZnVwYF91A7Vvvnpw/OzYa3k+x9odpI/h3Ie3TZqLAZWNogQr57LicmXB2GKUUpU+P2/MExGdVnLYKZmSSrWwWeeLXA7ChUEMXmxD88M65EKquElGo7pQcNWLszyaSAZdSUQ1zl5IBixZDO4aD7O1tNK1C7a8nFZsGW9rvrdDcXW5XFfGLeLbI3V1/I7S9+w2Z/nWNst9vlqL1qko2n5H5h4ECoSMTVdl6fGsK5IXOsejMHddBpJuy/JE2c5OFx0o6BGV6W7kMKrGqk+OxyDQjIYKMJ4wYn1R4ePhsrYo97AXd7EVZMqtYeLQpZcN2IA6zQqDbntBxDRX68owQfPOWgHUzlcUs8VjaC9TBLmR0QTilEWGrQmQGpKlb87LvLqY7Akz0F3G7w/S9TBW5ZbUcdWhjsbRqGRf6WErtGPCZ+U2Ph8U66zsN+qCoQxYX+76XYW2ZoYvL3ta1PcNd72mapbAZSIl1WXotj1UuwCx5mfeuV0PCa5S5zjTd5ktKV0RSo3leVcHtfmhN91MziJZY7u5KTiM7+iNmtk4mGd4ZxBqBQ5hwq8gjuU2R6nWLLVpN03b3ti4O4/nRI4X0Uo2OHlcWg5piztSsdrjakMTXRcxbGKVy2jJH9z6dE2huccotwUpdpdQhFfcboTWlNmvbOyiC7v93K7kQfUkE13Da7YqKo9fhhc2WZYaXsgSAtXximRIqF+WdKDmN7WDCIEXGP8IJp7haBwipr9g22aB8WcBibAK3oeSx14HSaQqeLvaxTfLvFwZG+C6tMyGhaKkJll33KqXG0I0hJqoCB+HfIFLoSyQkHXtmWa3XFwcfImwKS4oC0fbLZ1a41PKLyIzvIk2yQ4nyJEqE8W4esOnW0w4b9awwDFMBBUUfs7gobuIdpSTPpdtjfC68KJbXx+NNZQuj6RkiZY8KsiRzfGWUQTF1Luj1bCwX8knjxmNw1VpIlkP6K4+EeseVZBCYeWdemaQTDki3IhtRW0vbKUcTyPSg0t1p+esmVqxCm0LE+o2+aKywuty3Mkjl57xpOuBwKKPFM40bXtJgpwZpTRh9e02u9TGdY0dKHKHtEsUtIYQo1qZOvEkadSR6SbEOBz0QOIGp0H9lvVUwtyTIGGMG5jndlBez/sipJQwLvqlG3qkr8ybPklR/xqJNYxq7ZiQo3MQW0Z1hENzc5PhYNUeGFNv7LqnA/Z4pmEXphcLU2/YRRyi3Crpj41Z4AIKqxex4W6Ieut5HoW0FZRYGdzs+5UuVjBK90cBOu1k67yZ75BoKRBmtecHT4oSfzxtdTPBrrWl2C0mlduoaA5LMLCwLs0G1aLvlpA9T20WrvdG6WsmsmZrPCcj9tJhhxOuBue8vJDnfpnGJ34bCgB9t3lWQWeFDIkIbkwsWariudOVyzgc+YBRBdg6x7R5tiOwm1mMYlWlPlfuq1wSs+R2W0JDcXSJOqVNTWGFvNDn5dHJi94+LcC0uz5L57UqGKAckqrDc0JtE35FL2tsFW32XhNXTC5tepZLnUuKnlCpHpSDGm/i01je1me6ahkHC7UR2TfL9ggbmQ65qr+v6ZvTo2c9g+YBrMyFa13LZka4jKMg800rSZGkNSSaGDXS4oNCXwhfanNMMxx5OxdDeXC6ZsmHpEHvU2KzNVgrZG+wwKoysZKiqqCq4SKpztJCN0l6q3J2cDlu69Ewl+w3fdWcj+cuWzP7imkZ1mgtzaG8c7CQdGx7hLtUie1qc+FWZtXajEgn3v5kc6vDTb7hQs6pmMQvekYOdjzpseJtx9/o/ZAKNebSoXBNxlO/uqaNxFGjZgai4TelzR9ugq4RceGVauGTIrmTsr2BlA2+wYK1N0KghkrjElhL9OLmyVoF+9hNKlJw0buVFW0XunSQb7GUdOii3pimCjokvMMTwbvoO2ab9MIc3ugNQ0r40kOJDm2Xop5W0RqztlW7dN1LUsztsMacauUsxZ0+7KIUwUsoX4CRazXSQ2OLVWFLSX3aCEF2CdFduD3nErQj1nxZp5ZfLnVUYHfNahHWTc4KsUTjx3ELPK5ecHq8SPB1T118qxLWVbKwWbZd0BLDbFR7T7j9suJFPT81FI56p5S7MUfuXDSpdQnVfmgaV1lsbf9IRJfDmXeZDM8O7kVt04EkcudwYqqwrikiW1zWOrzm00DZHHvh5CIneL9IzJ5g86DXa6+iE8ZObhCPawnsXStGRVT+SGfRErsNPjWctomVw6JP7fEuij0syqtVSKEIbuRq0heRbbnC1ofJ9MDZ/qJA3WR1xnp+3KCbSsF9ktrJCLo6LijvcAFkicL1sDuXk6XJ+3OZUbCbthMFBrX6FTOe/BQinUpFVmzsRDKEXRuMbwQmTpH0KGhw4x3jcGthO0xvzvSyTMbSHk1aEZwrwWP5ZXVE1zd0rWJUFwhz63hi1utqPaeD9gqx68uQr/ZQMp/zK4iptPORoRIKCh3vAiG8Qq/PNqrTChetQw+S57EVCsaZcVX4GMCb/KKDPcmWZDb0xtkl7XDjlEbrZfE0ilduMazP23lMrpM8A4h7mW8ZbtA8JLM6YPUqGq+lXSGXZbElO2PMNf+EL29K4hTH01E/z/Uhg87WjVbMxIqpLtvAyXwdjlcL7D02LuXFY4NrEUSRo3Y5j8QVHvdg37YyOExAVGnHeDgv6+P5NG6CqsjgXCQlBHaojFyTHgKVc/tG57s4lIW6CXRjG+6COqSsYEEfFpiTM5px3lNehaA6n3ELJLLWYtbWDnrg563kBY3NYRFZEDjudH6nqeRxxBaKzhIQcaG0ELdwg+9bduA7sEV1YofImb1+LCjXDZgUTuJFf2LnBoz5Ubc8bAk/r2LTw4oN7o5YEg9ys9wg5EW5gtkNXWz6dn5UTZQ2ziNzW2fhaYmuUlwnNCkzcqhYr244tNpqemCzJCd0QndFu2zbrZYsrjf9oRe3K/vYb5u1tuwFuZBohtYqySZX08CH0Yd8eYIv0AJj+ZuMUpqXHuINkFarfsZnSnOWF2emRIe54FUrDTWXDFPzXIDLGX2EOpxAPUuiXJRyFwNpuifCX40OTg1Z7yU3HbReluqZZhH6Vn/IsSBca1vVbm9OSbDnUF40vtplNqF5qzrHvDOVGsYYiGjrRmW18gk838GtrxWUv1koKL0314tFjYw6D5HeTWPZuAl6ntTGgnA2dLAu1idhqMkyZ5bHbcTIXZRecRYZKAg9KWFHeyiGGCcPFCE2TzwfIogE5rYBqzHYOCfF1RjKhIhnkO5vlwhoaqDnqIXnYTqygebrXAL7+sAl1NHWgvBqDYUYzfdQxOS4LCPsJttvO0l12WzOmqhyUG7YWBNbl5FqJlHWS8UIfAldUfvrrTwtClZMsrLGuyCoS4tThEqxVE3vNRWGboJTIVYMHYSs8BeIyiEiN9ySXiEFpY5YQz+t9/pmiykrMPGuix16srsS5Bvp+G2nWXXdlWq+PiUmK7NoDA055vrFhrnKPW3yg2MiYAOOrQaWL8N9x0V924ZGSgumcGCgvaO7MDtGw2WvF9BBPjnpjrwwvGO6YMjzx5W6zRN3NHzqptCBH0uErJIprlBtFjLjpb9a9HEzH/dYhwwrg4JyyRlDW2wCWq2CBs6rpltZvAUXbJXPd/Foee7YBIR4g9SAPRVK48qrkglP2a68XDaidSaxPkc3MY+sL5ZvazdoUDiKGI31aaftKBPO5dpWd3N6gdJiiHF6xbLsP18+vUxn1c8T57/zdnk6APx/dg75ODJ8e/90P2z2be/LXdaXv6XVL59eajcGOj1OXJu0C5+Hk//lvPXzv/HiYmIwPF7bTi/Lbu3bCX1rh9MfH73Eudc1bT18a4q0ux/6fnoB09L0ZxDNt+fh9svdtKycTsrfZT5OzeMw/9YW32q/je+34nx6AeSDzXP7dhk+z6AB/QCiFLvNN4wkvvl1OZn6fBMCLERf4Vfk5ff/De+YR/fnJQAA -->
