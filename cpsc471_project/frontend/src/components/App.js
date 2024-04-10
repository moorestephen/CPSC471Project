import React, { useState, useEffect } from "react";
import { render } from "react-dom";

const App = () => {
    return <h1>Testing React Code</h1>
};

const AppWrapper = () => {
    return (
        <div id = "app">
            <App />
        </div>
    );
};

render(<AppWrapper />, document.getElementById('app'));