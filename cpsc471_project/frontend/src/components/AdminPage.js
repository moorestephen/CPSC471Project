import React, { useState, useEffect } from "react";
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Table from "@material-ui/core/Table";
import PropTypes from 'prop-types';
import DisplayAppBar from "./DisplayAppBar.js";
import UserInformation from "./UserInformation.js";
import { TableBody, TableCell, TableHead, TableRow, Button, Box,
         Dialog, DialogContent, TextField,
         DialogTitle, DialogActions} from "@material-ui/core";
import { Autocomplete } from '@material-ui/lab';

function AddSwimmerPopup(props) {
    const { open, onClose, setSwimmerData } = props;
    const [ groups, setGroups ] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/database/group-names/')
            .then(response => {
                setGroups(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
        }, []);

    const handleClose = () => {
        console.log("WHAT THE FUCK");
        axios.post('http://localhost:8000/database/swimmers/', {
            email: document.getElementById('email').value,
            dob: document.getElementById('dob').value,
            fname: document.getElementById('fname').value,
            lname: document.getElementById('lname').value,
            club: "Sockeyes"
        })
        .then(response => {
            console.log('received response from first post');
            axios.get('http://localhost:8000/database/group-names/')
                .then(response => {
                    console.log('received response from first get');
                    setGroups(response.data);
                    axios.post('http://localhost:8000/database/swimmers-group/', {
                        swimmer: document.getElementById('email').value,
                        group: document.getElementById('group-select').value
                    })
                        .then(response => {
                            console.log("successful");
                        }).catch((error) => {
                            console.log(error);
                    });
                })
                .catch((error) => {
                    console.log(error);
                })
            .catch((error) => {
                console.log(error);
            });    
        }); 

        onClose();

    };

    return (
        <Dialog onClose={handleClose} open={open}>
            <DialogTitle>Add Swimmer</DialogTitle>
            <DialogContent >
                <Grid container spacing={2}>
                    <Grid item>
                        <TextField required id="email" label="Email" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="fname" label="First Name" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="lname" label="Last Name" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <TextField required id="dob" type="date" label="Birthdate" variant="outlined" InputLabelProps={{shrink: true}}/>
                    </Grid>
                    <Grid item>
                        <Autocomplete
                            required
                            id="group-select"
                            options={groups}
                            getOptionLabel={(option) => option.name}
                            style={{ width: 300 }}
                            renderInput={(params) => <TextField {...params} label="Group" variant="outlined" />}
                        />
                    </Grid>
                </Grid>
            </DialogContent>
            <DialogActions>
                <Button variant="outlined" onClick={handleClose} >
                    Add Swimmer
                </Button>
            </DialogActions>
        </Dialog>
    )
}

AddSwimmerPopup.propTypes = {
    onClose: PropTypes.func.isRequired,
    open: PropTypes.bool.isRequired,
};


export default function AdminPage(props) {
    const [swimmerData, setSwimmerData] = useState([]);
    const [popupOpen, setPopupOpen] = useState(false);

    const handleClickOpen = () => {
        setPopupOpen(true);
    };

    const handleClose = () => {
        setPopupOpen(false);
    };

    /**
    * Hook that fetches swimmer data from the database - currently no dependencies
    */
    useEffect(() => {
        axios.get('http://localhost:8000/database/swimmers-and-group/')
            .then(response => {
                console.log(response.data);
                setSwimmerData(response.data);
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
                                <TableCell>Group</TableCell>
                            </TableHead>
                            <TableBody>
                                {swimmerData.map((swimmer) => (
                                    <TableRow key={swimmer.email}>
                                        <TableCell>{swimmer.fname} {swimmer.lname}</TableCell>
                                        <TableCell>{swimmer.email}</TableCell>
                                        <TableCell>{swimmer.dob}</TableCell>
                                        <TableCell>{swimmer.group_id}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                        <Box display="flex" justifyContent="flex-end">
                            <Button variant="outlined" onClick={handleClickOpen}>Add Swimmer</Button>
                            <AddSwimmerPopup open={popupOpen} onClose={handleClose} setSwimmerData={setSwimmerData} />
                        </Box>
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
