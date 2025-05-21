FROM python:3.13-slim
WORKDIR /backend
COPY backend ./
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
# RUN python db_modules/tables_creator.py
# RUN python orm_models/test_data_loader.py
ENTRYPOINT ["uvicorn", "fast_main:app", "--host", "0.0.0.0", "--reload"]