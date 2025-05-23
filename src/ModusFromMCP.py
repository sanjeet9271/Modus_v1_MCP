from mcp.server.fastmcp import FastMCP
from modules.component_registry import ComponentRegistry
import sys
import os
import json

# Instantiate MCP server
mcp = FastMCP(
    "Modus Components",  # Updated name to be more generic
    description="An MCP server providing information about Modus React form and UI components",
    version="1.0.0",
    transport="sse",
    port=3001,
    allow_origins=["*"]
)

# Initialize component registry
registry = ComponentRegistry()

# Tool 1: Return guidelines for getting started
@mcp.tool()
def getting_started_installation_and_guidelines():
    """Get guidelines for installation and usage of Modus components"""
    try:
        guidelines = registry.get_installation_guidelines()
        return {"success": True, "guidelines": guidelines}
    except Exception as e:
        print(f"Error in getting_started_installation_and_guidelines: {str(e)}")
        return {"success": False, "error": str(e)}

# Tool 2: List all Modus components
@mcp.tool()
def get_list_of_all_modus_components():
    """Get a list of all available Modus components (both form and UI)"""
    try:
        components = registry.get_all_components()
        return {"success": True, "components": components}
    except Exception as e:
        print(f"Error in get_list_of_all_modus_components: {str(e)}")
        return {"success": False, "error": str(e)}

# Tool 3: Get details for a specific component
@mcp.tool()
def get_component_details(component_name: str):
    """Get properties and usage examples for a specific Modus component"""
    try:
        print(f"Fetching details for component: {component_name}")
        
        # Get component properties from registry
        component_info = registry.get_component_properties_and_events(component_name)
        
        if not component_info["properties"]:
            error_msg = f"Component {component_name} not found in component registry"
            print(error_msg)
            return {"success": False, "error": error_msg}
        
        # Get examples using the registry method
        kb = get_knowledge_base()
        examples = []
        if kb and kb["content"]:
            examples = registry._extract_kb_examples(kb["content"], component_name)
        
        result = {
            "success": True,
            "component": component_name,
            "description": component_info["description"],
            "properties": component_info["properties"],
            "events": component_info["events"],
            "methods": component_info["methods"],
            "examples": examples
        }
        
        print(f"Successfully fetched details for {component_name}")
        return result
    except Exception as e:
        print(f"Error in get_component_details: {str(e)}")
        return {"success": False, "error": str(e)}

# Add knowledge base as a resource
@mcp.resource(name="modus_kb", uri="http://localhost:3001/resources/modus_kb")
def get_knowledge_base():
    """Knowledge base for Modus components with examples and best practices"""
    try:
        kb_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                            "Knowledge Base", "From_KB.md")
        ui_kb_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                               "Knowledge Base", "UI_KB.md")
        
        # Combine content from both knowledge bases
        content = ""
        
        # Read form components KB
        if os.path.exists(kb_path):
            with open(kb_path, 'r', encoding='utf-8') as f:
                content += f.read()
        
        # Read UI components KB
        if os.path.exists(ui_kb_path):
            with open(ui_kb_path, 'r', encoding='utf-8') as f:
                content += "\n\n" + f.read()
        
        return {
            "content": content,
            "type": "markdown",
            "description": "Knowledge base for Modus components including examples"
        }
    except Exception as e:
        print(f"Error loading knowledge base: {e}")
        return None

# Start the server when this module is run directly
if __name__ == "__main__":
    print("Starting Modus Components MCP Server on http://localhost:3001")
    print("Available tools:")
    print("- getting_started_installation_and_guidelines")
    print("- get_list_of_all_modus_components")
    print("- get_component_details")
    try:
        mcp.run(transport="sse")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)