---
name: "rar-discreetrappers-rapp-pipeline"
description: "Unified RAPP Pipeline agent for building AI agents from discovery to deployment.\n\nRECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.\n\nAll actions:\n- AUTO: auto_process (scans inputs, processes, generates reports), generate_report\n- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary\n- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document\n- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code\n- Quality Gates: execute_quality_gate (gate: QG1-QG6)\n- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/rapp_pipeline_agent", "rar_sha256": "feb4bd1dfa316f9aaa83bea4e4c220084794d1207ebee2ba4c3d823aa6bc7b44", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_pipeline_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/rapp-pipeline:20fe30927ecc5b0a83a316260132127f82dadbdbf8ad8e1c6b3af0ad79f1edee", "kind": "skill"}, "version": "1.0.2", "author": "Bill Whalen", "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/rapp_pipeline_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_pipeline_agent.py` is
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

RAPP Agent - Unified AI Agent Production Pipeline
Purpose: Single agent for ALL RAPP Pipeline operations from discovery to deployment

This unified agent consolidates all RAPP functionality:
- AUTO-PROCESS: Drop files into Azure storage, agent automatically processes and generates reports
- Discovery: Prepare calls, process transcripts, validate discovery (QG1)
- MVP: Generate proposals, prioritize features, define scope, estimate timeline
- Code: Generate agents, metadata, tests, deployment configs, review code (QG3)
- Quality Gates: Execute QG1-QG6 validations
- Pipeline: Track progress, get guidance, recommend next steps
- REPORTS: Generate professional Microsoft-style PDF reports for any step

AUTOMATED WORKFLOW:
1. Create project folder: rapp_projects/{project_id}/
2. Drop inputs into: rapp_projects/{project_id}/inputs/
   - discovery_transcript.txt - Call transcript
   - customer_feedback.txt - Customer responses
   - code_to_review.py - Code for QG3
   - deployment_metrics.json - Metrics for QG6
3. Call auto_process with project_id
4. Reports generated in: rapp_projects/{project_id}/outputs/

Use this agent for ANY RAPP Pipeline task - it handles all 14 steps.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The RAPP operation to perform. Use 'transcript_to_agent' for fastest transcript-to-deployable-agent workflow. Use 'auto_process' for full pipeline with PDF reports.",
      "enum": [
        "transcript_to_agent",
        "auto_process",
        "generate_report",
        "prepare_discovery_call",
        "process_transcript",
        "generate_discovery_summary",
        "generate_mvp_poke",
        "prioritize_features",
        "define_scope",
        "estimate_timeline",
        "generate_full_mvp_document",
        "generate_agent_code",
        "generate_agent_metadata",
        "generate_agent_tests",
        "generate_deployment_config",
        "review_code",
        "execute_quality_gate",
        "get_step_guidance",
        "get_pipeline_status",
        "recommend_next_action",
        "get_step_checklist",
        "validate_step_completion"
      ],
      "type": "string"
    },
    "agent_description": {
      "description": "Description of agent capabilities",
      "type": "string"
    },
    "agent_name": {
      "description": "Name for generated agent (e.g., 'InventoryOptimizer')",
      "type": "string"
    },
    "agent_priority": {
      "description": "Which agent to prioritize from transcript (e.g., 'contract', 'chargeback', 'social_media')",
      "type": "string"
    },
    "constraints": {
      "description": "Timeline, budget, or technical constraints",
      "type": "object"
    },
    "customer_name": {
      "description": "Customer/company name",
      "type": "string"
    },
    "data_sources": {
      "description": "Data sources for agent integration",
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "deploy_to_storage": {
      "description": "If true, automatically upload generated agent to Azure File Storage agents/ folder (for transcript_to_agent action)",
      "type": "boolean"
    },
    "discovery_data": {
      "description": "Structured discovery data from transcript processing",
      "type": "object"
    },
    "existing_code": {
      "description": "Existing code for review or test generation",
      "type": "string"
    },
    "features": {
      "description": "List of features/capabilities",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "gate": {
      "description": "Quality gate to execute (required for execute_quality_gate action)",
      "enum": [
        "QG1",
        "QG2",
        "QG3",
        "QG4",
        "QG5",
        "QG6"
      ],
      "type": "string"
    },
    "industry": {
      "description": "Customer industry (e.g., retail, healthcare, manufacturing)",
      "type": "string"
    },
    "input_data": {
      "description": "Input data for quality gate validation or other operations",
      "type": "object"
    },
    "problem_statement": {
      "description": "Validated problem statement",
      "type": "string"
    },
    "project_data": {
      "description": "Current project progress data",
      "type": "object"
    },
    "project_id": {
      "description": "Project ID for storing results",
      "type": "string"
    },
    "project_name": {
      "description": "Project name",
      "type": "string"
    },
    "report_type": {
      "description": "Type of report to generate (for generate_report action)",
      "enum": [
        "discovery",
        "qg1",
        "qg2",
        "qg3",
        "qg4",
        "qg5",
        "qg6",
        "mvp",
        "code",
        "deployment",
        "demo",
        "executive_summary",
        "full_pipeline"
      ],
      "type": "string"
    },
    "step": {
      "description": "Pipeline step number (1-14) for guidance/checklist/validation actions",
      "maximum": 14,
      "minimum": 1,
      "type": "integer"
    },
    "transcript": {
      "description": "Discovery call transcript to process",
      "type": "string"
    },
    "user_guid": {
      "description": "User GUID for project data access",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_pipeline_agent.py` and embedded as the fenced Python below (sha256 feb4bd1dfa316f9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_pipeline_agent.py` first:

```bash
python3 rapp_pipeline_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_pipeline_agent.py   # or on stdin
python3 rapp_pipeline_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
RAPP Agent - Unified AI Agent Production Pipeline
Purpose: Single agent for ALL RAPP Pipeline operations from discovery to deployment

This unified agent consolidates all RAPP functionality:
- AUTO-PROCESS: Drop files into Azure storage, agent automatically processes and generates reports
- Discovery: Prepare calls, process transcripts, validate discovery (QG1)
- MVP: Generate proposals, prioritize features, define scope, estimate timeline
- Code: Generate agents, metadata, tests, deployment configs, review code (QG3)
- Quality Gates: Execute QG1-QG6 validations
- Pipeline: Track progress, get guidance, recommend next steps
- REPORTS: Generate professional Microsoft-style PDF reports for any step

AUTOMATED WORKFLOW:
1. Create project folder: rapp_projects/{project_id}/
2. Drop inputs into: rapp_projects/{project_id}/inputs/
   - discovery_transcript.txt - Call transcript
   - customer_feedback.txt - Customer responses
   - code_to_review.py - Code for QG3
   - deployment_metrics.json - Metrics for QG6
3. Call auto_process with project_id
4. Reports generated in: rapp_projects/{project_id}/outputs/

Use this agent for ANY RAPP Pipeline task - it handles all 14 steps.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/rapp_pipeline_agent",
    "version": "1.0.2",
    "display_name": "RAPP",
    "description": "Runs the full RAPP pipeline \u2014 discovery, MVP, code gen, quality gates QG1-QG6, PDF reports \u2014 using Azure OpenAI and Azure File Storage.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

try:
    from openai import AzureOpenAI
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    AZURE_OPENAI_AVAILABLE = True
    AZURE_OPENAI_IMPORT_ERROR = None
except ImportError as e:
    AzureOpenAI = None
    DefaultAzureCredential = None
    get_bearer_token_provider = None
    AZURE_OPENAI_AVAILABLE = False
    AZURE_OPENAI_IMPORT_ERROR = str(e)

# Import report generator (optional - handles import errors gracefully)
try:
    from utils.rapp_report_generator import RAPPReportGenerator, generate_rapp_report
    REPORT_GENERATOR_AVAILABLE = True
except Exception:
    # Catches ImportError, NameError, and other module-level errors
    REPORT_GENERATOR_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_llm_json_response(response_text: str, fallback_key: str = "raw_response") -> dict:
    """Parse JSON from LLM response, handling markdown code blocks."""
    try:
        text = response_text
        if '```json' in text:
            text = text.split('```json')[-1].split('```')[0]
        elif '```' in text:
            parts = text.split('```')
            if len(parts) >= 2:
                text = parts[1]
        json_start = text.find('{')
        json_end = text.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            return json.loads(text[json_start:json_end])
        return {fallback_key: response_text}
    except json.JSONDecodeError:
        return {fallback_key: response_text}


class RAPPAgent(BasicAgent):
    """
    Unified RAPP Pipeline Agent - handles ALL pipeline operations.

    This is the ONLY agent needed for RAPP Pipeline work. Use this agent for:
    - Discovery call preparation and transcript processing
    - MVP document generation and scope definition
    - Agent code generation and review
    - Quality gate validations (QG1-QG6)
    - Pipeline orchestration and progress tracking

    DO NOT use individual RAPP agents - use this unified agent instead.
    """

    # Pipeline step definitions
    PIPELINE_STEPS = {
        1: {"name": "Discovery Call", "type": "manual"},
        2: {"name": "Transcript Analysis", "type": "audit", "gate": "QG1"},
        3: {"name": "Generate MVP Poke", "type": "manual"},
        4: {"name": "Customer Validation", "type": "audit", "gate": "QG2"},
        5: {"name": "Generate Agent Code", "type": "manual"},
        6: {"name": "Code Quality Review", "type": "audit", "gate": "QG3"},
        7: {"name": "Deploy Prototype", "type": "manual"},
        8: {"name": "Demo Review", "type": "audit", "gate": "QG4"},
        9: {"name": "Generate Video Demo", "type": "manual"},
        10: {"name": "Final Demo Review", "type": "audit", "gate": "QG5"},
        11: {"name": "Iteration Loop", "type": "manual"},
        12: {"name": "Production Deployment", "type": "manual"},
        13: {"name": "Post-Deployment Audit", "type": "audit", "gate": "QG6"},
        14: {"name": "Scale & Maintain", "type": "manual"}
    }

    # Quality gate configurations
    GATE_CONFIGS = {
        "QG1": {"name": "Transcript Validation", "step": 2, "decisions": ["PASS", "CLARIFY", "FAIL"]},
        "QG2": {"name": "Customer Validation", "step": 4, "decisions": ["PROCEED", "REVISE", "HOLD"]},
        "QG3": {"name": "Code Quality Review", "step": 6, "decisions": ["PASS", "FIX_REQUIRED", "FAIL"]},
        "QG4": {"name": "Demo Review", "step": 8, "decisions": ["PASS", "POLISH", "FAIL"]},
        "QG5": {"name": "Final Demo Review", "step": 10, "decisions": ["APPROVE", "MINOR_REVISIONS", "MAJOR_REVISIONS", "REJECT"]},
        "QG6": {"name": "Post-Deployment Audit", "step": 13, "decisions": ["GREEN", "YELLOW", "RED"]}
    }

    # Input file patterns for auto-detection
    INPUT_PATTERNS = {
        "discovery_transcript": ["transcript", "discovery", "call_notes", "meeting_notes"],
        "customer_feedback": ["feedback", "customer_response", "validation", "approval"],
        "code_to_review": [".py"],
        "requirements": ["requirements", "mvp_requirements", "features"],
        "demo_notes": ["demo", "presentation", "video_script"],
        "deployment_metrics": ["metrics", "telemetry", "usage", "health"],
    }

    # Report types for each step
    STEP_REPORTS = {
        1: "discovery",
        2: "qg1",
        3: "mvp",
        4: "qg2",
        5: "code",
        6: "qg3",
        7: "deployment",
        8: "qg4",
        9: "demo",
        10: "qg5",
        11: "iteration",
        12: "production",
        13: "qg6",
        14: "maintenance"
    }

    def __init__(self):
        self.name = 'RAPP'
        self.metadata = {
            "name": self.name,
            "description": """Unified RAPP Pipeline agent for building AI agents from discovery to deployment.

RECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.

All actions:
- AUTO: auto_process (scans inputs, processes, generates reports), generate_report
- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary
- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document
- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code
- Quality Gates: execute_quality_gate (gate: QG1-QG6)
- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "The RAPP operation to perform. Use 'transcript_to_agent' for fastest transcript-to-deployable-agent workflow. Use 'auto_process' for full pipeline with PDF reports.",
                        "enum": [
                            "transcript_to_agent",
                            "auto_process",
                            "generate_report",
                            "prepare_discovery_call",
                            "process_transcript",
                            "generate_discovery_summary",
                            "generate_mvp_poke",
                            "prioritize_features",
                            "define_scope",
                            "estimate_timeline",
                            "generate_full_mvp_document",
                            "generate_agent_code",
                            "generate_agent_metadata",
                            "generate_agent_tests",
                            "generate_deployment_config",
                            "review_code",
                            "execute_quality_gate",
                            "get_step_guidance",
                            "get_pipeline_status",
                            "recommend_next_action",
                            "get_step_checklist",
                            "validate_step_completion"
                        ]
                    },
                    "report_type": {
                        "type": "string",
                        "description": "Type of report to generate (for generate_report action)",
                        "enum": ["discovery", "qg1", "qg2", "qg3", "qg4", "qg5", "qg6", "mvp", "code", "deployment", "demo", "executive_summary", "full_pipeline"]
                    },
                    "gate": {
                        "type": "string",
                        "description": "Quality gate to execute (required for execute_quality_gate action)",
                        "enum": ["QG1", "QG2", "QG3", "QG4", "QG5", "QG6"]
                    },
                    "step": {
                        "type": "integer",
                        "description": "Pipeline step number (1-14) for guidance/checklist/validation actions",
                        "minimum": 1,
                        "maximum": 14
                    },
                    "customer_name": {
                        "type": "string",
                        "description": "Customer/company name"
                    },
                    "project_name": {
                        "type": "string",
                        "description": "Project name"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Customer industry (e.g., retail, healthcare, manufacturing)"
                    },
                    "transcript": {
                        "type": "string",
                        "description": "Discovery call transcript to process"
                    },
                    "problem_statement": {
                        "type": "string",
                        "description": "Validated problem statement"
                    },
                    "discovery_data": {
                        "type": "object",
                        "description": "Structured discovery data from transcript processing"
                    },
                    "input_data": {
                        "type": "object",
                        "description": "Input data for quality gate validation or other operations"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name for generated agent (e.g., 'InventoryOptimizer')"
                    },
                    "agent_description": {
                        "type": "string",
                        "description": "Description of agent capabilities"
                    },
                    "features": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of features/capabilities"
                    },
                    "data_sources": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Data sources for agent integration"
                    },
                    "existing_code": {
                        "type": "string",
                        "description": "Existing code for review or test generation"
                    },
                    "constraints": {
                        "type": "object",
                        "description": "Timeline, budget, or technical constraints"
                    },
                    "project_data": {
                        "type": "object",
                        "description": "Current project progress data"
                    },
                    "project_id": {
                        "type": "string",
                        "description": "Project ID for storing results"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User GUID for project data access"
                    },
                    "deploy_to_storage": {
                        "type": "boolean",
                        "description": "If true, automatically upload generated agent to Azure File Storage agents/ folder (for transcript_to_agent action)"
                    },
                    "agent_priority": {
                        "type": "string",
                        "description": "Which agent to prioritize from transcript (e.g., 'contract', 'chargeback', 'social_media')"
                    }
                },
                "required": ["action"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def _get_openai_client(self):
        """Initialize Azure OpenAI client with Entra ID authentication."""
        if not AZURE_OPENAI_AVAILABLE:
            raise RuntimeError(
                "Azure OpenAI support is unavailable. Install openai and "
                f"azure-identity ({AZURE_OPENAI_IMPORT_ERROR})."
            )
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://cognitiveservices.azure.com/.default"
        )
        return AzureOpenAI(
            azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT'),
            azure_ad_token_provider=token_provider,
            api_version=os.environ.get('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
        )

    def perform(self, **kwargs):
        """Execute RAPP Pipeline operations."""
        action = kwargs.get('action')
        if not action:
            return json.dumps({"status": "error", "error": "Action is required"})

        try:
            # FAST-PATH: Transcript to agent in one step
            if action == 'transcript_to_agent':
                return self._transcript_to_agent(kwargs)

            # AUTO-PROCESS actions (recommended entry points)
            elif action == 'auto_process':
                return self._auto_process(kwargs)
            elif action == 'generate_report':
                return self._generate_report(kwargs)

            # Discovery actions
            elif action == 'prepare_discovery_call':
                return self._prepare_discovery_call(kwargs)
            elif action == 'process_transcript':
                return self._process_transcript(kwargs)
            elif action == 'generate_discovery_summary':
                return self._generate_discovery_summary(kwargs)

            # MVP actions
            elif action == 'generate_mvp_poke':
                return self._generate_mvp_poke(kwargs)
            elif action == 'prioritize_features':
                return self._prioritize_features(kwargs)
            elif action == 'define_scope':
                return self._define_scope(kwargs)
            elif action == 'estimate_timeline':
                return self._estimate_timeline(kwargs)
            elif action == 'generate_full_mvp_document':
                return self._generate_full_mvp_document(kwargs)

            # Code actions
            elif action == 'generate_agent_code':
                return self._generate_agent_code(kwargs)
            elif action == 'generate_agent_metadata':
                return self._generate_agent_metadata(kwargs)
            elif action == 'generate_agent_tests':
                return self._generate_agent_tests(kwargs)
            elif action == 'generate_deployment_config':
                return self._generate_deployment_config(kwargs)
            elif action == 'review_code':
                return self._review_code(kwargs)

            # Quality gate actions
            elif action == 'execute_quality_gate':
                return self._execute_quality_gate(kwargs)

            # Pipeline orchestration actions
            elif action == 'get_step_guidance':
                return self._get_step_guidance(kwargs)
            elif action == 'get_pipeline_status':
                return self._get_pipeline_status(kwargs)
            elif action == 'recommend_next_action':
                return self._recommend_next_action(kwargs)
            elif action == 'get_step_checklist':
                return self._get_step_checklist(kwargs)
            elif action == 'validate_step_completion':
                return self._validate_step_completion(kwargs)

            else:
                return json.dumps({"status": "error", "error": f"Unknown action: {action}"})

        except Exception as e:
            logger.error(f"Error in RAPP agent: {str(e)}", exc_info=True)
            return json.dumps({"status": "error", "error": str(e), "agent": self.name})

    # =========================================================================
    # DISCOVERY METHODS
    # =========================================================================

    def _prepare_discovery_call(self, kwargs):
        """Generate discovery call preparation guide and questions."""
        customer_name = kwargs.get('customer_name', 'Customer')
        industry = kwargs.get('industry', 'technology')
        existing_context = kwargs.get('discovery_data', {})

        client = self._get_openai_client()
        prompt = f"""You are a discovery call facilitator for an AI agent development project.

CUSTOMER CONTEXT:
- Company: {customer_name}
- Industry: {industry}
{f"- Existing Notes: {json.dumps(existing_context)}" if existing_context else ""}

Generate a comprehensive discovery call preparation guide including:

1. RESEARCH CHECKLIST (before the call)
- Industry-specific pain points to investigate
- Common AI use cases in this industry
- Competitor analysis points

2. DISCOVERY QUESTIONS (prioritized)
- Opening rapport-building questions
- Problem identification questions
- Data source exploration questions
- Stakeholder mapping questions
- Success criteria questions
- Timeline and budget questions

3. RED FLAGS TO WATCH FOR
- Signs the project may not be a good fit
- Scope creep indicators
- Unrealistic expectations

4. IDEAL OUTCOMES
- What a successful discovery call produces
- Key artifacts to capture

Format as a structured guide that can be used during the call."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "prepare_discovery_call",
            "customer_name": customer_name,
            "industry": industry,
            "discovery_guide": response.choices[0].message.content,
            "generated_at": datetime.now().isoformat()
        })

    def _process_transcript(self, kwargs):
        """Process discovery call transcript and extract structured data."""
        customer_name = kwargs.get('customer_name', 'Customer')
        transcript = kwargs.get('transcript', '')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        if not transcript:
            return json.dumps({"status": "error", "error": "Transcript is required"})

        client = self._get_openai_client()
        prompt = f"""Analyze this discovery call transcript and extract structured data.

CUSTOMER: {customer_name}

TRANSCRIPT:
{transcript}

Extract the following in JSON format:

{{
  "callMetadata": {{
    "estimatedDuration": "estimated based on content",
    "participants": [{{"name": "", "role": "", "company": ""}}]
  }},
  "businessContext": {{
    "industry": "",
    "companySize": "small/medium/large/enterprise",
    "currentSystems": [],
    "technicalMaturity": "low/medium/high"
  }},
  "problemStatements": [
    {{
      "problem": "clear problem description",
      "verbatimQuote": "exact quote from customer if available",
      "category": "EFFICIENCY|ACCURACY|COST|COMPLIANCE|GROWTH",
      "severity": "LOW|MEDIUM|HIGH|CRITICAL",
      "currentProcess": "how they handle this today",
      "businessImpact": "quantified if possible"
    }}
  ],
  "dataSources": [
    {{
      "systemName": "",
      "dataType": "API|Database|File|Manual|SaaS",
      "accessLevel": "Full|Partial|Unknown|Blocked",
      "dataVolume": "estimated volume",
      "integrationComplexity": "LOW|MEDIUM|HIGH"
    }}
  ],
  "stakeholders": [
    {{
      "name": "",
      "role": "",
      "influenceLevel": "DECISION_MAKER|INFLUENCER|USER|TECHNICAL|BLOCKER",
      "concerns": [],
      "enthusiasm": "LOW|MEDIUM|HIGH"
    }}
  ],
  "successCriteria": [
    {{"metric": "", "currentValue": "", "targetValue": "", "measurementMethod": ""}}
  ],
  "timeline": {{
    "urgency": "LOW|MEDIUM|HIGH|CRITICAL",
    "targetLaunchDate": "",
    "budgetCycle": "",
    "keyMilestones": []
  }},
  "suggestedAgents": ["list of AI agent types that could address the problems"],
  "riskFactors": [{{"risk": "", "likelihood": "LOW|MEDIUM|HIGH", "mitigation": ""}}],
  "nextSteps": []
}}

Also provide:
1. A 3-paragraph executive summary
2. Recommended MVP scope
3. Confidence score (1-10) for data completeness"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content
        extracted_data = parse_llm_json_response(result, "raw_analysis")

        # Store discovery data if project_id provided
        stored = False
        if project_id:
            stored = self._store_discovery_data(project_id, extracted_data, user_guid)

        return json.dumps({
            "status": "success",
            "action": "process_transcript",
            "customer_name": customer_name,
            "extracted_data": extracted_data,
            "full_analysis": result,
            "stored_for_qg1": stored,
            "project_id": project_id,
            "processed_at": datetime.now().isoformat()
        })

    def _store_discovery_data(self, project_id: str, discovery_data: dict, user_guid: str = "default"):
        """Store discovery data to project storage."""
        try:
            directory = f"project_tracker/{user_guid}"
            self.storage_manager.write_file(
                directory,
                f"discovery_{project_id}.json",
                json.dumps(discovery_data, indent=2)
            )
            return True
        except Exception as e:
            logger.warning(f"Could not store discovery data: {e}")
            return False

    def _generate_discovery_summary(self, kwargs):
        """Generate executive summary from discovery data."""
        customer_name = kwargs.get('customer_name', 'Customer')
        discovery_data = kwargs.get('discovery_data', {})

        client = self._get_openai_client()
        prompt = f"""Generate a concise executive summary for this AI agent project.

