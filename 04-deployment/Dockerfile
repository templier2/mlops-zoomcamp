FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip && pip install pipenv && addgroup --system appuser && \
                                                adduser --system --ingroup appuser appuser

COPY ["Pipfile", "Pipfile.lock", "/app"]

RUN pipenv install --system

COPY starter.py /app

RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["python", "starter.py"]

CMD ["2023", "4"]