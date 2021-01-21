import React, { Component } from "react";
import JoinRoomPage from "./JoinRoomPage";
import CreateRoomPage from "./CreateRoomPage";
import { BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
        <Router>
            <Switch>
                <Route exact path='/'><p>This is the Home Page</p></Route>
                <Route path='/join' component={JoinRoomPage}></Route>
                <Route path='/create-room' component={CreateRoomPage}></Route>
            </Switch>
        </Router>)
    }
}