CUSTOMER: {customer_name}
DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create:
1. ONE-PARAGRAPH EXECUTIVE SUMMARY (max 100 words)
2. THREE KEY TAKEAWAYS (bullet points)
3. RECOMMENDED NEXT STEP
4. RISK ASSESSMENT (one sentence)

Format for easy reading by executives."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "generate_discovery_summary",
            "customer_name": customer_name,
            "executive_summary": response.choices[0].message.content,
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # MVP GENERATION METHODS
    # =========================================================================

    def _generate_mvp_poke(self, kwargs):
        """Generate a lightweight MVP Poke proposal."""
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        client = self._get_openai_client()
        prompt = f"""Generate a lightweight MVP "Poke" document for an AI agent project.

CUSTOMER: {customer_name}
PROJECT: {project_name}
PROBLEM: {problem_statement}

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create a concise MVP Poke with:
1. EXECUTIVE SUMMARY (2-3 sentences)
2. PROBLEM STATEMENT with Current State, Impact, Root Cause
3. PROPOSED SOLUTION with Agent Name and Core Capability
4. MVP FEATURES table (P0, P1, P2 priorities)
5. OUT OF SCOPE items (Phase 2)
6. DATA REQUIREMENTS table
7. SUCCESS METRICS table
8. TECHNICAL APPROACH (brief)
9. RISKS AND MITIGATIONS table
10. TIMELINE ESTIMATE
11. APPROVAL SECTION

Format as clean Markdown suitable for customer presentation.

Return JSON:
{{
  "status": "success",
  "document": "full markdown document",
  "features": {{"p0": [], "p1": [], "p2": []}},
  "outOfScope": [],
  "successMetrics": [{{"metric": "", "current": "", "target": ""}}],
  "estimatedDays": 0
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content
        parsed = parse_llm_json_response(result, "document")
        parsed["customer_name"] = customer_name
        parsed["project_name"] = project_name
        parsed["generated_at"] = datetime.now().isoformat()
        parsed["status"] = "success"
        parsed["action"] = "generate_mvp_poke"

        if project_id:
            self._update_project_with_mvp(project_id, parsed, user_guid)
            parsed["project_updated"] = True

        return json.dumps(parsed)

    def _update_project_with_mvp(self, project_id: str, mvp_data: dict, user_guid: str = "default"):
        """Update project with MVP document."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            project_content = self.storage_manager.read_file(directory, project_file)
            if project_content:
                project = json.loads(project_content)
                project["mvp_document"] = mvp_data
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
                return True
            return False
        except Exception as e:
            logger.warning(f"Could not update project with MVP: {e}")
            return False

    def _prioritize_features(self, kwargs):
        """Prioritize features using P0/P1/P2 method."""
        discovery_data = kwargs.get('discovery_data', {})
        features = kwargs.get('features', [])
        constraints = kwargs.get('constraints', {})

        client = self._get_openai_client()
        prompt = f"""Prioritize AI agent features for MVP development.

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

SUGGESTED FEATURES: {json.dumps(features) if features else 'Derive from discovery'}

CONSTRAINTS:
{json.dumps(constraints, indent=2) if constraints else 'None specified'}

Prioritize using P0/P1/P2 framework:
- P0: MUST have for MVP (blocks launch if missing)
- P1: SHOULD have (significant value, low risk)
- P2: COULD have (nice-to-have, defer if needed)
- DEFERRED: Phase 2 or later

Return JSON:
{{
  "features": [
    {{"name": "", "description": "", "priority": "P0|P1|P2|DEFERRED", "effort": "S|M|L", "businessValue": 0, "technicalRisk": "LOW|MEDIUM|HIGH", "rationale": ""}}
  ],
  "mvpCoreFeatures": [],
  "deferredFeatures": [],
  "totalEffort": "S|M|L|XL"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_analysis")
        parsed["status"] = "success"
        parsed["action"] = "prioritize_features"
        parsed["analyzed_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _define_scope(self, kwargs):
        """Define clear scope boundaries for MVP."""
        customer_name = kwargs.get('customer_name', 'Customer')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')

        client = self._get_openai_client()
        prompt = f"""Define clear scope boundaries for this AI agent MVP.

