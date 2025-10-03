import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="app">
        <main className="app-main">
          <div className="content">
            <h2>Sistema de Telemedicina</h2>
            <div className="button-group">
              <button className="primary-button">Agendar Consulta</button>
              <button className="primary-button">Minhas Consultas</button>
            </div>
          </div>
        </main>
        <Routes>
          <Route path="/" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;