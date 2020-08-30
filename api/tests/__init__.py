"""Integration testing module

Please note that the testing strategy for this project is currently focused on using the
simplest possible integration tests to obtain full code coverage. This generally means
that an individual test will have three responsibilities:

1. Setup an example environment (e.g. create necessary fake data for querying, typically
   via the testing API client)
2. Query the API endpoint we are testing
3. Verify the status code to ensure that permissions, success, and failure states are as
   expected

I am hoping to implement property based testing to ensure that the API fulfills the promises
the OpenAPI spec makes, but that's a pretty complicated problem, so I'm waiting until we are
closer to the API being an officially published spec consumed by external parties.
"""
