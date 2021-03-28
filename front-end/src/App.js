import "./App.css";
import { NavBar, Footer } from "./HeaderFooter";
import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
    <div className="App">
      <NavBar />
      <Footer />
    </div>
    </Router>
  );
}

export default App;
