FROM openjdk:8u312-jre-slim-buster
COPY ./bank-microservice/target/bank-microservice-0.1.0.jar app.jar
ENV APP_PORT 8083
ENTRYPOINT ["java", "-jar", "/app.jar"]