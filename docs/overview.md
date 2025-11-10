# Project Overview

This project is a Mood-Based Recipe Recommendation application. The codebase implements MVP and post-MVP features based on Jira issues SCRUM-223 to SCRUM-232.

## MVP Features (SCRUM-223 to SCRUM-227)

- **SCRUM-223: Architecture**
  - React SPA frontend
  - REST API backend
  - Mood analysis and recipe recommendation flow
  - Stateless, scalable components

- **SCRUM-224: Data Models**
  - Entities: User (anonymous), Mood, Recipe, Feedback
  - Well-defined attributes and relations

- **SCRUM-225: API Endpoints**
  - POST /api/mood
  - GET /api/recipes/{id}
  - POST /api/feedback

- **SCRUM-226: Security**
  - HTTPS enforcement
  - Encrypted data storage
  - GDPR compliance foundations

- **SCRUM-227: Performance & Scalability**
  - Stateless backend with horizontal scaling
  - Database indexing and caching
  - CDN for frontend assets

## Post-MVP Features (SCRUM-228 to SCRUM-232)

- **SCRUM-228: User Profiles & Authentication**
  - User registration, login
  - Favorites and preferences management
  - Secure endpoints for user data

- **SCRUM-229: Advanced Mood Detection**
  - Sentiment analysis microservice
  - NLP support for textual mood input

- **SCRUM-230: User Favorites & Preferences Support**
  - Frontend and backend support for favorites
  - Personalized recipe recommendations

- **SCRUM-231: Social Sharing & Grocery Integration**
  - Social feed for recipes and comments
  - Integration with grocery APIs

- **SCRUM-232: AI-Powered Personalization**
  - ML-based recommendation engine
  - Infrastructure for training, serving, feedback loops

This roadmap and specification have been derived from Jira issues as the basis for implementation.