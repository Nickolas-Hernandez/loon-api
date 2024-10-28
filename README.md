# Loon API

A RESTful API for retrieving moon phase and related data for the Loon mobile app.

## Overview

This API provides moon phase, visibility, and illumination data for specified dates, used by the Loon mobile app.

## Tech Stack

- **Ruby**
- **Sinatra**
- **JWT** (for authentication)
- **Net::HTTP** (for third-party API requests)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/loon-api.git
   cd loon-api
   ```

## Setup

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Set environment variables (e.g., API token, JWT secret):

   ```bash
   export THIRD_PARTY_API_TOKEN="your_api_token"
   export JWT_SECRET="your_jwt_secret"
   ```

4. Start the server:

   ```bash
   ruby app.rb
   ```

## API Endpoints

- **GET** `/moon-phase/:date` - Retrieves moon phase data for a specified date.​⬤

## Authentication

- Uses **JWT** for secure access. Pass the token in the `Authorization` header:

## Example Request

```bash
curl -X GET "http://localhost:8080/moon-phase/2024-10-27" -H "Authorization: Bearer <your_jwt_token>"
```

## To Do

- [ ] Add additional endpoints
- [ ] Implement refresh tokens
- [ ] Expand error handling

---

*This README is a work in progress and will be updated as the project evolves.*

