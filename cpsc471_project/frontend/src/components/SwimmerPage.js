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
    const [eventRecordData, setEventRecordData] = useState([]);
    const [competitionData, setCompetitionData] = useState([]);

    useEffect(() => {
        // Assuming you pass the coach's ID as props

        axios.get(`http://localhost:8000/database/event_record`)
            .then(response => {
                setEventRecordData(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

        axios.get(`http://localhost:8000/database/competition`)
            .then(response => {
                setCompetitionData(response.data);
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
                <Grid item xs={6}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Event Record</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={6}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Upcoming Competitions</Typography>
                        <Table size="small">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Name</TableCell>
                                    <TableCell>Sanctioned</TableCell>
                                    <TableCell>Date</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {competitionData.map((competition) => (
                                    <TableRow key={competition.name}>
                                        <TableCell>{competition.name}</TableCell>
                                        <TableCell>{competition.sanctioned ? 'Yes' : 'No'}</TableCell>
                                        <TableCell>{competition.start_date} to {competition.end_date}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </Paper>
                </Grid>
            </Grid>
        </div>
    );
}