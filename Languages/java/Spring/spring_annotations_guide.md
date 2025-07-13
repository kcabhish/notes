# Commonly Used Java Spring Annotations

| **Annotation**              | **Description**                                                                 | **Example**                                                                 |
|-----------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `@Component`               | Marks a class as a Spring-managed component.                                    | `@Component public class MyService {}`                                       |
| `@Service`                 | Specialized version of `@Component`, used for service layer classes.            | `@Service public class UserService {}`                                       |
| `@Repository`              | Specialized version of `@Component`, used for DAO classes.                      | `@Repository public class UserRepository {}`                                 |
| `@Controller`              | Marks a class as a Spring MVC controller.                                       | `@Controller public class HomeController {}`                                 |
| `@RestController`          | Combines `@Controller` and `@ResponseBody` for REST APIs.                       | `@RestController public class ApiController {}`                              |
| `@Autowired`               | Automatically injects dependencies by type.                                     | `@Autowired private UserService userService;`                                |
| `@Qualifier`               | Specifies the bean to inject when multiple candidates are available.            | `@Autowired @Qualifier("adminService") private UserService service;`         |
| `@Value`                   | Injects values from properties files.                                           | `@Value("${app.name}") private String appName;`                              |
| `@Configuration`           | Marks a class as a source of bean definitions.                                  | `@Configuration public class AppConfig {}`                                   |
| `@Bean`                    | Declares a Spring bean in a `@Configuration` class.                             | `@Bean public DataSource dataSource() { return new ...; }`                   |
| `@ComponentScan`           | Tells Spring which packages to scan for components.                             | `@ComponentScan("com.example.services")`                                     |
| `@PropertySource`          | Loads property files into the Spring Environment.                               | `@PropertySource("classpath:application.properties")`                        |
| `@Scope`                   | Specifies bean scope (e.g., singleton, prototype).                              | `@Scope("prototype")`                                                        |
| `@PostConstruct`           | Invokes a method after the bean is initialized.                                | `@PostConstruct public void init() {}`                                       |
| `@PreDestroy`              | Invokes a method before the bean is destroyed.                                 | `@PreDestroy public void cleanup() {}`                                       |
| `@RequestMapping`          | Maps HTTP requests to handler methods or classes.                               | `@RequestMapping("/users")`                                                  |
| `@GetMapping`              | Shortcut for `@RequestMapping(method = GET)`.                                   | `@GetMapping("/users") public List<User> getUsers() {}`                      |
| `@PostMapping`             | Shortcut for `@RequestMapping(method = POST)`.                                  | `@PostMapping("/users") public void addUser(@RequestBody User u) {}`        |
| `@PutMapping`              | Shortcut for `@RequestMapping(method = PUT)`.                                   | `@PutMapping("/users/{id}")`                                                 |
| `@DeleteMapping`           | Shortcut for `@RequestMapping(method = DELETE)`.                                | `@DeleteMapping("/users/{id}")`                                              |
| `@PathVariable`            | Binds method parameter to a URI template variable.                              | `@GetMapping("/users/{id}") public User getUser(@PathVariable int id) {}`    |
| `@RequestParam`            | Binds a query parameter to a method parameter.                                  | `@RequestParam String name`                                                  |
| `@RequestBody`             | Binds the HTTP request body to a method parameter.                              | `@PostMapping("/users") public void create(@RequestBody User user)`          |
| `@ResponseBody`            | Indicates return value should be bound to the web response body.                | `@ResponseBody public User getUser()`                                        |
| `@ResponseStatus`          | Marks a method to return a specific HTTP status.                                | `@ResponseStatus(HttpStatus.CREATED)`                                        |
| `@ExceptionHandler`        | Handles exceptions thrown by controller methods.                                | `@ExceptionHandler(RuntimeException.class)`                                  |
| `@ControllerAdvice`        | Global exception handling for controllers.                                      | `@ControllerAdvice public class GlobalHandler {}`                            |
| `@EnableAutoConfiguration` | Tells Spring Boot to automatically configure the application.                  | `@EnableAutoConfiguration`                                                   |
| `@SpringBootApplication`   | Combines `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan`.    | `@SpringBootApplication public class App {}`                                 |
| `@EnableScheduling`        | Enables Spring's scheduled task execution capability.                          | `@EnableScheduling`                                                          |
| `@Scheduled`               | Marks a method to be executed on a schedule.                                    | `@Scheduled(fixedRate = 5000)`                                               |
| `@EnableCaching`           | Enables annotation-driven cache management.                                     | `@EnableCaching`                                                             |
| `@Cacheable`               | Indicates method result should be cached.                                       | `@Cacheable("users") public User getUser(Long id)`                           |
| `@Transactional`           | Declares a transaction boundary.                                                | `@Transactional public void transferMoney(...)`                              |

---

Feel free to copy, extend, or export this as needed!

