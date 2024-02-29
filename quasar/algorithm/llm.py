from transformers import AutoTokenizer, AutoModelForCausalLM


class LLM:
    def __init__(self, model_name: str = "google/gemma-2b") -> None:
        """
        Initializes an instance of the LLM class.

        Args:
            model_name (str, optional): The name or path of the pre-trained language model. Defaults to "google/gemma-2b".
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate(self, input_text: str, max_length: int, **kwargs) -> str:
        """
        Generates text based on the given input text.

        Args:
            input_text (str): The input text to generate text from.
            max_length (int): The maximum length of the generated text.
            **kwargs: Additional keyword arguments to be passed to the model.generate() method.

        Returns:
            str: The generated text.
        """
        input_ids = self.tokenizer(
            input_text, return_tensors="pt", max_length=max_length, kwargs=kwargs)
        outputs = self.model.generate(**input_ids)
        return self.tokenizer.decode(outputs[0])
