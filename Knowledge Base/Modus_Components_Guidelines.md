# Modus Components Guidelines

## Overview

This document provides high-level guidelines for using Modus React components in your applications. For detailed property references and examples, please refer to the companion documents in the Knowledge Base.

## Component References

- For detailed component properties, events, and methods: see [React_Modus_Component_Properties.md](React_Modus_Component_Properties.md)
- For implementation examples and patterns: see [knowledge_base_final.md](knowledge_base_final.md)

## Installation

### Package Installation

```bash
npm install @trimble-oss/modus-react-components --save
```

### Required Font

Make sure the Open Sans font is available in your application:

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700&display=fallback" rel="stylesheet" />
```

### Web Components Setup (if using)

For Modus Web Components, use the following:

```bash
npm install @trimble-oss/modus-web-components --save
```

Then initialize the components in your entry file:

```javascript
import { defineCustomElements } from '@trimble-oss/modus-web-components/loader';

defineCustomElements(); 
```

## Available Components

### Form Components

- **ModusTextInput**: Text input field for capturing user input
- **ModusDatePicker**: Calendar popup for selecting dates
- **ModusCheckbox**: Checkbox selection control
- **ModusAutocomplete**: Input with autocomplete suggestions
- **ModusSelect**: For selcting form various options

## Best Practices

1. **Consistency**
   - Maintain consistent styling across your application
   - Use the same variant of a component throughout related sections
   - Follow Modus Design System color palette and spacing

2. **Accessibility**
   - Always include labels for form components
   - Use `ariaLabel` attributes when appropriate
   - Ensure sufficient color contrast (4.5:1 minimum)
   - Support keyboard navigation

3. **Responsive Design**
   - Test components across different viewport sizes
   - Use appropriate component sizes based on context
   - Consider mobile touch targets (min 44x44px)

4. **Form Validation**
   - Provide clear, concise error messages
   - Position error feedback close to the error source
   - Use helper text to provide guidance before errors occur
   - Validate inputs at appropriate times (on submit, on blur)

5. **Performance**
   - Avoid unnecessary re-renders of components
   - Implement pagination for large data sets
   - Consider lazy loading for complex components

## Component Selection Guide

When deciding which component to use:

1. **Purpose First**: Select components based on their intended purpose, not just appearance
2. **Simplicity**: Choose the simplest component that meets your requirements
3. **Consistency**: Use the same component for similar functions across your application
4. **Feedback**: Ensure components provide appropriate feedback for user interactions

## Additional Resources

- [Trimble Modus Design System](https://modus.trimble.com/)
- [Modus React Components GitHub](https://github.com/trimble-oss/modus-react-components)
- [Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/)