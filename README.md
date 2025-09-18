# monash-handbook-dataset-api
Handbook containing monash handbook data for 2025

# Monash Handbook Dataset API

This is a simple REST API that serves Monash University unit data.
It is built with Flask and hosted on Render.

## Endpoints
- `/units` → list all units or search by query (e.g., `?q=fit`)
- `/units/<code>` → get details of a specific unit (e.g., `/units/FIT3175`)
- `/health` → health check

## Example

