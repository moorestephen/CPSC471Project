import React, { useState, useEffect } from "react";
import { TableBody, TableCell, TableHead, TableRow, Button, Box,
    Dialog, DialogContent, TextField,
    DialogTitle, DialogActions, Grid, makeStyles } from "@material-ui/core";
import axios from "axios";

export default function LoginPage(props) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(username, password);
        try {
            const response = await axios.post('http://localhost:8000/database/retrieve-user/', {
                    username: username,
                    password: password
                });
            console.log(response);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <Box display="flex" justifyContent="center" alignItems="center" height="100vh">
            <form onSubmit={handleSubmit}>
            <Grid container direction="column" spacing={2}>
                <Grid item>
                <TextField
                    label="Username"
                    variant="outlined"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                </Grid>
                <Grid item>
                <TextField
                    label="Password"
                    variant="outlined"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                </Grid>
                <Grid item>
                <Button variant="contained" color="primary" type="submit">
                    Login
                </Button>
                </Grid>
            </Grid>
            </form>
        </Box>
    );
};
