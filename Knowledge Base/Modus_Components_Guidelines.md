# Modus Components Guidelines

## Overview

This document provides high-level guidelines for using Modus React components in your applications. For detailed property references and examples, please refer to the companion documents in the Knowledge Base.

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

### Angular Framework Setup

For using Modus with Angular, follow these steps:

1. Install the Modus Angular Components Library and its dependencies:

```bash
npm install @trimble-oss/modus-angular-components --save
```

2. Add the following snippet to your main.ts (or any main module):

```typescript
import { defineCustomElements } from '@trimble-oss/modus-web-components/loader';

defineCustomElements();
```

3. Add the CUSTOM_ELEMENTS_SCHEMA to your app.module.ts (or any app module):

```typescript
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@NgModule({
  // ...other module configurations
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
```

4. Example Usage - add a Modus button in your app.component.html:

```html
<modus-button color="primary" [disabled]="false">Modus Button</modus-button>
```

5. Contributing: To contribute to the Modus Angular Components library, please see the Modus Web Components contributing guidelines.

## Component Selection Guide

When deciding which component to use:

1. **Purpose First**: Select components based on their intended purpose, not just appearance
2. **Simplicity**: Choose the simplest component that meets your requirements
3. **Consistency**: Use the same component for similar functions across your application
4. **Feedback**: Ensure components provide appropriate feedback for user interactions
