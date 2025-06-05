# Modus Guidelines - Core Principles

> **ARCHITECT LEVEL GUIDANCE**: This document provides high-level direction for Modus project implementation. It defines the core principles that all team members must follow.

## Core Principles

### 1. Component Verification
- **ALWAYS** verify component existence before use through official tools
- **NEVER** assume a component exists or has specific properties

### 2. Evidence-Based Implementation
- **ALWAYS** base implementations on official examples and documentation
- **NEVER** make assumptions about component behavior

### 3. DOM Event Prioritization
- **ALWAYS** use native DOM events over React synthetic events
- **NEVER** create custom event handlers when native ones exist

### 4. Modular Architecture
- **ALWAYS** create modular, reusable components
- **NEVER** build monolithic page components

### 5. Visual Consistency
- **ALWAYS** ensure full-width layouts and proper component alignment
- **NEVER** sacrifice visual quality for implementation speed

### 6. Event Cleanup
- **ALWAYS** provide cleanup functions in useEffect hooks
- **NEVER** leave event listeners that could cause memory leaks

### 7. Icon Verification
- **ALWAYS** verify icon names before using them
- **NEVER** use unverified icon names that might not exist

### 8. Component Substitution
- **ALWAYS** use Modus components instead of HTML elements
- **NEVER** create custom components when Modus alternatives exist

### 9. Documentation
- **ALWAYS** document special considerations and workarounds
- **NEVER** implement undocumented solutions

### 10. Testing
- **ALWAYS** test components both individually and in context
- **NEVER** assume a component works without verification

## Standard Project Structure

```
src/
├── components/           # Reusable components
│   ├── layout/          # Layout components (Navbar, Sidebar, Footer)
│   ├── shared/          # Shared components used across features
│   └── feature/         # Feature-specific components
├── pages/               # Page components that use reusable components
├── context/             # Context providers for state management
├── hooks/               # Custom React hooks
├── routes/              # Routing configuration
├── utils/               # Utility functions
└── assets/              # Static assets
```
