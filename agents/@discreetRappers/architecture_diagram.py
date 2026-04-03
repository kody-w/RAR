"""
Architecture Diagram Agent
Purpose: Generate professional architecture diagrams for system documentation

Supported diagram types:
- Cloud architecture (Azure, AWS, GCP, On-premise)
- Multi-tier/N-tier architecture
- Microservices architecture
- Data flow diagrams
- Agent/AI system architecture
- Network topology

Output formats:
- PNG (default)
- SVG (for web/scalable)
- PDF (for documents)
- Mermaid (text-based, for markdown)
- Draw.io XML (for Visio compatibility)

Dependencies:
- diagrams: Python library for cloud architecture diagrams
- graphviz: Graph visualization (required by diagrams)

Usage:
1. Simple: action="create_diagram", diagram_type="azure", title="My Architecture"
2. Custom: action="create_diagram", nodes=[...], connections=[...], clusters=[...]
3. From agent config: action="diagram_from_agents", agents=[...]
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/architecture_diagram",
    "version": "1.0.0",
    "display_name": "ArchitectureDiagramAgent",
    "description": "Generates professional architecture diagrams from system configurations using Mermaid, SVG, and ASCII.",
    "author": "Bill Whalen",
    "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"],
    "category": "productivity",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import tempfile
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent

# Check for diagrams library and set up Graphviz path
DIAGRAMS_AVAILABLE = False
DIAGRAMS_IMPORT_ERROR = ""

# Ensure Graphviz is on PATH for Windows
import platform
if platform.system() == "Windows":
    graphviz_paths = [
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin",
    ]
    for gv_path in graphviz_paths:
        if os.path.exists(gv_path) and gv_path not in os.environ.get("PATH", ""):
            os.environ["PATH"] = gv_path + os.pathsep + os.environ.get("PATH", "")
            break

try:
    from diagrams import Diagram, Cluster, Edge
    from diagrams.azure.compute import FunctionApps, VM, ContainerInstances, KubernetesServices
    from diagrams.azure.database import CosmosDb, SQLDatabases, CacheForRedis, DatabaseForPostgresqlServers
    from diagrams.azure.integration import LogicApps, ServiceBus, APIManagement
    from diagrams.azure.ml import CognitiveServices, MachineLearningServiceWorkspaces, BotServices
    from diagrams.azure.network import LoadBalancers, VirtualNetworks, ApplicationGateway, CDNProfiles, Firewall
    from diagrams.azure.security import KeyVaults, ApplicationSecurityGroups
    from diagrams.azure.storage import StorageAccounts, BlobStorage, DataLakeStorage
    from diagrams.azure.web import AppServices, AppServicePlans
    from diagrams.azure.analytics import AnalysisServices, DataFactories, Databricks
    from diagrams.onprem.client import Users, Client
    from diagrams.onprem.compute import Server
    from diagrams.onprem.network import Internet
    from diagrams.programming.language import Python
    from diagrams.generic.compute import Rack
    from diagrams.generic.database import SQL
    from diagrams.generic.storage import Storage
    from diagrams.saas.chat import Slack, Teams
    DIAGRAMS_AVAILABLE = True
except ImportError as e:
    DIAGRAMS_IMPORT_ERROR = str(e)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ArchitectureDiagramAgent(BasicAgent):
    """
    Agent for generating professional architecture diagrams.
    Supports Azure, AWS, GCP, and custom architectures.
    """

    # Node type mappings for Azure
    AZURE_NODES = {
        "function": "FunctionApps",
        "function_app": "FunctionApps",
        "functions": "FunctionApps",
        "vm": "VM",
        "container": "ContainerInstances",
        "aks": "KubernetesServices",
        "kubernetes": "KubernetesServices",
        "app_service": "AppServices",
        "web_app": "AppServices",
        "cosmos": "CosmosDb",
        "cosmosdb": "CosmosDb",
        "sql": "SQLDatabases",
        "postgres": "DatabaseForPostgresqlServers",
        "redis": "CacheForRedis",
        "blob": "BlobStorage",
        "storage": "StorageAccounts",
        "datalake": "DataLakeStorage",
        "logic_app": "LogicApps",
        "service_bus": "ServiceBus",
        "apim": "APIManagement",
        "api_management": "APIManagement",
        "cognitive": "CognitiveServices",
        "openai": "CognitiveServices",
        "ai": "CognitiveServices",
        "bot": "BotServices",
        "ml": "MachineLearningServiceWorkspaces",
        "databricks": "Databricks",
        "data_factory": "DataFactories",
        "load_balancer": "LoadBalancers",
        "vnet": "VirtualNetworks",
        "app_gateway": "ApplicationGateway",
        "cdn": "CDNProfiles",
        "firewall": "Firewall",
        "key_vault": "KeyVaults",
        "security": "ApplicationSecurityGroups",
    }

    # Generic node types
    GENERIC_NODES = {
        "user": "Users",
        "users": "Users",
        "client": "Client",
        "internet": "Internet",
        "teams": "Teams",
        "slack": "Slack",
        "server": "Server",
        "database": "SQL",
        "storage": "Storage",
        "compute": "Rack",
        "python": "Python",
        "agent": "Rack",
    }

    # Diagram styles - Professional Visio-quality settings
    STYLES = {
        "default": {
            "graph_attr": {
                "fontsize": "16",
                "fontname": "Segoe UI",
                "bgcolor": "white",
                "pad": "1.0",
                "splines": "spline",
                "nodesep": "1.2",
                "ranksep": "1.5",
                "dpi": "300",
                "overlap": "false",
            },
            "node_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "11",
                "fontname": "Segoe UI",
                "color": "#666666",
                "penwidth": "1.5",
            }
        },
        "professional": {
            "graph_attr": {
                "fontsize": "18",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "white",
                "pad": "1.5",
                "splines": "spline",
                "nodesep": "1.5",
                "ranksep": "2.0",
                "dpi": "300",
                "overlap": "false",
                "sep": "+25,25",
            },
            "node_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.0",
            }
        },
        "microsoft": {
            "graph_attr": {
                "fontsize": "18",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "#FAFAFA",
                "pad": "1.5",
                "splines": "spline",
                "nodesep": "1.8",
                "ranksep": "2.5",
                "dpi": "300",
                "overlap": "false",
                "sep": "+30,30",
                "esep": "+15,15",
            },
            "node_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.0",
                "arrowsize": "1.0",
            }
        },
        "enterprise": {
            "graph_attr": {
                "fontsize": "20",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "white",
                "pad": "2.0",
                "splines": "spline",
                "nodesep": "2.0",
                "ranksep": "3.0",
                "dpi": "300",
                "overlap": "false",
                "sep": "+40,40",
                "esep": "+20,20",
                "concentrate": "false",
            },
            "node_attr": {
                "fontsize": "15",
                "fontname": "Segoe UI",
                "margin": "0.3,0.2",
            },
            "edge_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.5",
                "arrowsize": "1.2",
                "labeldistance": "3.0",
                "labelangle": "25",
            }
        },
        "dark": {
            "graph_attr": {
                "fontsize": "16",
                "fontname": "Segoe UI",
                "bgcolor": "#1a1a2e",
                "fontcolor": "white",
                "pad": "1.0",
                "dpi": "300",
                "overlap": "false",
                "nodesep": "1.5",
                "ranksep": "2.0",
            },
            "node_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
                "fontcolor": "white",
            },
            "edge_attr": {
                "fontsize": "11",
                "fontname": "Segoe UI",
                "fontcolor": "white",
                "color": "#00BCF2",
                "penwidth": "1.5",
            }
        },
        "minimal": {
            "graph_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI Light",
                "bgcolor": "white",
                "pad": "0.8",
                "splines": "polyline",
                "nodesep": "1.0",
                "ranksep": "1.2",
                "dpi": "300",
                "overlap": "false",
            },
            "node_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI Light",
            },
            "edge_attr": {
                "fontsize": "10",
                "fontname": "Segoe UI Light",
                "color": "#999999",
                "penwidth": "1.0",
            }
        }
    }

    def __init__(self):
        self.name = 'ArchitectureDiagramAgent'
        self.metadata = {
            "name": self.name,
            "description": """Generate professional architecture diagrams.

