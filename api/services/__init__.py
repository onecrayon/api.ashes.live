"""api.services

Services are functions that perform more involved logic that affects multiple models, or otherwise
requires a connection to the database. If a bit of "business logic" is shared by multiple endpoints
it should probably be a service (otherwise, default to leaving logic in the views where it's more
easily discoverable).
"""
