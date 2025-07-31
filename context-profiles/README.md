# Context Profiles

## Overview

This directory contains structured context profile templates designed for use with AI systems such as ChatGPT, Claude, and other platforms. These profiles provide a standardized framework for defining your authentic voice, audience characteristics, brand voice, business context, and story bank.

## Purpose

The context profiles serve as comprehensive input templates that can be used with AI systems to generate highly targeted, consistent, and authentic content. By providing detailed context about your voice, audience, and business objectives, these profiles enable AI systems to produce content that maintains brand consistency and resonates with your specific target audience.

## Structure

Each context profile consists of four core components:

### 1. Brand Voice (`brand-voice.yaml`)
- **Core personality traits** and communication style
- **Signature elements** that make your voice distinctive
- **Tone guidelines** for different content types
- **Authenticity checks** to maintain consistency
- **Platform-specific adaptations** for different channels

### 2. Audience Profile (`audience-profile.yaml`)
- **Demographics** of your target audiences
- **Psychographics** including mindset, values, and motivations
- **Pain points** and challenges your audience faces
- **Engagement preferences** and content consumption habits
- **Platform-specific behaviors** and expectations

### 3. Business Context (`business-context.yaml`)
- **Company positioning** and market differentiation
- **Services and offerings** you provide
- **Business objectives** and success metrics
- **Competitive advantages** and unique value propositions
- **Strategic priorities** for content creation

### 4. Story Bank (`story-bank.yaml`)
- **Categorized narratives** and experiences
- **Recurring themes** and messaging frameworks
- **Character archetypes** and scenarios
- **Content multiplication strategies** for different platforms

## Usage with AI Systems

### Option 1: Copy and Paste Method
Copy the relevant YAML structure into your AI prompt, then populate the fields with your specific content. The structured format ensures comprehensive context coverage and consistent output quality.

### Option 2: System Prompt Integration
Many AI platforms now support system prompts or project knowledge bases:

- **Claude**: Add context profiles to your project knowledge base
- **ChatGPT**: Include context profiles in your custom instructions
- **Other platforms**: Upload context profiles to your AI workspace

This approach keeps your brand voice and audience context always available for content creation.

### Best Practices
1. **Complete Profile Setup**: Fill out all relevant sections for maximum context richness
2. **Regular Updates**: Refresh profiles as your brand voice and audience evolve
3. **Platform Customization**: Adapt the voice and messaging for different social platforms
4. **Consistency Checks**: Use the authenticity check sections to maintain brand alignment

### Example Prompt Structure
```
Using the following context profile:

[Insert populated YAML content]

Create a [content type] that [specific request]
```

### Benefits
- **Consistency**: Maintains brand voice across all AI-generated content
- **Targeting**: Ensures content resonates with specific audience segments
- **Efficiency**: Reduces the need for lengthy context explanations in each prompt
- **Scalability**: Enables consistent content generation across team members
- **Quality**: Provides guardrails for authentic, on-brand messaging

## Implementation Notes

- These templates contain only the structural keys - populate with your specific content
- Adapt the structure to match your unique brand requirements
- Use in combination with specific content generation requests for best results
- Regular profile audits ensure continued relevance and effectiveness

## Supported AI Platforms

These context profiles are compatible with:
- OpenAI's ChatGPT
- Anthropic's Claude
- Google's Gemini
- Other YAML-compatible AI systems

The structured YAML format ensures broad compatibility across different AI platforms and can be easily adapted for various use cases.