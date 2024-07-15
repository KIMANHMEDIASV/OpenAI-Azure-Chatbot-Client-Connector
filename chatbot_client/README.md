# Chatbot Client Library

## Overview
This library serves as the backend infrastructure for a chatbot client, providing a comprehensive set of API endpoints to manage various aspects of the chatbot's functionality. This includes admin settings, bot operations, chat interactions, user management, system status, and statistical tracking. It ensures a robust and scalable framework for handling chatbot services, making it easier to build, deploy, and maintain an intelligent chatbot application.

## Admin Endpoints
These endpoints manage OpenAI service configurations:

- **GET /api/admin/openAiServices**: Retrieves a list of all OpenAI services.
- **POST /api/admin/openAiServices**: Creates a new OpenAI service.
- **GET /api/admin/openAiServices/{openAiServiceId}**: Retrieves a specific OpenAI service by ID.
- **PUT /api/admin/openAiServices/{openAiServiceId}**: Updates an existing OpenAI service by ID.
- **DELETE /api/admin/openAiService/{openAiServiceId}**: Deletes a specific OpenAi service by ID.

## Bot Endpoints
These endpoints manage chatbot instances and operations:

- **POST /api/bots/{botId}/search**: Initiates a search operation for a specific bot.
- **GET /api/bots**: Retrieves a list of all bots.
- **GET /api/bots/bystartbot/{startBotId}**: Retrieves bots by a specific start bot ID.
- **GET /api/bots/startbots**: Retrieves all start bots.
- **GET /api/bots/botimage/{botId}**: Retrieves the image of a specific bot.
- **GET /api/bots/stop**: Stops all running bots.

## Cache Endpoints
These endpoints manage caching functionalities:

- **DELETE /cache**: Clears the cache.

## Chat Endpoints
These endpoints handle chat interactions and session management:

- **POST /api/chats**: Creates a new chat session.
- **POST /api/chats/create/bybotcode**: Creates a chat session by bot code.
- **POST /api/chats/{chatId}/completions**: Adds a completion to a specific chat.
- **GET /api/chats/{chatId}**: Retrieves details of a specific chat by ID.
- **DELETE /api/chats/{chatId}**: Deletes a specific chat by ID.
- **POST /api/chats/{chatId}/feedback**: Submits feedback for a specific chat.
- **GET /api/chats/OpenChatBotId**: Retrieves the ID of an open chat bot.
- **PUT /api/chats/{chatId}/displayName**: Updates the display name of a chat.
- **PUT /api/chats/{chatId}/userSystemMessage**: Adds or updates a user system message in a chat.
- **DELETE /api/chats/{chatId}/userSystemMessage**: Deletes a user system message in a chat.
- **POST /api/chats/{chatId}/tickets**: Creates a ticket for a specific chat.
- **GET /api/chats/{chatId}/downloads/{path}**: Downloads data from a specific chat.

## Statistic Endpoints
These endpoints manage and retrieve statistics:

- **PUT /api/statistic**: Updates statistics.
- **GET /api/statistic/tokenUsageStatistic**: Retrieves token usage statistics.

## System Endpoints
These endpoints handle system-level functionalities:

- **GET /api/System/status/current**: Retrieves the current system status.
- **PUT /api/System/status/current**: Updates the current system status.

## User Endpoints
These endpoints manage user data and operations:

- **GET /api/users/current**: Retrieves the current user details.
- **PUT /api/users/current**: Updates the current user details.
- **PUT /api/users/current/acceptTerms**: Updates the user's acceptance of terms.
- **DELETE /api/users/current/chats/all/{keepfavorites}**: Deletes all chats of the current user, with an option to keep favorites.
- **DELETE /api/users/current/chats/byid/{chatid}**: Deletes a specific chat by ID.
- **DELETE /api/users/current/chats/{chatid}/completion/{completionid}**: Deletes a specific completion from a chat.
- **DELETE /api/users/current/chats/bybot/{botid}/{keepfavorites}**: Deletes chats by bot ID, with an option to keep favorites.
- **DELETE /api/users/current/chats/bybot/{botid}/{systemmessageid}/{keepfavorites}**: Deletes chats by bot and system message ID, with an option to keep favorites.
- **GET /api/users/current/chats/{botid}**: Retrieves chats for a specific bot.
- **GET /api/users/current/chats/{botid}/{usersystempromptid}**: Retrieves chats by bot and user system prompt ID.
- **GET /api/users/current/chats**: Retrieves all chats for the current user.
- **PUT /api/users/current/chats/{chatid}/isfavorite**: Marks a chat as a favorite.
- **GET /api/users/current/userSystemMessage**: Retrieves all user system messages.
- **POST /api/users/current/userSystemMessage**: Creates a new user system message.
- **GET /api/users/current/userSystemMessage/{userSystemMessageId}**: Retrieves a specific user system message by ID.
- **PUT /api/users/current/userSystemMessage/{userSystemMessageId}**: Updates a specific user system message by ID.
- **DELETE /api/users/current/userSystemMessage/{userSystemMessageId}**: Deletes a specific user system message by ID.
- **GET /api/users/current/userSystemMessageCount**: Retrieves the count of user system messages.

## Core Modules
These core modules provide essential functionality for the library:

- **client.py**: This is the entry point for the chatbot client, initializing the application and handling the main workflow, including API request routing and response handling.
- **exceptions.py**: Defines custom exceptions used throughout the library, providing a structured way to handle errors and exceptional cases.
- **models.py**: Contains the data models for the application, defining the structure of data objects such as user data, chat logs, and bot configurations.
- **utils.py**: A collection of utility functions and helpers used across the library to support various common tasks and operations, enhancing code reusability and maintainability.
