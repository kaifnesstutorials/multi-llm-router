import time
import asyncio
from utils.logger import log_usage


class LLMRouter:
    def __init__(self, providers):
        self.providers = providers

    async def route(self, prompt: str):

        last_error = None

        for provider in self.providers:

            for attempt in range(2):
                try:
                    start = time.time()

                    result = await asyncio.wait_for(
                        provider.generate(prompt),
                        timeout=provider.timeout
                    )

                    latency = time.time() - start
                    tokens = result["tokens_used"]
                    cost = (tokens / 1000) * provider.cost_per_1k_tokens

                    result_data = {
                        "provider": provider.name,
                        "modelUsed": provider.model,
                        "tokens": tokens,
                        "cost": round(cost, 6),
                        "latency": round(latency, 3),
                        "response": result["text"],
                        "status": "success"
                    }

                    log_usage(result_data)
                    return result_data

                except Exception as e:
                    print(f"\nProvider Failed: {provider.name}")
                    print(f"Reason: {str(e)}\n")

                    last_error = str(e)

                    if attempt == 1:
                        log_usage({
                            "provider": provider.name,
                            "status": "failed",
                            "reason": last_error
                        })

                    await asyncio.sleep(0.5)

        raise Exception(f"All providers failed: {last_error}")
