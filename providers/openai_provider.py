from providers.base import BaseProvider
import httpx


class OpenAIProvider(BaseProvider):

    async def generate(self, prompt: str):

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": self.model,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }

            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=payload
                )

            response.raise_for_status()
            data = response.json()

            content = data["choices"][0]["message"]["content"]

            if not content:
                raise Exception("Empty response from OpenAI")

            token_count = data.get("usage", {}).get("total_tokens")

            if token_count is None:
                token_count = len(prompt.split()) + len(content.split())

            return {
                "text": content,
                "tokens_used": token_count
            }

        except Exception as e:
            raise Exception(f"OpenAI Error: {str(e)}")
