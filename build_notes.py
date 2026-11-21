from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER

OUT = "subject-notes.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverX", parent=styles["Title"], fontSize=21, leading=27, alignment=TA_CENTER, textColor=colors.HexColor("#173B63"), spaceAfter=12))
styles.add(ParagraphStyle(name="H1X", parent=styles["Heading1"], fontSize=16, leading=20, textColor=colors.HexColor("#173B63"), spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontSize=11, leading=14, textColor=colors.HexColor("#8A6818"), spaceBefore=7, spaceAfter=4))
styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontSize=8.8, leading=12, spaceAfter=4))
styles.add(ParagraphStyle(name="SmallX", parent=styles["BodyText"], fontSize=8, leading=11, spaceAfter=3))

data = [
("1. Numerical Methods", [
("Unit I — Numerical solutions of algebraic and transcendental equations", [
"Bisection method: choose [a,b] with f(a)f(b)<0; compute c=(a+b)/2 and retain the half interval containing the sign change. It is reliable when the continuity and bracketing conditions hold.",
"Regula-Falsi (false position): c=(a f(b)-b f(a))/(f(b)-f(a)); replace the endpoint having the same sign as f(c). It maintains a bracket but may converge slowly.",
"Newton–Raphson: x(n+1)=x(n)-f(xn)/f'(xn). It is usually fast near a simple root, but depends on a suitable starting value and non-zero derivative.",
"Secant method: x(n+1)=x(n)-f(xn)(xn-x(n-1))/(f(xn)-f(x(n-1))). It estimates the derivative from two previous points.",
"Muller’s method fits a quadratic through three points and uses a root of that quadratic as the next approximation. It can also find complex roots."
]),
("Unit II — Numerical solutions of simultaneous linear equations", [
"Gauss elimination: use elementary row operations to form an upper-triangular system, then solve by back-substitution.",
"Gauss–Jordan: continue elimination above and below each pivot until the coefficient matrix is reduced; read the solution directly when the system is nonsingular.",
"Crout triangularisation: factor A=LU, with L lower triangular and U upper triangular (unit diagonal convention for U); solve Ly=b and Ux=y.",
"Jacobi iteration computes every new variable using only values from the previous iteration. Gauss–Seidel immediately uses newly computed values within the same iteration.",
"Successive Over-Relaxation (SOR) modifies Gauss–Seidel updates using a relaxation parameter omega. Convergence depends on the matrix and the selected parameter."
]),
("Unit III — Interpolation with equal and unequal intervals", [
"Finite differences: forward differences are useful near the beginning of equally spaced data; backward differences are useful near the end.",
"Newton forward formula: y=y0+u Δy0+u(u−1)Δ²y0/2!+… where u=(x−x0)/h.",
"Newton backward formula uses backward differences and u=(x−xn)/h.",
"Central-difference formulae are used near the middle of a table. Stirling’s formula is suited to an even number of intervals around the central value; Bessel’s formula is useful near the midpoint between two central values.",
"Lagrange interpolation: P(x)=Σ yi Π(j≠i)(x−xj)/(xi−xj). It works for unequal intervals.",
"Newton divided differences construct an interpolation polynomial for unequal x-values using a divided-difference table."
]),
("Unit IV — Numerical differentiation and integration", [
"Numerical differentiation estimates derivatives from tabulated values using forward, backward or central difference formulae according to the location in the table.",
"Newton–Cotes quadrature approximates an integral by integrating an interpolating polynomial through equally spaced data.",
"Composite trapezoidal rule: integral ≈ h/2 [y0+yn+2Σ(interior y)].",
"Simpson’s 1/3 rule: h/3 [y0+yn+4Σ(odd-index ordinates)+2Σ(even interior ordinates)]; it requires an even number of subintervals.",
"Simpson’s 3/8 rule applies when the number of subintervals is a multiple of three. Weddle’s rule uses seven ordinates over six equal subintervals."
]),
("Unit V — Numerical solution of ordinary differential equations", [
"Picard’s method converts the initial-value problem to an integral equation and obtains successive approximations.",
"Taylor-series method expands y(x+h) using derivatives evaluated from the differential equation.",
"Euler method: y(n+1)=yn+h f(xn,yn). Modified Euler improves the slope estimate by prediction and correction.",
"Runge–Kutta methods combine slopes at selected points; the classical fourth-order RK method uses four slope estimates in a weighted average.",
"Milne’s predictor-corrector method predicts a new value from previous values and corrects it using a newly estimated derivative."
])]),
("2. Object Oriented Programming with Java", [
("Unit I — OOP overview, data types and control structures", [
"OOP represents a program as objects that combine state (data) and behaviour (methods). Benefits include modularity, reuse, maintainability and clearer modelling.",
"Four central ideas: encapsulation bundles data and methods; abstraction exposes essentials; inheritance derives new classes from existing ones; polymorphism allows one interface to represent different behaviours.",
"C++ data types include built-in, user-defined and derived types. Constants preserve fixed values; variables store values; reference variables provide aliases.",
"Operators perform arithmetic, comparison, logical, assignment and other operations. Control structures include if/else, nested if, while, do-while, for, break, continue, switch and goto."
]),
("Unit II — Object classes and inheritance with C++", [
"A class defines data members and member functions; an object is an instance. Inline and nested member functions define behaviour inside or through class scope.",
"Arrays may be class members; structures and classes group related data. Objects can be passed as function arguments.",
"new allocates dynamic memory and delete releases it. Static data members and static member functions belong to the class rather than individual objects.",
"Constructors initialize objects: null/default, parameterized and copy constructors are common forms. A destructor performs cleanup when an object lifetime ends.",
"Inheritance may be single, multiple, multilevel, hierarchical or hybrid. Function overriding changes inherited behaviour. Access specifiers are public, private and protected; derived-class constructors initialize base-class parts."
]),
("Unit III — Introduction to Java", [
"Java source code is compiled to bytecode and executed by the Java Virtual Machine (JVM), supporting platform independence. The JDK provides development tools; the JRE provides runtime components.",
"Java primitive types are byte, short, int, long, float, double, char and boolean. Arrays store indexed values of a common type.",
"Type casting converts one type to another. Widening conversions are generally automatic; narrowing conversions may require an explicit cast.",
"Operators include arithmetic, relational, logical, assignment, unary, conditional and bitwise operators. Control structures include if/else, switch, loops, break and continue.",
"Lexical elements include identifiers, keywords, literals, operators, separators and comments."
]),
("Unit IV — Classes with Java", [
"A class defines fields, constructors and methods; an object is created with new. A constructor has the class name and no return type.",
"Method overloading uses the same method name with different parameter lists. Recursion occurs when a method calls itself and must have a terminating condition.",
"The static keyword associates a member with the class. Access control uses private, package/default, protected and public.",
"Inner classes are declared within another class. Inheritance uses extends; abstract classes may contain abstract and concrete methods."
]),
("Unit V — Packages, interfaces and Java application features", [
"A package groups related classes and interfaces. import makes types available by their simple names; access protection controls visibility.",
"An interface specifies a contract that implementing classes must fulfil. A class may implement multiple interfaces.",
"Exception handling uses try and catch; finally is commonly used for cleanup. throw raises an exception; throws declares exceptions a method may pass to its caller.",
"Multithreading allows concurrent execution paths. Thread creation, lifecycle, synchronization and inter-thread communication are used to coordinate work and protect shared data.",
"File handling uses input/output streams and reader/writer classes. Remote Method Invocation (RMI) supports invoking methods on remote Java objects."
])]),
("3. Database Management Systems", [
("Unit I — Database concepts and ER model", [
"A DBMS stores, organizes and retrieves related data while supporting controlled sharing, security, integrity, concurrency and recovery.",
"Database architecture separates external views, the conceptual logical structure and internal physical storage. Data independence reduces the effect of changes at one level on another.",
"Database languages include DDL (definition), DML (manipulation), DCL (control) and TCL (transactions). A DBA manages authorization, backup, recovery and performance.",
"ER modelling uses entities, attributes and relationships. Keys identify entities; cardinality and participation describe relationship constraints."
]),
("Unit II — Relational model and SQL", [
"A relation is a table, tuple a row, attribute a column and domain the permitted value set. A superkey uniquely identifies a row; a candidate key is minimal; a primary key is the selected candidate key; a foreign key references another relation.",
"Relational algebra includes selection, projection, union, difference, Cartesian product and join.",
"SQL commands: CREATE defines objects; INSERT adds rows; SELECT retrieves; UPDATE changes; DELETE removes rows; ALTER changes structure; DROP removes an object.",
"WHERE filters rows before grouping; GROUP BY creates groups; HAVING filters groups after aggregation; ORDER BY sorts the result.",
"Constraints include NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY and CHECK. Aggregate functions include COUNT, SUM, AVG, MIN and MAX."
]),
("Unit III — SQL advanced features and database programming", [
"Joins combine related rows. Equi-join uses equality; self-join relates rows in the same table. A subquery is nested within another query.",
"UNION combines compatible result sets and removes duplicates; INTERSECT returns common rows; MINUS (or EXCEPT in some systems) returns rows unique to the first result.",
"Views present stored queries as virtual tables. Indexes can improve retrieval speed but require storage and maintenance.",
"GRANT assigns privileges and REVOKE removes them. Triggers execute automatically when specified database events occur.",
"Embedded SQL is placed within a host language; dynamic SQL is constructed and executed at runtime."
]),
("Unit IV — Normalization", [
"A functional dependency X→Y means X determines Y. Normalization organizes relations to reduce redundancy and update anomalies.",
"1NF requires atomic values and no repeating groups. 2NF requires 1NF and no partial dependency of a non-prime attribute on a candidate key.",
"3NF requires 2NF and no transitive dependency of non-prime attributes on candidate keys. BCNF requires every determinant to be a superkey.",
"4NF addresses non-trivial multivalued dependencies; 5NF addresses join dependencies. Lossless decomposition avoids spurious tuples; dependency preservation retains constraints."
]),
("Unit V — Transactions and concurrency control", [
"A transaction is a logical unit of work. ACID means Atomicity, Consistency, Isolation and Durability.",
"COMMIT makes changes permanent; ROLLBACK undoes uncommitted work; SAVEPOINT marks a point for partial rollback.",
"Concurrency control coordinates simultaneous transactions. Locks restrict conflicting access; two-phase locking has growing and shrinking phases.",
"Deadlock is a cycle of transactions waiting for one another. Systems may prevent, avoid, detect or recover from deadlocks.",
"Serializability checks whether a concurrent schedule is equivalent to a serial order. Recovery uses logs, checkpoints and backups to restore consistency."
])]),
("4. Probability and Statistics (AI-ML)", [
("Unit I — Probability fundamentals and discrete distributions", [
"Probability lies between 0 and 1. For equally likely outcomes, P(A)=favourable outcomes/total outcomes. Complement: P(Aᶜ)=1−P(A).",
"Addition rule: P(A∪B)=P(A)+P(B)−P(A∩B). Conditional probability: P(A|B)=P(A∩B)/P(B). Independent events satisfy P(A∩B)=P(A)P(B).",
"Bayes’ theorem updates a prior probability using observed evidence. A random variable maps outcomes to numerical values; a distribution describes their probabilities.",
"Binomial distribution models the number of successes in n independent trials with success probability p: P(X=x)=C(n,x)pˣ(1−p)ⁿ⁻ˣ; mean=np and variance=np(1−p).",
"Multinomial distribution generalizes binomial trials to more than two outcome categories. Geometric distribution counts trials until the first success: P(X=k)=(1−p)ᵏ⁻¹p."
]),
("Unit II — Continuous distributions and joint random variables", [
"Normal distribution is symmetric and bell-shaped; standardization uses Z=(X−μ)/σ.",
"Beta distribution is continuous on [0,1]. Gamma and exponential distributions model positive continuous values and waiting times.",
"A joint distribution describes two variables together. Marginal distributions are obtained by summing or integrating over the other variable; conditional distributions describe one variable given another.",
"Expectation E[X] is the long-run average; variance Var(X)=E[X²]−(E[X])². Covariance describes joint variation; correlation standardizes it between −1 and +1."
]),
("Unit III — Transformations, sums and convergence", [
"For Y=g(X), determine the support and transform the distribution. For a one-to-one differentiable transformation, fY(y)=fX(x)|dx/dy|.",
"For independent random variables, the distribution of a sum can be found using convolution; means and variances add under independence.",
"Convergence in probability means large deviations become unlikely. Convergence in distribution means the cumulative distribution functions converge at continuity points.",
"Chebyshev’s inequality: P(|X−μ|≥kσ)≤1/k². The Law of Large Numbers states that sample averages approach the population mean under suitable conditions."
]),
("Unit IV — Descriptive statistics, sampling and estimation", [
"Mean, median and mode describe central tendency. Range, variance and standard deviation describe dispersion; frequency tables organize observations.",
"Sampling selects observations from a population. Standard error measures the sampling variability of a statistic.",
"The Central Limit Theorem states that, under common conditions, the standardized sample mean approaches a normal distribution as sample size increases.",
"A point estimate gives one parameter value; an interval estimate gives a range with a confidence level. Maximum likelihood selects parameters that maximize the likelihood of observed data."
]),
("Unit V — Hypothesis testing, correlation and regression", [
"Null hypothesis H0 is tested against alternative H1. Type I error rejects a true H0; Type II error fails to reject a false H0.",
"Significance level α is the tolerated Type I error probability. A p-value measures how unusual the observed result (or more extreme result) would be if H0 were true.",
"Choose a test appropriate to sample size, assumptions and known/unknown population variance. Student’s t distribution is commonly used for small samples when population variance is unknown under its assumptions.",
"Correlation measures association, not causation. Rank correlation uses ranks. Scatter plots help identify direction, form and outliers.",
"Simple linear regression models Y=a+bX. Least squares chooses a and b to minimize the sum of squared residuals."
])]),
("5. Frontend Design with React", [
("Unit I — Introduction to frontend development and React fundamentals", [
"Frontend development creates the user-facing interface. Client-server architecture separates the client interface from server-side services; APIs allow them to exchange data.",
"React is a JavaScript library for building component-based user interfaces. Node.js runs JavaScript outside the browser; npm manages packages; Vite supports project setup and builds.",
"JSX is HTML-like syntax used in JavaScript. Functional components are reusable UI units; props pass data from parent to child.",
"ES6 features include let, const, arrow functions, template literals, destructuring and modules. Event handling responds to user actions; conditional rendering displays UI according to conditions."
]),
("Unit II — React components, state, hooks and routing", [
"useState stores component state and returns a value and setter. Updating state triggers a re-render.",
"Forms can be controlled by React state. Lists should use stable keys. Component communication passes data through props and events through callback functions.",
"useEffect handles side effects such as subscriptions or data fetching; cleanup can remove subscriptions. useRef stores a mutable reference without causing a re-render.",
"React Router maps URL paths to components. Navigation, route parameters, nested routes and error pages support application routing. Context API shares values across a component tree."
]),
("Unit III — API integration, responsive design and deployment", [
"Fetch API and Axios send HTTP requests. REST APIs commonly expose CRUD operations: Create, Read, Update and Delete.",
"Handle loading, success and error states. Validate forms before submission; Local Storage can retain small browser-side values between sessions.",
"Responsive design adapts layouts to screen sizes. Bootstrap and Tailwind CSS provide styling tools for responsive interfaces.",
"Performance basics include avoiding unnecessary re-renders, optimizing assets and using efficient lists. Git tracks changes and GitHub supports collaboration.",
"The build process creates production assets. Deployment platforms such as Netlify and Vercel can host frontend applications. Mini-project development applies the complete workflow."
])])
]

