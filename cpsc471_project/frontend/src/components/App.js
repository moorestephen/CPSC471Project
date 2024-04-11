import React, { useState, useEffect } from "react";
import { render } from "react-dom";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";
import HomePage from "./HomePage.js";
import LoginPage from "./LoginPage.js";
import AdminPage from "./AdminPage.js";
import CoachPage from "./CoachPage.js";
import SwimmerPage from "./SwimmerPage.js";


function App(props) {
    return (
        <div>
            <Router>
                <Routes>
                    <Route exact path="/" element={<HomePage />}/>
                    <Route path="/login" element={<LoginPage />}/>
                    <Route path="/administrator" element={<AdminPage />}/>
                    <Route path="/coach" element={<CoachPage />}/>
                    <Route path="/swimmer" element={<SwimmerPage />}/>
                </Routes>
            </Router>
        </div>
    );
};

function AppWrapper() {
    return (
        <div id = "app">
            <App />
        </div>
    );
};

render(<AppWrapper />, document.getElementById('app'));