Supported diagram types:
- azure: Azure cloud architecture
- agent_system: AI agent/orchestrator architecture
- multi_tier: N-tier application architecture
- microservices: Microservices architecture
- data_flow: Data pipeline/flow diagram
- custom: Custom node/connection diagram

Output formats: png, svg, pdf, mermaid, drawio

Actions:
- create_diagram: Create a diagram from specification
- diagram_from_agents: Generate diagram from RAPP agent configurations
- list_node_types: List available node types
- generate_mermaid: Generate Mermaid.js code

Example:
{
  "action": "create_diagram",
  "diagram_type": "azure",
  "title": "RAPP Architecture",
  "output_format": "png",
  "nodes": [
    {"id": "user", "type": "user", "label": "User"},
    {"id": "func", "type": "function_app", "label": "Azure Functions"},
    {"id": "openai", "type": "openai", "label": "Azure OpenAI"}
  ],
  "connections": [
    {"from": "user", "to": "func", "label": "HTTP"},
    {"from": "func", "to": "openai", "label": "API"}
  ]
}""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["create_diagram", "diagram_from_agents", "list_node_types", "generate_mermaid"]
                    },
                    "diagram_type": {
                        "type": "string",
                        "enum": ["azure", "agent_system", "multi_tier", "microservices", "data_flow", "custom"]
                    },
                    "title": {"type": "string"},
                    "output_format": {
                        "type": "string",
                        "enum": ["png", "svg", "pdf", "mermaid", "drawio"]
                    },
                    "style": {
                        "type": "string",
                        "enum": ["default", "dark", "minimal"]
                    },
                    "nodes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "type": {"type": "string"},
                                "label": {"type": "string"},
                                "cluster": {"type": "string"}
                            }
                        }
                    },
                    "connections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "from": {"type": "string"},
                                "to": {"type": "string"},
                                "label": {"type": "string"},
                                "style": {"type": "string"}
                            }
                        }
                    },
                    "clusters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "label": {"type": "string"},
                                "nodes": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    },
                    "agents": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Agent configurations for diagram_from_agents"
                    },
                    "customer": {
                        "type": "string",
                        "description": "Customer name - creates a subfolder in arch_diagrams for this customer"
                    },
                    "output_filename": {"type": "string"},
                    "output_dir": {"type": "string"}
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)
        self.base_path = self._find_base_path()

    def _find_base_path(self) -> str:
        """Find the base path for the RAPP project."""
        possible_paths = [
            os.getcwd(),
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ]
        for path in possible_paths:
            if os.path.exists(os.path.join(path, "agents")):
                return path
        return os.getcwd()

    def perform(self, **kwargs) -> str:
        """Execute the requested action."""
        action = kwargs.get('action', 'create_diagram')

        try:
            if action == 'list_node_types':
                return self._list_node_types()
            elif action == 'generate_mermaid':
                return self._generate_mermaid(**kwargs)
            elif action == 'diagram_from_agents':
                return self._diagram_from_agents(**kwargs)
            elif action == 'create_diagram':
                output_format = kwargs.get('output_format', 'png')
                if output_format == 'mermaid':
                    return self._generate_mermaid(**kwargs)
                elif output_format == 'drawio':
                    return self._generate_drawio(**kwargs)
                else:
                    return self._create_diagram(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}",
                    "available_actions": ["create_diagram", "diagram_from_agents", "list_node_types", "generate_mermaid"]
                })
        except Exception as e:
            logger.error(f"Diagram generation error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })

    def _list_node_types(self) -> str:
        """List available node types."""
        return json.dumps({
            "status": "success",
            "azure_nodes": list(self.AZURE_NODES.keys()),
            "generic_nodes": list(self.GENERIC_NODES.keys()),
            "note": "Use these type values in the 'type' field of node definitions"
        }, indent=2)

    def _create_diagram(self, **kwargs) -> str:
        """Create a diagram using the diagrams library."""
        if not DIAGRAMS_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": f"diagrams library not available: {DIAGRAMS_IMPORT_ERROR}",
                "suggestion": "Install with: pip install diagrams",
                "fallback": "Use output_format='mermaid' for text-based diagrams"
            })

        title = kwargs.get('title', 'Architecture Diagram')
        diagram_type = kwargs.get('diagram_type', 'custom')
        output_format = kwargs.get('output_format', 'png')
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')
        style = kwargs.get('style', 'professional')  # Default to professional style
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        clusters = kwargs.get('clusters', [])

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            # Sanitize customer name for folder (lowercase, replace spaces with underscores)
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Clean filename (remove extension if present)
        if output_filename.endswith(('.png', '.svg', '.pdf')):
            output_filename = output_filename.rsplit('.', 1)[0]

        # Use temp directory for rendering to avoid path issues with spaces/OneDrive
        import shutil
        temp_dir = tempfile.mkdtemp()
        temp_output_path = os.path.join(temp_dir, output_filename)
        final_output_dir = output_dir
        final_output_path = os.path.join(final_output_dir, f"{output_filename}.{output_format}")

        # Get style configuration
        style_config = self.STYLES.get(style, self.STYLES["professional"])

        try:
            with Diagram(
                title,
                filename=temp_output_path,
                outformat=output_format,
                show=False,
                graph_attr=style_config["graph_attr"],
                node_attr=style_config.get("node_attr", {}),
                edge_attr=style_config.get("edge_attr", {})
            ):
                # Create node objects
                node_objects = {}

                # Handle clusters
                cluster_objects = {}
                for cluster in clusters:
                    cluster_id = cluster.get('id', cluster.get('label', 'Cluster'))
                    cluster_label = cluster.get('label', cluster_id)
                    cluster_objects[cluster_id] = {"label": cluster_label, "nodes": cluster.get('nodes', [])}

                # Create nodes within clusters first
                for cluster_id, cluster_info in cluster_objects.items():
                    with Cluster(cluster_info["label"]):
                        for node in nodes:
                            if node.get('cluster') == cluster_id:
                                node_obj = self._create_node(node)
                                if node_obj:
                                    node_objects[node['id']] = node_obj

                # Create standalone nodes
                for node in nodes:
                    if node['id'] not in node_objects:
                        node_obj = self._create_node(node)
                        if node_obj:
                            node_objects[node['id']] = node_obj

                # Create connections
                for conn in connections:
                    from_id = conn.get('from')
                    to_id = conn.get('to')
                    label = conn.get('label', '')
                    
                    if from_id in node_objects and to_id in node_objects:
                        if label:
                            node_objects[from_id] >> Edge(label=label) >> node_objects[to_id]
                        else:
                            node_objects[from_id] >> node_objects[to_id]

            # Move file from temp to final location
            temp_file = f"{temp_output_path}.{output_format}"
            if os.path.exists(temp_file):
                shutil.copy2(temp_file, final_output_path)
                # Clean up temp directory
                shutil.rmtree(temp_dir, ignore_errors=True)
            
            return json.dumps({
                "status": "success",
                "filename": f"{output_filename}.{output_format}",
                "path": final_output_path,
                "diagram_type": diagram_type,
                "style": style,
                "node_count": len(nodes),
                "connection_count": len(connections),
                "note": "Professional Visio-quality diagram with Azure icons"
            }, indent=2)

        except Exception as e:
            logger.error(f"Diagram creation failed: {e}")
            # Clean up temp directory
            if 'temp_dir' in locals():
                shutil.rmtree(temp_dir, ignore_errors=True)
            # Fallback to mermaid
            return self._generate_mermaid(**kwargs)

    def _create_node(self, node: Dict) -> Any:
        """Create a diagram node based on type."""
        node_type = node.get('type', 'server').lower()
        label = node.get('label', node.get('id', 'Node'))

        # Try Azure nodes first
        if node_type in self.AZURE_NODES:
            node_class_name = self.AZURE_NODES[node_type]
            # Get the class from the appropriate module
            if node_class_name == "FunctionApps":
                return FunctionApps(label)
            elif node_class_name == "VM":
                return VM(label)
            elif node_class_name == "ContainerInstances":
                return ContainerInstances(label)
            elif node_class_name == "KubernetesServices":
                return KubernetesServices(label)
            elif node_class_name == "AppServices":
                return AppServices(label)
            elif node_class_name == "CosmosDb":
                return CosmosDb(label)
            elif node_class_name == "SQLDatabases":
                return SQLDatabases(label)
            elif node_class_name == "DatabaseForPostgresqlServers":
                return DatabaseForPostgresqlServers(label)
            elif node_class_name == "CacheForRedis":
                return CacheForRedis(label)
            elif node_class_name == "BlobStorage":
                return BlobStorage(label)
            elif node_class_name == "StorageAccounts":
                return StorageAccounts(label)
            elif node_class_name == "DataLakeStorage":
                return DataLakeStorage(label)
            elif node_class_name == "LogicApps":
                return LogicApps(label)
            elif node_class_name == "ServiceBus":
                return ServiceBus(label)
            elif node_class_name == "APIManagement":
                return APIManagement(label)
            elif node_class_name == "CognitiveServices":
                return CognitiveServices(label)
            elif node_class_name == "BotServices":
                return BotServices(label)
            elif node_class_name == "MachineLearningServiceWorkspaces":
                return MachineLearningServiceWorkspaces(label)
            elif node_class_name == "Databricks":
                return Databricks(label)
            elif node_class_name == "DataFactories":
                return DataFactories(label)
            elif node_class_name == "LoadBalancers":
                return LoadBalancers(label)
            elif node_class_name == "VirtualNetworks":
                return VirtualNetworks(label)
            elif node_class_name == "ApplicationGateway":
                return ApplicationGateway(label)
            elif node_class_name == "CDNProfiles":
                return CDNProfiles(label)
            elif node_class_name == "Firewall":
                return Firewall(label)
            elif node_class_name == "KeyVaults":
                return KeyVaults(label)
            elif node_class_name == "ApplicationSecurityGroups":
                return ApplicationSecurityGroups(label)

        # Try generic nodes
        if node_type in self.GENERIC_NODES:
            node_class_name = self.GENERIC_NODES[node_type]
            if node_class_name == "Users":
                return Users(label)
            elif node_class_name == "Client":
                return Client(label)
            elif node_class_name == "Internet":
                return Internet(label)
            elif node_class_name == "Teams":
                return Teams(label)
            elif node_class_name == "Slack":
                return Slack(label)
            elif node_class_name == "Server":
                return Server(label)
            elif node_class_name == "SQL":
                return SQL(label)
            elif node_class_name == "Storage":
                return Storage(label)
            elif node_class_name == "Rack":
                return Rack(label)
            elif node_class_name == "Python":
                return Python(label)

        # Default to Server
        return Server(label)

    def _generate_mermaid(self, **kwargs) -> str:
        """Generate Mermaid.js diagram code."""
        title = kwargs.get('title', 'Architecture Diagram')
        diagram_type = kwargs.get('diagram_type', 'custom')
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        clusters = kwargs.get('clusters', [])
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Build mermaid code
        lines = ["```mermaid", "flowchart TB"]
        
        # Add title as comment
        lines.append(f"    %% {title}")
        lines.append("")

        # Group nodes by cluster
        cluster_nodes = {}
        standalone_nodes = []
        
        for node in nodes:
            cluster_id = node.get('cluster')
            if cluster_id:
                if cluster_id not in cluster_nodes:
                    cluster_nodes[cluster_id] = []
                cluster_nodes[cluster_id].append(node)
            else:
                standalone_nodes.append(node)

        # Add clusters
        for cluster in clusters:
            cluster_id = cluster.get('id', '')
            cluster_label = cluster.get('label', cluster_id)
            lines.append(f"    subgraph {cluster_id}[{cluster_label}]")
            
            # Add nodes in this cluster
            for node in cluster_nodes.get(cluster_id, []):
                node_id = node.get('id', '')
                label = node.get('label', node_id)
                shape = self._get_mermaid_shape(node.get('type', 'server'))
                lines.append(f"        {node_id}{shape[0]}{label}{shape[1]}")
            
            lines.append("    end")
            lines.append("")

        # Add standalone nodes
        for node in standalone_nodes:
            node_id = node.get('id', '')
            label = node.get('label', node_id)
            shape = self._get_mermaid_shape(node.get('type', 'server'))
            lines.append(f"    {node_id}{shape[0]}{label}{shape[1]}")

        lines.append("")

        # Add connections
        for conn in connections:
            from_id = conn.get('from', '')
            to_id = conn.get('to', '')
            label = conn.get('label', '')
            style = conn.get('style', 'arrow')
            
            arrow = self._get_mermaid_arrow(style)
            if label:
                lines.append(f"    {from_id} {arrow}|{label}| {to_id}")
            else:
                lines.append(f"    {from_id} {arrow} {to_id}")

        lines.append("```")

        mermaid_code = "\n".join(lines)

        # Save to file if requested
        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            md_path = os.path.join(output_dir, f"{output_filename}.md")
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(mermaid_code)

            return json.dumps({
                "status": "success",
                "format": "mermaid",
                "filename": f"{output_filename}.md",
                "path": md_path,
                "mermaid_code": mermaid_code
            }, indent=2)

        return json.dumps({
            "status": "success",
            "format": "mermaid",
            "mermaid_code": mermaid_code
        }, indent=2)

    def _get_mermaid_shape(self, node_type: str) -> Tuple[str, str]:
        """Get Mermaid shape markers for a node type."""
        shapes = {
            "user": ["((", "))"],       # Circle
            "users": ["((", "))"],
            "database": ["[(", ")]"],   # Cylinder
            "sql": ["[(", ")]"],
            "cosmos": ["[(", ")]"],
            "cosmosdb": ["[(", ")]"],
            "storage": ["[(", ")]"],
            "blob": ["[(", ")]"],
            "function": ["[/", "\\]"],  # Trapezoid
            "function_app": ["[/", "\\]"],
            "openai": ["{{", "}}"],     # Hexagon
            "cognitive": ["{{", "}}"],
            "ml": ["{{", "}}"],
            "agent": [">", "]"],        # Flag
            "server": ["[", "]"],       # Rectangle
            "default": ["[", "]"],
        }
        return shapes.get(node_type.lower(), shapes["default"])

    def _get_mermaid_arrow(self, style: str) -> str:
        """Get Mermaid arrow style."""
        arrows = {
            "arrow": "-->",
            "dotted": "-.->",
            "thick": "==>",
            "bidirectional": "<-->",
        }
        return arrows.get(style, "-->")

    def _generate_drawio(self, **kwargs) -> str:
        """Generate Draw.io XML (compatible with Visio import)."""
        title = kwargs.get('title', 'Architecture Diagram')
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Draw.io XML structure
        xml_parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<mxfile host="app.diagrams.net">',
            '  <diagram name="Page-1">',
            '    <mxGraphModel dx="1000" dy="600" grid="1" gridSize="10">',
            '      <root>',
            '        <mxCell id="0"/>',
            '        <mxCell id="1" parent="0"/>',
        ]

        # Add nodes
        x, y = 100, 100
        node_positions = {}
        
        for i, node in enumerate(nodes):
            node_id = node.get('id', f'node_{i}')
            label = node.get('label', node_id)
            node_type = node.get('type', 'server')
            
            # Calculate position (simple grid layout)
            pos_x = 100 + (i % 4) * 200
            pos_y = 100 + (i // 4) * 150
            node_positions[node_id] = (pos_x, pos_y)
            
            # Get shape style based on type
            style = self._get_drawio_style(node_type)
            
            xml_parts.append(f'        <mxCell id="{node_id}" value="{label}" style="{style}" vertex="1" parent="1">')
            xml_parts.append(f'          <mxGeometry x="{pos_x}" y="{pos_y}" width="120" height="60" as="geometry"/>')
            xml_parts.append('        </mxCell>')

        # Add connections
        for i, conn in enumerate(connections):
            from_id = conn.get('from', '')
            to_id = conn.get('to', '')
            label = conn.get('label', '')
            edge_id = f'edge_{i}'
            
            xml_parts.append(f'        <mxCell id="{edge_id}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" source="{from_id}" target="{to_id}" parent="1">')
            xml_parts.append('          <mxGeometry relative="1" as="geometry"/>')
            xml_parts.append('        </mxCell>')

        xml_parts.extend([
            '      </root>',
            '    </mxGraphModel>',
            '  </diagram>',
            '</mxfile>',
        ])

        xml_content = '\n'.join(xml_parts)

        # Save to file
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        xml_path = os.path.join(output_dir, f"{output_filename}.drawio")
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

        return json.dumps({
            "status": "success",
            "format": "drawio",
            "filename": f"{output_filename}.drawio",
            "path": xml_path,
            "note": "Open with draw.io or import into Visio"
        }, indent=2)

    def _get_drawio_style(self, node_type: str) -> str:
        """Get Draw.io style for a node type."""
        styles = {
            "user": "shape=ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
            "database": "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;fillColor=#f5f5f5;strokeColor=#666666;",
            "function": "shape=step;perimeter=stepPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#fff2cc;strokeColor=#d6b656;",
            "openai": "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;",
            "agent": "shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
            "server": "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;",
        }
        return styles.get(node_type.lower(), styles["server"])

    def _diagram_from_agents(self, **kwargs) -> str:
        """Generate diagram from RAPP agent configurations."""
        agents = kwargs.get('agents', [])
        title = kwargs.get('title', 'RAPP Agent Architecture')
        output_format = kwargs.get('output_format', 'png')

        if not agents:
            # Try to load agents from the agents directory
            agents = self._discover_agents()

        # Build nodes and connections from agent configs
        nodes = []
        connections = []

        # Add user node
        nodes.append({"id": "user", "type": "user", "label": "User"})

        # Add RAPP core
        nodes.append({"id": "rapp_core", "type": "function_app", "label": "RAPP Core\n(Azure Functions)", "cluster": "azure"})
        connections.append({"from": "user", "to": "rapp_core", "label": "HTTP"})

        # Add OpenAI
        nodes.append({"id": "openai", "type": "openai", "label": "Azure OpenAI", "cluster": "azure"})
        connections.append({"from": "rapp_core", "to": "openai", "label": "API"})

        # Add agents
        for i, agent in enumerate(agents):
            agent_id = f"agent_{i}"
            agent_name = agent.get('name', agent.get('id', f'Agent {i+1}'))
            nodes.append({
                "id": agent_id,
                "type": "agent",
                "label": agent_name,
                "cluster": "agents"
            })
            connections.append({"from": "rapp_core", "to": agent_id, "label": ""})

        # Define clusters
        clusters = [
            {"id": "azure", "label": "Azure Cloud"},
            {"id": "agents", "label": "RAPP Agents"}
        ]

        # Create the diagram
        return self._create_diagram(
            title=title,
            nodes=nodes,
            connections=connections,
            clusters=clusters,
            output_format=output_format,
            **kwargs
        )

    def _discover_agents(self) -> List[Dict]:
        """Discover agents from the agents directory."""
        agents = []
        agents_dir = os.path.join(self.base_path, 'agents')
        
        if os.path.exists(agents_dir):
            for filename in os.listdir(agents_dir):
                if filename.endswith('_agent.py') and not filename.startswith('__'):
                    agent_name = filename.replace('_agent.py', '').replace('_', ' ').title()
                    agents.append({"name": agent_name, "file": filename})

        return agents[:10]  # Limit to 10 agents for readability
