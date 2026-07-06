# Responsible AI on AWS

## AWS AI Authentication Patterns

User -> Cognito/IAM -> AI Application

## Service Authentication

AI Application -> IAM Role -> Model Endpoint
 * Token Validation -> * Policy Enforcement -> * Model Access Check

 ## Data Access Authentication (RAG)

 AI Model -> Vector Store -> Source Data
 * Query Auth -> * Data Access Control -> * Source Validation