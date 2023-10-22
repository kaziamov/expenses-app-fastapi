FROM python:3.11.2

WORKDIR /app
COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["uvicorn", "expenses_app:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80