---
name: "rar-kody-w-connected-solution"
description: "Turn an agent stack (a folder of BasicAgent *.py files + optional metadata.json) or an explicit list of sub-agents into ONE import-ready Microsoft Copilot Studio connected-agent solution: an orchestrator plus one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. When an agent.py carries its compiled CapIR (t2p-capir/1.0) \u2014 or one can be recompiled from its seeded data \u2014 each sub-agent ALSO gets a REAL deterministic capability topic that runs the same steps as the agent.py's perform() (trigger -> the user's real query -> filter the seeded records -> branch -> respond, plus the document for artifact capabilities); only the data is mocked, so flipping the in-topic Table() to a live Dataverse / SharePoint connector is the one-line move to production. No code deploy. Bot names are auto-capped to 42 chars and orchestrator channels default off so it imports and publishes fully headlessly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/connected_solution_agent", "rar_sha256": "23c5edf7914db69119e2463a528c4d6a2dee964b94f5f6b90f9dffbd1d58c9af", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/connected_solution_agent`. The original RAPP
agent is preserved byte-for-byte in `connected_solution_agent.py` and in the RCI capsule.

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

Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "capir_mode": {
      "description": "How to build the deterministic per-capability topic inside each sub-agent (the topic that runs the agent.py's perform() logic on STATIC synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else real seeded data, else SYNTHESIZES static stand-in records from the agent's inferred data shape \u2014 so EVERY agent.py maps to a self-documented topic; 'static' uses only real seeded data (no synthetic stand-in); 'embedded' uses only an embedded CapIR; 'off' emits instructions-only sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
      "type": "string"
    },
    "credentials_path": {
      "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE (under a top-level 'Values' object or at the root). Used only for deploy; the secret is never echoed back. If omitted, env vars / ~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
      "type": "string"
    },
    "deploy": {
      "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot Studio (Dataverse) environment and publish every bot (sub-agents first, orchestrator last) \u2014 no pac CLI needed, stdlib only. App-registration credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file \u2014 NEVER from chat. Default false (package only).",
      "type": "boolean"
    },
    "environment_url": {
      "description": "Optional override for the target Dataverse environment URL (e.g. https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
      "type": "string"
    },
    "orchestrator_channels": {
      "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false (headlessly publishable). True requires a maker-portal publish.",
      "type": "boolean"
    },
    "orchestrator_name": {
      "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
      "type": "string"
    },
    "output_path": {
      "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
      "type": "string"
    },
    "publish": {
      "description": "When deploy=true, also publish the bots after import (default true). false imports without publishing.",
      "type": "boolean"
    },
    "publisher_display": {
      "description": "Solution publisher friendly name (default 'Default Publisher').",
      "type": "string"
    },
    "publisher_name": {
      "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
      "type": "string"
    },
    "publisher_prefix": {
      "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a distinct solution instead of updating ones that already exist.",
      "type": "string"
    },
    "solution_display_name": {
      "description": "Solution friendly name.",
      "type": "string"
    },
    "solution_name": {
      "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
      "type": "string"
    },
    "stack_dir": {
      "description": "Path to an agent stack folder. Each BasicAgent *.py under it (or its agents/ subfolder) becomes one connected sub-agent; metadata.json (name/description/features/starters) shapes the orchestrator.",
      "type": "string"
    },
    "subagents": {
      "description": "Alternative to stack_dir: explicit sub-agents, each an object with agent_name, display_name, description, instructions.",
      "type": "array"
    },
    "version": {
      "description": "Solution version, e.g. 1.0.0.0.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `connected_solution_agent.py` and embedded as the fenced Python below (sha256 23c5edf7914db691…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `connected_solution_agent.py` first:

```bash
python3 connected_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 connected_solution_agent.py   # or on stdin
python3 connected_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/connected_solution_agent",
    "version": "1.0.3",
    "display_name": "ConnectedSolution",
    "description": "Packages a BasicAgent stack into an import-ready Copilot Studio connected-agents solution zip, optionally publishing via the Dataverse Web API.",
    "author": "Kody Wildfeuer",
    "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import io
import os
import re
import sys
import json
import ast
import base64
import uuid
import zipfile
import logging
import urllib.request
import urllib.parse
import urllib.error
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

# PUBLISHER PREFIX. Kody, 2026-08-27: "make it aibast for now."
#
# Env-overridable rather than hardcoded, because this repo is public: a bare "aibast"
# default would stamp every stranger's generated solution with a publisher that is not
# theirs, and a solution carrying the wrong publisher is a real problem for them to unpick
# in a tenant. Setting RAPP_PUBLISHER_PREFIX overrides it; unset, it is aibast.
_DEFAULT_PUBLISHER_PREFIX = os.getenv("RAPP_PUBLISHER_PREFIX", "aibast")

logger = logging.getLogger("connected_solution_agent")

# BasicAgent base — use the RAPP runtime's when present, else a minimal shim so
# this file also runs standalone (python connected_solution_agent.py <stack_dir>).
try:  # the RAPP runtime's base when hosted; a minimal shim when standalone
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:  # minimal fallback
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", self.__class__.__name__)
                self.metadata = metadata or getattr(self, "metadata", {})

# ============================================================================
# Embedded Copilot Studio solution templates (verbatim from the proven packager)
# ============================================================================

DEFAULT_ICON_BASE64 = (
    "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"
)

SOLUTION_XML_NATIVE = """\
<ImportExportXml version="9.2.26023.151" SolutionPackageVersion="9.2" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <SolutionManifest>
    <UniqueName>{solution_unique_name}</UniqueName>
    <LocalizedNames>
      <LocalizedName description="{solution_display_name}" languagecode="1033" />
    </LocalizedNames>
    <Descriptions />
    <Version>{solution_version}</Version>
    <Managed>{managed_flag}</Managed>
    <Publisher>
      <UniqueName>{publisher_unique_name}</UniqueName>
      <LocalizedNames>
        <LocalizedName description="{publisher_display_name}" languagecode="1033" />
      </LocalizedNames>
      <Descriptions>
        <Description description="Auto-generated publisher" languagecode="1033" />
      </Descriptions>
      <EMailAddress xsi:nil="true"></EMailAddress>
      <SupportingWebsiteUrl xsi:nil="true"></SupportingWebsiteUrl>
      <CustomizationPrefix>{publisher_prefix}</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
      <Addresses>
        <Address>
          <AddressNumber>1</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
        <Address>
          <AddressNumber>2</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
      </Addresses>
    </Publisher>
    <RootComponents />
    <MissingDependencies />
  </SolutionManifest>
</ImportExportXml>"""

CUSTOMIZATIONS_XML_NATIVE = """\
<ImportExportXml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <Entities></Entities>
  <Roles></Roles>
  <Workflows></Workflows>
  <FieldSecurityProfiles></FieldSecurityProfiles>
  <Templates />
  <EntityMaps />
  <EntityRelationships />
  <OrganizationSettings />
  <optionsets />
  <CustomControls />
  <EntityDataProviders />
  <connectionreferences>
{connection_references}
  </connectionreferences>
  <Languages>
    <Language>1033</Language>
  </Languages>
</ImportExportXml>"""

CONTENT_TYPES_XML_NATIVE = '<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/octet-stream" /><Default Extension="json" ContentType="application/octet-stream" />{overrides}</Types>'

CONTENT_TYPE_OVERRIDE = '<Override PartName="/{part_name}" ContentType="application/octet-stream" />'

BOT_XML = """\
<bot schemaname="{bot_schema}">
  <authenticationmode>2</authenticationmode>
  <authenticationtrigger>1</authenticationtrigger>
  <iconbase64>{icon_base64}</iconbase64>
  <iscustomizable>0</iscustomizable>
  <language>1033</language>
  <name>{bot_display_name}</name>
  <runtimeprovider>0</runtimeprovider>
  <template>default-2.1.0</template>
</bot>"""

