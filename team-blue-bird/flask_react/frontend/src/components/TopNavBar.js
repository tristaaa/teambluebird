import React, {Component} from 'react';
import logo from '../assets/logo.svg'
import '../styles/TopNavBar.css'
import LoginOutlined from "@ant-design/icons/lib/icons/LoginOutlined";
import LogoutOutlined from "@ant-design/icons/lib/icons/LogoutOutlined"
import {Switch, Route, Redirect, Link} from 'react-router-dom';

class TopNavBar extends Component{
    constructor() {
        super();
        this.handleJump = this.handleJump.bind(this);
    }
    handleJump(){
        console.log("button Clicked");
        return <Link to='/login'/>;
    }
    render() {
        return(
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <h1 className="App-title">Blue Bird</h1>
                <a onClick={this.handleJump} className="logout" >
                    <LogoutOutlined/>
                    {' '}Hello, Ding
                </a>

            </header>
        )
    }
}
export default TopNavBar;