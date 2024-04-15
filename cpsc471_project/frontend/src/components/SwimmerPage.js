import React, { useState, useEffect } from "react";
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from "@material-ui/core/Grid";
import PropTypes from 'prop-types';
import Typography from "@material-ui/core/Typography";
import Table from "@material-ui/core/Table";
import { TableBody, TableCell, TableHead, TableRow, Button, Box,
    Dialog, DialogContent, TextField,
    DialogTitle, DialogActions } from "@material-ui/core";
import { Autocomplete } from '@material-ui/lab';


import DisplayAppBar from "./DisplayAppBar.js";
import UserInformation from "./UserInformation.js";



function AddEventRecordPopup(props) {
    const {open, onClose, setEventRecordData} = props;
    const [competitionData, setCompetitionData ] = useState([]);
    const [swimmer, setSwimmer ] = useState([]);


    useEffect(() => {
        axios.get('http://localhost:8000/database/competitionNames/')
            .then(response => {
                
                setCompetitionData(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
        
        axios.get('http://localhost:8000/database/swimmers/')
            .then(response => {
                setSwimmer(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
        },

        []);

        
    const handleClose = () => {
        axios.post('http://localhost:8000/database/event_record/', {
            entry_time: document.getElementById('entry_time').value,
            final_time_seconds: document.getElementById('final_time_seconds').value,
            distance: document.getElementById('distance').value,
            stroke: document.getElementById('stroke').value,
            course: document.getElementById('course').value,
            competition: document.getElementById('competition-select').value,
            swimmer: document.getElementById('swimmer-select').value,
        })
        .then(response => {
            axios.get('http://localhost:8000/database/event_record/')  
                .then(response => {
                    setEventRecordData(response.data);
                })
                .catch((error) => {
                    console.log(error);
                });
            })
            .catch((error) => {
                console.log(error);
            });            
        onClose();
    };

    return (
        <Dialog onClose={handleClose} open={open}>
            <DialogTitle>Add Event Record</DialogTitle>
            <DialogContent >
                <Grid container spacing={2}>
                    <Grid item>
                        <TextField required id="entry_time" type='time' label="Entry Time" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="final_time_seconds" type='number' label="Final Time (Seconds)" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="distance" type='number' label="Distance" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="stroke" label="Stroke" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="course" label="Course" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <Autocomplete
                            required
                            id="swimmer-select"
                            options={swimmer}
                            getOptionLabel={(option) => option.email}
                            style={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="Swimmers" variant="outlined" />}
                        />
                    </Grid>
                    <Grid item>
                        <Autocomplete
                            required
                            id="competition-select"
                            options={competitionData}
                            getOptionLabel={(option) => option.name}
                            style={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="Competitions" variant="outlined" />}
                        />
                    </Grid>
                </Grid>
            </DialogContent>
            <DialogActions>
                <Button variant="outlined" onClick={handleClose} >
                    Add Event Record
                </Button>
            </DialogActions>
        </Dialog>
    
    )
}

AddEventRecordPopup.propTypes = {
    onClose: PropTypes.func.isRequired,
    open: PropTypes.bool.isRequired,
};

export default function SwimmerPage(props) {
    const [eventRecordData, setEventRecordData] = useState([]);
    const [competitionData, setCompetitionData] = useState([]);
    const [AddEventRecordPopupOpen, setAddEventPopupOpen] = useState(false);

    const handleAddEventClickOpen = () => {
        setAddEventPopupOpen(true);
    };

    const handleAddEventClickClose = () => {
        setAddEventPopupOpen(false);
    };

    useEffect(() => {
        // Assuming you pass the coach's ID as props

        axios.get(`http://localhost:8000/database/event_record/`)
            .then(response => {
                setEventRecordData(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

        axios.get(`http://localhost:8000/database/competitions/`)
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
                        <UserInformation name="Stephen" role="Swimmer" />
                    </Paper>
                </Grid>
                <Grid item xs={6}>
                    <Paper variant="outlined">
                        <Typography variant='h6'>Event Record</Typography>
                        <Table size="small">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Time</TableCell>
                                    <TableCell>Distance</TableCell>
                                    <TableCell>Stroke</TableCell>
                                    <TableCell>Course</TableCell>
                                    <TableCell>Competition</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {eventRecordData.map((event_record) => (
                                    <TableRow key={event_record.id}>
                                        <TableCell>{event_record.final_time_seconds}</TableCell>
                                        <TableCell>{event_record.distance}</TableCell>
                                        <TableCell>{event_record.stroke}</TableCell>
                                        <TableCell>{event_record.course}</TableCell>
                                        <TableCell>{event_record.competition}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                        <Box display="flex" justifyContent="flex-end">
                            <Button variant="outlined" onClick={handleAddEventClickOpen}>Add Event</Button>
                            <AddEventRecordPopup open={AddEventRecordPopupOpen} onClose={handleAddEventClickClose} setEventRecordData={setEventRecordData} />
                        </Box>
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