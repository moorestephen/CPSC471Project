import React, { useState, useEffect } from "react";
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
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
import Table from "@material-ui/core/Table";

import DisplayAppBar from "./DisplayAppBar.js";
import UserInformation from "./UserInformation.js";
import { TableBody, TableCell, TableHead, TableRow } from "@material-ui/core";

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
        <div>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <DisplayAppBar />
                </Grid>
                <Grid item xs={12}>
                    <Paper variant="outlined">
                        <UserInformation name="Admin" role="Administrator" />
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Paper variant="outlined" spacing={1}>
                        <Typography variant='h6'>Swimmers</Typography>
                        <Table size="small">
                            <TableHead>
                                <TableCell>Name</TableCell>
                                <TableCell>Email</TableCell>
                                <TableCell>Birthdate</TableCell>
                                <TableCell>Club</TableCell>
                            </TableHead>
                            <TableBody>
                                {clubData.map((club) => (
                                    <TableRow key={club.name}>
                                        <TableCell>{club.name}</TableCell>
                                        <TableCell>{club.city}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Coaches</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Competitions</Typography>
                    </Paper>
                </Grid>
            </Grid>
        </div>
    );
};
