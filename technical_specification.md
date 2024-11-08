# Technical Specification

## 1. API Endpoints

This application has two API endpoints.

## 2. First API Endpoint

### 2.1 Description

This endpoint reads a config file to fetch all URLs, scrapes them using jina.ai, converts the data to embeddings, and stores them in Supabase. It returns a status message indicating successful creation of embeddings and the collection name.

### 2.2 Endpoint Details

- **HTTP Method:** POST
- **Path:** `/api/v1/create-embeddings`

### 2.3 Request

No request body is required as the endpoint reads from a config file.

### 2.4 Response

```json
{
  "status": "success",
  "message": "Embeddings created successfully",
  "collection_name": "string"
}
```

### 2.5 Process Flow

1. Read URLs from the config file
2. For each URL:
   a. Use jina.ai to scrape the content
   b. Convert the scraped content to embeddings using OpenAI's API
   c. Store the embeddings in Supabase
3. Return success status and collection name

### 2.6 Credentials

Supabase and OpenAI API keys are stored in the .env file.

## 3. Second API Endpoint

### 3.1 Description

This endpoint takes a natural language query as input, matches it to the previously created embeddings, and returns an appropriate answer as a response.

### 3.2 Endpoint Details

- **HTTP Method:** POST
- **Path:** `/api/v1/query`

### 3.3 Request

```json
{
  "query": "string"
}
```

### 3.4 Response

```json
{
  "answer": "string"
}
```

### 3.5 Process Flow

1. Receive the natural language query
2. Convert the query to an embedding using OpenAI's API
3. Match the query embedding against the stored embeddings in Supabase
4. Retrieve the most relevant content based on the embedding match
5. Generate an appropriate answer using the retrieved content
6. Return the answer as the response

## 4. Environment Setup

### 4.1 .env File

The following environment variables should be set in the .env file:

```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
OPENAI_API_KEY=your_openai_api_key
```

## 5. Dependencies

- jina.ai for web scraping
- OpenAI API for creating embeddings and generating responses
- Supabase for storing and querying embeddings

## 6. Error Handling

Both endpoints should implement proper error handling for scenarios such as:
- Failed web scraping
- API rate limiting
- Database connection issues
- Invalid input

Appropriate error messages and status codes should be returned in case of failures.

## 7. Security Considerations

- Ensure that the .env file is not committed to version control
- Implement rate limiting on the API endpoints to prevent abuse
- Validate and sanitize all input to prevent injection attacks

## 8. Performance Considerations

- Implement caching mechanisms to improve response times for frequent queries
- Consider batch processing for large numbers of URLs in the first endpoint
- Optimize database queries for efficient embedding matching

## 9. Testing

Develop a comprehensive test suite including:
- Unit tests for individual functions
- Integration tests for the API endpoints
- Load tests to ensure the system can handle expected traffic

## 10. Documentation

Provide detailed API documentation including:
- Endpoint descriptions
- Request and response formats
- Example usage
- Error codes and their meanings

