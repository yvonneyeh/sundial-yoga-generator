import React, { Component } from "react";
import "./Global.css";
import "./App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Creators } from "./Creators";
import { NavItem, NavDropdownMenuItem } from "react-bootstrap/Nav";
import { Container, Row, Col, Navbar, Nav } from "react-bootstrap";
import { Poses } from "./Poses";

function NavBar() {
  return (
    <>
      <Container className="App container py-3">
        <Navbar
          variant="light"
          bg="light"
          className="navbar"
          expand="lg"
          fixed="top"
        >
          <Navbar.Brand href="/" className="font-weight-bold text-muted">
            Sundial
          </Navbar.Brand>
          <Navbar.Collapse
            id="basic-navbar-nav"
            className="justify-content-end"
          >
            <Nav className="mr-auto">
              <Nav.Link href="/home">Home</Nav.Link>
              <Nav.Link href="/poses">Poses</Nav.Link>
              <Nav.Link href="/users">My Account</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      </Container>
      {/* <img src={logo} className="App-logo" alt="logo" /> */}

      <div>
        {/* <nav>
              <ul>
                <li className="nav-item">
                  <Link to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link to="/poses">Poses</Link>
                </li>
                <li className="nav-item">
                  <Link to="/users">My Account</Link>
                </li>
              </ul>
            </nav> */}
        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/poses">
            <Poses />
          </Route>
          <Route path="/users">
            <Users />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </>
  );
}

function Footer() {
  return (
    <footer className="Footer">
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/creators">Creators</Link>
              </li>
              <li>
                <Link to="/hackor">HackOR Submission</Link>
              </li>
            </ul>
          </nav>

          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
          <Switch>
            <Route path="/creators">
              <Creators />
            </Route>
            <Route path="/hackor">
              <Hackor />
            </Route>
          </Switch>
        </div>
      </Router>
    </footer>
  );
}

function Home() {
  return (
    <>
      <Container className="w-50">
        <Row className="w-50p-5 m-5">
          <Col className="col-6">
            <h1>Welcome to Sundial</h1>
          </Col>
          <Col className="col-sm-12 col-md-4 m-2 w-50">
            <p>
              Sundial is a web app for yoga students, teachers, and enthusiasts
              that allows a user to create custom yoga sequences. Users can also
              generate random sequences of varying lengths, and save all
              sequences to their library of yoga "playlists". 🌞
            </p>
          </Col>
        </Row>
      </Container>
      <Container className="w-50">
        <Row className="w-50 p-5 m-5 d-flex">
          <Col className="col-sm-12 col-md-4 m-2">
            <h2>View Yoga Poses</h2>
            <p>Learn both English and Sanskrit names of over 70 yoga poses.</p>
          </Col>
          <Col className="col-sm-12 col-md-4 m-2">
            <h2>Generate Yoga Sequences</h2>
            <p>Create a short or long yoga sequence.</p>
          </Col>
          <Col className="col-sm-12 col-md-4 m-2">
            <h2>Save your Favorite Sequences</h2>
            <p>Practice your favorite sequences anytime, anywhere.</p>
          </Col>
        </Row>
      </Container>
    </>
  );
}

function About() {
  return <h2>About</h2>;
}

function Users() {
  return <h2>Users</h2>;
}

function Hackor() {
  return <h2>HackOr Submission</h2>;
}

export { NavBar, Footer };
