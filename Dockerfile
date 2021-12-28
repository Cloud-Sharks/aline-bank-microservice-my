FROM openjdk:8-jdk-alpine
COPY ./bank-microservice/target/bank-microservice-0.1.0.jar app.jar
ENV APP_PORT 8083
ENTRYPOINT ["java", "-jar", "/app.jar"]