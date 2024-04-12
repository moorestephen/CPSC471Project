import React, { useState, useEffect } from "react";
import axios from 'axios';
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import AppBar from "@material-ui/core/AppBar";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import { Link } from "react-router-dom";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

import DisplayAppBar from "./AppBar.js";

export default function AdminPage(props) {
    const [clubData, setClubData] = useState([]);

    /**
    * Hook that fetches club data from the database - currently no dependencies
    */
    useEffect(() => {
        axios.get('http://localhost:8000/database/clubs/')
            .then(response => {
                setClubData(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
        }, []);

    return (
        <DisplayAppBar />
    );
};
