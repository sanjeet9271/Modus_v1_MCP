# Modus Guidelines - High-Level Orchestration

> **ARCHITECT LEVEL GUIDANCE**: This document provides guidance on how to approach different types of Modus implementation queries **follow this religiously**
> **Important**: You're using `Powershell` terminal use the corresponding commands. Don't use `&&` instead use `;` to separate commands.
   - Keep Note of the following pointers very strictly
      1. Try to use Modus Components wherever possible, don't use HTML elements e.g. use `ModusAlert` instead of showing custom errors.
      2. Prefer the properties and events of the components rather than defining cutom events and CSS.
      3. **Before using any component always get it's details using `get_component_details`.**


> **IMPORTANT**:  Whenever you get a query follow the following sequence strictly.

1. **Identify Framework** - **First determine and log which framework the query is related to**:
   - React
   - Angular
   
2. **Identify Query Type** - Determine what category the query falls into:
   - New project implementation
   - Component implementation
   - Error troubleshooting
   - State management
   - Styling and layout
   
3. **Read the Appropriate Documents** - Based on framework and query type - Read the content whenever a new session starts.
   
   ## For React Framework
   
   - If related to new project setup:
     - Log: "Loading React project implementation guidance"
     - Read: [Implementation Steps](./modus-implementation-steps.instructions.md) - **Follow the steps in this strictly without skipping any one**
     - Read: [Core Principles](./instructions/core-principles.instructions.md)
     - Read: [React Best Practices](./instructions/frameworks/react/best-practices.instructions.md)
     - Read: [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)
   
   - If related to component implementation:
     - Log: "Loading React component implementation patterns"
     - Read: [Component Patterns](./instructions/frameworks/react/component-patterns.instructions.md)
     - Read: [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)
   
   - If related to state management:
     - Log: "Loading React state management patterns"
     - Read: [State Management](./instructions/frameworks/react/state-management.instructions.md)
     - Read: [Component Patterns](./instructions/frameworks/react/component-patterns.instructions.md)
   
   ## For Angular Framework
   
   - If related to new project setup:
     - Log: "Loading Angular project implementation guidance"
     - Read: [Implementation Steps](./modus-implementation-steps.instructions.md) - **Follow the steps in this strictly without skipping any one**
     - Read: [Core Principles](./instructions/core-principles.instructions.md)
     - Read: [Angular Best Practices](./instructions/frameworks/angular/best-practices.instructions.md)
     - Read: [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)
   
   - If related to component implementation:
     - Log: "Loading Angular component implementation patterns"
     - Read: [Component Patterns](./instructions/frameworks/angular/component-patterns.instructions.md)
     - Read: [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)
   
   - If related to state management:
     - Log: "Loading Angular state management patterns"
     - Read: [State Management](./instructions/frameworks/angular/state-management.instructions.md)
     - Read: [Component Patterns](./instructions/frameworks/angular/component-patterns.instructions.md)
   
   ## For All Frameworks
   
   - If related to error troubleshooting or adding mistake or pointer to lessons learned it should be added to common-mistakes:
     - Log: "Loading troubleshooting guidance"
     - Read: [Troubleshooting Guide](./instructions/error-correction/troubleshooting-guide.instructions.md)
     - Read: [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)
   
   - If related to styling and layout:
     - Log: "Loading style guide"
     - Read the Style Guide section below
     
3. **Each time Before Implementing any Component** - strictly check it's details:
   - Use `get_list_of_all_modus_components` to verify component existence
   - Use `get_component_details` to understand properties and events

## Style Guide

- **Component Grouping**: Always group related web components inside a container div
  ```jsx
  <div style={{
    display: 'flex',
    flexDirection: 'column', // or 'row' for horizontal layout
    gap: '16px', // minimum gap should be 8px
    padding: '16px',
    margin: '0 auto', // for center alignment
    width: '100%', // or appropriate width
    maxWidth: '1200px' // optional max width
  }}>
    {/* Child components go here */}
  </div>
  ```

- **Layout Principles**:
  - For vertically stacked elements: `flexDirection: 'column'`
  - For horizontally stacked elements: `flexDirection: 'row'`
  - Always provide a minimum gap of 8px between components
  - Either align content to center or provide consistent left/right padding (16px minimum)

- **Component Dimensions**:
  - Ensure all components have appropriate height and width
  - Prevent overflow with `overflow: 'auto'` or specific handling
  - Use relative units (%, vh/vw) when appropriate for responsive design

- **Navigation Components**:
  - Navbar should span full width at the top: `width: '100%', position: 'sticky', top: 0, zIndex: 1000`
  - SideNavigation height should be: `height: 'calc(100vh - 56px)'` to account for navbar

- **Typography**: Use `Open Sans` font family for all text elements

- **Image Placeholders**: When specific URLs are not provided, use:
  - Trimble assets: `https://modus.trimble.com/img/` or `https://modus-bootstrap.trimble.com/img/`
  - Default placeholders: `https://picsum.photos/[width]/[height]?random=[id]`
  - Logo variants for Navbar:
    - Blue variant: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg` (white version)
    - Default variant: `https://modus.trimble.com/img/trimble-logo.svg` (dark version)

## Documentation Procedures

### For New Discovered Issues
Whenever a new issue or error pattern is identified:
1. Document the issue in `[Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)`
2. Include:
   - Just a pointer regarding what was wrong and what is the correct way.

