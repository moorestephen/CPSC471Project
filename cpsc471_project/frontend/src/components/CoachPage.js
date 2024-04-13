import React, { useState, useEffect } from "react";
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Table from "@material-ui/core/Table";
import { TableBody, TableCell, TableHead, TableRow } from "@material-ui/core";

import DisplayAppBar from "./DisplayAppBar.js";
import UserInformation from "./UserInformation.js";

export default function CoachPage(props) {
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
                        <UserInformation name={props.coachName} role="Coach" />
                    </Paper>
                </Grid>
                <Grid item xs={6}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Swimmers</Typography>
                        <Table size="small">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Name</TableCell>
                                    <TableCell>Email</TableCell>
                                    <TableCell>Birthdate</TableCell>
                                    <TableCell>Club</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {swimmersData.map((swimmer) => (
                                    <TableRow key={swimmer.id}>
                                        <TableCell>{swimmer.fname} {swimmer.lname}</TableCell>
                                        <TableCell>{swimmer.email}</TableCell>
                                        <TableCell>{swimmer.dob}</TableCell>
                                        <TableCell>{swimmer.club}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </Paper>
                </Grid>
                <Grid item xs={6}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Competitions</Typography>
                    </Paper>
                </Grid>
            </Grid>
        </div>
    );
}