CUSTOMER: {customer_name}
PROBLEM: {problem_statement}
DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create explicit scope definition with:
1. IN SCOPE (What we WILL build)
2. OUT OF SCOPE (What we WON'T build in MVP)
3. ASSUMPTIONS
4. DEPENDENCIES
5. CONSTRAINTS
6. SCOPE CREEP INDICATORS

Return JSON:
{{
  "scope": {{
    "inScope": [{{"item": "", "description": "", "priority": "P0|P1|P2"}}],
    "outOfScope": [{{"item": "", "reason": "", "phase": "2|3|future"}}],
    "assumptions": [{{"category": "TECHNICAL|BUSINESS|DATA", "assumption": ""}}],
    "dependencies": [{{"type": "SYSTEM|STAKEHOLDER|DATA", "dependency": "", "risk": "LOW|MEDIUM|HIGH"}}],
    "constraints": [],
    "scopeCreepIndicators": []
  }},
  "scopeStatement": "One paragraph scope statement"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_scope")
        parsed["status"] = "success"
        parsed["action"] = "define_scope"
        parsed["customer_name"] = customer_name
        parsed["defined_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _estimate_timeline(self, kwargs):
        """Estimate MVP development timeline."""
        discovery_data = kwargs.get('discovery_data', {})
        constraints = kwargs.get('constraints', {})

        client = self._get_openai_client()
        prompt = f"""Estimate MVP development timeline for this AI agent project.

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

CONSTRAINTS:
{json.dumps(constraints, indent=2) if constraints else 'None specified'}

Provide realistic timeline with phases, milestones, and risk buffers.

Return JSON:
{{
  "timeline": {{
    "phases": [{{"name": "", "estimatedDays": 0, "dependencies": [], "deliverables": []}}],
    "totalDays": 0,
    "milestones": [{{"name": "", "targetDay": 0, "description": ""}}],
    "criticalPath": [],
    "riskBuffer": {{"days": 0, "reason": ""}}
  }},
  "confidenceLevel": "LOW|MEDIUM|HIGH"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_estimate")
        parsed["status"] = "success"
        parsed["action"] = "estimate_timeline"
        parsed["estimated_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _generate_full_mvp_document(self, kwargs):
        """Generate a complete MVP Poke document ready for customer presentation."""
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent MVP')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')

        client = self._get_openai_client()
        prompt = f"""Generate a complete, professional MVP Poke document.

CUSTOMER: {customer_name}
PROJECT: {project_name}
PROBLEM: {problem_statement}

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create a comprehensive document in clean Markdown with:
- Executive Summary
- Problem Statement (Current State, Impact, Root Cause)
- Proposed Solution (Agent Name, Core Capability, How It Works)
- MVP Features (P0/P1/P2 priority table)
- Out of Scope (Phase 2+)
- Data Requirements table
- Integration Points
- Success Metrics table
- Technical Approach
- Assumptions & Dependencies
- Risks & Mitigations table
- Timeline
- Investment & ROI
- Approval section with signature lines

End with scope lock notice."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "generate_full_mvp_document",
            "customer_name": customer_name,
            "project_name": project_name,
            "document": response.choices[0].message.content,
            "format": "markdown",
            "ready_for_customer": True,
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # CODE GENERATION METHODS
    # =========================================================================

    def _generate_agent_code(self, kwargs):
        """Generate complete Python agent code."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        agent_description = kwargs.get('agent_description', 'A custom AI agent')
        features = kwargs.get('features', [])
        data_sources = kwargs.get('data_sources', [])
        customer_name = kwargs.get('customer_name', 'Customer')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        # Create class name
        class_name = ''.join(word.capitalize() for word in agent_name.replace('-', '_').replace(' ', '_').split('_'))
        if not class_name.endswith('Agent'):
            class_name += 'Agent'
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')
        if not snake_name.endswith('_agent'):
            snake_name += '_agent'

        client = self._get_openai_client()
        prompt = f"""Generate a complete, production-ready Python agent following the BasicAgent pattern.

AGENT SPECIFICATIONS:
- Agent Name: {agent_name}
- Class Name: {class_name}
- Description: {agent_description}
- Features: {json.dumps(features)}
- Data Sources: {json.dumps(data_sources)}
- Customer: {customer_name}

REQUIREMENTS:
1. Follow the BasicAgent pattern exactly
2. Include complete JSON Schema metadata for all parameters
3. The perform() method must return JSON string (never dict or exception)
4. Wrap all external calls in try/except
5. Use logging, not print statements
6. No hardcoded credentials - use os.environ
7. Include usage example in __main__
8. Include comprehensive docstrings
9. Handle all edge cases gracefully

Generate the complete Python code."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        code = response.choices[0].message.content
        if '```python' in code:
            code_start = code.find('```python') + 9
            code_end = code.rfind('```')
            if code_end > code_start:
                code = code[code_start:code_end].strip()

        result = {
            "status": "success",
            "action": "generate_agent_code",
            "agent_name": agent_name,
            "class_name": class_name,
            "file_name": f"{snake_name}.py",
            "code": code,
            "features_implemented": features,
            "generated_at": datetime.now().isoformat()
        }

        if project_id:
            self._update_project_with_code(project_id, result, user_guid)
            result["project_updated"] = True

        return json.dumps(result)

    def _update_project_with_code(self, project_id: str, code_data: dict, user_guid: str = "default"):
        """Update project with generated code."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            project_content = self.storage_manager.read_file(directory, project_file)
            if project_content:
                project = json.loads(project_content)
                project["generated_code"] = code_data
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
                return True
            return False
        except Exception as e:
            logger.warning(f"Could not update project with code: {e}")
            return False

    def _generate_agent_metadata(self, kwargs):
        """Generate metadata schema for an agent."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        agent_description = kwargs.get('agent_description', 'A custom AI agent')
        features = kwargs.get('features', [])

        client = self._get_openai_client()
        prompt = f"""Generate a complete JSON Schema metadata definition for an AI agent.

AGENT: {agent_name}
DESCRIPTION: {agent_description}
FEATURES: {json.dumps(features)}

Create a complete metadata object with name, description, and parameters schema.

Return valid JSON:
{{
  "name": "{agent_name}",
  "description": "...",
  "parameters": {{"type": "object", "properties": {{}}, "required": []}}
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_metadata")
        return json.dumps({
            "status": "success",
            "action": "generate_agent_metadata",
            "agent_name": agent_name,
            "metadata": parsed,
            "generated_at": datetime.now().isoformat()
        })

    def _generate_agent_tests(self, kwargs):
        """Generate unit test stubs for an agent."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        existing_code = kwargs.get('existing_code', '')
        features = kwargs.get('features', [])

        class_name = ''.join(word.capitalize() for word in agent_name.replace('-', '_').replace(' ', '_').split('_'))
        if not class_name.endswith('Agent'):
            class_name += 'Agent'
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')
        if not snake_name.endswith('_agent'):
            snake_name += '_agent'

        client = self._get_openai_client()
        prompt = f"""Generate comprehensive pytest unit tests for this agent.

AGENT: {agent_name}
CLASS: {class_name}
FEATURES: {json.dumps(features)}
{f'CODE:{chr(10)}{existing_code}' if existing_code else ''}

Generate pytest-style tests covering initialization, metadata validation, perform() with valid/invalid inputs, error handling, and edge cases. Use mocking appropriately."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        test_code = response.choices[0].message.content
        if '```python' in test_code:
            code_start = test_code.find('```python') + 9
            code_end = test_code.rfind('```')
            if code_end > code_start:
                test_code = test_code[code_start:code_end].strip()

        return json.dumps({
            "status": "success",
            "action": "generate_agent_tests",
            "agent_name": agent_name,
            "test_file_name": f"test_{snake_name}.py",
            "test_code": test_code,
            "generated_at": datetime.now().isoformat()
        })

    def _generate_deployment_config(self, kwargs):
        """Generate deployment configuration."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        customer_name = kwargs.get('customer_name', 'Customer')
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')

        deployment_config = {
            "agent_name": agent_name,
            "file_name": f"{snake_name}_agent.py",
            "deployment_steps": [
                {"step": 1, "action": "Upload agent to Azure File Storage", "command": f"az storage file upload --share-name agents --source {snake_name}_agent.py"},
                {"step": 2, "action": "Verify agent loads", "command": "func start --verbose"},
                {"step": 3, "action": "Test agent endpoint", "command": f'curl -X POST http://localhost:7071/api/businessinsightbot_function -H "Content-Type: application/json" -d \'{{"user_input": "test {agent_name}"}}\''},
                {"step": 4, "action": "Deploy to Azure", "command": "func azure functionapp publish <FUNCTION_APP_NAME> --build remote"}
            ],
            "environment_variables": ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_API_VERSION"],
            "azure_file_storage_path": f"agents/{snake_name}_agent.py"
        }

        return json.dumps({
            "status": "success",
            "action": "generate_deployment_config",
            "agent_name": agent_name,
            "customer_name": customer_name,
            "deployment_config": deployment_config,
            "generated_at": datetime.now().isoformat()
        })

    def _review_code(self, kwargs):
        """Review existing code for issues."""
        existing_code = kwargs.get('existing_code', '')
        agent_name = kwargs.get('agent_name', 'Agent')

        if not existing_code:
            return json.dumps({"status": "error", "error": "No code provided for review"})

        client = self._get_openai_client()
        prompt = f"""Review this Python agent code for quality and security.

AGENT: {agent_name}
CODE:
```python
{existing_code}
```

Review for:
1. PATTERN VALIDATION - BasicAgent pattern, metadata schema, perform() returns JSON
2. SECURITY AUDIT - No hardcoded creds, input validation, injection vulnerabilities
3. LOGIC CORRECTNESS - Error handling, edge cases
4. CODE QUALITY - Naming, logging, complexity

Return JSON:
{{
  "overallScore": 0,
  "passesReview": true|false,
  "categories": {{
    "patternValidation": {{"score": 0, "passed": true|false, "issues": []}},
    "securityAudit": {{"score": 0, "passed": true|false, "issues": []}},
    "logicCorrectness": {{"score": 0, "passed": true|false, "issues": []}},
    "codeQuality": {{"score": 0, "passed": true|false, "issues": []}}
  }},
  "criticalIssues": [],
  "fixes": [{{"location": "", "issue": "", "fix": ""}}]
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_review")
        parsed["status"] = "success"
        parsed["action"] = "review_code"
        parsed["agent_name"] = agent_name
        parsed["reviewed_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    # =========================================================================
    # QUALITY GATE METHODS
    # =========================================================================

    def _execute_quality_gate(self, kwargs):
        """Execute a quality gate validation."""
        gate = kwargs.get('gate')
        if not gate:
            return json.dumps({"status": "error", "error": "Gate identifier (QG1-QG6) is required"})
        if gate not in self.GATE_CONFIGS:
            return json.dumps({"status": "error", "error": f"Invalid gate: {gate}. Use QG1-QG6."})

        input_data = kwargs.get('input_data') or kwargs.get('discovery_data', {})
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        # Retrieve discovery data from storage if needed
        if not input_data and project_id:
            input_data = self._get_discovery_data_from_storage(project_id, user_guid)

        client = self._get_openai_client()

        if gate == "QG1":
            result = self._execute_qg1(client, input_data, customer_name)
        elif gate == "QG2":
            result = self._execute_qg2(client, input_data, customer_name, project_name)
        elif gate == "QG3":
            result = self._execute_qg3(client, input_data, customer_name, project_name)
        elif gate == "QG4":
            result = self._execute_qg4(client, input_data, customer_name, project_name)
        elif gate == "QG5":
            result = self._execute_qg5(client, input_data, customer_name, project_name)
        elif gate == "QG6":
            result = self._execute_qg6(client, input_data, customer_name, project_name)

        # Store result in project
        if project_id:
            try:
                parsed_result = json.loads(result)
                self._update_project_with_qg_result(project_id, gate, parsed_result, user_guid)
            except json.JSONDecodeError:
                pass

        return result

    def _get_discovery_data_from_storage(self, project_id: str, user_guid: str) -> dict:
        """Retrieve discovery data from storage."""
        try:
            directory = f"project_tracker/{user_guid}"
            content = self.storage_manager.read_file(directory, f"discovery_{project_id}.json")
            if content:
                return json.loads(content)
            return {}
        except Exception:
            return {}

    def _update_project_with_qg_result(self, project_id: str, gate: str, qg_result: dict, user_guid: str):
        """Update project with quality gate result."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            content = self.storage_manager.read_file(directory, project_file)
            if content:
                project = json.loads(content)
                if "qg_results" not in project:
                    project["qg_results"] = {}
                project["qg_results"][gate] = qg_result
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
        except Exception as e:
            logger.warning(f"Could not update project with QG result: {e}")

    def _execute_qg1(self, client, input_data, customer_name):
        """QG1: Transcript/Discovery Validation."""
        prompt = f"""You are Quality Gate #1 (QG1) - Transcript Validation.

CUSTOMER: {customer_name}
DISCOVERY DATA:
{json.dumps(input_data, indent=2)}

Score each criterion 1-10:
1. PROBLEM CLARITY: Is the problem specific, measurable, with quantified pain points?
2. DATA AVAILABILITY: Are data sources identified with feasible access?
3. STAKEHOLDER ALIGNMENT: Clear decision-maker? Agreement on problem?
4. SUCCESS CRITERIA: Metrics defined with realistic targets?
5. SCOPE BOUNDARIES: MVP scope appropriate? Clear exclusions?

DECISION: Average >= 8: PASS, 6-7: CLARIFY, < 6: FAIL

Return ONLY valid JSON with gate, gateName, decision, overallScore, scores, validatedProblemStatement, strengths, concerns, clarifyingQuestions, recommendations, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG1")

    def _execute_qg2(self, client, input_data, customer_name, project_name):
        """QG2: Customer Validation (Scope Lock)."""
        prompt = f"""You are Quality Gate #2 (QG2) - Customer Validation.

CUSTOMER: {customer_name}
PROJECT: {project_name}
MVP PROPOSAL & FEEDBACK:
{json.dumps(input_data, indent=2)}

Validate: SCOPE AGREEMENT, DATA ACCESS, STAKEHOLDER BUY-IN, TIMELINE ACCEPTANCE
DECISION: All confirmed: PROCEED (SCOPE LOCKED), Minor issues: REVISE, Major: HOLD

Return ONLY valid JSON with gate, gateName, decision, scopeLocked, scores, lockedFeatures, deferredToPhase2, concerns, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG2")

    def _execute_qg3(self, client, input_data, customer_name, project_name):
        """QG3: Code Quality Review."""
        prompt = f"""You are Quality Gate #3 (QG3) - Code Quality Review.

CUSTOMER: {customer_name}
PROJECT: {project_name}
CODE & SPECIFICATION:
{json.dumps(input_data, indent=2)}

Review: PATTERN VALIDATION, SECURITY AUDIT, LOGIC CORRECTNESS, INTEGRATION COMPATIBILITY, CODE QUALITY
DECISION: All pass: PASS, Fixable: FIX_REQUIRED, Major problems: FAIL

Return ONLY valid JSON with gate, gateName, decision, securityScore, scores, criticalIssues, fixes, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG3")

    def _execute_qg4(self, client, input_data, customer_name, project_name):
        """QG4: Demo Review (Waiter Pattern)."""
        prompt = f"""You are Quality Gate #4 (QG4) - Demo Review using "Waiter Pattern".

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEMO DATA:
{json.dumps(input_data, indent=2)}

Waiter Pattern: "Would you confidently serve this to the customer?"
Score 1-10: RESPONSE QUALITY, CONVERSATION FLOW, VISUAL PRESENTATION, BUSINESS VALUE, EDGE CASES
DECISION: Average >= 8: PASS, 6-7: POLISH, < 6: FAIL

Return ONLY valid JSON with gate, gateName, decision, waiterScore, scores, strengths, polishItems, blockers, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG4")

    def _execute_qg5(self, client, input_data, customer_name, project_name):
        """QG5: Final Demo Review (Executive Readiness)."""
        prompt = f"""You are Quality Gate #5 (QG5) - Final Demo Review for Executive Presentation.

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEMO DATA:
{json.dumps(input_data, indent=2)}

Score 1-10: OPENING HOOK, PROBLEM ILLUSTRATION, SOLUTION WOW, METRICS CLARITY, INDUSTRY ACCURACY, CLOSING STRENGTH, TECHNICAL POLISH, MVP ALIGNMENT
DECISION: >= 8.5: APPROVE, 7-8.4: MINOR_REVISIONS, 5-6.9: MAJOR_REVISIONS, < 5: REJECT

Return ONLY valid JSON with gate, gateName, decision, executiveReadinessScore, scores, feedback, strengths, approvalReady, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG5")

    def _execute_qg6(self, client, input_data, customer_name, project_name):
        """QG6: Post-Deployment Audit."""
        prompt = f"""You are Quality Gate #6 (QG6) - Post-Deployment Audit.

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEPLOYMENT METRICS:
{json.dumps(input_data, indent=2)}

Score: SYSTEM HEALTH (25%), USAGE ADOPTION (25%), BUSINESS VALUE (30%), CUSTOMER SATISFACTION (20%)
STATUS: GREEN (all meeting targets), YELLOW (some below but trending up), RED (critical failing)

Return ONLY valid JSON with gate, gateName, decision, auditDate, scores, roiValidation, recommendations, optimizations, nextAuditDate."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG6")

    def _parse_gate_response(self, response_text, gate):
        """Parse and validate gate response."""
        parsed = parse_llm_json_response(response_text, "raw_response")
        parsed["status"] = "success"
        parsed["gate"] = gate
        parsed["evaluatedAt"] = datetime.now().isoformat()
        return json.dumps(parsed)

    # =========================================================================
    # PIPELINE ORCHESTRATION METHODS
    # =========================================================================

    def _get_step_guidance(self, kwargs):
        """Get detailed guidance for a specific pipeline step."""
        step = kwargs.get('step', 1)
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')
        project_data = kwargs.get('project_data', {})

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}. Use 1-14."})

        step_info = self.PIPELINE_STEPS[step]
        client = self._get_openai_client()

        prompt = f"""Provide detailed guidance for RAPP Pipeline Step {step}: {step_info['name']}

CUSTOMER: {customer_name}
PROJECT: {project_name}
STEP TYPE: {step_info['type']}

CURRENT PROJECT DATA:
{json.dumps(project_data, indent=2) if project_data else 'No data yet'}

Provide:
1. STEP OVERVIEW - Purpose and objectives
2. INPUTS REQUIRED - What you need before starting
3. KEY ACTIVITIES - Specific tasks and best practices
4. OUTPUTS EXPECTED - Deliverables and quality criteria
5. COMMON PITFALLS - What to avoid
6. RAPP AGENT ACTIONS - Which action to use (e.g., process_transcript, execute_quality_gate with gate=QG1)
7. SUCCESS CRITERIA - How to know you're done"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "get_step_guidance",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "guidance": response.choices[0].message.content,
            "related_gate": step_info.get('gate'),
            "generated_at": datetime.now().isoformat()
        })

    def _get_pipeline_status(self, kwargs):
        """Get overall pipeline status for a project."""
        project_data = kwargs.get('project_data', {})
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')

        completed_steps = project_data.get('completed_steps', [])
        current_step = project_data.get('current_step', 1)
        step_decisions = project_data.get('step_decisions', {})

        progress_percent = len(completed_steps) / 14 * 100

        # Build step status
        step_status = []
        for step_id, step_info in self.PIPELINE_STEPS.items():
            status = "completed" if step_id in completed_steps else "pending"
            if step_id == current_step:
                status = "in_progress"
            if str(step_id) in step_decisions:
                status = f"{status} ({step_decisions[str(step_id)]})"
            step_status.append({
                "step": step_id,
                "name": step_info['name'],
                "type": step_info['type'],
                "status": status
            })

        return json.dumps({
            "status": "success",
            "action": "get_pipeline_status",
            "customer_name": customer_name,
            "project_name": project_name,
            "progress_percent": round(progress_percent, 1),
            "current_step": current_step,
            "current_step_name": self.PIPELINE_STEPS[current_step]['name'],
            "completed_count": len(completed_steps),
            "total_steps": 14,
            "step_status": step_status,
            "generated_at": datetime.now().isoformat()
        })

    def _recommend_next_action(self, kwargs):
        """Recommend the next action based on current state."""
        project_data = kwargs.get('project_data', {})
        current_step = project_data.get('current_step', 1)
        step_decisions = project_data.get('step_decisions', {})

        step_info = self.PIPELINE_STEPS[current_step]
        client = self._get_openai_client()

        prompt = f"""Based on current RAPP Pipeline state, recommend the best next action.

CURRENT STEP: {current_step} - {step_info['name']} ({step_info['type']})
STEP DECISIONS: {json.dumps(step_decisions, indent=2)}

Provide:
1. IMMEDIATE NEXT ACTION - What to do now
2. RAPP AGENT ACTION - The exact action to call (e.g., process_transcript, execute_quality_gate)
3. REQUIRED INPUTS - What parameters are needed
4. BLOCKERS - Any issues to resolve first

Return JSON:
{{
  "recommended_action": "description",
  "rapp_action": "action name from RAPP agent",
  "required_parameters": {{}},
  "blockers": [],
  "priority": "HIGH|MEDIUM|LOW",
  "rationale": "why this is recommended"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_recommendation")
        parsed["status"] = "success"
        parsed["action"] = "recommend_next_action"
        parsed["current_step"] = current_step
        parsed["current_step_name"] = step_info['name']
        parsed["generated_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _get_step_checklist(self, kwargs):
        """Get the completion checklist for a step."""
        step = kwargs.get('step', 1)

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}"})

        step_info = self.PIPELINE_STEPS[step]

        checklists = {
            1: ["Scheduled discovery call", "Prepared questions", "Recorded call", "Captured problem statements", "Identified data sources", "Mapped stakeholders", "Documented success criteria"],
            2: ["Reviewed transcript clarity", "Verified data access", "Confirmed stakeholder alignment", "Validated measurable criteria", "Assessed MVP scope", "Made PASS/FAIL/CLARIFY decision"],
            3: ["Created executive summary", "Defined MVP features (P0/P1/P2)", "Listed out-of-scope items", "Documented data requirements", "Set success metrics", "Added approval section"],
            4: ["Presented MVP to customer", "Received feature approval", "Confirmed out-of-scope accepted", "Got decision-maker sign-off", "LOCKED scope"],
            5: ["Generated BasicAgent code", "Defined metadata schema", "Implemented perform() method", "Added input validation", "Integrated Azure OpenAI", "Added error handling", "No hardcoded credentials"],
            6: ["Validated pattern compliance", "Completed security audit", "Verified logic matches MVP", "Checked Azure integration", "Made PASS/FIX/FAIL decision"],
            7: ["Validated Azure infrastructure", "Deployed Function App", "Uploaded agent code", "Configured environment", "Tested endpoint"],
            8: ["Tested all MVP features", "Verified response quality", "Checked conversation flow", "Applied waiter pattern", "Made PASS/POLISH/FAIL decision"],
            9: ["Created narrative arc", "Wrote narration script", "Designed demo steps", "Included metrics", "Generated demo JSON"],
            10: ["Reviewed opening hook", "Validated problem illustration", "Confirmed wow moment", "Checked metrics", "Made APPROVE/REVISE/REJECT decision"],
            11: ["Collected feedback", "Classified items (bug/polish/feature/creep)", "Deferred scope creep", "Created iteration plan"],
            12: ["Completed security hardening", "Deployed production infra", "Configured Key Vault", "Set up monitoring", "Created documentation"],
            13: ["Collected health metrics", "Analyzed usage patterns", "Measured business value", "Gathered customer feedback", "Generated audit report"],
            14: ["Reviewed audit results", "Prioritized optimization backlog", "Identified scaling opportunities", "Documented lessons learned"]
        }

        return json.dumps({
            "status": "success",
            "action": "get_step_checklist",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "checklist": checklists.get(step, []),
            "generated_at": datetime.now().isoformat()
        })

    def _validate_step_completion(self, kwargs):
        """Validate if a step is ready for completion."""
        step = kwargs.get('step', 1)
        project_data = kwargs.get('project_data', {})

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}"})

        step_info = self.PIPELINE_STEPS[step]
        step_checklists = project_data.get('step_checklists', {})
        step_decisions = project_data.get('step_decisions', {})

        checklist_data = step_checklists.get(str(step), {})
        checklist_complete = all(checklist_data.values()) if checklist_data else False

        gate_decision = step_decisions.get(str(step))
        gate_passed = gate_decision in ['PASS', 'PROCEED', 'APPROVE', 'GREEN'] if gate_decision else None

        if step_info['type'] == 'audit':
            is_valid = checklist_complete and gate_decision is not None
            can_proceed = gate_passed
        else:
            is_valid = checklist_complete
            can_proceed = is_valid

        return json.dumps({
            "status": "success",
            "action": "validate_step_completion",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "validation": {
                "checklist_complete": checklist_complete,
                "gate_decision": gate_decision,
                "gate_passed": gate_passed,
                "is_valid": is_valid,
                "can_proceed": can_proceed
            },
            "next_step": step + 1 if can_proceed and step < 14 else None,
            "message": f"Step {step} {'ready to proceed' if can_proceed else 'not yet complete'}",
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # AUTO-PROCESS AND REPORT GENERATION METHODS
    # =========================================================================

    def _auto_process(self, kwargs):
        """
        Automatically process a project based on available inputs.

        Scans the project folder for input files, determines the appropriate
        pipeline step, processes the inputs, and generates professional PDF reports.

        Folder structure expected:
            rapp_projects/{project_id}/
                inputs/
                    discovery_transcript.txt
                    customer_feedback.txt
                    code_to_review.py
                    etc.
                outputs/
                    (reports generated here)
                project_state.json
        """
        project_id = kwargs.get('project_id')
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent Project')
        user_guid = kwargs.get('user_guid', 'default')

        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required for auto_process"})

        try:
            # Scan inputs
            inputs = self._scan_project_inputs(project_id, user_guid)
            if not inputs['files']:
                return json.dumps({
                    "status": "error",
                    "error": "No input files found",
                    "expected_location": f"rapp_projects/{project_id}/inputs/",
                    "supported_files": list(self.INPUT_PATTERNS.keys())
                })

            # Load or create project state
            project_state = self._load_project_state(project_id, user_guid)
            project_state['customer_name'] = customer_name
            project_state['project_name'] = project_name

            # Determine what to process based on inputs and current state
            actions_taken = []
            reports_generated = []

            # Process discovery transcript if present
            if inputs.get('discovery_transcript'):
                logger.info(f"Processing discovery transcript for project {project_id}")
                transcript_content = inputs['discovery_transcript']['content']

                # Process transcript
                result = json.loads(self._process_transcript({
                    'customer_name': customer_name,
                    'transcript': transcript_content,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if result.get('status') == 'success':
                    actions_taken.append("Processed discovery transcript")
                    project_state['discovery_data'] = result.get('extracted_data', {})
                    project_state['current_step'] = 2

                    # Generate discovery report
                    report_path = self._generate_and_save_report(
                        "discovery", result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "discovery", "path": report_path})

                    # Execute QG1
                    qg1_result = json.loads(self._execute_quality_gate({
                        'gate': 'QG1',
                        'customer_name': customer_name,
                        'project_name': project_name,
                        'input_data': result.get('extracted_data', {}),
                        'project_id': project_id,
                        'user_guid': user_guid
                    }))

                    if qg1_result.get('status') == 'success':
                        actions_taken.append(f"Executed QG1: {qg1_result.get('decision', 'N/A')}")
                        project_state['qg1_result'] = qg1_result
                        if qg1_result.get('decision') == 'PASS':
                            project_state['completed_steps'] = project_state.get('completed_steps', []) + [1, 2]
                            project_state['current_step'] = 3

                        # Generate QG1 report
                        report_path = self._generate_and_save_report(
                            "qg1", qg1_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "qg1", "path": report_path})

            # Process customer feedback for QG2 if present
            if inputs.get('customer_feedback') and project_state.get('current_step', 1) >= 3:
                logger.info(f"Processing customer feedback for project {project_id}")
                feedback_content = inputs['customer_feedback']['content']

                # First generate MVP if not done
                if not project_state.get('mvp_document'):
                    mvp_result = json.loads(self._generate_full_mvp_document({
                        'customer_name': customer_name,
                        'project_name': project_name,
                        'discovery_data': project_state.get('discovery_data', {}),
                        'problem_statement': project_state.get('discovery_data', {}).get('problemStatements', [{}])[0].get('problem', '')
                    }))

                    if mvp_result.get('status') == 'success':
                        actions_taken.append("Generated MVP document")
                        project_state['mvp_document'] = mvp_result

                        report_path = self._generate_and_save_report(
                            "mvp", mvp_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "mvp", "path": report_path})

                # Execute QG2 with customer feedback
                qg2_input = {
                    'mvp_document': project_state.get('mvp_document', {}),
                    'customer_feedback': feedback_content
                }
                qg2_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG2',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': qg2_input,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg2_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG2: {qg2_result.get('decision', 'N/A')}")
                    project_state['qg2_result'] = qg2_result
                    if qg2_result.get('decision') == 'PROCEED':
                        project_state['scope_locked'] = True
                        project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [3, 4]))
                        project_state['current_step'] = 5

                    report_path = self._generate_and_save_report(
                        "qg2", qg2_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg2", "path": report_path})

            # Process code for review if present
            if inputs.get('code_to_review') and project_state.get('current_step', 1) >= 5:
                logger.info(f"Processing code review for project {project_id}")
                code_content = inputs['code_to_review']['content']

                # First generate agent code if not done
                if not project_state.get('generated_code'):
                    discovery_data = project_state.get('discovery_data', {})
                    suggested_agents = discovery_data.get('suggestedAgents', ['CustomAgent'])
                    agent_name = suggested_agents[0] if suggested_agents else 'CustomAgent'

                    code_result = json.loads(self._generate_agent_code({
                        'agent_name': agent_name,
                        'agent_description': project_state.get('mvp_document', {}).get('document', '')[:500],
                        'features': [p.get('problem', '') for p in discovery_data.get('problemStatements', [])],
                        'customer_name': customer_name,
                        'project_id': project_id,
                        'user_guid': user_guid
                    }))

                    if code_result.get('status') == 'success':
                        actions_taken.append("Generated agent code")
                        project_state['generated_code'] = code_result

                        report_path = self._generate_and_save_report(
                            "code", code_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "code", "path": report_path})

                # Execute QG3 code review
                qg3_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG3',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': {
                        'code': code_content,
                        'features': project_state.get('mvp_document', {}).get('features', {})
                    },
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg3_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG3: {qg3_result.get('decision', 'N/A')}")
                    project_state['qg3_result'] = qg3_result
                    if qg3_result.get('decision') == 'PASS':
                        project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [5, 6]))
                        project_state['current_step'] = 7

                    report_path = self._generate_and_save_report(
                        "qg3", qg3_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg3", "path": report_path})

            # Process deployment metrics for QG6 if present
            if inputs.get('deployment_metrics') and project_state.get('current_step', 1) >= 12:
                logger.info(f"Processing deployment metrics for project {project_id}")
                try:
                    metrics_content = json.loads(inputs['deployment_metrics']['content'])
                except json.JSONDecodeError:
                    metrics_content = {"raw_metrics": inputs['deployment_metrics']['content']}

                qg6_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG6',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': metrics_content,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg6_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG6: {qg6_result.get('decision', 'N/A')}")
                    project_state['qg6_result'] = qg6_result
                    project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [13]))
                    project_state['current_step'] = 14

                    report_path = self._generate_and_save_report(
                        "qg6", qg6_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg6", "path": report_path})

            # Generate executive summary report
            exec_summary = self._generate_executive_summary_data(project_state, customer_name, project_name)
            report_path = self._generate_and_save_report(
                "executive_summary", exec_summary, customer_name, project_name, project_id, user_guid
            )
            if report_path:
                reports_generated.append({"type": "executive_summary", "path": report_path})

            # Save project state
            self._save_project_state(project_id, project_state, user_guid)

            return json.dumps({
                "status": "success",
                "action": "auto_process",
                "project_id": project_id,
                "customer_name": customer_name,
                "project_name": project_name,
                "inputs_detected": list(inputs['files'].keys()),
                "actions_taken": actions_taken,
                "reports_generated": reports_generated,
                "current_step": project_state.get('current_step', 1),
                "completed_steps": project_state.get('completed_steps', []),
                "progress_percent": len(project_state.get('completed_steps', [])) / 14 * 100,
                "processed_at": datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"Error in auto_process: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "project_id": project_id
            })

    def _scan_project_inputs(self, project_id: str, user_guid: str) -> Dict[str, Any]:
        """Scan project inputs folder for files."""
        inputs = {'files': {}}
        input_directory = f"rapp_projects/{project_id}/inputs"

        try:
            files = self.storage_manager.list_files(input_directory)
            if not files:
                return inputs

            for file_info in files:
                filename = file_info.name if hasattr(file_info, 'name') else str(file_info)
                filename_lower = filename.lower()

                # Determine file type
                file_type = None
                for input_type, patterns in self.INPUT_PATTERNS.items():
                    for pattern in patterns:
                        if pattern in filename_lower:
                            file_type = input_type
                            break
                    if file_type:
                        break

                if file_type:
                    content = self.storage_manager.read_file(input_directory, filename)
                    if content:
                        inputs['files'][filename] = {
                            'type': file_type,
                            'size': len(content)
                        }
                        inputs[file_type] = {
                            'filename': filename,
                            'content': content
                        }

        except Exception as e:
            logger.warning(f"Error scanning inputs for project {project_id}: {e}")

        return inputs

    def _load_project_state(self, project_id: str, user_guid: str) -> Dict[str, Any]:
        """Load or create project state."""
        state_directory = f"rapp_projects/{project_id}"
        state_file = "project_state.json"

        try:
            content = self.storage_manager.read_file(state_directory, state_file)
            if content:
                return json.loads(content)
        except Exception:
            pass

        return {
            'project_id': project_id,
            'current_step': 1,
            'completed_steps': [],
            'created_at': datetime.now().isoformat()
        }

    def _save_project_state(self, project_id: str, state: Dict[str, Any], user_guid: str):
        """Save project state."""
        state_directory = f"rapp_projects/{project_id}"
        state_file = "project_state.json"
        state['updated_at'] = datetime.now().isoformat()

        try:
            self.storage_manager.write_file(state_directory, state_file, json.dumps(state, indent=2))
        except Exception as e:
            logger.warning(f"Could not save project state: {e}")

    def _generate_and_save_report(
        self,
        report_type: str,
        data: Dict[str, Any],
        customer_name: str,
        project_name: str,
        project_id: str,
        user_guid: str
    ) -> Optional[str]:
        """Generate a PDF report and save it to the outputs folder."""
        if not REPORT_GENERATOR_AVAILABLE:
            logger.warning("Report generator not available. Install reportlab.")
            return None

        try:
            generator = RAPPReportGenerator()
            pdf_bytes = generator.generate_report(
                report_type=report_type,
                data=data,
                customer_name=customer_name,
                project_name=project_name
            )

            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{report_type}_report_{timestamp}.pdf"
            output_directory = f"rapp_projects/{project_id}/outputs"

            # Save to storage
            self.storage_manager.write_file(output_directory, filename, pdf_bytes)
            logger.info(f"Generated report: {output_directory}/{filename}")

            return f"{output_directory}/{filename}"

        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return None

    def _generate_executive_summary_data(
        self,
        project_state: Dict[str, Any],
        customer_name: str,
        project_name: str
    ) -> Dict[str, Any]:
        """Generate data for executive summary report."""
        completed_steps = project_state.get('completed_steps', [])
        current_step = project_state.get('current_step', 1)

        qg_decisions = []
        for gate in ['qg1', 'qg2', 'qg3', 'qg4', 'qg5', 'qg6']:
            result = project_state.get(f'{gate}_result', {})
            if result.get('decision'):
                qg_decisions.append(f"{gate.upper()}: {result['decision']}")

        return {
            'summary': f"RAPP Pipeline progress for {project_name} ({customer_name}). "
                      f"Currently at Step {current_step} ({self.PIPELINE_STEPS[current_step]['name']}). "
                      f"Completed {len(completed_steps)} of 14 steps.",
            'metrics': {
                'progress_percent': round(len(completed_steps) / 14 * 100, 1),
                'completed_steps': len(completed_steps),
                'current_step': current_step
            },
            'progress_percent': round(len(completed_steps) / 14 * 100, 1),
            'current_step': current_step,
            'current_step_name': self.PIPELINE_STEPS[current_step]['name'],
            'quality_gate_decisions': qg_decisions,
            'scope_locked': project_state.get('scope_locked', False),
            'discovery_data': project_state.get('discovery_data', {}),
            'generated_at': datetime.now().isoformat()
        }

    def _generate_report(self, kwargs):
        """Generate a professional PDF report for a specific report type."""
        report_type = kwargs.get('report_type')
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent Project')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')
        data = kwargs.get('input_data') or kwargs.get('data', {})

        if not report_type:
            return json.dumps({"status": "error", "error": "report_type is required"})

        if not REPORT_GENERATOR_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": "Report generator not available. Install reportlab: pip install reportlab"
            })

        try:
            generator = RAPPReportGenerator()
            pdf_bytes = generator.generate_report(
                report_type=report_type,
                data=data,
                customer_name=customer_name,
                project_name=project_name
            )

            # Save if project_id provided
            output_path = None
            if project_id:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{report_type}_report_{timestamp}.pdf"
                output_directory = f"rapp_projects/{project_id}/outputs"
                self.storage_manager.write_file(output_directory, filename, pdf_bytes)
                output_path = f"{output_directory}/{filename}"

            return json.dumps({
                "status": "success",
                "action": "generate_report",
                "report_type": report_type,
                "customer_name": customer_name,
                "project_name": project_name,
                "output_path": output_path,
                "pdf_size_bytes": len(pdf_bytes),
                "generated_at": datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"Error generating report: {e}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e)
            })

    # =========================================================================
    # TRANSCRIPT TO AGENT - FAST PATH FOR QUICK ITERATION
    # =========================================================================

    def _transcript_to_agent(self, kwargs):
        """
        FASTEST PATH: Transcript → Deployable Agent + Demo in one step.

        This method:
        1. Reads transcript from Azure storage or inline
        2. Analyzes transcript to extract agent requirements
        3. Generates complete agent Python code (BasicAgent pattern)
        4. Generates demo JSON for ScriptedDemoAgent
        5. Auto-deploys both to agents/ and demos/ folders

        User workflow:
        1. Drop transcript in rapp_projects/{project_id}/inputs/ OR pass inline
        2. Call this action
        3. Agent and demo are ready to use immediately

        Args:
            project_id: Project ID (reads transcript from rapp_projects/{project_id}/inputs/)
            transcript: Inline transcript text (alternative to project_id)
            customer_name: Customer/company name
            agent_priority: Which agent to prioritize (e.g., 'contract', 'chargeback')
            deploy_to_storage: If True, auto-deploy to agents/ and demos/ folders
            user_guid: User GUID for storage access
        """
        project_id = kwargs.get('project_id')
        transcript = kwargs.get('transcript', '')
        customer_name = kwargs.get('customer_name', 'Customer')
        agent_priority = kwargs.get('agent_priority', '')
        deploy_to_storage = kwargs.get('deploy_to_storage', True)
        user_guid = kwargs.get('user_guid', 'default')

        try:
            # Step 1: Get transcript content
            if not transcript and project_id:
                transcript = self._get_transcript_from_storage(project_id, user_guid)

            if not transcript:
                return json.dumps({
                    "status": "error",
                    "error": "No transcript provided. Either pass 'transcript' parameter or ensure transcript file exists in rapp_projects/{project_id}/inputs/",
                    "expected_patterns": self.INPUT_PATTERNS.get('discovery_transcript', [])
                })

            # Step 2: Analyze transcript to extract agent requirements
            logger.info(f"Analyzing transcript for {customer_name}...")
            agent_spec = self._analyze_transcript_for_agent(transcript, customer_name, agent_priority)

            if agent_spec.get('status') == 'error':
                return json.dumps(agent_spec)

            # Step 3: Generate complete agent Python code
            logger.info(f"Generating agent code for {agent_spec.get('agent_name')}...")
            agent_code = self._generate_complete_agent_code(agent_spec, customer_name)

            # Step 4: Generate demo JSON
            logger.info(f"Generating demo JSON...")
            demo_json = self._generate_demo_json(agent_spec, customer_name)

            # Step 5: Generate HTML tester
            logger.info(f"Generating HTML tester...")
            html_tester = self._generate_agent_tester_html(agent_spec, demo_json, customer_name)

            # Step 6: Deploy everything to project folder (and optionally to main folders)
            deployment_results = {}
            if deploy_to_storage:
                deployment_results = self._deploy_project_outputs(
                    project_id=project_id or agent_spec.get('agent_id'),
                    agent_spec=agent_spec,
                    agent_code=agent_code,
                    demo_json=demo_json,
                    html_tester=html_tester,
                    deploy_to_main_folders=kwargs.get('deploy_to_main_folders', True),
                    user_guid=user_guid
                )

            agent_id = agent_spec.get('agent_id')
            project_folder = project_id or agent_id

            # Build response
            result = {
                "status": "success",
                "action": "transcript_to_agent",
                "customer_name": customer_name,
                "project_id": project_folder,
                "agent_spec": {
                    "agent_name": agent_spec.get('agent_name'),
                    "agent_id": agent_id,
                    "class_name": agent_spec.get('class_name'),
                    "description": agent_spec.get('description'),
                    "category": agent_spec.get('category'),
                    "actions": [a.get('name') for a in agent_spec.get('actions', [])],
                    "use_cases": agent_spec.get('use_cases', []),
                    "data_sources": agent_spec.get('data_sources', [])
                },
                "files_generated": {
                    "agent_file": f"{agent_id}_agent.py",
                    "demo_file": f"{agent_id}_demo.json",
                    "tester_file": "agent_tester.html",
                    "agent_code_length": len(agent_code),
                    "demo_json_length": len(json.dumps(demo_json)),
                    "html_tester_length": len(html_tester)
                },
                "project_folder": f"rapp_projects/{project_folder}/outputs/",
                "deployment": deployment_results,
                "agent_code": agent_code,
                "demo_json": demo_json,
                "html_tester": html_tester,
                "next_steps": [
                    f"All files in: rapp_projects/{project_folder}/outputs/",
                    f"Open agent_tester.html to test the agent and demo",
                    f"Agent also deployed to: agents/{agent_id}_agent.py" if deployment_results.get('main_agent_deployed') else f"To deploy: copy {agent_id}_agent.py to agents/",
                    "Restart function app to load the new agent"
                ],
                "generated_at": datetime.now().isoformat()
            }

            return json.dumps(result)

        except Exception as e:
            logger.error(f"Error in transcript_to_agent: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "action": "transcript_to_agent"
            })

    def _get_transcript_from_storage(self, project_id: str, user_guid: str) -> str:
        """Read transcript from project inputs folder."""
        input_directory = f"rapp_projects/{project_id}/inputs"

        try:
            files = self.storage_manager.list_files(input_directory)
            if not files:
                return ""

            for file_info in files:
                filename = file_info.name if hasattr(file_info, 'name') else str(file_info)
                filename_lower = filename.lower()

                # Check for transcript patterns
                for pattern in self.INPUT_PATTERNS.get('discovery_transcript', []):
                    if pattern in filename_lower:
                        content = self.storage_manager.read_file(input_directory, filename)
                        if content:
                            logger.info(f"Found transcript: {filename}")
                            return content

            return ""
        except Exception as e:
            logger.warning(f"Error reading transcript from storage: {e}")
            return ""

    def _analyze_transcript_for_agent(self, transcript: str, customer_name: str, agent_priority: str = "") -> Dict[str, Any]:
        """Analyze transcript to extract agent specification."""
        client = self._get_openai_client()

        priority_instruction = ""
        if agent_priority:
            priority_instruction = f"\n\nIMPORTANT: The user wants to prioritize building an agent related to: {agent_priority}. Focus on this area if mentioned in the transcript."

        prompt = f"""Analyze this discovery call transcript and design a production-ready AI agent.

CUSTOMER: {customer_name}
{priority_instruction}

TRANSCRIPT:
{transcript}

Based on the transcript, design ONE specific AI agent that addresses their highest-priority need.

Return ONLY valid JSON (no markdown):
{{
  "agent_name": "Human readable name (e.g., 'Artist Contract Analyzer')",
  "agent_id": "snake_case_agent (e.g., 'artist_contract_analyzer_agent')",
  "class_name": "PascalCaseAgent (e.g., 'ArtistContractAnalyzerAgent')",
  "description": "2-3 sentence description of what the agent does and its value proposition",
  "category": "legal|finance|operations|sales|hr|analytics|communications",
  "problem_statement": "The specific problem this agent solves",
  "target_users": ["list of user roles who will use this"],
  "data_sources": [
    {{"name": "source name", "type": "API|Database|File|Manual", "description": "what data it provides"}}
  ],
  "actions": [
    {{
      "name": "action_name",
      "description": "What this action does",
      "parameters": ["param1", "param2"],
      "example_input": {{"action": "action_name", "param1": "value"}},
      "example_output": "Example response text"
    }}
  ],
  "use_cases": ["list of 4-6 specific use cases"],
  "integrations": ["list of systems this would integrate with"],
  "success_metrics": ["how success is measured"],
  "demo_conversation": [
    {{"role": "user", "content": "Example user message"}},
    {{"role": "agent", "content": "Example agent response with **markdown** formatting"}}
  ],
  "sample_scenarios": [
    {{
      "name": "Scenario Name",
      "description": "What this scenario demonstrates",
      "prompts": ["prompt 1", "prompt 2", "prompt 3"]
    }}
  ]
}}

Design 4-6 actions that cover the main capabilities. Make the demo_conversation show a realistic interaction that demonstrates the agent's value. Include at least 2-3 sample scenarios."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = parse_llm_json_response(response.choices[0].message.content, "raw_spec")

        # Validate required fields
        required = ['agent_name', 'agent_id', 'class_name', 'description', 'actions']
        missing = [f for f in required if not result.get(f)]
        if missing:
            result['status'] = 'error'
            result['error'] = f"Missing required fields: {missing}"
        else:
            result['status'] = 'success'

        return result

    def _generate_complete_agent_code(self, agent_spec: Dict[str, Any], customer_name: str) -> str:
        """Generate complete, production-ready agent Python code."""
        client = self._get_openai_client()

        prompt = f"""Generate a complete, production-ready Python agent following the BasicAgent pattern.

