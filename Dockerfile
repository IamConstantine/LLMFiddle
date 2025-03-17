FROM python:3.14-rc-alpine
LABEL authors="IamConstantine"

ENV ANTHROPIC_API_KEY ''
RUN pip install
ENTRYPOINT [“python”, “./main.py”]