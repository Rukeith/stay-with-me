FROM python
ENV FLASK_APP=app.py \
  FLASK_ENV=development \
  FLASK_DEBUG=1
COPY . .
RUN pip install Flask flask_sqlalchemy PyMySQL raven[flask]
CMD flask run