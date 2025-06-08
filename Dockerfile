FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -m pip install spacy
RUN python -m spacy download en_core_web_lg

COPY anno.py .

CMD ["anno.lambda_handler"]