AGENT SPECIFICATION:
{json.dumps(agent_spec, indent=2)}

CUSTOMER: {customer_name}

REQUIREMENTS:
1. Follow the BasicAgent pattern EXACTLY:
   - Import from agents.basic_agent import BasicAgent
   - Class inherits from BasicAgent
   - __init__ sets self.name, self.metadata with full JSON Schema, calls super().__init__()
   - perform(**kwargs) method that routes to action handlers and ALWAYS returns json.dumps()

2. Metadata must include:
   - name: {agent_spec.get('agent_name', 'Agent')}
   - description: Full description with all actions listed
   - parameters: Complete JSON Schema with all action parameters

3. Code quality:
   - Use logging, not print
   - No hardcoded credentials - use os.environ
   - Wrap external calls in try/except
   - Return JSON strings from perform() - NEVER raw dicts or exceptions
   - Include docstrings

4. Action handlers:
   - Create a _handle_{{action_name}} method for each action
   - Each handler returns a dict that gets json.dumps() in perform()
   - Include realistic mock data that demonstrates the agent's capabilities

5. Include:
   - Module docstring with agent purpose and usage
   - Usage example in if __name__ == "__main__" block
   - All necessary imports at the top

Generate the complete Python code - no placeholders, no TODOs. The agent should work immediately when dropped into the agents/ folder."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        code = response.choices[0].message.content

        # Extract code from markdown if present
        if '```python' in code:
            code_start = code.find('```python') + 9
            code_end = code.rfind('```')
            if code_end > code_start:
                code = code[code_start:code_end].strip()
        elif '```' in code:
            parts = code.split('```')
            if len(parts) >= 2:
                code = parts[1].strip()

        return code

    def _generate_demo_json(self, agent_spec: Dict[str, Any], customer_name: str) -> Dict[str, Any]:
        """Generate demo JSON in the ScriptedDemoAgent format."""

        # Build actions list from spec
        actions = []
        for action in agent_spec.get('actions', []):
            actions.append({
                "name": action.get('name'),
                "description": action.get('description'),
                "parameters": action.get('parameters', []),
                "example": {
                    "input": action.get('example_input', {}),
                    "output": action.get('example_output', '')
                }
            })

        # Build metadata
        parameters_properties = {
            "action": {
                "type": "string",
                "enum": [a.get('name') for a in agent_spec.get('actions', [])],
                "description": "The action to perform"
            }
        }

        # Add common parameters based on actions
        param_set = set()
        for action in agent_spec.get('actions', []):
            for param in action.get('parameters', []):
                param_set.add(param)

        for param in param_set:
            if param != 'action':
                parameters_properties[param] = {
                    "type": "string",
                    "description": f"{param.replace('_', ' ').title()} parameter"
                }

        demo_json = {
            "agent": {
                "id": agent_spec.get('agent_id'),
                "name": agent_spec.get('agent_name'),
                "version": "1.0.0",
                "category": agent_spec.get('category', 'general'),
                "icon": self._get_category_icon(agent_spec.get('category', 'general')),
                "description": agent_spec.get('description'),
                "tokens": 750,
                "author": f"RAPP Pipeline - {customer_name}",
                "created": datetime.now().strftime("%Y-%m-%d"),
                "updated": datetime.now().strftime("%Y-%m-%d")
            },
            "metadata": {
                "name": agent_spec.get('class_name', '').replace('Agent', ''),
                "description": agent_spec.get('description'),
                "parameters": {
                    "type": "object",
                    "properties": parameters_properties,
                    "required": ["action"]
                }
            },
            "actions": actions,
            "useCases": agent_spec.get('use_cases', []),
            "integrations": agent_spec.get('integrations', []),
            "demoConversation": agent_spec.get('demo_conversation', []),
            "sampleScenarios": agent_spec.get('sample_scenarios', [])
        }

        return demo_json

    def _get_category_icon(self, category: str) -> str:
        """Get FontAwesome icon for category."""
        icons = {
            "legal": "fa-gavel",
            "finance": "fa-chart-line",
            "operations": "fa-cogs",
            "sales": "fa-handshake",
            "hr": "fa-users",
            "analytics": "fa-chart-bar",
            "communications": "fa-comments",
            "general": "fa-robot"
        }
        return icons.get(category, "fa-robot")

    def _deploy_project_outputs(self, project_id: str, agent_spec: Dict, agent_code: str,
                                  demo_json: Dict, html_tester: str, deploy_to_main_folders: bool,
                                  user_guid: str) -> Dict:
        """Deploy all generated files to project folder and optionally to main folders."""
        results = {
            "project_deployed": False,
            "main_agent_deployed": False,
            "main_demo_deployed": False,
            "project_path": None,
            "files": [],
            "errors": []
        }

        agent_id = agent_spec.get('agent_id', 'generated_agent')
        output_dir = f"rapp_projects/{project_id}/outputs"

        # Ensure output directory exists
        try:
            self.storage_manager.ensure_directory_exists(output_dir)
        except Exception as e:
            logger.warning(f"Could not ensure directory exists: {e}")

        # Deploy to project folder
        try:
            # Agent code
            agent_filename = f"{agent_id}_agent.py"
            self.storage_manager.write_file(output_dir, agent_filename, agent_code)
            results['files'].append(f"{output_dir}/{agent_filename}")
            logger.info(f"Saved agent to: {output_dir}/{agent_filename}")

            # Demo JSON
            demo_filename = f"{agent_id}_demo.json"
            self.storage_manager.write_file(output_dir, demo_filename, json.dumps(demo_json, indent=2))
            results['files'].append(f"{output_dir}/{demo_filename}")
            logger.info(f"Saved demo to: {output_dir}/{demo_filename}")

            # HTML Tester
            self.storage_manager.write_file(output_dir, "agent_tester.html", html_tester)
            results['files'].append(f"{output_dir}/agent_tester.html")
            logger.info(f"Saved tester to: {output_dir}/agent_tester.html")

            # Result JSON (without the large code/html fields)
            result_summary = {
                "agent_id": agent_id,
                "agent_name": agent_spec.get('agent_name'),
                "customer_name": agent_spec.get('customer_name', 'Unknown'),
                "category": agent_spec.get('category'),
                "actions": [a.get('name') for a in agent_spec.get('actions', [])],
                "generated_at": datetime.now().isoformat(),
                "files": [agent_filename, demo_filename, "agent_tester.html"]
            }
            self.storage_manager.write_file(output_dir, "result.json", json.dumps(result_summary, indent=2))
            results['files'].append(f"{output_dir}/result.json")

            results['project_deployed'] = True
            results['project_path'] = output_dir
            logger.info(f"All project files saved to: {output_dir}")

        except Exception as e:
            results['errors'].append(f"Project deployment failed: {str(e)}")
            logger.error(f"Failed to deploy to project folder: {e}")

        # Optionally deploy to main agents/ and demos/ folders
        if deploy_to_main_folders:
            try:
                agent_path = f"{agent_id}_agent.py"
                self.storage_manager.write_file('agents', agent_path, agent_code)
                results['main_agent_deployed'] = True
                logger.info(f"Deployed agent to: agents/{agent_path}")
            except Exception as e:
                results['errors'].append(f"Main agent deployment failed: {str(e)}")
                logger.error(f"Failed to deploy to agents/: {e}")

            try:
                demo_path = f"{agent_id}_demo.json"
                self.storage_manager.write_file('demos', demo_path, json.dumps(demo_json, indent=2))
                results['main_demo_deployed'] = True
                logger.info(f"Deployed demo to: demos/{demo_path}")
            except Exception as e:
                results['errors'].append(f"Main demo deployment failed: {str(e)}")
                logger.error(f"Failed to deploy to demos/: {e}")

        return results

    def _generate_agent_tester_html(self, agent_spec: Dict, demo_json: Dict, customer_name: str) -> str:
        """Generate a self-contained HTML page to test both the real agent and demo."""
        agent_id = agent_spec.get('agent_id', 'agent')
        agent_name = agent_spec.get('agent_name', 'Agent')
        description = agent_spec.get('description', '')
        actions = agent_spec.get('actions', [])
        demo_conversation = demo_json.get('demoConversation', [])
        sample_scenarios = demo_json.get('sampleScenarios', [])

        # Build action buttons HTML
        action_buttons = ""
        for action in actions:
            action_buttons += f'''
            <button class="action-btn" onclick="testAction('{action.get('name')}')">
                <span class="action-name">{action.get('name')}</span>
                <span class="action-desc">{action.get('description', '')[:50]}...</span>
            </button>'''

        # Build demo conversation HTML
        demo_steps = ""
        for i, msg in enumerate(demo_conversation):
            role = msg.get('role', 'user')
            content = msg.get('content', '').replace('`', '\\`').replace('${', '\\${')
            demo_steps += f'''
            <div class="demo-step" data-step="{i}">
                <div class="step-role {role}">{role.upper()}</div>
                <div class="step-content">{content}</div>
            </div>'''

        # Build sample prompts
        sample_prompts = ""
        for scenario in sample_scenarios:
            for prompt in scenario.get('prompts', []):
                sample_prompts += f'<button class="sample-prompt" onclick="sendMessage(`{prompt}`)">{prompt}</button>'

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{agent_name} - Agent Tester</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

        /* Header */
        .header {{
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid #0f3460;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .header h1 {{ color: #00d4ff; margin-bottom: 8px; }}
        .header p {{ color: #888; font-size: 14px; }}
        .header .customer {{ color: #00ff88; font-size: 12px; margin-top: 8px; }}

        /* Config Panel */
        .config-panel {{
            background: #0a0a1a;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: 1fr 1fr auto;
            gap: 12px;
            align-items: end;
        }}
        .config-panel label {{ display: block; font-size: 12px; color: #888; margin-bottom: 4px; }}
        .config-panel input {{
            width: 100%;
            padding: 10px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 6px;
            color: #fff;
            font-size: 13px;
        }}
        .config-panel input:focus {{ outline: none; border-color: #00d4ff; }}
        .save-config {{
            padding: 10px 20px;
            background: #00d4ff;
            color: #1a1a2e;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }}

        /* Tabs */
        .tabs {{
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
        }}
        .tab {{
            padding: 12px 24px;
            background: #16213e;
            border: 2px solid #0f3460;
            border-radius: 8px;
            color: #888;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .tab:hover {{ border-color: #00d4ff; }}
        .tab.active {{
            background: #00d4ff;
            color: #1a1a2e;
            border-color: #00d4ff;
            font-weight: bold;
        }}

        /* Main Content Grid */
        .main-grid {{
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 20px;
        }}

        /* Sidebar */
        .sidebar {{
            background: #0f0f1a;
            border-radius: 12px;
            padding: 16px;
        }}
        .sidebar h3 {{
            color: #00d4ff;
            font-size: 14px;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #1a4a7a;
        }}
        .action-btn {{
            display: block;
            width: 100%;
            padding: 12px;
            margin-bottom: 8px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 8px;
            color: #fff;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .action-btn:hover {{
            background: #1a5a9a;
            border-color: #00d4ff;
            transform: translateX(4px);
        }}
        .action-name {{ display: block; font-weight: bold; margin-bottom: 4px; }}
        .action-desc {{ display: block; font-size: 11px; color: #666; }}

        .sample-prompts {{ margin-top: 16px; }}
        .sample-prompt {{
            display: block;
            width: 100%;
            padding: 8px 12px;
            margin-bottom: 6px;
            background: #0a0a1a;
            border: 1px solid #1a4a7a;
            border-radius: 6px;
            color: #aaa;
            font-size: 12px;
            text-align: left;
            cursor: pointer;
        }}
        .sample-prompt:hover {{ background: #16213e; color: #fff; }}

        /* Chat Area */
        .chat-area {{
            background: #0f0f1a;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            height: 600px;
        }}
        .chat-messages {{
            flex: 1;
            overflow-y: auto;
            padding: 16px;
        }}
        .message {{
            margin-bottom: 16px;
            padding: 12px 16px;
            border-radius: 12px;
            max-width: 85%;
        }}
        .message.user {{
            background: #00d4ff;
            color: #1a1a2e;
            margin-left: auto;
        }}
        .message.agent {{
            background: #16213e;
            border: 1px solid #0f3460;
        }}
        .message pre {{
            background: #0a0a1a;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            margin-top: 8px;
            font-size: 12px;
        }}

        .chat-input {{
            padding: 16px;
            border-top: 1px solid #1a4a7a;
            display: flex;
            gap: 12px;
        }}
        .chat-input input {{
            flex: 1;
            padding: 12px 16px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
        }}
        .chat-input input:focus {{ outline: none; border-color: #00d4ff; }}
        .chat-input button {{
            padding: 12px 24px;
            background: #00d4ff;
            color: #1a1a2e;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }}
        .chat-input button:hover {{ background: #00ffff; }}
        .chat-input button:disabled {{ background: #333; color: #666; cursor: not-allowed; }}

        /* Demo Panel */
        .demo-panel {{ display: none; }}
        .demo-panel.active {{ display: block; }}
        .demo-step {{
            background: #16213e;
            border-radius: 8px;
            margin-bottom: 12px;
            overflow: hidden;
        }}
        .step-role {{
            padding: 8px 16px;
            font-size: 11px;
            font-weight: bold;
            background: #0a0a1a;
        }}
        .step-role.user {{ color: #00ff88; }}
        .step-role.agent {{ color: #00d4ff; }}
        .step-content {{
            padding: 16px;
            white-space: pre-wrap;
            line-height: 1.6;
        }}

        .demo-controls {{
            display: flex;
            gap: 12px;
            margin-top: 16px;
        }}
        .demo-btn {{
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }}
        .demo-btn.play {{ background: #00ff88; color: #1a1a2e; }}
        .demo-btn.reset {{ background: #ff6b6b; color: #fff; }}

        /* Status */
        .status {{
            padding: 8px 16px;
            background: #0a0a1a;
            border-radius: 6px;
            font-size: 12px;
            color: #666;
            margin-top: 12px;
        }}
        .status.success {{ color: #00ff88; }}
        .status.error {{ color: #ff6b6b; }}
        .status.loading {{ color: #00d4ff; }}

        /* Responsive */
        @media (max-width: 900px) {{
            .main-grid {{ grid-template-columns: 1fr; }}
            .config-panel {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{agent_name}</h1>
            <p>{description}</p>
            <div class="customer">Customer: {customer_name}</div>
        </div>

        <div class="config-panel">
            <div>
                <label>API Endpoint</label>
                <input type="text" id="apiEndpoint" value="http://localhost:7071/api/businessinsightbot_function" placeholder="API URL">
            </div>
            <div>
                <label>Function Key (optional)</label>
                <input type="text" id="apiKey" placeholder="Function key for Azure deployment">
            </div>
            <button class="save-config" onclick="saveConfig()">Save</button>
        </div>

        <div class="tabs">
            <button class="tab active" onclick="switchTab('chat')">Real Agent</button>
            <button class="tab" onclick="switchTab('demo')">Demo Mode</button>
        </div>

        <div class="main-grid">
            <div class="sidebar">
                <h3>Agent Actions</h3>
                {action_buttons}

                <div class="sample-prompts">
                    <h3>Sample Prompts</h3>
                    {sample_prompts}
                </div>
            </div>

            <div id="chatPanel" class="chat-area">
                <div class="chat-messages" id="chatMessages"></div>
                <div class="chat-input">
                    <input type="text" id="messageInput" placeholder="Type a message..." onkeypress="if(event.key==='Enter')sendMessage()">
                    <button onclick="sendMessage()" id="sendBtn">Send</button>
                </div>
                <div class="status" id="status">Ready</div>
            </div>

            <div id="demoPanel" class="demo-panel chat-area">
                <div class="chat-messages">
                    {demo_steps}
                </div>
                <div class="demo-controls" style="padding: 16px;">
                    <button class="demo-btn play" onclick="playDemo()">Play Demo</button>
                    <button class="demo-btn reset" onclick="resetDemo()">Reset</button>
                </div>
                <div class="status" id="demoStatus">Click "Play Demo" to start</div>
            </div>
        </div>
    </div>

    <script>
        // Configuration
        let config = {{
            endpoint: localStorage.getItem('agentTesterEndpoint') || 'http://localhost:7071/api/businessinsightbot_function',
            key: localStorage.getItem('agentTesterKey') || ''
        }};

        // Demo JSON data (embedded)
        const demoJson = {json.dumps(demo_json)};
        const agentId = '{agent_id}';

        // Initialize
        document.getElementById('apiEndpoint').value = config.endpoint;
        document.getElementById('apiKey').value = config.key;

        let conversationHistory = [];
        let currentDemoStep = 0;

        function saveConfig() {{
            config.endpoint = document.getElementById('apiEndpoint').value;
            config.key = document.getElementById('apiKey').value;
            localStorage.setItem('agentTesterEndpoint', config.endpoint);
            localStorage.setItem('agentTesterKey', config.key);
            setStatus('Configuration saved!', 'success');
        }}

        function switchTab(tab) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');

            document.getElementById('chatPanel').style.display = tab === 'chat' ? 'flex' : 'none';
            document.getElementById('demoPanel').style.display = tab === 'demo' ? 'flex' : 'none';
            document.getElementById('demoPanel').classList.toggle('active', tab === 'demo');
        }}

        function setStatus(message, type = '') {{
            const status = document.getElementById('status');
            status.textContent = message;
            status.className = 'status ' + type;
        }}

        function addMessage(content, role) {{
            const messages = document.getElementById('chatMessages');
            const div = document.createElement('div');
            div.className = 'message ' + role;

            // Handle markdown-like formatting
            let formatted = content
                .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
                .replace(/\\n/g, '<br>')
                .replace(/`([^`]+)`/g, '<code>$1</code>');

            div.innerHTML = formatted;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }}

        async function sendMessage(text) {{
            const input = document.getElementById('messageInput');
            const message = text || input.value.trim();
            if (!message) return;

            input.value = '';
            addMessage(message, 'user');
            setStatus('Sending...', 'loading');
            document.getElementById('sendBtn').disabled = true;

            conversationHistory.push({{ role: 'user', content: message }});

            try {{
                let url = config.endpoint;
                if (config.key) {{
                    url += (url.includes('?') ? '&' : '?') + 'code=' + config.key;
                }}

                const response = await fetch(url, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        user_input: message,
                        conversation_history: conversationHistory
                    }})
                }});

                const data = await response.json();
                const assistantResponse = data.assistant_response || data.error || 'No response';

                addMessage(assistantResponse, 'agent');
                conversationHistory.push({{ role: 'assistant', content: assistantResponse }});
                setStatus('Ready', 'success');

            }} catch (err) {{
                setStatus('Error: ' + err.message, 'error');
                addMessage('Error: ' + err.message, 'agent');
            }}

            document.getElementById('sendBtn').disabled = false;
        }}

        function testAction(actionName) {{
            const prompt = `Test the ${{actionName}} action`;
            sendMessage(prompt);
        }}

        // Demo functions
        function playDemo() {{
            const steps = document.querySelectorAll('.demo-step');
            let i = 0;

            function showNext() {{
                if (i < steps.length) {{
                    steps[i].style.display = 'block';
                    steps[i].scrollIntoView({{ behavior: 'smooth' }});
                    i++;
                    document.getElementById('demoStatus').textContent = `Step ${{i}} of ${{steps.length}}`;
                    setTimeout(showNext, 2000);
                }} else {{
                    document.getElementById('demoStatus').textContent = 'Demo complete!';
                }}
            }}

            // Hide all first
            steps.forEach(s => s.style.display = 'none');
            showNext();
        }}

        function resetDemo() {{
            document.querySelectorAll('.demo-step').forEach(s => s.style.display = 'block');
            document.getElementById('demoStatus').textContent = 'Click "Play Demo" to start';
        }}
    </script>
</body>
</html>'''
        return html


# Usage example
if __name__ == "__main__":
    agent = RAPPAgent()

    # Test discovery preparation
    result = agent.perform(
        action="prepare_discovery_call",
        customer_name="Acme Corp",
        industry="manufacturing"
    )
    print("Prepare Discovery:", json.loads(result)["status"])

    # Test MVP generation
    result = agent.perform(
        action="generate_mvp_poke",
        customer_name="Acme Corp",
        project_name="Inventory Optimizer",
        problem_statement="Manual inventory counts take 4 hours daily"
    )
    print("MVP Poke:", json.loads(result)["status"])

    # Test quality gate
    result = agent.perform(
        action="execute_quality_gate",
        gate="QG1",
        customer_name="Acme Corp",
        input_data={"problemStatements": [{"problem": "Manual data entry"}]}
    )
    print("QG1:", json.loads(result).get("decision", "N/A"))

    # Test pipeline status
    result = agent.perform(
        action="get_pipeline_status",
        customer_name="Acme Corp",
        project_data={"current_step": 3, "completed_steps": [1, 2]}
    )
    print("Status:", json.loads(result)["progress_percent"], "% complete")
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
