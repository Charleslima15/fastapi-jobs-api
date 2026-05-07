# Job Listings REST API

A production-ready REST API for a job listings platform built with FastAPI, PostgreSQL, and SQLAlchemy. Supports two user roles — job seekers and recruiters — with JWT authentication and role-based access control.

## Features

- JWT authentication with bcrypt password hashing
- Role-based access control (seeker vs recruiter)
- Job posting, searching, and filtering with pagination
- Application lifecycle management with duplicate prevention
- Auto-generated interactive API docs via Swagger UI

## Tech Stack

- **FastAPI** — web framework
- **PostgreSQL** — database
- **SQLAlchemy** — ORM
- **Alembic** — database migrations
- **Pydantic** — data validation
- **python-jose** — JWT tokens
- **passlib** — password hashing

## Project Structure

## Data Models

- **User** — single table with seeker/recruiter roles
- **Company** — recruiters belong to a company
- **Job** — belongs to a company, has status lifecycle
- **Application** — links seeker to job, unique constraint prevents duplicate applications



