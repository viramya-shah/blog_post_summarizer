# Blog Post Summarization

The repo provides a clean and simple UI for summarization and acts a personal knowledge base. 

## Functionalities:
- You can get quick summaries of various blog posts. Simply copy paste the link in the input box on `Get Summary` page..
- The system generates 2 types of summaries - short and long. Irrespective of the type, all the summaries are stored in a local DB. 
- You can view all the summaries in the `View History` tab. This acts like your personal knowledge base. 
- You can also search for concepts, ideas that you might have read and logged in the system. You can do this using the `Search` page. (this is work in progress)

## How to run?
1. Clone the repo
2. Setp `OPENAI_API_KEY` as your enviornment variable.
3. Run `docker-compose -f run.yaml up`

## Next Steps
1. Replace closed-source model(s) with open-sourced models.
2. Add chat functionality along with search to enhance the experience.
3. Add support for other file formats like videos, podcasts, research papers. 