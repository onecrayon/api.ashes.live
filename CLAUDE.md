# CLAUDE.md - AI Assistant Configuration for Ashes.live API

## Project Overview
This is the backend API for Ashes.live, a fan-developed deckbuilder and community website for the card game Ashes Reborn. The project is built using FastAPI, SQLAlchemy, and PostgreSQL, following the Three Musketeers pattern (Docker + Docker Compose + Make).

## Architecture Patterns

### Three Musketeers Development
- **Make**: Simple interface for complex Docker operations
- **Docker**: Containerized development environment  
- **Docker Compose**: Multi-service orchestration
- All development tasks execute inside containers via Make commands

### Code Organization
- `api/views/`: FastAPI route handlers (controllers)
- `api/services/`: Business logic and complex operations
- `api/models/`: SQLAlchemy ORM models
- `api/schemas/`: Pydantic models for input/output validation
- `api/utils/`: Utility functions and helpers
- `api/tests/`: Integration and unit tests

### Database
- PostgreSQL with SQLAlchemy ORM
- Alembic for schema migrations
- UUID primary keys, full-text search capabilities

## Development Commands

### Essential Make Commands
- `make help` - Show all available commands
- `make up` - Start development server (http://localhost:8000)
- `make test` - Run test suite with coverage
- `make format` - Format code with black and isort
- `make migrate` - Run database migrations
- `make shell` - Open bash shell in API container
- `make shell-db` - Open bash shell with database running
- `make clean` - Clean up Docker containers and images

### Testing
- `make test` - Full test suite with coverage report
- `make test ARGS='api/tests/cards'` - Run specific test directory
- `make test ARGS='api/tests/cards/test_card_create.py::test_create_card_require_name` - Run one specific test
- Coverage report generated at `htmlcov/index.html`

### Database Operations  
- `make migrate` - Run migrations to head
- `make migrate REV='revision'` - Migrate to specific revision
- `make db` - Start standalone PostgreSQL server

## Code Style Guidelines

### Formatting
- **Black** for code formatting (line length: 88)
- **isort** for import organization (black profile)
- Run `make format` or `make format FILEPATH='api/main.py'` for specific files

### Testing Requirements
- Target 100% code coverage
- Integration tests preferred (test actual endpoints)
- Unit tests for complex business logic where integration testing isn't feasible
- Each test runs against clean database state

## Development Workflow

### Adding New Features
1. Create/update models in `api/models/`
2. Generate migration: `make migrate-new ARGS='DESCRIPTION HERE'`
3. Ask user to verify the migration file so they can make any necessary edits
4. Implement shared business logic in `api/services/`, if any, but for singleton logic keep it in the view code
5. Create Pydantic schemas in `api/schemas/`
6. Add route handlers in `api/views/`
7. Write comprehensive tests in `api/tests/`
8. Format code: `make format`
9. Verify tests pass: `make test`

### Adding Dependencies
1. Add the dependency to poetry: `make poetry-add ARGS='PACKAGE_NAME'`
2. Rebuild the container: `make build`

### Database Migrations
1. Create the migration: `make migrate-new ARGS='DESCRIPTION HERE'`
2. Review generated migration file to ensure no unexpected changes
3. Execute the migration: `make migrate`

## AI Assistant Guidelines

### When Working on This Codebase:
1. **Always use Make commands** - Never run Docker/compose commands directly
2. **NEVER use local imports** - Always add imports to the tops of files, unless explicitly told otherwise
3. **Follow the clean architecture** - Views → Services → Models
4. **Write tests** - Integration tests for endpoints, unit tests for complex logic
5. **Format code** - Automatically format changed files after major edits. **NEVER** summarize formatting changes when it succeeds (at most simply report success)
6. **Use existing patterns** - Study existing code before implementing new features

### Before Making Changes:
- Understand the feature requirements
- Check existing similar implementations
- Consider impact on related models/services
- Plan test strategy (integration vs unit tests)

### After Making Changes:
- Format code: `make format`
- Run tests: `make test`

### Common Patterns:
- Route dependencies in `api/depends.py`
- Pagination via `api/utils/pagination.py`
- Authentication via JWT tokens
- Error handling with custom exceptions
- Input validation with Pydantic schemas

## API Documentation
- Main docs: http://localhost:8000 (after running `make up`)
