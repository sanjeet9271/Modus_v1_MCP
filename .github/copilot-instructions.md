# Modus Project Instructions

> **IMPORTANT:** Before providing any assistance, ALWAYS review the `copilot-lessons-learned.md` file to ensure you don't repeat past mistakes, especially regarding event handling and component implementations.

**When working on a Modus project or generating components, strictly adhere to the following guidelines**:

## General Instructions for Modus Projects

- **You're using Powershell terminal so avoid using `&&` command for concatenation of multiple commands.**
- Work step by step, ensuring each component is correctly implemented before moving on to the next.
- **Don't waste Time on fixing trivial typescript errors**. Focus on the functionality and correctness of the components.

### **Strict Adherence Process for Modus Projects:**

1.  **Instructions Read and Understood**: Confirm that all project instructions have been thoroughly reviewed and comprehended.
2.  **.github/copilot-lessons-learned.md Read and Understood**: Verify that the `copilot-lessons-learned.md` file has been read and its contents understood to avoid past mistakes.
3.  **Modus React Components Installation Check**:
    * Inspect `package.json` to confirm the presence of `@trimble-oss/modus-react-components`.
    * If not found, use the appropriate tool to obtain installation instructions and proceed with the installation.
    * If legacy error occurs use the --legacy-peer-deps flag to install the package.
4.  **Planning and Logging**:
    * Develop a detailed plan for the project, outlining the components to be used and the overall structure.
    * **Log each step of the planning process.**
5.  **Iterative Component Implementation**:
    * For each part of the plan:
        * **Identify Modus React Components**: Use `get_list_of_all_modus_components` to identify suitable components.
        * **Obtain Component Details**: Use `get_component_details` to fetch properties and usage examples for the selected component.
        * **Implement and Test**: Implement the component. Use **Browser MCPs** to rigorously test its rendering and functionality.
        * **Iterate**: If the component renders correctly and meets requirements, proceed to the next part of the plan; otherwise, re-evaluate and fix.
6.  **Continuous Alignment and Width Check**: Throughout the development process, consistently use Browser MCP to ensure components maintain full screen width and proper alignment, keeping them aesthetically centered.
7.  **DOM Event Prioritization**: When implementing event handlers, always prioritize predefined DOM events. Use `get_component_details` to verify available events. Custom events are a last resort.
8.  **Modus Icon Verification**: Before using any Modus Icon, utilize the `get_list_of_all_modus_icons` tool to confirm the icon's availability and correct naming.



## Guidelines for Working on Modus Projects

1.  **Installation Verification**: Before starting any project, ensure that the `@trimble-oss/modus-react-components` library is installed. If not, use tools to get the instructions to install and install it accordingly.
2.  **Accuracy Priority**: Accuracy is paramount. You may proceed slowly and learn step-by-step, but the output must be highly accurate.
3.  **Component Listing**: Always begin by listing all available Modus components using the `get_list_of_all_modus_components` tool. Plan the components you intend to use.
4.  **Component Details**: Obtain component details regarding properties and usage examples using the `get_component_details` tool.
5.  **Error Fixing**: When addressing errors related to any component, first fetch the details and usage examples of that component using the tool.
6.  **Predefined Events**: Use predefined DOM events and interfaces rather than creating custom ones.
7.  **Imports**: Import only the names of components from the `@trimble-oss/modus-react-components` library. Avoid unnecessary imports as they may not exist.
8.  **Design Practices**: Follow best design practices by utilizing the full width of the screen.
9.  **Correct Properties**: Ensure you are using the correct properties defined for Modus components.
10. **Sequential Process**: Follow the sequence: **Do not invent custom properties.** First, find the properties and usage examples before using a component.
11. **Planning and Testing**: Follow an iterative approach; first create a component, then use your browser MCP to test it. If it is giving sufficient results, move to the next part of the plan. But first, write the plan.
12. **Modular Design**: Structure your code modularly. Avoid making a single file too large and adhere to best coding practices.
13. **Component-Specific Imports**: For components like `ModusList`, `ModusAccordion`, and `ModusTreeview`, ensure you import their corresponding `Item` and obtain their properties as well.
14. **Navbar Variants**: For the Navbar, choose between the `blue` and `default` variants. Change the logo accordingly:
    -   Blue variant: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg`
    -   Default variant: `https://modus.trimble.com/img/trimble-logo.svg`
    -   Note: The difference is the `rev` in the logo URL.
15. **Navbar Features**: When generating a Navbar, include minimum features like a hamburger menu (Apps Menu) and other elements as given in examples.
16. **DOM events**: Check for the DOM events that are available for the component you are working on. Use the `get_component_details` tool to fetch the list. **Always prefer the predefined DOM events**. Avoid creating custom events unless absolutely necessary.
17. **Screen Width and Alignment**: Always use the full screen-width; the react-components might have their own width. Make sure every component is properly aligned with others; you can test that out using your browser MCP.
18. **Alignment**: If you're using full width and there's a component, you must keep it in the center so that aesthetically it looks beautiful.
19. **Modus ICON Names**: Before using any Modus Icon name, ensure to Use the `get_list_of_all_modus_icons` tool to fetch the list of available icons. **You can pass starting character to fetch list of all the icons available with that starting character or you can pass empty string to fetch all the icons.**

---

## Best Practices Guide for Modus Projects

### Directory Structure

-   **Always follow the react best practices for a project. The Code should be Modular and maintainable.**
-   **Modular Organization**: Organize your project into a modular directory structure. Each component should have its own directory containing:
    -   `index.js` or `index.tsx` for the main component file.
    -   `styles.css` or `styles.module.css` for component-specific styles.
    -   `tests` directory for unit tests related to the component.
    -   `utils` directory for any helper functions specific to the component.
-   **Common Directories**:
    -   `components`: Contains all reusable components.
    -   `pages`: Contains page-level components that utilize the reusable components.
    -   `assets`: Contains images, fonts, and other static assets.
    -   `hooks`: Contains custom React hooks.
    -   `context`: Contains context providers for global state management.

### React Router Usage

-   **Routing Setup**: Use React Router to manage navigation between different pages. This helps avoid a single, bloated page and improves application performance.
    -   Define routes in a central `App.js` or `App.tsx` file.
    -   Use nested routes for complex layouts.
    -   Utilize `BrowserRouter` for standard web applications.

### Event Handling

-   **Isolated Event Variables**: Ensure event variables are isolated to prevent interference between components.
    -   Use local state within components for event handling.
    -   Utilize context or Redux for global state management when necessary, ensuring separation of concerns.

## Testing and Validation

-   **Browser MCP Tools**: Regularly use browser MCP (Modus Component Playground) tools to test and validate component functionality.
    -   Check for responsiveness and cross-browser compatibility.
    -   Validate component interactions and event handling.

---