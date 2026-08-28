---
name: "rar-cowork-cookbook-bulk-update-retire-knowledge-base-articles"
description: "Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_knowledge_base_articles", "rar_sha256": "9372c88b18d705f592bb5f71ad1acffce360903786eedc90d037c17d77e8b8f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retire_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retire_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Retire knowledge base articles Bulk Field Update — Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 9372c88b18d705f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_knowledge_base_articles_agent.py` first:

```bash
python3 bulk_update_retire_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retire_knowledge_base_articles_agent.py   # or on stdin
python3 bulk_update_retire_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire knowledge base articles Bulk Field Update — Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retire_knowledge_base_articles',
    "version": '2.0.0',
    "display_name": 'Retire knowledge base articles Bulk Field Update',
    "description": 'Applies a bulk field update across retire knowledge base articles records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-retire-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cc920a1430606841',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/retire-knowledge-base-articles'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-retire-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateRetireKnowledgeBaseArticles(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetireKnowledgeBaseArticles'
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
    print(BulkUpdateRetireKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bebSJLuv8Lc+cGu4dpiESDcp895oF0skkASoHIdmyXZN7FDvfrfXyLpXldNdfd0z8w5T/a1QWRGRH4R8UVkcn99MevKz4qXLy8qMFNkbcZx4IMCMVMHmWdtVkTwvyyy4A9iZ2lVBFZdZUX58vrigNIugrwKshRO5/I8DkCJmIhVxxHiBiB2kDp3zAogpl1kZYkUoAoKgERp1sbA8QBimSV8WFSBHYPxsZ0VTom4RZZA/UiQ5nWFxEFZvSJtUPmIU/SfijpF8gI0AWgRC7gZlGdnSRJUn6FFoDOTHIp6+fLzL68vAbx++fLrix2bJfzqhYd2ne8GKXdDhDc7eGgG97QCSonN1IPD8x4Ck8L7HBRQTwK/coCLPO8+liB2X5H/+I+oNQuv/OnL1xR5fr6+jH8UaGjlA6TKzLICDmKbuWkFcVD1nxEubs3+jkddpCNkJcQ19T4/Zv6QlOXIX8dnHx9KPnug+vj1JYMmmCPqX19+QrIC6oOgwOvPo5T840+f46wFxceffsgpaysEdjUKg1Z//va8f4qFA38MDdy71r9CqQ//WuDry+8WN34edo/rhDNfPodZkH58CM6LrAGpmdrg409/T6ztAzsavfpPyf35IdgHpgPX9DT8p9c7yL8g6HNB7zL/vtocuvVfWQkc/qbuFXkC9fdk3/H/T6LjIIUx/Yb43xT3tyagf0V+/rtr+0cTXhH368sCxEEDo8OKwRfk12/qYTn/+YPz48sPv/wGRf+XYtSsLuy7hG+JmQYuKKtv337+UN6//vDLzx/qHMYaMJNvdRH/LZl/C9e7nj8g+Bz18Y9zof5zOnJEirxHOvJrlv9b8dtn5GLGgfPj+/IL8vt8GT8oMi7iTekDgt/lTAlt/R2OP738Bokihaup7ftjmOX//u+IFIyMlbkVotoZJCHo4CpIwGj8yQ9KBP4dcxvyECjKAAL7HAfjf/TwaHHmIt//j31n0E/2k0EnIzV+e5Ditwcbfntnw28jG357Y8Pvn5ET1JAVgRekZowo3OHwNTU9kFajdkiBJSgayCtWX4FPkJE+jReQM5Hv/7ySb3d5n/P++53vgwdjKfPtyFZlHYPP44o1H6TP9dmQlkEH7BqqijMb2uUGUM4rRKLM4gay3YhOGQVxjDhQsQ1LRX+XDRH8Mgr7/v07NMH/mj7olUQeNaScwAHv5iCfPsEFunHg+dXXFNh+hnz49bcPyP9F/tGsu/BRxwHy/dM/0MKdupdhkfHqBA6DroPOhmRy98+vvz1hhmJSWPSgNwN3LGLjZBivEXDeMFc33CeCot9qDqwtGQQx9RBYeZCti7zbC5WOj0ZW97OyQhyQg9QBqd1DqSZczjuSaVYhJQzK0u1fkboEd63frcK8m5jAxDer74g0P8AaksXwn9HM+yA4OUsDCP97RDy+h0KKDyXCv4n4jMhjhCK5WZi5X5hPHa758AusHW/ToXATSUH7NR2rJhihuqfLAx44CCJjP136afT5vepCx5Zvuu9jzLHSne4Vr/ials9UMAtwL+7QlB7x6sAZC8RfniFV+lkNO4URP2jpKOnpBefplXsMKv+4dRhLO7K6txyPCo98rQkMnyL/37uS0XhuvVaWa+60XCBL+aQYD1DHbmoE/9GAwb4AgfMeCfSjV3hjmjfC/ZrGAYyQov/LY+TdFc8xDxKrC4icwil3+TAOIKij3HuYjmFXFHc8vqZvzP4KwbnTGPQUzGkY82OovSkcn75Z6sPEHe9/VPknOmOGw1BE8tqKYZi4ADiWaUfQqmJMtacvYMyCMe1aP7D9P6wKgdJhaED5CDQigMkD2f8OnZzBZcIsu6P/PjwY3QKtcGobWgvbVfAZ0WC2jBFTQgfABmgcA1H4cBeFJABiDE18R7j0zfxhzNjhPg00R19kyRgbv/PA8+GP+L7bMpoPpZowkiCW7ci8Dugenn238+kraGwyZuR90h/d/Vwr8vsS9Jev6d3Gd7KHiR6P1ft34CAwwZLyzqwjT5WQaxLwDCAYCfdC/flRax/F/N2WL39q6z/+a53/vXqe/+i5L4hfVXn5ZTJ5VLy3gvcZZsEExkiQg/Je/D49cu/TI+k+vSfdpzHpPr0l3R80PAD7gvxrVv5BxDO8vyD4Z+wzNj4SAxuM8fv8QFDmn3jj03R8OrLND28/Q2Jk27iH1fa99LwNgfXHK4A3Dn6UonKsYC0smnfuhf74mr5HxDNfILWn3lg3y+x3eXyvwdC/D/e9lwj4KK2gbmfs4jwwbnTi0fwSvHxJ6zh+fUnNBPwLG5yxHMDYhaCM2yOYR7A5qgJwv3tvlMabP+7w7hkGqcHJvoyJ9oqMTe0r8t6fviJvO4b7Xiyt4Zbp57E3HlXCofC/97Hv20cLvMCtWtXn4wIe26CxJXu2yn82YswvaLENxhKfvSfsqPFPQuCF54Hiz0L29wszfrJGWZljwQ6qt1wvoZ0ObH9eEehCmIMwrSBb1nDCn9VAPQW41RBuZ1zuD/x+LCt7rOW3OwzVYy/568sbezx98Owb4XCYpp/KsTZOYLhChfD+EVjw2f+go3xKgswH+xgoiiUZwp7NLHzmMBjlUixhWZTL4KaDm7br2oCkMRYjmRkN6dxmMQde2zjjMAyYWTMXh/IegfrtUeqgSMI07ZnN4FOHZUwaSsAs0gY4gTsMCTCKJd3ZDEwhUO9TI0ibzyU/ljji+d7cjtA8V/7ri0VP4cjNtNxyj898wl5MRhetztfZgXaNbTjLdqqS7YkkyUG1Xy0vxMHAnBDFsAhfTntuZ0R+zWvcUQzWBp6U8YLi0mG3IEmmFhbbOWnR+pGeqZ7iOwQLJg6abprai5bHcEXf1NwR9P0lSegYy8/HslCEvtioqqDWaCFKxewSFCKvu6sblHwIqxifrLTLKlrfZLVbqCh12JihXUeybAqzhKbycy4ll1snSvi6Xw1ZI3hFpMXWyVa0C1ErcVHlGgCBIGv4JS6VG63xjaSUcpEJCr0fdhgL9LClAEl2seVPJ00Rs/Rq2piW36x21E5TnOJM5DeK5IR4XVWKthPXaimRt3XT51LhVVZ8zmslT/Yqntab4rZTKSK/elmCL+NL3GcXccaCMg1yG9d6be/5aWwc9d21DOXVmkpvOc35qi40qpnvxWGu6NqKuDphaVquYqtMnTTTBj6vbCpL+zhbyZi/Bji5TpbM6ixkeGx7mrOdr+INekwus23Z6WYVTXQAjscoHmpVNOdc0fBFMpOjoSX3MY3ag9PskrznJ45Ee1equJj50RWBFhsLXLR7kKik3Lqbjbj0y9W6t8K4WBDFuUznZtKsxctOTl1r7pkAklJ01eYzl5s559sR97l0efL7aqtfZrjK2leqZN3D3rturUSmqauDspNMMRinXZVsvdmyV7koQ4E5YGU0LG0Cj5cXobC1xRZjy6ApVoEVumLHlahVR+25mFtLYcIYQrjVqal5AAkjXYxh0klR4Ss86gUYxki26uOH7dTU9sbVUtNITKpJjSZZhV8UGM95GTeLRUdj4hJtWyU7VvGVUooz5cTwB2CDyea5ArDeZFG/nGozcuWjqRGj/AJAh/gTdw66kNICIBwrfeJhm32Os+hhgknebH4aShudh8er27tBavG7m9EIQ57l0aWv1EILemXN9Jm1Wvhr2dA6wfUD3AaLYRunoivoJc8xt1wtHZ8dbg13bSgmyX3pctSTTXFZHux5NZW8TRAK60yVjWK5JZdDFklLOY7CNhOo+TK/rlaydp0aJ76TyLSs5bYOp3MU+CaQAidqIpLfUhWmVlq/61VWnV5BtwLGXq04J8LqK3VLCKW/kGfroPmEPAhnmzm62WSyxzMSFPFxtzujIh9Y7PVia2aPbjgpNbPTSiy2yQ1NjOk0MjrmvJJXpcXZrToRrikqerkQuibIUvQkeU1sbBZosMNOeeCdazzFnFnBC5l7St02XMK42aepO6XOmtHqerFcznCQkPJGAUlldjpa784r77JOV10PGHyRAJmXBVaXZJ71t5TjYG2kF/15yy8n0nJyO6StYp/ThTxVers22u2EVQ9ddsP8zA2VFeVl+DnQ6Miebi7xaRVoGNGzKFnYhz2oj0ecMfhCOF435aoEnboeKinHAoPibjCxaXsQQy2Yt561ggRg3LC+r/aqGjazsl0d84YAB5ouZC1ak4dhS2H0ESVjovFbfaSQiUdJhVRLVD7l2QWxGnQi0DqtIEIHpQ/N+bRpyIZcGC6TKSHe1s5ssaLo81LnrSs9W5cZKkVtKyeLMEiV02VdTxNnSluEwZuyZk4zb4+RnKHY5LRumg4YvLyf2Wq0WbqHtJjuk/MU311JcVKdIkKj93PulHPp1Vjuut5jTpTc5ru2Wxmh0NrSfn5cCfMtERildWlMghSbflks5JK/afF6qbVGFud+oNDDFpLRtNvOz8t6becM36tC6qb8pd4cXLveCsd9YpHaeWH2wcFkNsOhsaSpNFlLQ1gwaJ1SnSvrq/6oFlJlhNahdnP2HMWbndwbZNJKO2UmiIsQL6jMnoxyLBvt0OmCr6/ujLWXLHDR4YSyrFtPhobsCLIFgt6p2FpqCxI/2suSK4jdUl2z2SzO4wu/q+jaUXbpcVNDmUaCpeepannbxMNXM5a3Tuv+pla9GalmSGIRVwlKSOVJpXMzXukOc2PqTPkDodDnLlbwU6HOoxS/JkR0oBVtFuBXlRx2Db/kvMBynNP+HPLEqVTt2QbNjbmQVFlLluBon0BI+Jp9wIkO1gQqgk70s2nG9suWMyLNLxR9XzZZtXBDXpwOybDW1+F6XWpboi01S1nr+0NGXEViso7CCE+6vg5WvHj21VsQlCat0+SFmKbTCDIFVpbKopQZSmi9bd8F1HopEOVywFWccpJYX11lYTNZNkd5e+F0tLQ2G+K2EzwvmZvbLRVbprnLvAnenmawRvUKzXWce8Sc07zGHNgndAIuXSxZP+vLgbK43WqPJjfBNM/Zei7uLGl343xstegue6U/5Qc8noKsQj2VP9PcwLIXR8vlRNSiHXoFuzMXZcLOQvPZksmdZNoTkeRfrT0X2+45rasWz621unKk2Rwwq6G5pvnNXAcOjUlHYqeyJqqILmGkIn6S5XNJt0tGntzo+Bh1qcSsM8xzJAq2IzKGi+RGzU5gJZhlt3MxetuDkFfmNzpcSoNqJudtgVYepwcTYVlgO5UU9jRvSRoBF3zZLSNI/8Fte7ox23izVW8HIukmomqpEzZTI2847pkcR1ee1h6BA8jU3KvzfNhyOzGY0Xi7WZjRcDMx9tYbB9cFB1hEUTbju52Jw/ZotSESy9X77ZStikQ1Z0OYOgZaahdVd0+M0bPrReKoycTy2Os121zW4XZ+OQC0Xh9VXopVrlyuJgNFTC92sTM26BafK4YfZkZ42+liz+xv6szsu+25wNYQw0vKRoM0zDYJ72xV/Oafj7Z7uRliSCpn6XzL9Ebz9rRAcWJ8WTf6EJ8zvKAJqZ37njS1ag3v8ijUrDlthPmFV7cmtUUNYyXK3YUPm+R6u0iavTRlJVtFOVfq+XJ/Q68y7VEdVp8hfQnqYHvNNsUqwUWXUsvKu87EseE43TqYITPbYqqCs7TT9y3Ybwql9LzAiMWTq9oipxKKfdlfHaXEYMthJnYkJ/YNS08LYpszuyoBS+Pqelf8QIv8Sb6dJ3nvSYEE9kNASdbqQg1XodTrc293plJYjNlblHidivQx1OW5FR2IMG1jPS20fVHUMunL4U4rfGZ7TiibsXh8spMFIcxARhOnU+zYJ2NoTw11lveYxUSXmEpQjZOpWNFOsqJuiVwJ7PnixM75Ngpkicllgd+W8TpIhDpb69Wcug3eqVyaTTAraSZUzIbKNkmoUMqtn3UlelYiU3TR3alz2TMTVBGw10URb+dVo+K4EgXzw0Vp2iXNU5G3mbcKle8vnjiL0avX7PMdbGB34c0f5tsqvV3PM8pg9JqrcMESStXbd5cYXS5ulKlJG0ZdEgaT2zOD0IZ6zc2VWN9FCXs7HYKzOJASmcS8tEZPrE1cJlGvWLfSEsUzjzv8jtv6ihTzlNonx0QpZgubx2gG2mQe1NkZZUGKr3RPvh2Yfiug1nVHM416Pedrfg02bVX22bmYhPM8JjOaYmmvt4ztrdm2AeNjEyVTm9DqZn1JL/MDZhO3bVvYLSu41LZfK2KYZXBDkVuxCo6yyiw4u9ysvEIKF2sjwIymS1aqn/SSee0vQDultWHRwvo2SCY3Z7mWrmY1um20SSbuZMLnFnFQeJvrUK7FE3PcFsYgHJaSnVeFIZl7ozVhlxnoJo7vW2VjU9ScPk2q+KjwiukAYzeNYt3RsXxhCN4SmDeUVqtghjln2V0ssDzsd06ptBVZ4AsymJymjXW0Q5bSWmJCCGk3nGGlk+TI3VR9z2qzhTixN6vZ/gL3YDdvqrElWNJdRK8oUWHwflHtdxejTj2M2VOeHXqLMHLry36q0YKxmMFGpq5ulXDMDMNf+rdrfFKW6HZRHyaipRwU7lBuJO9WDJAIvMxUam7LTWXs0m33uJgMCt8J9K1Ye+bJ1TBtb20UppMsdBEwMWAsrY3klI0tuMVeXY1JsTMtT2fmDMFmB9zZn64ogU4m2daFLbok0ORk1k46DKsqhtQPvYkStNCV4kzb0fGUR1lulh4VVExvlrdGD7QhF53rneqsjdaHxdSk0gvPsS2RRadNItLzswqitF5MF8fI7Yw0JxuRlYUq5dHpWuKtmImszREDTLLRtDI6L1I9neUFGa+l2a7U7fk8GRYHep2lw4I8xD0n9yJBw43GYQYWB8fhSyxQms1KPApuzJLEyt2R4hod5O1VkGRnQ+/Ng+aw1XS92PJZQ2GrFmOcZYi5RYZtBKyZUQVrTfBwqNYCV9Psguav6lxgpM3Jmh5OGSDtyY6+zsWGaHRrqUlHiViZdmISTXO1dR+74rMu0wHkAzLd2MOBHOoVhrYng+fdgNIG7LCqtyfbgtVTDPnA8XesXJwCPJDIQpwpjnw5lnNlr3YHcmoFfhVcYrpM09rh9+EcJLa2W7R60mQcYVssaez6JUlllMoM1X7rcsBUPNGQ9G5Bz25Le4If3Pqge0f/tmGOm7OHRx2NdtgQt7ay4VfJfOAFTDTJXexNsfWyW/C61lDs8aSfrZm/nUyG7VRFA9SLJ7uaNEmKqcRS4UjYRA1YVHbyIBviIecJi9b3gOeuhtgSta1MUn03DXl4URK1E1syOj2tMMGO0IbnDyzg1vuUIyR544ZotzZbm09sh54wqE5B3G5ljdWQEFYecU51VbRFALvGprw5ppUzTYoVkjfgVnE2woAhuQJzDryYLI7cSkQja3k4BfVQdtts0UvusKMPfbTSd/Q+zTeZ35t0kLDsgZ8RNd56pM+ZG7ep9EXrETqjd71RzRpapIpal53ZBuOkaSmxB7yl8UXvyYML3Ws0zcScaLZMis5padX+OlpNNvWmbuC+sWZgx4DO0cm0W+4pHVtUk5WJhvQmWmz6MORWmDFPu1tRU2UHd8ZyduFhzEaNTsoXl3NYfeqxCwzjWuHss7o7TKfT/TzY0FV9XFJOE1NxQsZDehu0NZ2jpnAkim7tz6M9OM8Px6FEPc4Ms1bxr4W1TPTSJvJ1nldTghKFvJqQZQ4wILu4UXDmMtdW2AE9oieK5DYe7W58XcczhexPzX7DcaI+X850zROHw0YOhNssZynJ9K4YdfMlqZl3ZUUYrBBEFSNoGQEoD5VKj0bpejbbo4dSz7y53l0xlVyBCjbTpV1HtA4rG7nf1XNGnKU3cubvJH+/tzA6aHXLVoU1fpjdjqqP5q7kyBlbTSSeak6iB2yOBIqHOZGoZi2mG/axlA9kWHPN/nbaZzOPCS3Usd0dKg9malwPGqObB30rOGEzXXBM50WsnXMc99eX15fxzPp58vzfeOU8ngH+rx1FPk4N395K3Y+dgel8uev68t8x7pfXl8IOoGmPI9gyrr3nMeV/OoD99M+/1Rjl9I83u+MLta56O76vTG/8laWXIHXqsir6b2UW1/fD4FeIbDn+3kT57Xno/XJfaJJX92fvCxvP1seVVNm3+6v4t+lBOr4oAk7wGDPees/z6dcXp4fuC+zyG0lT30CRj6t+vioZD3PHdyUvv/0/6OLOzCImAAA= -->
