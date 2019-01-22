import React, { Component } from 'react';
import logo from './logo.svg';
import LoginPage from './components/login_page/LoginPage';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
          <LoginPage className="col-lg-12 cardPostion" />
      </div>
    );
  }
}

export default App;
