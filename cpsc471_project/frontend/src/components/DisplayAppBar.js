import React, { useState, useEffect } from "react";
import Grid from "@material-ui/core/Grid";
import AppBar from "@material-ui/core/AppBar";
import Typography from "@material-ui/core/Typography";


export default function DisplayAppBar(props) {

    return (
        <AppBar position="static" color="transparent" variant="outlined">
            <Grid container justifyContent="center" alignItems="center" spacing={8}>
                <Grid item>
                    <img src="/static/images/dinos-logo.jpg" alt="Dinos Logo" width="100" height="100" />
                </Grid>
                <Grid item>
                    <Typography variant="h3">
                        University of Calgary Dinos Swimming
                    </Typography>                    
                </Grid>
                <Grid item>
                    <img src="/static/images/canada-west-logo.jpg" alt="Canada West Logo" width="100" height="100" />
                </Grid>
            </Grid>
        </AppBar>
    );
};
