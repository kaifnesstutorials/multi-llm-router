class BaseProvider:

    def __init__(self, config: dict):
        self.name = config.get("name")
        self.base_url = config.get("base_url")
        self.model = config.get("model")
        self.api_key = config.get("api_key", None)
        self.cost_per_1k_tokens = config.get("cost_per_1k_tokens", 0.0)
        self.timeout = config.get("timeout", 30)

    async def generate(self, prompt: str):
        raise NotImplementedError("Each provider must implement generate()")
