import React, { useState, useEffect } from "react";
import Grid from "@material-ui/core/Grid";
import AppBar from "@material-ui/core/AppBar";
import Grid from "@material-ui/core/Grid";
import AppBar from "@material-ui/core/AppBar";

export default function DisplayAppBar(props) {
    return (
        <AppBar position="static">
            <Grid container justifyContent="center" alignItems="center">
                <Grid item>
                    <h1>Swim Club Management System</h1>
                </Grid>
            </Grid>
        </AppBar>
    );
};
