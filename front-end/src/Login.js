import React from "react";
import logo from "./logo.svg";
import "./Global.css";
import "./App.css";
import useSWR from "swr";

// SignUpComponent
function SignUp() {

  const [formData, setFormData] = useState({
    user: {},
    loggedIn: false,
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.target);

    fetch("/api/register-user", {
      method: "POST",
      body: data,
    }).then((response) => {
      if (response.status !== 200) {
        alert('Please try a different phone number.');
        return;
      }
      alert(
        "You created an account! Build your favorite recipes to easily view your grocery list!"
      );
      response.json().then((data) => {
        console.log(JSON.stringify(data.user));
        console.log(data.user);
        localStorage.setItem("user", JSON.stringify(data.user));
        localStorage.setItem("loggedIn", true);
        setFormData({ loggedIn: true, user: data.user });
      });
    });
  };

  return (
    <Col className="col-12 col-md-8 p-4 bg-light border-right rounded-left">
      <h2>Create your Account</h2>
      <h3>
        Ready to realign yourself?
      </h3>
      <form onSubmit={handleSubmit}>
        <table>
          <tbody>
            <tr>
            <td>
                <label htmlFor="level">Level:</label> <br />
                <select id="level" name="level">
                  <option value="beginner">Beginner</option>
                  <option value="intermediate">Intermediate</option>
                  <option value="advanced">Advanced</option>
                  <option value="instructor">Instructor</option>
                </select>
              </td>
              <td>
                <label htmlFor="first_name">First Name:</label> <br />
                <input
                  type="text"
                  name="first_name"
                  id="first_name"
                  placeholder="Jerilyn"
                  required
                  minLength="2"
                  maxLength="30"
                  autoFocus
                />
              </td>
              <td>
                <label htmlFor="last_name">Last Name:</label> <br />
                <input
                  type="text"
                  name="last_name"
                  id="last_name"
                  placeholder="Blossom"
                  minLength="2"
                  maxLength="50"
                  required
                />
              </td>
            </tr>
            <tr>
              <td>
                <label htmlFor="email">Email:</label> <br />
                <input
                  type="tel"
                  name="email"
                  id="email"
                  placeholder="yoginiblossom@gmail.com"
                  maxLength="50"
                  required
                />
              </td>
              <td>
                <label htmlFor="password">Password:</label>
                <br />
                <input
                  type="password"
                  name="password"
                  id="password"
                  placeholder="Password"
                  required
                />
              </td>
            </tr>
            <tr>
              <td>
                <Button type="submit" className="submit-button">
                  Create
                </Button>
              </td>
            </tr>
          </tbody>
        </table>
      </form>
    </Col>
  );
}


// SignInComponent
function SignIn() {

  const [formData, setFormData] = useState({
    user: {},
    loggedIn: false,
  });

  const handleSubmitSignIn = (event) => {
    event.preventDefault();
    // new keyword calls a constructor
    const data = new FormData(event.target);

    fetch("/api/login-user", {
      method: "POST",
      body: data,
    }).then((response) => {
      console.log(response);
      if (response.status !== 200) {
        alert("Login Failed. Email and/or password is incorrect.");
        return;
      }
      response.json().then((data) => {
        localStorage.setItem("user", JSON.stringify(data.user));
        localStorage.setItem("loggedIn", true);
        setFormData({ loggedIn: true, user: data.user });
        alert(`Welcome ${data.user.first_name}!`);
      });
    });
  };

  return (
    <Col className="col-12 col-md-4 p-4 bg-light rounded-right">
      <h2>Log In</h2>
      <h3>View your sequences and add new ones!</h3>
      <form onSubmit={handleSubmitSignIn}>
        <p>
          <label htmlFor="emailin">Email:</label> <br />
          <input
            type="text"
            name="emailin"
            id="emailin"
            placeholder="yogablossom@gmail.com"
            maxLength="40"
            // autoComplete="off"
          />
        </p>
        <p>
          <label htmlFor="passwordin">Password:</label> <br />
          <input
            type="password"
            name="passwordin"
            id="passwordin"
            placeholder="Your password"
          />
        </p>
        <p>
          <Button type="submit">Log In</Button>
        </p>
      </form>
    </Col>
  );
}

// Container Holding SignIn Component and SignUp Component
function SignInUpContainer() {
  return (
    <section>
      <Container className="my-4 py-4 h-75 w-75">
        <Row className="w-100 h-75 pt-5 rounded">
          <SignUp />
          <SignIn />
        </Row>
      </Container>
    </section>
  );
}

export default function Login() {
  return (
    <div id="page-container">
      <NavBar />
        <SignInUpContainer />
      <Footer />
    </div>
  );
}
}

export { Login };
