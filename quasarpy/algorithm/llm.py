from transformers import AutoTokenizer, AutoModelForCausalLM
from quasarpy.utils.logger import logger
from dataclasses import dataclass
import huggingface_hub 
import os
from dotenv import load_dotenv


@dataclass
class LLMConfig:
    model_name: str = "google/gemma-2b"
    max_new_tokens: int = 100


# Load the API token from the .env file
load_dotenv()


class LLM:
    logger = logger

    def __init__(self, model_config: LLMConfig, is_online: bool = True) -> None:
        """
        Initializes an instance of the LLM class.

        Args:
            model_name (str, optional): The name or path of the pre-trained language model. Defaults to "google/gemma-2b".
        """

        self.is_online = is_online
        self.model_config = model_config
        self.logger.info(
            f"LLM class initialized with model {model_config.model_name} and is_online set to {is_online}."
        )
        if not is_online:
            self.tokenizer = AutoTokenizer.from_pretrained(model_config.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_config.model_name)

    def _generate_online(self, prompt: str, **kwargs) -> str:
        try:
            client = huggingface_hub.InferenceClient(token=os.getenv("HUGGINGFACE_TOKEN"))
            response = client.text_generation(
                prompt=prompt,
                model="mistralai/Mistral-7B-Instruct-v0.2",
                max_new_tokens=self.model_config.max_new_tokens,
                **kwargs
            )
            return response
        except huggingface_hub.hf_api.HTTPError as e:
            self.logger.error(f"An error occurred while generating text: {str(e)}")
            raise

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generates text based on the given input text.

        Args:
            prompt (str): The input text to generate text from.
            max_length (int): The maximum length of the generated text.
            **kwargs: Additional keyword arguments to be passed to the model.generate() method.

        Returns:
            str: The generated text.
        """
        if not self.is_online:
            input_ids = self.tokenizer(
                prompt,
                return_tensors="pt",
                max_new_tokens=self.model_config.max_new_tokens,
                **kwargs,
            )
            outputs = self.model.generate(**input_ids)
            return self.tokenizer.decode(outputs[0])
        else:
            return self._generate_online(prompt, **kwargs)

