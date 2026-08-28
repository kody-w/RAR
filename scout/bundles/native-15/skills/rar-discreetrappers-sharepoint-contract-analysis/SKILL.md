---
name: "rar-discreetrappers-sharepoint-contract-analysis"
description: "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sharepoint_contract_analysis_agent", "rar_sha256": "befdce082ff846fa57e936fc130bd1e423451de8da911a50674b9a4c9c261d32", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Bill Whalen", "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/sharepoint_contract_analysis_agent`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_contract_analysis_agent.py` and in the RCI capsule.

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

Agent: ContractAnalysisAgent
Purpose: Analyze, interpret, and summarize contracts stored in Azure File Storage
Data Sources: Azure File Storage (contracts/ folder), Azure OpenAI for analysis
Production Ready: Reads real documents, extracts text, performs AI-powered analysis

Supported formats: PDF, DOCX, TXT
Storage path: contracts/ folder in Azure File Storage

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform. Use 'full_workup' when user says 'work on' a contract to run comprehensive analysis.",
      "enum": [
        "list_contracts",
        "full_workup",
        "analyze_contract",
        "extract_clauses",
        "summarize_contract",
        "identify_risks",
        "compare_contracts"
      ],
      "type": "string"
    },
    "audience": {
      "description": "Target audience for summary: legal, business, executive",
      "enum": [
        "legal",
        "business",
        "executive"
      ],
      "type": "string"
    },
    "clause_types": {
      "description": "Specific clause types to extract: financial, rights, obligations, termination, exclusivity, territory, duration",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "contract_name": {
      "description": "Name of the contract file in Azure storage (e.g., 'artist_agreement_2026.pdf')",
      "type": "string"
    },
    "contract_name_b": {
      "description": "Second contract name for comparison (used with compare_contracts action)",
      "type": "string"
    },
    "summary_type": {
      "description": "Type of summary: executive (brief), detailed, or legal",
      "enum": [
        "executive",
        "detailed",
        "legal"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_contract_analysis_agent.py` and embedded as the fenced Python below (sha256 befdce082ff846fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_contract_analysis_agent.py` first:

```bash
python3 sharepoint_contract_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_contract_analysis_agent.py   # or on stdin
python3 sharepoint_contract_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Agent: ContractAnalysisAgent
Purpose: Analyze, interpret, and summarize contracts stored in Azure File Storage
Data Sources: Azure File Storage (contracts/ folder), Azure OpenAI for analysis
Production Ready: Reads real documents, extracts text, performs AI-powered analysis

Supported formats: PDF, DOCX, TXT
Storage path: contracts/ folder in Azure File Storage
"""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/sharepoint_contract_analysis_agent",
    "version": "1.0.2",
    "display_name": "ContractAnalysis",
    "description": "Analyzes contract documents in Azure File Storage with Azure OpenAI \u2014 clause extraction, risk flagging, and comparison.",
    "author": "Bill Whalen",
    "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": ["AZURE_FILES_SHARE_NAME", "AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT", "AZURE_STORAGE_ACCOUNT_NAME"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import io
import re
from datetime import datetime
from typing import Optional, Dict, List, Any
from agents.basic_agent import BasicAgent

# Document processing imports
# Note: Auto-installation of missing packages is handled globally by function_app.py
# These imports will trigger auto-install if the packages are missing

# PDF support - try pypdf (modern) first, then PyPDF2 (legacy)
PDF_SUPPORT = False
pypdf_module = None

try:
    import pypdf
    pypdf_module = pypdf
    PDF_SUPPORT = True
except ImportError:
    try:
        import PyPDF2
        pypdf_module = PyPDF2
        PDF_SUPPORT = True
    except ImportError:
        logging.warning("PDF support disabled - pypdf/PyPDF2 not available")

# PDF generation support (reportlab)
PDF_GENERATION = False
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    PDF_GENERATION = True
except ImportError:
    logging.warning("PDF generation disabled - reportlab not available")

# DOCX support
DOCX_SUPPORT = False
DocxDocument = None

try:
    from docx import Document as DocxDocument
    DOCX_SUPPORT = True
except ImportError:
    logging.warning("DOCX support disabled - python-docx not available")

# Azure imports
try:
    from azure.identity import DefaultAzureCredential
    from azure.storage.fileshare import ShareFileClient, ShareDirectoryClient, ShareServiceClient
    from openai import AzureOpenAI
    from azure.identity import get_bearer_token_provider
    AZURE_SUPPORT = True
except ImportError as e:
    AZURE_SUPPORT = False
    logging.warning(f"Azure SDK not fully installed: {e}")


class ContractAnalysisAgent(BasicAgent):
    """
    Production contract analysis agent that reads documents from Azure File Storage
    and uses Azure OpenAI to extract clauses, generate summaries, and identify risks.

    Storage Structure:
        contracts/           - Root folder for all contracts
        contracts/templates/ - Standard contract templates for comparison
        contracts/analysis/  - Stored analysis results (optional)

    Supported Actions:
        - list_contracts: List available contracts in storage
        - analyze_contract: Full analysis with all extractions
        - extract_clauses: Extract specific clause categories
        - summarize_contract: Generate executive summary
        - identify_risks: Compare against standard terms
        - compare_contracts: Compare two contracts side-by-side
    """

    def __init__(self):
        self.name = 'ContractAnalysis'
        self.metadata = {
            "name": self.name,
            "description": "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "Action to perform. Use 'full_workup' when user says 'work on' a contract to run comprehensive analysis.",
                        "enum": [
                            "list_contracts",
                            "full_workup",
                            "analyze_contract",
                            "extract_clauses",
                            "summarize_contract",
                            "identify_risks",
                            "compare_contracts"
                        ]
                    },
                    "contract_name": {
                        "type": "string",
                        "description": "Name of the contract file in Azure storage (e.g., 'artist_agreement_2026.pdf')"
                    },
                    "contract_name_b": {
                        "type": "string",
                        "description": "Second contract name for comparison (used with compare_contracts action)"
                    },
                    "clause_types": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific clause types to extract: financial, rights, obligations, termination, exclusivity, territory, duration"
                    },
                    "summary_type": {
                        "type": "string",
                        "description": "Type of summary: executive (brief), detailed, or legal",
                        "enum": ["executive", "detailed", "legal"]
                    },
                    "audience": {
                        "type": "string",
                        "description": "Target audience for summary: legal, business, executive",
                        "enum": ["legal", "business", "executive"]
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

        # Initialize Azure clients
        self.storage_account = os.environ.get('AZURE_STORAGE_ACCOUNT_NAME', 'stov4bzgynnlvii')
        self.share_name = os.environ.get('AZURE_FILES_SHARE_NAME', 'azfrapp-ov4bzgynnlviiov4bzgynnlvii')
        self.contracts_folder = 'contracts'

        # Initialize OpenAI client
        self.openai_client = None
        self.deployment_name = os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-5.1-chat')
        self._init_openai_client()

    def _init_openai_client(self):
        """Initialize Azure OpenAI client with managed identity."""
        try:
            endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
            if not endpoint:
                logging.warning("AZURE_OPENAI_ENDPOINT not set")
                return

            credential = DefaultAzureCredential()
            token_provider = get_bearer_token_provider(
                credential,
                "https://cognitiveservices.azure.com/.default"
            )

            self.openai_client = AzureOpenAI(
                azure_endpoint=endpoint,
                azure_ad_token_provider=token_provider,
                api_version=os.environ.get('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
            )
            logging.info("ContractAnalysisAgent: OpenAI client initialized")
        except Exception as e:
            logging.error(f"Failed to initialize OpenAI client: {e}")

    def _get_share_service_client(self) -> Optional[ShareServiceClient]:
        """Get Azure File Share service client."""
        try:
            credential = DefaultAzureCredential()
            account_url = f"https://{self.storage_account}.file.core.windows.net"
            return ShareServiceClient(
                account_url=account_url,
                credential=credential,
                token_intent="backup"  # Required for token-based auth
            )
        except Exception as e:
            logging.error(f"Failed to create share service client: {e}")
            return None

    def _list_files_in_folder(self, folder_path: str = None) -> List[Dict]:
        """List all files in the contracts folder."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return []

            share_client = service_client.get_share_client(self.share_name)
            target_folder = folder_path or self.contracts_folder

            try:
                directory_client = share_client.get_directory_client(target_folder)
                files = []

                for item in directory_client.list_directories_and_files():
                    if not item.get('is_directory', False):
                        file_name = item['name']
                        # Get file properties
                        file_client = directory_client.get_file_client(file_name)
                        props = file_client.get_file_properties()

                        files.append({
                            "name": file_name,
                            "size_kb": round(props.size / 1024, 2),
                            "last_modified": props.last_modified.isoformat() if props.last_modified else None,
                            "path": f"{target_folder}/{file_name}"
                        })

                return files
            except Exception as e:
                if "ResourceNotFound" in str(e):
                    logging.info(f"Folder {target_folder} does not exist, will be created on first upload")
                    return []
                raise

        except Exception as e:
            logging.error(f"Error listing files: {e}")
            return []

    def _read_file_content(self, file_path: str) -> Optional[bytes]:
        """Read file content from Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return None

            share_client = service_client.get_share_client(self.share_name)
            file_client = share_client.get_file_client(file_path)

            download = file_client.download_file()
            return download.readall()

        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
            return None

    def _write_file_content(self, file_path: str, content: str) -> bool:
        """Write content to Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return False

            share_client = service_client.get_share_client(self.share_name)

            # Ensure directory exists
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                try:
                    dir_client = share_client.get_directory_client(dir_path)
                    dir_client.create_directory()
                except Exception:
                    pass  # Directory may already exist

            file_client = share_client.get_file_client(file_path)
            content_bytes = content.encode('utf-8')
            file_client.upload_file(content_bytes)

            logging.info(f"Successfully wrote file: {file_path}")
            return True

        except Exception as e:
            logging.error(f"Error writing file {file_path}: {e}")
            return False

    def _generate_download_url(self, file_path: str) -> str:
        """Generate a download URL for the file.

        Note: This storage account uses Entra ID authentication only (shared key access disabled).
        The returned URL requires authentication to access. Users can:
        1. Open in Azure Portal to download
        2. Use Azure Storage Explorer with their credentials
        3. Access via authenticated API calls
        """
        account_url = f"https://{self.storage_account}.file.core.windows.net"
        file_url = f"{account_url}/{self.share_name}/{file_path}"
        return file_url

    def _save_analysis_report(self, contract_name: str, analysis_data: Dict) -> Dict:
        """Save analysis report as professional PDF and return download info."""
        try:
            # Generate report filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = contract_name.rsplit('.', 1)[0]  # Remove extension
            report_name = f"{base_name}_analysis_{timestamp}.pdf"
            report_path = f"contracts/analysis/{report_name}"

            # Generate PDF report
            if PDF_GENERATION:
                pdf_bytes = self._generate_pdf_report(contract_name, analysis_data)
                if pdf_bytes:
                    # Write PDF to storage
                    if self._write_file_bytes(report_path, pdf_bytes):
                        download_url = self._generate_download_url(report_path)
                        return {
                            "saved": True,
                            "format": "PDF",
                            "report_name": report_name,
                            "report_path": report_path,
                            "download_url": download_url,
                            "size_kb": round(len(pdf_bytes) / 1024, 2)
                        }

            # Fallback to JSON if PDF generation fails
            report_name = f"{base_name}_analysis_{timestamp}.json"
            report_path = f"contracts/analysis/{report_name}"
            report_content = json.dumps(analysis_data, indent=2, default=str)

            if self._write_file_content(report_path, report_content):
                download_url = self._generate_download_url(report_path)
                return {
                    "saved": True,
                    "format": "JSON",
                    "report_name": report_name,
                    "report_path": report_path,
                    "download_url": download_url,
                    "size_kb": round(len(report_content) / 1024, 2)
                }
            else:
                return {"saved": False, "error": "Failed to write file"}

        except Exception as e:
            logging.error(f"Error saving analysis report: {e}")
            return {"saved": False, "error": str(e)}

    def _write_file_bytes(self, file_path: str, content: bytes) -> bool:
        """Write binary content to Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return False

            share_client = service_client.get_share_client(self.share_name)

            # Ensure directory exists
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                try:
                    dir_client = share_client.get_directory_client(dir_path)
                    dir_client.create_directory()
                except Exception:
                    pass  # Directory may already exist

            file_client = share_client.get_file_client(file_path)
            file_client.upload_file(content)

            logging.info(f"Successfully wrote binary file: {file_path}")
            return True

        except Exception as e:
            logging.error(f"Error writing binary file {file_path}: {e}")
            return False

    def _generate_pdf_report(self, contract_name: str, analysis_data: Dict) -> Optional[bytes]:
        """Generate a professional PDF analysis report."""
        if not PDF_GENERATION:
            return None

        try:
            # === DEBUG LOGGING: Dump structure of all data sections ===
            logging.info("=" * 60)
            logging.info("PDF GENERATION - DATA STRUCTURE ANALYSIS")
            logging.info("=" * 60)

            # Check executive_summary
            exec_summary = analysis_data.get('executive_summary', {})
            if isinstance(exec_summary, dict):
                logging.info(f"executive_summary keys: {list(exec_summary.keys())}")
                if exec_summary.get('parse_error'):
                    logging.error(f"executive_summary has PARSE ERROR")
                logging.info(f"  - summary length: {len(exec_summary.get('summary', ''))}")
                logging.info(f"  - risk_level: {exec_summary.get('risk_level', 'MISSING')}")
                logging.info(f"  - key_points count: {len(exec_summary.get('key_points', []))}")
            else:
                logging.error(f"executive_summary is NOT a dict: {type(exec_summary)}")

            # Check risk_assessment
            risk_assessment = analysis_data.get('risk_assessment', {})
            if isinstance(risk_assessment, dict):
                logging.info(f"risk_assessment keys: {list(risk_assessment.keys())}")
                if risk_assessment.get('parse_error'):
                    logging.error(f"risk_assessment has PARSE ERROR - raw: {risk_assessment.get('raw_analysis', '')[:500]}")
                logging.info(f"  - overall_risk_level: {risk_assessment.get('overall_risk_level', 'MISSING')}")
                logging.info(f"  - risk_score: {risk_assessment.get('risk_score', 'MISSING')}")
                logging.info(f"  - risks count: {len(risk_assessment.get('risks', []))}")
                logging.info(f"  - summary length: {len(risk_assessment.get('summary', ''))}")
            else:
                logging.error(f"risk_assessment is NOT a dict: {type(risk_assessment)}")

            # Check full_analysis
            full_analysis = analysis_data.get('full_analysis', {})
            if isinstance(full_analysis, dict):
                logging.info(f"full_analysis keys: {list(full_analysis.keys())}")
                if full_analysis.get('parse_error'):
                    logging.error(f"full_analysis has PARSE ERROR - raw: {full_analysis.get('raw_analysis', '')[:500]}")
                logging.info(f"  - contract_type: {full_analysis.get('contract_type', 'MISSING')}")
                logging.info(f"  - parties count: {len(full_analysis.get('parties', []))}")
                logging.info(f"  - financial_terms keys: {list(full_analysis.get('financial_terms', {}).keys()) if isinstance(full_analysis.get('financial_terms'), dict) else 'NOT DICT'}")
            else:
                logging.error(f"full_analysis is NOT a dict: {type(full_analysis)}")

            # Check extracted_clauses
            extracted_clauses = analysis_data.get('extracted_clauses', {})
            if isinstance(extracted_clauses, dict):
                logging.info(f"extracted_clauses keys: {list(extracted_clauses.keys())}")
                if extracted_clauses.get('parse_error'):
                    logging.error(f"extracted_clauses has PARSE ERROR")

            logging.info("=" * 60)

            # Create PDF in memory
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                leftMargin=0.75*inch,
                rightMargin=0.75*inch,
                topMargin=0.75*inch,
                bottomMargin=0.75*inch
            )

            # Define styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=20,
                spaceAfter=20,
                alignment=TA_CENTER,
                textColor=colors.HexColor('#1a365d')
            )
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                spaceBefore=20,
                spaceAfter=10,
                textColor=colors.HexColor('#2c5282')
            )
            subheading_style = ParagraphStyle(
                'CustomSubHeading',
                parent=styles['Heading3'],
                fontSize=12,
                spaceBefore=12,
                spaceAfter=6,
                textColor=colors.HexColor('#4a5568')
            )
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=8,
                leading=14,
                alignment=TA_JUSTIFY
            )
            bullet_style = ParagraphStyle(
                'CustomBullet',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=4,
                leftIndent=20,
                bulletIndent=10
            )
            risk_high = ParagraphStyle(
                'RiskHigh',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#c53030'),
                spaceAfter=8
            )
            risk_medium = ParagraphStyle(
                'RiskMedium',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#dd6b20'),
                spaceAfter=8
            )
            risk_low = ParagraphStyle(
                'RiskLow',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#38a169'),
                spaceAfter=8
            )

            story = []

            # Title
            story.append(Paragraph("CONTRACT ANALYSIS REPORT", title_style))
            story.append(Spacer(1, 0.1*inch))

            # Contract info header
            story.append(Paragraph(f"<b>Contract:</b> {contract_name}", body_style))
            story.append(Paragraph(f"<b>Analysis Date:</b> {analysis_data.get('analyzed_at', datetime.now().isoformat())}", body_style))
            story.append(Spacer(1, 0.2*inch))

            # Horizontal line
            story.append(Table([['']], colWidths=[7*inch], rowHeights=[2]))
            story[-1].setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c5282'))]))
            story.append(Spacer(1, 0.2*inch))

            # Executive Summary Section
            exec_summary = analysis_data.get('executive_summary', {})
            if exec_summary:
                story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

                if isinstance(exec_summary, dict):
                    summary_text = exec_summary.get('summary', '')
                    if summary_text:
                        # Use larger max_length for executive summary - don't truncate
                        story.append(Paragraph(self._clean_text(summary_text, max_length=2000), body_style))

                    # Risk Level Box
                    risk_level = exec_summary.get('risk_level', 'unknown').upper()
                    risk_style = risk_high if risk_level == 'HIGH' else (risk_medium if risk_level == 'MEDIUM' else risk_low)
                    story.append(Spacer(1, 0.1*inch))
                    story.append(Paragraph(f"<b>Overall Risk Level: {risk_level}</b>", risk_style))

                    # Key Points
                    key_points = exec_summary.get('key_points', [])
                    if key_points:
                        story.append(Paragraph("<b>Key Points:</b>", subheading_style))
                        for point in key_points[:10]:  # Limit to 10 points
                            if isinstance(point, dict):
                                # Format dict with point and clickable ref
                                point_text = point.get('point', '')
                                point_ref = point.get('ref', '')
                                clickable_ref = self._format_clickable_ref(point_ref, analysis_data.get('_contract_text', '')) if point_ref else ""
                                formatted = f"{self._clean_text(point_text, max_length=300)} {clickable_ref}"
                            else:
                                formatted = self._clean_text(str(point), max_length=300)
                            story.append(Paragraph(f"* {formatted}", bullet_style))

                    # Recommendation
                    recommendation = exec_summary.get('recommendation', '')
                    if recommendation:
                        story.append(Spacer(1, 0.1*inch))
                        story.append(Paragraph(f"<b>Recommendation:</b> {self._clean_text(recommendation, max_length=1000)}", body_style))

            story.append(PageBreak())

            # Risk Assessment Section
            risk_assessment = analysis_data.get('risk_assessment', {})
            story.append(Paragraph("RISK ASSESSMENT", heading_style))

            if isinstance(risk_assessment, dict):
                # Check for parse error
                if risk_assessment.get('parse_error'):
                    story.append(Paragraph(
                        "<b><font color='red'>Warning: Risk assessment data extraction encountered issues.</font></b>",
                        body_style
                    ))
                    # Show raw analysis if available
                    raw_analysis = risk_assessment.get('raw_analysis', '')
                    if raw_analysis and len(raw_analysis) > 50:
                        story.append(Paragraph("<b>Raw Analysis Output:</b>", subheading_style))
                        # Show first 2000 chars of raw analysis
                        story.append(Paragraph(self._clean_text(raw_analysis[:2000], max_length=2000), body_style))
                else:
                    # Overall risk
                    overall_risk = risk_assessment.get('overall_risk_level', 'Unknown').upper()
                    risk_score = risk_assessment.get('risk_score', 'N/A')
                    risk_style = risk_high if overall_risk == 'HIGH' else (risk_medium if overall_risk == 'MEDIUM' else risk_low)
                    story.append(Paragraph(f"<b>Risk Level: {overall_risk} | Score: {risk_score}/100</b>", risk_style))

                    # Summary
                    risk_summary = risk_assessment.get('summary', '')
                    if risk_summary:
                        story.append(Paragraph(self._clean_text(risk_summary, max_length=1000), body_style))
                    else:
                        story.append(Paragraph("<i>No risk summary available.</i>", body_style))

                    # Individual risks
                    risks = risk_assessment.get('risks', [])
                    if risks:
                        story.append(Paragraph("<b>Identified Risks:</b>", subheading_style))

                        # Create table cell style for wrapping text
                        cell_style = ParagraphStyle(
                            'CellStyle',
                            parent=styles['Normal'],
                            fontSize=8,
                            leading=10,
                            spaceAfter=0
                        )
                        header_cell_style = ParagraphStyle(
                            'HeaderCellStyle',
                            parent=styles['Normal'],
                            fontSize=9,
                            leading=11,
                            textColor=colors.white,
                            fontName='Helvetica-Bold'
                        )

                        # Build header row with Paragraphs
                        risk_data = [[
                            Paragraph('Category', header_cell_style),
                            Paragraph('Severity', header_cell_style),
                            Paragraph('Description', header_cell_style)
                        ]]

                        for risk in risks[:10]:  # Limit to 10 risks
                            if isinstance(risk, dict):
                                desc_text = self._clean_text(risk.get('description', 'N/A'), max_length=300)
                                risk_data.append([
                                    Paragraph(risk.get('category', 'N/A'), cell_style),
                                    Paragraph(risk.get('severity', 'N/A').upper(), cell_style),
                                    Paragraph(desc_text, cell_style)
                                ])

                        if len(risk_data) > 1:
                            # Adjusted widths: Category 1", Severity 0.7", Description 5"
                            risk_table = Table(risk_data, colWidths=[1*inch, 0.7*inch, 5*inch])
                            risk_table.setStyle(TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
                                ('FONTSIZE', (0, 0), (-1, -1), 8),
                                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
                                ('TOPPADDING', (0, 0), (-1, -1), 4),
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                                ('LEFTPADDING', (0, 0), (-1, -1), 4),
                                ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                            ]))
                            story.append(risk_table)
                    else:
                        story.append(Paragraph("<i>No individual risks identified.</i>", body_style))

                    # Artist-favorable terms from risk assessment
                    artist_favorable = risk_assessment.get('artist_favorable_terms', [])
                    if artist_favorable:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Artist-Favorable Terms (Label Concerns):</b>", subheading_style))
                        for term in artist_favorable[:6]:
                            if isinstance(term, dict):
                                term_text = term.get('term', 'N/A')
                                label_impact = term.get('label_impact', '')
                                ref = term.get('ref', '')
                                impact_text = f" - {label_impact}" if label_impact else ""
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(term_text))}{impact_text}{ref_text}", bullet_style))

                    # Negotiation points
                    negotiation = risk_assessment.get('negotiation_points', risk_assessment.get('negotiation_priorities', []))
                    if negotiation:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Recommended Negotiation Points:</b>", subheading_style))
                        for point in negotiation[:8]:
                            if isinstance(point, dict):
                                priority_text = point.get('priority', point.get('point', str(point)))
                                ref = point.get('ref', '')
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(priority_text))}{ref_text}", bullet_style))
                            else:
                                story.append(Paragraph(f"* {self._clean_text(str(point))}", bullet_style))

                    # Deal breakers
                    deal_breakers = risk_assessment.get('deal_breakers', [])
                    if deal_breakers:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Potential Deal Breakers:</b>", subheading_style))
                        for item in deal_breakers[:5]:
                            if isinstance(item, dict):
                                issue = item.get('issue', 'N/A')
                                ref = item.get('ref', '')
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(issue))}{ref_text}", bullet_style))
                            else:
                                story.append(Paragraph(f"* {self._clean_text(str(item))}", bullet_style))
            else:
                story.append(Paragraph("<i>Risk assessment data not available.</i>", body_style))

            story.append(PageBreak())

            # Full Analysis Section
            full_analysis = analysis_data.get('full_analysis', {})
            logging.info(f"PDF Generation - full_analysis keys: {list(full_analysis.keys()) if isinstance(full_analysis, dict) else 'NOT DICT'}")

            story.append(Paragraph("DETAILED CONTRACT ANALYSIS", heading_style))

            if isinstance(full_analysis, dict):
                # Check for parse error
                if full_analysis.get('parse_error'):
                    story.append(Paragraph(
                        "<b><font color='red'>Warning: Detailed analysis data extraction encountered issues.</font></b>",
                        body_style
                    ))
                    # Show raw analysis if available
                    raw_analysis = full_analysis.get('raw_analysis', '')
                    if raw_analysis and len(raw_analysis) > 50:
                        story.append(Paragraph("<b>Raw Analysis Output:</b>", subheading_style))
                        # Show first 3000 chars of raw analysis
                        story.append(Paragraph(self._clean_text(raw_analysis[:3000], max_length=3000), body_style))
                else:
                    # Contract Type
                    contract_type = full_analysis.get('contract_type', 'Not identified')
                    logging.info(f"PDF Generation - contract_type: {contract_type}")
                    story.append(Paragraph(f"<b>Contract Type:</b> {contract_type}", body_style))

                    # Get contract text for snippets
                    contract_text = analysis_data.get('_contract_text', '')
                    logging.info(f"PDF Generation - contract_text length: {len(contract_text) if contract_text else 0}")

                    # Parties
                    parties = full_analysis.get('parties', [])
                    logging.info(f"PDF Generation - parties count: {len(parties) if parties else 0}")
                    if parties:
                        story.append(Paragraph("<b>Parties:</b>", subheading_style))
                        for party in parties:
                            if isinstance(party, dict):
                                try:
                                    party_ref = party.get('ref', '')
                                    clickable_ref = self._format_clickable_ref(party_ref, contract_text) if party_ref else ""
                                    story.append(Paragraph(f"* {party.get('name', 'N/A')} - {party.get('role', 'N/A')} {clickable_ref}", bullet_style))
                                except Exception as e:
                                    logging.error(f"Error rendering party: {e}")
                                    story.append(Paragraph(f"* {party.get('name', 'N/A')} - {party.get('role', 'N/A')}", bullet_style))

                    # Term - handle both string and dict formats
                    term = full_analysis.get('term_duration', '')
                    if term:
                        if isinstance(term, dict):
                            term_val = term.get('value', 'N/A')
                            term_ref = term.get('ref', '')
                            clickable_ref = self._format_clickable_ref(term_ref, contract_text) if term_ref else ""
                            story.append(Paragraph(f"<b>Term:</b> {self._clean_text(str(term_val))} {clickable_ref}", body_style))
                        else:
                            story.append(Paragraph(f"<b>Term:</b> {self._clean_text(str(term))}", body_style))

                    # Effective Date
                    effective_date = full_analysis.get('effective_date', {})
                    if effective_date and isinstance(effective_date, dict):
                        date_val = effective_date.get('value', '')
                        if date_val:
                            date_ref = effective_date.get('ref', '')
                            clickable_ref = self._format_clickable_ref(date_ref, contract_text) if date_ref else ""
                            story.append(Paragraph(f"<b>Effective Date:</b> {self._clean_text(str(date_val))} {clickable_ref}", body_style))

                    # Financial Terms
                    financial = full_analysis.get('financial_terms', {})
                    if financial and isinstance(financial, dict):
                        story.append(Paragraph("<b>Financial Terms:</b>", subheading_style))
                        # Use the formatter for complex nested values
                        if financial.get('advances'):
                            formatted_advances = self._format_value_for_pdf(financial.get('advances'))
                            story.append(Paragraph(f"* Advances: {formatted_advances}", bullet_style))
                        if financial.get('royalty_rates'):
                            formatted_royalties = self._format_value_for_pdf(financial.get('royalty_rates'))
                            story.append(Paragraph(f"* Royalty Rates: {formatted_royalties}", bullet_style))
                        if financial.get('payment_schedule'):
                            formatted_schedule = self._format_value_for_pdf(financial.get('payment_schedule'))
                            story.append(Paragraph(f"* Payment Schedule: {formatted_schedule}", bullet_style))
                        if financial.get('label_investment'):
                            formatted_investment = self._format_value_for_pdf(financial.get('label_investment'))
                            story.append(Paragraph(f"* Label Investment: {formatted_investment}", bullet_style))
                        if financial.get('recoupment_terms'):
                            formatted_recoup = self._format_value_for_pdf(financial.get('recoupment_terms'))
                            story.append(Paragraph(f"* Recoupment: {formatted_recoup}", bullet_style))

                    # Rights Secured (AI returns 'rights_secured' not 'rights_granted')
                    rights = full_analysis.get('rights_secured', []) or full_analysis.get('rights_granted', [])
                    if rights:
                        story.append(Paragraph("<b>Rights Secured:</b>", subheading_style))
                        for right in rights[:8]:
                            if isinstance(right, dict):
                                exclusivity = "Exclusive" if right.get('exclusivity') else "Non-exclusive"
                                right_desc = right.get('right', '') or right.get('description', 'N/A')
                                scope = right.get('scope', '')
                                duration = right.get('duration', '')
                                ref = right.get('ref', '')

                                details = [f"{exclusivity}"]
                                if scope:
                                    details.append(f"Territory: {scope}")
                                if duration:
                                    details.append(f"Duration: {duration}")

                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(right_desc))} ({', '.join(details)}) {clickable_ref}",
                                    bullet_style
                                ))

                    # Artist Obligations
                    artist_obligations = full_analysis.get('artist_obligations', [])
                    if artist_obligations:
                        story.append(Paragraph("<b>Artist Obligations:</b>", subheading_style))
                        for obligation in artist_obligations[:6]:
                            if isinstance(obligation, dict):
                                obl_text = obligation.get('obligation', 'N/A')
                                deadline = obligation.get('deadline', '')
                                ref = obligation.get('ref', '')

                                deadline_text = f" (Deadline: {deadline})" if deadline else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(obl_text))}{deadline_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Label Obligations
                    label_obligations = full_analysis.get('label_obligations', [])
                    if label_obligations:
                        story.append(Paragraph("<b>Label Obligations:</b>", subheading_style))
                        for obligation in label_obligations[:6]:
                            if isinstance(obligation, dict):
                                obl_text = obligation.get('obligation', 'N/A')
                                impact = obligation.get('financial_impact', '')
                                ref = obligation.get('ref', '')

                                impact_text = f" (Cost: {impact})" if impact else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(obl_text))}{impact_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Label Protections
                    protections = full_analysis.get('label_protections', [])
                    if protections:
                        story.append(Paragraph("<b>Label Protections:</b>", subheading_style))
                        for protection in protections[:6]:
                            if isinstance(protection, dict):
                                clause = protection.get('clause', 'N/A')
                                ref = protection.get('ref', '')
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(clause))} {clickable_ref}", bullet_style))

                    # Termination Clauses
                    termination = full_analysis.get('termination_clauses', [])
                    if termination:
                        story.append(Paragraph("<b>Termination Provisions:</b>", subheading_style))
                        for term_clause in termination[:6]:
                            if isinstance(term_clause, dict):
                                trigger = term_clause.get('trigger', 'N/A')
                                who = term_clause.get('who_can_trigger', '')
                                impact = term_clause.get('label_impact', '')
                                ref = term_clause.get('ref', '')

                                who_text = f" (By: {who})" if who else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(trigger))}{who_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Artist-Favorable Terms (risks to label)
                    artist_favorable = full_analysis.get('artist_favorable_terms', [])
                    if artist_favorable:
                        story.append(Paragraph("<b>Artist-Favorable Terms (Label Concerns):</b>", subheading_style))
                        for term in artist_favorable[:5]:
                            if isinstance(term, dict):
                                term_desc = term.get('term', 'N/A')
                                concern = term.get('concern', '')
                                ref = term.get('ref', '')

                                concern_text = f" - {concern}" if concern else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(term_desc))}{concern_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Overall Assessment
                    assessment = full_analysis.get('overall_assessment', '')
                    if assessment:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Overall Assessment:</b>", subheading_style))
                        story.append(Paragraph(self._clean_text(str(assessment)), body_style))
            else:
                story.append(Paragraph("<i>Detailed analysis data not available or could not be parsed.</i>", body_style))

            # SOURCE CONTRACT SECTION - Appended with page anchors for clickable references
            contract_text = analysis_data.get('_contract_text', '')
            if contract_text:
                story.append(PageBreak())
                story.append(Paragraph("SOURCE CONTRACT", heading_style))
                story.append(Paragraph(
                    "<i>The original contract text is included below. Click any page reference in the analysis above to jump directly to that location.</i>",
                    body_style
                ))
                story.append(Spacer(1, 0.2*inch))

                # Style for contract text (smaller, monospace-like)
                contract_style = ParagraphStyle(
                    'ContractText',
                    parent=styles['Normal'],
                    fontSize=9,
                    spaceAfter=6,
                    leading=12,
                    leftIndent=10,
                    rightIndent=10
                )

                # Split contract by page markers and create anchors
                # Look for [PAGE N] markers in the text
                page_pattern = re.compile(r'\[PAGE\s*(\d+)\]', re.IGNORECASE)

                # Split text by page markers, keeping the markers
                parts = page_pattern.split(contract_text)

                if len(parts) > 1:
                    # We have page markers
                    current_page = None
                    for i, part in enumerate(parts):
                        if i % 2 == 1:  # This is a page number
                            current_page = part
                            # Create anchor for this page
                            anchor_name = f"contract_page_{current_page}"
                            story.append(Spacer(1, 0.15*inch))
                            # Page header with anchor
                            story.append(Paragraph(
                                f'<a name="{anchor_name}"/><b>--- PAGE {current_page} ---</b>',
                                subheading_style
                            ))
                        else:
                            # This is content
                            if part.strip():
                                # Clean and split into paragraphs
                                paragraphs = part.strip().split('\n\n')
                                for para in paragraphs:
                                    if para.strip():
                                        clean_para = self._clean_text(para.strip(), max_length=2000)
                                        if clean_para:
                                            story.append(Paragraph(clean_para, contract_style))
                else:
                    # No page markers - create anchors for every ~2000 chars as "pages"
                    chunk_size = 2000
                    chunks = [contract_text[i:i+chunk_size] for i in range(0, len(contract_text), chunk_size)]
                    for page_num, chunk in enumerate(chunks, 1):
                        anchor_name = f"contract_page_{page_num}"
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph(
                            f'<a name="{anchor_name}"/><b>--- PAGE {page_num} ---</b>',
                            subheading_style
                        ))
                        clean_chunk = self._clean_text(chunk.strip(), max_length=2500)
                        if clean_chunk:
                            story.append(Paragraph(clean_chunk, contract_style))

            # Footer
            story.append(Spacer(1, 0.5*inch))
            story.append(Table([['']], colWidths=[7*inch], rowHeights=[2]))
            story[-1].setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c5282'))]))
            story.append(Spacer(1, 0.1*inch))

            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                textColor=colors.grey,
                alignment=TA_CENTER
            )
            story.append(Paragraph(
                f"Generated by ContractAnalysis Agent | {datetime.now().strftime('%B %d, %Y at %I:%M %p')}",
                footer_style
            ))
            story.append(Paragraph(
                "This analysis is for informational purposes only and does not constitute legal advice.",
                footer_style
            ))

            # Build PDF
            doc.build(story)
            pdf_bytes = buffer.getvalue()
            buffer.close()

            logging.info(f"Generated PDF report: {len(pdf_bytes)} bytes")
            return pdf_bytes

        except Exception as e:
            logging.error(f"Error generating PDF report: {e}")
            return None

    def _clean_text(self, text: str, max_length: int = 500) -> str:
        """Clean text for PDF rendering - escape special characters and normalize Unicode."""
        if not text:
            return ""
        text = str(text)

        # Normalize Unicode characters that don't render in standard PDF fonts
        unicode_replacements = {
            '\u2011': '-',   # Non-breaking hyphen → regular hyphen
            '\u2010': '-',   # Hyphen → regular hyphen
            '\u2012': '-',   # Figure dash → regular hyphen
            '\u2013': '-',   # En-dash → regular hyphen
            '\u2014': '-',   # Em-dash → regular hyphen
            '\u2015': '-',   # Horizontal bar → regular hyphen
            '\u2018': "'",   # Left single quote → apostrophe
            '\u2019': "'",   # Right single quote → apostrophe
            '\u201a': "'",   # Single low quote → apostrophe
            '\u201b': "'",   # Single high-reversed quote → apostrophe
            '\u201c': '"',   # Left double quote → regular quote
            '\u201d': '"',   # Right double quote → regular quote
            '\u201e': '"',   # Double low quote → regular quote
            '\u201f': '"',   # Double high-reversed quote → regular quote
            '\u2022': '*',   # Bullet → asterisk
            '\u2023': '>',   # Triangular bullet → greater than
            '\u2024': '.',   # One dot leader → period
            '\u2025': '..',  # Two dot leader → two periods
            '\u2026': '...', # Ellipsis → three periods
            '\u2027': '-',   # Hyphenation point → hyphen
            '\u2032': "'",   # Prime → apostrophe
            '\u2033': '"',   # Double prime → quote
            '\u2039': '<',   # Single left angle quote
            '\u203a': '>',   # Single right angle quote
            '\u00ab': '<<',  # Left double angle quote
            '\u00bb': '>>',  # Right double angle quote
            '\u00a0': ' ',   # Non-breaking space → regular space
            '\u200b': '',    # Zero-width space → remove
            '\u200c': '',    # Zero-width non-joiner → remove
            '\u200d': '',    # Zero-width joiner → remove
            '\ufeff': '',    # BOM → remove
            '\u00b7': '*',   # Middle dot → asterisk
            '\u2212': '-',   # Minus sign → hyphen
            '\u00d7': 'x',   # Multiplication sign → x
            '\u00f7': '/',   # Division sign → slash
            '\u2248': '~',   # Almost equal → tilde
            '\u2260': '!=',  # Not equal → !=
            '\u2264': '<=',  # Less than or equal
            '\u2265': '>=',  # Greater than or equal
            '\u00b0': ' deg', # Degree symbol
            '\u00a9': '(c)', # Copyright
            '\u00ae': '(R)', # Registered
            '\u2122': '(TM)', # Trademark
        }

        for unicode_char, replacement in unicode_replacements.items():
            text = text.replace(unicode_char, replacement)

        # Replace any remaining non-ASCII characters that might cause issues
        # Keep basic extended ASCII (accented letters) but remove other oddities
        cleaned_chars = []
        for char in text:
            if ord(char) < 128:  # Standard ASCII
                cleaned_chars.append(char)
            elif ord(char) < 256:  # Extended ASCII (accented chars) - keep these
                cleaned_chars.append(char)
            else:  # Other Unicode - replace with space or skip
                cleaned_chars.append(' ')
        text = ''.join(cleaned_chars)

        # Clean up multiple spaces
        while '  ' in text:
            text = text.replace('  ', ' ')

        # Replace problematic characters for reportlab XML
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('\n', ' ')
        text = text.replace('\r', '')

        # Limit length to prevent overflow
        if max_length and len(text) > max_length:
            text = text[:max_length - 3] + "..."
        return text.strip()

    def _format_clickable_ref(self, ref_text: str, contract_text: str = '') -> str:
        """Format a reference string as a clickable internal PDF link with snippet.

        Converts refs like "Page 3, Section 4.1" to clickable links that jump
        to the corresponding page in the appended contract text.
        Includes a short snippet from the referenced page for context.
        """
        if not ref_text or ref_text == 'N/A':
            return ""

        # Extract page number from reference (e.g., "Page 3" or "Pages 3-4")
        page_match = re.search(r'[Pp]age[s]?\s*(\d+)', str(ref_text))
        if page_match:
            page_num = page_match.group(1)
            anchor_name = f"contract_page_{page_num}"
            clean_ref = self._clean_text(str(ref_text), max_length=100)

            # Extract a snippet from the referenced page if contract text is available
            snippet = ""
            if contract_text:
                # Find the page marker and extract text after it
                page_pattern = re.compile(rf'\[PAGE\s*{page_num}\](.*?)(?:\[PAGE\s*\d+\]|$)', re.IGNORECASE | re.DOTALL)
                match = page_pattern.search(contract_text)
                if match:
                    page_content = match.group(1).strip()
                    # Get first 80 chars as snippet, clean it up
                    if page_content:
                        snippet_text = page_content[:120].replace('\n', ' ').strip()
                        # Truncate at word boundary
                        if len(snippet_text) >= 80:
                            last_space = snippet_text[:80].rfind(' ')
                            if last_space > 40:
                                snippet_text = snippet_text[:last_space]
                        snippet = self._clean_text(snippet_text, max_length=80)

            # Build the clickable reference with optional snippet
            if snippet:
                return f'<a href="#{anchor_name}" color="blue"><i>(Ref: {clean_ref})</i></a> <font size="8" color="gray">["{snippet}..."]</font>'
            else:
                return f'<a href="#{anchor_name}" color="blue"><i>(Ref: {clean_ref})</i></a>'
        else:
            # No page number found, just return plain ref
            clean_ref = self._clean_text(str(ref_text), max_length=100)
            return f"<i>(Ref: {clean_ref})</i>"

    def _format_value_for_pdf(self, value: Any, indent: int = 0) -> str:
        """Format a value (potentially nested dict/list) into readable text for PDF."""
        if value is None:
            return "N/A"

        if isinstance(value, str):
            return self._clean_text(value, max_length=None)

        if isinstance(value, (int, float, bool)):
            return str(value)

        if isinstance(value, list):
            if not value:
                return "None"
            # For simple lists, join with commas
            if all(isinstance(item, str) for item in value):
                return ", ".join(str(item) for item in value[:5])  # Limit to 5 items
            # For complex lists, format each item
            parts = []
            for item in value[:5]:
                parts.append(self._format_value_for_pdf(item, indent + 1))
            return "; ".join(parts)

        if isinstance(value, dict):
            # Format dict as readable key-value pairs
            parts = []
            for k, v in value.items():
                # Clean up key name (replace underscores, capitalize)
                key_name = k.replace('_', ' ').title()
                formatted_value = self._format_value_for_pdf(v, indent + 1)
                if formatted_value and formatted_value != "N/A":
                    parts.append(f"{key_name}: {formatted_value}")
            return "; ".join(parts) if parts else "N/A"

        return str(value)

    def _extract_text_from_pdf(self, content: bytes) -> str:
        """Extract text from PDF content using pypdf or PyPDF2.

        Includes clear page markers for document reference tracking.
        """
        if not PDF_SUPPORT or pypdf_module is None:
            return "[ERROR: PDF library not available. Install with: pip install pypdf]"

        try:
            pdf_file = io.BytesIO(content)
            pdf_reader = pypdf_module.PdfReader(pdf_file)

            text_parts = []
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    # Clear page markers for AI to reference
                    text_parts.append(f"[PAGE {page_num + 1}]\n{page_text}\n[END PAGE {page_num + 1}]")

            return "\n\n".join(text_parts)
        except Exception as e:
            logging.error(f"PDF extraction error: {e}")
            return f"[ERROR: Failed to extract PDF text: {e}]"

    def _extract_text_from_docx(self, content: bytes) -> str:
        """Extract text from DOCX content."""
        if not DOCX_SUPPORT or DocxDocument is None:
            return "[ERROR: python-docx not available. Install with: pip install python-docx]"

        try:
            doc_file = io.BytesIO(content)
            doc = DocxDocument(doc_file)

            text_parts = []
            for para in doc.paragraphs:
                if para.text.strip():
                    text_parts.append(para.text)

            # Also extract tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join(cell.text.strip() for cell in row.cells)
                    if row_text.strip():
                        text_parts.append(row_text)

            return "\n\n".join(text_parts)
        except Exception as e:
            logging.error(f"DOCX extraction error: {e}")
            return f"[ERROR: Failed to extract DOCX text: {e}]"

    def _extract_text(self, file_path: str, content: bytes) -> str:
        """Extract text based on file extension."""
        ext = file_path.lower().split('.')[-1]

        if ext == 'pdf':
            return self._extract_text_from_pdf(content)
        elif ext in ['docx', 'doc']:
            return self._extract_text_from_docx(content)
        elif ext == 'txt':
            return content.decode('utf-8', errors='ignore')
        else:
            return f"[ERROR: Unsupported file format: {ext}. Supported: pdf, docx, txt]"

    def _extract_json_from_response(self, response: str) -> Dict:
        """Extract JSON from AI response, handling various formats."""
        if not response:
            logging.error("_extract_json_from_response: Empty response received")
            return {"parse_error": True, "raw_analysis": response, "error_type": "empty_response"}

        # Clean up common issues in AI responses
        cleaned_response = response.strip()

        # Remove control characters that can break JSON parsing
        cleaned_response = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', cleaned_response)

        # Check for truncated JSON (common when hitting token limits)
        # If it starts with { but doesn't end with }, try to repair it
        if cleaned_response.startswith('{') and not cleaned_response.rstrip().endswith('}'):
            logging.warning("_extract_json_from_response: Detected possibly truncated JSON, attempting repair...")
            # Try to find the last complete key-value pair and close the JSON
            repaired = self._repair_truncated_json(cleaned_response)
            if repaired:
                try:
                    result = json.loads(repaired)
                    logging.info(f"_extract_json_from_response: Parsed from repaired truncated JSON, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e:
                    logging.warning(f"_extract_json_from_response: Repaired JSON still invalid: {e}")

        # Try 1: Look for ```json code block
        json_match = re.search(r'```json\s*(.*?)\s*```', cleaned_response, re.DOTALL)
        if json_match:
            try:
                result = json.loads(json_match.group(1))
                logging.info(f"_extract_json_from_response: Parsed from ```json block, keys: {list(result.keys())}")
                return result
            except json.JSONDecodeError as e:
                logging.warning(f"_extract_json_from_response: Failed to parse ```json block: {e}")

        # Try 2: Look for ``` code block without json tag
        code_match = re.search(r'```\s*(.*?)\s*```', cleaned_response, re.DOTALL)
        if code_match:
            code_content = code_match.group(1).strip()
            if code_content.startswith('{'):
                try:
                    result = json.loads(code_content)
                    logging.info(f"_extract_json_from_response: Parsed from ``` block, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e:
                    logging.warning(f"_extract_json_from_response: Failed to parse ``` block: {e}")

        # Try 3: Look for first { to last } (the JSON object)
        first_brace = cleaned_response.find('{')
        last_brace = cleaned_response.rfind('}')
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            json_str = cleaned_response[first_brace:last_brace + 1]
            try:
                result = json.loads(json_str)
                logging.info(f"_extract_json_from_response: Parsed from braces, keys: {list(result.keys())}")
                return result
            except json.JSONDecodeError as e:
                # Try to fix common JSON issues
                logging.warning(f"_extract_json_from_response: Initial brace parse failed: {e}")

                # Apply multiple fixes in sequence
                fixed_json = json_str

                # Fix 1: Remove trailing commas before ] or }
                fixed_json = re.sub(r',\s*([}\]])', r'\1', fixed_json)

                # Fix 2: Fix missing commas between } and { or ] and [
                fixed_json = re.sub(r'}\s*{', '},{', fixed_json)
                fixed_json = re.sub(r']\s*\[', '],[', fixed_json)

                # Fix 3: Fix missing commas between } and "
                fixed_json = re.sub(r'}\s*"', '},"', fixed_json)
                fixed_json = re.sub(r']\s*"', '],"', fixed_json)

                # Fix 4: Fix newlines inside strings (convert to spaces)
                # This is tricky - need to only fix inside strings
                # For now, just remove literal newlines that aren't escaped
                fixed_json = re.sub(r'(?<!\\)\n', ' ', fixed_json)

                try:
                    result = json.loads(fixed_json)
                    logging.info(f"_extract_json_from_response: Parsed after JSON fixes, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e2:
                    logging.warning(f"_extract_json_from_response: JSON fixes didn't help: {e2}")

                # Try to find and fix the specific position of the error
                try:
                    # Sometimes the AI includes extra text after the JSON
                    # Try parsing incrementally to find where valid JSON ends
                    for end_pos in range(last_brace, first_brace, -1):
                        if cleaned_response[end_pos] == '}':
                            try:
                                result = json.loads(cleaned_response[first_brace:end_pos + 1])
                                logging.info(f"_extract_json_from_response: Parsed with truncated end, keys: {list(result.keys())}")
                                return result
                            except json.JSONDecodeError:
                                continue
                except Exception:
                    pass

        # Try 4: Direct parse (if entire response is JSON)
        try:
            result = json.loads(cleaned_response)
            logging.info(f"_extract_json_from_response: Parsed directly, keys: {list(result.keys())}")
            return result
        except json.JSONDecodeError as e:
            logging.warning(f"_extract_json_from_response: Direct parse failed: {e}")

        # Failed to parse - log detailed error info
        logging.error(f"_extract_json_from_response: ALL PARSE ATTEMPTS FAILED")
        logging.error(f"Response length: {len(response)}")
        logging.error(f"Response starts with: {response[:200]}")
        logging.error(f"Response ends with: {response[-200:] if len(response) > 200 else response}")

        return {"parse_error": True, "raw_analysis": response, "error_type": "json_parse_failed"}

    def _repair_truncated_json(self, json_str: str) -> Optional[str]:
        """Attempt to repair truncated JSON by closing unclosed brackets/braces."""
        try:
            # Track the nesting level
            stack = []
            in_string = False
            escape_next = False
            last_complete_pos = 0

            for i, char in enumerate(json_str):
                if escape_next:
                    escape_next = False
                    continue

                if char == '\\' and in_string:
                    escape_next = True
                    continue

                if char == '"' and not escape_next:
                    in_string = not in_string
                    continue

                if in_string:
                    continue

                if char == '{':
                    stack.append('}')
                elif char == '[':
                    stack.append(']')
                elif char in '}]':
                    if stack and stack[-1] == char:
                        stack.pop()
                        last_complete_pos = i + 1

                # Track positions after complete key-value pairs
                if char == ',' and not in_string:
                    last_complete_pos = i + 1

            # If we're still in a string, try to close it
            if in_string:
                json_str = json_str + '"'

            # Find the last complete structure and close everything
            # Try to truncate at the last comma and close
            if stack:
                # Find last comma outside of string
                truncate_pos = json_str.rfind(',')
                if truncate_pos > 0:
                    # Truncate at last comma and close all open brackets
                    repaired = json_str[:truncate_pos]
                    repaired += ''.join(reversed(stack))
                    return repaired
                else:
                    # Just close all open brackets
                    return json_str + ''.join(reversed(stack))

            return json_str

        except Exception as e:
            logging.warning(f"_repair_truncated_json failed: {e}")
            return None

    def _call_openai(self, system_prompt: str, user_prompt: str, max_tokens: int = 4000) -> str:
        """Call Azure OpenAI with the given prompts. Handles model-specific parameter differences."""
        if not self.openai_client:
            return "[ERROR: OpenAI client not initialized]"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Try different parameter combinations for model compatibility
        # gpt-5.x models may not support temperature or max_tokens
        param_combinations = [
            # Try minimal params first (most compatible with newer models)
            {"model": self.deployment_name, "messages": messages, "max_completion_tokens": max_tokens},
            # Try with max_tokens instead
            {"model": self.deployment_name, "messages": messages, "max_tokens": max_tokens},
            # Try with temperature for older models
            {"model": self.deployment_name, "messages": messages, "max_tokens": max_tokens, "temperature": 0.3},
        ]

        last_error = None
        for params in param_combinations:
            try:
                response = self.openai_client.chat.completions.create(**params)
                return response.choices[0].message.content
            except Exception as e:
                error_msg = str(e).lower()
                # If it's a parameter compatibility error, try next combination
                if "unsupported" in error_msg or "not supported" in error_msg:
                    logging.info(f"Parameter compatibility issue, trying next combination: {e}")
                    last_error = e
                    continue
                # For other errors, fail immediately
                logging.error(f"OpenAI call failed: {e}")
                return f"[ERROR: OpenAI analysis failed: {e}]"

        # All combinations failed
        logging.error(f"All parameter combinations failed. Last error: {last_error}")
        return f"[ERROR: OpenAI analysis failed after trying multiple parameter combinations: {last_error}]"

    def _chunk_text(self, text: str, max_chars: int = 30000) -> List[str]:
        """Split text into chunks for processing large documents."""
        if len(text) <= max_chars:
            return [text]

        chunks = []
        current_chunk = ""

        # Split by paragraphs to maintain context
        paragraphs = text.split('\n\n')

        for para in paragraphs:
            if len(current_chunk) + len(para) < max_chars:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def _analyze_full_contract(self, text: str, file_name: str) -> Dict:
        """Perform comprehensive contract analysis from LABEL perspective."""
        system_prompt = """You are an expert contract analyst working for a MAJOR RECORD LABEL (Label perspective).
Your job is to analyze contracts and assess them from the LABEL'S business interests.

This is a BUSINESS ANALYSIS tool for internal use. You are analyzing an ACTUAL contract document.
The document text includes [PAGE N] markers showing where each page begins - use these for references.

Analyze the provided contract and extract structured information.
IMPORTANT: All assessments should be from the LABEL's perspective - what benefits the label, what risks the label faces.

REFERENCE FORMAT: Use the [PAGE N] markers in the text to identify page numbers.
- If you see content after "[PAGE 3]", reference it as "Page 3"
- If the document has visible section/article numbers, include them: "Page 3, Section 4.1"
- If no section numbers are visible, just use the page: "Page 3"
- References help readers locate content but don't need to be formal citations

Return your analysis as a valid JSON object with the following structure:
{
    "contract_type": "type of contract (e.g., Recording Agreement, Licensing Deal, Service Agreement)",
    "parties": [{"name": "party name", "role": "role in contract (Label/Artist/Licensor/etc)", "ref": "Page X"}],
    "effective_date": {"value": "date or null if not found", "ref": "Page X"},
    "term_duration": {"value": "duration description", "ref": "Page X, Section Y"},
    "financial_terms": {
        "advances": {"value": "amount or null", "ref": "Page X, Section Y"},
        "royalty_rates": {"value": "rates description", "ref": "Page X, Section Y"},
        "payment_schedule": {"value": "description or null", "ref": "Page X"},
        "label_investment": {"value": "total label financial commitment", "ref": "Page X"},
        "recoupment_terms": {"value": "how label recoups investment", "ref": "Page X, Section Y"},
        "other_payments": [{"description": "...", "ref": "Page X"}]
    },
    "rights_secured": [{"right": "description", "scope": "scope/territory", "exclusivity": true/false, "duration": "how long label holds rights", "ref": "Page X, Section Y"}],
    "label_protections": [{"clause": "protection description", "ref": "Page X, Section Y"}],
    "artist_obligations": [{"obligation": "what artist must do", "deadline": "when", "consequence_if_breached": "label remedy", "ref": "Page X, Section Y"}],
    "label_obligations": [{"obligation": "what label must do", "financial_impact": "cost to label", "ref": "Page X, Section Y"}],
    "termination_clauses": [{"trigger": "what triggers termination", "who_can_trigger": "label/artist/either", "label_impact": "effect on label", "ref": "Page X, Section Y"}],
    "key_dates": [{"event": "description", "date": "date or relative timing", "ref": "Page X"}],
    "artist_favorable_terms": [{"term": "term that favors artist MORE than industry standard", "concern": "why this is a concern for label", "ref": "Page X, Section Y"}],
    "missing_label_protections": ["standard label protections that appear to be missing"],
    "overall_assessment": "2-3 sentence assessment from LABEL's perspective - is this deal favorable to the label?"
}

Be thorough but concise. Extract actual values from the contract text.
Remember: You work for the LABEL. Artist-favorable terms are potential concerns.
ALWAYS include page/section references for every finding.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
1. Output ONLY the JSON object - no other text before or after
2. Do NOT ask any questions - just analyze and output JSON immediately
3. Do NOT ask for confirmation or clarification - proceed with analysis
4. Do NOT mention length limits or offer to split output - just output the JSON
5. Start your response with { and end with } - nothing else
6. If information is missing, use null or "Not specified" - do not ask about it

Your response must be valid JSON starting with { and ending with }."""

        # Handle large documents by chunking
        chunks = self._chunk_text(text)

        if len(chunks) == 1:
            user_prompt = f"Analyze this contract:\n\n{text}"
            # Use larger max_tokens for full contract analysis to accommodate detailed JSON
            response = self._call_openai(system_prompt, user_prompt, max_tokens=16000)
        else:
            # For large documents, analyze chunks and synthesize
            chunk_analyses = []
            for i, chunk in enumerate(chunks):
                user_prompt = f"Analyze this section (Part {i+1} of {len(chunks)}) of a contract:\n\n{chunk}"
                chunk_response = self._call_openai(system_prompt, user_prompt, max_tokens=2000)
                chunk_analyses.append(chunk_response)

            # Synthesize the chunks
            synthesis_prompt = """You are synthesizing multiple partial analyses of a single contract.
Combine these analyses into one comprehensive JSON structure, removing duplicates and resolving any conflicts.

CRITICAL: Output ONLY valid JSON. Start with { and end with }. No other text.
Do NOT ask questions. Do NOT offer options. Just output the combined JSON immediately."""

            user_prompt = f"Combine these partial contract analyses:\n\n" + "\n\n---\n\n".join(chunk_analyses)
            response = self._call_openai(synthesis_prompt, user_prompt)

        # Parse the JSON response with retry logic for empty results
        essential_keys = ['contract_type', 'parties', 'rights_secured', 'financial_terms']
        max_retries = 3

        for attempt in range(max_retries):
            analysis = self._extract_json_from_response(response)

            # Check if analysis has essential keys (not just empty or error)
            has_essential_data = any(
                key in analysis and analysis[key]
                for key in essential_keys
            )

            if has_essential_data or analysis.get('parse_error'):
                # Either we got good data or a clear error - don't retry
                break

            if attempt < max_retries - 1:
                logging.warning(f"Full analysis returned empty (attempt {attempt + 1}/{max_retries}). Retrying...")
                # Retry with more forceful prompt
                retry_prompt = f"""IMPORTANT: Your previous response was empty or incomplete.
You MUST output a complete JSON object with contract analysis.

Analyze this contract NOW and output ONLY the JSON (start with {{ end with }}):

{text[:40000]}"""
                response = self._call_openai(system_prompt, retry_prompt, max_tokens=16000)

        # DEBUG: Enhanced logging for analysis result
        logging.info("=" * 40)
        logging.info("_analyze_full_contract - RESULT ANALYSIS")
        logging.info(f"Full analysis completed with keys: {list(analysis.keys())}")
        logging.info(f"Raw response length: {len(response) if response else 0}")
        logging.info(f"Raw response preview: {response[:500] if response else 'None'}")

        if analysis.get('parse_error'):
            logging.error(f"_analyze_full_contract - JSON PARSE FAILED!")
            logging.error(f"Raw analysis: {analysis.get('raw_analysis', '')[:1000]}")

        # Log specific key values
        logging.info(f"  - contract_type: {analysis.get('contract_type', 'MISSING')}")
        logging.info(f"  - parties: {len(analysis.get('parties', []))} found")
        logging.info(f"  - financial_terms: {type(analysis.get('financial_terms')).__name__}")
        logging.info(f"  - rights_secured: {len(analysis.get('rights_secured', []))} found")

        if not any(key in analysis for key in essential_keys):
            logging.warning(f"Analysis may be incomplete - no essential keys found!")
        logging.info("=" * 40)

        analysis["_metadata"] = {
            "file_name": file_name,
            "analyzed_at": datetime.now().isoformat(),
            "text_length": len(text),
            "chunks_processed": len(chunks),
            "retry_attempts": attempt + 1
        }
        return analysis

    def _extract_specific_clauses(self, text: str, clause_types: List[str]) -> Dict:
        """Extract specific types of clauses from the contract."""
        clause_descriptions = {
            "financial": "All financial terms including advances, royalties, payments, fees, revenue sharing, expenses",
            "rights": "All rights granted or reserved including intellectual property, licensing, usage rights, exclusivity",
            "obligations": "All obligations and duties of each party, deliverables, performance requirements",
            "termination": "Termination conditions, notice periods, breach definitions, consequences of termination",
            "exclusivity": "Exclusivity clauses, non-compete provisions, first refusal rights",
            "territory": "Geographic scope, territory definitions, regional limitations",
            "duration": "Term length, renewal options, extension conditions, effective dates"
        }

        types_to_extract = [ct for ct in clause_types if ct in clause_descriptions]
        if not types_to_extract:
            types_to_extract = list(clause_descriptions.keys())

        extraction_details = "\n".join([f"- {ct}: {clause_descriptions[ct]}" for ct in types_to_extract])

        system_prompt = f"""You are a contract clause extraction specialist.
Extract the following types of clauses from the contract:

{extraction_details}

CRITICAL: For EVERY clause extracted, you MUST include a document reference:
- "ref": "Page X, Section Y" or "ref": "Page X, Article Y"
The document text includes [PAGE N] markers - use these for exact page numbers.

Return a JSON object where each key is a clause type and the value is an array of extracted clauses.
Each clause should have: "text" (the clause text or summary - keep under 200 words), "ref" (Page X, Section Y), "key_points" (2-3 bullet points).

Example format:
{{
    "financial": [
        {{"text": "...", "ref": "Page 3, Section 4.1", "key_points": ["Advance of $X", "Royalty rate of Y%"]}}
    ]
}}

ALWAYS include page and section references for every extracted clause.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
1. Output ONLY the JSON object - no other text before or after
2. Do NOT ask any questions - just extract and output JSON immediately
3. Do NOT ask for confirmation or clarification - proceed with extraction
4. Do NOT mention length limits or offer to split output - output the JSON directly
5. Start your response with {{ and end with }} - nothing else
6. If a clause type has no matches, use an empty array: "type": []
7. Keep each clause summary under 200 words - summarize if needed
8. Extract UP TO 3-5 most important clauses per category (prioritize key terms)

Your response must be valid JSON starting with {{ and ending with }}."""

        # For large documents, process only the most relevant text
        text_to_process = text[:35000]  # Reduced limit for better processing

        user_prompt = f"Extract clauses from this contract. Output ONLY valid JSON:\n\n{text_to_process}"
        response = self._call_openai(system_prompt, user_prompt, max_tokens=6000)

        # Add logging for debugging
        logging.info(f"_extract_specific_clauses - Response length: {len(response) if response else 0}")

        result = self._extract_json_from_response(response)

        # If parse failed, try with retry
        if result.get('parse_error'):
            logging.warning("_extract_specific_clauses - Initial parse failed, retrying...")
            retry_prompt = f"""IMPORTANT: Output ONLY valid JSON. No other text. Start with {{ end with }}.

Extract clauses from this contract into JSON format:
{text_to_process[:25000]}"""
            response = self._call_openai(system_prompt, retry_prompt, max_tokens=6000)
            result = self._extract_json_from_response(response)

        return result

    def _generate_summary(self, text: str, summary_type: str, audience: str) -> Dict:
        """Generate a summary tailored to the audience - FROM LABEL PERSPECTIVE."""
        audience_instructions = {
            "legal": "Use precise legal terminology. Include specific clause references. Highlight legal risks to the LABEL and compliance considerations.",
            "business": "Focus on commercial terms and business implications FOR THE LABEL. Emphasize label ROI, recoupment timeline, and operational impacts to the label.",
            "executive": "Provide a high-level overview for LABEL C-suite. Focus on label investment, rights secured, strategic value, and key risks to the label. Keep it concise."
        }

        length_instructions = {
            "executive": "Provide a brief 150-200 word summary with key bullet points.",
            "detailed": "Provide a comprehensive 400-500 word summary covering all major aspects.",
            "legal": "Provide a thorough legal summary of 300-400 words with specific clause references."
        }

        system_prompt = f"""You are a contract summarization expert working for a MAJOR RECORD LABEL.
Your summaries are FOR LABEL EXECUTIVES and should reflect the LABEL's interests and perspective.

{audience_instructions.get(audience, audience_instructions['business'])}
{length_instructions.get(summary_type, length_instructions['detailed'])}

IMPORTANT: Frame everything from the label's business perspective:
- "Label investment" instead of "artist advance"
- "Rights secured by label" instead of "rights granted"
- "Artist-favorable terms" = potential concerns for the label
- Risk assessment = risks TO THE LABEL

CRITICAL: Include document references (Page X, Section Y) for key claims.
The document text includes [PAGE N] markers - use these for exact page numbers.

CRITICAL: The recommendation MUST align with the risk level:
- LOW risk: "Proceed" or "Proceed as drafted"
- MEDIUM risk: "Proceed with caution; consider negotiating [specific terms]"
- HIGH risk: "Do not proceed without changes to [specific critical terms]" or "Renegotiate [specific issues] before proceeding"

Return a JSON object with:
{{
    "summary": "the main summary text FROM LABEL PERSPECTIVE",
    "key_points": [{{"point": "bullet point text", "ref": "Page X, Section Y"}}],
    "label_investment_total": {{"value": "total financial commitment from label", "ref": "Page X"}},
    "rights_secured": {{"value": "summary of rights label obtains", "ref": "Page X, Section Y"}},
    "critical_dates": [{{"event": "...", "date": "...", "ref": "Page X"}}],
    "action_items": ["any actions needed by label team"],
    "risk_level": "low/medium/high (risk TO THE LABEL)",
    "artist_leverage_concerns": [{{"concern": "term giving artist unusual leverage", "ref": "Page X, Section Y"}}],
    "recommendation": "recommendation aligned with risk level - if HIGH risk, must specify required changes before proceeding"
}}

ALWAYS include page/section references for key findings.

IMPORTANT: Do NOT ask clarifying questions. Do NOT ask for confirmation. Just execute the summary and return the JSON."""

        user_prompt = f"Summarize this contract for a {audience} audience:\n\n{text[:40000]}"
        response = self._call_openai(system_prompt, user_prompt)
        return self._extract_json_from_response(response)

    def _identify_risks(self, text: str) -> Dict:
        """Identify risks TO THE LABEL and deviations from standard terms."""
        system_prompt = """You are a contract risk analyst working for a MAJOR RECORD LABEL.
Your job is to identify risks TO THE LABEL, not to the artist.

IMPORTANT PERSPECTIVE:
- Artist-favorable terms = RISKS to the label (higher costs, less control, early reversion)
- High advances/royalties = FINANCIAL RISK to label
- Strong artist termination rights = OPERATIONAL RISK to label
- Early master reversion = ASSET RISK to label
- Creative control for artist = COMMERCIAL RISK to label
- Non-recoupable payments = DIRECT COST to label

CRITICAL: For EVERY risk identified, you MUST include a document reference:
- "ref": "Page X, Section Y" or "ref": "Page X, Article Y"
The document text includes [PAGE N] markers - use these for exact page numbers.

Analyze the contract for RISKS TO THE LABEL:
1. Financial exposure (high advances, guaranteed payments, non-recoupable costs)
2. Asset risks (early master reversion, limited rights duration, territory restrictions)
3. Operational risks (artist approval requirements, key man clauses, delivery delays)
4. Revenue risks (high royalty rates, favorable streaming splits, limited 360 participation)
5. Legal/compliance risks (regulatory, indemnification gaps)
6. Competitive risks (artist leverage, termination options)

Return a JSON object:
{
    "overall_risk_level": "low/medium/high (RISK TO LABEL)",
    "risk_score": 1-100 (higher = worse for label),
    "label_financial_exposure": "total potential label investment/loss",
    "risks": [
        {
            "category": "financial/asset/operational/revenue/legal/competitive",
            "severity": "low/medium/high/critical",
            "description": "what the risk TO THE LABEL is",
            "ref": "Page X, Section Y",
            "label_impact": "specific impact on label operations/finances",
            "recommendation": "how label should address this in negotiation"
        }
    ],
    "artist_favorable_terms": [
        {"term": "what favors the artist", "industry_standard": "what's typical", "label_impact": "why this hurts the label", "ref": "Page X, Section Y"}
    ],
    "missing_label_protections": ["standard label protections not found in this contract"],
    "negotiation_priorities": [{"priority": "item label should push back on", "ref": "Page X, Section Y"}],
    "deal_breakers": [{"issue": "term that may be unacceptable", "ref": "Page X, Section Y"}],
    "summary": "2-3 sentence risk summary FROM LABEL'S PERSPECTIVE"
}

ALWAYS cite the specific page and section for every risk and concern.

IMPORTANT: Do NOT ask clarifying questions. Do NOT ask for confirmation. Just execute the analysis and return the JSON."""

        user_prompt = f"Analyze risks in this contract:\n\n{text[:50000]}"
        response = self._call_openai(system_prompt, user_prompt)

        # DEBUG: Log the raw response before parsing
        logging.info(f"_identify_risks - Raw response length: {len(response) if response else 0}")
        logging.info(f"_identify_risks - Raw response preview: {response[:1000] if response else 'EMPTY'}")

        result = self._extract_json_from_response(response)

        # DEBUG: Log the parsed result
        logging.info(f"_identify_risks - Parsed result keys: {list(result.keys()) if isinstance(result, dict) else 'NOT DICT'}")
        if isinstance(result, dict) and result.get('parse_error'):
            logging.error(f"_identify_risks - JSON PARSE FAILED!")

        return result

    def _compare_contracts(self, text_a: str, text_b: str, name_a: str, name_b: str) -> Dict:
        """Compare two contracts using sectioned analysis for better coverage."""

        # For any substantial contracts, use sectioned comparison to avoid truncation
        # Sectioned mode analyzes each area (financial, rights, etc.) separately
        # This provides better coverage and avoids the model refusing due to incomplete text
        total_length = len(text_a) + len(text_b)
        max_single_contract = max(len(text_a), len(text_b))

        # Use sectioned mode if total > 30k OR if either contract alone is > 20k
        # This ensures we don't truncate important contract content
        use_sectioned = total_length > 30000 or max_single_contract > 20000

        if use_sectioned:
            return self._compare_contracts_sectioned(text_a, text_b, name_a, name_b)

        system_prompt = """You are a contract analysis assistant performing an EDUCATIONAL comparison of two recording agreements.
This is a BUSINESS ANALYSIS exercise for training purposes, NOT legal advice.

Your task: Compare these two contracts and identify factual differences in their terms.
Analyze which contract has more favorable terms from a BUSINESS perspective (lower financial commitments, stronger protections, better rights retention).

When comparing terms, note which contract (A or B) has:
- Lower advance/payment obligations
- Longer rights retention periods
- Broader territorial coverage
- More comprehensive protections
- Clearer deliverable requirements

CRITICAL: Include document references for BOTH contracts in the format:
- "ref_a": "Page X, Section Y" (for Contract A)
- "ref_b": "Page X, Section Y" (for Contract B)
The document text includes [PAGE N] markers - use these for exact page numbers.

Compare these two contracts and identify:
1. Key differences in financial terms, rights, obligations
2. Which contract has more protective clauses (from a business standpoint)
3. Which contract has higher financial exposure
4. Notable terms that differ significantly between the two

Return a JSON object:
{
    "similarity_score": 0-100,
    "contract_types_match": true/false,
    "more_label_favorable": "a/b/neutral (which contract has more protective business terms)",
    "key_differences": [
        {
            "aspect": "what's being compared",
            "contract_a": "terms in first contract",
            "contract_b": "terms in second contract",
            "ref_a": "Page X, Section Y",
            "ref_b": "Page X, Section Y",
            "label_preference": "a/b (which has stronger business protections)",
            "label_impact": "business significance of this difference"
        }
    ],
    "unique_to_a": [{"clause": "clause description", "ref": "Page X, Section Y"}],
    "unique_to_b": [{"clause": "clause description", "ref": "Page X, Section Y"}],
    "financial_comparison": {
        "contract_a": {"label_investment": "total financial commitment", "royalty_exposure": "royalty rates", "ref": "Page X"},
        "contract_b": {"label_investment": "total financial commitment", "royalty_exposure": "royalty rates", "ref": "Page X"},
        "lower_label_cost": "a/b",
        "better_label_margin": "a/b"
    },
    "rights_comparison": {
        "contract_a": {"rights_duration": "...", "territory": "...", "reversion": "...", "ref": "Page X, Section Y"},
        "contract_b": {"rights_duration": "...", "territory": "...", "reversion": "...", "ref": "Page X, Section Y"},
        "stronger_label_rights": "a/b"
    },
    "risk_comparison": {
        "contract_a_risk_level": "low/medium/high (financial/operational risk level)",
        "contract_b_risk_level": "low/medium/high (financial/operational risk level)",
        "lower_label_risk": "a/b"
    },
    "overall_assessment": "factual summary of which contract has more favorable business terms and key differences",
    "recommended_standard_terms": ["notable terms from either contract worth considering"]
}

ALWAYS include page/section references from both contracts for every comparison point.

IMPORTANT: This is an educational analysis. Provide factual comparisons. Do NOT ask clarifying questions. Just execute the comparison and return the JSON."""

        user_prompt = f"""Compare these two contracts:

=== CONTRACT A: {name_a} ===
{text_a[:30000]}

=== CONTRACT B: {name_b} ===
{text_b[:30000]}"""

        response = self._call_openai(system_prompt, user_prompt, max_tokens=6000)
        result = self._extract_json_from_response(response)
        result["_metadata"] = {
            "contract_a": name_a,
            "contract_b": name_b,
            "compared_at": datetime.now().isoformat(),
            "comparison_mode": "standard"
        }
        return result

    def _compare_contracts_sectioned(self, text_a: str, text_b: str, name_a: str, name_b: str) -> Dict:
        """Compare large contracts by analyzing sections separately then synthesizing."""
        logging.info(f"Using sectioned comparison for large contracts: {name_a} vs {name_b}")

        # Define comparison sections
        sections = {
            "financial": {
                "focus": "advances, royalties, recoupment, payment schedules, 360 terms, merchandise, touring splits",
                "analysis_criteria": "Compare total financial commitments, royalty rates, recoupment structures"
            },
            "rights": {
                "focus": "master ownership, duration of rights, territory, exclusivity, reversion triggers, publishing",
                "analysis_criteria": "Compare scope and duration of rights granted, territorial coverage, reversion terms"
            },
            "obligations": {
                "focus": "delivery requirements, album commitments, promotional obligations, key man clauses",
                "analysis_criteria": "Compare deliverable requirements, commitment levels, operational obligations"
            },
            "termination_risk": {
                "focus": "termination triggers, exit clauses, breach remedies, force majeure, key man provisions",
                "analysis_criteria": "Compare termination conditions, exit mechanisms, breach remedies"
            }
        }

        section_results = {}

        for section_name, section_info in sections.items():
            section_prompt = f"""You are a contract analysis assistant performing an EDUCATIONAL comparison of two recording agreements.
Focus ONLY on {section_name.upper()} terms in these two contracts.

FOCUS AREAS: {section_info['focus']}
ANALYSIS CRITERIA: {section_info['analysis_criteria']}

Extract and compare {section_name} terms from both contracts factually.

Return a JSON object with this EXACT structure:
{{
    "section": "{section_name}",
    "contract_a_terms": {{
        "summary": "brief summary of {section_name} terms in Contract A",
        "key_values": ["specific values/terms found"],
        "refs": ["Page X, Section Y"]
    }},
    "contract_b_terms": {{
        "summary": "brief summary of {section_name} terms in Contract B",
        "key_values": ["specific values/terms found"],
        "refs": ["Page X, Section Y"]
    }},
    "differences": [
        {{
            "aspect": "specific term being compared",
            "contract_a": "value/term in A",
            "contract_b": "value/term in B",
            "label_preference": "a/b/neutral (which has more favorable business terms)",
            "reason": "factual explanation of the difference"
        }}
    ],
    "section_winner": "a/b/neutral (which contract has more favorable terms in this section)",
    "section_assessment": "1-2 sentence factual assessment of key differences"
}}

IMPORTANT: This is educational analysis. Do NOT ask questions. Just analyze and return the JSON."""

            user_prompt = f"""Compare {section_name.upper()} terms:

=== CONTRACT A: {name_a} ===
{text_a[:50000]}

=== CONTRACT B: {name_b} ===
{text_b[:50000]}"""

            response = self._call_openai(section_prompt, user_prompt, max_tokens=3000)
            section_results[section_name] = self._extract_json_from_response(response)

        # Synthesize all section results into final comparison
        synthesis_prompt = """You are an educational contract analysis assistant synthesizing sectioned comparison results.

Based on the section-by-section analysis provided, create a comprehensive factual comparison summary.

Return a JSON object:
{
    "similarity_score": 0-100,
    "contract_types_match": true/false,
    "more_label_favorable": "a/b/neutral (which has more favorable business terms overall)",
    "section_winners": {
        "financial": "a/b/neutral",
        "rights": "a/b/neutral",
        "obligations": "a/b/neutral",
        "termination_risk": "a/b/neutral"
    },
    "key_differences": [
        {
            "aspect": "term being compared",
            "contract_a": "value in A",
            "contract_b": "value in B",
            "label_preference": "a/b (which has more favorable terms)",
            "label_impact": "business significance of this difference"
        }
    ],
    "financial_comparison": {
        "contract_a": {"label_investment": "total commitment amount", "royalty_exposure": "royalty rates"},
        "contract_b": {"label_investment": "total commitment amount", "royalty_exposure": "royalty rates"},
        "lower_label_cost": "a/b",
        "better_label_margin": "a/b"
    },
    "rights_comparison": {
        "contract_a": {"rights_duration": "...", "territory": "...", "reversion": "..."},
        "contract_b": {"rights_duration": "...", "territory": "...", "reversion": "..."},
        "stronger_label_rights": "a/b"
    },
    "risk_comparison": {
        "contract_a_risk_level": "low/medium/high",
        "contract_b_risk_level": "low/medium/high",
        "lower_label_risk": "a/b"
    },
    "deal_breakers": [{"contract": "a/b", "issue": "notable concern"}],
    "overall_assessment": "2-3 sentence factual summary of key differences between the contracts",
    "recommended_standard_terms": ["notable terms from either contract"]
}

IMPORTANT: This is educational analysis. Provide factual comparisons only."""

        synthesis_user = f"""Synthesize these section comparisons:

{json.dumps(section_results, indent=2, default=str)}

Contract A: {name_a}
Contract B: {name_b}"""

        synthesis_response = self._call_openai(synthesis_prompt, synthesis_user, max_tokens=4000)
        result = self._extract_json_from_response(synthesis_response)

        # Add section details and metadata
        result["_section_details"] = section_results
        result["_metadata"] = {
            "contract_a": name_a,
            "contract_b": name_b,
            "compared_at": datetime.now().isoformat(),
            "comparison_mode": "sectioned",
            "sections_analyzed": list(sections.keys())
        }

        return result

    def perform(self, **kwargs) -> str:
        """Execute contract analysis action."""
        try:
            action = kwargs.get('action', 'list_contracts')
            contract_name = kwargs.get('contract_name')
            contract_name_b = kwargs.get('contract_name_b')
            clause_types = kwargs.get('clause_types', [])
            summary_type = kwargs.get('summary_type', 'detailed')
            audience = kwargs.get('audience', 'business')

            # List contracts
            if action == 'list_contracts':
                files = self._list_files_in_folder()
                return json.dumps({
                    "status": "success",
                    "action": "list_contracts",
                    "contracts_folder": self.contracts_folder,
                    "files": files,
                    "count": len(files),
                    "supported_formats": ["pdf", "docx", "txt"],
                    "usage": "Use contract_name parameter with the file name to analyze"
                }, indent=2)

            # All other actions require a contract name
            if not contract_name:
                return json.dumps({
                    "status": "error",
                    "message": "contract_name is required for this action",
                    "available_contracts": self._list_files_in_folder()
                }, indent=2)

            # Read the contract
            file_path = f"{self.contracts_folder}/{contract_name}"
            content = self._read_file_content(file_path)

            if not content:
                return json.dumps({
                    "status": "error",
                    "message": f"Could not read contract: {contract_name}",
                    "path_tried": file_path,
                    "available_contracts": self._list_files_in_folder()
                }, indent=2)

            # Extract text
            text = self._extract_text(file_path, content)
            if text.startswith("[ERROR"):
                return json.dumps({
                    "status": "error",
                    "message": text
                }, indent=2)

            # Execute the requested action
            if action == 'full_workup':
                # Comprehensive analysis: runs everything in one go
                logging.info(f"Running full workup on {contract_name}")

                # 1. Full contract analysis
                analysis = self._analyze_full_contract(text, contract_name)

                # 2. Risk identification (run first - this is the authoritative risk source)
                risks = self._identify_risks(text)

                # 3. Executive summary for business audience
                summary = self._generate_summary(text, 'executive', 'business')

                # 4. Extract key clauses (all types)
                all_clause_types = ['financial', 'rights', 'obligations', 'termination', 'exclusivity', 'territory', 'duration']
                clauses = self._extract_specific_clauses(text, all_clause_types)

                # Synchronize risk levels - use risk assessment as authoritative source
                # This ensures consistency throughout the PDF report
                authoritative_risk_level = risks.get('overall_risk_level', 'unknown')
                authoritative_risk_score = risks.get('risk_score', 'N/A')
                if isinstance(summary, dict):
                    summary['risk_level'] = authoritative_risk_level
                    summary['risk_score'] = authoritative_risk_score

                # Compile full report (include contract text for PDF with clickable references)
                full_report = {
                    "contract": contract_name,
                    "analyzed_at": datetime.now().isoformat(),
                    "executive_summary": summary,
                    "full_analysis": analysis,
                    "risk_assessment": risks,
                    "extracted_clauses": clauses,
                    "text_length": len(text),
                    "_contract_text": text  # Include for PDF generation with clickable refs
                }

                # Save the analysis report to Azure storage
                save_result = self._save_analysis_report(contract_name, full_report)

                # Build concise chat response (fits on one screen)
                risk_level = risks.get('overall_risk_level', 'Unknown').upper()
                risk_score = risks.get('risk_score', 'N/A')
                risk_summary = risks.get('summary', '')

                # Get top 3 risks with references
                top_risks = []
                for r in risks.get('risks', [])[:3]:
                    if isinstance(r, dict):
                        ref = r.get('ref', 'N/A')
                        desc = r.get('description', '')[:80]
                        severity = r.get('severity', '').upper()
                        top_risks.append(f"- [{severity}] {desc} (Ref: {ref})")

                # Get key financial terms with references
                fin_terms = analysis.get('financial_terms', {})
                advances = fin_terms.get('advances', {})
                adv_val = advances.get('value', 'N/A') if isinstance(advances, dict) else advances
                adv_ref = advances.get('ref', '') if isinstance(advances, dict) else ''

                royalties = fin_terms.get('royalty_rates', {})
                roy_val = royalties.get('value', 'N/A') if isinstance(royalties, dict) else royalties
                roy_ref = royalties.get('ref', '') if isinstance(royalties, dict) else ''

                # Build the chat summary (short, fits one screen)
                chat_summary = {
                    "headline": f"Analysis Complete: {contract_name}",
                    "risk_level": risk_level,
                    "risk_score": f"{risk_score}/100",
                    "key_findings": [
                        f"Advance: {adv_val}" + (f" (Ref: {adv_ref})" if adv_ref else ""),
                        f"Royalty: {roy_val}" + (f" (Ref: {roy_ref})" if roy_ref else ""),
                    ],
                    "top_risks": top_risks,
                    "recommendation": summary.get('recommendation', '') if isinstance(summary, dict) else '',
                    "full_report": {
                        "message": "Full analysis with all details saved to PDF report:",
                        "download_url": save_result.get('download_url', 'Report generation failed'),
                        "report_name": save_result.get('report_name', ''),
                        "size_kb": save_result.get('size_kb', 0)
                    }
                }

                return json.dumps({
                    "status": "success",
                    "action": "full_workup",
                    "contract": contract_name,
                    "chat_response": chat_summary,
                    "_full_data": {
                        "executive_summary": summary,
                        "full_analysis": analysis,
                        "risk_assessment": risks,
                        "extracted_clauses": clauses,
                        "report_saved": save_result
                    },
                    "_metadata": {
                        "analyzed_at": datetime.now().isoformat(),
                        "file_name": contract_name,
                        "text_length": len(text)
                    }
                }, indent=2)

            elif action == 'analyze_contract':
                result = self._analyze_full_contract(text, contract_name)
                return json.dumps({
                    "status": "success",
                    "action": "analyze_contract",
                    "contract": contract_name,
                    "analysis": result
                }, indent=2)

            elif action == 'extract_clauses':
                result = self._extract_specific_clauses(text, clause_types)

                # Build concise chat summary
                clause_summary = []
                for clause_type, clauses in result.items():
                    if isinstance(clauses, list) and len(clauses) > 0:
                        # Get first clause of each type with its reference
                        first_clause = clauses[0]
                        if isinstance(first_clause, dict):
                            clause_summary.append({
                                "type": clause_type,
                                "count": len(clauses),
                                "sample": first_clause.get('text', '')[:100] + "..." if len(first_clause.get('text', '')) > 100 else first_clause.get('text', ''),
                                "ref": first_clause.get('ref', 'N/A')
                            })

                chat_summary = {
                    "headline": f"Clauses Extracted: {contract_name}",
                    "clause_types_found": list(result.keys()) if isinstance(result, dict) else [],
                    "summary": clause_summary
                }

                return json.dumps({
                    "status": "success",
                    "action": "extract_clauses",
                    "contract": contract_name,
                    "clause_types_requested": clause_types or "all",
                    "chat_response": chat_summary,
                    "_full_data": {"extractions": result}
                }, indent=2)

            elif action == 'summarize_contract':
                result = self._generate_summary(text, summary_type, audience)

                # Build concise chat response
                summary_text = result.get('summary', '') if isinstance(result, dict) else str(result)

                # Extract key points with refs
                key_points = []
                for pt in (result.get('key_points', []) if isinstance(result, dict) else [])[:4]:
                    if isinstance(pt, dict):
                        key_points.append({
                            "point": pt.get('point', ''),
                            "ref": pt.get('ref', 'N/A')
                        })
                    else:
                        key_points.append({"point": str(pt), "ref": "N/A"})

                chat_summary = {
                    "headline": f"Summary: {contract_name}",
                    "risk_level": result.get('risk_level', 'N/A') if isinstance(result, dict) else 'N/A',
                    "summary": summary_text[:300] + "..." if len(summary_text) > 300 else summary_text,
                    "key_points": key_points,
                    "recommendation": result.get('recommendation', '') if isinstance(result, dict) else ''
                }

                return json.dumps({
                    "status": "success",
                    "action": "summarize_contract",
                    "contract": contract_name,
                    "summary_type": summary_type,
                    "audience": audience,
                    "chat_response": chat_summary,
                    "_full_data": {"result": result}
                }, indent=2)

            elif action == 'identify_risks':
                result = self._identify_risks(text)

                # Build concise chat response
                risk_level = result.get('overall_risk_level', 'Unknown').upper()
                risk_score = result.get('risk_score', 'N/A')

                # Get top 3 risks with references
                top_risks = []
                for r in result.get('risks', [])[:3]:
                    if isinstance(r, dict):
                        ref = r.get('ref', 'N/A')
                        desc = r.get('description', '')[:100]
                        severity = r.get('severity', '').upper()
                        top_risks.append({
                            "severity": severity,
                            "description": desc,
                            "ref": ref
                        })

                # Get deal breakers with references
                deal_breakers = []
                for db in result.get('deal_breakers', [])[:2]:
                    if isinstance(db, dict):
                        deal_breakers.append({
                            "issue": db.get('issue', ''),
                            "ref": db.get('ref', 'N/A')
                        })

                chat_summary = {
                    "headline": f"Risk Analysis: {contract_name}",
                    "risk_level": risk_level,
                    "risk_score": f"{risk_score}/100",
                    "financial_exposure": result.get('label_financial_exposure', 'N/A'),
                    "top_risks": top_risks,
                    "deal_breakers": deal_breakers,
                    "summary": result.get('summary', '')
                }

                return json.dumps({
                    "status": "success",
                    "action": "identify_risks",
                    "contract": contract_name,
                    "chat_response": chat_summary,
                    "_full_data": {"risk_analysis": result}
                }, indent=2)

            elif action == 'compare_contracts':
                if not contract_name_b:
                    return json.dumps({
                        "status": "error",
                        "message": "contract_name_b is required for comparison",
                        "available_contracts": self._list_files_in_folder()
                    }, indent=2)

                # Read second contract
                file_path_b = f"{self.contracts_folder}/{contract_name_b}"
                content_b = self._read_file_content(file_path_b)

                if not content_b:
                    return json.dumps({
                        "status": "error",
                        "message": f"Could not read second contract: {contract_name_b}"
                    }, indent=2)

                text_b = self._extract_text(file_path_b, content_b)
                result = self._compare_contracts(text, text_b, contract_name, contract_name_b)

                # Build concise chat response
                more_favorable = result.get('more_label_favorable', 'neutral')
                winner = contract_name if more_favorable == 'a' else (contract_name_b if more_favorable == 'b' else 'Neither')

                # Get comparison mode from metadata
                metadata = result.get('_metadata', {})
                comparison_mode = metadata.get('comparison_mode', 'standard')

                # Get top key differences with refs
                key_diffs = []
                for diff in result.get('key_differences', [])[:5]:
                    if isinstance(diff, dict):
                        key_diffs.append({
                            "aspect": diff.get('aspect', ''),
                            "contract_a": diff.get('contract_a', '')[:60],
                            "contract_b": diff.get('contract_b', '')[:60],
                            "preference": diff.get('label_preference', '').upper(),
                            "impact": diff.get('label_impact', '')[:100] if diff.get('label_impact') else ''
                        })

                # Financial comparison
                fin_comp = result.get('financial_comparison', {})
                financial_summary = {
                    "contract_a_investment": fin_comp.get('contract_a', {}).get('label_investment', 'N/A') if isinstance(fin_comp.get('contract_a'), dict) else 'N/A',
                    "contract_b_investment": fin_comp.get('contract_b', {}).get('label_investment', 'N/A') if isinstance(fin_comp.get('contract_b'), dict) else 'N/A',
                    "lower_cost": fin_comp.get('lower_label_cost', 'N/A'),
                    "better_margin": fin_comp.get('better_label_margin', 'N/A')
                }

                # Rights comparison
                rights_comp = result.get('rights_comparison', {})
                rights_summary = {
                    "contract_a_duration": rights_comp.get('contract_a', {}).get('rights_duration', 'N/A') if isinstance(rights_comp.get('contract_a'), dict) else 'N/A',
                    "contract_b_duration": rights_comp.get('contract_b', {}).get('rights_duration', 'N/A') if isinstance(rights_comp.get('contract_b'), dict) else 'N/A',
                    "stronger_rights": rights_comp.get('stronger_label_rights', 'N/A')
                }

                # Risk comparison
                risk_comp = result.get('risk_comparison', {})

                # Section winners (for sectioned mode)
                section_winners = result.get('section_winners', {})

                # Deal breakers
                deal_breakers = []
                for db in result.get('deal_breakers', [])[:3]:
                    if isinstance(db, dict):
                        deal_breakers.append({
                            "contract": db.get('contract', ''),
                            "issue": db.get('issue', '')[:100]
                        })

                chat_summary = {
                    "headline": f"CONTRACT COMPARISON: {contract_name} vs {contract_name_b}",
                    "comparison_mode": comparison_mode,
                    "overall_winner": {
                        "more_favorable_to_label": winner,
                        "verdict": "Contract A" if more_favorable == 'a' else ("Contract B" if more_favorable == 'b' else "Neutral - Neither clearly better")
                    },
                    "section_breakdown": {
                        "financial": section_winners.get('financial', fin_comp.get('lower_label_cost', 'N/A')),
                        "rights": section_winners.get('rights', rights_comp.get('stronger_label_rights', 'N/A')),
                        "obligations": section_winners.get('obligations', 'N/A'),
                        "termination_risk": section_winners.get('termination_risk', risk_comp.get('lower_label_risk', 'N/A'))
                    },
                    "financial_comparison": financial_summary,
                    "rights_comparison": rights_summary,
                    "risk_comparison": {
                        "contract_a_risk": risk_comp.get('contract_a_risk_level', 'N/A'),
                        "contract_b_risk": risk_comp.get('contract_b_risk_level', 'N/A'),
                        "lower_risk": risk_comp.get('lower_label_risk', 'N/A')
                    },
                    "key_differences": key_diffs,
                    "deal_breakers": deal_breakers if deal_breakers else "None identified",
                    "overall_assessment": result.get('overall_assessment', ''),
                    "recommended_terms": result.get('recommended_standard_terms', [])[:3]
                }

                return json.dumps({
                    "status": "success",
                    "action": "compare_contracts",
                    "contract_a": contract_name,
                    "contract_b": contract_name_b,
                    "chat_response": chat_summary,
                    "_full_data": {"comparison": result}
                }, indent=2)

            else:
                return json.dumps({
                    "status": "error",
                    "message": f"Unknown action: {action}",
                    "valid_actions": ["list_contracts", "analyze_contract", "extract_clauses",
                                     "summarize_contract", "identify_risks", "compare_contracts"]
                }, indent=2)

        except Exception as e:
            logging.error(f"ContractAnalysisAgent error: {e}")
            return json.dumps({
                "status": "error",
                "message": str(e),
                "type": type(e).__name__
            }, indent=2)


if __name__ == "__main__":
    # Test the agent
    agent = ContractAnalysisAgent()

    print("Testing ContractAnalysisAgent...")
    print("\n1. Listing contracts:")
    print(agent.perform(action="list_contracts"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9S8eZOjVrYv+lUUdf5w+VIuQMx+0TceIAFCEiBAAsl2VDPPgxgl+fq7P5CUWZlZmTX08bndr+yIzGRPa6/xt/b05zurbcKievfrOyZK04kRWqmXv/vwzvVqp4rKJiryoYzOrfR88epJ5TlF5UZ5MLFyd+LljVc1VpRnw28Tp8ibynKaesKp8nqiC/PJimbmq5+0iTJXNWXO6ovd/ONk4Q61Iz8au4vqpJ40xaQJvUlq2V76YeKnVlBPrKqJ6uYX3+qKyrJTbzKMlNUfJt7pPoaTWm3tDV9GQgIv9yqrGXr0Tp7TNlHnTeo2y6xqHMUvqlvnE9dzonqY0i+ZlXhV/XGitWVZVEN3yoz7MJnJrHnrUDf1sVlmNfXHgRveycrK1Kvf/frbHx/eRcPv7379891AQj18esfeJ37lUh3V9EBOM7RKrTwYisvzwOGRp6VXjX0On1zPn9z/el97qf9h8r/+V9JbVVD/PPnlf0/qpvr193xy//f7u/G/+XVi3iOXBzJvo02GP4YpfbxV+9ysqc5POhn/3SpO/jG5DfUx8Jr3P90+/vRh8lM6MPzToxB/+vl544eCT7mVeS/6eFb21Yaf7K81/WR/0fgq5U/NuRzk+KLlk6KB/N/+eNH0Jv/ztcKLpk+Lxpm73qDEqee+HN1q3cjLnZfNHz6PTe22jnKvvrLreeP/mqwGhn62iuelkf8ojn98wfoXchv/+QN9IwdGbfn46Vr/+ulTlH/yi9T1qvc/f9mq8pq2yidxPeiH22Zl/f7PLyvddKxurKatf3/36/h76zjDnH5/9+Gt2jfab7WfE/+VRo917hSPza/zeVnwZg/XKY/Nrr98ZaA2b8Zqgy97f63685t165sH8NxPd3sf2/32+7vS9YepDBXcwjndfmtOQ6d/vNlTW1uBd2PJtvZeGExpVcOPwYlN+qgJr/5uJGxyLRwcoHXzsE8N+OHfXx8mUT76zH9MX1EyevDaxdBddden0Ucf26jyJtZnXzGO8oX+5UXznMhf/zYF8qqqqL6iCdmgXY/Mes6o6HEC7tVxN+Gji/uaPnaDAY9x4qki/vqD1vJ1Rque5V7l9jDC8wpj/59Ka5DtPyaD5vz5qmL/Bf75bLZ/vZT3WDrG0gdDr4ZBr6R/upe8fxznCxKfiHSo+G8R5jBxtmhT90rISPsjs36dfDHzNzscZ/epGUK3+2Dq1wn/O4U/v8GOAYWcXsh9/PIorjs6+TR+/CypDw8y+fkLgY0VPw7MHiDI6Bfe//7ut7mqyurv737+twjwy/l9D29uyGS0jdF0vXrwpg8m+5Wg57dp+qkvqqQtX4t4/zVhi6ysvNDL6xHPPeCdXydVO3g5r/OqAViNUDTKJ0XuTYLiy07SIgiGKh+j3C/eD9qptnk+NhnHntzGHtp+qZtfTPNGEfxxwo0tvwBhX1Z+hGcPunH38J+u037o4P3I8A/P3fAbY08/TtQBLk+iO3x2rCsn3w/cGGykGqDGLzdnOfw/iuIG7KNBD0bujUh7Uhdt5Xiv4YQrDn+g9D7C+dP185XEN2hCPt6l/xlwn69e+wEWPUKoL1s/VH8Y9QHDf7oX3Fnz0yOi/zrcuhGEfnw01cQ7PyQJk/fWILQrUnxl8tYoj+c487ef/Ci3ciey0nHUKgrCZgSZPxV2GgVXxl//HJOSoeIDgvZOTjoQ2EXN+V468L+orn+4bXWr98eXFDyQ+dKN1OWQrwySvpNX31nykuA3eKGdcyesijy63MWfDjaT1oOaDC1vX4b8ZWDmNXuz6hcac1OW1zrWRy0brLKtBpoH1R20fPBuznlQu6pog7Bom6sGDjnV4BBGdPUK05+OdVW0T1fyBh5cte6GtIvByMfZfi4fWdnmSV70+U8/f1e39ZCxes+7/fx97E4C6de6GpzVkCvmgyMd1Pf9XSk/TNzIaV7zzU9U+refntD7xzD0W5P9nl5uZL7Ry7XwdemPznMEmFdPd5PC5H2UDwrqPkkir9FrNNhRVldk6qSRk1wz7srzvWq03deM5urF7t3+Y/LntyD/GFueObm3g/nNTbqfrGsjd/AITZR5HweJv//5Y1QXN5j+/m1E/+gwHjzJFQzc5fdmZjHO59GbDw0efn+zxVUAnw1obHNVsa/QdZ3+MLW7OV+Zcl/GeKvRKKBBWfKgCR8Smqs/frPBY2i5gpCHmD5qxOIu/Adx3x3uGES+lPwrEe2vN9yM1d1i/2PEu6vFkNXQl8FHTOrBB4744ssQYI2K7NVt+hlCXb89dHXXsPfPVeep8r3h+5g2Sq/g04nGVCy0Rjhal4Ov8iYDMGvqMeqPoKF2Ks/L3wiJ3++Stg8u6eOQTr6Ri/93nNGt0mPEfNL8/nFs+1ZQ5L1RGOUEucf5q7Q/W/eXTYbKnx4gwW+vxKtRg6oRdr2Yxn0d5rdfkT/e8JDPnWr1dXd6g7z+ON/7GJ7/FR49/BuXLj+3ebKQeePRb7+S0B9vt65HYDkE8M89PHy5NX9bwF9w76M1VM3dEXf+Mvntz4d+/vpj8udI1V+T96rnD4nRMK2/fn4Tc47SG7HMIyK5LYV+W4pDg0+3qv94tM3bjB67upUPE/vzr9eCqduNYhrbP/Z1XwG7l3yl5afOGi3noeat3fCt/azmL7ThoepdKSYDVvEe278+xk07no9xV5Lv6/6nn15jelWcrbSJXpv5rWiAxuNq81vTHyrdp//Y03fM/7HuMwofv74+zN0+ng/zFgteH+F1Hjz40OuKx+g/H7zP+3pAIQMKvXvRr7jQsdkTp/UmSAg9y00HWH9fQXhYRr9CmNRrvB9ZO3gCru4B+fbX1xvccNRt+D8/f/kLhCHoK4MNZvlp0I9xP+S+bPimUxjndVPAYTZ38xjmMQEmo3t48AR3nR69wTVZvqv4VUzj6v5bYf8+gnpTztGl3DTwyxHuOvMwwoMKfXOEt5c9H93dFWs8/PE2vz2nyAbA5FoPK8h3DXlQ3afFr2rxcyj+oMNfR3b3NGQY7c+3OfhiXfKa6T+Cmqu7HdPI22ZBfQUv7ghyPqc5v76pK7fu3QEipIXlfmqrq3o+wT/3YPWkwjh39YakniA1/75R8dVxbtRcbeXVYZ6U3zj81d7qIYH8lNiv9nQvG3qB3oiIf30nkPy/slXxZMnpO/Ypvj9puXq6B4B5bfbE9b0N1a/kDJpufVMx/4Wc5l/La/6l3OZfzm+eqevVoF5o2Rs69TZLs8E6v4uj/9088/OG1KOdfY+ufD2r+34T+sqKrJc+X2d9WHh8IO+nV1eWnyVhP7JW+W8x5Jdz+lut+am5vKWGPyKAh+W8uy18B/+/sQD4HYt/ryTAD57jjeXHJ0jtrZzvybgfHhctxzTwFhGixsvq9z9/V+r3eHxj3J/5+XrmYrSC++efJ/97An0lK7xlRbdV71uTSTGAGMsJr6u8t2A94tPH/OgruGns5c7gYe53Cn77Wo74fCpPO/h2Qvslwx/SxD+/3ujuOYbpffarN1F8T7tnW+IPXP6ulvX16MttJ+7zRG/hf1THh6x6gMp/DGDz93cfP368gcvb7vvbbUYpD61uCO5rFb+LzkHUrxP5fasGV6N+1Zj+xTSGvdvH/CEs/kga89TCP/mD7K6BcbSV93djG3KPwda+yPCuhc+g8W9/fOXswyOWeK6S/0mY7YX3/Htx21M2P+5dvrCvIcutRprS9Gtj/y0I8GGy4/7S5+jz34z/94NwP4YA3tiNe3py6sPj5t6PL8K+uR346b6f/izJeLrE+W2Fr5vq/vkNup7uEJZFlDefF9NeWWUZk/x7rbcjY9mMcfD9U6o/t7utin6PpQ5uFP2+pdOy+Xao+UzBd4aY399dq4+aV95ncf3wXV740QOXzY/43b/eKBs58oNz+0z9qAJl8/OHz0T9/m6g4/d3f6uH124t/hvLU09z8mf7Ca+uD36pMdd63+Pen1rXb78ir4bqp3XG0Iw8hOanBV9dC7sJZBzv818/sBD0fInim+tAr/Hjp/+kyPWl4/1bg9dTX/xMxm9jwoG+h/MY41LA/ff/6aB2z6H+rnj2/HjKd8Sy7z/P8kMR6/kO4RPd/Zu2CF86h5d7hP+Xt/pekPP/k72+MSv5v7rZ980Q+zDC7Yji7fdvhtYnM7uuVg1/fm84Hn/kP5bx3PTI9ax0Ylfe9arEtzVprP7psfrb2uTaL9XpWcsHtZp+n1q59rf16ln/3y2nqK7bq9Nz7RuZ1w8/BoUemn4/FPrbwMn1rCD9eGbyP3QH7fNOtHcqi/FE2UsgcL248+nLeo/8/Ls2pp5pyc3Innz4HpD1Zs7ynwRKngfD/8BdkPvmwxdrsP9N1DDAydKqvK/fsnntVsQn+w3X8t3i+tET2d+6I/HJ/uKWxG12Uf2VSxJ/41n5b/H+yYWJesDxufvGnYln9yauV8O+++bEJ/uv1+7K3A/aX/v65g2KT/arlD+/R/EfIP4vb1W84OpL9/4Gc75HbNedKfsbFxo+2R8+s+fnb+LvL0zvvph0G+vFjtKHl9b3d0D1bAhFnz7fJX0Orq+F9zDzUGX027nXDnSkr7nvPspzrxp3C57fXfK/GGncf/vplpy+/8KIX61u//SQ23vReK/ra1D/s9kPPY1HO6simzxugX7JhnvJCwY8bpq+dZ7p8zCfrsP847Gnh0ucz8pH5o3wzLUq91uJyrgG50b+A6z81kLcWPWr4HIofwkvH9rdh3gAmNh3Asyh5fcttV1p+254aY17e7et56Hd/Vjd9dt3QsxHbbKed/L5+0MOhEN/fH9v9hu92T/SW/l53+1Zbzcr+1z6PMv6ZrfRoGYveXbr8lbybCtqEOMbtb6yWPStvIh7PIT5JOK+evJyLH9hZ59B7OfGb5nc57rfAf0/i3yI251XNw+HNh4IeUUzhlGfseax3VvLj2/29fMPLEl+Vqfvo9T+Gym1f4jStOi9auimfoW8W9mNnLHGt3MR22uaockgyCDKv+zwXnzr8VbpK/niGwfx1estpa8q5u0i02u6+aTk64p5r/hjWvlw+emWUT6O9DW1vFd7vDb11qL4V3r7FxXz+4i1/1Zif0w366Yq8mBQmFuHrxL6WOemVJ+vsP2oUtXJN1RqyNZeVaj79+fq9OoNEs+530IZUVU9eT9G8vr2cchvRkjxCsH3Cp8eWr3YM3xe+rXhZ0/Xuf7H17WQf/e61tO8/mF96nFj+Pugx9eWxr615Pr3nrGQJV2lWX3CymuFVheaLH2x1DXp6tfSo694gmdg9rb88ezTm00fFv5vSvft08bPwP+nprjZ6tju1sNXE8RhrFFBbhnlwxM0E/q2n/e1NORJbebN2g9ZyO/vpFsaNPllck9IJk7qWVV6ntyi1vXiyo+d0nwwzqvujmeev8mqRzh0W6x4ZtsvwNVPH743Wn/jEPWjb311vEeH+oOe9+uDPrlf/ObIL+4gfw14PJw2fbylfF31e7PnlxWvs7u78S95ea9xn9aP6sBrYPgOjJ4D36+sO7+ALE/i4LfbPotO39S/J1jmgYMvOPOixout/A/f1bn9zc7tH+78JrE3+n1TnD8qzRc59sMRgGtK/C+uuF8TuGcfHhzSeOno4RWE8bTWN/3xi5Psr2zVfq7x1RD45NSC596uhb15cGGo8LAI8njN7o4A/pP2A75YnPuOLYHbksN3bgo8W1h4EYf/p7cSXviGf20fofb+XW/p3I8M3Lcxxvth11++hl46K43cT0+OEP72ygNdrx+g/4Gzlm/ug0VfdPnFftPrOvfH90vFOzle2Uzm1x9j3mANruGFiB7efbny+73/++tv9E2uxQNf70++/LCAv1e4zwQ7Hk7zfn611sNRnvHnUOfjp5udfHpe9ylj3v314d2YNFTtTeTvfn33X/81WUdOVdSF30w0Z3yNo2rz8XLLyEX9yRMx1Xj8oI5GzHerV1ZFfE/GCn/yz//Xja6XOxt1TC6qGqxDa7ysE+Wf9enzXX1rZOk/P070oediiMNDIE8nKq0ov+fXonHUcrBBrxovztnnxvtlyJt+GX8ZM6d/frvzj+X5n9erAkP1kX6VXUwcqxys2vs4zs0Ivfw+E8fK729BeoMyOAMltyfjRidQpNcXCwZy6mR89NKNBqc9vtNy7Xvg1a9jZ//85z9tqw5/z2/vNyKT2wmMGhwqPJIz+eWXcTUzHVHH77nnhMXkpz//+mnyfyZfa3XtfBxDGeLOXRIDheKQvkysKmjHODRerKibcbNnlMSff90ZO3Qz7jyMx0auL2heH86M8mSIg3cuawL9yxTDB3TujweJomy8XHV9Jqn5OFn4k0d675cW64k1CQdYPATbMYG8P+RiDdN55OS471QPsLD2zx+uj8eMo/7Trqwridmn0Tn/c7JmlUlTFOl4J3J8lOh6c9jKizwa2P+oA7fvQyfVT/WEeeji45BcDHO6PpNXhpV1H8O3bnIZ0uuH5uNbeZPc63/Px2c4vZFVV8B6Y8/12HLk3EX6y/WJvTEeD4KtH8Z+ONrsTvTCqscMJr+j4YH53vWJ0/FtqUnQRu6Yi/8/d5Wqw+sm3G31+trTXQruXSpXHbw6ll8nr/qbQeBtVRZDQJncX1QdLXmgYOizuT08+uhGnzynOr6f4V2V/vaeBjfOSnt4VGM2buho18d66l9fqfF536kGJ7fN1J8/3OvJg8TpxXX54vNLVkpVuDdvct3CPf96/VHfdNQtnJt6PnmK9babd3/PtJ7Qi1/KEVeOj4A9djpo08NDiw8Pq/769NFV3dSHKneKxz3Gz1jhkezXOTA+tBo53iDDd7/mQ/z/8G70ma88yzq+wPrwCmM9vt86eLuB6PE+/PjXLWaOv714+/bGikHv7jP8OBmfd3z2fNmkHz3PqNSDnZzryU/j90mR//T0Eca7WTivvmp2fWU2b7N3v/72Il4PBU+GGv56Gbqv79M+i9vDly/D8fDxeSwePnwRiN/98eEahIZ5DzFl8BpjfHk4J/olb/TBW3nN53dSrwt3D6eiUy+w0g+PT4F9+Pw279O5jpWGvx9qXSfzUO01Yp5ezPiSIO1+Ye7hVtjt/sbA+TuHnuSXD5n7h8mThPrD5EkOPFL8+KDXteT2nNeHycNC78jT8dLbSMgXlN4/WFVlna+UP8W+X5IujTvIg69/+sTk7Y3QR7WvHyza+xh8HPKU2yPJQ1gZYvRolJ+m0BT/WLr+Tz+/e411z8H3K9x7fqzg9jjp8+Mlk/cDW937g0EvtecOVF8d/Onp5FcUaby1N0z+UXk+v+P83q4izx+Xx++v9H4Yw8GD3jzo0VPdeqg4eoZrtS/1aCDo4fzM2Ppu+5/rFfaIg0a6y9Rqbq82//nuYdf77jzuUGmoXlnVL/UYJED4IzQMO/x9C/ZD2b8Aou49DBWHQD50MYRy1/Egcur7JIr7FkZ4FIL7DoxAtgt76BRBMdj1SNeiYNjCIJxAbcpCHcqZ4rCLTEd/cA0QY+qfRSNVg6L4MGmjEIV4iOdAhDP1EYxyXQqHSRQhPWgKWZDtfW6aDJjzPtUbkSMTH/Hc1YPeZvznOxtHh5oCWi/o2z8WBKaUhTi2ii0CIJyCRVh6q55G2BmatDq03xLrjebmdZoEXhIekRBYMdyCZg0N2oQWymrS3CGkVKHANUVRF4IBPBMR4qQlFkvmsDwjtlJBuMvRYqZmh7ma+MLyLBwps21c1ZUwiQpXZbeGhDVGQAhzzsntwd9BhGFpF3HR4rSJUBq1kdE2IbXMLSWeFFBzsz0sWju7sJKPZmyxYTeMO5Rba7WhT3h3vmhLIbB1fBXMVui6wleWHwdKQEhJssHjSm7K+WyzK9ZwkM9P/NYtjxFiC/U0tmRU7banyC7hhNAOirqPIyWZpj1fGDFwJqik35XcHGe3uuggaxqv8/3GV61LRko+YdBGuZllYtDg4am9YCzBslq7b2yFs0UrccBA5tHdJZNzEWyaaS0AJEW5U0chTBI7OoR2dkzEmyHiZsWlpOBLPm+ZC51SuvikngAC9GYAbQtBw+dn/TIPHXreBRVAgiDRgdQJ7P2LAkzdnNYoocflS6EgnaXMmt7NMZIDwSMIDvxW6DTI7TUlOWEDBwF5WAhpP8OADs3OHhJ4M3XfLwjlMivwmd/1WU7q8RKrZkJLcrPVfgbiTd7LVSHi1DTIC+sy3VoLc2VhiJsdGzBHLDPQUQsE9yc17wdRYEd/s5ofLxevx/WldKDbi5lSupH2ui1eaO3EQhBzLtklzaL1WQYZNLpoZuynkIwKS9BSdeasiPWKX6wua8hMsmNH7hjCOflSlU3X4Cq3pk1K8j2UoWd2JUYBCwqWeqKiZK+Ty2rQWvykiWkmXdabpZqc7U1cnjYt1rhiVEnYHCKzfguaqKZZ5xDM0d2WV2Bku9VVt3ROLKXbgXGcr5Vz4p02QGjk0iaHVBO1VGBp0dKmZ7VScdCMnm78QRaL8jInwQ5QFlixiWd2Rm63XTmXoDbuoksk1TkKddaupHyi6YGUAQEkbFH5AjaZovgxcVR8gJ77mYliyqzA8BBEvLMhgGZPyZceV2JkCRIq4HSzDgB0qE8IsOtdATj7QgjZOYB6FxJgNLSiQHt66YDFqnGP4ZS31ZSDpnNn7dkAc1rFWDRbo0c+EI0IBxduPqi2dJYskNYFsTs7InSoyIzXz9UlUn18q7JAokLrBdkVWRKJlg+4PgZuLsFZAuTIEFhW7TVSpeVMcIJLO3OyBrvsSfEIx9xmNWuB3gLRhjbmRN95bHYo6chNysRfoJIXHxZYThpLz17rus1gsphozkZfyHYmtgrdCnlPAyS/N0x6TehbFjCTqUbbGqVCc8JMziLlH3sUQw7KhqY6FD23zmadMc7eFgl+B7t9VJi8Np+Ts9Y2ExWls3krR7Es0KclROsFEqAQrfp57cd7iyGnNiPrWMMYa/SkqnTMZr2TUJJEilkdEj3YGDOdgC8X3MmZs58Xcu0zjVwfQx7xu43X8+eD6htKAR+l/cwWtYUxXUo8tTB1U6GC/oIpHDxvgPi8PnRKkPC0U/KZtk5pDlEjpsSPgLs/nPzOWIc70oz3PsiaVY0szJJTsAZO4HlQ9zJDRBx/ufRlQjvCUQhtNVRIycU1YOEf2TDyrG0gcfN5mUvFmYv4OZgHjeDI22QfGsepteQMmIAu0cbweOM0jQHRr+ckzND+Bg7JNWfwy9AoCabD1gtWKci2FvyNkJCsx9M0l16QDSEHCzzixE1pLgQUm54ABeeMHTW3IYkEuC107JHDMV82hR/a0VbSKWJWsshOk1SONOjtiqm82RwCOHizVQ4HMVwn8aYKwoPEXZzlNM+6rvfPQMtCsQkAMhISeg6SgKMcAE+w89MuNJpG1crGk+P5FGHpnaRBfm7R8hLP4jCkzjHt2lSai4V6iWtDm4v5Mj1m2Z4xDqbVQutaQpeXIchX9OzYC9pMbLnDYshyt1llzXvw1EDoOqRI55Kd4ZAPnFV0uOBVIJTBDOATwjHDfPAg0Gk5axPjHC5PPVDQLSzt29jCInC62dT7TekSONVelqupFOLLVIh4Zn7J1uKWtVi5kY/4XoYl0ldpGiUcQNcpHpr1vrDS1YgLzWXPViRKHTjTIBUxyH2quFSxHF1AG9ysit701toCOi8sdy8L1iKxt4EMr8iOZLKDniNoI4SUJPKDLblOedpJR9s8W32SaOjgEeESM7RNuhOa9WpviVN2UxaHqM1JSD2Wc5FhjEYluW1C7DpyltcXqvaRcuVmuXpkUrPqpvqZ4zdSsnJ7qYdnYHPiHbEIuibUxaww451uwq6IroZ+Aymj99k828ex6sFrcq7LnSIkgRYeamazLdftye2zzdw8zOeXuVOutfNpkzlralpy6xVCx9mCjQqo19aiqpLu3LHsgOu5eBGvkQCJOJvrS1pCgtVhqeXqaj8vEseeHXLVNC82d+rM2YaY65l1sZhIQXEekveqNTs1JcXZMjtVUAHQZRUDYtRYeAhUWIMLw7V4VcxPWUD2qioEnBsmMVjP8ZNqMlukDGKyweZihSUImLr7rtzsF5HU+xAPHjs06NC96skBgoIhJldIBicQb/uQ3c6EWVMi/SqQUmBuuZVsWwwuQ0wS2zsFywmV4Wx2Cpqy6m9ibZWkwnGxjkpIL0SsmMltWEB0Q3hIRSpxDJIag8JIcyGX2Ikrz/TFlM614ALAkhRyj93M1TqW55tmHTnHfMus5lZsWGwUoXEi8E29DwmX1rdhHPLm7GQpe551IkPPV4QR1PzComkYF9ZuJfEXPxQJNpCx1XFNKXDQzxQQKVpku9I2nIEGB2gerjkSWuJnyDlO8W66tmUqIWcOymMXb8byXNHTBq8kYT1LSG4dI+AUl9LFvFUI5BxzGpqfTxDtC6wKHeTsyDJoBYMprvncMLyzcJeKTKMze9UrQW0BwnSjMw1jzaNUnAfm9rzCpMVqyhuitx6SSXtuFdqSc40mYo0mY8t+4zW6lXX4sVxiktGY3hxaVplnZZdj4TR2asGXOtt7mUBoANlpIEmfi3WkbEM/6I7yVghSm0+OWrLkNLC11m1SxHFp5qa92QtzWs23lqqFNRA3w7Spac+Fx8G6FROmQHKxMzz6EDlZ4SCR1hLmmrBYYrPalrk5RREasAHXdflGygXD8HdcaGWWGfrNEd3DNM5inhi1m/0552ULy9ziwCF7YJqggmMXxjyPj9MGwjRvppkXzqyS6dnEin7QTYjvcxajLwUD6qtptgZyh+BZZK9xxeBEVw6Bdqm/SSN54cmajEXHQYfUeCs4c1YyLkMgXkYMvbV6ZxZVZy49bEzb4DQVYpNiH1bUZbXT5tFJ2C/JdRcW+57R6yxZrjfyOdpCwsXuN/TUDcvUXeNVujPpgGT2W9GhSZ6UioBWms1xn1iEN99D8Szb2gOejMF+OZOSo13tscFH0SzBl80SY62phadln7qCAhLLOJrnNa3zghsXepB4l+Vlp/fh0u9CRwzqs3hQ6mTAWXtEP0gFE84c++QQEZOEBi6AxACeVrAPQ3KVSShkr+g9OLU5oMgQYlE1A1P3Fhiz+XTvzFthG4tdhffZliV2LgmzHR1VqzaUqs1OmVlTADzrlMDsV1tbtcWVA01TrY1x0D9hpqcbtk1cjjZPrvttCMPk2rbJaTTVl5BHgkp8XChwwsrMsueGiHmi8Wq903QJ7lJKhStTNpzc07J8gR6Nijs28Wy/P59FED/EDs2IS4l0OtkHZO5cMGdLxLrDdpbMD4MxUBXcuTPMwhnL7yh5DtlJC2XBDudWpZrZwQGXFiTaioRygFPEQeS9KQseMt8fAOR4nlVNi7Kxz6yP0dIt8q3TeAnmLmYHauOnKLThgMhPfQDSsIJf4E7qEZZwQahDzvkMc0AGSx7MfR3yKN1SWRlbpw5kYJu21Ysr79TYxxbJPAEFzVZaV01hYbtUOBVYz8SFqhzRGRD4De8hoVN7A0BTDEHyfSjIxHPiOou5sdWg5rQsF3IE8Sf4ZIFM2Ha73aVYtCDVEjoK7N3C7rLmvJ4XxaI6nakU8bfoBoNEMDGWZq2tAoYCy1rTQPFEn7aK6CoMlLpwmvNxNr8wlyNpqrjG7ZUu60hEI8LWhc5Utl6eSrpZzxlqThMqVK8v6E5zoKO62y5babOPcWlr7dhpfNK8zaw+62ZhOIK42WHO+tC6ye5wkKZaecoNcY1SxfE4dZjLVPa3c5eFT0HIY4XvN3Qkb6ScP22n6Hmxk5emwGfBYSsmsgkddmt0ti7zAc6svDkptNAU2aw3Aod5srrcMLHISUsGopi9QswUc574QGLz5a5P6NxqQi92ZE/foHDDdxpiUGsIC3TdFRuI0LMhvPXeashJgShApmxrLVbhoSp7GdpQ5BArhrjhxGVkZcdpuwPWOwBdbwyrErID2mrCckmfdCjdybs2XLCtEQcheUj3e6+jSxU9SGWVww7mLcw9IhTikGWLW3Ka7TaBykCmwzcQxM+m8eHYGHKUoAjv7XWXI5eKv2RFQMya4CieBDy84OHsvODOeniEsp4A+Gk/ANiOsE81c2kbTqezhTpjdF1k/XNlLenLDKj2+qHPiXVZNyLNKcmZZWPNYerpAj2wQ6LgI0zRVilWSBa1Wu0524RQLlnQ0PJSWVnL1QBbtm2+3dpimPgiyMJRXWOnaKUe1PXZYAMxyh1jXuOHIKWZOKkqIlMX1JKHozmdH5T+qC09h2DouhcHAINsAcFoqtQP8ni1LChMv0Q9gy7pXBfnPbbSQ7Lce3HdHyJrv/Tml1TCSIapzrwi7DKSp8B1Ufekq6/VhAndICrES4dRF/U0pArAKqn3uz2R6wtWZ+aNszYK4SAlFu30mgGKYSgRPbESQ8QxdzSnr4WppYisIS7JIHBg3NjBiue0oStFks3D4gYuobBOzo4WNRi5SZcLeLtWgQum846/y0XbsHy79/SZ5HRxURk7/RCEKnBY73JpGtZSXII0LqkJjOYZBEcQvZny+HRF1Pb0YOBYnbtAskMlbYOjYY4m6jRqaOkQtlbNSMqaMtkVoiMs326OtHIwqLl7nlM4jS/w7YqTLC+wkoZGnbJJyCEhYheXKZPMMEmF+b7GWlkiTkeuOOoztT9fusBcLTZ5fpg19myAYYm0nhLNYu7RLuMOmQhVrfvDYU6aZhDgOFkq9Lmd+3uEQXxCC1iW3aWkUfNgXENN0E1D7tj7egOcSjMesuC4SM0VjvkpnC+TIBW0ZptWIq0WUu/NAeNwKMoe47x2v11LfQKFAZfjIkHQxn53TqVqj1poeOIxe8crQ4KitxeWUQR+ywZkNqSk69mm8Kpmlge1K80aEcoTtN9h58IaPgYuqupLxZB85nBmjxyz8clIYc8Cd+Rl0YpWAwSYwd6Fh5wsV+YHkdc3WLw78WGjNWDu6sTmkDSbWW/X5UYrmOVuq4k5bZ2wdA7WB1W0uAYT5MbzEznh4l0dDg5HO4rmECiwjayvNcGH46172lu0yavNwl/TUIXynARuLSBq5sRazhmZ3LCHVukhAKryOoj37cxyjjyyPsWuKgVUd8hCM9ro+SXWMIs4BHNqcfKzi9GBBIZjbaeC084HLzjouvksa6M1tLP8cA/IxwTdzMpAmeLIqtq3U3U6ky5k3y+ccsAv2jwjWT1V2QCDt73o4syJ2Kais8eOQ8BfhDN7d0HKGUrxy3WNE9uoZIWstXYE0WRiBqYXZibPS501l4W22YKRXrD0atcTh0Y4T2N6VSlEBrBpwPR5MsuJFtsFaJ+XXuirQlIWPNCEeH+SUYQxKKA9HPZDLmRmgMFehrQBIiPNklaRZm+O5F5ZG2h/pjPRwLboPl3wWQNi2+pA9sEWStLOuZCbtXvZU5UcRHSNNXjX9/nGFjhitwCEJapTYh1R/gUjlHCRrI6Hw6yXUSifSguCa0+hctilio3nU4IS05jECkdXVll4UFAX5pQVNXUvbKa3xMncbdZWtdtV7FyaozVGCHNKUEQn54TlXN2ivUfTiLRluTQyKclJAX8nItsuGkxrhUtnGbXW5pGi9x7MFCK91ee9utlAxtayHWC+0dzCN9P1NALX7CrX0ir30bw1LifRzZwG3O3hM7jdSZWx4eudQWmsF2b0ClTBGOjIPQxS+1O3XW6QtJnDSd9nVLxU25lC7QIp1FVqOz2sj0C330nEjElXUy5hNwiDZgbRuK6IEyLhIi4cgMBMCk8A65IOCAoMStHSWvA3jMlIPrRmtzJ65rcdRnAdD9PtyUiKc2/0AMDahLusG7NntxZHFNOgQzxPI8dVPKoWfAD1NwHOIDDSwaTbBtaWNmN50VktitHSbjBIBEF2wUI3ZtpW6VnQkDpha8OOf5lJQrnHUFXK3QWVy8WA6pLTJhfpIcuRCEYCEzXhOwbd+2vmFG68SzAjYcOCcySLT8YWrujV/MR0Z31qLc8LdB545xrM+DDuSsHF3ZB2chH1cqTi3dBKbLRzGJzlTXkuAsUM14ThjyMghTnlCk20n0pTX135KiMkGAMrYMzPfAHDXXo3R47BQuAUpxQ2cUeyZME688EsoU1YZehlDXoVpDWDXfegJJxkszpAtKMpPBsdZztAw81dS6uKhroxDeiL+JAvVHBFgzWskFs8Tn29bZbUkmwxR1+IiJ82DDklqhO2pOSzLOCicOzjdl/kDgnMs4MNXZYcBZsG3JrcNmkHF3vZz1algeiNoMU+Gc8TvYIuLk0aqySCPfZEZki9ZM55lJtGEoUu2hpseSqLVjeHTHaabi8DJCoHtHWxeWjVrU0Fpix9dziXroEvE9CqLzQGdWXK6KBlD8TH/sGJ8lhdU3td3vGla0cwGPK1WIBhnKaLo74wfDA6hTUymDgFg7ikNOBp6ZZ8ec4I2WW3SLs4Z6AE20GzQVnLYrqVCLaC73nMBZnqeoDp00rThTzy6hO0DT05V7Yb2TcXKbKxdgeGQ1R8xzkLRM0P7FG44NCxgXgE9CRzk+/c4cd5XdXooeAD5SQpgViVojDfUTUTKUs/6fW47KDFHlcEa42n83MoUhdJ18+evVkvW4pNsC3hVmmkEgQjMpWCDHF3xbvIEZTzHUUF4L4hl0QJNXZ1UAbEZsfqAuuU5JTBZhrkIKftzydYJinB78SCF5cRS3TBIhiiDqjQrp3pZXBRrUpKAq9Ap5S6sS/K2pVnKhVtwU1EgoMhqSTGGBbhuPkU40MZm3ooc2lsQCUv1WKm8aTieQIpi+B8Zx4ID7Z2czILBLohZkWkEaZ4TMipAmX6ADFhqgnPAODr26NueyBWZV10yk7Y+ohOtZy7+ENu2JzJyLGC6oiwiG8bXhYfeJuwAAPPORY57DtmcRH7hmnrCIO2mJPby2SnoPJZyafgricvIkl5lU1A5WkNhTwFNBG2QSBjP1UW/UnX18fTdosuETCbC6xw0KYbI8QyztuUxixxLm2Rm+asg4F4Z4DUokMDioPWnZ7tnITPTl1qnd3BRiqZPh5XSr/lO3JhH6gc0rsq8Wc9vB8wMdxKuzgLK6466rq25C7ujgNbz+jI7HyaSl2I1IqQYQmgtXha+aLpgeet6PuM2/pgo1hnYgupjkYWRzw9D7GujZIL4e0yH1quSARHOkEFjLQj4DPmFIpOn8/bHQ/YcjJEkM15jWNDvkF1zC7zbEqkDDOfbpsNtznj6swo1YsR85TjI0RvdId2yFexloFJnsWog9PrZ4Q+43ZJi1uEXIgUNJ9zhwXFLbQyj5UiBJrMsdlVfEz4CkjUtS9DW1TuBHEBg4Fp8MmU1nSomSbHai1pZMsXyEpDT6gu4EsVVCpb8SO93xy6pNXbExkfY7n3CO6CH7r9yRkwqubM0oO8VyWvsWAU4qcU7iEghvr6YMZzYLUCMMZc8zSxxOiD4g/gFg6mYloKJrZjeue4XjAHchm768Mp1kh9MaMZbDttFt0eA+SOQQKvphjZ8c0Y7HIfX2MsUxoZrKxcWgh5ec8OCRVP0sVGXJkeX6yg86AyDKQB6Hm/sVNmCSzKNScBq1xB4styQSK7ZFNM+1VkS63NKBy8Xu/k85zvGT5OeyUYvFhSXaxyUHmmi3ucB0NVLZxdyRBhvKRa2gXSITCSaQ5OoR1mrWC0UaYoi2c5OmtKFDYOFz72Ap9bLAdHd9iu8c3WDACIH2xTGX1cv8P3ZZ6yGNwCyuAWQIXxGtHIMwSE4L04IE8olM18jWT9LKMWvq5KTtFqdYPCKTcFFya+ItCFxq5dlFfTmdCc0na59BZdbhBEVSaR3O0S4Lws7Wy6xWt0SCmwoK/lEyfFi9B3CQtZrY6rwDR7fTtEeyrcI5d5eUGzE9OrfnA+a/MEhPnDSYYxXM3zsNyVIjHvIWpAi2fpFDWMc+DahWkXAcIo6IFMoWiv0JB12Ti0yW34Yrmpg9VMQUEZtpWLvTN4xPcstoo9eakqLFOnwo5b5DreGTsHWKlrXXbmwe6yT/r4EorRCmL51ZZX15pHrRhQIlC0ySDKK2tMz1O6krBU6xemhh66YLOBF3hBhXppLbBNsIppuV4LnoHj/aJGU1/iGumckGQ7hbnjjjl4S1QrlAMeWtZhejoRcbPnbU9WU3jdnU+quzXOaOZ6pbaoEHelr0t4Tm37M66tLU8oB2ToRW6uTp3c4LBsZ+JQK7FT7eiF/eKQewEDOJ6/voRuvSIiIIFplgLi2gmX5BnfDKp+AiKvFSQlzXW+14uEbBO1CDgvH7AiMy86f8hGo3Nc+fZ5icLIac3t8ero2Ha5YI9dX8lVzc/1ek3k3mJ+5sTdVoFJq9enpWJd5ODkn1f7TJqdoeUCq30pWZqB1zUhBp9LkG3LDeetzvvLyR7y4QtCJym5UgsYmjLobK/N2l2QoSVezw7tqmvjaCM6VeqtjgwZmoGrn5y1TOrOeRselxJlOZTPhUOWctiGyfJcHxZuHB+I2DR3NlJL2KZEqxaOd+YMWc3YnSXIm4NP+/0hOxBzbmUaOEtw1KzXiYsozQ4Rx03JthzgyHIq0QycQ4TFVDp5tD22TJ1KLbbRQsCoVGH0lbrItUpjzAXsw/iQGg1msjV7Oz7twzVEGZFyrOMVYxoz1Um65LRP0J1wIlRgJ2ZQuVnIqkDkA2rB+2DO6Mo+U0R0bzBrbG26q4XG5NpR4L3zhga1xC2Q8xSSd4i982AARjAP3p55o+pEJGwo6GhzIZmvGLtRKPSgwAtaQN1UgXX1oDYp4a9kJ+6qVsIaoZANbodwpz3Z7pHeaQk+m27OVqkH3UIjEWBGmPQKw1k4NeAk7LoYFXPUYBynOyc1MeR8NbHI84ypGnBhdUeBijezbLY5axIGAfP6CKzSvGC4g3vojufdkIsu6vqgcykMUJB36tiTAWo1oRC0dUTUvbcmHa5CYwuc1rvjKRe4BloszP40eBsqJgp2A8GOEx+GNMFcV9FBDD1+SRknkeRMYzXEfFo9G85SrmXnaB60draX5Q6eAghMcp0r+NwQe/Ckicnl2tYYdNW0fJ/gPRt2Zx9dSgxJ8pVzdFaX/VLpdjBwgVzlQh+n9WJNm5sdOM+p06Jh0uNZJH0wTEXNXqGxZGMef3ADM7BRQLnUpAwCCM2DFVaFywVSdTMBxUlQHaBAysbzkgFXe+7s5ydt5gRKifoALx0MDDNZmNtayM5j3bwiE8imsj1L2A5P1XMUusD4Grxs5BMp8Tix0qLVbJNQBKBk1glI7VMdLjcS6ecY6Xd5jwoUQJTbOcHQea1l687gj9jqYiCKDeXzOIQCBFaYIFerjFlTxKUO0GzbTiEhCTXamzUzikV7ucHg5UrDT5umB2KQj7v8mCywLUsVZ7uZlg2GajYWNzg+3XS0CoW5YTUqdGjmNF/Uq6jq5BDwqNTdQA0jiwbM8X3dqDqZXRwBPJeIk0ZLKcJBgQLX61XHMrwCbGfCvC/mu5kl4s7CEhKjPsCoLKFr3ulXoiwSNQbjxYkrozltu9iAD1T1tJRSHMLlIY0Jp91yEeaes8itgjtUQ9peO34SHOAtReTzOV8nQxYd8poXdla8qVAOj6M9vqgy/HAKUq9NzSFeHFdlW8rdxVKOcCDiwiLrSjRf8HVNLFcEsivrbkcUO2uGI6Fz5nSQEfKAPerlHMarZbUHlqWPGwq/DRkwO4ai4Qkh5/rIcQ0O/qTbg0odkD0SWqlf7r3NvgVsTpjDnBWTpbK3urKqgVBch046NfLQBjaQUHv2sTlfWktbEccWzhiZ2ckHKSqnYlTj59VMJbcgQh9sW0d88tQuUAPwu1hKtDilUiOGp1EiNPHRtS7HY7sj6yJ0zcrdOlvN3wjwgQhwPO2Bglis28LeqdUs61x6uYM5iurX1cn3kRmJESFAylQhOYeOwwsfO1JTxWSVDUgMScQa9TGKNC47/XgEUzKAOLCMWwpM9BkYwWR1UciIAw4g6Wz6DqrY08W3On5ae5QCxA7sVjrBSidr2+BSkMO+uAJduQF3mLEjQSjDG9iG0H7OVq2h99rGjw1vpTgIsbQHYmt6m+XizsdFH+nCy1w8L+QTIS5XaQAmToTwmEwjZCW6NgIlxAxlNg22MVHEELYNmAorspmCw0xPx6ONmhYQblbHRVgAmpCtqPiyJQrdAYRqcIUhdpmDjeGe5Z1oLNEM2XcOMjsRyBaeCubFkXcooTFKLBTn3cH0duoxqzUVP26NIzXvILXMK12zs3iKekRa4msnd6yMQlKFZ4DeZlxGDwNMXosceWo4UlGwrbT3dYE+qpW8XudzF193PYFOtz0Oa8nK1PuzqTXnsKs41sxDbCHnA6ifSy1i5E260wDFhyIpmcbOMscbK3Z10LGJnXQIpbhdxZJuzJbHk+EeL5EQeumabYWlxWaY51U7J3Vg7SKVEN7DVokDDLA+TWMF2R4gjaJ96SBKpLDpIDGvpZC4XCJmw5zwc5yn5kUpYdHfRQuIx9wEEMKkLeYKLNHJ4BcHvFSmK99YUzKBLEiBmFatft4hGcQu2XUdWZtlylG0zVNpqeKyLaT20SgAP1ld4KA4FvFGOp/nZxQVjpyv7oq4x45Itp3ud+ZczlU2F1YiZ3RRAkQXcg4VZa8s2mUdC8TOS/TeQbTVmeytJakBbdNp6QV2gqMWkhvFEDLImHVKgV+2FG2JlblS1QROZ1snjxdzpO377GhCLGydWbYld9W+XhwIaQik/BbttZytTTbCum1Srk+sH5IYD2NC0ZtDOmCeFnlbhwebdBYgf6GzGVuj8yVdY/MO1x1WYhtKsvezI05y64NEVIrRxOIMDAtCYPl+OWcPBifEIA2FRUXvRET1iwK3sB0W5cf2BLNYrxLKtj9uL7sZRKlHEzjGNC0cQQ6IEFvZy6qRxys+3HTWtB6y+25mrubnMxUuGgkrXG/Bn7Yoz08LjK/oE4SvMvJ42rW6tac6QVbrRphdNAuaxQ6wrzdpjejJlFrGtdwLrLtarVCuXMcuquCBH+xhdZsd6C0HW2hIBwpcTDV8biUyZ4oJvSv8ObQv6WVJQxhQ8/ThDDgG1lr1bLuWEq5JYohzdkPM1M6rTbib0RTZc6yDwkvKmm4a9BLSZhG48AlcKyxQcUA7y6ay5yM7k6ai5TxfoZeqsIxsjdFTLZCZLalnQR0hG5IMQ2pqIuicY5edKiqNuF2uaC2PhMAYPMjJ45TLoFJSvPGT+QXdbQymbKxzajvZMoCP53a6E3aHVBzPdkIpqZqtnmpbT6yOB3Na5VN4t5Rj3XJPgC9PoxYthcjYgnON2UOHym3b46w10rTYnJyDIbHUSd2tKTvDT8yFwSthntCeA/JJ03oOa2w7lDTDLKk1AKDxwZMNKcW8LaKdm6I+uaQTqVWyw9mQQwusDlGQmvVut2Rd/7jbRCuz4k48JhYDYtSTXUfX82iBNAhJ0hanRfCQ9jY5FLF6LKKRaC6xk3MGRUjo1aOzr4XGXq87vBPDy/ogm34wDdDe8viwNqK9dQBXp/VSraRzYdCQv1gM4dmmpmzUBwkb7mm4M7d80MIDguV6WuBlaogIC9SifTiBMXfJkYkrSiaKY1GX8ZDLH+dB0bLmlJWWaoN08ra6OHFgi+7eCnVpxiynor9pXSHcmmp7Cc8FqNtynsxqToH0He1v7frSrF23YJYbGIpm0fFcHzcGCHFZnOZ4qYMSDKPFemaCnqDNCguJi9yiCS8BiMIQZ4Y8o05zxw6Bjd34fijnYouSHeDOkukpHWSg1Zva78nMBfGIh8k6Z716t7KOZkDXTS2CsdeAg7QIfwkAJAMBqOuSBDMFFhroBBELeOBK6qzjbIr4yEl0SXs7+j6yqjUW4TbGLLIGfziLF9t0SnGqx1x8kRKCJLAg6sD5pyV5LKEWBoku5YB+D2xmpbma1YrMk8A81XZ2hUBlqc0uCHE05imD99PFuTiS43JheRRYDlx2AaHEM9zFmS5XT25F53l7qSHjXMiBbQT0tFsvm8ITpwlvuXq23AXFRWeRxcpycOfSkrmwvHA5svLKKFsLNEbYYkKqgh1xGOWhG5DbxUsAnCb5gMqbSC77er6m+jTaIYJOz+kVT1dmx7fOoh1yRzOxrJlDz+qI9gkEZMQdguuesFRM8tz1SNJre7te8vMjucZbTCaEY250q3rbsvPLDlyJJlKf2mAGxA2DOKIkz7WMaXRZVPJosYqClbE0iF0i5iQGDVmPkxew1hwqqwx2PmHMVsnpYAzGOvD8BBZikh9OB6kDdTpvMtOZkULaxP6ZKZatvV7uiHKnG5nWwqxvT3shMkXhZOLtMqFIiXEErWyDNqLEw6lHhN709tjynJbweu6shNNFzmBSnAd+PQUsAXJBW5iSp2VXbD2/D3ElhlCZQpqUOe+WC188pc1CUrbOhsMsYpcShCBrQdeL570nEM4usshBOdPDflmXq3izIzlla9IuktgGoVxMRd2XSQr4fEucDRLjllnllFUSN8chzSgsL1UPl+WWsmcVKg/y1zDd3kH6EcQafzqkxu6GKeeWmUalDouCIA7ZyJZKsMO+Iw/qfMuUOoDRMSJv5GMyDWd21R8uC6dA5hdlu2VTlBUi+VwztevHZ2RauhuR9CQCmPcnvISojTNjnA7Hsm6zj/dTKVhFstBRtHlWpskpbjZEacUtzPlVjFJyJZmZyAE7M9tiC52B19SBHJy/kSKQzEXAZldrfU+fTnBNmTAVXFoOgjjR6ZhwExYDH4Gc2/dZvWnyHeNA4bw/4tsTuVrN8LozTiF3zC5aXV40l9UlH63882IZtkeTP17w6RyMDbTJZblCEpHUolOMQxJGzSIOOtC4TSrg0VW3cb4O4iMFAoHJO8qAj1VdOAECszxFDSAaKXeKc3VhOroPFOihPx+WVlLNWHxnzA9WfqaA3DqVUXOGi5O/F4a8PqmzpmVzwJu5jrykphEni2avQXpJUk3aeM4m5KuM2++Cw4bb1yGe7Rt0wAe+OkOIqQebvF9ULrtm49WR3IM6tMbKvaOJIjb1mwMWHQgKjMBpKGlg5gunQsvwmrTX6dHHtClKnAuSGXf/oppK0mpaZS7HhIh58neWNAc7eAv3ru4BLmq0RUcuhLI3LwVtnrroNPVjXPdn8JGBSdBc02Kbm0OQ7ZDe9S9AiBe0s+JbAJ7XeC13CY5rSrak1kmx9OvtRl/xy8tpqi1d0Y8tR19wEJa0Amv3rAsV/Rw5KCLaoYvzQeXcAbDvIH5IRy9lcXGRaHPsLZ9YUTByiduZwppihMhmS9WSjCoknyaL+QFAT4N5YnqJGCdMSJV2xnp9ydsHj0Syrl2keKxZopXhaxYRrDM0AxpfxIDN2tahRtniHI8jwJB+mGi4QKY8aLjCEit5sV6Xh2Ou9PAsOpkCHedSzEkcDqhZs0SjUxGjDJM61ezE56Dh4J2J4yf/WHW4wnBYgezjaCWG8qKhKfRSeOHqyIFh0MRsWJK6c5yHZLa2Z4chsR5qhrV+svryUMGE4xV4VivJRT6s662qmQve0RxGTylgBsF5vD/O1MjiF9uSuCyXvAVlq1M4FzCaog/8og7WJbHmLRNQ4n3mVh7RqTO1sBeLAzZv1tKyyv4/js5jyU0oioIfxAIQeUnOGUTYkXMW8evNuMoLu2rGCN5953SXBOITbQBGGJYggAZBHASZM6GC7mG/0tO/ndzbR3+1EUrEW4GQud+0keIMAhziIMISEnQiSVuQePglP4kxLsA2F7Mk2qW9OCpNnAx9fIWRNoGG9B6ZNuBTOuCXtVUxku1qN+OZrmgSLEGF4EmEMyKeVyb6WavVmrBkKw8auuASNmrZ90vLNi+f4RzeM6KUaRTxDpRq9fWmI4irYppYZqowIc03Q1oCMX7idU9ydAK8PN1bpX05zhKNSg8PtdX/YJEnBn1D5ABFtXDKZkKMVMnmaSsHXnhQDy+sGdxFWGHH6Uq+YKM6A8e0to+chJNo31nrQXlTVwRcq9LBr2UraUTzzMNIEWUmEhvHQ+hA2qeVATMy+rHjZiSIFYHh+4lnM96FoFveIZjl90z/nbWluYpCivF5rb4EYMtvVAvU+Ymg2TLsDd/H4NPuM9CKPcqowAD/altPiPEoOMUs3XUzFuNYYeox0EW6Ub8dGAL3KvDphTX0DHDo058UMbRSgcLuK/XPX1+Ky5T35a2TyRKzGbkxGt6KeoO7xR7LQXC7eQ3mQ2BHS93BL4pgUH8Jq/QeNqhbWcG/b8LqZVuALe7KnBmSsOYKe8C4BvXtP+8cDWRwuhnByBSIZ8TTDO28u+dgmcBPybeqyzqrV47N41aLB520LDA6RlW5BdrudboIZogMacs9T+UZAglOU6LUn5DCt3aM+CgKACBY4I+xIBp6aKtSCFEsx1DCCgH6O4VTkEeqGU1d6Qj20IFFpdZf5lM+hmypMIfuxLDxgUFhWmyV4jTffK7rsJeOVRJmftyHmvaES1qH4ANyEGL5FNMuiudp3yyZIAf+NjO2iEPD8cFc3HWxtx7t/aKQE54yNhfE8sbCL6C0Ttjf7L1qgBfyPNPgIOpC8ZFp5DcWaPH6VvipF0/rNJ1ZYjani/PwPZvT3EWr4ZZod8vj1CjmpswJfzaPRwMzJqcQU79MF277Uak6xSxH1WLVx6SalxGcYO9OoAQDMaVwVKQJ3xH0I2R4Mqjc92CoTUOeMC640dfyuR2/h4R2ZnxDET2I3W1V1XtVqOATjkS0B5zMMKopTgMd0dveXCdQOJ4X6Ymgi/WUZi96yZt6C/eelNE8wlHCRjjXB21nZAFi4APjcNevb+D+PBF5eecTFn5YfoFMTxMtd8A6cG5hQLwHx1jJD+KVPqNorxZBGSXP6KvHc71KBo8VCJMX+S3AlMEHIcX084B9/7k/4IwlHpAt4oqPNVwsooTnd1GEht+WsfvgsAwTv+uo1GXJKo3jnvg8k/UzuuJOEfep6qO8wp/VxV97bqfhgJCzLkI6BjlzqXCx9wKmlQxxrEPvHfiBakTlALe++WW0FKmuh0qxWMBnV0ktabbpqQURpKJ4hON3KAbzMdmdphW1YlnnKKL0DEoR4h2Bre60lYoNM9BJhDJSoOoaNt2EepzZYeb151ozvnVY/i0omEs/798KrO6W2DG6fZBvAsmT0LM/XtLO3x368jTXjjnDFF5o69d9jU9y8bKdwOQlMz0xRcK1W7n/Hqf5Ct1TKPkzRFs2btEslfTlP8ZHc9CzU36OZy2hFCb8SMGSPALPJIfiTRrf65XpgC5rqshyjBEibyHTJTEazIqV8vp0X+QN+5PirdDDotOIb13Ab7sqTv5mG9Fjk1rB7tkQVmv4NbAtXYUSxUUw2O2MVGJAIkFpkTcmsd/ipL5pWjjpUp5dCfUhG6zhk36zMVUEJfqJhoY6UKM78r7G5K+qlZ/Ok98ZUwIzD1T5AkDx/pTjEMKrUQLDIn2k1oIJ4EKodQ+68QzBCgORlqRwIgdHuk3syUQAPsl+imxJfNFeXazCcq1DzNHBhnukmIwbrxI76yNh4wtjAri6cUezWiZHgUAc/oSVXeIpPOU1DFQMzU58nrzosBJaRm2WRWj7Qq4sZe9wSW5Hni6TTPbLT8V+aCNNZma6n6Al22JfjeSDrtp6BEmDv1QibRchrrPjGmslUlyP7d+kPtLFMl+F4Xb4Fgqc3P7e0n7tmlgjraIxqASKy7BWwB2iRme1ak/R/SA/WyDPCLsbGZ1rJdA7iCREwQ9HLUV+5R1sMUBz11iFBiQVxQE9ihQtdlr9CG0r3Qg4I0sRByIFhqEA+pIedX1S7eG0zfAEqQkRWqYfAaEE7aNK1i0nDrj0am52z6RedZd/04mFHRGFf6BwbcSif4tk2qTNnQUECTjkcIE2ob5+xpfcYmx98bNgTpie3SU4zCCCsDNSqP4bWkx4h6MyeYpfqADPWU18sDqT6CwqWmmFbnoYpIkH05wzZ5NBEO3zDFJCSczJ8SYiTMwBjdYRsYWkoxfhLfGPXsQK+3TastH8PN9zky8BcV6O65p5mGRkO0XgmRNaFi0FbSMJppcN2BUSRSs6klUfLR6IzdffMIbZqjhmqdonjb2GpCjSrUYucvtoxf574NKXLXOzv+nNo78Krz4Nr2MDIWjPHF5vcsW3G4c7IMDguVRQxG9q6gnNwIF0a/R7kQ4XuJEuH9/4HmiH5RVKYn3QgF008ZMk+YMJ1HXoMqGfeauYLsKdrFdnaMYd78psGdPI0Oiy82jLbx5GLg1YL2voJ9yR81X3YN0Iay8b4OJ+65TwhSK9SkbBcvqbh9MZBsJ6E0aaMG9+chWKwtyREyB+3oDaBXDLI2rNv10c/lJnmRyxq44Gds/uljzV+6by5n+jyuBriEU/cS1EJRXOXN7t33ax0HAUqIhds5hJKtPdYMj/ivDuUxXveDhgF+XvvDzh17u4VnkmxFuJu//d992pP0e9OlSyVtC9YUVUY5DapQ571VvSi54tnYNvlm/wjkTI3NlY42U+fQ2ra68qTAnaKSId4eKYV9z1vXZo39nNh5oGfuMIomNxrzEy/4rtUHKLyIgs79rZ4em7J3bbUfoF1TGN8iPOoMP5qPJQnJfctVrA6cBAO4pkm/bdGFgtPhcM5on31jniMcpS9L2Yuz35digIEghX6RiylZ2QU0eftF8pzJu53Fr1JncLOjO4fRcQz0IGCokqAbKAjk2oygeq2kdoUD8jpqJVH3fHZnKh4ndrBAVFCvaiADCiuJ5ys8IeZH3ucFurUwjKkdRqgMyJEvOp8tstgHYo5bGdyEp0GP+CJbGX4V16XPxM5n6P5uzfsudO9+TZgrDE5AdUX7t6JDMnIlwJXgFCHpP8lHGaN6N7mHu6/X5oB+EO61HCsDujWX8Ld97q377iba/giwOTNWHnpKrXWQ0DXa9WEniLlorcxweesuIs64CcCW9HcUDKg5DN34N/cloBpRZ4iAXkET2bHt1rmWBD6moBHPsnMbkIo5tR1iQkyqzrn3Eg+83s1IuRNvkoHAFK+IPrIICmEgf9OElqnyZVun7y5QQIj52pi7E8V7L6UiMXu/UO55ozva1gYUkRbLMGqRQa0KbC5DEMHMGq13SvUXV9/absM6AockTMAsF5v8sEnlQ9kSbKm47EaIAPZwit+ZYWH/AWFiuka/zdkMhjjxIS+6SkrhN5AEJjTdPfK9A3Xy9sMgLUDJnxRjTCMkNvWKX0aPXgvAsjrFbGUuorsiFAhNhtIz4pEpzBo8EQXuMEGDAxHY7bNkPYanM6MqeOHaX6tOf1sGqKm86I+QW+RWkC+ntR9fU5hs/iHui3AXqvQubaTdGjJupAXDfgJ6e+73oCsK1+dMZNztBe+04MmwDLtca228WO6qA6MnAd1O079+EntxPqI+OFc0TVC9i6GxJFbUUBqV+T11MxALkukgLFTS/BxwViw5zH4vdCHfd1kfxBgy0ni9qoIp54dJds98Ivn59lbeLIfte6PjxSbatsuvS4HSZSJvue5Gkm3+7wmi+vMziSSlUjfqK1HBptqDGyKCxmEBfJDrQw3s0acrT4ZxnkCTsFjKq1Y+19cFMpv9u5hd1I1XiIjF/vpIqWoh8N/cWLX8v53I/1aXhmL+tdcDOMlrXbU+FFDT6CIVVfR8Z54EcbASKJJh42MseVwJX/tizwCy28We9YZD/jYFAnldBBBtJCCpindwqzTvIPzRc0yvJ57KPqTDFXqCaYtbAuw5mN4qTrZPRAhZmjPN+F1lSTVmSiQT6lChjsyBS8DNzeYBYFCWh+36N1sL4+vU5JpM6HNNMP029Zu7iPn4pa/I5fCpcgQICAadOWutW13i2SiakSUwqCDtnZK5htVI1gLaJklFg7G/h0Jq60N5aFU0/kZtD0d87m4/mYs/1R+U7jd+8VhxNcoI2N8kQNrPByYbgXaNbbPopT+7YuQ0H5Au93e4Nw1Hd3qhqo8Go6TfJkRlv9kWcRC6QZ93n1C2B2iynQ1POg97hNmlVQ6SAFxQtjP22KB4R1C12Q1DE3+mXGlxLxiJwm5f+9r2oZ3EsAg50kn0aY+9ndwmfOpmo2xx+B4MM5M5o7NewSP8XPtWXY7AQW0SeEWbZfjxXVEtwFE9W5LYYsNEoFErD9pEkObKtmYeitT8D/JDv3MA2Mx+mERr9kPfhtpLZo1MLPSN9iE/WZxQN17vjxmcsHBkbnrABbrYk49wO+hHRjpt6orj/oMnxw0B3ia+OBlOjfXpPYSWNq/vQcJ5um3xZ4uAztUqoq5NHX5KHd4zNbL/ZT/GdYEzWuJImxsIf+NJ+4ZcEGYuLwkjXLZHhtH60GXb0gUBPOmOwbTDj9JSyaRa++iFj5e380fPphfiDMuRcOEpBjMAVS1rNaFoz/igHEzN56QW2bIpzvN78d3Ne//V74hIQsY/f0WaavQC60txkWRfJiJZq1l+Z2l+bbpuHYKcZW9+xfH6I7cxrHwPrqD4pt3noLLR0lyJfMvpmjkzAAgKQltfcnvlOdNT57jgxhSvHtdat9Q5gxDR4g7AFAHj8DQNkL63sPG6a7qbS6X7abAG0AZLmDy2YuNz9x7l+IZD/OLwKVQhks/CxBsyx48W2eTPFy6OftLbHCXJDSW0QBw5Ac4y9of7u9WMypKHiC0nGUykJ+5c7NuHfoNKHKziFcdTRCbCeoQJcNU+maG0pEL8zohP3An6/SM8D8kjJ5iM2UF8tzd4TxbW/Mtndv9W0hCTOp4yGMRZz+qPggmtaM/MDfYZLbH7xgdjFmped8PX7WV+ndU8DzVgh3JtfRkQIlewHke6Me3a7zm1vWltOZmhaug7+fwni9+zWq6qDW1IjBCY49kEp9zIlx9rLRlVA/7paa8oUSdD93e8Leavdlgl5VXnhIR841H4hgpXXEzvJNX8Kq1oI6kUwCzhgIZXbMVqqHbXppFvaTwkO/APxQl7h6pBvxd19Ab7MVov9gBOV2xN9jEJ8HhoksUGdjGVQ0lkQsFNZHkJN5pCPm75KfdU4Zd8yrS2Ctrh5cN6dSFUu+JsgI7fXZ6+OIsu9kEVtPNUMmlzJgwowUsxjQFOkrkLP8PcjqUvNPLCJ4c57Tw9eSq2iLoXS4wwe315yh9GO4bat2yETEPUhFFY6pO2ER0MRgC2oF/Rwh5KOuPU9ZCb4n8bNfNrbYCC7eOsHk+IInQYd/AD+og4JVANBoKxghe3OZ9ObwPjUnrZzjJ4HWJxm2nxW4kOBRrX1f/4iKFMTKcYZ0qn6fB00WNc5YdDnTbqttw4e/dSFUHMuJQFOyy1MjVM0zrXStWO/E10WvZqcZZemA0LW0OXA48SjHYeixTcT44ndlPCz1ob8HbTxodc6iFIVGrshFeVxvkDLfjT/aQ3prz8O7pouIZoSxC3BIyRQO63aUoQFFHb/MaTL1XlAOa4BdcFUzpUrhm9IbrqiZXnt8v60PB+XsVY26a0hbWWep2eLYj6fF/i5F2lE/fvEUK2T+1gWGw9dK6YMDzaiiX9lWoIaJk7rJRpUVYPjh5rJHSnzSiPc/rCnjHIS1dkMVfLdOB9ZjThfb76mSh3XRaR0D95iopWr8yZ9xys6lFL9sll40CDCTE24n6ddTTDUJVkULwRTKc993fjCD1WcEBKs1MfMj9vBP+CbqtBzncYuhpDNcdH4uiS6o7Eozx8ojvtIMk2TN4YuycUkbKhU479I4tTgpApcrmyBTPRY65V2FQol0V6FvcP6M2pNOHgSIg/27HesJAcVZYjX8Vvcnh5JQC0nHBmDD6OxtKt4SeSgoiJgUh3yt3wTQ4TFjpTjJWS1g6BNUUGL9NBj6Bb/N0Wzlst2l6io7L7ldUSyNRE7hMbB6P8wZwISCpjDTKbsI8iZRVfba2aVMcYsPlolo4ABUMmnTjG5tQX+cbZPQLNdrHku+Sv3iLdak7yRGyC63wnVdJeqr+cGnJgrhxmR0I5qEua5UmX+PH1Y4FAtk0kHzbcA6St4l6SFpERM5WD/xVJxLvvl79GkPEghuPX1MOIm7s7ZO9MNkJfRyqrh8B+Tg3t+L6U61la3klu8e+DfOQ8MNggkj6L/pNbUClDekEuE4JxwA+8G7jv1I7HcUb6PTNClBaBq69tlggbZujXFCh/CNX2+a8S4WIx75xP7k1gUcq0nlnGKlqLwoXBUyCPWjokarRKNOVwZyzCZw/Dgll/y7MRyINHHkzImdoKDl2AOv6nvXlH+Dm37VUR7xp9EPLDnPHLyK0sW+ZzXIqTcxFdgOSr0KNh14ACnbA2LXt6DTLT42KGWmO9vgy7TEzpFrOB4D6aNcMWfC2rvukbU1i//+FMkTX53qqgUWp3Y8msP8HkNbvJgXUjJ1cJ+ojyQ1x3a16UbvGyyTphFJdxz0/uwx9kPTd99LeeHY/Zx9vZZkf5jBRrXZf2eRMDDFZsOAawEYbtkW71FaS0VbMXqCC/Zl2tR384u/4ytKrUjpN6vOm8mTJW6FJvly3GL39Tjjy/40Y/HtQ3hogPxomm/YPMEw8NpXsC6GN2Un5FVeYcqPQyFFeoJN/VzsG3VQeEJR6LwIoq5++3YE1vkQPF0Gki+/YHoWzr3vp83uhDmj+SqnFqUo1lsFwFXGr8aT6fm7PRtovoouNdE1dGk4iOi+fdiZkp3Gz662MHLiBW+TBYvaa2+prpM6+ExDF4QU9nEZ3z9pGi8DTjdXbrAXyWd6LGbxc2coggSlmZTmd/0vPEUjrz2DGH0S/GfTGbOSmtPbOhcpDC/7OUv87oYkpuit3Ps38gYnBh5Hm4iG6lTANZ5WffrZOAjrwjYrRnOJ+XxH2wQWCgDHjaRv0XWThtf4SZZNS7djvPEqYWmzhwtnArsonACdZg68CbYYRQ4DwpuqLx+HmpWLbujmCKuwXII4Rj9g76WTbaivlZKUlEXouqQ+5wl3AvwcdF/jzdIsvaW52v7tt2cqnJcRMf/5kS1YyEVXjqE3fSjOiA1OILfPZO9Bazzih2VzrBalzfYS47L0t/hP+bORENjQmYml+clZXPYKQfFetUIyoZwRAcujQCSi5dIx4t/LHh+Xzq6wYY0LLAcpxOldlvDHg7cvEwv4hHbjkzb3b9FuZE1LTVSIvVWTNszKD7EjXEi2QghBwirvTGorLcaZyj1F+e+O0Y7eQSKx7QsfuqraWtPpmZqe6UV+kqTPsw82JjM148xzGpmsI5jkLkCYEehlvOUlVGlTV9bEWEJmmUZhfoI4Q0l97oHtXquzkp8965PYWDjpDjz2p747+Hu01ebiqYzrDsCCuNC7MNuoNAaL5+32W1dRq/6Rije+F+/iB9spia6sGUUMo1Y4kMTu73FuW9rRLp2XhZOCe2lChZFQYIxwfkowaAeaNqppxxB9x7NZLtTT6bEB6dhkBZR9iL+svw8qCdGZJS1f5gSgyaUz5mwehPUBbgLkEikHms8fpBNKWcmzUpi0klknj7pqP4Zs1QQkV6q8/Qbcgtqa21vBUy1j+crTaF3i0h9EjTPJsQblJzB5w5P0HYOx1/TUQDne8zGpvZb0UB4/MPHzhHHVnIH+HDJxc/iHEez7ztbqa759RRz29ypJHeAqK7N0QX0g2XfT28EeaYCX4PRxrrje7bzA7C+K9E7AWEzyp92I9uXD0tx0U6dctfn7ssKbYDBWiStXWSp3jmPptk12hESbIjGT/9Ifj6nnxQeNQeiT6BaIg0c2Xh8zuS2qHyRoEXdMJHTVS5kMPfGFasPtRomCyb7rJUn44BeJxZqRNSBDYh5mBE6THchQDH7zSqfwISQlYpSyflcHtH12Nw1IE0+17gaxqj2mhTg3WtHAQIfhZcuBv1qCTBsrRxO7eGdbodmTLcAwCJfv7Qlb9METEhywJDgxhwPCUmDRT3WSHOY9km4T9zCx6GgMR/UOxFNbCbuRKSfjBq5HizOnw0S1EAyd/EKhYqgaQKAoNcbbtsdoyyRNU7DVmxJE3ovFLrdqlpwqIebLZUmldyWPJJsr/HhHg6Chb24MblFSZNExMD4Y821Fy+EUcNmFs2xZT6uoBDhixlcRscgkFzP4VfbuLL8R0XsmP978m0WL1DTZOv1I8XF+ZAUGfiMcHJvHjIOyZdzqXkSs+nxbSlGhjzTKibyvx85j1ewP1UjwAewoc3JQ7nrD688rJtB15m1tcKX3xcxRW3rBF0yWEtpjZEyMEz0MXrJGWQoXRdgNBSmCLDJ3c1/kCfJNvOgmoLj1Xyh7e+B3OhALEwRCLGB4DzmH+E+b9PqSwdluftXztn3nY3x+xIyWYy39KqWG8hHDs7cIkUAnOeUhs7I6svLZMAYMEYQ4mhG1HqkiTC4dPgR/nQfWGhEASs6Ovb9A+mUH8x4aWc1Cuhk2XYMQLPgvhs1NIXmHLMeNs0iP7eUlOpFSNr6e2ItTONikwGaKiKPbF4si3lXukN8eOsYhKXLnujpRl/x8eLKBqKRz+55YCvrd24zmf0U/fehmom2OxW67uVFDd/XrC7586eIAPtBOSNCnGxrftZ8vNOZ1aQydLmSE7fu9ZcoFiJjmvsIGukrCYuy4XOKUmQ1+jWsgs6rUZtXrJ9/8xbjTJI3ZslTgKpJ1sAUFi9Sv5M+o8wnTADRsxCXUjUtI88KdzLn0Hk4Y5NQWTe3/WCcJ8inDepDtNzRNfmADu9kvjWyXXmh1MJpViFBJDgQYqrjLzmwASesgST2n1T8t94WjoENH6UbZAVTYXcGY6rv33fjbg78nJHMNm7RVtSZDJXJSgRxEWHws41shP43+5Wzx3Qjxaq1eYi4L8gnLQt+M/hGOjAVfwdOX3e1NHlR9cwhcbeDa+zAqtERb6qcZml20Alz8DjaFjI4CftIzM+eBvnBBhKAF8Ym9DvCvnWcQ+E71cPpkQRbbzKSOfOj4RDnDHmBDt1/L76wNdIe+TQKbaUSRkKH9pnrx0qeJnQktvZLFdXlMRxO3ThQNQq0Do2Nhfm7iBUhUILFB119Qke/QalS0Bwi/677auywZHuiYLZ1DPjQi1pdMmM2toL2kWIsgSPB1TK2ElnJE62qM0EeUnCaO4nHHJn2+fIOEs08h0Yejl4pqfKifJdFooEgRpz5X1CRd8UALrI5z2DT4uKH+5azt1/u2W0kQTE4We1Y/TioFrAPktAc3mhAzxapCMOnrGkCpduVc6OiU/ORbXunq4hPARJb/MoXy49VBqylIjxU2wxNWtynmxd2TGZh5X0ouNzP8NdmM4vgMk8ykiwN5Ulpqj5mLwETxQS8PAk3kyalvUU2Rv2Fz0Q6MBKAVQx5/D7dyWIqIsTOkfqddD7nZlImIusb+RInT/Y5T+KGErOvDLu+sSnLcKxqvO3wVWEDazDTF4rhWohkKF/LHrDV9EcQpx8nS41f8yKcjUlA6v0HbybQ1pIa+G244MWAnCXuZlNzLjWmEn8HIZ+lMBvY39gZzz+rMfeoockZuae4zDaHzOby8d1Z4N1VGGUlVpXrv50j6wM+fTss52vHQvLbzqLrSW6VcLG9HMPZRbUufsV5kzj7k0X+Cz69khnhrawbSZQ3l8aSiMr1uvO5hnUPAyuF72fnWJLelzoYc25+HQklAlNKRPg8bn4O1qZg5ereTu+Hvma3aB/j/7I4vtv/sGaCqoq0Yx+JIFDi4X0jGBk6/6iGZX5Et3fh7hz4zdrv7VKdH6kT7lcDSpvdfI3lUy0slvi22qvG4juNySatG+xrSxGMqDa1LDthDs/VuQZgOI96N7WFn5ZUdWHPH11fZPGvnU1o3Me+Q5qn6O9r33y9Fq4UHipjPlvBYcLGKC5Ng5YyxDmyTpgKrQlPCyoPbCIubLjKJwxc/9KBWjwitYepCBSyjf7xsIOdsmlnErDQq28VewAkSzBBQf48X14Pnl1EUgTvPMvFU/pQ9T1M6hZybZcHJW1o47JnXIL8vjX6cu0dFDGdHt/y8itwnleFkUuE2yEoy/AlYVzn3RDVq+zSXMLHh/YCM888XbPTB5XCpRiPf0PuqO4KIs3V2eE8NWIoxsCBD17yBcPnHc4jWiEviQ1gjbG0FQdl3GBVQFKFXSgUQs0FZuFhndFNqtd4Ssi72oeXPwijpPQyqGiVdyhRyVP6wMZ5C5ApYUX7CJ43Hig1tKfrVEQNrUZvFgL4qkGPZyogdIiSIekmuldNukQPanjnSYaQZeY3dXfvp+MBMVmJQS/qcm6+F+qHM3+1bdebfp/YIoBe1IqP19FIwU0ai5Lywpsxk4LtDIc+7kJCr6K0zV3K9iA4FkGX5CAPIS6nARMXWUi7PjFWhn8aN7v2r/n1SOH3piF/3DvRwE9AGEUywOl73X13vkkXxab5fXHZ8mirShdcL+3ljrluzWbUFRWWJUHtNJDWgKLSAIwKhuc/cYir7eTeEqE+qwAR+PnOXrlzTgMriIPueUCLK6k98f3I4Bwss4H/p+XJwe51Ci9o0V9XX8ihoUI4b7nrkuK3UzvUhej/JtiDYxnPwD7E20/SVhaIyTM2rCkI1dnqE3jgCEus0dncFOvp8OribXbIl4d1dbupZzxObFNiHrYeZ3YuQ/ZG/MxDru+wEXnR/d+mh4isawU/B1oDwUglpYybH0B3f60Y6PXvoivpscNeSAr6Q3EVcP+aSo7swBII5ztPcB10nLbcfLzuH/VzMAM8VByoCoAoOij+ZCiX1+/qMzoMqpASqucs/vzR2+DirCcJ6Ev7qWosqw7v63Tzyd/8XsbqYw8skGn4Azhl8txNLTgs0J7m3Sb5Kv6OCmmMZzhU0l47V55JzXv+gos3QrCNIdo50cW4N3BrKucw1TDHoU2A8eYT0O1n4uYCbXaFxaEPj2YtaPTXQqPqevE5Q/LoxA3RKrFfQSXh8DmavSKAGHbta2jwIf+hifk1lhB7UFJkYmKzROxTzSFGRt1bSGcSP1R8lGZbe02lyV81rW5nlgePlOnY2CNzMCKJnF262i2piOkTgg4jt4kFApF4yidAe2hVmxLe5+wEtWev2PtKirvqYuOClynouMIOaDXp7k9/1Z3j1fiPZw7uM1mc+SapzmjhkA+z60I6IwaDNooTEsC+S/wIAAiSbu0sGCKUz2o2vreUpWh/6z85hVx9lMYj9k8AyNJaS918mrb/61lmKrc9JAsJ03xRub//6ItIXeysHu11Q4/FWQ5n5Hy7ajZGkjdTKN0fcQSaHK8WIcQF6CS8V3Lh4DN3/bBHQxHZMiy7Zf/DcQFyvczxlzyQdr5BRX4cbYOsueyfQYdxJHrH0g51eqM4vtSyf5VvwiWg2UBF71qwk6wTy7/xqud1KmncwPx6AgRXue3/pN6f3JXfFt1Usr21aYisqIMgwYmLVt+ZXRrLTraVoYlzRbQEUKJLUNnhn3adkTQSuEiS5rnl4Bi1gIgHYhauC0TSSUPwH8kJUbNohX0Ky5Q4W2l4bBpRyWhhutwTNaigrKxnh1Cm7VxpsrrtRFTUN0dSEpqv0pKwQPbafYnEdYXkVUX0sJKTJn9ovCFHwkIUi2HvUzg1T0QBlKW/iVuV/bHhWilZJ2mGCai0MH6j5WMxt+WZZOWvSKYf26HT3TXJctYOjbQxtviOY8SFgV5yLjx14lAwl7pIWNAj2lpPZ03rbT+Yo61pPgfkSNwp5I//edYK5ubczhH4qVLe9KzUNbqKs4ZTMHnJ9HG0eVVk3AD15UFfJcvVbRcOe4K68H7q10Zv0OianheHnVGsmJCczsy9Nbn5CX0pDZ97Z1sLRCgWD6dEHxno3m/3RYkg+q6/0fMo6s4dUNjDs3Mfmpft6ZEuFQYYNwlzSaHTt4wSdv7KA7Uxc9LnBz2+x3UlsIrNDf1jYSqbS5ZNvwCdWHdSTfMa2P2uysbdB0LGB1qwq/ToI279LLcqrSf29v4Xu89eWhbjsBM6KX6pum72Y2f3Im5+qOmroj9/WEuDY+RqwxK+O5RiA6uuqAyvLwB0XsZU+g2V6pFrxj9NFAdK/PaIYrsF/5ilcMkal/NU2m6wjAAj0tWF6eXwLpTj4RYWlO0LEX8ynTByU/3J+FTF6A7CHHqwFH8/sAL9UMb7N4/C6Egv1wRM1AS5kIz/E+sjLbAN2+nx9DoA/NPmMXgtDxTya4DKNDwWuKIr8Rm0u7hVpIa4NoykinD3f02odmJ+fuKHjqQXT6xSWQtywfdiv93aHmRKKuVEHte/zmOvP6bqf+dZfd5Z123nlZV9WkagAbTH5D2oPMkJwkrwPPdKsQV7XkcHq71krbP4CFhhZFnEh5tRMydrScknFo/etpv7sK+m8hQaH+GtCsEt93bpFT5R0YQ4d4XgMJDwNXoe89kjg1yg6Hc3oVRnoXYw4EteV3mgcQvP5+POC0O0z/JwUcwnW7hG5ZnW85gQA8i36M+dykpkgCXRS7vJIcEymVD8zZYvNMLKx/BIw5Y0Lii0dEAYSPZwFlpwfgD0R/ShxPqqbHtcWms1vG5nkL+BcBjO2Yc4H7HFdDLGwzi7CXVrtYKs/EfWjTsgcY8JkW+aSFCeyzKZnszU4exXm2YXGji8/PV2Pl6Is3LBiEl7oZJqIfvxYl4fNHue6tgWU4p22/nhZmN6Nk138CxAiobIEoJq5qCk51uxbdYINQ3ypCxsIae4mxMA3r+/qDm4/lkh9myeYf0YxJHZx9Y/I9iL5MGrlmKtqZnEdI3LBp1esnH3dFPLhYRDh7WW/x48QjZshJIYp5prfqCN08Yd7FRYRMedTQg/mF5fm/gKacrDD8IZa0+7c1yQfQkhEDLE8gsZt1joqywDpu+xt4SIVTfR9NpJ2ll8LUH36vnwx6Z6SU+/SN6hpI0aVQN2KY0NySke0GdsHVO/PYWqpVp6f2lMKw/5i1ngwSyHFCIltlIdNcndX7GRDugnzsHNe/I8hXFqFyJ46+SCMlts4eH4Y7PlMlxVV6vQ0n2eRCiinXvXXzenmDhujXzTX6voy2T7OUaMNeNmy0k9BVBnUYNtpP0U4VBeEz59cip9x2Kk6i7V3M7NyPnESUiGf9geA1tPC3qFPQ4CfpB/L3SmkpUocvJS++Lmw3cLjBa1vDq00CmCA0GvwRSYlXd3rVhPX3XFQq7fQZ37J+nJX9luMly4eQiPNW9nsXbRw3gcm+TP4QKxU0jf8RRZhd35EnhI6J5i0ws8q43Nm0syxLB668vHlEEyFurKP028/ZeSf4fEkLPRKijAlBd40ZyPO7SxF70JZfo9V560Ib1uLwVivDt8ssdx3Tly9FkpB4xsl1FyXN/rbft4Rxdcb/TF9UNQO2r1xQhZzNT3n4kF3sSGbgNp4PnAmCu9uFXVw//DA5RzcNKQrF6on2P+2wJT7NiP3Xcd/+HOwKmwvZAVWyrKFvop3jqW/G4uI4N8mLz1nzMLkdtNrV1scDJzZ/BToxVR6fUNZmgijyZV+HrgYSaJHHzQ+4LlafcQP5D5Jis2ASH6cMhWxzvm1JPvgdyrzBt+sJMdAaupzh7WzwDGoMMX2dGLk0SMAwe3IzdjsDZCp6Jh0C3v8DEpevTWNZeedVOdW5x0Q2DtjCmHqJU1o5lp9zdVT30wbHbeB88yhimQu0B655i9f+k1zN+Mhg+m39D1H4h8cKD86GYNSTSxDocHyY8sW9l22X8RIIaz4BrBgrOzWezN8kY0pwzNBMR22ybiX2xr3f0jc/LZm//vAqL7A76WrDt1QfuFzsQX991UzCDGxap22vFHDDcUixSaOLUetzh44KuxScPjBAEMnN3YNhr50aq3+jqEROi/HracmuXAXulEp8AbSrVsI7UL/yS738xInf1FgHjx4cWDSO3h14zOxGqnueaiFC7pcNsZDu4nojBJVOAq8hvtxt2JUYUPRg3zG67DEsn50rm2ro++TYgCY+BMh/qISgg4j6F2sZ7IILcDClaL6/D6kthUTNbiPXq63SgzzRIHCU68si7cjvEp+8nONPo7PuoDxFRY0sbmPffHedJIcGYlu71vPiXO8/7taQJdIreVVzf1MprzZUi7JXksGfpipokhjNkQOtDWP2+bTXbDmbG3NfD2d2g0MDhi4NI1fAQdzSR5V4LsJPaBhDbf9e39Kh+65ogPJ/vKzFnxy5JmKXKhuKU4/WzEiDexQjsP2D0x6YSfRnyGrU1EQnfrh23h1qxu4ROZt2Xti8MGv+Wuzqe61ce4TOoaBH/3oGy1L9vjhgEvzrpe1fJ4EDSbkc/r8ip6pps/Ma1s9tpX2StN6cVPShbk5YAwF119t0yrnBuxpo8xLPcZvzzUJeS+F5ju/RXEP5nH7ufEXsYAW3Oh+eTbxQFCG39CryCkV4Rgv6eBQNGSRrG0aN8Xi5zevzqZI7G7JpePF6EXVJZB/Zn5ZgElAkhP8CJZ4ROIY6ADRw2w4nnvLeOrSZb7ZNPvXTt9wnOo4RElTPi/AFv2htjd6dSFfuy6A/mwP0siVW94beXG5Rq5Ok2kfMUaK9qKBgROnPWF9m4q/psdiFyhbuLdh2rEWYp39Ns1XNTTCjjfQ9L5b9W4TKLGjl7gIkVgk874rtq9i9YqW8r+PYEenT3Nj8xEXlAfRUlNo4/Ny3NF2jr4av1/PsePjnUPvDfL7x30QLxC34R5LWI6GF3Q2iBDrK96g05/zu05HIRWis6jUacvM65pW+yLNsNH47GfjTX7fj7qJy8zISH2X4KfeNrxZldFQP5bkcucv06APv7GFA79Xn5oMlcgB6OjoaGVlpfscg0aJlEtq5s/+Up5SE4ehK2WzVMnaOz9MUJGhU+8+cvxV+almzKV1ZqmidLWIucuIO0ns96k+iLzvjMAIPXmFuImH173CxDQ9M5aTnbpCfoCQ7nST4NGXv5qlICv1yeuHnmX/mr11Diu3TmoHoZfJ+OHnujZvsQSJAYiEwn/OjLHCi8vDwkMRWaolE2RDwEYbasiWAMgMp9xr6MKnQCfpJBdQd5dRFORMH40mD7h40pzfs5eK72TCIxM9jPO8i62FrKn2cetP4fT7fpfVYtmkqAMnK9HnCwpOAWvdCtd69NC27kG/XP+hjeNaP/+HJjHLYac6j0GLG1q8YnAPkTu7akLmFuY3qYXzeEDPDUrCJkflEbaRYnbLc90TlSTErX60Ti7jc7tHUlm2OEHFh/wFr1HXM5QvJNQY7PlLKdnxB2EhzunHXH4CUQwBgNDSuMYZupTqfzhKvb3ra/+2lVi1D9IUFowhzaXapD5y5xoopr/JPfIyKxvBMmPksv3d95iah2Y7Wp0kXWPrshZz2i/XR1u0k8u6EHlOl8FDhGqV8Gqy+jC9t1AhOY3AdmeK+lFdvdKfxo83dxJ0sh5a+MUiHGKVPXL3tD4qPtaYA3APWoWYGvEHoUaASW/gFdzv78ivmOugsp9TgCRxWpy35/PhTFrqCjILR6fcRNBKSkw0aiB67GLZveDCoMMu0bl9TJxAZxVSHFwYv2+iefSSNXAkfteHX8OCbDGcb2pa3nTp8oriC+4/jrfIG2lOwEoUbBmZ4ysCJqYzzA5p9qpmwbuQq3ZK1yNh50vgYnxe3z4vjb/PtK+EIahjkjvph8zU9QqUu/tNDm9Da6j3wK34+RKRFx3P/LqTwK8jvO9YPDQ86AJCiIl6nh1HYyAzfSwyYjfL6LpindbE8PDxIALFV05kq0S/c769WvmS4WywwUS36YRMmNz7rXHb3uyA0uMMe1Gms7NdieXetS4Ai3lj9LzJGFAl++kiusZxmQXruDI/afgVMMiLPFsI6qvN7/xtByAND4o1Yh837cWJYKpLId26VzEFMrZWLAbd0kJXXKfxaoCzGuyQRXj7vsz+aVIzwrsU5+q0qRqsmTUoEILjChbX6c2HPZmjAJ13/vbstnglvBe6OzdnDhxdhoCpVi6+GXHqeHBCMGwOpd8q0+uBTGMvRHeuwUmg9Lf4WBqS6dUB/+ZNd39QqSgwNvPbTO7iKmD51k29weF/Pf59kVgA1Z7kUXdPIMljED0fs+9WV+SofX3n77Oi9LGGH8CkuE/OEKBb5VT6lSXuEs5P01XppJCz1lA4VlEWFy7YnI7FNRCToTTgIwvqlriY4eXOV4RHbaAuxO3V/PPW+GvlixdE9d9XgKCraMNvQuM4hqiGDUP057nkuiYB6Gt/EESrvPPdn+q8DTRYA7uROTHdqv7zmgbbOvYaX9oCpcTAHd3qMY48IvM6eCfI/jASf6XbYIzvXo0boj0wooZQ4szP2lbhOqSPSJDzIo836Bfr6h3B2I/BO04bIRcTCTyuV3+ve6IoU3jit9E1bTRyUIDuFwXUp0OQsJFesbNRxdX+HpXM5cSvdT45cEtjSl1hVQzEr7n6VNp0m6C+uErawFAg5ujOxTff0fmrwNvyQZYDTjU4lPrf8UvhcfRTgfkBGsJ8IwxzSV3ISaCoOjaxdu2LkxCIsta0zsrb/Y8azSH+C/hffvGznf+EFA5VwJHviP/7zkDe0i9+iTwojNtMI+sZJ+j7KlRbMttXvR/q4h6vmuas3cEd5cSXpL1MTPtCgYWmNNQG/rr3KyMW728OLh7V16yWhf061Ace+qnY/VKIGAyZBZvy8ghz+flzI9RuSVmHMX3LyQl24iDylazTesmHpK8WTCyRW7GsNGmkpXnyekPrd5RF99bftCg3eZq5dm85DmoLIqlGDGWkbAuSTMgNus1s0SalhRyoev8yJcBQdYrbBU5xkc9/jlgHeSeQYyH05yaziVpP+d+THuAxyDnbP2roGov3VM3AyOy2JBI5FOy9U21Dxz8a7kJWq87tOGxhTNjfpPilmvOsAYlYCpyBCmwZTkjr1vf7zPmLV+gd3o654QtiB/YB1GVZu0t2lNDAjW1ysZ71/bt/OSjCb1f6ooXhLQ3cIGlsmgOSEPKvsfPYuRZJ0vC9/FuqCu9K6gUHd3AHbw6jUQvvvUfqe2++6inNLGeJICIDiMh4H4lMeuDBZDFv9iJhU2b6JrMjDzhqU3JoGHvGrFfRba/9YOWrvWC6GnwhKX/26xdPOuj4XMsAZnljM0EneWsEC0dfQDi30kgYJ/8A4jpBxkCxHEQbFOtlT82gX15wZPFIY6zbl8kfP/gHEw9Ogfzp7tg1U+O0/gzOmW8WPoPbiLJTgeemR9gBrTkUhbIn+P50TlqAyefLnN6dtmt3IaLP1jKGJPA8Oo7m159Nqei6M05Z4fs54eh9YkjVE1xDw5QSrh9AScd9tTcvfZl7/M5CkOxN5EDEVfeAzsE6z3Zv1HA233wNLwVbWta6zZz4+iTNdZVG4mBVg6OF9tcIEC4Q96prEt5NOJfXgpEQ0iAEApKkdu8ytV9zvqK9xKAKZIMR8XoKfeBT8f6c4wTaCeZacmQqVXb4osxvidgTxIS/Ad8bjMRnlSgCXFQLZ4dSlUfz1SqecqS7fU5gsZxpfyVtEFY+ilU69NEzAFD88bV04Hq9UW6c6W7eRI42itCmkveWzfFxCGQ7qF9duCjR4/Ri9pgeiFUvapMEJV+xnHwb3Bj2nKGlowXafYN3lqOEqlYbbYvp7879tboTnGePvgdUVv0BUvuwYnum9FUB/4jegFq51PMzMhWsKwuzLpJQFxjJ0o8hbdivpBixa7IN0UUHhbCLIf/i4m5XV9fKrXET7/N4WVQy1YZv0cZrA9wMpq2LfFAo7+v8prIlvZAwKlFMhvQW6mwBrIU8G7ov/24unxjWa8OLF+GDihqhan4dnXLZUmbhINux8OvqGgxngRzWa6QUTuTEzDJHehgC3YqIFKdrtmXxqaVMUFcU7ebjfe3VMfISiW/345XCaKc6CEW5GrUL4Pu1lTlDduZEZva0WzpAGNQXpRjl0u2mIbh2sVdebwINyfS9xRqgKyvJyC5t0lCmxs0JEMwnI8QjxY2fcef3R5qMXQzk+uAjlOSdFUR8Le48Zmt9t0IXDJlv2M7oehdmnQFs0CvFkoSBNNQzz4dqSYxcu7d1+gjjwrqObRxBZhwHxG/9olnysJwm0ELKd3dDhmxs1WC/hCTVj4d6/WGBhQMvFnEcBYWAmFJPv4xkAfPLl2zBZO1IOoFB7+63DqGd1HKL98H6sWzQGrN967L59POu+WZhHBfN2DIwALGgNDtsgjc1fTJe64IQuOdB5ZLFlIT3mZShowD8pQKqWOqA+k2CxvqUqWaNifKB8bElhw60CL93BWfeC+KbfGAIaaYFtXfE14mp+VnzuJmo/qZFNYYqWT3heYjUR4HOw56obcvJplqXcdQkyjeVpjhSKxV3JsvVJr91Kr4tgun9szDasGZlkPFY7rblK02lk1xDW3Up+GmuOtIHEIsGtTtoG9EKbLLATKJcbYX5fvgIca61uwH2B8XrfHczajAUtX9aYzteMXEIKwDKxw4yICznNoEFCDtYJPazv/sq7TR+zEjkXk0fuFqEu/WL/VQ4X4OUTkrkpCbhhzeGR06kYfvgUghDJtd86IOk5PXOhM8+IAqHyonBFw+77QUTZRAnTz0UFhuJPRkWzGU7tFP8iVRD2RBundHQ7xaqyA5keXNQry3VfNorC7WKLhj8TLkp5bji6/Q/j4YV9NERgcwsNLz6ROR9XQBt3i8Z4TXpmgpxT9/SQC8LkPmLv8SKwuL+8rYGCY82RvC+Gy6iEXQa+VO9lsPyhjtb1A5xwOe7y7YLQq9dbyM1vXnW63SdM1lzrg63pWuFdykhzA+40+lIl7s1M7wNkR/c9Mi4nv0qAFvO96uvU+uLAeyfK0HXeUIKk5Nr1R1Kf+Xud5LLKR8ceY23RZWAFbatZ7FQAmYqe3M08yVXyABju64u4fquypfoCjzeqH7LCgwLj+PrhJo8NSubdgXdyS2vhInLkF8M/Wq2aA+2CaJ9S+4QTxFfIIROVtbjhpE//NeT+jtGHJM1XHUqp1390tseFDNRaRhip7KuD7tbmaSJuFaIoad+kVj7dnOT5CMWSOnLZigO7JSgwx6DXIzMZuA4DjEOmPpqlsGIqprj33W6SiqgZTgmS8Tb+1WhH12ssA01pDQnCd74yC6VLRSfH++IXtyaZGZ4TtZ3l+adYElvUXVqnI6qne2LqWqJ9xZZYUpms8RqoRm6bYAPKZuKLryoRAChS4t/gmvztf3yEyOnkf0a1c0MEVkrDld5WIqYJ7d2ZA6LWnun5Gul5RHn+PsFmJ7+dK23UrNLzb3ja9WCC2Yp8IpElMTtFi6OQOPhGShozyAIIT70dRg/KhkyFssL+5jsb0pvbM5Px1v07FJEbJX3C4jhw+6dfvdL5RtDC4Y8zIlA7vgMXjU3s/ftcHTuvSfH6n9QudZxBRXioV3fXHraEvSANnV28o3W0qNoIWMZSJM8D07tsBeCzXBJtXk0Ld+vO1JVgD0ZoLR1ec5DOr47fiSZZtNltvd9Tz18pzBWUOX55iDo6LuRxVJ/elWjqW6j6agM5AYL9NG1Q9aLbh0vW+ImKH17lLwNtFWaI8jAYWjfy9JE5zhcVx2LyQY9aKs22vDcb5diOJ4ACKWNQw8bAPPTvuIRkGeScLToVYE5IVBO3+XlG2sGsGQ6WogXCL6fgOPsuOblBUrHQwaoNN1AMnLmQOdk8DJjFNRCFZZA4RTqYgj1cdslpwvAkTI5ZFntBIpS9EBioLvk+gWAYdtoJPhODFpCMXhE4GlLFZC7hRzn6WkVtKMjfz5LSC85msMhsVrusG+Ru3xd2j2zNnAT9ukKAZMZtb+AzFkAQWqdehM5ERdnGXV48/Uj34OUQLUH3FyTABjc541gbWFIzoh/Hx3sOnH4xbHqLGBI9B3cWLW9Te08of1NnMOfvyI8U1vK6MDL5bxr101AExij76veMOcdMPprSHuDA9fAX9jrG+0aY1/MsihUL24bbjvcVBfuQnpNKpv35kViAfl8+ySkrQCXuuPSIRq8QexSlEn76sGenpmYXpCqnV0LST66jtkV+u5elklL1ftnw11LmBMErn0c9wmHEEtK2GfO+Mp0v59UseQbsDm5Nlt9tX1xp09zqz/Br5B/Wid9pj47hfYbAzcukCIq+W7nS2fuUGCDLz1KbZ8pKzrsI8xtnw86T+EA12DeUJWiJwQlQ9q8ZNFObRzwBuc8xuFT3L8fwTtLEooFoiKr5cCmJJ3ueC45258CAC9p46tn6sxwz/02+IRW19jc7Ss3P6mw4XTqZqbMz/PmkTJLBXzDBdsb2sPwiFn9I3NxTHR109HO96E9u71faV7d3jrABbc7FrMi3g1fg8cupnFvsncrVOElD9NJlSF9C50ao5R29srxyFmNEwsVdg53sDkWuo5Y3sY8q70gsCaxEnO0DVn6gHMbKbLnOYgnQyLJWteqV7NdTHn6XT2TfuU2tdc/v8ybJkbMW5YjJnY5CipqhcU76nD2lpdrPeI1My5O8LtXbK+Dl52LEqdvdBxhPoUIFYn9904uiazvBG++vkDXKaS3D3TEeI7MOovMsRxblZbqzUkZeEc1e2kLhriJTpz6OZyPnpCc+FG7qqgq7RE6t4Jky1KMvGjCD9TpIl51l+tfdWbp0GntqxxYg6DX0uZfCVTCwhZyFZg1cPVhhodqNLeJBGdHdHNITza23pAvtp1JZGkUz42iTFakTI3uFNmyeTMPi76YEbVU8oOl5/BFv02VUF+KAhRXdZwMYCI6VeBRPnmid30RB5kprybxbRsucFH6+fTJSeG0Ncp62CVVXXl6cxW1czk/fWJmXqGFkE+VwTIJOgdpFAN+I5W0QLhIRCaUopW4YOgrR5oMvjyhulWHdKH0fQgFDBYkM1Yq+Y6/L7NhLiydqHGZZ8kmmm95nW5n7rDk8XHMSnjThodswIEWQgC9ejHQA+aTqqdWX/C79hr89oXAOtdpVZZsVXx8bWUpK1Kn6YUP7w3I0KL+7WxLAgOQJSym/b1wvn9li4iR/piZZ9+4VRlWpr+vmSuGq3wi/lb1t5VIy+0rWpHuZiCujzjkJA1+lXMSeXhAJ/x4tS6TzUwX0lRiPG1nh9eJyCWPCUMGOOvPZxwduLSYi+bsMmsQYG+UAdl6vZ/YJm5fyJPnwtFZtCaCg+GlkiOD/k4GqvG8Mn9zYZnegGYFk1VnU+qBoC0dV7UH+P5G1IdHCel65G94k5ny1HxVuopIcrZzTyX15RAfl6WW9tM0cPdIGRzgZJJDW416ImapRglOB4oTSiCOdvkz/m77RQdKC15MmZPHoLIfdi80YXjAzvPyaD9WLASwOHRw4a1q5RKAx1vsHcLRQdqv+SiqOCfkPm6fjbSmWS8e6APRTPNXllrn7mpHteNRNdMv5+khp/Ap0jMUF/2t9/GbrYxsHasD5uQ4x88tJSpGONOhdQHXl+CBlogFoSJo03dbsu4LvCn0nqSyW6kXw/zjH79++5VXbdZHXfbrz19LGc3ZOFT9+s9k6Nc5StZ/Rn3UXku1/DMqsn79Y7wek+c6BCcegzjL0ySDKCTPKYzII5zMaJTIExiF4hTOMATFcDjNqDSiYTjCIYLEYjrCEjpBCDhFkV//+tdvv8aHUJ4I+uQJ4b9+zVmU/vnXWH/+/8L5799+zUn1BAP/Af3E1m7FczBH8+9ptSRzlj2G45jNy+//6+/3v/39/re/H8trWbPur6Gyc/31Z7+17W+/1qhYfuJ6rLJijtZq6Jf/PIL/8fUc/O3t58T/cdhmRdT+xLc/oz92/4nxj+eu/w11AJwT0+UAAA== -->
