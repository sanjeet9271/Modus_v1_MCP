import os
import json

class ComponentRegistry:
    """Registry for Modus components, handling component details and examples"""
    
    def __init__(self):
        # Paths for knowledge base files
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.db_path = os.path.join(self.base_path, "Knowledge Base", "db.json")
        self.db_ui_path = os.path.join(self.base_path, "Knowledge Base", "db_ui.json")
        self.kb_path = os.path.join(self.base_path, "Knowledge Base", "From_KB.md")
        self.ui_kb_path = os.path.join(self.base_path, "Knowledge Base", "UI_KB.md")
    
    def get_all_components(self):
        """Get list of all available components (both form and UI)"""
        try:
            components = []
            
            # Get form components
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "components" in data and "form" in data["components"]:
                    components.extend(list(data["components"]["form"].keys()))
            
            # Get UI components
            with open(self.db_ui_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "components" in data and "ui" in data["components"]:
                    components.extend(list(data["components"]["ui"].keys()))
            
            return components
        except Exception as e:
            print(f"Error getting component list: {e}")
            return []
    
    def get_component_properties_and_events(self, component_name):
        """Get properties, events and description for a specific component"""
        try:
            # Check form components first
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if ("components" in data and 
                "form" in data["components"] and 
                component_name in data["components"]["form"]):
                
                component_data = data["components"]["form"][component_name]
                return {
                    "properties": component_data.get("properties", []),
                    "events": component_data.get("events", []),
                    "methods": component_data.get("methods", []),
                    "description": component_data.get("description", "")
                }
            
            # If not found in form components, check UI components
            with open(self.db_ui_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if ("components" in data and 
                "ui" in data["components"] and 
                component_name in data["components"]["ui"]):
                
                component_data = data["components"]["ui"][component_name]
                return {
                    "properties": component_data.get("properties", []),
                    "events": component_data.get("events", []),
                    "methods": component_data.get("methods", []),
                    "description": component_data.get("description", "")
                }
            
            return {"properties": [], "events": [], "methods": [], "description": ""}
        except Exception as e:
            print(f"Error getting component properties: {e}")
            return {"properties": [], "events": [], "methods": [], "description": ""}
    
    def _extract_kb_examples(self, content, component_name):
        """Extract examples for a specific component from the knowledge base"""
        examples = []
        try:
            # Try to find examples in Form KB
            examples = self._extract_examples_from_content(self.kb_path, component_name)
            
            # If no examples found, try UI KB
            if not examples:
                examples = self._extract_examples_from_content(self.ui_kb_path, component_name)
            
            return examples
        except Exception as e:
            print(f"Error extracting examples: {e}")
            return []
    
    def _extract_examples_from_content(self, kb_path, component_name):
        """Helper method to extract examples from a specific KB file"""
        try:
            with open(kb_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            examples = []
            # Parse examples section for the component
            sections = content.split("# <")
            component_section = None
            
            for section in sections:
                if section.startswith(component_name):
                    component_section = section
                    break
            
            if component_section:
                # Extract examples from the component section
                prompts = component_section.split("## Prompt")
                
                # Skip the first split which contains the component header
                for i, prompt in enumerate(prompts[1:], 1):
                    example = {
                        "prompt_number": i,
                        "question": "",
                        "code": ""
                    }
                    
                    # Extract the user question
                    question_parts = prompt.split("**User Question:**")
                    if len(question_parts) > 1:
                        answer_parts = question_parts[1].split("**Agent Answer:**")
                        if len(answer_parts) > 0:
                            example["question"] = answer_parts[0].strip()
                    
                    # Extract the code example
                    code_start = prompt.find("```tsx")
                    code_end = prompt.find("```", code_start + 6) if code_start != -1 else -1
                    
                    if code_start != -1 and code_end != -1:
                        example["code"] = prompt[code_start+6:code_end].strip()
                    
                    examples.append(example)
            
            return examples
        except Exception as e:
            print(f"Error extracting examples from {kb_path}: {e}")
            return []
            
    def get_installation_guidelines(self):
        """Get installation and usage guidelines"""
        try:
            guidelines_path = os.path.join(self.base_path, "Knowledge Base", "Modus_Components_Guidelines.md")
            with open(guidelines_path, 'r', encoding='utf-8') as f:
                guidelines = f.read()
            return guidelines
        except Exception as e:
            print(f"Error loading guidelines: {e}")
            return "Guidelines not available."