story = [
    Spacer(1, 24*mm),
    Paragraph("ITM UNIVERSITY, RAIPUR", styles["CoverX"]),
    Paragraph("B.Tech CSE — Semester III", styles["CoverX"]),
    Paragraph("COMPLETE SUBJECT NOTES", styles["H1X"]),
    Paragraph("Syllabus-aligned revision handbook • Batch 2025–2029", styles["BodyX"]),
    Spacer(1, 10*mm),
    Paragraph("<b>Subjects:</b> Numerical Methods • OOP with Java • DBMS • Probability & Statistics (AI-ML) • Frontend Design with React", styles["BodyX"]),
    Paragraph("<b>Faculty correction:</b> Numerical Methods — Mr. Rajesh Ubale.", styles["BodyX"]),
    Paragraph("Prepared as a student study aid from the Semester III syllabus supplied for this project. Follow faculty instructions and official university notices where they differ.", styles["SmallX"]),
    PageBreak()
]
for subject, units in data:
    story.append(Paragraph(subject, styles["H1X"]))
    for unit, points in units:
        story.append(Paragraph(unit, styles["H2X"]))
        items = [ListItem(Paragraph(p, styles["BodyX"]), bulletColor=colors.HexColor("#8A6818")) for p in points]
        story.append(ListFlowable(items, bulletType="bullet", leftIndent=14, bulletFontSize=6, spaceAfter=4))
    story.append(PageBreak())

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.grey)
    canvas.drawString(16*mm, 9*mm, "ITM University Raipur • B.Tech CSE Semester III")
    canvas.drawRightString(A4[0]-16*mm, 9*mm, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=16*mm, leftMargin=16*mm, topMargin=15*mm, bottomMargin=16*mm)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Built", OUT)
