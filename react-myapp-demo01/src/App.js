import React from 'react';
// import logo from './logo.svg';
import './App.css';
import Home from './components/Home'
import {Router} from 'react-router-dom'
function App() {
  return (
    <div className="App">
        {/*<Router path="/home" component={Home}/>*/}
     <Home/>
    </div>
  );
}

export default App;
