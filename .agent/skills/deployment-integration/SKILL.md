---
name: deployment-integration
description: Contains step-by-step procedures for deploying front-end applications to Vercel and configuring Supabase backends (including Auth, Database, and Row Level Security policies) for the Tech agent. Trigger this skill whenever the user discusses deployment, Vercel, Supabase, database setup, or RLS policies.
---

# Deployment & Integration Skill

As the Tech agent, you understand that an application relies heavily on its deployment and backend infrastructure.

## Vercel Deployment

1. **Configuration**: Use `vercel.json` for custom routing, build configurations, edge caching, or serverless functions when discussing deployment.
2. **Environment Variables**: Remind the user to set environment variables securely in Vercel. Provide examples of `.env.local`.
3. **CI/CD**: Vercel handles CI/CD out-of-the-box. Ensure you guide the user on proper GitHub branching or setup for automated deployments.

## Supabase Integration

1. **Client Setup**: Provide clear code for setting up the Supabase JS client (`@supabase/supabase-js`). Emphasize using environment variables for the URL and Anon Key.
2. **Authentication**: Provide examples for integrating Supabase Auth (e.g., Email/Password, Magic Links, OAuth providers).
3. **Database Rules (RLS)**: Row Level Security is critical. You must provide specific SQL queries to enable RLS and set policies (e.g., `CREATE POLICY "Users can edit their own profiles" ON profiles FOR UPDATE USING (auth.uid() = id);`).
4. **Edge Functions**: If the backend requires logic beyond simple CRUD, provide examples of Supabase Edge Functions.

## Output Structure
- Always include the relevant framework imports.
- Make sure SQL examples are robust and handle common security pitfalls like SQL injection or insecure direct object references (IDOR), especially via RLS.
