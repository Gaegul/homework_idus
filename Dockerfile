FROM python

ENV ENV PROD
ENV DATABASE_URL $DATABASE_URL
ENV JWT_SECRET_KEY $JWT_SECRET_KEY

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["-m", "homework"]
ENTRYPOINT ["python"]