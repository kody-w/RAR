---
name: "rar-cowork-cookbook-bulk-update-identify-workplace-hazards"
description: "Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_identify_workplace_hazards", "rar_sha256": "e0ee9fe72edf26dc405fb0f9f15fe022d96c1277820bd99bb64758075e2100ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_identify_workplace_hazards_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-identify-workplace-hazards:856934f1c0b62a730bdd9d83059c094655391d311207b8d37d2e0aae43f00957", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_identify_workplace_hazards`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_identify_workplace_hazards_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Identify workplace hazards Bulk Field Update — Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 e0ee9fe72edf26dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_identify_workplace_hazards_agent.py` first:

```bash
python3 bulk_update_identify_workplace_hazards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_identify_workplace_hazards_agent.py   # or on stdin
python3 bulk_update_identify_workplace_hazards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify workplace hazards Bulk Field Update — Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_identify_workplace_hazards',
    "version": '2.0.0',
    "display_name": 'Identify workplace hazards Bulk Field Update',
    "description": 'Applies a bulk field update across identify workplace hazards records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-identify-workplace-hazards',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5c604dc98e59509e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/identify-workplace-hazards'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-identify-workplace-hazards', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateIdentifyWorkplaceHazards(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIdentifyWorkplaceHazards'
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
    print(BulkUpdateIdentifyWorkplaceHazards().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjRpP+K2zvh7GXnhYgIVC/4YjVAehAiBsJj6OHo7gvcQiQ1/99C0ndM17bu683NmI1Md0CqrIyn8x8MqvoX5+spg7y8un1SQFWhnBWkoQBKBErc5Fl3uZlDH/lsQ3/I06e1WVoN3VeVk/PTy6onDIs6jDP4PR5USQhqBALsZskRrwQJC7SFK5VA8RyyryqkNAFWR16PTKILRLLAUhgXa3SrZASOPnw2yvzFK6NhFnR1EgSVvUz0oZ1gLhl/7lsMqQowSUELWIDLy8BVClNw/oFagM6Ky0SUD29/vzL81MIvz+9/vrkJFYFbz0toE7aTZnNQwnjXYf1XQUoIrEyH44teohIBq8LUMJFUnjLBR7yuPqhAon3jPzbv8WtVfrVj69fMuTx+fI0/JOhlnUAkDq3qhq4iGMVlh0mYd2/IPOktfrB2ropswGrCgKa+S/3md8k5QXy0/Dsh/siLz6of/jylEMVrAHuL08/InkJ14OIwO8vg5Tihx9fkrwF5Q8/fpNTNXYEnHoQBrV+eXtcP8TCgd+Ght5t1Z+g1LtjbfDl6Tvjhs9d78FOOPPpJcrD7Ie74KLMLyCzMgf88ONfiXUC4MSDS/8puT/fBQfAcqFND8V/fL6B/AuCPgz6kPnXy0InZ3/HEjj8fbln5AHUX8m+4f9fRCdhBtPgHfE/FfdnE9CfkJ//0rb/bsIz4n15WoEkvMDosBPwivz6pojM8udP7rebn375DYr+H8UoeVM6NwlvqZWFHqjqt7efP1W3259++flTU8BYA1b61pTJn8n8M1xv6/wOwceoH34/F66vZXGWtxnyEenIr3nxL+VvL4huJaH77X71inyfL8MHRQYj3he9Q/BdzlRQ1+9w/PHpN8gSGbSmcW6PYZb/678i+3CgqtyrEcXJIQNBB9dhCgbl1SCsEPWR1F+V3YbnX1L3KwLvDukOKcJqkhrhSitMIE3lg8cHC3IP+frvzo1KPzsPKh0NHPl2Z8e3d1p8+6DFtwctfn1B1AAunpehH2ZWgshzUUQsH44flr0FSNWkny/DylCr8M488nIzsE7VJOAfyNd/bqm3m9SXoh8M+pJBD1nQbS5Sg7TIS6sMkx6xbuze1+AzJFvIKmWeJLblxMjwoyleBpSMAGQP7BzI46ADTgMrQJI7UH0vhAT9DN1f5ckFMuSAaBWHSYK4IawAsK70t8IDUX8dhH39+tW2quBLdqfkMXIvONUIDvhQGPn8GRYFLwn9oP6SASfIkU+//vYJ+Q/kv5t1Ez6sIcICcUMNhnWCbJWDgMAcbVI4DFYsGCCQgG4+/PW3uzsG7TJYIWFmhd5Q8erBRd8FxGDB3UfvDoI2DyqC8rHS73FD2gDigoQ1RAtme/X8JRtE5HBo2YYVeAfxPvkO/bvH7+sMPqkeGEI/3YroMPYWi4Mzh+L6gmw85AMpaC70az14NMirGoZvATIYHU4PZ1r1NxdmeY1UMIMqr39GmgqaOkj+akPRAzgppCmr/orslyKseHkCfwwA3ZaHs/MsHBz/CNn7bSik/ARjbPEu4gURAEQTKazSKoLSqsBtnGfdIwJWuvf5ULiFZLD8D/UdDD665fYt8jZ/3V0M1R9hbx3JvQlAvjQEhk+Q/9emZVB6znEyw81VZoUwgiqf7hE2NFqDwffeDHYOCJx3T5dv3cQ78bxT8pcsCaFXyv4f95HeLajuY+4015QwYuS5fJM/pHd5kwtVQTaDr8vyhsWX7J37nyEw0DHVQGMwg+OBD/KPBYen75oGME2H6299wAOdIRtgPCNFYyehg3gAuLfQr4NySKyHH2CcgCHJYCY4we+sQqB0GANQPgKVCGHAwvpwg06ACQJ7pzv6H8PDwS1QC7dxoLYwg8ALYgwBDf1QQQfAFmkYA1H4dBOFpABiDFX8QLgKrOKuzND8PhS0Bl/k6RAX33ng8RAG51Bk4HofmQelWjCKIJYtdAJMrO7u2Q89H76CyqZDFtwm/d7dD1uR74vUP4bsgzp+KwGwXx/q+3fgQMou0+rGQrDyxhXM7xQ8AghGwq2Uv9yr8b3cf+jy+oeO/4e/tym41Vft9557RYK6LqrX0eheA99L4AvMghGMkbAA1a0cfr7n3ef3hPv8kXCfHwn3O+l3sF6Rv6fh70Q8QvsVwV+wF2x4xIcOGGL38YGALD8vTp8nw9MvmQy+efoRDgO7Qca1+48i8z4EVhq/BP4w+F50qqFWtbA83rjuVjQ+ouGRK5BKM3+okFX+XQ4PNg2+vbvug5Pho2xge3fo8Xww7IGSQf0KPL1mTZI8P2VWCv7Zvc/AvTBoISLDtgkmEOyb6hDcrj56qOHi97u+W2pBTnDz1yHDYJ2D/e4z8tG6PiPvm4nbHi1r4G7q56FtHpaEQ+Gvj7EfW0obPMEtXN0Xg/b3HdLQrT266D8qMSQW1NgBQyXPPzJ1WPEPQuAX3wflH4Ucbl+s5EEXVW0N1REW5UeSV1BPF3ZUzwj0H0w+mE+QJhs44Y/LwHVKcG5gPXYHc7/h982s/G7LbzcY6vs289end9oYvt+bg3vswAl/s40bgH0vv2+DeGsQcmu2bjjfmtU3aGM4lNnvHvlDz/B2D8inV8g84PlpQLMMYQd+ve2vn+46QWO+tblQAuSQz9XQNoxgPkFJsJgXgyEx5L/vFhhuh+5t/PDl9U974/+ZDF5pcjobTzzcwewpYVFjzHbdmUuPMXLmYLPJlCTHM9wd4ziBUTbtjimXAJhlgcnYw7AZSUFVBp+m1kOVET54AxrxAfn/smt/ukuBdYQgp1AMwACYeYAigOsRU9eZYKRnY97Mw0kPYAThzqYOTlAUTUATZjPbnk4oksYoEhA4hlnuIO/RMd5Ve3vvzt/9c2eGt3tfAVckLMuhHQqfuDPKmjoAYjN2AE7gLjUGEJ+xR9NgAgbJj6kPHw0uvFs/xDBsW2CrdhnW+fXh8yEupxM4cj2pNvP7Zzma6daUoGw5sNFyCk7mcbaxQ+1MqTarJ/FlWhYH7rzYznvPzbM568bhodjFxaqqYLcXcr5KMhm1EKsaNZfETMl2Ct9Zu4VBN06qCtm10ahxF5+XG17GcDVO9GtNaFMdx44cQzPEiIXda1HMDMM7UjyjGc4Z3eFbsPTstU2h12rKbwphua/IiNMJi66bPb0zj4bKk6YZxopsz46Fm/dZdDDZ8ZHdn9Ny5162ViUqTkSXU7LVCzuUT5UbVvouOW0yy041PYrNTCVJ5xi1JBgfO9auJ6Om7ANyOSPqRXtMWbFr6nOOFSYlJ0Zl5JGg1ZPWOJiYKtK6wfZHEJ7ZdUv1qezQGT/qGdLptetkZwbSFtfdsJDdLMEsWr+meSSHueRSRsy2hlysIv5EJ329kNFVJReydS66ZFdm3DTOcWLG5fhYXM1ONsrHBb4Z70CL8ca+XGwPFX89VGTcJuayWLFieWbU7U7lRmW2W+j7sq4vG1PYU6uJGDsx2nOyIrFHqnaKqGocnqRLAweqYMbRofXwPMPW+0gJuJ66AvpULtGgjq+1tScPInVaclt77jZpTlstqPb8uU1pm1Ujc43ihRblxhbncJ/n2pGo7WLWkrpujYkreZXYojZaW6Dk5es1XispGYCmMS7ZxV3aa6vx6xSfzDg5Aug2rGyKcMwIXZ/wcFcxjW7EU66Tx1MYJ2YdnKojYCndVLa+4JggzVFh49dEWXXylTSm0YXxUqrVlgcmIxh+6cV26Mxz8rKVuivLnxkaBkGDlgu31nSLOdLjJGRDszmegknW70NzucYycVuZkVCRiVDiZ9W47nRDp0Icm+xm2Zh0l8p0z6LXiGbWk/lS9HpGllK+GO33NkntK88sZqGzlgrjgk6X20WMrgh+hrVZobRn0XPVTUmChNgKcS9G2wAzpE0uBCVToMZK6zYrPjTUFU0dJe0Ke75pga3Xu2Im+3QGwPkUFCtwMmqtTTpr7Pfz/VnIKz+zZKXTxicqj/fMoY79Jt+wS6wA7OoQXYM2W51NQjy4tu+uO3Z2ovYoZA2S3zSh2vN5bCWYetga+6wLUnW7xpfkRRW1adx53Yi03ck67CqzDcpT76GjvBSP/enknT0BnYPoqI/7uvKK84rtc0YqKWXXVEV4OBRE6+BdIZVrDaZ22aYkFUwoK6e4KOK84rrBKllX8rN80sUZo6aJSIeJMeFGNs6dVmUxlSkQb9LD6EKZLRZq3TEqEiZvvel4J8rQ5VNTRgtgMbOOTWQ1nXKKeqgcVZwy2mWmSpLmhJfpWuXlSmR9fpL0XstdMfFyXvjZ3nV6Wk6VwzL1qgUQRC00Vyh5CnYJUyXySJKzDXbZ5blMjDQ+G4nlxlwkfednthRYyjnx6D6y9MoRqsCXt2XIWT193UVcsw3nO6s4606urGxxtSmWB70+Qp9Ywsa54qhemyFxGp/QfeXAPHftCS2QYkRz1VGIzQRPBZEB2gFr6Iu1dVnrYrkEtQG4zBgjD/XG/ujgp2tlRTbzPRy/5eY7os7UFlt3ccbJu9bZS+VOyfsx0zVr8WL6rNQFVcDn4+vq2M0LEvWqvqNPQsQWmRVp3R69FtPZUiITmlCtxLPs3uZnc3LDnuYKjSlMT8p2SYc5H4DTXG77il9EfrxQrBA/gciuirE229Qbj9vPqz5hNP1UnBZOqJREt+6hmxJ2qfkF45hk6seuVpVURe/YyWTC491C6WgT56Il4YY+IaIo6QZktiso1QCeJ66IERCp3o+VpaHEtePas4wUdvuwRI1GP4N+FShcJOfARb1LeF0UquvKV3vRnnfxxtuaLY2qpihCMgbehWpbANC0DFjpdKBg1pd9LjHOvCCKjcIJ+Yws/OOi0PvaZLeZz2fsxjbTtXg0FnjLlLJdHYBfyqWJy9pUUMRDF2Lq/CBuJezcckEK5hM5W1RznWwvTa7vSuU0zcXgML0qFeY0IU3F05Bbb+OVih7nODNF2+MkTyWloMdN7xipo0D0UG3TUr4IIwmXKalRBQ7XrWg3mQhH7sAfLrhdh/NQLgwG9/q+jyYz4sBcg53tgDQr5x2/ONgajtJqLKcrsIWbeo0i81PMjS5LKmB2clDKZqIQysGjjsf52JSccD13eilZjsahGSzlJOK65XZnorIcXDWiahsUbiodr1lYktmifs6cpo04U2N9QWEr0Er1LtNwpVtUSX0caXndq63fLRxqcgq8oyWYc26TUrslZtTNNTAxbxNLyXGfcP0Wmrs4xO6Oqf2gYmpCPxi0WohCPAFSQgRMoPVzNKEN1yh07toQDuFc4C2RXmuukTbnWVfrjGk7SykXsqWibuJsVXdEaq/9BLDt+qDuDkLjpnauteg2HUdSzNfp5FBfTz21zExyl56TI3sSZ5w+rULMPFOY4TO51FzxZIP2Q++1Ebe2td6FGb6NaCrvNd+vN+edqIlZOs+wJKd12F6EvMC2HJMZDCCWsiQwZz3sdtuNL+sMhilbu9WYnHL3XMOMrMZTxCKXsPmkd70AOwh5MCIulpqTjJDF+cIDq74ONNfdRkbBF0SyjemZOD6a05HjnuaLuJSahSO505PgtpPIn4rHBYZNSw5FO5iKZaLsdJK2+Bji5vKn2XSjwWK5Zpa76EiPbOAvmKXUahvuqlZFeTSkxDe7gK50KTVyELI5GiXhpL5amc1d5opIT6MYjNWdrokXniHBZokHkZZrLtvPmUV3oXBF0ooxVLzJyAK9yIwtAENXr7KqdNO5uF9ES5cWLtuFb15Pqsq4+2LXrY6w1pwXO6rS5xJJpuCs5sR8T9iSsZj32uocY1mrlCSnCiVsCxXgBjo+HyWdjEZCya0Ori50HUETc93wtMSabiNWNbRVu9YN0Ggbiduu2E62Qzve6HPYn/bhqZ0qq9wxALHvDhbnjnyDxRuzyP2xOVEDfLrytWtZXbeRkpl7fRl2kUq42Q526ZcVp9TsNRP5vTE5EShWnVGVAEs05ierXHUW8A4q7mhHaXH7bGV7FQ+peR7zo8zAfdLtrihf7PiIsxUca7JDX4EN4aRueDZnVlcIWZmWm3wxNmTmWpHcRlVirmh7V5xv1kuDx1fnBMtXvrXBjO5stsm2KPoTlLyacOHFCGsLyyQQrXPs4MuwBz5r1/q6iXbY8Uhvrzhw41lUMxbYlSG16cta0Qsp7jlRXoitZm3J2F8vJFnPD5DnaXaat6irtIosqam+SGPZFEpswmcbw9JXsdEpDNW3s+UWdwVqN193nMVxuJeGcZk6+6UW7Ru1ECiDk5m0GjlXL8ROrU3yeG8erxK2rfGsqGYSy846oJwkaSsBvSL9XWyRCzwI9s2VGfPjcA8pSE3g5sp30Dk+pQ90nWc0zTeCpYULVVxOugboCktZBhmkudGM8uw4XUt4leeVvdij6glNA74+XAXFohqfOZq6ladzS/fOanZgt8EGQw9Z4pzTRgbkvF9V+8VFEiJJpg7t9gybczSaV9qeUAMV1UvVkkbXyNVbVzutJvNjbuXHEkY4Oe3HvsvES3ITCCsnItiEdPL4mBuYmqYHpsUdy+AcjbPF9rqruSbLNwFRVN56nHlgXE5qw1jHlB03UW4tNtzRZC5UvUx3o9zKKHezdlUGwwlzfR5bmZI55UyM6l1Oru0p3EBSY4sKR4C7rNXRZeVPzh3VHD19jbcHHVJN3574AyGuXOmEL9ytMiMmZJox5zJTxPOmj3w0C1a87xi6aCokZbMlta5L91yH9ogbL1h7J58lm6G3ym4/ugJfTDWAxdgmhJuES0LLNHuda762uhJYd2BX2bjZtrtdWrMtUEbpdXbgeXkMCaHpGwJn+0iQT+BQHq70eSL0i1Ld9m7Az7Y1JRqrmaHGQKy8ywjl1t2yWy0bHB3tL7Qrbi3UxTvaurhoWLhLMAqBDOajoyTE2FLoXFc15k3QpCvb4ffbkXRU1IVPrxz63Mb2hFe2rEyGqC+FKh3OpONciSOU77XkkupXMzlVK7YV+ul1N86n4qLtSN+WZHECKxx/dkn5mq66nXJaK2yiV8xIO5GXldGgXLwi6IoaL0E68hsOPdPzy/4Szi6M6KeEPj6ejo7unG1+A2tZccXZ9Zjeg4u9Utr91FiS3PbMFwUBqspcB6QVjQwdhCO09tC2kxJKyrwTk+RMXuXA9ALgrDg8I8feXhYifTbL5VPHZHv+1KduNiGyhARGoB1olGr3se2eyMgc2eJp7JFLoWLYwypzL1po8DuRELTz6dAa2+v2kEfgpFZyD3f6CT9uR0uJXZNBQNIhGde0UmZsS7pSK2L5ugsSYX9c+ifcr/NTNxuv8l5Nt66PB9vLoZoEzmJSGLuLv/CYwxYtsW5ULnyMRpeOKHnn+ZRh6pVLNbMqjEV+5YfqwvPjcFHZWN86u9XKCfyzfJk10iU7C6GU2BdSd7a2pJ50siEmNtziXMo6VMaKfbjGcdaB6/7EZ9UiPV6JxpjPt9q2PV/Ezexqxwc9aDbUVCizupTrcShVwbWR0/2edUeEWJncssol0ctcf8+ep0tYF4WLnZnGSgIWQcs527bGyiwMNEgluHulzhcnPVuzCahtzFlI5JXiW4HV+dnSbhUhoGDb0Oyky362oCjRZsL5ateNFtnWE7YbVI1NUTHkVYzhujCt0fWmFsYBe+HmGEd6Brr2F/RlOm7Zk7BvphTJN0fgehQlLDwhygKsWae+h/mVRaer9fF4wS69GdhsWnj1WII91nRKLJqLPLXlqVfN0CU6KgPmQB4xviZTfCZo+y4V47XB7HKfFRPZrjMzoyBLyudVwUQbqyG0ZjQvpxeCRbkiZ32tWE6bSxQErcMyDmFdRtXEbXAyacaTY9RcLUHYp329nF44eslqDp3PDwFl0vM5zilttlQPxGY/dib1UlcvNTl1mqy0VZey7FodT0bsKV6cxJ1I7Y8uafk64YhRfObDdFt2wjhbp3PWb1mHlwPLnq8FdH/e59Q0xTfX0+qw3urbRUQadQl7MqyYboiKBIVJHfaTM7o7z2ZGv7iMK32ZLcxxeFl4aX3eO1KaTqmIVNZ7HqDjfLv2KtOw94t0eRpPXYbKMcapG93jxkyunsfXXrW82uFb64T12DryD1g8ERK40cv35hZjMX6uJnTkl6M8Xu3ETePASDf4Xr04uNkz4hnYF42s3YLYj3zRZmNfSfp4Pp//9NPT89PtTe/TK45NJ9Tz0/B64HHI//ePh/1rWLw95I2p8fj56f/uxPJ+evj+KvB25A8s9/W2+uvfVfWX56fSCaFa92PlKmn8x1Hlfzmf/fzPnRwPMvr7q+vh7WVXv78vqS3/drwdZm5T1WX/VuVJczvchsA31fBnLNXb40XD083AtKhvzz4MgldBWIK3Oh8OaeG3p+GvTIY3csAN78+HS//xPuD5ye2hA0OnehtPyTdQFoO1j/dSw0Hu8GLq6bf/BL9I7R6mJwAA -->
