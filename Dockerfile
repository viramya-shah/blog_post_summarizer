FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install uv
RUN uv pip install -r requirements.txt --system
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "/app/src/app/home_page.py"]x