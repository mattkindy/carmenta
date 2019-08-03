import React, { Component } from 'react';
import { Grid, TextField, Button } from '@material-ui/core';
import scrapingService from '../service/ScrapingService';

export default class StartScrapingDialog extends Component {
  setUsername(username) {
    this.setState({
      username,
    })
  }

  setPassword(password) {
    this.setState({
      password,
    })
  }

  submit() {
    const { username, password } = this.state;

    if (!username) {
      console.error("You fucked up username")
      return;
    }

    if (!password) {
      console.error("You fucked up username")
      return;
    }

    // submit to our api
    scrapingService.scrape(username, password)
  }

  render() {
    return (
      <Grid direction="column">
        <TextField
          label="LinkedIn Username"
          onChange={e => this.setUsername(e.target.value)}
          // className={classes.formControl}
          variant="outlined"
        />
         <TextField
          label="Password"
          // className={classes.textField}
          type="password"
          variant="outlined"
          onChange={e => this.setPassword(e.target.value)}
        />
        <Button onClick={e => this.submit()}>
          SCRAPE!
        </Button>
      </Grid>
    )
  }
}