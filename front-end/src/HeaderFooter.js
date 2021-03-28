import React from "react";
import './Global.css';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Creators} from './Creators';
import Navbar from 'react-bootstrap/Navbar';




function NavBar() {
  return (
    <header className="Nav-bar">
      {/* <img src={logo} className="App-logo" alt="logo" /> */}
      <p>
        Sundial
        </p>
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/poses">Poses</Link>
              </li>
              <li>
                <Link to="/users">My Account</Link>
              </li>
            </ul>
          </nav>

          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
          <Switch>
            <Route path="/poses">
              <About />
            </Route>
            <Route path="/users">
              <Users />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </div>
      </Router>
    </header>
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
  return <h2>Home</h2>;
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


