import React, {Component} from 'react';
import { Switch, Router, Route, Redirect } from 'react-router-dom';
import FlightForm from "./FlightForm";
import '../styles/Main.css';
import AssignMap from "./AssignMap"
import {MarkerMap} from './NewMap'
import Login from "./Login";
import Output from "./Output";
import history from './History'



export default class Main extends  React.Component{

    constructor(props) {
        super(props);
        this.state = {
            "assign_table" : [],
            'top5_table':[],
            'map_table':[],
        };
        this.setAssign = this.setAssign.bind(this);
        this.setTop = this.setTop.bind(this);
        this.setMap = this.setMap.bind(this);
    }

    setAssign= ( data ) =>{
        this.setState({"assign_table" : data})
    }
    setTop= ( data ) => {
        this.setState({"top5_table" : data})
    }
    setMap = ( data )=>{
        this.setState({"map_table" : data})
    }


    render() {
        return (
                <Router
                    history={history}
                >
                    <Route
                        exact path="/"
                        // setAssign={this.setAssign}
                        // setTop={this.setTop}
                        // setMap={this.setMap}
                        render={props => <FlightForm setAssign = {this.setAssign} setTop={this.setTop} setMap={this.setMap} />}
                    />
                    <Route path="/login" component={Login} />
                    <Route path="/output"
                           render={props => <Output assign_table = {this.state.assign_table} top5_table={this.state.top5_table} />}
                    />
                    <Route path="/map"
                           render={props => <AssignMap
                               assign_table = {this.state.assign_table}
                               map_table={this.state.map_table}/> }
                    />
                </Router>
        );
    }
}
// export function Main(props) {
//     // const getLogin = () => {
//     //     return props.isLoggedIn ? <Redirect to="/" /> : <Login handleLogin={props.handleLogin} />;
//     // }
//
//
// }