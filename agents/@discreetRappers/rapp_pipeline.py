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
    "name": "@discreetRappers/rapp_pipeline",
    "version": "1.0.0",
    "display_name": "RAPP",
    "description": "Full RAPP pipeline — transcript to agent, discovery, MVP, code gen, quality gates QG1-QG6, PDF reports.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT"],
    "dependencies": ["@rapp/basic-agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from utils.storage_factory import get_storage_manager

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
