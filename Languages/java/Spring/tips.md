# Enable logging for springframework

in `src/main/java/resources/application.properties` add the folloing:

```JAVA
spring.application.name=spring-in-5-steps // app name by default
logging.level.org.springframework = debug; // add this line
```

This is a handy way to debug and check the beans registered for the spring boot

---

