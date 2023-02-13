FROM python:3.9.16-slim
LABEL maintainer="Toggle <deploy@toggle.ai>"

ENV SERVICE_NAME insight-accuracy
ENV PYTHONUNBUFFERED 1

# CREATE UNPRIVILEGED USER AND SET PERMISSIONS
RUN groupadd -g 10001 appuser && \
    useradd  -m -u 10001 -s /bin/bash -g appuser appuser

RUN mkdir -p /src/app; exit 0
COPY --chown=appuser:appuser . /src/app/
WORKDIR /src/app

USER appuser
RUN pip install -r requirements.txt

# LIGHT IT UP
CMD ["python", "runner.py"]