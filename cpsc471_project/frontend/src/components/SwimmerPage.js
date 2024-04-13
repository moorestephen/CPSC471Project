import React, { useState, useEffect } from "react";
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Table from "@material-ui/core/Table";
import { TableBody, TableCell, TableHead, TableRow } from "@material-ui/core";

import DisplayAppBar from "./DisplayAppBar.js";
import UserInformation from "./UserInformation.js";

export default function SwimmerPage(props) {
    const [swimmersData, setSwimmersData] = useState([]);

    useEffect(() => {
        // Assuming you pass the coach's ID as props
        axios.get(`http://localhost:8000/database/swimmers`)
            .then(response => {
                setSwimmersData(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    return (
        <div>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <DisplayAppBar />
                </Grid>
                <Grid item xs={12}>
                    <Paper variant="outlined">
                        <UserInformation name={props.swimmerName} role="Swimmer" />
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Entries</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Event Record</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Upcoming Competitions</Typography>
                    </Paper>
                </Grid>
            </Grid>
        </div>
    );
}