BOT_CONFIGURATION_JSON_NATIVE = """{{
  "$kind": "BotConfiguration",
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": false
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

ORCHESTRATOR_CHANNELS_BLOCK = """
  "channels": [
    {
      "$kind": "ChannelDefinition",
      "channelId": "MsTeams"
    },
    {
      "$kind": "ChannelDefinition",
      "channelId": "Microsoft365Copilot"
    }
  ],"""

ORCHESTRATOR_CONFIGURATION_JSON = """{{
  "$kind": "BotConfiguration",{channels_block}
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,{publish_on_import_line}
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "isLightweightBot": false,
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": true
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

GPT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>15</componenttype>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

GPT_DATA_YAML = """\
kind: GptComponentMetadata
displayName: {display_name}
instructions: |-
{instructions_indented}
gptCapabilities:
  webBrowsing: true
  codeInterpreter: true

aISettings:
  model:
    modelNameHint: GPT5Chat

  extensionData:
    lastUsedCustomModel: {{}}

declarativeSkillsMetadata:"""

BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>{component_type}</componenttype>{description_element}
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

CONN_REF_SET_XML = """\
<botcomponent_connectionreferenceset>
{entries}
</botcomponent_connectionreferenceset>"""

INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>9</componenttype>
  <description>{description}</description>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{orchestrator_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

INVOKE_CONNECTED_AGENT_DATA = """\
kind: TaskDialog
modelDisplayName: {display_name}
modelDescription: |-
{description_indented}{inputs_block}
action:
  kind: InvokeConnectedAgentTaskAction{input_type_block}
  botSchemaName: {child_schema}
  historyType:
    kind: ConversationHistory"""


def _connected_inputs_yaml(params):
    """The orchestrator-side typed inputs for a connected agent, from the source
    agent.py's perform() params. Per the Copilot Studio connected-agent schema:
    `inputs` (AutomaticTaskInput list) sits at the TaskDialog root and `inputType`
    sits INSIDE the action block. These populate the connected agent's Inputs
    panel and let the orchestrator pass the params when it delegates. Returns
    (inputs_block, input_type_block) — both '' when there are no params."""
    params = params or []
    if not params:
        return "", ""
    inlines, props = [], []
    for entry in params:
        pn = entry[0] if isinstance(entry, (list, tuple)) else entry
        required = bool(entry[2]) if isinstance(entry, (list, tuple)) and len(entry) > 2 else False
        name = re.sub(r"[^A-Za-z0-9_]", "", str(pn)) or "input"
        inlines.append("  - kind: AutomaticTaskInput\n    propertyName: " + name)
        props.append("      " + name + ":\n"
                     "        displayName: " + name + "\n"
                     "        isRequired: " + ("true" if required else "false") + "\n"
                     "        type: String")
    return ("\ninputs:\n" + "\n".join(inlines),
            "\n  inputType:\n    properties:\n" + "\n".join(props))

INVOKE_CONNECTED_AGENT_DEPENDENCIES = '[{{"type":"bot","schemaName":"{child_schema}"}}]'

SYSTEM_TOPICS = {
    "ConversationStart": {
        "display_name": "Conversation Start",
        "description": "This system topic triggers when the agent receives an Activity indicating the beginning of a new conversation. If you do not want the agent to initiate the conversation, disable this topic.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnConversationStart
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_M0LuhV
      activity:
        text:
          - Hello, I'm {{System.Bot.Name}}. How can I help?
        speak:
          - Hello and thank you for calling {{System.Bot.Name}}. Please note that some responses are generated by AI and may require verification for accuracy. How may I help you today?"""
    },
    "EndofConversation": {
        "display_name": "End of Conversation",
        "description": "This system topic is only triggered by a redirect action,\nand guides the user through rating their conversation with the agent.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: Question
      id: 41d42054-d4cb-4e90-b922-2b16b37fe379
      conversationOutcome: ResolvedImplied
      alwaysPrompt: true
      variable: init:Topic.SurveyResponse
      prompt: Did that answer your question?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition-0
      conditions:
        - id: condition-0-item-0
          condition: =Topic.SurveyResponse = true
          actions:
            - kind: CSATQuestion
              id: csat_1
              conversationOutcome: ResolvedConfirmed

            - kind: SendActivity
              id: sendMessage_8r29O0
              activity: Thanks for your feedback.

            - kind: Question
              id: question_1
              alwaysPrompt: true
              variable: init:Topic.Continue
              prompt: Can I help with anything else?
              entity: BooleanPrebuiltEntity

            - kind: ConditionGroup
              id: condition-1
              conditions:
                - id: condition-1-item-0
                  condition: =Topic.Continue = true
                  actions:
                    - kind: SendActivity
                      id: sendMessage_4eOE6h
                      activity: Go ahead. I'm listening.

              elseActions:
                - kind: SendActivity
                  id: yHBz55
                  activity: Ok, goodbye.

                - kind: EndConversation
                  id: jh1GMT

      elseActions:
        - kind: Question
          id: PM68ot
          alwaysPrompt: true
          variable: init:Topic.TryAgain
          prompt: Sorry I wasn't able to help better. Would you like to try again?
          entity: BooleanPrebuiltEntity

        - kind: ConditionGroup
          id: KNxYBf
          conditions:
            - id: DPveFP
              condition: =Topic.TryAgain = false
              actions:
                - kind: BeginDialog
                  id: cngqi4
                  dialog: {bot_schema}.topic.Escalate

          elseActions:
            - kind: SendActivity
              id: GrVHEW
              activity: Go ahead. I'm listening."""
    },
    "Escalate": {
        "display_name": "Escalate",
        "description": "This system topic is triggered when the user indicates they would like to speak to a representative.\nYou can configure how the agent will handle human hand-off scenarios in the agent settings..\nIf your agent does not handle escalations, this topic should be disabled.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnEscalate
  id: main
  intent:
    displayName: Escalate
    includeInOnSelectIntent: false
    triggerQueries:
      - Talk to agent
      - Talk to a person
      - Talk to someone
      - Call back
      - Call customer service
      - Call me please
      - Call support
      - Call technical support
      - Can an agent call me
      - Can I call
      - Can I get in touch with someone else
      - Can I get real agent support
      - Can I get transferred to a person to call
      - Can I have a call in number Or can I be called
      - Can I have a representative call me
      - Can I schedule a call
      - Can I speak to a representative
      - Can I talk to a human
      - Can I talk to a human assistant
      - Can someone call me
      - Chat with a human
      - Chat with a representative
      - Chat with agent
      - Chat with someone please
      - Connect me to a live agent
      - Connect me to a person
      - Could some one contact me by phone
      - Customer agent
      - Customer representative
      - Customer service
      - I need a manager to contact me
      - I need customer service
      - I need help from a person
      - I need to speak with a live argent
      - I need to talk to a specialist please
      - I want to talk to customer service
      - I want to proceed with live support
      - I want to speak with a consultant
      - I want to speak with a live tech
      - I would like to speak with an associate
      - I would like to talk to a technician
      - Talk with tech support member

  actions:
    - kind: SendActivity
      id: sendMessage_s39DCt
      conversationOutcome: Escalated
      activity: |-
        Escalating to a representative is not currently configured for this agent, however this is where the agent could provide information about how to get in touch with someone another way.

        Is there anything else I can help you with?"""
    },
    "Fallback": {
        "display_name": "Fallback",
        "description": "This system topic triggers when the user's utterance does not match any existing topics.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_LktzXw
      conditions:
        - id: conditionItem_tlGIVo
          condition: =System.FallbackCount < 3
          actions:
            - kind: SendActivity
              id: sendMessage_QZreqo
              activity: I'm sorry, I'm not sure how to help with that. Can you try rephrasing?

      elseActions:
        - kind: BeginDialog
          id: 5aXj5M
          dialog: {bot_schema}.topic.Escalate"""
    },
    "Goodbye": {
        "display_name": "Goodbye",
        "description": "This topic triggers when the user says goodbye. By default, it does not end the conversation. If you would like to end the conversation when the user says goodbye, you can add an \"End of Conversation\" action to this topic, or redirect to the \"End of Conversation\" system topic.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Goodbye
    includeInOnSelectIntent: false
    triggerQueries:
      - Bye
      - Bye for now
      - Bye now
      - Good bye
      - No thank you. Goodbye.
      - See you later

  actions:
    - kind: Question
      id: question_zf2HhP
      variable: Topic.EndConversation
      prompt: Would you like to end our conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition_DGc1Wy
      conditions:
        - id: condition_DGc1Wy-item-0
          condition: =Topic.EndConversation = true
          actions:
            - kind: BeginDialog
              id: dn94DC
              dialog: {bot_schema}.topic.EndofConversation

        - id: condition_DGc1Wy-item-1
          condition: =Topic.EndConversation = false
          actions:
            - kind: SendActivity
              id: sendMessage_LdLhmf
              activity: Go ahead. I'm listening."""
    },
    "Greeting": {
        "display_name": "Greeting",
        "description": "This topic is triggered when the user greets the agent.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Greeting
    includeInOnSelectIntent: false
    triggerQueries:
      - Good afternoon
      - Good morning
      - Hello
      - Hey
      - Hi

  actions:
    - kind: SendActivity
      id: sendMessage_abmysR
      activity:
        text:
          - Hello, how can I help you today?
        speak:
          - Hello, <break strength="medium" /> how can I help?

    - kind: CancelAllDialogs
      id: cancelAllDialogs_01At22"""
    },
    "MultipleTopicsMatched": {
        "display_name": "Multiple Topics Matched",
        "description": "This system topic triggers when the agent matches multiple Topics with the incoming message and needs to clarify which one should be triggered.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSelectIntent
  id: main
  triggerBehavior: Always
  actions:
    - kind: SetVariable
      id: setVariable_M6434i
      variable: init:Topic.IntentOptions
      value: =System.Recognizer.IntentOptions

    - kind: SetTextVariable
      id: setTextVariable_0
      variable: Topic.NoneOfTheseDisplayName
      value: None of these

    - kind: EditTable
      id: sendMessage_g5Ls09
      changeType: Add
      itemsVariable: Topic.IntentOptions
      value: "={{ DisplayName: Topic.NoneOfTheseDisplayName, TopicId: \\"NoTopic\\", TriggerId: \\"NoTrigger\\", Score: 1.0 }}"

    - kind: Question
      id: question_zf2HhP
      interruptionPolicy:
        allowInterruption: false

      alwaysPrompt: true
      variable: System.Recognizer.SelectedIntent
      prompt: "To clarify, did you mean:"
      entity:
        kind: DynamicClosedListEntity
        items: =Topic.IntentOptions

    - kind: ConditionGroup
      id: conditionGroup_60PuXb
      conditions:
        - id: conditionItem_rs7GgM
          condition: =System.Recognizer.SelectedIntent.TopicId = "NoTopic"
          actions:
            - kind: ReplaceDialog
              id: YZXRDb
              dialog: {bot_schema}.topic.Fallback"""
    },
    "OnError": {
        "display_name": "On Error",
        "description": "This system topic triggers when the agent encounters an error. When using the test chat pane, the full error description is displayed.",
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnError
  id: main
  actions:
    - kind: SetVariable
      id: setVariable_timestamp
      variable: init:Topic.CurrentTime
      value: =Text(Now(), DateTimeFormat.UTC)

    - kind: ConditionGroup
      id: condition_1
      conditions:
        - id: bL4wmY
          condition: =System.Conversation.InTestMode = true
          actions:
            - kind: SendActivity
              id: sendMessage_XJBYMo
              activity: |-
                Error Message: {{System.Error.Message}}
                Error Code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}

      elseActions:
        - kind: SendActivity
          id: sendMessage_dZ0gaF
          activity:
            text:
              - |-
                An error has occurred.
                Error code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}.
            speak:
              - An error has occurred, please try again.

    - kind: LogCustomTelemetryEvent
      id: 9KwEAn
      eventName: OnErrorLog
      properties: "={{ErrorMessage: System.Error.Message, ErrorCode: System.Error.Code, TimeUTC: Topic.CurrentTime, ConversationId: System.Conversation.Id}}"

    - kind: CancelAllDialogs
      id: NW7NyY"""
    },
    "ResetConversation": {
        "display_name": "Reset Conversation",
        "description": None,
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_OPsT1O
      activity: What can I help you with?

    - kind: ClearAllVariables
      id: clearAllVariables_73bTFR
      variables: ConversationScopedVariables

    - kind: CancelAllDialogs
      id: cancelAllDialogs_12Gt21"""
    },
    "Search": {
        "display_name": "Conversational boosting",
        "description": "Create generative answers from knowledge sources.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  priority: -1
  actions:
    - kind: SearchAndSummarizeContent
      id: search-content
      variable: Topic.Answer
      userInput: =System.Activity.Text

    - kind: ConditionGroup
      id: has-answer-conditions
      conditions:
        - id: has-answer
          condition: =!IsBlank(Topic.Answer)
          actions:
            - kind: EndDialog
              id: end-topic
              clearTopicQueue: true"""
    },
    "Signin": {
        "display_name": "Sign in ",
        "description": "This system topic triggers when the agent needs to sign in the user or require the user to sign in",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSignIn
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_ypjGKL
      conditions:
        - id: conditionItem_7XYIIR
          condition: =System.SignInReason = SignInReason.SignInRequired
          actions:
            - kind: SendActivity
              id: sendMessage_1jHUNO
              activity: Hello! To be able to help you, I'll need you to sign in.

    - kind: OAuthInput
      id: gOjhZA
      title: Login
      text: To continue, please login"""
    },
    "StartOver": {
        "display_name": "Start Over",
        "description": None,
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Start Over
    includeInOnSelectIntent: false
    triggerQueries:
      - let's begin again
      - start over
      - start again
      - restart

  actions:
    - kind: Question
      id: question_zguoVV
      alwaysPrompt: false
      variable: init:Topic.Confirm
      prompt: Are you sure you want to restart the conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: conditionGroup_lvx2zV
      conditions:
        - id: conditionItem_sVQtHa
          condition: =Topic.Confirm = true
          actions:
            - kind: BeginDialog
              id: 0YKYsy
              dialog: {bot_schema}.topic.ResetConversation

      elseActions:
        - kind: SendActivity
          id: sendMessage_lk2CyQ
          activity: Ok. Let's carry on."""
    },
    "ThankYou": {
        "display_name": "Thank you",
        "description": "This topic triggers when the user says thank you.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Thank you
    includeInOnSelectIntent: false
    triggerQueries:
      - thanks
      - thank you
      - thanks so much
      - ty

  actions:
    - kind: SendActivity
      id: sendMessage_9iz6v7
      activity: You're welcome."""
    },
}


# ============================================================================
# Packager: orchestrator + connected sub-agents, with the 42-char name cap,
# 100-char schema cap, and optional channels (default off = headless-publishable)
# ============================================================================

MAX_SCHEMA = 100


_CONNECTED_INFIX = ".InvokeConnectedAgentTaskAction."   # 32 chars (incl. both dots)


_MIN_ACTION_BUDGET = 26   # always leave at least this many chars for the action suffix


MAX_BOT_NAME = 42


def _cap_bot_name(name: str, preserve_suffix: Optional[str] = None) -> str:
    """Truncate a bot display name to the 42-char limit, keeping a trailing word
    like 'Orchestrator' intact when present."""
    name = (name or "").strip()
    if len(name) <= MAX_BOT_NAME:
        return name
    if preserve_suffix and name.endswith(preserve_suffix):
        budget = MAX_BOT_NAME - len(preserve_suffix) - 1
        head = name[: -len(preserve_suffix)].rstrip()[:budget].rstrip()
        return f"{head} {preserve_suffix}"
    return name[:MAX_BOT_NAME].rstrip()


def _sanitize_schema(name: str) -> str:
    """Lowercase alphanumeric fragment for a bot schema name."""
    return re.sub(r"[^a-zA-Z0-9]", "", name or "").lower()


def _pascal(name: str) -> str:
    """PascalCase alphanumeric fragment for a connected-action schema name."""
    parts = re.split(r"[^a-zA-Z0-9]+", name or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _xml_escape(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _indent(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(f"{pad}{line}" for line in (text or "").split("\n"))


def _yaml_display_safe(text: str) -> str:
    """Make a one-line value safe as a bare YAML scalar (no colons/quotes/newlines)."""
    clean = re.sub(r"\s+", " ", (text or "").replace(":", " -")).strip()
    return clean.replace('"', "").replace("'", "")


# ============================================================================
# CapIR -> deterministic capability topic (the 1:1 conversion)
#
# A converted agent.py compiles its perform() to a CapIR (t2p-capir/1.0). When a
# sub-agent carries that CapIR, the packager emits a REAL Copilot Studio topic
# that runs the SAME steps perform() runs: OnRecognizedIntent (the agent's real
# triggers) -> Question (the user's real input) -> SetVariable Table() of the
# SEEDED records -> Filter by the real query -> branch -> SendActivity, plus a
# document render for artifact-producing capabilities. The control flow is real;
# only the DATA is mocked. Flipping the in-topic Table() to a Dataverse /
# SharePoint connector (binding.connector) is the one-line move to live data, and
# the same filter/respond/document logic runs unchanged. This is the opposite of
# an actions:[]+modelDescription "gamed" topic.
# ============================================================================

def _yaml_dq(text) -> str:
    """A YAML double-quoted scalar: robust for Power Fx expressions and message
    text (escapes backslash/quote, encodes newlines)."""
    s = (str(text).replace("\\", "\\\\").replace('"', '\\"')
         .replace("\n", "\\n").replace("\t", "\\t").replace("\r", ""))
    return '"' + s + '"'


def _pfx_str(value) -> str:
    """A Power Fx double-quoted string literal (internal quotes doubled)."""
    return '"' + str(value).replace('"', '""') + '"'


def _pfx_safe_text(text) -> str:
    """Strip literal braces from message text so Copilot Studio does not parse
    them as variable bindings (unparseable {...} fails publish). Template tokens
    like {Topic.X} are added AFTER this, so they survive."""
    return str(text).replace("{", "(").replace("}", ")")


def _capir_topic_fields(records):
    """Stable union of record field names (the Table()/filter columns) when the
    binding omits an explicit field list (recovered / recompiled CapIRs)."""
    fields = []
    for r in records or []:
        if isinstance(r, dict):
            for k in r.keys():
                if k not in fields:
                    fields.append(k)
    return fields


def _numeric_metric_field(records, fields, hint=None):
    """Pick the field numeric-threshold queries compare against (e.g. "assets
    above a 30% failure probability" -> a real `Value(field) >= 0.30`). A field
    qualifies only if it parses as a number in EVERY record (so Power Fx Value()
    never errors). Prefers probability/score-like names and 0..1-ranged fields;
    honors an explicit binding `metric_field` hint."""
    if hint and hint in (fields or []):
        return hint
    if not records:
        return None
    numeric, ratio = [], []
    for f in fields:
        vals, ok = [], True
        for r in records:
            if not isinstance(r, dict) or f not in r or str(r.get(f)).strip() == "":
                ok = False; break
            try:
                vals.append(float(str(r.get(f)).strip()))
            except (TypeError, ValueError):
                ok = False; break
        if ok and vals:
            numeric.append(f)
            if all(0.0 <= v <= 1.0 for v in vals):
                ratio.append(f)
    pool = ratio or numeric
    if not pool:
        return None
    for pat in (r"p_?fail|prob|likeli|risk", r"score|rate|ratio|pct|percent|conf"):
        for f in pool:
            if re.search(pat, f, re.I):
                return f
    return pool[0]


# The load-bearing perform() constants (t2p-capir/1.0 CAPIR_CONSTS). The topic
# reads these off the CapIR when present so it mirrors the agent.py's numbers.
_CAPIR_TOPIC_CONSTS = {
    "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


def capir_topic_action_name(capir: dict) -> str:
    """The custom-topic schema suffix for a capability: Handle<Pascal(key)>."""
    key = (capir or {}).get("key") or "capability"
    return "Handle" + (_pascal(key) or "Capability")


def capir_topic_data_yaml(display_name: str, capir: dict) -> str:
    """Render a capability's CapIR into a REAL deterministic Copilot Studio topic
    'data' YAML that goes INSIDE the sub-agent: OnRecognizedIntent triggers ->
    Question (slot) -> SetVariable Table() of the SEEDED records -> Filter by the
    real query -> ConditionGroup on the match count -> SendActivity, plus (for an
    artifact capability) a SetVariable that renders the document from the matched
    (or fallback) records exactly like perform()'s artifact step. The synthetic
    records live IN the topic and the control flow runs deterministically; only
    the DATA is mocked. Structural 1:1 with the generated agent.py's perform()."""
    capir = capir or {}
    consts = dict(_CAPIR_TOPIC_CONSTS)
    consts.update(capir.get("consts") or {})
    binding = capir.get("binding") or {}
    fields = binding.get("fields") or _capir_topic_fields(binding.get("records"))
    table = binding.get("table") or "records"
    records = binding.get("records") or []
    customer = str(capir.get("customer") or "the customer")
    response = _pfx_safe_text(capir.get("response") or f"Here is how I handle {display_name}.")
    # triggers + grounding facts + the artifact doc come straight from the steps
    triggers, facts, doc = [], [], None
    for step in capir.get("steps") or []:
        op = step.get("op")
        if op == "trigger_match":
            triggers = step.get("queries") or []
        elif op == "knowledge_lookup":
            facts = step.get("facts") or []
        elif op == "artifact":
            doc = step.get("doc")
    prompt = None
    for slot in capir.get("slots") or []:
        prompt = slot.get("prompt"); break
    prompt = prompt or f"What would you like help with for {display_name}?"

    # Power Fx: a real Table() of the seeded records, a real query Filter, a real
    # count, then a real branch -- the exact perform() path.
    recs = []
    for r in records:
        if isinstance(r, dict):
            cells = ", ".join("%s: %s" % (f, _pfx_str(r.get(f, ""))) for f in fields)
            recs.append("{" + cells + "}")
    table_pfx = "=Table(" + ", ".join(recs) + ")" if recs else "=Blank()"
    conds = " || ".join("(Lower(ThisRecord.%s) in Lower(Topic.Query))" % f for f in fields)
    text_clause = "(%s)" % (conds or "false")

    # numeric-threshold support: a query like "assets above a 30% failure
    # probability" sets Topic.Threshold (number, %-aware) + Topic.Direction
    # (ge/le) and the Filter does a REAL Value()-comparison on the metric field,
    # not just text containment. Falls back to text match when no number is asked.
    metric_field = _numeric_metric_field(records, fields, (binding.get("metric_field")))
    threshold_actions, filter_inner = "", text_clause
    if metric_field:
        num_re = r"\d+\.?\d*"
        thr_pfx = ('=If(IsMatch(Topic.Query, "\\d"), '
                   'Value(First(MatchAll(Topic.Query, "' + num_re + '")).FullMatch) '
                   '/ If(IsMatch(Topic.Query, "%"), 100, 1), Blank())')
        dir_pfx = ('=If(IsMatch(Lower(Topic.Query), "above|over|greater|more than|exceed|at least|higher|>"), "ge", '
                   'If(IsMatch(Lower(Topic.Query), "below|under|less|fewer|within|at most|lower|<"), "le", "ge"))')
        threshold_actions = (
            "    - kind: SetVariable\n"
            "      id: setThreshold\n"
            "      variable: Topic.Threshold\n"
            "      value: " + _yaml_dq(thr_pfx) + "\n"
            "    - kind: SetVariable\n"
            "      id: setDirection\n"
            "      variable: Topic.Direction\n"
            "      value: " + _yaml_dq(dir_pfx) + "\n")
        num_clause = ('(!IsBlank(Topic.Threshold) && If(Topic.Direction = "le", '
                      'Value(ThisRecord.' + metric_field + ') <= Topic.Threshold, '
                      'Value(ThisRecord.' + metric_field + ') >= Topic.Threshold))')
        filter_inner = "(" + text_clause + " || " + num_clause + ")"
    filter_pfx = "=Filter(Topic.Records, !IsBlank(Topic.Query) && " + filter_inner + ")"

    grounding = "\n".join("- " + _pfx_safe_text(f) for f in facts)
    ground_block = ("\n\nGrounded in what you told us:\n" + grounding) if grounding else ""

    # artifact (op==artifact): render the document from the matched-or-fallback
    # records, exactly like perform()'s artifact step (hits[:pdf_records] with a
    # data[:fallback_take] fallback). Materializing the real downloadable file is
    # the live-data flip -- a Create-file / Convert-to-PDF flow over these records.
    doc_actions, doc_block = "", ""
    if doc and fields:
        cells_pfx = ' & " | " & '.join('"%s: " & Text(ThisRecord.%s)' % (f, f) for f in fields)
        source = ("If(Topic.MatchCount > 0, Topic.Matches, FirstN(Topic.Records, %d))"
                  % consts["fallback_take"])
        document_pfx = ("=Concat(FirstN(%s, %d), %s & Char(10))"
                        % (source, consts["pdf_records"], cells_pfx))
        doc_actions = (
            "    - kind: SetVariable\n"
            "      id: setDocument\n"
            "      variable: Topic.Document\n"
            "      value: " + _yaml_dq(document_pfx) + "\n")
        prepared = _pfx_safe_text(consts["pdf_prepared"].replace("{customer}", customer))
        footer = _pfx_safe_text(consts["pdf_footer"])
        safe_doc = _pfx_safe_text(str(doc))
        doc_block = ("\n\n[" + safe_doc + "] " + prepared + ":\n"
                     + "{Topic.Document}\n" + footer
                     + "\n(In production, a Create-file / Convert-to-PDF flow over these "
                       "records delivers the real " + safe_doc + ".)")

    hit_msg = (response + ground_block
               + "\n\nI found {Topic.MatchCount} matching record(s) in the "
               + table + " data (synthetic demo data - no customer data needed)."
               + doc_block)
    miss_msg = (response + ground_block
                + "\n\nNo matching record in the " + table
                + " data; here are reference examples to ground the answer."
                + doc_block)
    trig = "\n".join("      - " + _yaml_dq(t) for t in triggers) or ("      - " + _yaml_dq(display_name))

    # intake: ask for the value to filter on. We intentionally do NOT read an
    # orchestrator-passed `Global.<param>` here. A connected agent can only
    # reference a global it has DECLARED as external-settable, and the solution
    # package format gives no reliable way to emit that declaration — referencing
    # an undeclared Global makes Copilot Studio's topic checker throw a
    # PowerFxError ("Identifier not recognized"), which blocks publish. The
    # orchestrator still DECLARES + PASSES the typed inputs (see the connected
    # action's inputType); the agent's generative layer receives them, and this
    # deterministic topic captures the value it filters on via the Question.
    intake_actions = (
        "    - kind: Question\n"
        "      id: question_query\n"
        "      variable: Topic.Query\n"
        "      prompt: " + _yaml_dq(prompt) + "\n"
        "      entity: StringPrebuiltEntity\n")

    return (
        "kind: AdaptiveDialog\n"
        "beginDialog:\n"
        "  kind: OnRecognizedIntent\n"
        "  id: main\n"
        "  intent:\n"
        "    displayName: " + _yaml_dq(display_name) + "\n"
        "    includeInOnSelectIntent: false\n"
        "    triggerQueries:\n" + trig + "\n"
        "  actions:\n"
        + intake_actions +
        "    - kind: SetVariable\n"
        "      id: setRecords\n"
        "      variable: Topic.Records\n"
        "      value: " + _yaml_dq(table_pfx) + "\n"
        + threshold_actions +
        "    - kind: SetVariable\n"
        "      id: setMatches\n"
        "      variable: Topic.Matches\n"
        "      value: " + _yaml_dq(filter_pfx) + "\n"
        "    - kind: SetVariable\n"
        "      id: setCount\n"
        "      variable: Topic.MatchCount\n"
        "      value: " + _yaml_dq("=CountRows(Topic.Matches)") + "\n"
        + doc_actions +
        "    - kind: ConditionGroup\n"
        "      id: hasMatches\n"
        "      conditions:\n"
        "        - id: hasMatches_hit\n"
        "          condition: " + _yaml_dq("=Topic.MatchCount > 0") + "\n"
        "          actions:\n"
        "            - kind: SendActivity\n"
        "              id: replyHit\n"
        "              activity: " + _yaml_dq(hit_msg) + "\n"
        "      elseActions:\n"
        "        - kind: SendActivity\n"
        "          id: replyMiss\n"
        "          activity: " + _yaml_dq(miss_msg) + "\n"
    )


@dataclass
class SubAgentSpec:
    """One connected sub-agent (one agent.py promoted to its own bot)."""
    agent_name: str           # e.g. "loanoriginationassistant"
    display_name: str         # e.g. "Loan Origination Assistant"
    description: str          # routing description the orchestrator selects on
    instructions: str         # the sub-agent's gpt.default instruction blob
    # The capability's compiled CapIR (t2p-capir/1.0), records already injected.
    # When present, the packager emits a REAL deterministic topic INSIDE this
    # sub-agent that runs the same steps as the converted agent.py's perform(),
    # instead of leaving the behavior to the gpt.default instruction blob. The
    # instructions remain as the persona/router fallback.
    capir: Optional[dict] = None
    # The source agent.py's perform() params [(name, description, required), ...],
    # declared as typed INPUTS on the orchestrator's connected-agent action so the
    # Copilot Studio orchestrator passes them when it delegates (the agent's
    # "Inputs" panel) — the contract, structurally, not just in the description.
    params: Optional[list] = None


@dataclass
class ConnectedSolutionSpec:
    """A single solution bundling an orchestrator + N connected sub-agents."""
    solution_unique_name: str
    solution_display_name: str
    orchestrator_display_name: str
    subagents: List[SubAgentSpec]
    orchestrator_instructions: str = ""   # synthesized if empty
    publisher_prefix: str = _DEFAULT_PUBLISHER_PREFIX
    publisher_unique_name: str = "DefaultPublisher"
    publisher_display_name: str = "Default Publisher"
    solution_version: str = "1.0.0.0"
    managed: bool = False
    orchestrator_schema_suffix: str = "orchestrator"
    # When True the orchestrator auto-publishes on import. Leave False so the
    # import itself never depends on the (slower, fail-prone) publish step.
    orchestrator_publish_on_import: bool = False
    # When True the orchestrator declares MsTeams + M365 Copilot channels. This
    # requires a maker-portal publish (headless `pac copilot publish` 409s on the
    # channel registration). Default False = fully headlessly publishable.
    orchestrator_channels: bool = False


class ConnectedSolutionPackager:
    """Assembles a multi-bot connected-agent solution zip from a spec."""

    def __init__(self, spec: ConnectedSolutionSpec):
        self.spec = spec
        # publisher_prefix is the one untamed length input feeding the schema caps
        # below; bound it to Dataverse's 8-char prefix limit so no schema exceeds
        # MAX_SCHEMA for ANY direct caller (perform() already caps it). Mutate the
        # spec too so the CustomizationPrefix stays consistent with the schemas.
        spec.publisher_prefix = spec.publisher_prefix[:8]
        prefix = spec.publisher_prefix

        # Connected-agent components are named
        #   {orch_schema}.InvokeConnectedAgentTaskAction.{Action}
        # and the full schema name must stay within Dataverse's 100-char limit.
        # Cap the orchestrator schema (reserving room for the action suffix) so a
        # long stack name can never push a component name over the limit.
        suffix = spec.orchestrator_schema_suffix
        base = re.sub(r"stack$", "", _sanitize_schema(spec.solution_unique_name)) or "agents"
        orch = f"{prefix}_{base}{suffix}"
        max_orch = MAX_SCHEMA - len(_CONNECTED_INFIX) - _MIN_ACTION_BUDGET   # 42
        if len(orch) > max_orch:
            keep = max(4, max_orch - len(prefix) - 1 - len(suffix))
            orch = f"{prefix}_{base[:keep]}{suffix}"
        self.orch_schema = orch
        # Whatever room is left after the (capped) orchestrator schema + infix.
        self._action_budget = MAX_SCHEMA - len(_CONNECTED_INFIX) - len(self.orch_schema)

        # Assign a unique schema name + connected-action name to each sub-agent.
        self._children = []  # list of (SubAgentSpec, child_schema, action_name)
        seen_schemas = {self.orch_schema}
        seen_actions = set()
        # Children need room for a ".topic.<Name>" suffix within MAX_SCHEMA. The
        # orchestrator schema is capped above; children were NOT, so a long
        # solution + capability name overflowed the Dataverse 100-char limit.
        child_base_max = max(4, MAX_SCHEMA - 35 - len(prefix) - 1)
        for sub in spec.subagents:
            base = (_sanitize_schema(sub.agent_name) or "agent")[:child_base_max]
            child_schema = f"{prefix}_{base}"
            n = 2
            while child_schema in seen_schemas:
                child_schema = f"{prefix}_{base}{n}"
                n += 1
            seen_schemas.add(child_schema)

            pascal = _pascal(sub.display_name or sub.agent_name) or "Agent"
            action = pascal[: self._action_budget]
            n = 2
            while action in seen_actions:
                tag = str(n)
                action = pascal[: max(1, self._action_budget - len(tag))] + tag
                n += 1
            seen_actions.add(action)

            self._children.append((sub, child_schema, action))

    # -- public ----------------------------------------------------------

    def package(self, output_path: Optional[Path] = None) -> bytes:
        buf = io.BytesIO()
        overrides: List[str] = []  # /data parts for [Content_Types].xml

        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            # 1. solution + customizations (connector-less, empty RootComponents)
            zf.writestr("solution.xml", self._solution_xml())
            zf.writestr(
                "customizations.xml",
                CUSTOMIZATIONS_XML_NATIVE.format(connection_references=""),
            )

            # 2. Orchestrator bot (router) — instructions list the sub-agents
            self._write_bot(
                zf,
                bot_schema=self.orch_schema,
                display_name=self.spec.orchestrator_display_name,
                instructions=self._orchestrator_instructions(),
                overrides=overrides,
                is_orchestrator=True,
            )

            # 3. Connected-agent delegation components (under the orchestrator)
            for sub, child_schema, action in self._children:
                self._write_connected_action(
                    zf, sub, child_schema, action, overrides
                )

            # 4. Each sub-agent as its own connectable bot — now carrying the REAL
            #    deterministic capability topic (1:1 with its agent.py) when a
            #    CapIR is present.
            for sub, child_schema, _action in self._children:
                self._write_bot(
                    zf,
                    bot_schema=child_schema,
                    display_name=sub.display_name,
                    instructions=sub.instructions,
                    overrides=overrides,
                    capir=sub.capir,
                )

            # 5. Empty connection reference set (no connectors in this topology)
            zf.writestr(
                "Assets/botcomponent_connectionreferenceset.xml",
                CONN_REF_SET_XML.format(entries=""),
            )

            # 6. [Content_Types].xml — every extensionless /data part listed
            zf.writestr(
                "[Content_Types].xml",
                CONTENT_TYPES_XML_NATIVE.format(overrides="".join(overrides)),
            )

        data = buf.getvalue()
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(data)
        return data

    @property
    def bot_schemas(self) -> List[str]:
        return [self.orch_schema] + [c[1] for c in self._children]

    # -- bot writers -----------------------------------------------------

    def _write_bot(
        self,
        zf: zipfile.ZipFile,
        bot_schema: str,
        display_name: str,
        instructions: str,
        overrides: List[str],
        is_orchestrator: bool = False,
        capir: Optional[dict] = None,
    ) -> None:
        """Write a complete bot: bot.xml, configuration.json, gpt.default, system
        topics, and (for a sub-agent carrying a CapIR) the REAL deterministic
        capability topic that runs the same steps as the converted agent.py."""
        # Copilot Studio caps the bot name at 42 chars; keep "Orchestrator" intact.
        display_name = _cap_bot_name(
            display_name, preserve_suffix="Orchestrator" if is_orchestrator else None
        )
        # bot.xml + configuration.json
        zf.writestr(
            f"bots/{bot_schema}/bot.xml",
            BOT_XML.format(
                bot_schema=bot_schema,
                bot_display_name=display_name,
                icon_base64=DEFAULT_ICON_BASE64,
            ),
        )
        gpt_schema = f"{bot_schema}.gpt.default"
        if is_orchestrator:
            # The connected-agent root needs the channels + isLightweightBot config
            # or its post-publish provisioning fails with a 409 ExternalServiceException.
            poi = '\n  "publishOnImport": true,' if self.spec.orchestrator_publish_on_import else ""
            channels = ORCHESTRATOR_CHANNELS_BLOCK if self.spec.orchestrator_channels else ""
            config_json = ORCHESTRATOR_CONFIGURATION_JSON.format(
                gpt_schema=gpt_schema, publish_on_import_line=poi, channels_block=channels
            )
        else:
            config_json = BOT_CONFIGURATION_JSON_NATIVE.format(gpt_schema=gpt_schema)
        zf.writestr(f"bots/{bot_schema}/configuration.json", config_json)

        # gpt.default component (instructions)
        gpt_folder = f"botcomponents/{gpt_schema}"
        zf.writestr(
            f"{gpt_folder}/botcomponent.xml",
            GPT_BOTCOMPONENT_XML.format(
                schema_name=gpt_schema,
                display_name=display_name,
                bot_schema=bot_schema,
            ),
        )
        instr = instructions or f"You are {display_name}. Help the user with their request."
        zf.writestr(
            f"{gpt_folder}/data",
            GPT_DATA_YAML.format(
                display_name=display_name,
                instructions_indented=_indent(instr, 2),
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{gpt_folder}/data"))

        # system topics (one set per bot)
        for topic_key, topic_data in SYSTEM_TOPICS.items():
            schema_name = f"{bot_schema}.topic.{topic_key}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(bot_schema, topic_key, topic_data),
            )
            zf.writestr(
                f"{folder}/data",
                topic_data["data"].format(bot_schema=bot_schema),
            )
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

        # custom per-capability topic: the REAL deterministic behavior, INSIDE
        # this sub-agent (1:1 with the converted agent.py's CapIR steps). The
        # orchestrator stays a pure router and never carries one.
        if capir and not is_orchestrator:
            action = capir_topic_action_name(capir)
            # keep "{bot_schema}.topic.{action}" within the 100-char schema limit
            action = action[: max(4, MAX_SCHEMA - len(bot_schema) - len(".topic."))]
            schema_name = f"{bot_schema}.topic.{action}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(
                    bot_schema, action,
                    {"display_name": _xml_escape(display_name),
                     "description": f"Deterministic handler for {display_name} "
                                    "(seeded records + the real user query, 1:1 with the agent.py)."}),
            )
            zf.writestr(f"{folder}/data", capir_topic_data_yaml(display_name, capir))
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    def _write_connected_action(
        self,
        zf: zipfile.ZipFile,
        sub: SubAgentSpec,
        child_schema: str,
        action: str,
        overrides: List[str],
    ) -> None:
        """Write the orchestrator's delegation component for one sub-agent."""
        schema_name = f"{self.orch_schema}.InvokeConnectedAgentTaskAction.{action}"
        folder = f"botcomponents/{schema_name}"
        description = sub.description or f"Delegate to {sub.display_name}."

        zf.writestr(
            f"{folder}/botcomponent.xml",
            INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML.format(
                schema_name=schema_name,
                description=_xml_escape(description),
                display_name=_xml_escape(sub.display_name),
                orchestrator_schema=self.orch_schema,
            ),
        )
        zf.writestr(
            f"{folder}/dependencies.json",
            INVOKE_CONNECTED_AGENT_DEPENDENCIES.format(child_schema=child_schema),
        )
        inputs_block, input_type_block = _connected_inputs_yaml(getattr(sub, "params", None))
        zf.writestr(
            f"{folder}/data",
            INVOKE_CONNECTED_AGENT_DATA.format(
                display_name=_yaml_display_safe(sub.display_name),
                description_indented=_indent(description, 2),
                child_schema=child_schema,
                inputs_block=inputs_block,
                input_type_block=input_type_block,
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    # -- xml helpers -----------------------------------------------------

    def _topic_botcomponent_xml(self, bot_schema, topic_key, topic_data) -> str:
        schema_name = f"{bot_schema}.topic.{topic_key}"
        desc = topic_data.get("description")
        desc_element = ""
        if desc:
            desc_element = f"\n  <description>{_xml_escape(desc)}</description>"
        return BOTCOMPONENT_XML.format(
            schema_name=schema_name,
            component_type=9,
            display_name=topic_data["display_name"],
            bot_schema=bot_schema,
            description_element=desc_element,
        )

    def _solution_xml(self) -> str:
        return SOLUTION_XML_NATIVE.format(
            solution_unique_name=self.spec.solution_unique_name,
            solution_display_name=self.spec.solution_display_name,
            publisher_unique_name=self.spec.publisher_unique_name,
            publisher_display_name=self.spec.publisher_display_name,
            publisher_prefix=self.spec.publisher_prefix,
            solution_version=self.spec.solution_version,
            managed_flag="1" if self.spec.managed else "0",
        )

    # -- orchestrator instructions --------------------------------------

    def _orchestrator_instructions(self) -> str:
        if self.spec.orchestrator_instructions:
            return self.spec.orchestrator_instructions
        lines = [
            f"You are {self.spec.orchestrator_display_name}, the orchestrator for the "
            f"{self.spec.solution_display_name} workflow. You route each user request to the "
            "right connected sub-agent and never answer specialized questions yourself.",
            "",
            "Connected sub-agents you can delegate to:",
        ]
        for sub, _schema, _action in self._children:
            one_line = re.sub(r"\s+", " ", (sub.description or sub.display_name)).strip()
            lines.append(f"- {sub.display_name}: {one_line}")
        lines += [
            "",
            "Routing rules:",
            "- Read the user's request, pick the single best-matching sub-agent from the list, and delegate to it.",
            "- Pass each sub-agent only the inputs it needs; do not paraphrase or pre-answer its work.",
            "- If the request spans several sub-agents, handle one sub-agent per turn and confirm before moving on.",
            "- If no sub-agent fits, say so and ask a clarifying question rather than inventing an answer.",
        ]
        return "\n".join(lines)


def generate_connected_solution(
    spec: ConnectedSolutionSpec,
    output_path: Optional[Path] = None,
) -> bytes:
    """Build a connected (multi-bot) solution zip from a ConnectedSolutionSpec."""
    return ConnectedSolutionPackager(spec).package(output_path=output_path)


# ============================================================================
# Build sub-agents from an agent stack (agents/*.py + metadata.json) and validate
# ============================================================================

def _humanize(name: str) -> str:
    name = re.sub(r"_stacks$", "", name or "")
    name = name.replace("_", " ").replace("-", " ").strip()
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _humanize_class(name: str) -> str:
    name = re.sub(r"Agent$", "", name or "")
    name = re.sub(r"_agent$", "", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = name.replace("_", " ").strip()
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _safe_literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


# Class-body literals a converted agent.py embeds. CAPIR is the compiled CapIR
# (perform()'s spec); SYNTHETIC_DATA holds the seeded records (the build keeps
# them OUT of the CapIR binding, so we re-inject them); the rest let us recompile
# a CapIR when one was not embedded.
_RECOVERED_ATTRS = {"CAPIR", "SYNTHETIC_DATA", "KNOWLEDGE", "RESPONSE",
                    "DOC_NAME", "CUSTOMER", "TRIGGERS"}


def _parse_basic_agent(py_path: Path):
    """AST-extract (display_name, agent_name, description, module_doc, params,
    recovered) from a BasicAgent .py — `recovered` carries any embedded CapIR /
    seeded records used to build the deterministic capability topic."""
    src = py_path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    module_doc = (ast.get_docstring(tree) or "").strip()

    cls = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and any(
            isinstance(b, ast.Name) and b.id == "BasicAgent" for b in node.bases
        ):
            cls = node
            break
    if cls is None:
        return None

    self_name = None
    description = ""
    params = []  # (name, description, required)
    recovered = {}  # class-level CAPIR / SYNTHETIC_DATA / ... for deterministic topics
    for sub in ast.walk(cls):
        if not isinstance(sub, ast.Assign):
            continue
        for tgt in sub.targets:
            # class-body literals the build stage embeds (CAPIR = {...},
            # SYNTHETIC_DATA = [...], KNOWLEDGE / RESPONSE / DOC_NAME / CUSTOMER / TRIGGERS)
            if isinstance(tgt, ast.Name) and tgt.id in _RECOVERED_ATTRS:
                val = _safe_literal(sub.value)
                if val is not None:
                    recovered[tgt.id] = val
                continue
            if not (isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "self"):
                continue
            if tgt.attr == "name" and isinstance(sub.value, ast.Constant) and isinstance(sub.value.value, str):
                self_name = sub.value.value
            elif tgt.attr == "metadata" and isinstance(sub.value, ast.Dict):
                # Walk the dict node key-by-key: the metadata literal contains a
                # non-literal value ("name": self.name), so literal_eval on the
                # whole dict fails — pull the literal keys we care about directly.
                for k, v in zip(sub.value.keys, sub.value.values):
                    key = k.value if isinstance(k, ast.Constant) else None
                    if key == "description":
                        dv = _safe_literal(v)
                        if isinstance(dv, str):
                            description = dv.strip()
                    elif key == "parameters":
                        pv = _safe_literal(v)
                        if isinstance(pv, dict):
                            props = pv.get("properties") or {}
                            req = set(pv.get("required") or [])
                            for pn, pinfo in props.items():
                                pdesc = (pinfo.get("description") if isinstance(pinfo, dict) else "") or pn
                                params.append((pn, pdesc, pn in req))

    stem_name = re.sub(r"_agent$", "", py_path.stem)
    agent_name = stem_name
    display = _humanize_class(self_name or stem_name)
    if not description:
        # First paragraph of the module docstring.
        description = re.sub(r"\s+", " ", module_doc.split("\n\n")[0]).strip()
    # Statically infer the SHAPE of the data this agent works with (the dict keys
    # its perform()/helpers read & write) so we can synthesize matching static
    # stand-in records — no execution, no domain rules.
    recovered["INFERRED_FIELDS"] = _infer_record_fields(tree, exclude=[p[0] for p in params])
    return display, agent_name, description, module_doc, params, recovered


def _stack_subagent_instructions(display, description, module_doc, params) -> str:
    """The sub-agent's brain: self-documents the agent.py end-to-end — its purpose
    and its FULL input contract (what the orchestrator passes to delegate). Generic
    for ANY agent.py; no domain assumptions."""
    lines = [f"You are the {display} agent.", "", "# Purpose"]
    lines.append(module_doc.strip() if module_doc else (description or f"Handle {display} requests."))
    lines += ["", "# Inputs the orchestrator passes you"]
    if params:
        for pn, pdesc, required in params:
            tag = "required" if required else "optional"
            clean = re.sub(r"\s+", " ", pdesc).strip()
            lines.append(f"- {pn} ({tag}): {clean}")
    else:
        lines.append("- No structured inputs are required; use the user's request directly.")
    lines += ["", "# How you answer",
              "- Run your deterministic capability topic and ground every answer in its seeded records.",
              "- That seeded data is SYNTHETIC stand-in data for your real source system, so you load "
              "and run end-to-end with no live connection. Swapping the topic's Table() for the live "
              "connector takes you to production with no change to the logic.",
              "- Stay in your lane: if the request belongs to another connected agent, say so and let "
              "the orchestrator route it."]
    return "\n".join(lines)


def _contract_description(description, params, limit=850):
    """The orchestrator-facing routing description: the agent's purpose PLUS its
    input contract, so the Copilot Studio agent knows what to pass when it
    delegates. Self-documenting, generic, length-capped for the component."""
    base = re.sub(r"\s+", " ", description or "").strip()
    if params:
        ins = "; ".join("%s (%s)" % (pn, "required" if req else "optional")
                        for pn, _pd, req in params)
        base = (base + " Inputs to pass: " + ins + ".").strip()
    return base[:limit]


# t2p-capir/1.0 — the load-bearing perform() constants, mirrored so a recompiled
# CapIR carries the same numbers the agent.py uses.
_CAPIR_SCHEMA = "t2p-capir/1.0"
_RECOMPILE_CONSTS = {
    "word_min_len": 3, "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


# Envelope / structural dict keys that are NOT data columns, so schema inference
# never mistakes the result wrapper for record fields.
_ENVELOPE_KEYS = {"status", "agent", "data", "parameters", "properties",
                  "required", "type", "name", "description", "items", "enum",
                  "error", "result", "results", "success", "ok", "count", "as_of_utc"}
# Objects whose `.get("x")` calls are NOT record reads (input kwargs, env, etc.).
_SKIP_GET_OBJS = {"kwargs", "self", "metadata", "os", "sys", "environ", "params", "config"}


def _flatten_record(r):
    """Flatten one record to top-level scalar fields (the Table()/filter columns):
    a nested dict is merged up one level; lists/dicts are json-encoded to strings."""
    if not isinstance(r, dict):
        return {}
    out = {}
    for k, v in r.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                out[str(kk)] = vv if not isinstance(vv, (list, dict)) else json.dumps(vv, ensure_ascii=False)
        elif isinstance(v, list):
            out[str(k)] = json.dumps(v, ensure_ascii=False)
        else:
            out[str(k)] = v
    return out


def _infer_record_fields(tree, exclude=None, max_fields=14):
    """Infer the SHAPE of the data an agent.py works with by statically scanning
    its code for the dict keys it reads/writes: `rec.get("field")`, `rec["field"]`
    and `{"field": ...}` literals. Excludes input-param names + envelope keys so
    only genuine data columns remain. 100% static — no execution, no domain rules."""
    exclude = set(exclude or []) | _ENVELOPE_KEYS
    keys = []

    def add(k):
        if (isinstance(k, str) and k and k.isidentifier()
                and k not in exclude and k not in keys):
            keys.append(k)

    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            obj = node.func.value
            if isinstance(obj, ast.Name) and obj.id in _SKIP_GET_OBJS:
                continue
            a = node.args[0]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                add(a.value)
        elif isinstance(node, ast.Subscript):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                add(sl.value)
        elif isinstance(node, ast.Dict):
            klits = [k.value for k in node.keys
                     if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "status" in klits and "data" in klits:
                continue  # a result-envelope literal, not a data record
            for k in klits:
                add(k)
    return keys[:max_fields]


def _synthesize_value(field, i):
    """A clearly-synthetic, generic value for `field` on row i — typed by the field
    NAME's TOKENS only (token-matched, so "age" never fires inside "message"). No
    domain knowledge. Deterministic (index-based, no RNG)."""
    f = field.lower()
    toks = set(t for t in re.split(r"[^a-z0-9]+", f) if t)
    if toks & {"prob", "probability", "score", "rate", "ratio", "pct", "percent",
               "confidence", "likelihood", "fail", "risk"}:
        return round(0.15 + 0.7 * (((i - 1) % 5) / 4.0), 2)   # 0.15 .. 0.85
    if f.startswith(("is_", "has_")) or toks & {"enabled", "active", "flag", "bool"}:
        return (i % 2 == 0)
    if toks & {"date", "time", "utc", "timestamp", "datetime", "created", "updated"}:
        return "2026-01-%02dT00:00:00Z" % min(i, 28)
    if toks & {"id", "guid", "uuid", "code", "ref"}:
        return "%s-%04d" % ((re.sub(r"[^A-Za-z]", "", field).upper()[:4] or "REC"), i)
    if toks & {"count", "qty", "quantity", "amount", "price", "cost", "value", "age",
               "days", "years", "hours", "num", "number", "level", "index", "size",
               "total", "kv", "voltage", "pct"}:
        return i * 10
    return "synthetic %s %d" % (f.replace("_", " "), i)


def _synthesize_records(fields, n=5):
    """Generate n self-documenting STATIC stand-in records over `fields` — the
    synthetic data that lets the topic load and run end-to-end with no live
    connection. Generic for any field set; swap the Table() for the live connector."""
    fields = [f for f in (fields or []) if f] or ["id", "label", "detail"]
    return [{f: _synthesize_value(f, i) for f in fields} for i in range(1, n + 1)]


def _resolve_capir(recovered, display, agent_name, description, params, capir_mode):
    """Decide the CapIR a sub-agent's deterministic topic is built from — the
    topic that IS this agent.py's perform() running on STATIC stand-in data, so
    the Copilot Studio orchestrator gets the same result it would by chatting the
    brainstem and invoking the agent.py.

    Policy (capir_mode):
      off       -> never emit a topic (instructions-blob only)
      embedded  -> only when the agent.py embeds a CAPIR literal
      static    -> embedded, else recompile ONLY from real seeded data
                   (SYNTHETIC_DATA); do not synthesize a stand-in
      auto      -> (default) embedded, else recompile from SYNTHETIC_DATA, else
                   SYNTHESIZE static stand-in data from the agent's inferred data
                   shape. Maps EVERY agent.py to a self-documented topic."""
    mode = (capir_mode or "auto").lower()
    if mode in ("capture", "always", "run"):
        mode = "auto"
    if mode == "off":
        return None
    synth = recovered.get("SYNTHETIC_DATA") or []
    embedded = recovered.get("CAPIR")
    if isinstance(embedded, dict) and embedded.get("steps"):
        binding = dict(embedded.get("binding") or {})
        if not binding.get("records"):
            binding["records"] = synth
        if not binding.get("fields"):
            binding["fields"] = _capir_topic_fields(binding.get("records"))
        out = {**embedded, "binding": binding}
        out.setdefault("customer", recovered.get("CUSTOMER") or "the customer")
        return out
    if mode == "embedded":
        return None
    if mode == "static":
        return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                          params, records=synth) if synth else None
    # auto: always map — real seeded data if present, else a STATIC stand-in
    # synthesized from the agent's inferred data shape (its perform() field reads).
    records = synth
    if not records:
        fields = recovered.get("INFERRED_FIELDS") or [p[0] for p in (params or [])]
        records = _synthesize_records(fields)
    return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                      params, records=records)


def _recompile_capir_from_meta(recovered, display, agent_name, description, params, records=None):
    """Build a CapIR for an agent.py with no embedded CAPIR — mirrors T2P's
    _compile_capir shape from its records (real or synthesized), KNOWLEDGE,
    RESPONSE, DOC_NAME, TRIGGERS plus the parsed metadata. Same structure and
    perform()-parity constants as the generated path; only the source differs."""
    records = [_flatten_record(r) for r in (records if records is not None
               else (recovered.get("SYNTHETIC_DATA") or []))][:10]
    knowledge = list(recovered.get("KNOWLEDGE") or [])
    triggers = list(recovered.get("TRIGGERS") or [])
    if not triggers:
        triggers = [display] + ([re.sub(r"\s+", " ", description).strip()[:60]]
                                if description else [])
    response = recovered.get("RESPONSE") or description or f"Here is how I handle {display}."
    doc = recovered.get("DOC_NAME") or None
    key = re.sub(r"[^a-z0-9_]", "", (agent_name or display).lower().replace(" ", "_")) or "capability"
    fields = _capir_topic_fields(records)
    prompt = f"What would you like to ask the {display} agent? (a keyword, id, or value to filter on)"
    binding = {
        "connector": "table",
        "table": "rec_" + key,
        "library": display + " Library",
        "fields": fields,
        "key_field": fields[0] if fields else "id",
        "row_count": len(records),
        "records": records,
    }
    steps = [
        {"id": "trigger", "op": "trigger_match", "queries": triggers},
        {"id": "slot_query", "op": "slot_fill", "slot": "query"},
        {"id": "ground", "op": "knowledge_lookup", "facts": knowledge, "into": "Grounding"},
        {"id": "lookup", "op": "record_lookup", "source": "binding", "from": "query",
         "into": "Matches", "take": _RECOMPILE_CONSTS["example_take"],
         "fallback_take": _RECOMPILE_CONSTS["fallback_take"]},
        {"id": "respond", "op": "respond", "template_kind": "standard"},
    ]
    if doc:
        steps.append({"id": "artifact", "op": "artifact", "doc": doc,
                      "from": ["Grounding", "Matches"]})
    return {
        "schema": _CAPIR_SCHEMA,
        "key": key,
        "response": response,
        "customer": recovered.get("CUSTOMER") or "the customer",
        "binding": binding,
        "slots": [{"name": "query", "entity": "StringPrebuiltEntity",
                   "prompt": prompt, "required": True}],
        "consts": dict(_RECOMPILE_CONSTS),
        "steps": steps,
        "expect": list(triggers),
        "triggers_owned": True,
    }


def _subagents_from_stack(stack_dir: Path, capir_mode: str = "auto") -> List[SubAgentSpec]:
    agents_dir = stack_dir / "agents"
    if not agents_dir.is_dir():
        agents_dir = stack_dir
    subs: List[SubAgentSpec] = []
    for py in sorted(agents_dir.glob("*.py")):
        if py.name.startswith("_") or py.name == "basic_agent.py":
            continue
        parsed = _parse_basic_agent(py)
        if not parsed:
            logger.warning("  - %s: no BasicAgent subclass, skipping", py.name)
            continue
        display, agent_name, description, module_doc, params, recovered = parsed
        capir = _resolve_capir(recovered, display, agent_name, description, params, capir_mode)
        subs.append(SubAgentSpec(
            agent_name=agent_name,
            display_name=display,
            # description carries the input contract so the orchestrator knows what
            # to pass when it delegates (self-documented, like the agent.py).
            description=_contract_description(description, params) or f"Handle {display} requests.",
            instructions=_stack_subagent_instructions(display, description, module_doc, params),
            capir=capir,
            params=params,
        ))
        logger.info("  + %s%s", display, "  [deterministic topic]" if capir else "")
    return subs


def _load_stack_metadata(stack_dir: Path) -> dict:
    mpath = stack_dir / "metadata.json"
    if mpath.is_file():
        try:
            return json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _orchestrator_instructions_from_metadata(meta: dict, subs: List[SubAgentSpec]) -> str:
    name = meta.get("name", "the agent stack")
    desc = meta.get("description", "")
    lines = [f"You are the orchestrator for {name}.", ""]
    if desc:
        lines += [desc, ""]
    lines.append("You route each user request to the right connected sub-agent and never do their specialized work yourself.")
    features = meta.get("features") or []
    if features:
        lines += ["", "End-to-end flow this stack supports, in order:"]
        lines += [f"- {f}" for f in features]
    lines += ["", "Connected sub-agents you can delegate to:"]
    for sub in subs:
        lines.append(f"- {sub.display_name}: {sub.description}")
    starters = meta.get("starters") or []
    if starters:
        lines += ["", "Example requests you should expect:"]
        lines += [f"- {s}" for s in starters]
    lines += [
        "",
        "Routing rules:",
        "- Pick the single best-matching connected agent for the request and delegate to it; pass it the inputs named in its description.",
        "- Calling a connected agent gives you the SAME result you would get by chatting the source brainstem and letting it invoke that agent.py — each connected agent's topic runs the agent's deterministic logic on its seeded sample data.",
        "- If a request spans several connected agents, handle one per turn, show its result, then continue to the next.",
        "- If a required input is missing, ask for it. The seeded data is synthetic stand-in data; do not invent records beyond it.",
        "- If no connected agent fits, say so and ask a clarifying question.",
    ]
    return "\n".join(lines)


def validate_connected_solution(zip_path: Path) -> bool:
    """Structural checks that the connected solution is import-shaped."""
    ok = True
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = set(zf.namelist())

        for required in ("[Content_Types].xml", "solution.xml", "customizations.xml"):
            if required not in names:
                logger.error("  X missing %s", required)
                ok = False

        bots = sorted({n.split("/")[1] for n in names if n.startswith("bots/")})
        logger.info("  bots: %d (%s)", len(bots), ", ".join(bots))

        # Every connected-action must reference an existing child bot.
        actions = [n for n in names if ".InvokeConnectedAgentTaskAction." in n and n.endswith("/dependencies.json")]
        logger.info("  connected-agent actions: %d", len(actions))
        for dep in actions:
            child = json.loads(zf.read(dep).decode("utf-8"))[0]["schemaName"]
            if f"bots/{child}/bot.xml" not in names:
                logger.error("  X action %s -> missing child bot %s", dep, child)
                ok = False
            data_path = dep.rsplit("/", 1)[0] + "/data"
            if data_path in names:
                data_text = zf.read(data_path).decode("utf-8")
                if f"botSchemaName: {child}" not in data_text:
                    logger.error("  X %s data does not invoke %s", data_path, child)
                    ok = False

        # Every extensionless /data part must be declared in [Content_Types].xml.
        ct = zf.read("[Content_Types].xml").decode("utf-8")
        data_parts = [n for n in names if n.endswith("/data")]
        missing = [p for p in data_parts if f'PartName="/{p}"' not in ct]
        if missing:
            logger.error("  X %d /data parts missing from [Content_Types].xml (e.g. %s)",
                         len(missing), missing[0])
            ok = False
        else:
            logger.info("  content-types: all %d /data parts declared", len(data_parts))

        # Each bot needs gpt.default + the system-topic set.
        for bot in bots:
            if f"botcomponents/{bot}.gpt.default/data" not in names:
                logger.error("  X bot %s missing gpt.default", bot)
                ok = False

        # No botcomponent schema name may exceed the Dataverse 100-char limit.
        schemas = {n.split("/")[1] for n in names if n.startswith("botcomponents/")}
        longest = max(schemas, key=len) if schemas else ""
        if len(longest) > 100:
            logger.error("  X schema name too long (%d > 100): %s", len(longest), longest)
            ok = False
        else:
            logger.info("  schema lengths: max %d/100 (%s)", len(longest), longest)

        # Copilot Studio rejects bot display names longer than 42 chars.
        worst_name, worst_len = "", 0
        for bot in bots:
            bx = zf.read(f"bots/{bot}/bot.xml").decode("utf-8")
            m = re.search(r"<name>(.*?)</name>", bx, re.DOTALL)
            nm = (m.group(1).strip() if m else "")
            if len(nm) > worst_len:
                worst_name, worst_len = nm, len(nm)
        if worst_len > 42:
            logger.error("  X bot name too long (%d > 42): %s", worst_len, worst_name)
            ok = False
        else:
            logger.info("  bot names: max %d/42 (%s)", worst_len, worst_name)
    return ok


# ===========================================================================
# Autonomous deploy to Microsoft Copilot Studio (Dataverse Web API, stdlib only)
#
# Self-contained so this one file, dropped into any brainstem, can BOTH package a
# connected-agents solution AND import + publish it into a real Copilot Studio
# environment — no pac CLI, no third-party packages. App-registration credentials
# come ONLY from env vars or a settings file, never from chat, and the secret is
# never echoed back. Same proven path as the T2P deploy agent: service-principal
# token -> ImportSolution -> PvaPublish (children first, orchestrator last).
# ===========================================================================

_DEPLOY_AUTH = "https://login.microsoftonline.com"


def _http(url, data=None, headers=None, method=None, timeout=300):
    """Minimal stdlib HTTP: dict data -> form-encoded (OAuth), else JSON bytes."""
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    elif data is not None and not isinstance(data, (bytes, bytearray)):
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(body) if body[:1] in ("{", "[") else body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body
    except Exception as e:  # network / DNS / timeout
        return 0, str(e)


def _extract_dyn_creds(creds):
    """From a settings dict ({IsEncrypted,Values} or bare), a Values dict, or a
    JSON string -> {client_id, client_secret, tenant_id, resource} or None."""
    if isinstance(creds, str):
        try:
            creds = json.loads(creds)
        except Exception:
            return None
    if not isinstance(creds, dict):
        return None
    vals = creds.get("Values", creds)
    cid, sec = vals.get("DYNAMICS_365_CLIENT_ID"), vals.get("DYNAMICS_365_CLIENT_SECRET")
    ten, res = vals.get("DYNAMICS_365_TENANT_ID"), vals.get("DYNAMICS_365_RESOURCE")
    if not all([cid, sec, ten, res]):
        return None
    return {"client_id": cid, "client_secret": sec, "tenant_id": ten, "resource": str(res).rstrip("/")}


def _deploy_creds(kwargs):
    """Resolve app-registration creds for deploy — env / settings file ONLY, never
    from chat. Returns (creds_dict, source_label) or (None, None)."""
    candidates = [
        os.path.expanduser(kwargs["credentials_path"]) if kwargs.get("credentials_path") else None,
        os.environ.get("RAPP_DEPLOY_SETTINGS"),
        os.path.expanduser("~/.rapp_deploy_settings.json"),
        "local.settings.json",
    ]
    for cand in candidates:
        if cand and os.path.isfile(cand):
            try:
                c = _extract_dyn_creds(json.load(open(cand)))
                if c:
                    return c, cand
            except Exception:
                pass
    c = _extract_dyn_creds({"Values": dict(os.environ)})
    if c:
        return c, "process env"
    return None, None


def _sp_token(client_id, secret, tenant, resource):
    """Service-principal (client-credentials) token for the Dataverse env."""
    code, t = _http(f"{_DEPLOY_AUTH}/{tenant}/oauth2/v2.0/token",
                    data={"grant_type": "client_credentials", "client_id": client_id,
                          "client_secret": secret, "scope": resource.rstrip("/") + "/.default"},
                    headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200 or not isinstance(t, dict) or "access_token" not in t:
        raise RuntimeError("service-principal auth failed: " + str(t)[:200])
    return t["access_token"]


def _dataverse_action(resource, token, action, body=None, method="POST"):
    data = json.dumps(body).encode() if body is not None else None
    return _http(resource.rstrip("/") + "/api/data/v9.2/" + action, data=data, method=method,
                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                          "Accept": "application/json", "OData-MaxVersion": "4.0",
                          "OData-Version": "4.0"})


def _import_solution(resource, token, zip_bytes):
    """ImportSolution (unmanaged, overwrite) then PublishAllXml."""
    code, r = _dataverse_action(resource, token, "ImportSolution", {
        "OverwriteUnmanagedCustomizations": True, "PublishWorkflows": True,
        "ImportJobId": str(uuid.uuid4()),
        "CustomizationFile": base64.b64encode(zip_bytes).decode()})
    if code not in (200, 204):
        raise RuntimeError("ImportSolution failed (%s): %s" % (code, str(r)[:400]))
    _dataverse_action(resource, token, "PublishAllXml")


def _find_botid(resource, token, schema):
    qs = urllib.parse.urlencode({"$select": "botid,schemaname",
                                 "$filter": "schemaname eq '%s'" % schema,
                                 "$orderby": "createdon desc", "$top": "1"})
    code, r = _http(resource.rstrip("/") + "/api/data/v9.2/bots?" + qs,
                    headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    rows = (r.get("value") if isinstance(r, dict) else None) or []
    return rows[0]["botid"] if rows else None


def _publish_botid(botid, resource, token):
    """Publish ONE bot via the Dataverse PvaPublish Web API action. PURE HTTPS —
    no pac/CLI/subprocess — so this agent.py runs identically in a local brainstem
    AND inside an Azure-Function-hosted brainstem (no binary to ship)."""
    code, r = _dataverse_action(resource, token,
                                "bots(%s)/Microsoft.Dynamics.CRM.PvaPublish" % botid, {})
    if code in (200, 204):
        return {"bot_id": botid, "status": "publish_requested", "via": "PvaPublish"}
    return {"bot_id": botid, "status": "publish_failed", "via": "PvaPublish", "error": str(r)[:160]}


def _publish_connected(bot_schemas, resource, token):
    """Publish every bot — CHILDREN first, ORCHESTRATOR last (a connected-agent
    root cannot publish until its invoked sub-agents are published)."""
    if not bot_schemas:
        return []
    orch = bot_schemas[0]
    order = list(bot_schemas[1:]) + [orch]
    out = []
    for schema in order:
        botid = _find_botid(resource, token, schema)
        if not botid:
            out.append({"schema": schema, "status": "not_found"})
            continue
        out.append({"schema": schema, **_publish_botid(botid, resource, token)})
    return out


def _run_deploy(zip_bytes, bot_schemas, orch_display, kwargs):
    """Import + (optionally) publish the connected solution into Copilot Studio.
    Returns a result dict with a human `summary`; never includes the secret."""
    creds, src = _deploy_creds(kwargs)
    if creds and kwargs.get("environment_url"):
        creds = {**creds, "resource": str(kwargs["environment_url"]).rstrip("/")}
    if not creds:
        return {"status": "creds_missing",
                "summary": "NOT deployed — no app-registration credentials found.",
                "how_to": ("Set env DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / "
                           "DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE, or pass "
                           "credentials_path=<local.settings.json>, or place "
                           "~/.rapp_deploy_settings.json. Secrets never travel through chat.")}
    publish = bool(kwargs.get("publish", True))
    try:
        token = _sp_token(creds["client_id"], creds["client_secret"],
                          creds["tenant_id"], creds["resource"])
    except Exception as e:
        return {"status": "auth_failed", "summary": "NOT deployed — service-principal auth failed.",
                "error": str(e)[:300], "creds_source": src, "environment": creds["resource"]}
    try:
        _import_solution(creds["resource"], token, zip_bytes)
    except Exception as e:
        return {"status": "import_failed", "summary": "Import FAILED.", "error": str(e)[:400],
                "environment": creds["resource"], "creds_source": src}
    published = _publish_connected(bot_schemas, creds["resource"], token) if publish else []
    npub = sum(1 for p in published if p.get("status") in ("published", "publish_requested"))
    summary = ("Imported into " + creds["resource"] + " and "
               + (("published %d/%d bots. " % (npub, len(published))) if publish else "skipped publish. ")
               + "Open Copilot Studio, select that environment, open '"
               + orch_display[:42] + "' and use the Test pane.")
    return {"status": "deployed", "summary": summary, "environment": creds["resource"],
            "orchestrator": orch_display[:42], "publish_enabled": publish,
            "published": published, "creds_source": src,
            "test_in_studio": "https://copilotstudio.microsoft.com"}


# ---------------------------------------------------------------------------
# RAPP agent wrapper
# ---------------------------------------------------------------------------

class ConnectedSolutionAgent(BasicAgent):
    """Generate a connected-agent (orchestrator + sub-agents) Copilot Studio solution."""

    def __init__(self):
        self.name = "ConnectedSolutionAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn an agent stack (a folder of BasicAgent *.py files + optional "
                "metadata.json) or an explicit list of sub-agents into ONE import-ready "
                "Microsoft Copilot Studio connected-agent solution: an orchestrator plus "
                "one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. "
                "When an agent.py carries its compiled CapIR (t2p-capir/1.0) — or one can be "
                "recompiled from its seeded data — each sub-agent ALSO gets a REAL "
                "deterministic capability topic that runs the same steps as the agent.py's "
                "perform() (trigger -> the user's real query -> filter the seeded records -> "
                "branch -> respond, plus the document for artifact capabilities); only the "
                "data is mocked, so flipping the in-topic Table() to a live Dataverse / "
                "SharePoint connector is the one-line move to production. No code deploy. Bot "
                "names are auto-capped to 42 chars and orchestrator channels default off so it "
                "imports and publishes fully headlessly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "stack_dir": {
                        "type": "string",
                        "description": "Path to an agent stack folder. Each BasicAgent *.py under it "
                                       "(or its agents/ subfolder) becomes one connected sub-agent; "
                                       "metadata.json (name/description/features/starters) shapes the orchestrator.",
                    },
                    "subagents": {
                        "type": "array",
                        "description": "Alternative to stack_dir: explicit sub-agents, each an object with "
                                       "agent_name, display_name, description, instructions.",
                    },
                    "solution_name": {
                        "type": "string",
                        "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
                    },
                    "solution_display_name": {"type": "string", "description": "Solution friendly name."},
                    "orchestrator_name": {
                        "type": "string",
                        "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
                    },
                    "orchestrator_channels": {
                        "type": "boolean",
                        "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false "
                                       "(headlessly publishable). True requires a maker-portal publish.",
                    },
                    "capir_mode": {
                        "type": "string",
                        "description": "How to build the deterministic per-capability topic inside each "
                                       "sub-agent (the topic that runs the agent.py's perform() logic on STATIC "
                                       "synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else "
                                       "real seeded data, else SYNTHESIZES static stand-in records from the "
                                       "agent's inferred data shape — so EVERY agent.py maps to a self-documented "
                                       "topic; 'static' uses only real seeded data (no synthetic stand-in); "
                                       "'embedded' uses only an embedded CapIR; 'off' emits instructions-only "
                                       "sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
                    },
                    "version": {"type": "string", "description": "Solution version, e.g. 1.0.0.0."},
                    "output_path": {
                        "type": "string",
                        "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
                    },
                    "deploy": {
                        "type": "boolean",
                        "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot "
                                       "Studio (Dataverse) environment and publish every bot (sub-agents first, "
                                       "orchestrator last) — no pac CLI needed, stdlib only. App-registration "
                                       "credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) "
                                       "or a settings file — NEVER from chat. Default false (package only).",
                    },
                    "publish": {
                        "type": "boolean",
                        "description": "When deploy=true, also publish the bots after import (default true). "
                                       "false imports without publishing.",
                    },
                    "credentials_path": {
                        "type": "string",
                        "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE "
                                       "(under a top-level 'Values' object or at the root). Used only for deploy; "
                                       "the secret is never echoed back. If omitted, env vars / "
                                       "~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Optional override for the target Dataverse environment URL (e.g. "
                                       "https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, "
                                       "default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a "
                                       "distinct solution instead of updating ones that already exist.",
                    },
                    "publisher_name": {
                        "type": "string",
                        "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh "
                                       "publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
                    },
                    "publisher_display": {
                        "type": "string",
                        "description": "Solution publisher friendly name (default 'Default Publisher').",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        stack_dir = kwargs.get("stack_dir")
        subagents_in = kwargs.get("subagents")
        if not stack_dir and not subagents_in:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide 'stack_dir' (a folder of BasicAgent *.py + optional metadata.json) "
                           "or 'subagents' (a list of {agent_name, display_name, description, instructions}).",
            }

        meta: Dict[str, Any] = {}
        if stack_dir:
            sd = Path(stack_dir)
            if not sd.exists():
                return {"status": "error", "agent": self.name, "message": f"stack_dir not found: {sd}"}
            subs = _subagents_from_stack(sd, capir_mode=str(kwargs.get("capir_mode") or "auto"))
            meta = _load_stack_metadata(sd)
            fallback = _humanize(sd.name)
        else:
            subs = []
            for s in subagents_in:
                dn = s.get("display_name") or s.get("agent_name") or "Agent"
                subs.append(SubAgentSpec(
                    agent_name=s.get("agent_name") or dn,
                    display_name=dn,
                    description=(s.get("description") or "").strip() or f"Handle {dn} requests.",
                    instructions=s.get("instructions") or "",
                    capir=s.get("capir") if isinstance(s.get("capir"), dict) else None,
                ))
            fallback = kwargs.get("solution_name") or "Connected Agents"

        if not subs:
            return {"status": "error", "agent": self.name, "message": "No sub-agents found to bundle."}

        short = re.sub(r"\b(Agent\s+Stack|Agent|Stack)\b", "", meta.get("name", "")).strip()
        unique = re.sub(r"[^A-Za-z0-9]", "",
                        kwargs.get("solution_name") or meta.get("id", "") or fallback.replace(" ", ""))
        display = kwargs.get("solution_display_name") or meta.get("name") or f"{fallback} Agents"
        orch_name = kwargs.get("orchestrator_name") or f"{short or fallback} Orchestrator"
        orch_instructions = _orchestrator_instructions_from_metadata(meta, subs) if meta else ""

        spec = ConnectedSolutionSpec(
            solution_unique_name=unique or "ConnectedAgents",
            solution_display_name=display,
            orchestrator_display_name=orch_name,
            subagents=subs,
            orchestrator_instructions=orch_instructions,
            orchestrator_channels=bool(kwargs.get("orchestrator_channels", False)),
            solution_version=kwargs.get("version", "1.0.0.0"),
            # publisher controls — a fresh publisher_prefix mints brand-new bot
            # schema names (an isolated, clearly-distinct solution), instead of
            # updating bots that already exist under the default 'rapp' prefix.
            publisher_prefix=re.sub(r"[^a-z0-9]", "", str(kwargs.get("publisher_prefix") or _DEFAULT_PUBLISHER_PREFIX).lower())[:8] or _DEFAULT_PUBLISHER_PREFIX,
            publisher_unique_name=kwargs.get("publisher_name") or "DefaultPublisher",
            publisher_display_name=kwargs.get("publisher_display") or "Default Publisher",
        )
        packager = ConnectedSolutionPackager(spec)
        out = Path(kwargs.get("output_path") or f"{spec.solution_unique_name}_connected_solution.zip")
        data = packager.package(output_path=out)
        ok = validate_connected_solution(out)

        # autonomous deploy: import into Copilot Studio + publish the bots
        # (children first, orchestrator last). Creds come ONLY from env / a
        # settings file — never from chat.
        deploy_result = _run_deploy(data, list(packager.bot_schemas), display, kwargs) \
            if kwargs.get("deploy") else None

        capir_topics = sum(1 for s in subs if getattr(s, "capir", None))
        msg = (f"Generated '{out.name}' — {len(packager.bot_schemas)} bots "
               f"(1 orchestrator + {len(subs)} connected sub-agents, "
               f"{capir_topics} with a deterministic capability topic), "
               f"{round(len(data)/1024,1)} KB. Validation: {'pass' if ok else 'fail'}.")
        if deploy_result:
            msg += " " + deploy_result.get("summary", "")

        data_block = {
            "solution_path": str(out),
            "size_kb": round(len(data) / 1024, 1),
            "orchestrator_schema": packager.orch_schema,
            "sub_agents": [s.display_name for s in subs],
            "capir_topics": capir_topics,
            "deterministic_topics": [s.display_name for s in subs if getattr(s, "capir", None)],
            "validation": "pass" if ok else "fail",
        }
        status = "success" if ok else "error"
        if deploy_result:
            data_block["deploy"] = deploy_result
            if deploy_result.get("status") not in ("deployed",):
                status = "partial"
        else:
            data_block["deploy_hint"] = ("Pass deploy=true to import + publish into your Copilot Studio "
                                         "environment automatically (creds from env DYNAMICS_365_CLIENT_ID/"
                                         "SECRET/TENANT_ID/RESOURCE or a settings file via credentials_path).")
            data_block["m365_exposure"] = ("Set orchestrator_channels=true and publish the orchestrator "
                                           "in the maker portal for M365/Teams exposure.")
        return {"status": status, "agent": self.name, "message": msg, "data": data_block}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target:
        print("usage: python connected_solution_agent.py <stack_dir> [output.zip]")
        sys.exit(1)
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    result = ConnectedSolutionAgent().perform(stack_dir=target, output_path=out_path)
    print(json.dumps(result, indent=2))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
