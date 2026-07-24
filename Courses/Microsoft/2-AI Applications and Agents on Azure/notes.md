# Azure

Azure provides four categories of services

- Compute: The ability to run applications, programs, and workloads in the cloud. You can think of compute as renting computers in the cloud that you can scale up or down whenever you need.

- Storage: Servicevs that let you save and manage data in the cloud. Storate can include files, databases, images, backups.

- Networking: Tools that connect your cloud resources to each other, to the internet, or to your organization.

- App Services: Ready- made platforms for buildin, hosting, andrunning applications without managing the underlying servers.


## Azure Organizational Structure

- Tenant
- Subscription
- Resrouce Group
- Resrouces

## Hosting and Scaling

### Host
Applications run on computers or environments known as a host. In cloud contexts, a host can be a virtual machine (VM) providing the compute, memory and networking the application needs to execute.

### Scaling
Scaling your applications means to automtically or manually adjust the amount ofcompute power your app uses. Usually by adding or removing instances.

There are two types of Scaling:
- Horizontal : Add more instances
- Vertical : Increase CPU/memory on the existing instance

# Microsoft Foundry

It is a unified, enterprise-grade platform-as-a-service(PaaS) for building, andeploying and managing AI applications and agents. Foundry offers powerful capabilities for developers, including the ability to choose from a wide range of models, use those models to build agents, connect those agets to tools and integrate knowledge by using Foundry IQ, the centralized connectio point for data source.

- Models : Foundry supports thousands of model
- Agents : agent-first approach lets developers build intelligent within the foundry.
- Tools : provides speech, vision, language, document intelligence and more that can be built into web or mobile apps.
- Knowledge : Foundry IQ provides a permisson-aware multi-source knowledge layer that gives agents accurate grounded answers using an organization's own data.

# Using Microsoft Foundry Endpoints

Below is the sample of an endpoint:

```
https://<foundry-project>-resource.cognitiveservices.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-05-01-preview
```
## Two common types of endpoints in Foundry include:

Project-level endpoints: for working with your Foundry project and its resources
Model endpoints: for sending prompts to deployed models

# Create Microsoft Foundry Project

1. In a web browser, open [Microsoft Foundry](https://ai.azure.com) at  to start building.
1. If it isn’t already enabled, in the tool bar the top of the page, enable the New Foundry option.

Additional information can be found in [here](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Exercises/00-explore-foundry.html)
