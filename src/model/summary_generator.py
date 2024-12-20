import pandas as pd
from openai import OpenAI
from .data_model import Document, ShortSummaryDataModel, LongSummaryDataModel

class Summary:
    def __init__(self, client: OpenAI, prompts: dict):
        """
        Init with necessary attributes
        """
        self.client = client
        self.prompts = prompts

    def _generate_summary(self, text_to_summarize: str, type: str = 'short'):
        """
        Internal function to generate a particular kind of summary
        :param text_to_summarize: str-like object that needs to be summarized
        :param type: Whether to create a short or a long summary. Possible values: [short, long]
        """
        match type:
            case 'short':
                completion = self.client.beta.chat.completions.parse(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": self.prompts['SYSTEM_PROMPT']['SHORT_SUMMARY']},
                        {"role": "user", "content": f"Summarize this text: {text_to_summarize}"},
                    ],
                    store=False,
                    response_format=ShortSummaryDataModel
                )
            
            case 'long':
                completion = self.client.beta.chat.completions.parse(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": self.prompts['SYSTEM_PROMPT']['LONG_SUMMARY']},
                        {"role": "user", "content": f"Summarize this text: {text_to_summarize}"},
                    ],
                    store=False,
                    response_format=LongSummaryDataModel
                )

        return completion.choices[0].message.parsed.summary, completion.choices[0].message.parsed.title 
    
    def _save(self, docs: list[Document]):
        """
        Maintains a CSV file with all the generated summaries
        :param docs: List of Document-like object
        """
        file_path = './data/master_summaries.csv'

        try:
            df = pd.read_csv(file_path)
            print("CSV loaded successfully.")
        except FileNotFoundError:
            print("CSV file not found. Creating a new one.")
            df = pd.DataFrame() 

        new_df = pd.DataFrame(list(map(lambda x: x.__dict__, docs)))

        df = pd.concat([df, new_df], ignore_index=True)

        df.to_csv(file_path, index=False)
        print(f"CSV updated and saved to {file_path}.")
    
    def generate_summary(self, documents: list[Document]) -> list[Document]:
        """
        Main function to generate summary
        :param documents: list of Document-like objects
        :return: A list of Document-like object
        """
        res = []
        for docs in documents:
            
            docs.short_summary, docs.title = self._generate_summary(text_to_summarize=docs.content, type='short')
            docs.long_summary, _ = self._generate_summary(text_to_summarize=docs.content, type='long')

            res.append(docs)
        self._save(res)
        return res