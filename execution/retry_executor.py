from execution.retry_policy import RetryPolicy


class RetryExecutor:
    @staticmethod
    def execute(function, payload, state, node_name):

        policy = RetryPolicy()

        attempts = 0

        while attempts < (policy.max_retries):
            try:
                return function(payload)

            except Exception as error:
                attempts += 1

                state.increment_retry(node_name)

                state.add_error(node_name, error)

        raise RuntimeError(f"Node '{node_name}' exceeded retry limit")
