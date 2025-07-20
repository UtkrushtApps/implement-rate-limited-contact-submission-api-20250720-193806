# Task Overview
You are maintaining a notification microservice built with FastAPI. Users can create notifications and retrieve them per user, but newly created notifications are not appearing when fetched, despite successful POST responses. The service uses an in-memory store for notifications, and you need to ensure notifications are immediately available after creation. The service must run within a Docker container.

# Guidance
- Review the existing implementation for any issues related to in-memory data persistence.
- Focus on how notifications are stored and accessed in the application's logic.
- Confirm that notifications for each user are consistently available after creation, without delay.
- Make sure that all endpoints behave as expected with regards to notification lifecycle.
- Ensure Dockerization is correct and production-like for a FastAPI microservice.

# Objectives
- Diagnose and fix the notification persistence issue so notifications created for a user are immediately available via the corresponding retrieval endpoint.
- Ensure in-memory storage logic properly supports creation and retrieval without data loss or delay.
- Maintain a production-like Docker setup for the FastAPI application.

# How to Verify
- Create a new notification through the POST endpoint and confirm it appears in the GET endpoint response for the same user immediately after.
- Validate this behavior for multiple users and multiple notifications per user.
- Confirm the service runs inside a Docker container and endpoints are accessible as expected.
