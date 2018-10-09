FROM python
ENV FLASK_APP=app.py \
  FLASK_ENV=development \
  FLASK_DEBUG=1 \
  FLASK_RUN_PORT=5000
COPY . .
RUN pip install -r requirements.txt
CMD flask run