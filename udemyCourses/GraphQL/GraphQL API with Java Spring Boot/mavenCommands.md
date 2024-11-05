| Command | Description |
|--------|-------------|
| `mvn clean install` | Cleans the project and installs dependencies, compiling and packaging the code into a local `.jar` or `.war`. |
| `mvn clean` | Removes the `target` directory (clean build artifacts). |
| `mvn install` | Compiles, tests, and installs the package into the local repository. |
| `mvn package` | Compiles the code and packages it into a `.jar` or `.war` file. |
| `mvn compile` | Compiles the source code of the project. |
| `mvn test` | Runs the tests defined in the project. |
| `mvn dependency:tree` | Displays the dependency tree for the project. |
| `mvn validate` | Validates the project structure and checks for necessary information. |
| `mvn verify` | Runs any checks to verify the project is valid and meets quality criteria. |
| `mvn site` | Generates the project's site documentation. |
| `mvn exec:java -Dexec.mainClass="com.example.Main"` | Executes a Java class with a `main` method. |
| `mvn help:effective-pom` | Displays the effective POM after inheritance and interpolation. |
| `mvn versions:display-dependency-updates` | Lists newer versions of the dependencies. |
| `mvn dependency:analyze` | Analyzes declared but unused dependencies and used but undeclared dependencies. |
| `mvn help:describe -Dcmd=clean` | Shows detailed information about the `clean` command. |
