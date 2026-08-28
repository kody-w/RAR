---
name: "rar-cowork-cookbook-demo-data-manage-customer-collections"
description: "Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_customer_collections", "rar_sha256": "ed267f9cfa6b5d9a0aadb2941467be23c4f0cf3d2578ddb0995e86190dde7cbf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_customer_collections`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_customer_collections_agent.py` and in the RCI capsule.

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

Manage customer collections Demo Data Generator — Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-customer-collections
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 ed267f9cfa6b5d9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_customer_collections_agent.py` first:

```bash
python3 demo_data_manage_customer_collections_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_customer_collections_agent.py   # or on stdin
python3 demo_data_manage_customer_collections_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer collections Demo Data Generator — Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-customer-collections
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_customer_collections',
    "version": '2.0.0',
    "display_name": 'Manage customer collections Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-customer-collections',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-customer-collections',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b121a4da052620ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-collections'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-customer-collections', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageCustomerCollections(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageCustomerCollections'
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
    print(DemoDataManageCustomerCollections().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjRpb2X9Hc+VD2qOoKxCaqwxGDEEILEhKITS5HmSXZN7GDX//3N5F0b5XH3T3tiYkYVdQVCZlnP+c5mei3F7Ou/Kx4+fwiAzOd8GYcBz4oJmbqTNiszYoIfmWRBf9P7CytisCqq6woXz6+OKC0iyCvgiyFy3mQgsKsQHlfahfgfg2/4qCsAnvigCSDQzsrnHLiZsUkMVPTAxO7LqssgRztLI6BPVIrJ0E6MSclJGRl3aQCqZlW9zVVYQZpkHp3HnkQZ9WktOHjIsjKVygS6Mwkj0H58vnnXz6+BPD65fNvL3ZslvDWywqKsDIr83DnzD4Zs9/4QgqxmXpwat5Dq6RwnIMCMk7gLQe4k+fohxLE7sfJf/xH1JqFV/74+Us6eX6+vIz/pDqdVD6YVJlZVgCaw8xNK4iDqn+dMHFr9qNlqrqAqkI9oVFT7/Wx8hulLJ/8ND774cHk1QPVD19esny0MhT2y8uPE2iRLy9FPV6/jlTyH358jbMWFD/8+I1OWVsh1G8kBqV+/focP8nCid+mBu6d60+Q6sO5Fvjy8p1y4+ch96gnXPnyGmZB+sODcF5kzegqG/zw4z8ia/vAjsaI+Jfo/vwg7APTgTo9Bf/x493Iv0ymT4Xeaf5jtjl061/RBE5/Y/dx8jTUP6J9t/9/IR0HKQz+N4v/XXJ/b8H0p8nP/1C3f7bg48T9AsM7DhoYHVYMPk9++yqfOPbnD863mx9++R2S/m/JyFld2HcKX2GKBi4oq69ff/5Q3m9/+OXnD3UOYw2Yyde6iP8ezb9n1zufP1jwOeuHP66F/JU0SrM2nbxH+uS3LP+34vfXiQprifPtfvl58n2+jJ/pZFTijenDBN/lTAll/c6OP778DotECrWpn/n/+eXf/31yCOwiKzO3msh2VlcT6OAqSMAo/MUPYHEq77ldAGjXMoCGfc6D8R8+Cskkcye//qd9L5+f7Gf5nI0V8KsD68/XR+n7+lb6vn5X+n59nVwg8awIvCA144nEnE5fxtmwAkLGeQFKUDSwpFh9BT7BYvRpvBgL5q//Ev2vd1Kvef/rvYYGjzolsduxRpV1DF5HPTUfpE+tbIgKoAN2DbnEmQ1FcgNYYT9C/cssbmCNG21SRkEcT5wAFniIDv2dNrTb55HYr7/+apml/yV9FFVs8oCNcgYnvIsz+fQJ6ubGgedXX1Jg+9nkw2+/f5j8v8k/W3UnPvI4wQr/9AqUcCeLxwnMsjqB00Y0gUXYdO5e+e33p4UhGQhYE+jDwA3AYzGM0gg4b+aWN8ynOUFOLADNDE2c5FlRjeATVK+TrTt5lxcyHR+NtdzPygpCXQ5SB6R2D6maUJ13S6YjYMFQLN3+46QuwZ3rr9aIalDEBKa7Wf06ObAniBxZDP+MYt4nwcVZGkDzvwfD4z4kUnwoJ8s3Eq+T4xiXk9wszNwvzCcP13z4BSLG23JI3JykoP2SjjgJRlPdk+RhHm+E8xG27y79NPocInQCI8sp33h7T8h3Jpc7zhVf0vKZAGYB7mAPReknXh04Iyz87RlSpZ/VsXO3H5R0pPT0gvP0yj0GD/+kPxiRfDJC+eTZdoxIWM8RFJ/83/cho/AMz0scz1y41YQ7XiTjYdSxgRqN/+i5YDfwIDYm0LcO4a2+vJXZL2kcwAgp+r89Zt5d8ZzzKF11AS0nMdKdPhQMKjHSvYfpGHZFMQa4+SV9q+cfoVb34gU9BXMaxvwYam8Mx6dvkvowccfxN2x/2m7UHIbiJK+tGFrVBcCxTDuCUhVjqj2dAWMWjGnX+oHt/0GrCaQOQwPSn0AhApg8sObfTXfMoJrQtG6RJd+mB6MPoRRObUNpYYcKXicazJYxYkqYorDtGedAK3y4k5okANoYivhu4dI384cwY1P7FNAcfZElMEa+98Dz4bf4vssyig+pmmOJ/ZK2Y9F1QPfw7LucT19BYZMxI++L/ujup66T74Hnb1/Su4zvdR4mejxi9nfGgfFXJI+oHutUCWtNAp4BBCPhDs+vD4R9QPi7LJ//1Mn/8Nea/TtmKn/03OeJX1V5+Xk2e+DcG8y9wioxgzES5KC8Q96n0V6fHln26S3LPn2XZX8g/rDV58lfE/APJJ6R/XmCviKvyPhICGByQoM8P9Ae7Kel8Qkfn35JJfDN0c9oGAtt3EOMfUedtykQerwCeOPkBwqVI3i1EC/vZRe64kv6HgzPVIFVPfVGyCyz71L4Dr/QtQ/PvaMDfJRWkLcztm0eGHc18Sh+CV4+p3Ucf3xJzQT8i7uZEQVgyEKDjPsgmD6wE6oCcB+9d0Xj4I97uXtiwYrgZJ/H/Po4GTvYj5P3ZvTj5G17cN90pTXcH/08NsIjSzgVfr3Pfd8oWuAF7smqPh+Ff+x5xv7r2Rf/WYgxraDENhiRPXvP05Hjn4jAC88DxZ+JiPcLM34Wi7IyR5wOqrcUL6GcDux6Pk6g+2DqPfCghgv+zAbyKcCthoDojOp+s983tbKHLr/fzVA9No6/vbwVjacPnk0inA6z81M5QuIMhipkCMePoILP/mft45MIrHWwc4FUgDMnKZe2XZO0CIc2EdN0rDmNozhJWWCO2biL2C7mzAlq4TgWQtMEWJAojTgOoGzLhfQe8fl1BP9gFGxumvbCplDcoSmTtAGGWJgN0DnqUBhACBpzFwuAQxu9L41goXxq+9BuNOV7Jzta5an0by8WicOZG7zcMo8PO6NVk9IF6+hbdEG6TBnSUdXt1euxmSpHg3IkJE2IKBku4ZXSJXt1ruVoK5vb2GPDvYCCvXFCZLeMpj0xZZlcTnmTqofyKJ60g7e29WN/sheL9VrRJZJRINFbWxzXvKVcjodYUbbhUY6vGc1JzTpNV6v55SgFeWap1sl1mwidsQqCz3WxjAtjmPmqzKNRl+5MFa8OqBUncj+YmCDuhGWc8tlOpg38qriCPF9pCVHsFcIuasWOWd40htXRkUndQ8R0NqfEop+7idX3brmoNes2pUM6MY8b9bzjDKvrbp0q2JgYqLkwXHZgoZ41mulmvNLV+2Tu0fxV6YVLQgOyS6hA8c/+5bDf7C5rUUjXc0dH0w5hsnQrbORO7AlYQkgorcAZeB4je4tVKEStziYxF9d9Qrbzmz8Xu+wIbiShVydXNaG3K27AAcrnHeWD60E7iL4crIZ4fkYRL7vY4m2t5Nry1lvXIjExbCgPXu2QksUY6/zAN9Y5uTTqGd+0PVkctSTph51NezNrELJaMtHgGGMwkA3MZqibHCpxbXlT/lAEPMJZu/qklafb0Zzau9ttWpp5VxYzc8sWpHoDUmxMbYyNl1p0sIduHWb9vNRrK0jdY3SDUbrKL3Z7uoiC29S07HJmbdfsrdlsydLKPEKrKrxhc4otr+ia4we0y9R2a5fW4Jjbi7RoFkJ3I6OBMbOernzakoBVnqsk1AMfjabbmdPszMVuS7edIdPFQfbR0xa31INxvZopIiSnmUMfNacw+oxOF0hfD6uBnO4OlgZVWEe7kykiSb7P84B084B38wJdkGU1v+a3IUTFRlisN4trS4fLGbcaVn2onMXWD6ebedcdXIycTtOUX3ZOYJP0yWOiuY5tEB/tK8JUEevQ7gBfqDKqHVdJp1e7rlIOrdEFVuRVvHUO8fgQas263Z2MdQPyeN/1/EnM3CWiqTtly/tIsip0TrDZjDwwGzPcMRGRBJcyPM5FcslKQ2VsiyQUszzXUUe+HRbiLsMjS5jFvLG5LGL9JB434QYEZz/sL+IWSVv5KAz90RcWlhGdjdk2qdeEkKrqYo3IThNvJZ5aszxExoU+25DiygjwvWyCU7AQW6xh1a4uioPDLPtKo6R9HWxtneeGq8i3KIOG2dLndfxiz1pbPVyn1ZkMThSjAO6aEdvDjStPVy46bzfb3RyXZ+rAmmsCa/Dl/koCudExUgqEzBSojueB2ajCPDzMdK1aFjNss2Sbg7Q17Olxd8SR3ZXkWEvH6yuPItsow2hBWt+Q077ltsLqpHBYBlxFWYpKTcR5KkSlf5rBMDGjih82FELLl91OErjZNjyc95ainrGKTmrHmcVhMk+3fE+XDBpvCwEjVczNw+U8UXpp53gnSV9exWtVbLeBwwxaTRyFzWl3rXnlSMVxVjPHSu9mHOYEXIQRtZEeUsDPy7pZAH4RsfKqXUV9SUZCknqnojH0JSyddeJrlUhgHkAlVpqB6f7AzGDXdJI7Yn44yCIZecHREmWPt0O8v6yEROmwXs7gZQ8unH31jspSDQOh7yEicMt03ds2P53lhM/hNrIvXGkxFYiE9vs8ZjFLm7u3QjAGaY0Za2PPnhlNmU/Pwonm+7PPtdvC72qOWUWxH6i+UxmMRsJNGtIhIXs9s+heUaurYpj2SlIFJUw3e+3a4t52r/LcziG256DSNpUGNit7MWX257xQQISvWtUALW/ogCCd3FD3V+yizS/uSegJtynwKDKXmhzVtuO6m3y3PbT0NFcSRNwt+52wKhDh0J9cesuURQ2MmeN7wTZy3TDbQkgk2ukUnC5wn+IE5Pm0FvDc7AWlwLrI4iImn+82Mu9kC8JQtOXu2tdX6apAZxCZu9XSpYItly1ryWZJuF7Rhdfj1rTJaGVK/fa8WUeZqRpCG4vMYicxc5Gjzjoq7+c6knC3le+auaIeBMpowGafAR89JluwYSholm0tkPsLoIQO0dFbqUhRkjHTw1TPetgAiIV1IBDa9I/49mYdYRyaM4Vizuv+yPWJNZckRFzX3ZwC850hs2slgVadujuwa/Mo5E8X0in7arMvEUVyNyuV3YfcZWl7OjID5kyjO99Lj/G1rEBWb5ZS1VyP6tTkNryrLfGTmRyZ9cUitW0ViHvvmixpap/AbYefst2JV9Oukqg+wHYIu1X2F3mZotolOXPLSg2oMlPdwlQWuN7mZzKWYuFwzlfASxzO8YNFtELTpTbbWyIWbxVP3WdhKJj0MUKa9TXj5eEYFquDJ130fkVIDUupmVox6sZMuJWwSLRrvW90QzTam4ezSEWEmsmeRP10EdrcmxEkH3UrvNijBTGtGnmIgbzOb3FmLpsaq8NMDQzKDhUjZHeYVUnW7LRza+VsJEdCu63c2tzk2CUi1oy+lvlGWV3UNkB8ZaEqJ7YvKq7UuFTknDkLzqVfq0G/YzY5g3NTxNwZbcRlPcRjO5pStSuf8vKMMPPecn1ErGKfRguNzQhO2NxEhseWBIooYhIdU6VCFVXhKnGTZjU2tZsZ7zQHjdkcEapbormhzxt/ujLMOZc2Mo5i2iZXB/uGIXPsMG3WnRgrgC5BJXAHS+6C5e6SXx23Pyx24o1Z+h5KWU6pmizrrqbZKd6Xhz7eV3gsdFNHj5ehfTPQ6dJl1CULkDlhJsnVo3whZ7XSUKR1R6hMhNwIsmMjlaXJhBB4GC97r8lvOCoc45JN96e25Q87bHDo/YFNTNa0w7zctJxjR662XQtQx+UqTdZksSuM5UDASedQkImzKzPucp8uzhSxvwgWKHhZc/11zsxi4jIdlil/CWy1Qjur8rK5vl5uanlrGtfeB0yyHy4D33WWf9hweXCpL77C7oVT2dxOddgSG3WI4tKU4pXJTbu1ynEEH+Hbtp8xqQYQnk/R/DJN952MMzYlhtXlJlmo1le7HtV37NyWsDorUjBQDlSoiC7Z5uDTyIFcCj1tdegeI/zsStaEjNusjWJD6K0XGKlMMxY7LwLqKooxgvlS0Imz+IJYUmMZzZbFZgIzY+uVzt3WeGrE/K5tK3a9xZa23gY0Dv1faI0mc/FNRsljYF1tcVnjZ3IFBs+h16t50K0zzUwadEeJ5Fx123Ka5tTlClP9Rl5Z1rKSKt+z2rkyt0eqTVqxL5n5folUy05hqqhWeW3I5yoNb/XZ0AbClUpVkddEqmHm5PEY8oeOp07DIlie5Url2TBDLd4gCmGNydaeq2UnknMiHkwjD46h0aizll9wW2IDe508zqlhj/cL/hwNpILzZ1h+WIWN5YUSZFTt8bkRrqp5RUr4igfR2aEPIbJcnFcz3SciWwmd2qmKc6Dsrpk0Q6m2PehVRSGN6VuUGehuJg1qH7BDiYTNKexNppnZBbrNaqS9OOYlN41jtZvmos3BzjgYFBKot4JHOV4WtiKM1BWDHpebgGKsTF2bZMl25+Far1exXB3zFSUKR32Jns9HjwEe7YOFb29MBNNLweByXtytzY6l56uoW2iBngnIxd87bVvaprgkFU0rt8O+DGpQ7dSVgym1WNssMouEMAMOLagqukCy3tt7ceuk1FlFjur8nF/OsjfdG/zQVDipkWtiR+VuuDjb6GY7AyoZNxD28JpdFrkym/utjeknVKjFhoaNVUs4ZIwmS9+a9/gQ7KPzWrg113rr5O1+72DYHjSJudniDEyKwfcxTj9ZZ1c3HGVVobVEs6S8DdfDcX/dptKm6Gadxez6gala1FMuphW2p4Vysh3BWp4xZjPzLgW2znYrWUUrcbdCpHmzjgxYYqvQ0PFTTN9uReWuzhCsVAdFmWPuT22/aJbWTWhcFHZMKBE2lFVQM29JykXLFdVs1l1mp4s8TxvnMJ1agpulmFI12+KMtasekVkgpXgpLhN0cVXra79Sbdo/koHcmuVJwxre2/I1i3C9veia8yVYtTENk85UhmnBESJNWLtcLYkTxnSMAHJ5sEk+HOyWrFGcD7iZlSyIEIsFhrwYCcnF65h3kUPXFMoIzMx8W1PI8hS5+JSf9mRYHoKAnm5FT5vqmKuoMEoARR0QPylaZDgg2AGU1HBtD3s57PQuE/J87pRXc9OhZtiY+lU+TasZ0XW4T0iuK+4o5iDtOJo6yRS5kTJxALNrb7FFOm82F047nHfFnqivhTml4w5spFQfPK9eNOtNI/JUMktTW8hpP8E9dnbYV2lkC3BE6ZF5wMCOQ6MUySpe0LYDKGedSi4RHz949h52BR3oNW2n6fseAAzhyMMR7wP/4LK5BYOgMFqaXNqSQJVlfsVTbCOe4d6hVQveQgK0Xq9TFzufNmFLrjm7m+Ir1FgrWiFYFF5VQFtJnMaTTH7gdL1qvFJZbSRrpQgbku4ON7ih9nezzVCQpyHk8ZjiYNTRl7m7cY/rup0vMEsEQZpcI1OQLotsjtpw+9Wng78E02FgG2ptbLZWYR4XSYU1RZdiwTnzh0VqtK06k41phxj73mewxayUolLnDB07V3OAl501YBom+UytBS21l4qYLtfNmSD1qS4ej2iFFbgqnAeUuuHlZo01Sz2jAHs5MO1yDUk7DFa4sBEyOGVF8KdpdN2kMhtG9EZHPOVMHOnrAM4br6Z0E5curVcJlS4PId5aAq3O9MGJ05lvT2lysSvAytyuZu7CFuPzAvdBRof6bmbuzdmUEk5X3r8WOqwn1Fy3Qyq1ilJDB7pBYJC47i0LNouCXM+nnTn1jDXep30YMmvEYFM5a2q37GbpdJepSySQIritYlR36Sws+gZ8U2aN9V6eCilFksp6Ke0XmhWSoq7zYI3WU4TGy3lhyXR4O2tF651jbXParzaZhLjn7UlSjD2urJtgWCEiZfvKTQBLfXsl5wsazGu8pHkx55es1or+dL+ZAzHj6M0Kp/c3smKlqewQLcEsr6UPt7mZjLTdYIe3ZkvRlhldo2UallnEdItivuAjqdfomFLsk13SG96+nkBci6vGo1CaYuJWo5G81eekuaI2uxxUuH32h2BWVqaowyhS0pQZlqXV5qyKmQGvYbcmF2AgogJKbZtNXRPt6UBe7dXQ8mTv8EHZAYXnEpIN1l5Ozqh2TSPyOkoCHTbShsD1htOYERVGR6FSE7uuFWIzazcxRhCaJEcMw/z008vHl/Ho+XmA/NfeF4/Hef9rp4qPA8C3V0r3w2NgOp/vvD7/Rbl++fhS2AGU6nGGWsa19zxs/C8nqJ/+pbcRI4n+8TJ2fAfWVW/H7pXpjb8reglSBy4r+q9lFtf3g9yPL1Zdjj9wKL8+D6xf7uol+eP0+6kOvM4KB6pRZV9ts/Rfxh8fjC91gBOYFXgOveehMlzYQ0cFdvkVI4mvoMhHTZ/vNsZj2PHlxsvv/x/JHM5ZwSUAAA== -->
